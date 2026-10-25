"""Final reserved head-family refinement: both low slabs plus delta2>=18.

The high-gap theorem is paper-only at the numerical40 boundary (minimum52).
Versions1/2, their failures and their gates remain unchanged.
"""
from collections import Counter
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location('h3_v2', Path(__file__).with_name('revision-v2-bridge.py'))
v2 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v2)
m, e, slab, y1 = v2.m, v2.e, v2.slab, v2.y1


def high_gap(c):
    return c.a == 4 and c.b == 0 and c.mu[2] - c.mu[1] >= 18


def domain(c):
    return v2.domain(c) or high_gap(c)


def high_forward(c):
    x, t, y, z = c.mu[0], c.mu[1] - c.mu[0], c.mu[2] - c.mu[1], c.mu[3] - c.mu[2]
    q, r = divmod(x, 2)
    v, s = divmod(y, 6)
    if v < 3:
        raise m.Outside('outside large second-gap domain')
    K = 6 * r + s
    if K <= 5:
        A, B = K, 0
    elif K <= 9:
        A, B = K - 6, 1
    else:
        A, B = K - 10, 2
    h = 20 + 4 * r + 2 * s - 6 * A - 10 * B
    assert h >= 0
    return m.sorted_parts(Counter({12: v - 1, 10: B, 8: q + 1, 6: A, 3: t, 1: z + h}))


def high_inverse(u):
    n, S = Counter(u), set(u)
    if S - {12, 10, 8, 6, 3, 1} or n[12] < 2 or n[8] < 1:
        raise m.Outside('outside high-gap support')
    A, B = n[6], n[10]
    if B == 0 and A <= 5:
        K = A
    elif B == 1 and A <= 3:
        K = A + 6
    elif B == 2 and A <= 1:
        K = A + 10
    else:
        raise m.Outside('invalid bounded head code')
    r, s = divmod(K, 6)
    q, v, t = n[8] - 1, n[12] + 1, n[3]
    h = 20 + 4 * r + 2 * s - 6 * A - 10 * B
    z = n[1] - h
    if z < 0:
        raise m.Outside('missing high-gap mandatory ones')
    x, y = 2 * q + r, 6 * v + s
    return m.kr1.ClusterData(4, 0, (x, x + t, x + t + y, x + t + y + z), ())


def forward(c):
    return high_forward(c) if high_gap(c) else v2.forward(c)


def inverse(u):
    m.kr1.decode_columns(u)
    try:
        return high_inverse(u)
    except m.Outside:
        return v2.inverse(u)
