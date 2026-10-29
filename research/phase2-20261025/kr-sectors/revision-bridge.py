"""Single reserved refinement: coherent H3 low-b a4 carry slabs.

All initial frozen files remain unchanged. No finite matching or ranked table
defines this map. New universal assurance awaits the distinct final critic.
"""
from collections import Counter
import extension as e
import bridge as m


def slab(c):
    return c.a == 4 and c.b == 0 and c.mu[1] == c.mu[2]


def y1(c):
    return c.a == 4 and c.b == 0 and c.mu[0] == c.mu[1] and c.mu[2] == c.mu[0] + 1


def domain(c):
    return e.extended_domain(c) or slab(c) or y1(c)


def slab_forward(c):
    x, t, z = c.mu[0], c.mu[1] - c.mu[0], c.mu[3] - c.mu[2]
    q, r = divmod(x, 2)
    if r:
        return (12,) + (8,) * (q + 1) + (3,) * t + (1,) * z
    if t <= 2:
        return (8,) * (q + 2) + (3,) * t + (1,) * z
    return (12, 10) + (8,) * q + (3,) * (t - 2) + (1,) * z


def slab_inverse(u):
    n, S = Counter(u), set(u)
    if S <= {12, 8, 3, 1} and n[12] == 1 and n[8] >= 1:
        x, t, z = 2 * (n[8] - 1) + 1, n[3], n[1]
    elif S <= {8, 3, 1} and n[8] >= 2 and n[3] <= 2:
        x, t, z = 2 * (n[8] - 2), n[3], n[1]
    elif S <= {12, 10, 8, 3, 1} and n[12] == n[10] == 1 and n[3] >= 1:
        x, t, z = 2 * n[8], n[3] + 2, n[1]
    else:
        raise m.Outside('outside a4 middle-equality slab')
    return m.kr1.ClusterData(4, 0, (x, x + t, x + t, x + t + z), ())


def y1_forward(c):
    x, z = c.mu[0], c.mu[3] - c.mu[2]
    q, r = divmod(x, 2)
    if r == 0:
        return (10,) + (8,) * (q + 1) + (1,) * z
    return (12, 9) + (8,) * q + (1,) * (z + 1)


def y1_inverse(u):
    n, S = Counter(u), set(u)
    if S <= {10, 8, 1} and n[10] == 1 and n[8] >= 1:
        x, z = 2 * (n[8] - 1), n[1]
    elif S <= {12, 9, 8, 1} and n[12] == n[9] == 1 and n[1] >= 1:
        x, z = 2 * n[8] + 1, n[1] - 1
    else:
        raise m.Outside('outside a4 first-equality y1 plane')
    return m.kr1.ClusterData(4, 0, (x, x, x + 1, x + 1 + z), ())


def forward(c):
    if slab(c):
        return slab_forward(c)
    if y1(c):
        return y1_forward(c)
    return e.forward(c)


def inverse(u):
    m.kr1.decode_columns(u)
    for operation in (slab_inverse, y1_inverse, e.inverse):
        try:
            return operation(u)
        except m.Outside:
            pass
    raise m.Outside('outside H3 image')
