"""P013 bounded forest surgery. Local reversibility does not prove unimodality."""
from __future__ import annotations

import argparse
from collections import Counter, deque
from dataclasses import asdict, dataclass, field, replace
from datetime import datetime, timezone
from itertools import combinations, product
import hashlib
import json
from pathlib import Path
import signal
import time

from . import forest_triples as ft
from . import height_three as h3

PHASE = h3.ROOT / "research/partitions/height-three-forest-surgery"
PROTOCOL = PHASE / "protocol.json"
DEVELOPMENT = ((2, 4, 4, 6, 7, 7, 7), (3, 6, 6, 6, 7, 7, 7),
               (3, 3, 3, 6, 6, 6, 8, 8), (3, 5, 5, 7, 7, 7, 8, 8))


def heldout():
    excluded = set(h3.development() + h3.HELDOUT + DEVELOPMENT)
    result = []
    for n in (9, 10):
        eligible = (h for h in h3.tab.hessenberg_vectors(n)
                    if h not in excluded and all(h[i] > i + 1 for i in range(n - 1))
                    and h3.height(h) == 3)
        result.extend(sorted(eligible, key=lambda h: hashlib.sha256(
            ("h3-forest-surgery-v1:" + ",".join(map(str, h))).encode()).hexdigest())[:2])
    return tuple(result)


def protocol():
    return dict(program="P013", schema_version=1, development=DEVELOPMENT,
                heldout=heldout(), limits=h3.LIMITS, target="height=3; lambda=(n-4,3,1)",
                primitives=["one mark step and epsilon toggle",
                            "checked last-part canonical-word break and exact inverse join"],
                selectors="priority (mark,word) or (word,mark), each first/last lex target; reciprocal only",
                order="n,h,degree,(parents,compositions,marks,epsilon)",
                holdout_rule="run only in round two, after development-only repair and selector lock",
                repair_limit="one recorded repair; no third proposal/review round",
                matching="grammar-only augmenting paths, only if no isolated negative; diagnostic not proof")


def freeze():
    data = h3.encoded(protocol())
    if PROTOCOL.exists():
        if PROTOCOL.read_text() != data:
            raise ValueError("Refusing to replace a different P013 protocol")
    else:
        h3.write_report(PROTOCOL, protocol())
    return dict(protocol=str(PROTOCOL.relative_to(h3.ROOT)), sha256=h3.digest(PROTOCOL))


def verify_protocol():
    if json.loads(PROTOCOL.read_text()) != json.loads(h3.encoded(protocol())):
        raise ValueError("P013 protocol differs from implemented specification")


@dataclass(frozen=True, order=True)
class State:
    parents: tuple
    compositions: tuple
    marks: tuple
    epsilon: int
    inversion: int = field(compare=False)

    @property
    def sign(self):
        return (-1) ** (sum(map(len, self.compositions)) - len(self.marks) + self.epsilon)

    @property
    def degree(self):
        return self.inversion + sum(r - 1 for r in self.marks) + self.epsilon

    def record(self):
        return asdict(self) | dict(sign=self.sign, degree=self.degree)


def startmin(word):
    """Tom's value-rank swaps; returns normalized word and rank of old first."""
    values = sorted(word)
    rank = values.index(word[0]) + 1
    result = tuple(word)
    for i in range(rank - 2, -1, -1):
        a, b = values[i:i + 2]
        result = tuple(b if x == a else a if x == b else x for x in result)
    return result, rank


def startr(word, rank):
    values = sorted(word)
    if not 1 <= rank <= len(word) or word[0] != values[0]:
        raise ValueError("Invalid normalized word/mark")
    result = tuple(word)
    for i in range(rank - 1):
        a, b = values[i:i + 2]
        result = tuple(b if x == a else a if x == b else x for x in result)
    return result


class Geometry:
    def __init__(self, h):
        self.h = h3.oracle._hessenberg(h)
        self.edges = set(h3.tab.graph_edges(self.h))
        self.cache = {}
        self.decode_cache = {}

    def data(self, parents):
        if parents not in self.cache:
            words = ft.tree_words(parents)
            word = tuple(x for w in words for x in w)
            pos = {u: i for i, u in enumerate(word)}
            inv = sum(pos[v] < pos[u] for u, v in self.edges)
            self.cache[parents] = (words, inv)
        return self.cache[parents]

    def decode(self, word):
        """Reconstruct a proposed canonical word, then check actual round trip."""
        if word in self.decode_cache:
            return self.decode_cache[word]
        if not word or len(set(word)) != len(word) or word[0] != min(word):
            return None
        parents = {}
        maxima = []
        for i, u in enumerate(word):
            if not maxima or u > maxima[-1]:
                maxima.append(u)
            else:
                parents[u] = next(v for v in reversed(word[:i]) if v > u)
        parents.update(zip(maxima, maxima[1:] + [0]))
        valid = all(p == 0 or (u, p) in self.edges for u, p in parents.items())
        if valid:
            full = tuple(parents.get(u, 0) for u in range(1, len(self.h) + 1))
            valid = word in self.data(full)[0]
        value = tuple(sorted(parents.items())) if valid else None
        self.decode_cache[word] = value
        return value

    def build(self, parents, payload, epsilon):
        parents = tuple(parents)
        if epsilon not in (0, 1) or len(parents) != len(self.h):
            return None
        if any(p and (u, p) not in self.edges for u, p in enumerate(parents, 1)):
            return None
        words, inv = self.data(parents)
        if set(payload) != {frozenset(w) for w in words}:
            return None
        comps, marks = [], []
        for w in words:
            alpha, r = payload[frozenset(w)]
            if not alpha or min(alpha) <= 0 or sum(alpha) != len(w) or not 1 <= r <= alpha[0]:
                return None
            comps.append(tuple(alpha)); marks.append(r)
        return State(parents, tuple(comps), tuple(marks), epsilon, inv)

    def payload(self, state):
        return {frozenset(w): (a, r) for w, a, r in
                zip(self.data(state.parents)[0], state.compositions, state.marks)}


def enumerate_states(geo, budget):
    """Full signed coefficient before retaining doubled lower-half states."""
    lam = h3.target(len(geo.h)); M = len(geo.edges)
    poly = [0] * (M + 1); differences = [0] * (M // 2 + 1)
    states = []; census = Counter(); blocks = forests = triples = 0
    for parents in ft.forests(geo.h, len(lam), budget):
        forests += 1
        words, inv = geo.data(parents)
        for comps in ft.composition_assignments(tuple(map(len, words)), lam, budget):
            blocks += 1
            for marks in product(*(range(1, a[0] + 1) for a in comps)):
                budget.tick(); triples += 1
                base = State(parents, comps, marks, 0, inv)
                if base.degree >= len(poly):
                    # The signed polynomial may cancel above M; retain those terms.
                    poly.extend([0] * (base.degree + 1 - len(poly)))
                poly[base.degree] += base.sign
                census[(len(words), base.sign)] += 1
                for epsilon in (0, 1):
                    state = replace(base, epsilon=epsilon)
                    if state.degree <= M // 2:
                        states.append(state); differences[state.degree] += state.sign
    if any(poly[M + 1:]):
        raise AssertionError("Forest coefficient has nonzero terms beyond coloring degree")
    poly = poly[:M + 1]
    expected = [poly[d] - (poly[d - 1] if d else 0) for d in range(M // 2 + 1)]
    if differences != expected or poly != poly[::-1] or len(set(states)) != len(states):
        raise AssertionError("Complete state identity, uniqueness or palindromicity failed")
    return tuple(sorted(states, key=lambda s: (s.degree, s))), dict(
        edges=M, coefficient=poly, first_differences=expected,
        nonnegative_lower_differences=all(x >= 0 for x in expected),
        forests_scanned=forests, composition_blocks=blocks, forest_triples=triples,
        census=[dict(trees=m, sign=s, triples=c) for (m, s), c in sorted(census.items())])


def word_operations(geo, source, budget):
    words, _ = geo.data(source.parents)
    payload = geo.payload(source)
    # Break the final composition part.
    for i, (word, alpha) in enumerate(zip(words, source.compositions)):
        budget.tick("candidates")
        if len(alpha) < 2:
            continue
        head, tail = word[:-alpha[-1]], word[-alpha[-1]:]
        normalized, rank = startmin(tail)
        left, right = geo.decode(head), geo.decode(normalized)
        if left is None or right is None:
            continue
        parents = list(source.parents)
        for u, p in left + right:
            parents[u - 1] = p
        changed = dict(payload); del changed[frozenset(word)]
        changed[frozenset(head)] = (alpha[:-1], source.marks[i])
        changed[frozenset(tail)] = ((alpha[-1],), rank)
        yield geo.build(parents, changed, source.epsilon)
    # Exact word inverse, including nonconsecutive components; global weight is checked below.
    for i, j in combinations(range(len(words)), 2):
        budget.tick("candidates")
        if len(source.compositions[j]) != 1:
            continue
        word = words[i] + startr(words[j], source.marks[j])
        decoded = geo.decode(word)
        if decoded is None:
            continue
        parents = list(source.parents)
        for u, p in decoded:
            parents[u - 1] = p
        changed = dict(payload)
        del changed[frozenset(words[i])]; del changed[frozenset(words[j])]
        changed[frozenset(word)] = (source.compositions[i] + source.compositions[j], source.marks[i])
        yield geo.build(parents, changed, source.epsilon)


def edge_operations(geo, source, budget):
    """The one R2 repair: one edge, composition cuts, exact scalar marks."""
    words, old_inv = geo.data(source.parents)
    payload = geo.payload(source)
    component = {u: i for i, word in enumerate(words) for u in word}
    for u, parent in enumerate(source.parents, 1):
        if not parent:
            continue
        budget.tick("candidates")
        i = component[u]; alpha = source.compositions[i]
        if len(alpha) < 2:
            continue
        parents = list(source.parents); parents[u-1] = 0
        parents = tuple(parents)
        split_words, new_inv = geo.data(parents)
        pieces = [w for w in split_words if set(w) <= set(words[i])]
        if len(pieces) != 2:
            raise AssertionError("Cut did not produce exactly two components")
        left_set, right_set = map(frozenset, pieces)
        for cut in range(1, len(alpha)):
            a, b = alpha[:cut], alpha[cut:]
            for left, right in sorted({(a, b), (b, a)}):
                budget.tick("candidates")
                if (sum(left), sum(right)) != tuple(map(len, pieces)):
                    continue
                total = source.marks[i] + 1 + old_inv - new_inv
                for r_left in range(1, left[0]+1):
                    budget.tick("candidates")
                    r_right = total-r_left
                    if not 1 <= r_right <= right[0]:
                        continue
                    changed = dict(payload); del changed[frozenset(words[i])]
                    changed[left_set] = (left, r_left); changed[right_set] = (right, r_right)
                    yield geo.build(parents, changed, source.epsilon)
    for u, parent in enumerate(source.parents, 1):
        if parent:
            continue
        for v in range(u+1, geo.h[u-1]+1):
            budget.tick("candidates")
            i, j = component[u], component[v]
            if i == j:
                continue
            parents = list(source.parents); parents[u-1] = v; parents = tuple(parents)
            _, new_inv = geo.data(parents)
            mark = source.marks[i] + source.marks[j] - 1 + old_inv-new_inv
            a, b = source.compositions[i], source.compositions[j]
            for alpha in sorted({a+b, b+a}):
                budget.tick("candidates")
                if not 1 <= mark <= alpha[0]:
                    continue
                changed = dict(payload)
                del changed[frozenset(words[i])]; del changed[frozenset(words[j])]
                changed[frozenset(words[i]+words[j])] = (alpha, mark)
                yield geo.build(parents, changed, source.epsilon)


def neighbors(geo, source, budget, repair=False):
    groups = [set(), set(), set()]
    for i, r in enumerate(source.marks):
        budget.tick("candidates")
        new_r = r + (1 if source.epsilon else -1)
        if 1 <= new_r <= source.compositions[i][0]:
            marks = source.marks[:i] + (new_r,) + source.marks[i + 1:]
            groups[0].add(replace(source, marks=marks, epsilon=1 - source.epsilon))
    for dest in word_operations(geo, source, budget):
        if dest and dest.sign == -source.sign and dest.degree == source.degree:
            groups[1].add(dest)
    if repair:
        for dest in edge_operations(geo, source, budget):
            if dest and dest.sign == -source.sign and dest.degree == source.degree:
                groups[2].add(dest)
    return tuple(tuple(sorted(g)) for g in groups)


def selector_spec(repair):
    orders = ((0, 1, 2), (2, 1, 0)) if repair else ((0, 1), (1, 0))
    return tuple((order, end) for order in orders for end in (0, -1))


def choose(groups, selector, repair):
    order, end = selector_spec(repair)[selector]
    return next((groups[k][end] for k in order if groups[k]), None)


def hall_diagnostic(states, graph, budget):
    """Augment only along grammar edges; return a verifiable deficient subset."""
    matched_right = {}; matched_left = {}
    for root in (s for s in states if s.sign < 0):
        queue = deque([root]); left_seen = {root}; right_from = {}; end = None
        while queue and end is None:
            source = queue.popleft(); budget.tick()
            for dest in sorted(set(x for g in graph[source] for x in g)):
                budget.tick("candidates")
                if dest in right_from:
                    continue
                right_from[dest] = source
                if dest not in matched_right:
                    end = dest; break
                left = matched_right[dest]
                if left not in left_seen:
                    left_seen.add(left); queue.append(left)
        if end is None:
            right = set(right_from)
            actual = {v for u in left_seen for g in graph[u] for v in g}
            if actual != right or len(left_seen) <= len(right):
                raise AssertionError("Invalid Hall certificate")
            return dict(status="Hall deficiency", negative_count=len(left_seen), neighbor_count=len(right),
                        negatives=[s.record() for s in sorted(left_seen)],
                        neighbors=[s.record() for s in sorted(right)],
                        scope="complete frozen grammar only; first failed augmentation, not minimum-cardinality witness")
        while end is not None:
            source = right_from[end]
            previous = matched_left.get(source)
            matched_left[source] = end; matched_right[end] = source
            end = previous
    return dict(status="grammar saturates negatives", matched=len(matched_left),
                scope="finite diagnostic matching; no explanatory rule or theorem")


def analyze(geo, states, budget, repair=False, selector_ids=range(4)):
    universe = set(states); graph = {}; first_isolated = None
    for source in states:
        groups = neighbors(geo, source, budget, repair)
        for dest in (x for g in groups for x in g):
            if dest not in universe or dest.sign != -source.sign or dest.degree != source.degree:
                raise AssertionError("Move escaped exact signed space")
        graph[source] = groups
        if source.sign < 0 and not any(groups) and first_isolated is None:
            first_isolated = source
    for source, groups in graph.items():
        for k, group in enumerate(groups):
            for dest in group:
                budget.tick("candidates")
                if source not in graph[dest][k]:
                    raise AssertionError("Primitive failed inverse recovery")
    negative = [s for s in states if s.sign < 0]
    selectors = []
    for selector in selector_ids:
        paired = collisions = 0; seen = {}; failure = collision = None
        for source in negative:
            budget.tick()
            dest = choose(graph[source], selector, repair)
            back = choose(graph[dest], selector, repair) if dest else None
            if dest and dest in seen:
                collisions += 1
                if collision is None:
                    collision = dict(source=source.record(), other=seen[dest].record(), target=dest.record())
            elif dest:
                seen[dest] = source
            paired += back == source
            if back != source and failure is None:
                failure = dict(source=source.record(), target=dest.record() if dest else None,
                               reverse=back.record() if back else None,
                               reason="isolated" if dest is None else "nonreciprocal selection")
        selectors.append(dict(id=selector, negative=len(negative), paired=paired,
                              unpaired=len(negative)-paired, directed_collisions=collisions,
                              first_failure=failure, first_collision=collision))
    diagnostic = (dict(status="isolated negative", state=first_isolated.record()) if first_isolated
                  else hall_diagnostic(states, graph, budget))
    return dict(status="complete", states=len(states), negative=len(negative),
                mark_only_isolates=sum(not graph[s][0] for s in negative),
                primitive_inverse_checked=True, grammar_diagnostic=diagnostic, selectors=selectors)


def provenance():
    value = h3.provenance()
    paths = [Path(__file__), PROTOCOL, h3.ROOT / "programs/partition-h3-forest-surgery.json",
             PHASE / "README.md"]
    paths.extend(p for p in (PHASE / "repair.md", PHASE / "round-two-protocol.json") if p.exists())
    for path in paths:
        value["sources"][str(path.relative_to(h3.ROOT))] = h3.digest(path)
    return value


def run_case(h, budget, *, repair=False, held_out=False, selector=None, previous=None):
    report = dict(h=h, split="heldout" if held_out else "development", status="incomplete")
    before = budget.receipt()
    try:
        for kind in ("extensions", "candidates"):
            if getattr(budget, kind) >= budget.limits[kind]:
                raise h3.Capped("round " + kind + " exhausted before case")
        budget.begin_case()
        remaining = min(budget.limits["case_seconds"], budget.limits["round_seconds"] -
                        (time.monotonic() - budget.start))
        signal.setitimer(signal.ITIMER_REAL, max(.001, remaining))
        geo = Geometry(h)
        if h3.height(geo.h) != 3:
            raise ValueError("P013 requires height exactly three")
        states, report["signed_space"] = enumerate_states(geo, budget)
        report["moves"] = analyze(geo, states, budget, repair,
                                  range(4) if selector is None else (selector,))
        if previous is not None:
            expected = previous["signed_space"]["coefficient"]
            mode = "saved round-one coloring-checked coefficient"
        elif held_out:
            _, census = h3.enumerate_signed(h, budget)
            expected = census["coefficient"]; mode = "complete tableau expansion; no new coloring check"
        else:
            expected = h3.coloring_coefficient(h, budget); mode = "independent coloring/subset oracle"
        if expected != report["signed_space"]["coefficient"]:
            raise AssertionError("Forest coefficient disagrees with comparison")
        report["comparison"] = dict(status="agrees", mode=mode)
        report["status"] = "complete"
    except (h3.Capped, MemoryError) as exc:
        report["status"] = "capped"; report["cap_reason"] = str(exc) or "allocation"
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
    after = budget.receipt()
    report["resources"] = {k: after[k]-before[k] for k in
                           ("extensions", "candidates", "wall_seconds", "process_seconds")}
    report["resources"]["peak_rss_bytes"] = after["peak_rss_bytes"]
    return report


def run_round(round_number, output, input_path=None, repair=False):
    verify_protocol()
    previous = None
    if round_number == 2:
        if input_path is None:
            raise ValueError("Round two requires the preserved round-one receipt")
        previous = json.loads(input_path.read_text())
        if previous.get("program") != "P013" or previous.get("round") != 1 or not previous.get("source_stable"):
            raise ValueError("Expected stable P013 round-one report")
        repair_protocol = dict(round=2, repair=repair, input_sha256=h3.digest(input_path),
            primitive="single parent-edge cut/join; both composition concatenation orders; exact scalar mark compensation" if repair else "unchanged checked word grammar",
            selector_orders=selector_spec(repair), heldout_used_for_repair=False)
        path = PHASE / "round-two-protocol.json"
        if path.exists():
            if not ft.same_protocol_spec(json.loads(path.read_text()), json.loads(h3.encoded(repair_protocol))):
                raise ValueError("Refusing to change the frozen repair")
        else:
            h3.write_report(path, repair_protocol)
    elif repair or input_path is not None:
        raise ValueError("Repair/input only applies to round two")
    signal.signal(signal.SIGALRM, h3._alarm)
    budget = h3.Budget(); source = provenance()
    report = dict(program="P013", round=round_number, repair=repair, research_validated=False,
                  status="finite-exact-evidence", started_utc=datetime.now(timezone.utc).isoformat(),
                  provenance=source, cases=[])
    if round_number == 2:
        report["round_two_spec"] = repair_protocol
    for h in DEVELOPMENT:
        old = next((c for c in previous["cases"] if tuple(c["h"]) == h and c["status"] == "complete"), None) if previous else None
        case = run_case(h, budget, repair=repair, previous=old)
        report["cases"].append(case)
        print(h3.encoded(dict(h=h, status=case["status"])).strip(), flush=True)
    if round_number == 2:
        scores = [sum(next(s["unpaired"] for s in c["moves"]["selectors"] if s["id"] == i)
                      for c in report["cases"] if c["status"] == "complete") for i in range(4)]
        chosen = min(range(4), key=lambda i: (scores[i], i))
        lock = dict(selector=chosen, development_scores=scores,
                    eligible=all(c["status"] == "complete" for c in report["cases"]) and scores[chosen] == 0,
                    development_sha256=hashlib.sha256(h3.encoded(report["cases"]).encode()).hexdigest())
        h3.write_report(output.with_name(output.stem + "-selection-lock.json"), lock)
        report["selection_lock"] = lock
        for h in heldout():
            case = run_case(h, budget, repair=repair, held_out=True, selector=chosen)
            report["cases"].append(case)
            print(h3.encoded(dict(h=h, status=case["status"])).strip(), flush=True)
    report["resources"] = budget.receipt()
    report["source_stable"] = source["sources"] == provenance()["sources"]
    if not report["source_stable"]:
        raise ValueError("P013 sources changed during enumeration")
    h3.write_report(output, report)
    return dict(output=str(output), resources=report["resources"])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("freeze")
    run = sub.add_parser("run")
    run.add_argument("--round", type=int, choices=(1, 2), required=True)
    run.add_argument("--output", type=Path, required=True)
    run.add_argument("--input", type=Path)
    run.add_argument("--repair", action="store_true")
    args = parser.parse_args()
    result = freeze() if args.command == "freeze" else run_round(args.round, args.output, args.input, args.repair)
    print(h3.encoded(result), end="")


if __name__ == "__main__":
    main()
