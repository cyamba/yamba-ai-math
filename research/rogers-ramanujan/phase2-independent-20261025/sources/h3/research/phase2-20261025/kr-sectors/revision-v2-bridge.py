"""Reserved H-family refinement, broadened to both full delta2=0/1 slabs.

Version1 and its checks are preserved. The new carry keeps every version1
assignment unchanged. New assurance is author-only until final review.
"""
from collections import Counter
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location('h3_v1', Path(__file__).with_name('revision-bridge.py'))
v1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v1)
m, e, slab = v1.m, v1.e, v1.slab


def y1(c):
    """Name retained for check interface; now all delta3, with delta2=1."""
    return c.a == 4 and c.b == 0 and c.mu[2] == c.mu[1] + 1


def domain(c):
    return e.extended_domain(c) or slab(c) or y1(c)


def y1_forward(c):
    x, t, z = c.mu[0], c.mu[1] - c.mu[0], c.mu[3] - c.mu[2]
    q, r = divmod(x, 2)
    if r:
        return (12, 9) + (8,) * q + (3,) * t + (1,) * (z + 1)
    if t <= 2:
        return (10,) + (8,) * (q + 1) + (3,) * t + (1,) * z
    # Sorted order puts any8s between9 and6.
    return (12, 9) + (8,) * q + (6,) + (3,) * (t - 3) + (1,) * z


def y1_inverse(u):
    n, S = Counter(u), set(u)
    if S <= {12, 9, 8, 3, 1} and n[12] == n[9] == 1 and n[1] >= 1:
        x, t, z = 2 * n[8] + 1, n[3], n[1] - 1
    elif S <= {10, 8, 3, 1} and n[10] == 1 and n[8] >= 1 and n[3] <= 2:
        x, t, z = 2 * (n[8] - 1), n[3], n[1]
    elif S <= {12, 9, 8, 6, 3, 1} and n[12] == n[9] == n[6] == 1:
        x, t, z = 2 * n[8], n[3] + 3, n[1]
    else:
        raise m.Outside('outside a4 delta2=1 slab')
    return m.kr1.ClusterData(4, 0, (x, x + t, x + t + 1, x + t + 1 + z), ())


def forward(c):
    if slab(c):
        return v1.slab_forward(c)
    if y1(c):
        return y1_forward(c)
    return e.forward(c)


def inverse(u):
    m.kr1.decode_columns(u)
    for operation in (v1.slab_inverse, y1_inverse, e.inverse):
        try:
            return operation(u)
        except m.Outside:
            pass
    raise m.Outside('outside H3 version2 image')
