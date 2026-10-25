"""Explicit local partial cancellation; no used set or global enumeration.

T(5,1) + T(4,2) -> T(4,1,1) + T(3,2,1) + 2 T(6).
The same weighted-set formulas extend to arm length >=4. Only n=6 is tested.
Tags distinguish both literal determinant copies of T(6).
Also incorporates a disjoint conditional three-label rotation from T(2,2,1,1).
"""
from __future__ import annotations
from inventory import tb


def lt(h, a, b):
    return tb.lt_p(h, a, b)


def incomparable(h, a, b):
    return not lt(h, a, b) and not lt(h, b, a)


def triangle_conditions(h, u, v, a, b, c, d):
    return (c < v < b and lt(h, u, v) and lt(h, u, c) and
            lt(h, a, c) and lt(h, c, b) and lt(h, a, v) and
            incomparable(h, c, v) and incomparable(h, b, v) and
            not lt(h, a, u) and not lt(h, d, b) and not lt(h, d, c))


def triangle_source(h, rows):
    """Returns intrinsic branch tag, or None off the conditional subdomain."""
    if tuple(map(len, rows)) != (2, 2, 1, 1):
        return None
    (u, v), (a, w), (z,), (d,) = rows
    if triangle_conditions(h, u, v, a, z, w, d):
        return 'triangle0'
    if triangle_conditions(h, u, v, a, w, z, d):
        return 'triangle1'
    return None


def forward(h, source_tag, rows):
    if source_tag in ('triangle0', 'triangle1'):
        if triangle_source(h, rows) != source_tag:
            raise ValueError('not in the conditional triangle subdomain')
        (u, v), (a, w), (z,), (d,) = rows
        if source_tag == 'triangle0':
            c, b = w, z
            return ('21111', ((u, v), (a,), (c,), (b,), (d,)))
        b, c = w, z
        return ('321', ((u, c, b), (a, v), (d,)))
    arm = rows[0]
    if source_tag == 'hook':
        y, z, x = arm[-1], rows[1][0], arm[-2]
        prefix = arm[:-1]
        if lt(h, x, z) and (lt(h, z, y) or lt(h, y, z)):
            if lt(h, z, y):
                return ('row0', (prefix + (z, y),))
            return ('row1', (prefix + (y, z),))
        leg = (z, y) if lt(h, z, y) else (y, z)
        return ('411', (prefix, (leg[0],), (leg[1],)))
    if source_tag != 'two':
        raise ValueError('source tag must be hook or two')
    a, b = rows[1]
    x = arm[-1]
    if not (lt(h, x, b) and not lt(h, x, a)):
        return ('411', (arm, (a,), (b,)))
    if lt(h, a, x):
        return ('321', (arm[:-1], (a, x), (b,)))
    w = arm[-2]
    return ('321', (arm[:-2] + (b,), (w, x), (a,)))


def inverse(h, output_tag, rows):
    """Intrinsic image recognition, using only entries and P-comparisons."""
    if output_tag in ('row0', 'row1'):
        if len(rows) != 1:
            return None
        chain = rows[0]
        if output_tag == 'row0':
            return ('hook', (chain[:-2] + (chain[-1],), (chain[-2],)))
        return ('hook', (chain[:-1], (chain[-1],)))
    if output_tag == '411':
        if len(rows) != 3 or len(rows[1]) != 1 or len(rows[2]) != 1:
            return None
        arm, (s,), (t,) = rows
        x, v = arm[-1], arm[1]
        if lt(h, s, t) and lt(h, x, t) and not lt(h, x, s):
            return ('hook', (arm + (t,), (s,)))
        if lt(h, x, s) and incomparable(h, s, t):
            return ('hook', (arm + (s,), (t,)))
        if lt(h, s, t) and not lt(h, t, v) and not (
                lt(h, x, t) and not lt(h, x, s)):
            return ('two', (arm, (s, t)))
        return None
    if output_tag == '321':
        if len(rows) != 3 or len(rows[1]) != 2 or len(rows[2]) != 1:
            return None
        arm, (s, t), (z,) = rows
        if lt(h, arm[-1], t) and lt(h, t, z):
            return ('two', (arm + (t,), (s, z)))
        if (lt(h, arm[-2], s) and lt(h, t, arm[-1]) and
                lt(h, z, arm[-1]) and incomparable(h, z, t)):
            return ('two', (arm[:-1] + (s, t), (z, arm[-1])))
        if len(arm) == 3:
            u, c, b = arm
            a, v, d = s, t, z
            if triangle_conditions(h, u, v, a, b, c, d):
                return ('triangle1', ((u, v), (a, b), (c,), (d,)))
        return None
    if output_tag == '21111':
        if tuple(map(len, rows)) != (2, 1, 1, 1, 1):
            return None
        (u, v), (a,), (c,), (b,), (d,) = rows
        if triangle_conditions(h, u, v, a, b, c, d):
            return ('triangle0', ((u, v), (a, c), (b,), (d,)))
        return None
    return None


def destination_shape(n, tag):
    return {'row0': (n,), 'row1': (n,), '411': (n-2, 1, 1),
            '321': (n-3, 2, 1), '21111': (2, 1, 1, 1, 1)}[tag]
