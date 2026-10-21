"""Reproduce bounded comparisons of independent exact algorithms.

Run from any directory, for example:
  python3 research/partitions/checks/verify.py --max-n 5 --output \
    research/partitions/evidence/comparison.json

Agreement and nonnegative coefficients in these finite instances do not
settle the general chromatic quasisymmetric e-positivity conjecture.
"""

import argparse
import json
from pathlib import Path

try:
    from . import coloring_oracle, tableaux
except ImportError:  # Direct invocation as a file.
    import coloring_oracle
    import tableaux


def _height_two(h):
    """Independent direct test that P(h) has no three-element chain."""
    n = len(h)
    return not any(
        h[a - 1] < b and h[b - 1] < c
        for a in range(1, n + 1)
        for b in range(a + 1, n + 1)
        for c in range(b + 1, n + 1)
    )


def _valid_tableau(h, rows, shape):
    if tuple(map(len, rows)) != shape:
        return False
    if sorted(label for row in rows for label in row) != list(range(1, len(h) + 1)):
        return False
    for row in rows:
        if any(h[a - 1] >= b for a, b in zip(row, row[1:])):
            return False
    return not any(
        h[lower - 1] < upper
        for top, bottom in zip(rows, rows[1:])
        for upper, lower in zip(top, bottom)
    )


def _inversion(h, rows):
    row_index = {label: i for i, row in enumerate(rows) for label in row}
    return sum(
        row_index[b] < row_index[a]
        for a in range(1, len(h) + 1)
        for b in range(a + 1, len(h) + 1)
        if b <= h[a - 1]
    )


def _verify_bubble(max_n):
    sizes = []
    failures = []
    for n in range(2, max_n + 1):
        stats = {
            "n": n,
            "height_at_most_two_vectors": 0,
            "source_families": 0,
            "sources": 0,
            "valid_images": 0,
            "inversion_preserved": 0,
            "recovered_sources": 0,
            "distinct_images": 0,
        }
        for h in tableaux.hessenberg_vectors(n):
            small_height = _height_two(h)
            if small_height != tableaux.height_two(h):
                failures.append({"kind": "height_predicate_disagreement", "h": h})
            if not small_height:
                continue
            stats["height_at_most_two_vectors"] += 1
            for k in range(n // 2):
                source_shape = (2,) * (k + 1) + (1,) * (n - 2 * k - 2)
                target_shape = (2,) * k + (1,) * (n - 2 * k)
                stats["source_families"] += 1
                images = set()
                for source in tableaux.tableaux(h, source_shape):
                    stats["sources"] += 1
                    image = tableaux.bubble_demote(h, source, k)
                    if _valid_tableau(h, image, target_shape):
                        stats["valid_images"] += 1
                    else:
                        failures.append({"kind": "invalid_bubble_image", "h": h, "k": k, "source": source})
                    if _inversion(h, source) == _inversion(h, image):
                        stats["inversion_preserved"] += 1
                    else:
                        failures.append({"kind": "bubble_weight_changed", "h": h, "k": k, "source": source})
                    if tableaux.recover(h, image, k) == source:
                        stats["recovered_sources"] += 1
                    else:
                        failures.append({"kind": "bubble_recovery_failed", "h": h, "k": k, "source": source})
                    if image in images:
                        failures.append({"kind": "bubble_collision", "h": h, "k": k, "image": image})
                    images.add(image)
                stats["distinct_images"] += len(images)
        sizes.append(stats)
    return sizes, failures


def verify(max_n=5, bubble_max_n=7):
    if not 0 <= max_n <= 6:
        raise ValueError("the bounded comparison supports 0 <= max_n <= 6")
    if not 0 <= bubble_max_n <= 7:
        raise ValueError("the bounded bubble check supports 0 <= n <= 7")
    sizes = []
    failures = []
    for n in range(max_n + 1):
        stats = {
            "n": n,
            "hessenberg_vectors": 0,
            "independent_expansion_agreements": 0,
            "nonnegative_expansions": 0,
            "height_at_most_two_vectors": 0,
            "height_at_most_two_nonnegative_expansions": 0,
        }
        for h in tableaux.hessenberg_vectors(n):
            stats["hessenberg_vectors"] += 1
            direct = coloring_oracle.elementary_expansion(h)
            via_tableaux = tableaux.elementary_expansion(h)
            if direct == via_tableaux:
                stats["independent_expansion_agreements"] += 1
            else:
                failures.append({"kind": "expansion_disagreement", "h": h})
            nonnegative = all(c >= 0 for poly in direct.values() for c in poly)
            if nonnegative:
                stats["nonnegative_expansions"] += 1
            else:
                failures.append({"kind": "negative_coefficient", "h": h})
            if _height_two(h):
                stats["height_at_most_two_vectors"] += 1
                if nonnegative:
                    stats["height_at_most_two_nonnegative_expansions"] += 1
        sizes.append(stats)
    bubble_sizes, bubble_failures = _verify_bubble(bubble_max_n)
    failures.extend(bubble_failures)
    return {
        "schema_version": 1,
        "status": "finite_exact_comparison_passed" if not failures else "failed",
        "claim_scope": "All natural unit interval Hessenberg vectors with 0 <= n <= max_n",
        "maximum_n": max_n,
        "methods": {
            "direct": "Proper colorings with prescribed named-color multiplicities; elementary subset expansion; exact rational matrix inversion",
            "tableaux": "P-tableau enumeration; graph inversion weights; dual Jacobi--Trudi determinant",
        },
        "q_convention": "asc counts graph edges i < j with color(i) < color(j)",
        "coefficient_arithmetic": "Exact Python integers and fractions; standard library only",
        "sizes": sizes,
        "total_hessenberg_vectors": sum(row["hessenberg_vectors"] for row in sizes),
        "bubble_maximum_n": bubble_max_n,
        "bubble_scope": "All height-at-most-two Hessenberg vectors and source shapes (2^(k+1),1^(n-2k-2)), 0 <= k < floor(n/2)",
        "bubble_sizes": bubble_sizes,
        "bubble_total_sources": sum(row["sources"] for row in bubble_sizes),
        "failures": failures,
        "general_conjecture_status": "Not settled by this finite computation",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-n", type=int, choices=range(7), default=5)
    parser.add_argument("--bubble-max-n", type=int, choices=range(8), default=7)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = verify(args.max_n, args.bubble_max_n)
    rendered = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered)
    else:
        print(rendered, end="")
    raise SystemExit(bool(result["failures"]))
