"""RR003 recursive discovery: attributed exact encodings and a refuted insertion.

This does not implement a full KR1 bijection. No enumeration defines a map.
See rr003/recursive-discovery.md for proofs, attribution and the collision.
"""
from collections import Counter
import kr1

TAILS = ((), (1,), (1, 2), (1, 3), (2,), (3,), (3, 3))
LINKS = (frozenset(range(7)), frozenset(range(7)), frozenset(range(7)),
         frozenset((0, 4, 5, 6)), frozenset(range(7)),
         frozenset((0, 4, 5, 6)), frozenset((0, 5, 6)))


def gap_strip(parts):
    if not kr1.is_gap(parts):
        raise ValueError('expected ascending gap partition')
    tail = tuple(x for x in parts if x <= 3)
    rest = tuple(x-3 for x in parts if x > 3)
    return TAILS.index(tail), rest


def gap_unstrip(state, rest):
    if type(state) is not int or not 0 <= state < 7 or not kr1.is_gap(rest):
        raise ValueError('expected seven-tail state and actual gap residual')
    next_state = TAILS.index(tuple(x for x in rest if x <= 3))
    if next_state not in LINKS[state]:
        raise ValueError('forbidden Chern-Li linking branch')
    return TAILS[state] + tuple(x+3 for x in rest)


def residue_strip(parts):
    if not kr1.is_residue(parts):
        raise ValueError('expected ascending residue partition')
    counts = Counter(x for x in parts if x < 9)
    return tuple(counts[x] for x in (1, 3, 6, 8)), tuple(x-9 for x in parts if x > 9)


def residue_unstrip(counts, rest):
    if (not isinstance(counts, (tuple, list)) or len(counts) != 4
            or any(type(x) is not int or x < 0 for x in counts)
            or not kr1.is_residue(rest)):
        raise ValueError('expected four nonnegative counts and residue residual')
    tail = tuple(x for x, m in zip((1, 3, 6, 8), counts) for _ in range(m))
    return tail + tuple(x+9 for x in rest)


def _three_gap(parts):
    return kr1.is_gap(parts) and all(x % 3 == 0 for x in parts)


def glaisher_three(parts):
    """Classical ternary Glaisher on B parts divisible by three only."""
    if not kr1.is_residue(parts) or any(x % 3 for x in parts):
        raise ValueError('restricted endpoint requires every residue part divisible by three')
    out = []
    for part, count in Counter(parts).items():
        while count:
            count, digit = divmod(count, 3)
            out.extend([part] * digit)
            part *= 3
    return tuple(sorted(out))


def unglaisher_three(parts):
    if not _three_gap(parts):
        raise ValueError('restricted endpoint requires every gap part divisible by three')
    counts = Counter()
    for part in parts:
        copies = 1
        while part % 9 == 0:
            part //= 3
            copies *= 3
        counts[part] += copies
    return tuple(x for x in sorted(counts) for _ in range(counts[x]))


def refuted_insert_one(parts, *, capture_trace=False):
    """Preserved failed proposal; valid outputs but not an injection (weight 43).

    Start a charge 1 and ternary gap core. Single priority precedes double.
    This function must never be presented as a full or restricted bijection.
    """
    if not _three_gap(parts):
        raise ValueError('charge exploration requires a three-divisible gap core')
    counts = Counter(x//3 for x in parts)
    index, trace = 0, []
    while True:
        before = (index, tuple(sorted((j, m) for j, m in counts.items() if m)))
        if index and counts[index]:
            counts[index] -= 1
            counts[index-1] += 1
            index += 1
            rule = 'single'
        elif counts[index+1] == 2:
            counts[index+1] -= 2
            if index:
                counts[index] += 2
            index += 2
            rule = 'double'
        else:
            break
        if capture_trace:
            trace.append((rule, before,
                          (index, tuple(sorted((j, m) for j, m in counts.items() if m)))))
    result = tuple(sorted([3*index+1] + [3*j for j, m in counts.items() if j for _ in range(m)]))
    return (result, tuple(trace)) if capture_trace else result
