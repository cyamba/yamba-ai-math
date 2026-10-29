"""Exact KR1 objects and candidate falsifiers. Finite agreement is not a proof.

No enumeration or ranking is used to define a claimed KR1 bijection.
The column encoding is an attributed conjugation interface, not the missing
weighted-to-cluster bridge. All public partition tuples have explicit order.
"""

from collections import Counter
from dataclasses import dataclass
from functools import lru_cache
from math import isqrt
from itertools import product


ROW_WEIGHTS = (1, 2, 3, 2, 1)
RESIDUES = frozenset((1, 3, 6, 8))
PREFIX = (0, 1, 3, 6, 8)


def natural(n):
    if type(n) is not int or n < 0:
        raise ValueError("weight must be a nonnegative integer")
    return n


def _integers(parts, *, positive=True):
    return isinstance(parts, (tuple, list)) and all(
        type(p) is int and p >= int(positive) for p in parts
    )


def is_gap(parts):
    """A: positive ascending list, literal adjacent/distance-two predicates."""
    return (
        _integers(parts)
        and all(x <= y for x, y in zip(parts, parts[1:]))
        and all(parts[i + 2] >= parts[i] + 3 for i in range(len(parts) - 2))
        and all(y > x + 1 or (x + y) % 3 == 0
                for x, y in zip(parts, parts[1:]))
    )


def is_residue(parts):
    """B: ascending positive parts, residues 1,3,6,8 modulo nine."""
    return (_integers(parts)
            and all(x <= y for x, y in zip(parts, parts[1:]))
            and all(p % 9 in RESIDUES for p in parts))


def is_weighted(parts):
    """W: descending positive parts, multiplicities at most four."""
    return (_integers(parts)
            and all(x >= y for x, y in zip(parts, parts[1:]))
            and all(count <= 4 for count in Counter(parts).values()))


def weighted_size(parts):
    if not is_weighted(parts):
        raise ValueError("not a weighted partition")
    return sum(ROW_WEIGHTS[i % 5] * p for i, p in enumerate(parts))


def prefix_weight(height):
    natural(height)
    quotient, residue = divmod(height, 5)
    return 9 * quotient + PREFIX[residue]


def inverse_prefix(value):
    natural(value)
    quotient, residue = divmod(value, 9)
    if residue not in PREFIX:
        raise ValueError("not a weighted column value")
    return 5 * quotient + PREFIX.index(residue)


def conjugate(descending):
    if not _integers(descending) or any(
            x < y for x, y in zip(descending, descending[1:])):
        raise ValueError("conjugation expects descending positive parts")
    return tuple(sum(p >= j for p in descending)
                 for j in range(1, (descending[0] if descending else 0) + 1))


def weighted_columns(parts):
    """Lossless U encoding: weighted conjugate column heights, descending."""
    if not is_weighted(parts):
        raise ValueError("not a weighted partition")
    return tuple(prefix_weight(h) for h in conjugate(parts))


def decode_columns(columns):
    if not _integers(columns) or any(x < y for x, y in zip(columns, columns[1:])):
        raise ValueError("columns must be descending positive integers")
    heights = tuple(inverse_prefix(c) for c in columns)
    # The final boundary is essential: the last height must also be <5.
    if any(x - y >= 5 for x, y in zip(heights, heights[1:] + (0,))):
        raise ValueError("decoded heights are not 5-flat, including the tail")
    result = conjugate(heights)
    if not is_weighted(result):
        raise ValueError("column encoding has invalid multiplicities")
    return result


def row_projection(parts):
    """Frozen, refuted candidate R; retained to reproduce its failures."""
    if not is_weighted(parts):
        raise ValueError("not a weighted partition")
    return tuple(sorted(ROW_WEIGHTS[i % 5] * p for i, p in enumerate(parts)))


@dataclass(frozen=True)
class RuleProfile:
    plateau_first: bool = False
    residue_guard: bool = True
    plateau_spread: bool = True
    merge_upper: bool = True

    @property
    def name(self):
        return "".join(str(int(value)) for value in
                       (self.plateau_first, self.residue_guard,
                        self.plateau_spread, self.merge_upper))


RULE_PROFILES = tuple(RuleProfile(*values) for values in product((False, True), repeat=4))
DEFAULT_PROFILE = RuleProfile()


def column_straighten(parts, *, profile=DEFAULT_PROFILE, capture_trace=False):
    """Frozen R2 candidate: a total normalization, not an asserted bijection.

    Return (image, rewrite_count, optional_trace). Trace capture is diagnostic
    and can exceed the contracted quadratic working space; default execution
    retains no history. Every rule raises the sum of squares at fixed weight,
    so there are at most N^2/2 updates. Injectivity is never assumed.
    """
    state = tuple(sorted(weighted_columns(parts)))
    weight = sum(state)
    trace = []
    rewrites = 0
    while True:
        rule = None
        if profile.plateau_first:
            for i, (x, y, z) in enumerate(zip(state, state[1:], state[2:])):
                if z - x <= 2 and y == z:
                    if profile.plateau_spread:
                        replacement = tuple(p for p in (x - 1, y - 1, z + 2) if p)
                        rule = "triple_spread"
                    else:
                        replacement = (x, y + z)
                        rule = "triple_merge_upper"
                    width = 3
                    break
        if rule is None:
            for i, (x, y) in enumerate(zip(state, state[1:])):
                if y - x <= 1 and (x + y) % 3:
                    if profile.residue_guard and (x + y) % 9 in RESIDUES:
                        replacement = (x - 1, y + 1)
                        rule = "pair_spread"
                    else:
                        replacement = (x + y,)
                        rule = "pair_merge"
                    width = 2
                    break
        if rule is None:
            for i, (x, y, z) in enumerate(zip(state, state[1:], state[2:])):
                if z - x <= 2:
                    if y == z and profile.plateau_spread:
                        replacement = tuple(p for p in (x - 1, y - 1, z + 2) if p)
                        rule = "triple_spread"
                    else:
                        if y == z or profile.merge_upper:
                            replacement = (x, y + z)
                            rule = "triple_merge_upper"
                        else:
                            replacement = (x + y, z)
                            rule = "triple_merge_lower"
                    width = 3
                    break
        if rule is None:
            return state, rewrites, tuple(trace)
        updated = tuple(sorted(state[:i] + replacement + state[i + width:]))
        if (not _integers(updated) or sum(updated) != weight
                or sum(p * p for p in updated) <= sum(p * p for p in state)):
            raise AssertionError("R2 update violated its termination invariant")
        rewrites += 1
        if capture_trace:
            trace.append({"rule": rule, "index": i, "before": state, "after": updated})
        if rewrites * 2 > weight * weight:
            raise AssertionError("R2 exceeded its proved energy step bound")
        state = updated


def first_straightening_falsifier(ceiling, profile=DEFAULT_PROFILE):
    """Exact finite fibres of frozen R2; a collision is mathematical evidence."""
    natural(ceiling)
    tested = steps = max_steps = 0
    for n in range(ceiling + 1):
        fibres = {}
        for parts in sorted(weighted_partitions(n)):
            image, rewrites, _ = column_straighten(parts, profile=profile)
            tested += 1
            steps += rewrites
            max_steps = max(max_steps, rewrites)
            if sum(image) != n or not is_gap(image):
                return {"status": "invalid_image", "weight": n, "input": parts,
                        "image": image,
                        "trace": column_straighten(parts, profile=profile, capture_trace=True)[2],
                        "tested": tested}
            if image in fibres:
                previous = fibres[image]
                return {"status": "refuted_collision", "weight": n,
                        "inputs": (previous, parts), "image": image,
                        "traces": (column_straighten(previous, profile=profile, capture_trace=True)[2],
                                   column_straighten(parts, profile=profile, capture_trace=True)[2]),
                        "tested": tested,
                        "rewrites": steps, "max_rewrites": max_steps}
            fibres[image] = parts
        missing = set(gap_partitions(n)) - set(fibres)
        if missing:
            return {"status": "refuted_missing_image", "weight": n,
                    "missing": sorted(missing), "tested": tested}
    return {"status": "empirical_no_falsifier", "ceiling": ceiling,
            "tested": tested, "rewrites": steps, "max_rewrites": max_steps,
            "inverse": None}


def ordinary_partitions(n, minimum=1):
    """All ascending ordinary partitions, independent of gap restrictions."""
    natural(n)
    if n == 0:
        yield ()
    else:
        for first in range(minimum, n + 1):
            for rest in ordinary_partitions(n - first, first):
                yield (first,) + rest


def gap_partitions(n):
    """Generate A directly, pruning only newly formed local restrictions."""
    natural(n)

    def extend(prefix, remaining):
        if remaining == 0:
            yield prefix
            return
        minimum = prefix[-1] if prefix else 1
        if len(prefix) >= 2:
            minimum = max(minimum, prefix[-2] + 3)
        for part in range(minimum, remaining + 1):
            if prefix and part <= prefix[-1] + 1 and (prefix[-1] + part) % 3:
                continue
            yield from extend(prefix + (part,), remaining - part)

    yield from extend((), n)


def residue_partitions(n):
    """Generate B by coin multiplicities, not by the gap predicate."""
    natural(n)
    coins = tuple(p for p in range(1, n + 1) if p % 9 in RESIDUES)

    def extend(index, remaining):
        if index == len(coins):
            if remaining == 0:
                yield ()
            return
        part = coins[index]
        for count in range(remaining // part + 1):
            for tail in extend(index + 1, remaining - count * part):
                yield (part,) * count + tail

    yield from extend(0, n)


def weighted_partitions(n):
    """Generate W using remaining positional weight, not ordinary size."""
    natural(n)

    def extend(prefix, remaining, previous, repeats):
        if remaining == 0:
            yield prefix
            return
        cost = ROW_WEIGHTS[len(prefix) % 5]
        for part in range(1, min(previous, remaining // cost) + 1):
            next_repeats = repeats + 1 if part == previous else 1
            if next_repeats <= 4:
                yield from extend(prefix + (part,), remaining - cost * part,
                                  part, next_repeats)

    yield from extend((), n, n + 1, 0)


def nonnegative_vectors(length, total, minimum=0):
    """Exact length, ascending, zero-padded increment vectors."""
    natural(length)
    natural(total)
    if length == 0:
        if total == 0:
            yield ()
        return
    for first in range(minimum, total // length + 1):
        for tail in nonnegative_vectors(length - 1, total - first, first):
            yield (first,) + tail


@dataclass(frozen=True)
class ClusterData:
    a: int
    b: int
    mu: tuple
    nu: tuple

    def __post_init__(self):
        natural(self.a)
        natural(self.b)
        for vector, length in ((self.mu, self.a), (self.nu, self.b)):
            if (not isinstance(vector, tuple) or len(vector) != length
                    or not _integers(vector, positive=False)
                    or any(x > y for x, y in zip(vector, vector[1:]))):
                raise ValueError("increments must be ascending exact-length nonnegative tuples")

    @property
    def weight(self):
        return (self.a ** 2 + 3 * self.a * self.b + 3 * self.b ** 2
                + sum(self.mu) + 3 * sum(self.nu))

    @property
    def gap_length(self):
        return self.a + 2 * self.b


def cluster_data(n):
    natural(n)
    for a in range(isqrt(n) + 1):
        for b in range(isqrt(n // 3) + 1):
            remaining = n - (a * a + 3 * a * b + 3 * b * b)
            if remaining < 0:
                continue
            for nu_sum in range(remaining // 3 + 1):
                for mu in nonnegative_vectors(a, remaining - 3 * nu_sum):
                    for nu in nonnegative_vectors(b, nu_sum):
                        yield ClusterData(a, b, mu, nu)


def residue_counts(ceiling):
    """Independent Euler-product coefficient DP for B."""
    natural(ceiling)
    counts = [1] + [0] * ceiling
    for part in range(1, ceiling + 1):
        if part % 9 in RESIDUES:
            for n in range(part, ceiling + 1):
                counts[n] += counts[n - part]
    return counts


def cluster_counts(ceiling):
    """Independent denominator coefficient DP, not increment enumeration."""
    natural(ceiling)
    counts = [0] * (ceiling + 1)
    for a in range(isqrt(ceiling) + 1):
        for b in range(isqrt(ceiling // 3) + 1):
            base = a * a + 3 * a * b + 3 * b * b
            if base > ceiling:
                continue
            coefficients = [1] + [0] * (ceiling - base)
            for part in tuple(range(1, a + 1)) + tuple(range(3, 3 * b + 1, 3)):
                for n in range(part, len(coefficients)):
                    coefficients[n] += coefficients[n - part]
            for n, coefficient in enumerate(coefficients):
                counts[base + n] += coefficient
    return counts


def flat_column_counts(ceiling):
    """Independent W coefficient DP on 5-flat column paths.

    A height h contributes F(h); the next height is h-d, 0<=d<=4.
    Zero decrement is a repeated column; positive weight makes recursion
    in remaining weight well founded. Height zero is the unique empty tail.
    """
    natural(ceiling)

    @lru_cache(maxsize=None)
    def paths(height, remaining):
        if height == 0:
            return int(remaining == 0)
        remaining -= prefix_weight(height)
        if remaining < 0:
            return 0
        return sum(paths(height - decrement, remaining)
                   for decrement in range(min(4, height) + 1))

    max_height = 0
    while prefix_weight(max_height + 1) <= ceiling:
        max_height += 1
    return [int(n == 0) + sum(paths(h, n) for h in range(1, max_height + 1))
            for n in range(ceiling + 1)]


def first_projection_falsifiers(ceiling):
    """Ascending N; lexical tuple order fixes reproducible witness choice."""
    natural(ceiling)
    invalid = collision = length_mismatch = None
    for n in range(ceiling + 1):
        weighted = sorted(weighted_partitions(n))
        seen = {}
        for parts in weighted:
            projected = row_projection(parts)
            if invalid is None and not is_gap(projected):
                invalid = {"weight": n, "input": parts, "projection": projected}
            if collision is None and projected in seen:
                collision = {"weight": n, "inputs": (seen[projected], parts),
                             "projection": projected}
            seen[projected] = parts
        w_lengths = Counter(map(len, weighted))
        c_lengths = Counter(item.gap_length for item in cluster_data(n))
        if length_mismatch is None and w_lengths != c_lengths:
            length_mismatch = {"weight": n, "weighted_lengths": dict(w_lengths),
                               "cluster_gap_lengths": dict(c_lengths)}
        if invalid and collision and length_mismatch:
            break
    return {"invalid_projection": invalid, "projection_collision": collision,
            "length_mismatch": length_mismatch}
