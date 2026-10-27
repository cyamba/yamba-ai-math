"""Independent coefficient audit of the positive all-n word formulas.

Words and gap partitions are enumerated only to verify coefficient identities;
they do not define any proposed bijection. Pure Python, exact integer arithmetic.
"""

from itertools import combinations, product
from functools import lru_cache
from pathlib import Path
import argparse
import json


def coin_series(coins, bound):
    out = [1] + [0] * bound
    for coin in coins:
        for j in range(coin, bound + 1):
            out[j] += out[j - coin]
    return out


def convolve(a, b, bound):
    out = [0] * (bound + 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b[:bound-i+1]):
                out[i+j] += x*y
    return out


def word_base(n, kind, word):
    length = len(word)
    layer = 0
    total = 0
    if kind == "A" and word and word[0] == "a":
        total += 9 * length
    for i, symbol in enumerate(word):
        if i and word[i-1] == "b" and symbol == "a":
            total += 9 * (length-i)
        if symbol == "|":
            layer += 1
        elif kind == "C":
            total += 3*n+4+3*layer if symbol == "a" else 6*n+5-3*layer
        else:
            total += 3*n-1+3*layer if symbol == "a" else 6*n+1-3*layer
    return total


def positive_counts(n, kind, bound):
    if kind == "A" and n == 0:
        return coin_series((j for j in range(1, bound+1) if j % 9 in (1,3,6,8)), bound), 0
    min_particle = 3*n+4 if kind == "C" else 3*n-1
    m = n // 3
    result = [0] * (bound + 1)
    words_checked = 0
    for particles in range(bound//min_particle+1):
        length = n + particles
        denominator = coin_series((9*h for h in range(m+1, length+1)), bound)
        for cut_positions in combinations(range(length), n):
            cuts = set(cut_positions)
            for colors in product("ab", repeat=particles):
                it = iter(colors)
                word = tuple("|" if i in cuts else next(it) for i in range(length))
                base = word_base(n, kind, word)
                words_checked += 1
                if base <= bound:
                    for d in range(bound-base+1):
                        result[base+d] += denominator[d]
    common = coin_series((3*j for j in range(n+1, bound//3+1) if j % 3), bound)
    return convolve(result, common, bound), words_checked


def literal_gap_counts(minimum, bound):
    """DP on the last two actual parts; no transfer-matrix or word formulas."""
    @lru_cache(None)
    def exact(left, previous, before):
        if left == 0:
            return 1
        count = 0
        for value in range(max(minimum, previous), left+1):
            if previous and value-previous <= 1 and (value+previous) % 3:
                continue
            if before and value-before < 3:
                continue
            count += exact(left-value, value, previous)
        return count
    return [exact(weight, 0, 0) for weight in range(bound+1)]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--bound", type=int, default=45)
    parser.add_argument("--max-n", type=int, default=8)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.bound < 0 or args.max_n < 0:
        parser.error("bounds must be nonnegative")
    records = []
    for n in range(args.max_n+1):
        for kind, offset in (("A", 1), ("C", 3)):
            # A1's excluded smallest particle makes an unconstrained word
            # traversal expensive. Bound its check explicitly, not silently.
            bound = min(args.bound, 30) if kind == "A" and n == 1 else args.bound
            counts, words = positive_counts(n, kind, bound)
            expected = literal_gap_counts(3*n+offset, bound)
            mismatches = [i for i,(x,y) in enumerate(zip(counts, expected)) if x != y]
            row = {"family": kind, "n": n, "bound": bound,
                   "words_visited": words, "matched_coefficients": bound+1,
                   "mismatches": mismatches, "coefficients": counts}
            records.append(row)
            print(f"{kind}_{n}: coefficients 0..{bound}, {words} words, mismatches={mismatches}", flush=True)
            if mismatches:
                raise AssertionError(row)
    report = {"status": "finite coefficient checks only", "records": records,
              "full_kr1_bijection": False}
    if args.output:
        args.output.write_text(json.dumps(report, indent=2)+"\n")


if __name__ == "__main__":
    main()
