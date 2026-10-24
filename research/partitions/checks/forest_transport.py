"""P014: bounded sibling-fork transport, not a proof of e-unimodality."""
from __future__ import annotations

import argparse
from dataclasses import replace
from datetime import datetime, timezone
import hashlib
from itertools import combinations, product
import json
from pathlib import Path
import signal
import time

from . import forest_surgery as fs
from . import forest_triples as ft
from . import height_three as h3

PHASE = h3.ROOT / "research/partitions/height-three-forest-transport"
PROTOCOL = PHASE / "protocol.json"
DEVELOPMENT = ((2, 4, 4, 6, 7, 7, 7), (3, 6, 6, 6, 7, 7, 7),
               (3, 3, 4, 6, 6, 7, 8, 8), (3, 5, 5, 7, 7, 7, 8, 8))


def heldout():
    excluded = set(h3.development() + h3.HELDOUT + fs.DEVELOPMENT + fs.heldout() + DEVELOPMENT)
    result = []
    for n in (9, 10):
        eligible = (h for h in h3.tab.hessenberg_vectors(n)
                    if h not in excluded and h3.height(h) == 3
                    and all(h[i] > i + 1 for i in range(n - 1)))
        result.append(min(eligible, key=lambda h: hashlib.sha256(
            ("h3-forest-transport-v1:" + ",".join(map(str, h))).encode()).hexdigest()))
    return tuple(result)


def selector_spec(repair):
    # Existing groups: mark, word, edge; added groups: fork, optional digit.
    order = (3, 4, 2, 1, 0) if repair else (3, 2, 1, 0)
    return tuple((p, end) for p in (order, order[::-1]) for end in (0, -1))


def protocol():
    return dict(program="P014", schema_version=1, development=DEVELOPMENT,
        heldout=heldout(), limits=h3.LIMITS, target="height=3; lambda=(n-4,3,1)",
        primitives=["all three preserved P013 primitives", "sibling-fork split/join with exact scalar mark compensation"],
        selectors=selector_spec(False), order="n,h,degree,(parents,compositions,marks,epsilon)",
        repair="one maximum-insertion digit step with epsilon toggle, otherwise unchanged",
        coordinate_order="ascending nonminimum vertices within components ordered by minima; then all marks",
        heldout_rule="round two only, after development-only repair and selector lock",
        matching="complete grammar only, diagnostic; verify Hall witness if augmentation fails",
        stop="two rounds, one repair; no capped-case replacements or research reruns")


def freeze():
    data = h3.encoded(protocol())
    if PROTOCOL.exists():
        if PROTOCOL.read_text() != data:
            raise ValueError("Refusing to replace P014 protocol")
    else:
        h3.write_report(PROTOCOL, protocol())
    return dict(protocol=str(PROTOCOL.relative_to(h3.ROOT)), sha256=h3.digest(PROTOCOL),
                heldout=heldout())


def verify_protocol():
    if json.loads(PROTOCOL.read_text()) != json.loads(h3.encoded(protocol())):
        raise ValueError("P014 specification changed after freezing")


def encode_word(geo, word):
    """Tom Lemma 3.13 digits in ascending vertex order; empty blocks rejected."""
    if geo.decode(word) is None:
        raise ValueError("Expected an actual tree list")
    pos = {u: i for i, u in enumerate(word)}
    bounds, digits = [], []
    for v in sorted(word)[1:]:
        lower = [u for u in word if u < v and (u, v) in geo.edges]
        if not lower:
            raise ValueError("Empty tree block")
        bounds.append(len(lower)-1)
        digits.append(sum(pos[u] > pos[v] for u in lower))
    return tuple(bounds), tuple(digits)


def decode_word(geo, vertices, digits):
    values = sorted(vertices)
    if not values or len(set(values)) != len(values) or len(digits) != len(values)-1:
        raise ValueError("Bad insertion coordinates")
    word = [values[0]]
    for v, k in zip(values[1:], digits):
        neighbors = [u for u in word if (u, v) in geo.edges]
        if type(k) is not int or not 0 <= k < len(neighbors):
            raise ValueError("Digit outside its insertion bound")
        where = len(word) if k == 0 else word.index(neighbors[-k])
        word.insert(where, v)
    result = tuple(word)
    if geo.decode(result) is None:
        raise AssertionError("Insertion bijection produced an invalid tree list")
    return result


def chain_encode(bounds, point):
    """Explicit recursive rectangle SCD: (chain label, position, bottom, length)."""
    if len(bounds) != len(point):
        raise ValueError("Dimension mismatch")
    label = []; bottom = length = position = 0
    for b, y in zip(bounds, point):
        if type(b) is not int or type(y) is not int or b < 0 or not 0 <= y <= b:
            raise ValueError("Point outside product of chains")
        j = min(y, length-position)
        label.append(j)
        position += y-j
        bottom += j
        length += b-2*j
    return tuple(label), position, bottom, length


def chain_decode(bounds, label, position):
    if len(bounds) != len(label):
        raise ValueError("Chain label dimension mismatch")
    lengths = [0]
    for b, j in zip(bounds, label):
        if b < 0 or not 0 <= j <= min(lengths[-1], b):
            raise ValueError("Invalid chain label")
        lengths.append(lengths[-1]+b-2*j)
    if not 0 <= position <= lengths[-1]:
        raise ValueError("Position outside chain")
    point = []
    for a, b, j in reversed(tuple(zip(lengths, bounds, label))):
        if position <= a-j:
            x, y = position, j
        else:
            x, y = a-j, position-a+2*j
        point.append(y); position = x
    return tuple(reversed(point))


def block_coordinates(geo, source):
    bounds, point = [], []
    for word in geo.data(source.parents)[0]:
        b, x = encode_word(geo, word); bounds.extend(b); point.extend(x)
    bounds.extend(a[0]-1 for a in source.compositions)
    point.extend(r-1 for r in source.marks)
    return tuple(bounds), tuple(point)


def fork_operations(geo, source, budget):
    """Two removed sibling edges, one added edge; exact inverse fork join."""
    words, old_inv = geo.data(source.parents)
    payload = geo.payload(source)
    component = {u: i for i, word in enumerate(words) for u in word}
    # Split: v<u have common parent p; set parent(u)=0, parent(v)=u.
    for v, u in combinations(range(1, len(geo.h)+1), 2):
        budget.tick("candidates")
        p = source.parents[u-1]
        if not p or source.parents[v-1] != p or (v, u) not in geo.edges:
            continue
        i = component[u]; alpha = source.compositions[i]
        if len(alpha) < 2:
            continue
        parents = list(source.parents); parents[u-1] = 0; parents[v-1] = u
        parents = tuple(parents)
        split_words, new_inv = geo.data(parents)
        pieces = [w for w in split_words if set(w) <= set(words[i])]
        if len(pieces) != 2:
            raise AssertionError("Fork failed to split into two components")
        for cut in range(1, len(alpha)):
            a, b = alpha[:cut], alpha[cut:]
            for left, right in sorted({(a, b), (b, a)}):
                budget.tick("candidates")
                if (sum(left), sum(right)) != tuple(map(len, pieces)):
                    continue
                total = source.marks[i]+1+old_inv-new_inv
                for r_left in range(1, left[0]+1):
                    budget.tick("candidates")
                    r_right = total-r_left
                    if not 1 <= r_right <= right[0]:
                        continue
                    changed = dict(payload); del changed[frozenset(words[i])]
                    changed[frozenset(pieces[0])] = (left, r_left)
                    changed[frozenset(pieces[1])] = (right, r_right)
                    yield geo.build(parents, changed, source.epsilon)
    # Join: choose root u, its child v, and larger p in another component.
    for u, parent in enumerate(source.parents, 1):
        if parent:
            continue
        for v in range(1, u):
            budget.tick("candidates")
            if source.parents[v-1] != u:
                continue
            for p in range(u+1, geo.h[u-1]+1):
                budget.tick("candidates")
                i, j = component[u], component[p]
                if i == j or (v, p) not in geo.edges:
                    continue
                parents = list(source.parents); parents[u-1] = p; parents[v-1] = p
                parents = tuple(parents)
                _, new_inv = geo.data(parents)
                mark = source.marks[i]+source.marks[j]-1+old_inv-new_inv
                for alpha in sorted({source.compositions[i]+source.compositions[j],
                                     source.compositions[j]+source.compositions[i]}):
                    budget.tick("candidates")
                    if not 1 <= mark <= alpha[0]:
                        continue
                    changed = dict(payload)
                    del changed[frozenset(words[i])]; del changed[frozenset(words[j])]
                    changed[frozenset(words[i]+words[j])] = (alpha, mark)
                    yield geo.build(parents, changed, source.epsilon)


def digit_operations(geo, source, budget):
    """Sole R2 repair: change one maximum-insertion digit, toggle epsilon."""
    words, _ = geo.data(source.parents)
    payload = geo.payload(source)
    delta = 1 if source.epsilon else -1
    for word in words:
        bounds, digits = encode_word(geo, word)
        for k, (bound, value) in enumerate(zip(bounds, digits)):
            budget.tick("candidates")
            if not 0 <= value+delta <= bound:
                continue
            changed_digits = digits[:k]+(value+delta,)+digits[k+1:]
            changed_word = decode_word(geo, word, changed_digits)
            parents = list(source.parents)
            for u, p in geo.decode(changed_word):
                budget.tick()
                parents[u-1] = p
            yield geo.build(parents, payload, 1-source.epsilon)


def neighbors(geo, source, budget, repair):
    groups = list(fs.neighbors(geo, source, budget, repair=True))
    for operation in ((fork_operations, digit_operations) if repair else (fork_operations,)):
        group = set()
        for dest in operation(geo, source, budget):
            if dest and dest.sign == -source.sign and dest.degree == source.degree:
                group.add(dest)
        groups.append(tuple(sorted(group)))
    return tuple(groups)


def choose(groups, selector, repair):
    order, end = selector_spec(repair)[selector]
    return next((groups[k][end] for k in order if groups[k]), None)


def analyze(geo, states, budget, repair, selector_ids=range(4)):
    universe = set(states); graph = {}; isolated = None; edge_counts = [0]*(5 if repair else 4)
    for source in states:
        groups = neighbors(geo, source, budget, repair)
        for k, group in enumerate(groups):
            edge_counts[k] += len(group)
            for dest in group:
                if dest not in universe or dest.sign != -source.sign or dest.degree != source.degree:
                    raise AssertionError("Transport escaped complete signed space")
        graph[source] = groups
        if source.sign < 0 and not any(groups) and isolated is None:
            isolated = source
    for source, groups in graph.items():
        for k, group in enumerate(groups):
            for dest in group:
                budget.tick("candidates")
                if source not in graph[dest][k]:
                    raise AssertionError("Transport failed same-primitive inverse membership")
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
    diagnostic = (dict(status="isolated negative", state=isolated.record()) if isolated
                  else fs.hall_diagnostic(states, graph, budget))
    return dict(status="complete", states=len(states), negative=len(negative),
        primitive_directed_edges=edge_counts, primitive_inverse_checked=True,
        grammar_diagnostic=diagnostic, selectors=selectors)


def provenance():
    value = fs.provenance()
    paths = [Path(__file__), PROTOCOL, PHASE / "README.md",
             h3.ROOT / "programs/partition-h3-forest-transport.json"]
    paths.extend(p for p in (PHASE / "repair.md", PHASE / "round-two-protocol.json",
                            PHASE / "upstream.json") if p.exists())
    for path in paths:
        value["sources"][str(path.relative_to(h3.ROOT))] = h3.digest(path)
    return value


def compare(geo, census, budget, prior=None, held_out=False):
    if prior is not None:
        if prior.get("comparison", {}).get("status") != "agrees":
            raise ValueError("Saved comparison lacks completed independent check")
        expected = prior["signed_space"]["coefficient"]
        mode = "saved coefficient with recorded independent comparison"
    elif held_out:
        _, tableau = h3.enumerate_signed(geo.h, budget)
        expected = tableau["coefficient"]
        mode = "complete tableau expansion; no new coloring calculation"
    else:
        expected = h3.coloring_coefficient(geo.h, budget)
        mode = "independent coloring/subset oracle"
    if expected != census["coefficient"]:
        raise AssertionError("Complete forest coefficient disagrees with comparison")
    result = dict(status="agrees", mode=mode)
    if prior is not None:
        result["inherited_comparison"] = prior["comparison"]
    return result


def run_case(h, budget, *, repair=False, prior=None, held_out=False, selector=None):
    report = dict(h=h, split="heldout" if held_out else "development", status="incomplete")
    before = budget.receipt()
    try:
        for kind in ("extensions", "candidates"):
            if getattr(budget, kind) >= budget.limits[kind]:
                raise h3.Capped("round " + kind + " exhausted before case")
        budget.begin_case()
        remaining = min(budget.limits["case_seconds"], budget.limits["round_seconds"]-
                        (time.monotonic()-budget.start))
        signal.setitimer(signal.ITIMER_REAL, max(.001, remaining))
        geo = fs.Geometry(h)
        if h3.height(geo.h) != 3:
            raise ValueError("P014 requires height exactly three")
        states, report["signed_space"] = fs.enumerate_states(geo, budget)
        report["comparison"] = compare(geo, report["signed_space"], budget, prior, held_out)
        if len(h) == 8 and prior is None and not held_out:
            _, tableau = h3.enumerate_signed(h, budget)
            if tableau["coefficient"] != report["signed_space"]["coefficient"]:
                raise AssertionError("Boundary tableau comparison failed")
            report["boundary_tableau"] = tableau
        report["moves"] = analyze(geo, states, budget, repair,
                                   range(4) if selector is None else (selector,))
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
            raise ValueError("Round two requires round-one receipt")
        previous = json.loads(input_path.read_text())
        if previous.get("program") != "P014" or previous.get("round") != 1 or not previous.get("source_stable"):
            raise ValueError("Expected stable P014 round-one report")
        repair_spec = dict(round=2, repair=repair, input_sha256=h3.digest(input_path),
            primitive="one Tom maximum-insertion digit step and epsilon toggle" if repair else "unchanged fork grammar",
            selectors=selector_spec(repair), heldout_used_for_repair=False)
        path = PHASE / "round-two-protocol.json"
        if path.exists():
            if not ft.same_protocol_spec(json.loads(path.read_text()), json.loads(h3.encoded(repair_spec))):
                raise ValueError("Refusing to change frozen repair")
        else:
            h3.write_report(path, repair_spec)
    elif repair or input_path is not None:
        raise ValueError("Repair/input only applies to round two")
    old_path = fs.PHASE / "evidence.json"
    old = json.loads(old_path.read_text())["round_one"]["cases"]
    source = provenance(); signal.signal(signal.SIGALRM, h3._alarm)
    budget = h3.Budget()
    report = dict(program="P014", round=round_number, repair=repair, research_validated=False,
        status="finite-exact-evidence", started_utc=datetime.now(timezone.utc).isoformat(),
        provenance=source, inherited_evidence_sha256=h3.digest(old_path), cases=[])
    if round_number == 2:
        report["round_two_spec"] = repair_spec
    for h in DEVELOPMENT:
        prior = next((c for c in old if tuple(c["h"]) == h and c["status"] == "complete"), None)
        if previous is not None:
            # A completed R1 new boundary comparison can be reused, with exact mode retained.
            fresh_prior = next((c for c in previous["cases"] if tuple(c["h"]) == h
                                and c.get("comparison", {}).get("status") == "agrees"), None)
            if prior is None and fresh_prior is not None:
                prior = fresh_prior
        case = run_case(h, budget, repair=repair, prior=prior)
        report["cases"].append(case)
        print(h3.encoded(dict(h=h, status=case["status"])).strip(), flush=True)
    if round_number == 2:
        scores = [sum(next(s["unpaired"] for s in c["moves"]["selectors"] if s["id"] == i)
                      for c in report["cases"] if c["status"] == "complete") for i in range(4)]
        chosen = min(range(4), key=lambda i: (scores[i], i))
        lock = dict(selector=chosen, development_scores=scores,
            eligible=all(c["status"] == "complete" for c in report["cases"]) and scores[chosen] == 0,
            development_sha256=hashlib.sha256(h3.encoded(report["cases"]).encode()).hexdigest())
        h3.write_report(output.with_name(output.stem+"-selection-lock.json"), lock)
        report["selection_lock"] = lock
        for h in heldout():
            case = run_case(h, budget, repair=repair, held_out=True, selector=chosen)
            report["cases"].append(case)
            print(h3.encoded(dict(h=h, status=case["status"])).strip(), flush=True)
    report["resources"] = budget.receipt()
    report["source_stable"] = source["sources"] == provenance()["sources"]
    if not report["source_stable"]:
        raise ValueError("P014 sources changed during execution")
    h3.write_report(output, report)
    return dict(output=str(output), resources=report["resources"])


def state_from_record(geo, value):
    """Do not trust stored sign, degree or inversion in a Hall certificate."""
    parents = tuple(value["parents"])
    compositions = tuple(map(tuple, value["compositions"]))
    marks = tuple(value["marks"])
    if (len(parents) != len(geo.h) or any(type(p) is not int or (p and (u, p) not in geo.edges)
            for u, p in enumerate(parents, 1))):
        raise ValueError("Malformed Hall parent forest")
    words, _ = geo.data(parents)
    if len(words) != len(compositions) or len(words) != len(marks):
        raise ValueError("Malformed Hall payload")
    payload = {frozenset(w): (a, r) for w, a, r in zip(words, compositions, marks)}
    state = geo.build(parents, payload, value["epsilon"])
    if state is None or h3.encoded(state.record()) != h3.encoded(value):
        raise ValueError("Hall record is not an actual signed state")
    if (tuple(sorted((x for a in state.compositions for x in a), reverse=True)) != h3.target(len(geo.h))
            or state.degree > len(geo.edges)//2):
        raise ValueError("Hall record has wrong type or degree")
    return state


def verify_hall_certificate(geo, diagnostic, budget, repair=True):
    if diagnostic.get("status") != "Hall deficiency":
        raise ValueError("Expected an explicit Hall deficiency")
    negative = tuple(state_from_record(geo, s) for s in diagnostic["negatives"])
    advertised = {state_from_record(geo, s) for s in diagnostic["neighbors"]}
    if (len(set(negative)) != len(negative) or not negative
            or any(s.sign != -1 for s in negative) or any(s.sign != 1 for s in advertised)
            or len(negative) != diagnostic["negative_count"]
            or len(advertised) != diagnostic["neighbor_count"]):
        raise ValueError("Invalid Hall sides or cardinalities")
    actual = set(); per_state = []; inverse = {}
    for source in negative:
        budget.tick()
        groups = neighbors(geo, source, budget, repair)
        for k, group in enumerate(groups):
            for dest in group:
                budget.tick("candidates")
                if dest.sign != -source.sign or dest.degree != source.degree:
                    raise AssertionError("Hall edge has incorrect sign or degree")
                if dest not in inverse:
                    inverse[dest] = neighbors(geo, dest, budget, repair)
                if source not in inverse[dest][k]:
                    raise AssertionError("Hall edge lacks same-primitive inverse")
                actual.add(dest)
        per_state.append(dict(source=source.record(), neighbors_by_primitive=[len(g) for g in groups]))
    if actual != advertised or len(negative) <= len(actual):
        raise ValueError("Advertised Hall deficiency fails complete-neighborhood verification")
    return dict(status="verified Hall deficiency", negative_count=len(negative), neighbor_count=len(actual),
        negatives=[s.record() for s in negative], neighbors=[s.record() for s in sorted(actual)],
        per_state=per_state, repair=repair, complete_neighborhood_verified=True,
        same_primitive_inverse_verified=True,
        scope="complete frozen grammar on this finite Hall subset; not a counterexample to unimodality")


def certify(input_path, output):
    """Round two stops at the already decisive repaired-grammar certificate."""
    verify_protocol()
    prior = json.loads(input_path.read_text())
    if prior.get("program") != "P014" or prior.get("round") != 1 or not prior.get("source_stable"):
        raise ValueError("Expected stable P014 round-one report")
    choices = [(tuple(c["h"]), c) for c in prior["cases"] if c.get("status") == "complete"
               and c.get("moves", {}).get("grammar_diagnostic", {}).get("status") == "Hall deficiency"]
    if not choices:
        raise ValueError("No completed development Hall certificate")
    h, case = min(choices, key=lambda x: (len(x[0]), x[0]))
    spec = dict(round=2, mode="direct Hall certificate verification only", repair=True,
        input_sha256=h3.digest(input_path), h=h, limits=h3.LIMITS,
        primitive="one Tom maximum-insertion digit step and epsilon toggle",
        selection="first complete development Hall deficiency by n,h; saved first failed augmentation subset",
        heldout_used_for_repair=False, heldout_executed=False,
        reason="Both saved negatives have zero digits and minimal marks, so repair adds no neighbor")
    path = PHASE / "round-two-protocol.json"
    if path.exists():
        if not ft.same_protocol_spec(json.loads(path.read_text()), json.loads(h3.encoded(spec))):
            raise ValueError("Refusing to change round-two verification specification")
    else:
        h3.write_report(path, spec)
    source = provenance(); signal.signal(signal.SIGALRM, h3._alarm)
    budget = h3.Budget(); budget.begin_case()
    report = dict(program="P014", round=2, repair=True, mode=spec["mode"],
        research_validated=False, started_utc=datetime.now(timezone.utc).isoformat(),
        provenance=source, round_two_spec=spec, heldout_executed=False,
        unrun_heldout=heldout(), selector_locked=False)
    signal.setitimer(signal.ITIMER_REAL, budget.limits["case_seconds"])
    try:
        geo = fs.Geometry(h)
        if h3.height(geo.h) != 3:
            raise ValueError("Certificate is not height three")
        report["verification"] = verify_hall_certificate(geo, case["moves"]["grammar_diagnostic"], budget)
        report["status"] = "verified finite grammar obstruction"
    except (h3.Capped, MemoryError) as exc:
        report["status"] = "capped"; report["cap_reason"] = str(exc) or "allocation"
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
    report["resources"] = budget.receipt()
    report["source_stable"] = source["sources"] == provenance()["sources"]
    if not report["source_stable"]:
        raise ValueError("P014 sources changed during verification")
    h3.write_report(output, report)
    return dict(output=str(output), status=report["status"], resources=report["resources"])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("freeze")
    run = sub.add_parser("run")
    run.add_argument("--round", type=int, choices=(1, 2), required=True)
    run.add_argument("--output", type=Path, required=True)
    run.add_argument("--input", type=Path)
    run.add_argument("--repair", action="store_true")
    certificate = sub.add_parser("certify")
    certificate.add_argument("--input", type=Path, required=True)
    certificate.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.command == "freeze":
        result = freeze()
    elif args.command == "certify":
        result = certify(args.input, args.output)
    else:
        result = run_round(args.round, args.output, args.input, args.repair)
    print(h3.encoded(result), end="")


if __name__ == "__main__":
    main()
