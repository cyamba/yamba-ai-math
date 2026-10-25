"""Exact all-b dimension reductions, independent of any U bridge."""
import bridge as m
from extension import gaps, from_gaps


def forward(c):
    if c.a not in (3, 4, 5):
        raise ValueError('a in {3,4,5} required')
    ds = gaps(c.mu)
    B = c.b + 1
    q, k = divmod(ds[3], B)
    nu = (q,) + tuple(q + t for t in c.nu)
    if c.a == 3:
        child = m.kr1.ClusterData(1, B, (ds[1],), nu)
        boundary = (ds[2], k)
        excess = 2 + 2 * ds[2] + 3 * k
    elif c.a == 4:
        child = m.kr1.ClusterData(2, B, (ds[2], ds[2] + ds[1]), nu)
        boundary = (ds[4], k)
        excess = 3 + 4 * ds[4] + 3 * k
    else:
        t, r = divmod(ds[4], 3)
        mu = (4 * t, 4 * t + ds[2], 4 * t + ds[2] + ds[1])
        child = m.kr1.ClusterData(3, B, mu, nu)
        boundary = (ds[5], r, k)
        excess = 4 + 5 * ds[5] + 4 * r + 3 * k
    return child, boundary, excess


def inverse(child, boundary):
    a, b = child.a + 2, child.b - 1
    if a not in (3, 4, 5) or b < 0:
        raise ValueError('invalid child dimension')
    q = child.nu[0]
    nu = tuple(t - q for t in child.nu[1:])
    ds = gaps(child.mu)
    if a == 3:
        y, k = boundary
        parent_gaps = {1: ds[1], 2: y, 3: (b + 1) * q + k}
    elif a == 4:
        x, k = boundary
        parent_gaps = {1: ds[1], 2: ds[2], 3: (b + 1) * q + k, 4: x}
    else:
        x, r, k = boundary
        if ds[3] % 4 or not 0 <= r < 3:
            raise ValueError('invalid a5 child phase')
        parent_gaps = {1: ds[1], 2: ds[2], 3: (b + 1) * q + k,
                       4: 3 * (ds[3] // 4) + r, 5: x}
    if not 0 <= k <= b or any(v < 0 for v in parent_gaps.values()):
        raise ValueError('invalid boundary')
    return m.kr1.ClusterData(a, b, from_gaps(parent_gaps, a), nu)
