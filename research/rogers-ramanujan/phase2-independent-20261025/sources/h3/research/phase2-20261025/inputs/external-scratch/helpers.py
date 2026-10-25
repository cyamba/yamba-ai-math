"""Self-contained helper in scratch for sandboxed mathematical exploration."""
from __future__ import annotations
from collections import Counter, defaultdict
from dataclasses import dataclass
from functools import lru_cache
from itertools import permutations, product
from math import isqrt

# --- TABLEAUX HELPERS ---
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

def lt_p(h, u, v):
    return h[u - 1] < v

def graph_edges(h):
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
    boundaries = [0]
    for x in shape:
        boundaries.append(boundaries[-1] + x)
    for word in permutations(range(1, len(h) + 1)):
        rows = tuple(word[a:b] for a, b in zip(boundaries, boundaries[1:]))
        if validates(h, rows):
            yield rows

def inv_g(h, rows):
    row_of = {u: i for i, row in enumerate(rows) for u in row}
    return sum(row_of[v] < row_of[u] for u, v in graph_edges(h))

@lru_cache(None)
def djt_terms(shape):
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

# --- KR1 HELPERS ---
ROW_WEIGHTS = (1, 2, 3, 2, 1)
RESIDUES = frozenset((1, 3, 6, 8))
PREFIX = (0, 1, 3, 6, 8)

def is_gap(parts):
    return (
        all(x >= 1 for x in parts)
        and all(x <= y for x, y in zip(parts, parts[1:]))
        and all(parts[i + 2] >= parts[i] + 3 for i in range(len(parts) - 2))
        and all(y > x + 1 or (x + y) % 3 == 0 for x, y in zip(parts, parts[1:]))
    )

def is_residue(parts):
    return (all(x >= 1 for x in parts)
            and all(x <= y for x, y in zip(parts, parts[1:]))
            and all(p % 9 in RESIDUES for p in parts))

def is_weighted(parts):
    return (all(x >= 1 for x in parts)
            and all(x >= y for x, y in zip(parts, parts[1:]))
            and all(count <= 4 for count in Counter(parts).values()))

def prefix_weight(height):
    quotient, residue = divmod(height, 5)
    return 9 * quotient + PREFIX[residue]

def inverse_prefix(value):
    quotient, residue = divmod(value, 9)
    if residue not in PREFIX:
        raise ValueError("not a weighted column value")
    return 5 * quotient + PREFIX.index(residue)

def conjugate(descending):
    return tuple(sum(p >= j for p in descending)
                 for j in range(1, (descending[0] if descending else 0) + 1))

def weighted_columns(parts):
    return tuple(prefix_weight(h) for h in conjugate(parts))

def decode_columns(columns):
    if any(x <= 0 for x in columns) or any(x < y for x, y in zip(columns, columns[1:])):
        raise ValueError("columns must be descending positive integers")
    heights = tuple(inverse_prefix(c) for c in columns)
    if any(x - y >= 5 for x, y in zip(heights, heights[1:] + (0,))):
        raise ValueError("decoded heights are not 5-flat, including the tail")
    result = conjugate(heights)
    if not is_weighted(result):
        raise ValueError("column encoding has invalid multiplicities")
    return result

def weighted_partitions(n):
    def extend(prefix, remaining, previous, repeats):
        if remaining == 0:
            yield prefix
            return
        cost = ROW_WEIGHTS[len(prefix) % 5]
        for part in range(1, min(previous, remaining // cost) + 1):
            next_repeats = repeats + 1 if part == previous else 1
            if next_repeats <= 4:
                yield from extend(prefix + (part,), remaining - cost * part, part, next_repeats)
    yield from extend((), n, n + 1, 0)

def gap_partitions(n):
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

def nonnegative_vectors(length, total, minimum=0):
    if length == 0:
        if total == 0:
            yield ()
        return
    for first in range(minimum, total // length + 1):
        for tail in nonnegative_vectors(length - 1, total - first, first):
            yield (first,) + tail

@dataclass(frozen=True, order=True)
class ClusterData:
    a: int
    b: int
    mu: tuple
    nu: tuple

    @property
    def weight(self):
        return (self.a ** 2 + 3 * self.a * self.b + 3 * self.b ** 2
                + sum(self.mu) + 3 * sum(self.nu))

    @property
    def gap_length(self):
        return self.a + 2 * self.b

def cluster_data(n):
    for a in range(isqrt(n) + 1):
        for b in range(isqrt(n // 3) + 1):
            remaining = n - (a * a + 3 * a * b + 3 * b * b)
            if remaining < 0:
                continue
            for nu_sum in range(remaining // 3 + 1):
                for mu in nonnegative_vectors(a, remaining - 3 * nu_sum):
                    for nu in nonnegative_vectors(b, nu_sum):
                        yield ClusterData(a, b, mu, nu)
