"""Complete Tom forest triples; P012 round-two comparison, not a new involution.

Primary definitions: arXiv:2311.08020v2, Definitions 3.1/3.3, Theorem 3.4.
Every vertex chooses either no parent or one larger adjacent parent. Increasing
parent labels exclude cycles; the resulting components are exactly decreasing
trees. Distinct parent vectors encode distinct forests, even with equal words.
"""
from __future__ import annotations

from collections import Counter
from itertools import combinations, permutations, product
import json
from pathlib import Path
import signal
import time

from . import height_three as h3


def forests(h, max_components, budget):
    """All decreasing forests with at most max_components trees, without repeats."""
    parents = []
    def visit(i, roots):
        if i > len(h):
            yield tuple(parents)
            return
        for parent in (0,) + tuple(range(i + 1, h[i - 1] + 1)):
            budget.tick()
            new_roots = roots + (parent == 0)
            if new_roots > max_components:
                continue
            parents.append(parent)
            yield from visit(i + 1, new_roots)
            parents.pop()
    yield from visit(1, 0)


def tree_words(parents):
    """Components ordered by minima; canonical frontier-minimum word per tree."""
    adjacency = {u: set() for u in range(1, len(parents) + 1)}
    for u, parent in enumerate(parents, 1):
        if parent:
            adjacency[u].add(parent)
            adjacency[parent].add(u)
    remaining = set(adjacency)
    words = []
    while remaining:
        start = min(remaining)
        word = [start]
        frontier = set(adjacency[start])
        remaining.remove(start)
        while frontier:
            u = min(frontier)
            frontier.remove(u)
            if u not in remaining:
                continue
            word.append(u)
            remaining.remove(u)
            frontier.update(adjacency[u] & remaining)
        words.append(tuple(word))
    return tuple(words)


def composition_assignments(sizes, lam, budget):
    """Every composition tuple of sorted total type lam and given component sizes."""
    m = len(sizes)
    for ordered in sorted(set(permutations(lam))):
        for cuts in combinations(range(1, len(lam)), m - 1):
            budget.tick()
            boundaries = (0,) + cuts + (len(lam),)
            compositions = tuple(ordered[a:b] for a, b in zip(boundaries, boundaries[1:]))
            if tuple(map(sum, compositions)) == sizes:
                yield compositions


def coefficient(h, lam, budget, *, diagnostics=False):
    h = h3.oracle._hessenberg(h)
    lam = tuple(lam)
    if tuple(sorted(lam, reverse=True)) != lam or not lam or min(lam) <= 0 or sum(lam) != len(h):
        raise ValueError("Expected a nonempty partition of the vertex count")
    edges = h3.tab.graph_edges(h)
    M = len(edges)
    polynomial = Counter()
    census = Counter()
    centers = Counter()
    difference = Counter()
    signs = {1: Counter(), -1: Counter()}
    first_isolated = None
    isolated_count = neighbor_count = 0
    forest_count = block_count = triple_count = 0
    for parents in forests(h, len(lam), budget):
        forest_count += 1
        words = tree_words(parents)
        word = tuple(u for w in words for u in w)
        positions = {u: i for i, u in enumerate(word)}
        inv = sum(positions[v] < positions[u] for u, v in edges)
        sign = (-1) ** (len(lam) - len(words))
        for compositions in composition_assignments(tuple(map(len, words)), lam, budget):
            block_count += 1
            maxima = tuple(alpha[0] for alpha in compositions)
            centers[(sign, 2 * inv + sum(x - 1 for x in maxima))] += 1
            for marks in product(*(range(1, x + 1) for x in maxima)):
                budget.tick()
                triple_count += 1
                weight = inv + sum(r - 1 for r in marks)
                polynomial[weight] += sign
                census[(len(words), sign)] += 1
                for epsilon in (0, 1):
                    d = weight + epsilon
                    if d > M // 2:
                        continue
                    total_sign = sign * (-1) ** epsilon
                    signs[total_sign][d] += 1
                    difference[d] += total_sign
                    if not diagnostics or total_sign > 0:
                        continue
                    # Diagnostic grammar only: retain the forest/compositions,
                    # change one mark by one and toggle epsilon. No selection
                    # or collision-free matching is asserted.
                    neighbors = 0
                    for r, maximum in zip(marks, maxima):
                        budget.tick("candidates")
                        neighbors += int(r < maximum if epsilon else r > 1)
                    neighbor_count += neighbors > 0
                    if not neighbors:
                        isolated_count += 1
                        value = (d, parents, compositions, marks, epsilon)
                        if first_isolated is None or value < first_isolated[0]:
                            first_isolated = (value, dict(parents=parents, words=words,
                                compositions=compositions, marks=marks, epsilon=epsilon,
                                word_inversions=inv, weight=weight, degree=d, sign=total_sign))
    largest = max(M, max(polynomial, default=0))
    poly = [polynomial[d] for d in range(largest + 1)]
    if any(poly[M + 1:]):
        raise AssertionError("nonzero forest coefficient beyond coloring degree")
    poly = poly[:M + 1]
    diffs = [poly[d] - (poly[d - 1] if d else 0) for d in range(M // 2 + 1)]
    if diffs != [difference[d] for d in range(M // 2 + 1)]:
        raise AssertionError("forest doubling failed")
    return dict(status="complete", h=h, target=lam, coefficient=poly, first_differences=diffs,
                forests_scanned=forest_count, composition_blocks=block_count, forest_triples=triple_count,
                census=[dict(trees=m, sign=s, triples=c) for (m, s), c in sorted(census.items())],
                block_centers=[dict(sign=s, twice_center=d, blocks=c) for (s, d), c in sorted(centers.items())],
                lower_positive=[signs[1][d] for d in range(M // 2 + 1)],
                lower_negative=[signs[-1][d] for d in range(M // 2 + 1)],
                rank_step_diagnostic=dict(enabled=diagnostics, negatives_with_neighbor=neighbor_count,
                    isolated_negatives=isolated_count,
                    first_isolated=first_isolated[1] if first_isolated else None,
                    interpretation="r-step grammar only; no join/split moves or matching theorem"))


def obstruction_case(report):
    choices = []
    for case in report["cases"]:
        state = case.get("moves", {}).get("isolated_negative")
        if case["split"] == "development" and case["status"] == "complete" and state:
            key = (len(case["h"]), tuple(case["h"]), state["degree"],
                   tuple(state["shape"]), tuple(state["sigma"]),
                   tuple(map(tuple, state["rows"])), state["epsilon"])
            choices.append((key, case))
    if not choices:
        raise ValueError("Round two requires a complete development grammar obstruction")
    return min(choices, key=lambda item: item[0])[1]


def same_protocol_spec(recorded, proposed):
    """Execution hashes differ on replay; the mathematical experiment may not."""
    return ({k: v for k, v in recorded.items() if k != "input_sha256"}
            == {k: v for k, v in proposed.items() if k != "input_sha256"})


def run_comparison(input_path, output):
    h3.verify_protocol()
    previous = json.loads(input_path.read_text())
    if previous.get("program") != "P012" or previous.get("round") != 1 or not previous.get("source_stable"):
        raise ValueError("Expected a stable P012 round-one execution record")
    case = obstruction_case(previous)
    h = tuple(case["h"])
    # Pre-register precisely the one comparison before its first enumeration.
    frozen = dict(round=2, input_sha256=h3.digest(input_path), h=h, target=h3.target(len(h)),
                  selection="lexicographically smallest complete development isolated tableau state",
                  enumeration="all decreasing parent forests, all compositions of target type, all marks",
                  diagnostic="one mark changes by one with epsilon toggle; no join/split search",
                  limits=h3.LIMITS, holdout_used_for_repair=False)
    protocol_path = h3.PHASE / "forest-protocol.json"
    if protocol_path.exists():
        if not same_protocol_spec(json.loads(protocol_path.read_text()), json.loads(h3.encoded(frozen))):
            raise ValueError("Refusing to change the round-two protocol")
    else:
        h3.write_report(protocol_path, frozen)
    source = h3.provenance()
    signal.signal(signal.SIGALRM, h3._alarm)
    budget = h3.Budget()
    budget.begin_case()
    signal.setitimer(signal.ITIMER_REAL, budget.limits["case_seconds"])
    report = dict(program="P012", round=2, status="finite-exact-evidence", research_validated=False,
                  protocol=frozen, protocol_sha256=h3.digest(protocol_path), provenance=source)
    try:
        result = coefficient(h, h3.target(len(h)), budget, diagnostics=True)
        if result["coefficient"] != case["signed_space"]["coefficient"]:
            raise AssertionError("complete forest and tableau coefficients disagree")
        if case.get("oracle", {}).get("status") != "agrees":
            raise ValueError("Selected comparison lacks a completed independent coloring check")
        report["comparison"] = result | dict(tableau_agrees=True, coloring_agrees=True)
    except (h3.Capped, MemoryError) as exc:
        report["comparison"] = dict(status="capped", reason=str(exc) or "memory allocation")
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
    report["resources"] = budget.receipt()
    report["source_stable"] = source["sources"] == h3.provenance()["sources"]
    if not report["source_stable"]:
        raise ValueError("Experiment sources changed during forest comparison")
    h3.write_report(output, report)
    return dict(output=str(output), status=report["comparison"]["status"], resources=report["resources"])
