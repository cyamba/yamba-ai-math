from __future__ import annotations
from collections import Counter, defaultdict
import helpers as hp

# Let's include the exact functions from rr003_columns, rr003_revision, and rr003_a2
class OutsideRestrictedDomain(ValueError):
    pass

def first_supported(c):
    return c.a <= 1 or (c.a == 2 and c.mu[0] <= 1)

def first_reconstruct(c):
    if not first_supported(c):
        raise OutsideRestrictedDomain()
    delta = [c.nu[c.b-j] - (c.nu[c.b-j-1] if j < c.b else 0)
             for j in range(1, c.b+1)]
    counts = Counter()
    for j, inc in enumerate(delta, 1):
        counts[3*j] = 2 + inc - int(c.a == 0 and j == c.b)
    if c.a == 1:
        counts[1] = 1 + c.mu[0]
    elif c.a == 2 and c.mu[0] == 0:
        counts[3*(c.b+1)] += 1
        counts[1] = 1 + c.mu[1]
    elif c.a == 2:
        counts[3*(c.b+2)] += 1
        counts[1] = c.mu[1] - 1
    return tuple(x for x in sorted(counts, reverse=True) for _ in range(counts[x]))

def _marker_digits(k):
    y = (k+2) % 4
    x = (k+2-5*y) // 4
    return (x, y) if x >= 0 and x+y >= 1 else None

def rev_supported(c):
    return first_supported(c) or (c.a == 2 and (c.b == 0 or _marker_digits(c.mu[0]) is not None))

def rev_reconstruct(c):
    if first_supported(c):
        return first_reconstruct(c)
    if not rev_supported(c):
        raise OutsideRestrictedDomain()
    k, v = c.mu
    if c.b:
        x, y = _marker_digits(k)
        delta = [c.nu[c.b-j] - (c.nu[c.b-j-1] if j < c.b else 0)
                 for j in range(1, c.b+1)]
        counts = Counter({3*j: 2+d for j, d in enumerate(delta, 1)})
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

def _template(b, k):
    if k == 4:
        if b == 1:
            return Counter({9:1,6:1,3:2}), 0, 'ordinary'
        if b == 2:
            return Counter({17:1,9:1,6:1,3:1}), 1, 'ordinary'
        counts=Counter({3*j:2 for j in range(1,b+1)})
        counts[3*(b-2)] += 1
        counts[17] += 1
        return counts, 1, 'ordinary'
    if k == 5:
        if b == 1:
            return Counter({10:1,6:2}), 1, 'parity'
        if b == 2:
            return Counter({19:1,12:1,6:1}), 1, 'ordinary'
        if b == 3:
            return Counter({19:1,12:1,9:1,6:2,3:2}), 1, 'ordinary'
        counts=Counter({3*j:2 for j in range(1,b+1)})
        counts[3*(b-2)] += 1
        counts[19] += 1
        return counts, 1, 'ordinary'
    if k == 9:
        if b == 1:
            return Counter({10:2,6:1}), 5, 'parity'
        if b == 2:
            return Counter({17:2,9:1,3:1}), 0, 'ordinary'
        if b <= 5:
            return Counter({26:b-2,18:1,10:1,3:1}), {3:10,4:11,5:18}[b], 'ordinary'
        counts=Counter({3*j:2 for j in range(1,b+1)})
        counts[3*(b-2)] += 1
        counts[26] += 1
        return counts, 2, 'ordinary'
    raise ValueError()

def a2_reconstruct(c):
    if rev_supported(c):
        return rev_reconstruct(c)
    if c.a > 2:
        raise OutsideRestrictedDomain()
    k, v = c.mu
    counts, minimum_ones, mode = _template(c.b, k)
    if mode == 'parity':
        quotient, residue = divmod(c.nu[0], 2)
        counts[6] += quotient
        counts[3] += residue
    else:
        for j in range(1, c.b+1):
            counts[3*j] += c.nu[c.b-j] - (c.nu[c.b-j-1] if j < c.b else 0)
    counts[1] += minimum_ones + v - k
    return tuple(x for x in sorted(counts, reverse=True) for _ in range(counts[x]))

for n in range(9, 21):
    cs = list(hp.cluster_data(n))
    us = sorted(hp.weighted_columns(w) for w in hp.weighted_partitions(n))
    a2_cs = [c for c in cs if c.a <= 2]
    a3_cs = [c for c in cs if c.a >= 3]
    a2_imgs = {a2_reconstruct(c) for c in a2_cs}
    rem_us = [u for u in us if u not in a2_imgs]
    print(f"=== Weight n={n}: |C(a>=3)| = {len(a3_cs)}, |U_rem| = {len(rem_us)} ===")
    for c, u in zip(a3_cs, rem_us):
        print(f"  C: a={c.a} b={c.b} mu={c.mu} nu={c.nu}  |  U: {u}")
