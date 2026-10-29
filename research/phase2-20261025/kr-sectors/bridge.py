"""Phase 2 executable transcription of RR007 H1; no ranked matching.

The two auxiliary injections and the accepted partial injection are kept
distinct. New implementation assurance is author-only until fresh review.
"""
from collections import Counter
import importlib.util
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
CHECKS = ROOT / 'research/rogers-ramanujan/checks'
sys.path.insert(0, str(CHECKS))
import kr1
import rr003_a2 as g2

spec = importlib.util.spec_from_file_location('rr007_literal', ROOT /
    'research/rogers-ramanujan/rr007/fleet-a/checks/critic-a-literal.py')
old = importlib.util.module_from_spec(spec)
spec.loader.exec_module(old)
Outside = g2.OutsideRestrictedDomain


def unpack(c):
    return c.a, c.b, c.mu, c.nu


def pack(t):
    return kr1.ClusterData(*t)


def sorted_parts(n):
    return tuple(x for x in sorted(n, reverse=True) for _ in range(n[x]))


def domain(c):
    return c.a <= 2 or c.a == 3 and c.b == 0


def retained_domain(c):
    return old.ctag(unpack(c)) is not None or c.a == 2 and c.b == 1


def b1_forward(c):
    k, s, t = c.mu[0], c.mu[1] - c.mu[0], c.nu[0]
    if k == 0:
        return (6,) + (3,) * (t + 2) + (1,) * (s + 1)
    m, r = divmod(k - 1, 3)
    if r == 0:
        M, T = m + 1, t
        ell = min(M - 1, T - 1) if T else 0
        return (9,) * (ell + 1) + (6,) * (M - ell) + (3,) * (T - ell) + (1,) * s
    if r == 1:
        return (9, 8) + (6,) * m + (3,) * t + (1,) * s
    if m or t:
        return (10, 9) + (6,) * m + (3,) * t + (1,) * s
    return (9, 9) + (1,) * (s + 1)


def b1_inverse(u):
    n, S = Counter(u), set(u)
    if S <= {9, 6, 3, 1} and n[9] >= 1 and n[6] >= 1:
        r, p, q = n[9], n[6], n[3]
        if (q == 0 and r == 1) or (q >= 1 and min(p, q) == 1):
            ell = r - 1
            M, t = p + ell, q + ell
            k, s = 3 * (M - 1) + 1, n[1]
            return kr1.ClusterData(2, 1, (k, k + s), (t,))
    if S <= {9, 8, 6, 3, 1} and n[9] == n[8] == 1:
        k, s, t = 3 * n[6] + 2, n[1], n[3]
        return kr1.ClusterData(2, 1, (k, k + s), (t,))
    if S <= {10, 9, 6, 3, 1} and n[10] == n[9] == 1 and n[6] + n[3] >= 1:
        k, s, t = 3 * n[6] + 3, n[1], n[3]
        return kr1.ClusterData(2, 1, (k, k + s), (t,))
    if S <= {9, 1} and n[9] == 2 and n[1] >= 1:
        s = n[1] - 1
        return kr1.ClusterData(2, 1, (3, 3 + s), (0,))
    raise Outside('outside new b1 phases')


def f1_forward(c):
    if c.a == 2 and c.b == 1:
        return b1_forward(c)
    return old.c_to_u(unpack(c))


def f1_inverse(u):
    kr1.decode_columns(u)
    tags = old.utags(u)
    if tags:
        if len(tags) != 1:
            raise AssertionError(('old image ambiguity', u, tags))
        return pack(old.u_to_c(u))
    return b1_inverse(u)


def g3_forward(c):
    assert c.a == 3 and c.b == 0
    x, y, z = c.mu[0], c.mu[1] - c.mu[0], c.mu[2] - c.mu[1]
    if y == 0:
        q, r = divmod(x + 3, 2)
        head = (6,) * q + (3,) * r
    elif y in (1, 2):
        marker = 8 if y == 1 else 10
        head = ((marker,) + (3,) * (x + 1) if x <= 1 else
                (marker, 6) + (3,) * (x - 1))
    elif y == 3:
        if x == 0:
            return (9, 6) if z == 0 else (10, 6) + (1,) * (z - 1)
        head = ((10, 8) + (3,) * (x - 1) if x <= 2 else
                (10, 8, 6) + (3,) * (x - 3))
    else:
        q, r = divmod(y, 3)
        if r == 1:
            head = (9, 8) + (6,) * (q - 1) + (3,) * x
        elif r == 2:
            head = ((9, 9, 1) if q == 1 and x == 0 else
                    (10, 9) + (6,) * (q - 1) + (3,) * x)
        else:
            M, T = q - 2, x + 1
            ell = min(M - 1, T - 1) if M else 0
            head = (9,) * (ell + 2) + (6,) * (M - ell) + (3,) * (T - ell)
    return head + (1,) * z


def g3_inverse(u):
    kr1.decode_columns(u)
    n, S, result = Counter(u), set(u), None
    z = n[1]
    if S <= {6, 3, 1} and n[3] <= 1 and 2 * n[6] + n[3] >= 3:
        result = 2 * n[6] + n[3] - 3, 0, z
    for marker, y in ((8, 1), (10, 2)):
        if S <= {marker, 6, 3, 1} and n[marker] == 1:
            if n[6] == 0 and n[3] in (1, 2):
                result = n[3] - 1, y, z
            if n[6] == 1 and n[3] >= 1:
                result = n[3] + 1, y, z
    if S <= {10, 6, 1} and n[10] == n[6] == 1:
        result = 0, 3, z + 1
    if u == (9, 6):
        result = 0, 3, 0
    if S <= {10, 8, 6, 3, 1} and n[10] == n[8] == 1:
        if n[6] == 0 and n[3] in (0, 1):
            result = n[3] + 1, 3, z
        if n[6] == 1:
            result = n[3] + 3, 3, z
    if S <= {9, 8, 6, 3, 1} and n[9] == n[8] == 1:
        result = n[3], 3 * (n[6] + 1) + 1, z
    if S <= {10, 9, 6, 3, 1} and n[10] == n[9] == 1 and n[6] + n[3] >= 1:
        result = n[3], 3 * (n[6] + 1) + 2, z
    if S <= {9, 1} and n[9] == 2 and n[1] >= 1:
        result = 0, 5, z - 1
    if S <= {9, 6, 3, 1} and n[9] >= 2 and n[3] >= 1:
        if n[6] == 0 and n[9] == 2:
            result = n[3] - 1, 6, z
        elif n[6] >= 1 and min(n[6], n[3]) == 1:
            ell = n[9] - 2
            result = n[3] + ell - 1, 3 * (n[6] + ell + 2), z
    if result is None:
        raise Outside('outside repaired a3,b0 image')
    x, y, z = result
    return kr1.ClusterData(3, 0, (x, x + y, x + y + z), ())


def g_forward(c):
    return g2.reconstruct_columns(c) if c.a <= 2 else g3_forward(c)


def g_inverse(u):
    try:
        return g2.decompose_columns(u)
    except Outside:
        return g3_inverse(u)


def h1_forward(c, *, steps=False):
    if not domain(c):
        raise Outside('outside H1 source domain')
    if retained_domain(c):
        value, length = f1_forward(c), 0
    else:
        value, length = g_forward(c), 1
        while True:
            try:
                old_source = f1_inverse(value)
            except Outside:
                break
            value = g_forward(old_source)
            length += 1
    return (value, length) if steps else value


def h1_inverse(u, *, steps=False):
    kr1.decode_columns(u)
    try:
        source = f1_inverse(u)
        return (source, 0) if steps else source
    except Outside:
        pass
    value, length = u, 0
    while True:
        source = g_inverse(value)
        length += 1
        if not retained_domain(source):
            return (source, length) if steps else source
        value = f1_forward(source)


def bounded_phase_forward(c):
    """Exact a3,b -> (a1,b+1 child,y,k), not a U map."""
    if c.a != 3:
        raise ValueError('a3 only')
    x, y, z = c.mu[0], c.mu[1] - c.mu[0], c.mu[2] - c.mu[1]
    q, k = divmod(x, c.b + 1)
    child = kr1.ClusterData(1, c.b + 1, (z,), (q,) + tuple(q + t for t in c.nu))
    return child, y, k


def bounded_phase_inverse(child, y, k):
    if child.a != 1 or child.b < 1 or not 0 <= k < child.b or y < 0:
        raise ValueError('invalid bounded-phase data')
    q, b = child.nu[0], child.b - 1
    x, z = child.b * q + k, child.mu[0]
    nu = tuple(t - q for t in child.nu[1:])
    return kr1.ClusterData(3, b, (x, x + y, x + y + z), nu)
