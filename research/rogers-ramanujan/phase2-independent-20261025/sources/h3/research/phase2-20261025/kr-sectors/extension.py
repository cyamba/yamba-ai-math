"""H-family version 2: explicit new planes and a full large-b sector tail.

The large-b construction has a written universal argument; it is deliberately
not instantiated above the numerical40 boundary. No table or ranking occurs.
"""
from collections import Counter
from math import gcd, prod

import bridge as m

COINS = {2: 8, 3: 10, 4: 17, 5: 19}
BIT_COINS = (35, 37, 44, 46, 53, 55, 62, 64, 71, 73, 80, 82, 89, 91)


def radices(a):
    return tuple(COINS[j] // gcd(j, COINS[j]) for j in range(2, a + 1))


def width(a):
    return (prod(radices(a)) - 1).bit_length()


def tail_threshold(a):
    overhead = 28 * (a - 2) + sum(BIT_COINS[:width(a)])
    return max(31, (overhead - a * a + 3 * (a - 1) - 1) // (3 * (a - 1)))


def plane(c):
    return c.a in (4, 5) and c.b == 0 and len(set(c.mu[:-1])) == 1


def tail(c):
    return c.a in (3, 4, 5) and c.b >= tail_threshold(c.a)


def extended_domain(c):
    return m.domain(c) or plane(c) or tail(c)


def plane_forward(c):
    x, z = c.mu[0], c.mu[-1] - c.mu[0]
    q, r = divmod(x, 2)
    if c.a == 4:
        return ((8,) * (q + 2) + (1,) * z if r == 0 else
                (12,) + (8,) * (q + 1) + (1,) * z)
    return ((15,) + (10,) * q + (9,) + (1,) * (z + 1) if r == 0 else
            (17,) + (10,) * q + (9, 3) + (1,) * (z + 1))


def plane_inverse(u):
    n, S = Counter(u), set(u)
    if S <= {8, 1} and n[8] >= 2:
        a, x, z = 4, 2 * (n[8] - 2), n[1]
    elif S <= {12, 8, 1} and n[12] == 1 and n[8] >= 1:
        a, x, z = 4, 2 * (n[8] - 1) + 1, n[1]
    elif S <= {15, 10, 9, 1} and n[15] == n[9] == 1 and n[1] >= 1:
        a, x, z = 5, 2 * n[10], n[1] - 1
    elif S <= {17, 10, 9, 3, 1} and n[17] == n[9] == n[3] == 1 and n[1] >= 1:
        a, x, z = 5, 2 * n[10] + 1, n[1] - 1
    else:
        raise m.Outside('outside new a4/a5 planes')
    return m.kr1.ClusterData(a, 0, (x,) * (a - 1) + (x + z,), ())


def gaps(v):
    return {j: v[len(v) - j] - (v[len(v) - j - 1] if j < len(v) else 0)
            for j in range(1, len(v) + 1)}


def from_gaps(d, length):
    out, total = [], 0
    for j in range(length, 0, -1):
        total += d[j]
        out.append(total)
    return tuple(out)


def tail_forward(c):
    if not tail(c):
        raise m.Outside('outside large-b domain')
    ds, ns = gaps(c.mu), gaps(c.nu)
    n = Counter({3 * j: 2 + ns[j] for j in range(1, c.b + 1)})
    n[28] = c.a - 2
    residue_weight = phase = 0
    factor = 1
    for j in range(2, c.a + 1):
        d, t = COINS[j] // gcd(j, COINS[j]), j // gcd(j, COINS[j])
        q, r = divmod(ds[j], d)
        n[COINS[j]] = t * q
        residue_weight += j * r
        phase += factor * r
        factor *= d
    for i, coin in enumerate(BIT_COINS[:width(c.a)]):
        n[coin] = (phase >> i) & 1
    head = 28 * (c.a - 2) + sum(coin * n[coin] for coin in BIT_COINS[:width(c.a)])
    h = c.a * c.a + 3 * (c.a - 1) * c.b + residue_weight - head
    assert h >= 0
    n[1] = ds[1] + h
    return m.sorted_parts(n)


def tail_inverse(u):
    n, S = Counter(u), set(u)
    a = n[28] + 2
    if a not in (3, 4, 5):
        raise m.Outside('missing large-b guard')
    allowed = {1, 28} | {COINS[j] for j in range(2, a + 1)} | set(BIT_COINS[:width(a)])
    multiples = [x for x in S if x % 3 == 0]
    b = max(multiples, default=0) // 3
    if b < tail_threshold(a) or S - allowed - {3 * j for j in range(1, b + 1)}:
        raise m.Outside('invalid tail support/dimension')
    if any(n[3 * j] < 2 for j in range(1, b + 1)):
        raise m.Outside('missing full nu contour')
    if any(n[coin] > 1 for coin in BIT_COINS[:width(a)]):
        raise m.Outside('nonbinary residue marker')
    phase = sum(n[coin] << i for i, coin in enumerate(BIT_COINS[:width(a)]))
    if phase >= prod(radices(a)):
        raise m.Outside('unused phase word')
    ds, residue_weight = {}, 0
    for j in range(2, a + 1):
        d, t = COINS[j] // gcd(j, COINS[j]), j // gcd(j, COINS[j])
        phase, r = divmod(phase, d)
        if n[COINS[j]] % t:
            raise m.Outside('quotient marker divisibility')
        ds[j] = d * (n[COINS[j]] // t) + r
        residue_weight += j * r
    assert phase == 0
    head = 28 * (a - 2) + sum(coin * n[coin] for coin in BIT_COINS[:width(a)])
    h = a * a + 3 * (a - 1) * b + residue_weight - head
    ds[1] = n[1] - h
    if ds[1] < 0:
        raise m.Outside('missing mandatory ones')
    ns = {j: n[3 * j] - 2 for j in range(1, b + 1)}
    return m.kr1.ClusterData(a, b, from_gaps(ds, a), from_gaps(ns, b))


def auxiliary_forward(c):
    if m.domain(c):
        return m.g_forward(c)
    if plane(c):
        return plane_forward(c)
    return tail_forward(c)


def auxiliary_inverse(u):
    m.kr1.decode_columns(u)
    for inverse in (m.g_inverse, plane_inverse, tail_inverse):
        try:
            return inverse(u)
        except m.Outside:
            pass
    raise m.Outside('outside extended auxiliary image')


def forward(c, *, steps=False):
    if not extended_domain(c):
        raise m.Outside('outside H2 domain')
    if m.domain(c):
        value, length = m.h1_forward(c), 0
    else:
        value, length = auxiliary_forward(c), 1
        while True:
            try:
                old_source = m.h1_inverse(value)
            except m.Outside:
                break
            value = auxiliary_forward(old_source)
            length += 1
    return (value, length) if steps else value


def inverse(u, *, steps=False):
    m.kr1.decode_columns(u)
    try:
        source = m.h1_inverse(u)
        return (source, 0) if steps else source
    except m.Outside:
        pass
    value, length = u, 0
    while True:
        source = auxiliary_inverse(value)
        length += 1
        if not m.domain(source):
            return (source, length) if steps else source
        value = m.h1_forward(source)
