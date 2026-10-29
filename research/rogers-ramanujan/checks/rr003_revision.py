"""RR003 round-two extension: mixed markers, all a=2,b=0 and the frozen first domain.

No enumeration or ranking in either map. Proof: rr003/round-2-proposal.md.
"""
from collections import Counter
import kr1
import rr003_columns as first

OutsideRestrictedDomain = first.OutsideRestrictedDomain


def supported(c):
    return first.supported(c) or (isinstance(c, kr1.ClusterData) and c.a == 2
                                   and (c.b == 0 or _marker_digits(c.mu[0]) is not None))


def _marker_digits(k):
    # k+2 = 4*x+5*y, with 0<=y<=3. These are literal column multiplicities.
    y = (k+2) % 4
    x = (k+2-5*y) // 4
    return (x, y) if x >= 0 and x+y >= 1 else None


def reconstruct_columns(c):
    if first.supported(c):
        return first.reconstruct_columns(c)
    if not supported(c):
        raise OutsideRestrictedDomain('unresolved: a>=3 or mixed common increment k in {4,5,9}')
    k, v = c.mu
    if c.b:
        x, y = _marker_digits(k)
        delta = [c.nu[c.b-j] - (c.nu[c.b-j-1] if j < c.b else 0)
                 for j in range(1, c.b+1)]
        counts = Counter({3*j:2+d for j, d in enumerate(delta, 1)})
        counts[3*c.b] += 1
        counts[8], counts[10], counts[1] = x, y, v-k
        return tuple(p for p in sorted(counts, reverse=True) for _ in range(counts[p]))
    quotient, residue = divmod(k-2, 3)
    tail = v-k
    if residue == 0:
        carrier, ones = (8,), tail
    elif residue == 1:
        carrier, ones = (9,), tail+1
    else:
        carrier, ones = (9, 3), tail
    return tuple(sorted(carrier + (6,)*quotient + (1,)*ones, reverse=True))


def decompose_columns(columns):
    # The first map validates literal U even when it reports unsupported.
    try:
        return first.decompose_columns(columns)
    except OutsideRestrictedDomain:
        pass
    counts = Counter(columns)
    # Mixed images have isolated non-three markers, and at least two 3s.
    if counts[3] >= 2 and (counts[8] or counts[10]):
        x, y, ones = counts.pop(8, 0), counts.pop(10, 0), counts.pop(1, 0)
        if not 0 <= y <= 3 or x+y < 1 or any(p % 3 for p in counts):
            raise OutsideRestrictedDomain('invalid mixed marker pattern')
        b = max(counts) // 3
        if (set(counts) != {3*j for j in range(1, b+1)} or counts[3*b] < 3
                or any(counts[3*j] < 2 for j in range(1, b))):
            raise OutsideRestrictedDomain('mixed baseline not recognized')
        delta = [counts[3*j]-2-int(j == b) for j in range(1, b+1)]
        nu, total = [], 0
        for d in reversed(delta):
            total += d
            nu.append(total)
        k = 4*x+5*y-2
        return kr1.ClusterData(2, b, (k, k+ones), tuple(nu))
    counts = Counter(columns)
    ones = counts.pop(1, 0)
    sixes = counts.pop(6, 0)
    if counts == Counter({8: 1}):
        k, tail = 3*sixes+2, ones
    elif counts == Counter({9: 1}) and ones >= 1:
        k, tail = 3*sixes+3, ones-1
    elif counts == Counter({9: 1, 3: 1}):
        k, tail = 3*sixes+4, ones
    else:
        raise OutsideRestrictedDomain('valid U outside the revised restricted image')
    return kr1.ClusterData(2, 0, (k, k+tail), ())


def raise_common_zero_b(c):
    if not isinstance(c, kr1.ClusterData) or c.a != 2 or c.b != 0:
        raise ValueError('common carry proved only for a=2,b=0')
    return kr1.ClusterData(2, 0, tuple(x+1 for x in c.mu), ())


def lower_common_zero_b(c):
    if not isinstance(c, kr1.ClusterData) or c.a != 2 or c.b != 0 or c.mu[0] == 0:
        raise ValueError('inverse common carry needs a=2,b=0,mu[0]>0')
    return kr1.ClusterData(2, 0, tuple(x-1 for x in c.mu), ())


def _replace(columns, removed, added):
    counts = Counter(columns)
    for x in removed:
        if counts[x] <= 0:
            raise ValueError('carry rule attempted to remove an absent column')
        counts[x] -= 1
    counts.update(added)
    return tuple(x for x in sorted(counts, reverse=True) for _ in range(counts[x]))


def raise_common_columns(columns):
    c = decompose_columns(columns)
    if c.a != 2 or c.b != 0:
        raise ValueError('common carry proved only for a=2,b=0')
    k = c.mu[0]
    if k == 0:
        removed, added = (3, 1), (6,)
    elif k == 1:
        removed, added = (6,), (8,)
    else:
        residue = (k-2) % 3
        removed, added = (((8,), (9, 1)), ((1,), (3,)), ((9, 3), (8, 6)))[residue]
    return _replace(columns, removed, added)


def lower_common_columns(columns):
    c = decompose_columns(columns)
    if c.a != 2 or c.b != 0 or c.mu[0] == 0:
        raise ValueError('inverse common carry needs a=2,b=0,mu[0]>0')
    k = c.mu[0]
    if k == 1:
        removed, added = (6,), (3, 1)
    elif k == 2:
        removed, added = (8,), (6,)
    else:
        residue = (k-2) % 3
        removed, added = (((8, 6), (9, 3)), ((9, 1), (8,)), ((3,), (1,)))[residue]
    return _replace(columns, removed, added)


def raise_common_mixed_columns(columns):
    c = decompose_columns(columns)
    if c.a != 2 or c.b == 0:
        raise ValueError('mixed common carry needs a=2,b>0')
    if c.mu[0] == 0:
        return _replace(columns, (3*(c.b+1), 1), (3*(c.b+2),))
    if c.mu[0] == 1:
        return _replace(columns, (3*(c.b+2),), (3*c.b, 8))
    x, y = _marker_digits(c.mu[0])
    if y == 3:
        return _replace(columns, (10,)*3, (8,)*4)
    if x > 0:
        return _replace(columns, (8,), (10,))
    raise OutsideRestrictedDomain('next common increment is one of the unresolved 4,5,9')


def lower_common_mixed_columns(columns):
    c = decompose_columns(columns)
    if c.a != 2 or c.b == 0 or c.mu[0] == 0:
        raise ValueError('mixed inverse carry needs a=2,b>0,mu[0]>0')
    if c.mu[0] == 1:
        return _replace(columns, (3*(c.b+2),), (3*(c.b+1), 1))
    if c.mu[0] == 2:
        return _replace(columns, (3*c.b, 8), (3*(c.b+2),))
    if _marker_digits(c.mu[0]-1) is None:
        raise OutsideRestrictedDomain('preceding common increment outside marker domain')
    x, y = _marker_digits(c.mu[0])
    if y:
        return _replace(columns, (10,), (8,))
    return _replace(columns, (8,)*4, (10,)*3)
