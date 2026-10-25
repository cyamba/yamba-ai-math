"""Exact small-case P-tableaux and dual Jacobi--Trudi calculations.

Standard library only. Labels and Hessenberg values are 1-based. All output is
finite evidence, not a proof of positivity for arbitrary size.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from functools import lru_cache
from itertools import permutations
import argparse
import json
from pathlib import Path


def partitions(n: int, maximum: int | None = None):
    if n == 0:
        yield ()
    else:
        for first in range(min(n, n if maximum is None else maximum), 0, -1):
            for rest in partitions(n - first, first):
                yield (first,) + rest


def hessenberg_vectors(n: int):
    def generate(prefix):
        i = len(prefix) + 1
        if i > n:
            yield tuple(prefix)
        else:
            for x in range(max(i, prefix[-1] if prefix else 1), n + 1):
                yield from generate(prefix + [x])
    yield from generate([])


def check_h(h):
    n = len(h)
    if any(not i <= x <= n for i, x in enumerate(h, 1)) or any(
        a > b for a, b in zip(h, h[1:])
    ):
        raise ValueError("Expected a weakly increasing 1-based Hessenberg vector")


def lt_p(h, u, v):
    return h[u - 1] < v


def graph_edges(h):
    check_h(h)
    return tuple((u, v) for u in range(1, len(h) + 1)
                 for v in range(u + 1, h[u - 1] + 1))


def validates(h, rows, shape=None):
    if shape is not None and tuple(map(len, rows)) != tuple(shape):
        return False
    if any(not row for row in rows):
        return False
    word = [u for row in rows for u in row]
    if sorted(word) != list(range(1, len(h) + 1)):
        return False
    if any(not lt_p(h, u, v) for row in rows for u, v in zip(row, row[1:])):
        return False
    for upper, lower in zip(rows, rows[1:]):
        if len(lower) > len(upper):
            return False
        if any(lt_p(h, v, u) for u, v in zip(upper, lower)):
            return False
    return True


def tableaux(h, shape):
    check_h(h)
    if sum(shape) != len(h) or any(x <= 0 for x in shape):
        raise ValueError("Shape must be a partition of the number of vertices")
    if any(a < b for a, b in zip(shape, shape[1:])):
        raise ValueError("Shape must be weakly decreasing")
    boundaries = [0]
    for x in shape:
        boundaries.append(boundaries[-1] + x)
    for word in permutations(range(1, len(h) + 1)):
        rows = tuple(word[a:b] for a, b in zip(boundaries, boundaries[1:]))
        if validates(h, rows):
            yield rows


def inv_g(h, rows):
    """Count larger labels in an earlier row across graph edges."""
    row_of = {u: i for i, row in enumerate(rows) for u in row}
    return sum(row_of[v] < row_of[u] for u, v in graph_edges(h))


def demote(rows, k):
    """Split row k (zero indexed) [a,b] into [a],[b]. Does not assume validity."""
    if len(rows[k]) != 2 or any(len(row) != 1 for row in rows[k + 1:]):
        raise ValueError("Expected a final two-cell row followed by singleton rows")
    a, b = rows[k]
    return tuple(rows[:k]) + ((a,), (b,)) + tuple(rows[k + 1:])


def suffix_admissible(h, rows, k):
    return k + 1 == len(rows) or not lt_p(h, rows[k + 1][0], rows[k][1])


def height_two(h):
    """Whether P_h has no strict chain of three distinct elements."""
    return not any(lt_p(h, a, b) and lt_p(h, b, c)
                   for a in range(1, len(h) + 1)
                   for b in range(1, len(h) + 1)
                   for c in range(1, len(h) + 1))


def bubble_demote(h, rows, k):
    """Cho--Huh insertion: pass the corner across an initial comparable block.

    k is the zero-based index of the last two-cell row. It may be zero.
    Validity is preserved for posets; injectivity additionally needs height <=2.
    """
    if len(rows[k]) != 2 or any(len(row) != 1 for row in rows[k + 1:]):
        raise ValueError("Expected a final two-cell row followed by singleton rows")
    a, b = rows[k]
    tail = tuple(row[0] for row in rows[k + 1:])
    split = 0
    while split < len(tail) and lt_p(h, tail[split], b):
        split += 1
    new_tail = tail[:split] + (b,) + tail[split:]
    return tuple(rows[:k]) + ((a,),) + tuple((z,) for z in new_tail)


def recover(h, rows, k):
    """First eligible extraction; returns None outside the putative image.

    A successful inverse is required to satisfy all original tableau conditions
    and to reproduce the supplied positive tableau when reinserted.
    """
    a = rows[k][0]
    tail = tuple(row[0] for row in rows[k + 1:])
    for i, b in enumerate(tail):
        if lt_p(h, a, b):
            source = tuple(rows[:k]) + ((a, b),) + tuple(
                (z,) for z in tail[:i] + tail[i + 1:])
            if validates(h, source) and bubble_demote(h, source, k) == tuple(rows):
                return source
            return None
    return None


@lru_cache(None)
def djt_terms(shape):
    """Coefficient of each e_lambda in s_shape, from the integer determinant."""
    if not shape:
        return {(): 1}
    columns = tuple(sum(x > j for x in shape) for j in range(shape[0]))
    result = Counter()
    for sigma in permutations(range(len(columns))):
        indices = tuple(x - i + sigma[i] for i, x in enumerate(columns))
        if min(indices) < 0:
            continue
        target = tuple(sorted((x for x in indices if x), reverse=True))
        inversions = sum(a > b for i, a in enumerate(sigma) for b in sigma[i + 1:])
        result[target] += (-1) ** inversions
    return {key: val for key, val in result.items() if val}


def trim(poly):
    result = list(poly)
    while result and result[-1] == 0:
        result.pop()
    return tuple(result)


def elementary_expansion(h):
    """Finite Schur-tableau sum converted to the elementary basis."""
    result = defaultdict(Counter)
    for shape in partitions(len(h)):
        weights = Counter(inv_g(h, rows) for rows in tableaux(h, shape))
        for target, sign in djt_terms(shape).items():
            for degree, count in weights.items():
                result[target][degree] += sign * count
    return {target: p for target, counts in result.items()
            if (p := trim(counts[i] for i in range(max(counts, default=-1) + 1)))}


def pdf_arm_leg(h, rows):
    """The top-only rule actually stated on PDF page 3; not its later trace."""
    corner = rows[0][0]
    arm = rows[0][1:]
    leg = tuple(row[0] for row in rows[1:])
    if arm and (not leg or not lt_p(h, leg[0], arm[0])):
        return ((corner,) + arm[1:], (arm[0],)) + tuple((x,) for x in leg)
    if leg and lt_p(h, corner, leg[0]) and (not arm or lt_p(h, leg[0], arm[0])):
        return ((corner, leg[0]) + arm,) + tuple((x,) for x in leg[1:])
    return rows


def run_audit(max_n=5):
    report = {"status": "finite-exact-evidence", "max_n": max_n,
              "conventions": "1-based h; row strict P-chain; no column P-descent",
              "sizes": [], "first_slide_failure": None,
              "first_negative_hook_fixed_point": None}
    for n in range(2, max_n + 1):
        stats = Counter()
        for h in hessenberg_vectors(n):
            stats["hessenberg_vectors"] += 1
            for k in range(1, n // 2):
                if n < 2 * (k + 1):
                    continue
                shape = (2,) * (k + 1) + (1,) * (n - 2 * k - 2)
                for rows in tableaux(h, shape):
                    stats["slide_sources"] += 1
                    target = demote(rows, k)
                    valid = validates(h, target)
                    assert valid == suffix_admissible(h, rows, k)
                    assert inv_g(h, rows) == inv_g(h, target)
                    assert tuple(x for row in rows for x in row) == tuple(
                        x for row in target for x in row)
                    if not valid:
                        stats["blocked_slides"] += 1
                        if report["first_slide_failure"] is None:
                            report["first_slide_failure"] = {
                                "h": h, "k": k, "source": rows, "target": target}
            for c in range(2, n + 1):
                if c % 2:
                    continue  # negative sign means c even
                for rows in tableaux(h, (c,) + (1,) * (n - c)):
                    if pdf_arm_leg(h, rows) == rows:
                        stats["negative_hook_fixed_points"] += 1
                        if report["first_negative_hook_fixed_point"] is None:
                            report["first_negative_hook_fixed_point"] = {"h": h, "tableau": rows}
        report["sizes"].append({"n": n, **dict(stats)})
    total_order = tuple(range(1, 6))
    report["cardinality_obstruction"] = {
        "h": total_order,
        "negative_221": list(tableaux(total_order, (2, 2, 1))),
        "positive_2111": list(tableaux(total_order, (2, 1, 1, 1))),
        "djt_e41": {"".join(map(str,s)): djt_terms(s).get((4, 1), 0)
                    for s in partitions(5)}}
    h = (3, 4, 4, 5, 5)
    source = ((1, 4), (2, 5), (3,))
    assert validates(h, source) and not validates(h, demote(source, 1))
    report["connected_height_two_witness"] = {
        "h": h, "edges": graph_edges(h), "source": source,
        "target": demote(source, 1), "inv": inv_g(h, source),
        "source_count": len(list(tableaux(h, (2, 2, 1)))),
        "target_count": len(list(tableaux(h, (2, 1, 1, 1)))),
        "elementary_expansion": {str(s): p for s,p in elementary_expansion(h).items()}}
    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-n", type=int, default=5, choices=range(2, 7))
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = json.dumps(run_audit(args.max_n), indent=2) + "\n"
    if args.output:
        args.output.write_text(result)
    else:
        print(result, end="")
