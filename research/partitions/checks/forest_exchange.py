"""P015 bounded component-payload exchanges; no universal theorem is assumed."""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
from itertools import combinations
import json
from pathlib import Path
import signal
import time

from . import forest_surgery as fs
from . import forest_transport as tr
from . import forest_triples as ft
from . import height_three as h3

PHASE = h3.ROOT / "research/partitions/height-three-forest-exchange"
PROTOCOL = PHASE / "protocol.json"
DEVELOPMENT = tr.DEVELOPMENT
ORDER = (5, 3, 2, 1, 4, 0)
SELECTORS = tuple((order, end) for order in (ORDER, ORDER[::-1]) for end in (0, -1))


def heldout():
    excluded = set(h3.development() + h3.HELDOUT + fs.DEVELOPMENT + fs.heldout()
                   + tr.DEVELOPMENT + tr.heldout())
    result = []
    for n in (9, 10):
        eligible = (h for h in h3.tab.hessenberg_vectors(n) if h not in excluded
                    and h3.height(h) == 3
                    and all(h[i] > i+1 for i in range(n-1)))
        result.append(min(eligible, key=lambda h: hashlib.sha256(
            ("h3-forest-exchange-v1:" + ",".join(map(str, h))).encode()).hexdigest()))
    return tuple(result)


def protocol():
    return dict(program="P015", schema_version=1, development=DEVELOPMENT,
        heldout=heldout(), limits=h3.LIMITS, target="height=3; lambda=(n-4,3,1)",
        primitives=["all five final P014 groups",
                    "adjacent labels in different components: relabel parents and carry payloads; toggle epsilon"],
        filter="actual larger graph parents, opposite sign and equal full effective degree",
        selectors=SELECTORS, order="n,h,degree,(parents,compositions,marks,epsilon)",
        repair="only extend adjacent label pairs to all label pairs; all other conditions unchanged",
        heldout_rule="round two only, after complete development and zero-unpaired reciprocal selector lock",
        matching="complete frozen grammar diagnostic, never unrestricted matching or universal proof",
        stop="two formal rounds, one repair, no extra critic preflight or nested agents; no silent reruns")


def freeze():
    data = h3.encoded(protocol())
    if PROTOCOL.exists():
        if PROTOCOL.read_text() != data:
            raise ValueError("Refusing to change frozen P015 protocol")
    else:
        h3.write_report(PROTOCOL, protocol())
    return dict(protocol=str(PROTOCOL.relative_to(h3.ROOT)), sha256=h3.digest(PROTOCOL),
                heldout=heldout())


def verify_protocol():
    if json.loads(PROTOCOL.read_text()) != json.loads(h3.encoded(protocol())):
        raise ValueError("P015 implementation differs from frozen protocol")
    upstream = json.loads((PHASE / "upstream.json").read_text())
    for path, expected in upstream["protected_sha256"].items():
        if h3.digest(h3.ROOT / path) != expected:
            raise ValueError("Protected prior work changed: " + path)


def transpose(geo, source, a, b):
    """Fixed-label partial involution; carry payloads by sets, never by position."""
    n = len(geo.h)
    if not (type(a) is int and type(b) is int and 1 <= a < b <= n):
        raise ValueError("Expected distinct ordered labels")
    words, _ = geo.data(source.parents)
    if any(a in word and b in word for word in words):
        return None

    def tau(v):
        return b if v == a else a if v == b else v

    parents = [0]*n
    for u, p in enumerate(source.parents, 1):
        parents[tau(u)-1] = tau(p)
    payload = {frozenset(tau(v) for v in vertices): value
               for vertices, value in geo.payload(source).items()}
    dest = geo.build(parents, payload, 1-source.epsilon)
    return dest if dest and dest.sign == -source.sign and dest.degree == source.degree else None


def adjacent_defect(geo, source, a):
    """Exact word inversion delta when the transported component order is stable."""
    b = a+1
    if not 1 <= a < b <= len(geo.h):
        raise ValueError("Bad adjacent labels")
    words, _ = geo.data(source.parents)
    if any(a in word and b in word for word in words):
        raise ValueError("Labels must occupy different components")
    tau = lambda v: b if v == a else a if v == b else v
    moved = tuple(tuple(tau(v) for v in word) for word in words)
    if list(map(min, moved)) != sorted(map(min, moved)):
        raise ValueError("Component order changes; use full statistic")
    word = tuple(v for w in words for v in w)
    positions = {v: i for i, v in enumerate(word)}
    lo, hi = sorted((positions[a], positions[b]))
    between = word[lo+1:hi]
    defect = sum((k < a and geo.h[k-1] == a)
                 or (k > b and geo.h[a-1] < k <= geo.h[b-1]) for k in between)
    direction = 1 if positions[a] < positions[b] else -1
    return direction * (int((a, b) in geo.edges)-defect), defect


def exchange_operations(geo, source, budget, wide=False):
    n = len(geo.h)
    pairs = combinations(range(1, n+1), 2) if wide else ((a, a+1) for a in range(1, n))
    for a, b in pairs:
        budget.tick("candidates")
        dest = transpose(geo, source, a, b)
        if dest is not None:
            yield dest


def neighbors(geo, source, budget, wide=False):
    groups = tr.neighbors(geo, source, budget, repair=True)
    return groups + (tuple(sorted(set(exchange_operations(geo, source, budget, wide)))),)


def choose(groups, selector):
    order, end = SELECTORS[selector]
    return next((groups[k][end] for k in order if groups[k]), None)


def hall_diagnostic(states, graph, budget):
    """Grammar-constrained augmentation, with diagnostic traversals charged."""
    matched_right = {}; matched_left = {}
    for root in (s for s in states if s.sign < 0):
        queue = [root]; left_seen = {root}; right_from = {}; end = None
        for source in queue:
            budget.tick()
            adjacent = set()
            for group in graph[source]:
                for dest in group:
                    budget.tick("candidates"); adjacent.add(dest)
            for dest in sorted(adjacent):
                budget.tick("candidates")
                if dest in right_from:
                    continue
                right_from[dest] = source
                if dest not in matched_right:
                    end = dest; break
                left = matched_right[dest]
                if left not in left_seen:
                    left_seen.add(left); queue.append(left)
            if end is not None:
                break
        if end is None:
            actual = set()
            for source in left_seen:
                for group in graph[source]:
                    for dest in group:
                        budget.tick("candidates"); actual.add(dest)
            if actual != set(right_from) or len(left_seen) <= len(actual):
                raise AssertionError("Hall subset does not have advertised neighbors")
            return dict(status="Hall deficiency", negative_count=len(left_seen), neighbor_count=len(actual),
                negatives=[s.record() for s in sorted(left_seen)],
                neighbors=[s.record() for s in sorted(actual)],
                scope="complete direct-neighbor grammar; first failed augmentation, not global minimality")
        while end is not None:
            budget.tick()
            source = right_from[end]; previous = matched_left.get(source)
            matched_left[source] = end; matched_right[end] = source; end = previous
    return dict(status="grammar saturates negatives", matched=len(matched_left),
                scope="finite grammar diagnostic; not an explanatory selector or universal theorem")


def verify_failure(geo, diagnostic, budget, wide=False):
    """Reconstruct actual signed objects and regenerate the complete neighbor union."""
    if diagnostic["status"] == "isolated negative":
        records = [diagnostic["state"]]; advertised_records = []
    elif diagnostic["status"] == "Hall deficiency":
        records = diagnostic["negatives"]; advertised_records = diagnostic["neighbors"]
    else:
        raise ValueError("Expected an isolated negative or Hall certificate")
    sources = tuple(tr.state_from_record(geo, x) for x in records)
    advertised = {tr.state_from_record(geo, x) for x in advertised_records}
    if (not sources or len(set(sources)) != len(sources) or any(s.sign != -1 for s in sources)
            or any(s.sign != 1 for s in advertised) or len(advertised) != len(advertised_records)):
        raise ValueError("Malformed certificate sides")
    if diagnostic["status"] == "Hall deficiency" and (
            len(sources) != diagnostic["negative_count"] or len(advertised) != diagnostic["neighbor_count"]):
        raise ValueError("Malformed certificate cardinalities")
    actual = set(); details = []; inverse = {}
    for source in sources:
        budget.tick()
        groups = neighbors(geo, source, budget, wide)
        details.append(dict(source=source.record(), neighbors_by_primitive=[len(g) for g in groups]))
        for k, group in enumerate(groups):
            for dest in group:
                budget.tick("candidates")
                if dest not in inverse:
                    inverse[dest] = neighbors(geo, dest, budget, wide)
                if source not in inverse[dest][k]:
                    raise AssertionError("Certificate edge lacks same-primitive inverse")
                actual.add(dest)
    if actual != advertised or len(sources) <= len(actual):
        raise ValueError("Complete-neighborhood deficiency failed")
    return dict(status="verified finite grammar obstruction", negative_count=len(sources),
        neighbor_count=len(actual), complete_neighborhood_verified=True,
        same_primitive_inverse_verified=True, per_state=details)


def analyze(geo, states, budget, wide=False, selector_ids=range(4)):
    universe = set(states); graph = {}; edge_counts = [0]*6; isolated = None
    for source in states:
        groups = neighbors(geo, source, budget, wide)
        for k, group in enumerate(groups):
            edge_counts[k] += len(group)
            for dest in group:
                if dest not in universe or dest.sign != -source.sign or dest.degree != source.degree:
                    raise AssertionError("Move escaped complete signed space")
        graph[source] = groups
        if source.sign < 0 and not any(groups) and isolated is None:
            isolated = source
    for source, groups in graph.items():
        for k, group in enumerate(groups):
            for dest in group:
                budget.tick("candidates")
                if source not in graph[dest][k]:
                    raise AssertionError("Same-primitive inverse recovery failed")
    negative = [s for s in states if s.sign < 0]; selectors = []
    for selector in selector_ids:
        paired = collisions = 0; seen = {}; failure = collision = None
        for source in negative:
            budget.tick()
            dest = choose(graph[source], selector)
            back = choose(graph[dest], selector) if dest else None
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
    diagnostic = (dict(status="isolated negative", state=isolated.record()) if isolated else
                  hall_diagnostic(states, graph, budget))
    result = dict(status="complete", states=len(states), negative=len(negative),
        primitive_directed_edges=edge_counts, primitive_inverse_checked=True,
        grammar_diagnostic=diagnostic, selectors=selectors)
    if diagnostic["status"] != "grammar saturates negatives":
        result["certificate_verification"] = verify_failure(geo, diagnostic, budget, wide)
    return result


def selection_decision(cases):
    complete = all(c.get("status") == "complete" for c in cases) and bool(cases)
    scores = [sum(next(s["unpaired"] for s in c["moves"]["selectors"] if s["id"] == i)
                  for c in cases if c.get("status") == "complete") for i in range(4)]
    candidate = min(range(4), key=lambda i: (scores[i], i)) if complete else None
    return dict(all_development_complete=complete, development_scores=scores,
        candidate_selector=candidate, eligible=complete and scores[candidate] == 0,
        development_sha256=hashlib.sha256(h3.encoded(cases).encode()).hexdigest())


def prior_hall_transport(geo, budget):
    prior = json.loads((tr.PHASE / "evidence.json").read_text())["round_two"]["verification"]
    records = []; targets = set()
    for value in prior["negatives"]:
        budget.tick("candidates")
        source = tr.state_from_record(geo, value); dest = transpose(geo, source, 2, 3)
        if dest is None or transpose(geo, dest, 2, 3) != source:
            raise AssertionError("Motivating exchange or exact inverse failed")
        targets.add(dest); records.append(dict(source=source.record(), target=dest.record()))
    if len(targets) != len(records):
        raise AssertionError("Payload transport collapsed composition order")
    return dict(status="old two-state subset repaired", transposition=(2, 3),
        distinct_positive_targets=len(targets), pairs=records,
        scope="only the retained subset, not full grammar coverage")


def provenance():
    value = tr.provenance()
    paths = [Path(__file__), h3.ROOT / "tests/test_forest_exchange.py", PROTOCOL,
        PHASE / "README.md", PHASE / "upstream.json", tr.PHASE / "evidence.json",
        h3.ROOT / "programs/partition-h3-forest-exchange.json",
        h3.ROOT / "research/partitions/failed-attempts.md"]
    paths.extend(p for p in (PHASE / "repair.md", PHASE / "round-two-protocol.json",
                             PHASE / "review-r1.md", PHASE / "degree-zero.md") if p.exists())
    for path in paths:
        value["sources"][str(path.relative_to(h3.ROOT))] = h3.digest(path)
    return value


def snapshot_sources(source, output):
    directory = output.parent / (output.stem+"-source")
    if directory.exists():
        raise ValueError("Refusing to overwrite a source snapshot")
    total = sum(p.stat().st_size for p in output.parent.rglob("*") if p.is_file())
    total += sum((h3.ROOT / p).stat().st_size for p in source["sources"])
    if total > h3.LIMITS["artifact_bytes"]:
        raise h3.Capped("source snapshots exceed output-directory artifact budget")
    for path, expected in source["sources"].items():
        original = h3.ROOT / path
        if h3.digest(original) != expected:
            raise ValueError("Source changed before snapshot: " + path)
        target = directory / path; target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(original.read_bytes())


def run_case(h, budget, *, wide=False, prior=None, held_out=False, selector=None):
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
            raise ValueError("P015 requires height exactly three")
        states, report["signed_space"] = fs.enumerate_states(geo, budget)
        report["comparison"] = tr.compare(geo, report["signed_space"], budget, prior, held_out)
        if tuple(h) == DEVELOPMENT[-1]:
            report["prior_hall_transport"] = prior_hall_transport(geo, budget)
        report["moves"] = analyze(geo, states, budget, wide,
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


def run_round(round_number, output, input_path=None):
    if output.exists():
        raise ValueError("Refusing to overwrite a run artifact before execution")
    verify_protocol(); wide = False; spec = None
    if round_number == 2:
        if input_path is None:
            raise ValueError("Round two requires the frozen round-one receipt")
        previous = json.loads(input_path.read_text())
        if (previous.get("program") != "P015" or previous.get("round") != 1
                or previous.get("source_stable") is not True):
            raise ValueError("Expected stable P015 round one")
        wide = not selection_decision(previous["cases"])["eligible"]
        spec = dict(program="P015", round=2, input_sha256=h3.digest(input_path), repair=wide,
            primitive="all label pairs" if wide else "adjacent pairs unchanged",
            selectors=SELECTORS, limits=h3.LIMITS, heldout_used_for_repair=False,
            heldout_rule="only after complete zero-unpaired development selector lock")
        path = PHASE / "round-two-protocol.json"
        if path.exists():
            if not ft.same_protocol_spec(json.loads(path.read_text()), json.loads(h3.encoded(spec))):
                raise ValueError("Refusing to change frozen round-two repair")
        else:
            h3.write_report(path, spec)
        if not (PHASE / "repair.md").is_file() or not (PHASE / "review-r1.md").is_file():
            raise ValueError("Record first review and repair decision before second execution")
    elif round_number != 1 or input_path is not None:
        raise ValueError("Expected round one without input, or round two with input")
    old_path = tr.PHASE / "evidence.json"
    old = json.loads(old_path.read_text())["round_one"]["cases"]
    held_out_vectors = tuple(map(tuple, json.loads(PROTOCOL.read_text())["heldout"]))
    source = provenance(); snapshot_sources(source, output)
    signal.signal(signal.SIGALRM, h3._alarm); budget = h3.Budget()
    report = dict(program="P015", round=round_number, repair=wide, research_validated=False,
        status="finite-exact-evidence", started_utc=datetime.now(timezone.utc).isoformat(),
        provenance=source, inherited_evidence_sha256=h3.digest(old_path), cases=[],
        heldout_executed=False, selector_locked=False, unrun_heldout=held_out_vectors)
    if spec is not None:
        report["round_two_spec"] = spec
    for h in DEVELOPMENT:
        prior = next((c for c in old if tuple(c["h"]) == h and c["status"] == "complete"), None)
        if prior is None:
            raise ValueError("Frozen development case lacks inherited completed coloring comparison")
        report["cases"].append(run_case(h, budget, wide=wide, prior=prior))
        print(h3.encoded(dict(h=h, status=report["cases"][-1]["status"])).strip(), flush=True)
    decision = selection_decision(report["cases"])
    report["development_decision"] = decision
    if round_number == 2:
        lock = decision | dict(selector_locked=decision["eligible"],
                               selector=decision["candidate_selector"] if decision["eligible"] else None)
        h3.write_report(output.with_name(output.stem+"-selection-decision.json"), lock)
        report["selection_decision"] = lock
        if lock["selector_locked"]:
            report["selector_locked"] = True
            for h in held_out_vectors:
                report["heldout_executed"] = True
                report["cases"].append(run_case(h, budget, wide=wide, held_out=True, selector=lock["selector"]))
                print(h3.encoded(dict(h=h, status=report["cases"][-1]["status"])).strip(), flush=True)
            report["unrun_heldout"] = []
    report["resources"] = budget.receipt()
    report["source_stable"] = source["sources"] == provenance()["sources"]
    verify_protocol()
    if not report["source_stable"]:
        raise ValueError("P015 sources changed during research execution")
    h3.write_report(output, report)
    return dict(output=str(output), resources=report["resources"], selector_locked=report["selector_locked"])


def continuation_spec(input_path):
    return dict(program="P015", round=2, input_sha256=h3.digest(input_path), repair=True,
        mode="direct all-pairs selector certificates and ordered-partword capacity census",
        primitive="all label pairs; unchanged payload, validity, sign and full-degree filters",
        selector_certificates="first completed development vector by n,h; first failure for each of four selectors, all degree zero",
        partword_diagnostic="complete original four development lower-half signed spaces, grouped by flattened ordered composition parts",
        independent_verification="in each deficient case choose least (D,A); recompute its sector polynomial by component sets and insertion factors",
        diagnostic_adaptation="declared after R1, before R2; not an originally preregistered outcome or new move",
        heldout_executed=False, selector_locked=False, limits=h3.LIMITS)


def verify_selector_certificates(geo, cases, budget):
    result = []
    for item in cases:
        selector = item["id"]; failure = item["first_failure"]
        records = [failure[k] for k in ("source", "target", "reverse")]
        actual = []
        for record in records:
            budget.tick()
            actual.append(tr.state_from_record(geo, record))
        source, expected_target, expected_reverse = actual
        if any(s.degree != 0 for s in actual) or source.sign != -1 or expected_target.sign != 1:
            raise ValueError("Expected actual degree-zero nonreciprocal selection")
        groups = neighbors(geo, source, budget, wide=True)
        target = choose(groups, selector)
        if target is None or target.record() != expected_target.record():
            raise AssertionError("All-pairs selector changed the advertised target")
        back_groups = neighbors(geo, target, budget, wide=True)
        reverse = choose(back_groups, selector)
        if (reverse is None or reverse.record() != expected_reverse.record() or reverse == source
                or groups[5] or back_groups[5]):
            raise AssertionError("Degree-zero selector obstruction was not recovered")
        for k, group in enumerate(groups):
            if target in group:
                budget.tick("candidates")
                if source not in back_groups[k]:
                    raise AssertionError("Relation inverse failed despite selector nonreciprocity")
        result.append(dict(selector=selector, source=source.record(), target=target.record(),
            selected_reverse=reverse.record(), source_neighbors=[len(g) for g in groups],
            target_neighbors=[len(g) for g in back_groups], nonreciprocal=True,
            all_pairs_exchange_empty=True, relation_inverse_verified=True))
    if sorted(x["selector"] for x in result) != list(range(4)):
        raise ValueError("Four distinct selector certificates required")
    return dict(status="all four selectors refuted under the all-pairs repair", cases=result,
        scope="complete neighborhoods for these saved failures, not a full repaired-grammar census")


def partword_census(states, edges, budget):
    size = edges//2+1; counts = {}; first_negative = {}
    for state in states:
        budget.tick()
        word = tuple(x for alpha in state.compositions for x in alpha)
        if word not in counts:
            counts[word] = {1: [0]*size, -1: [0]*size}
        counts[word][state.sign][state.degree] += 1
        if state.sign < 0:
            key = (word, state.degree)
            if key not in first_negative or state < first_negative[key]:
                first_negative[key] = state
    sectors = []; deficits = []
    for word, signs in sorted(counts.items()):
        signed = [p-n for p, n in zip(signs[1], signs[-1])]
        sectors.append(dict(partword=word, positive=signs[1], negative=signs[-1], signed=signed))
        for degree, value in enumerate(signed):
            if value < 0:
                deficits.append(dict(partword=word, degree=degree, signed=value,
                    positive=signs[1][degree], negative=signs[-1][degree],
                    example_negative=first_negative[word, degree].record()))
    deficits.sort(key=lambda d: (d["degree"], d["partword"]))
    return dict(sectors=sectors, deficits=deficits,
        minimum_deficit=deficits[0] if deficits else None,
        scope="necessary capacity for a cancellation that preserves the full partword, not for the larger grammar")


def component_sets(n, maximum, budget):
    """Restricted-growth generation of each set partition, ordered by minima."""
    blocks = []

    def visit(v):
        if v > n:
            yield tuple(map(tuple, blocks)); return
        for block in blocks:
            budget.tick(); block.append(v)
            yield from visit(v+1)
            block.pop()
        if len(blocks) < maximum:
            budget.tick(); blocks.append([v])
            yield from visit(v+1)
            blocks.pop()

    yield from visit(1)


def partword_block_polynomial(geo, partword, budget):
    """Independent component-set product formula, with no tree enumeration."""
    partword = tuple(partword)
    if not partword or min(partword) <= 0 or sum(partword) != len(geo.h):
        raise ValueError("Expected a composition of the vertex count")
    terms = Counter(); partitions = assignments = 0
    for blocks in component_sets(len(geo.h), len(partword), budget):
        partitions += 1; m = len(blocks)
        factors = []; valid = True
        component = {v: i for i, block in enumerate(blocks) for v in block}
        for block in blocks:
            for v in block[1:]:
                budget.tick("candidates")
                b = sum((u, v) in geo.edges for u in block if u < v)
                if b == 0:
                    valid = False; break
                if b > 1:
                    factors.append(b)
            if not valid:
                break
        if not valid:
            continue
        shift = sum(component[u] > component[v] for u, v in geo.edges)
        for cuts in combinations(range(1, len(partword)), m-1):
            budget.tick("candidates")
            ends = (0,)+cuts+(len(partword),)
            alphas = tuple(partword[a:b] for a, b in zip(ends, ends[1:]))
            if tuple(map(sum, alphas)) != tuple(map(len, blocks)):
                continue
            assignments += 1
            bounds = tuple(sorted(factors+[alpha[0] for alpha in alphas if alpha[0] > 1]))
            terms[((-1)**(len(partword)-m), shift, bounds)] += 1
    total = Counter()
    for (sign, shift, factors), multiplicity in sorted(terms.items()):
        polynomial = [1]
        for b in factors:
            product = [0]*(len(polynomial)+b-1)
            for d, coefficient in enumerate(polynomial):
                for j in range(b):
                    budget.tick("candidates"); product[d+j] += coefficient
            polynomial = product
        for d, coefficient in enumerate(polynomial):
            budget.tick("candidates"); total[d+shift] += sign*multiplicity*coefficient
    values = [total[d] for d in range(max(total, default=-1)+1)]
    coefficient = h3.oracle._trim(values)
    differences = [(coefficient[d] if d < len(coefficient) else 0)-
                   (coefficient[d-1] if 0 < d <= len(coefficient) else 0)
                   for d in range(len(geo.edges)//2+1)]
    return dict(partword=partword, coefficient=coefficient, first_differences=differences,
        set_partitions=partitions, compatible_assignments=assignments,
        product_terms=[dict(sign=sign, shift=shift, factors=factors, multiplicity=count)
                       for (sign, shift, factors), count in sorted(terms.items())],
        method="component-set products q^cross times tree insertion q-integers and first-part mark q-integers; not a coloring oracle")


def capacity_case(h, budget, prior):
    report = dict(h=h, split="development", status="incomplete")
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
        states, report["signed_space"] = fs.enumerate_states(geo, budget)
        report["comparison"] = tr.compare(geo, report["signed_space"], budget, prior)
        census = report["partword_capacity"] = partword_census(states, len(geo.edges), budget)
        total = [sum(s["signed"][d] for s in census["sectors"])
                 for d in range(len(geo.edges)//2+1)]
        if total != report["signed_space"]["first_differences"]:
            raise AssertionError("Partword partition lost a signed state")
        if census["minimum_deficit"] is not None:
            word = census["minimum_deficit"]["partword"]
            check = partword_block_polynomial(geo, word, budget)
            expected = next(s["signed"] for s in census["sectors"] if s["partword"] == word)
            if check["first_differences"] != expected:
                raise AssertionError("Independent component-set polynomial disagrees")
            report["independent_sector_check"] = check | dict(status="agrees")
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


def continue_phase(input_path, output):
    if output.exists():
        raise ValueError("Refusing to overwrite a run artifact before execution")
    verify_protocol(); prior = json.loads(input_path.read_text())
    if prior.get("program") != "P015" or prior.get("round") != 1 or prior.get("source_stable") is not True:
        raise ValueError("Expected a stable P015 round-one receipt")
    spec = continuation_spec(input_path); path = PHASE / "round-two-protocol.json"
    if not path.is_file() or not ft.same_protocol_spec(json.loads(path.read_text()),
                                                      json.loads(h3.encoded(spec))):
        raise ValueError("Freeze the continuation specification before execution")
    for name in ("repair.md", "review-r1.md", "degree-zero.md"):
        if not (PHASE / name).is_file():
            raise ValueError("Missing recorded revision: " + name)
    first = min((c for c in prior["cases"] if c["status"] == "complete"),
                key=lambda c: (len(c["h"]), c["h"]))
    source = provenance(); snapshot_sources(source, output)
    held_out_vectors = json.loads(PROTOCOL.read_text())["heldout"]
    signal.signal(signal.SIGALRM, h3._alarm); budget = h3.Budget()
    report = dict(program="P015", round=2, repair=True, mode=spec["mode"],
        status="finite-exact-evidence", research_validated=False,
        started_utc=datetime.now(timezone.utc).isoformat(), provenance=source,
        round_two_spec=spec, heldout_executed=False, selector_locked=False,
        unrun_heldout=held_out_vectors, cases=[])
    budget.begin_case(); signal.setitimer(signal.ITIMER_REAL, budget.limits["case_seconds"])
    try:
        report["selector_verification"] = dict(h=first["h"], **verify_selector_certificates(
            fs.Geometry(first["h"]), first["moves"]["selectors"], budget))
    except (h3.Capped, MemoryError) as exc:
        report["selector_verification"] = dict(status="capped", reason=str(exc) or "allocation")
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
    for h in DEVELOPMENT:
        saved = next(c for c in prior["cases"] if tuple(c["h"]) == h and c["comparison"]["status"] == "agrees")
        report["cases"].append(capacity_case(h, budget, saved))
        print(h3.encoded(dict(h=h, status=report["cases"][-1]["status"])).strip(), flush=True)
    report["resources"] = budget.receipt()
    report["source_stable"] = source["sources"] == provenance()["sources"]
    verify_protocol()
    if not report["source_stable"]:
        raise ValueError("P015 sources changed during second execution")
    h3.write_report(output, report)
    return dict(output=str(output), resources=report["resources"], heldout_executed=False)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("freeze")
    run = sub.add_parser("run")
    run.add_argument("--round", type=int, choices=(1, 2), required=True)
    run.add_argument("--output", type=Path, required=True)
    run.add_argument("--input", type=Path)
    continuation = sub.add_parser("continue")
    continuation.add_argument("--input", type=Path, required=True)
    continuation.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.command == "freeze":
        result = freeze()
    elif args.command == "continue":
        result = continue_phase(args.input, args.output)
    else:
        result = run_round(args.round, args.output, args.input)
    print(h3.encoded(result), end="")


if __name__ == "__main__":
    main()
