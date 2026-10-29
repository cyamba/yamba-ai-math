"""Entrywise fiber repairs and a KR1 infinite-family encoding candidate.

No target-set enumeration, ranks, used-output sets, or matching tables occur
in the forward/inverse maps. These are restricted maps, not complete KR1.
"""
from collections import Counter
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'research/rogers-ramanujan/checks'))
import kr1


def ordinary_forward(rows):
    """Standard tableaux (2,2,1^r), r>=1, into two recognized shape languages."""
    (u, v), (a, b), *singletons = rows
    tail = tuple(row[0] for row in singletons)
    if not tail:
        raise ValueError('r >= 1 is required')
    lower = [c for c in tail if v < c < b]
    if not lower:
        return ((u, v), (a,)) + tuple((c,) for c in sorted(tail + (b,)))
    c = max(lower)
    rest = tuple(t for t in tail if t != c)
    return ((u, v, b), (a, c)) + tuple((t,) for t in rest)


def ordinary_inverse(rows):
    if len(rows[0]) == 2:
        (u, v), (a,), *singletons = rows
        tail = tuple(row[0] for row in singletons)
        eligible = [b for b in tail if b > v]
        if not eligible:
            raise ValueError('outside hook image')
        b = min(eligible)
        source = ((u, v), (a, b)) + tuple((t,) for t in tail if t != b)
    elif len(rows[0]) == 3:
        (u, v, b), (a, c), *singletons = rows
        tail = tuple(row[0] for row in singletons)
        if not v < c < b or any(c < t < b for t in tail):
            raise ValueError('outside rotated image')
        source = ((u, v), (a, b)) + tuple((t,) for t in sorted(tail + (c,)))
    else:
        raise ValueError('outside image shapes')
    if ordinary_forward(source) != rows:
        raise ValueError('outside exact image')
    return source


def middle_parameters(c):
    if c.a != 4 or c.b != 0:
        raise ValueError('expected a4,b0')
    x, t, y, z = c.mu[0], c.mu[1]-c.mu[0], c.mu[2]-c.mu[1], c.mu[3]-c.mu[2]
    if not 2 <= y <= 17:
        raise ValueError('expected middle band')
    k = (2*y + 6) // 3  # ceil((2y+4)/3)
    q, r = divmod(x, 3)
    if q < k:
        raise ValueError('common width below funded threshold')
    return x, t, y, z, k, q, r


def middle_forward(c):
    """Candidate covering every t,z when x>=3*ceil((2y+4)/3), 2<=y<=17."""
    x, t, y, z, k, q, r = middle_parameters(c)
    h = 12*k - 8*y - 12 - 2*r
    assert h >= 0
    n = {12:q-k, 10:y+2, 8:1, 6:r, 3:t, 1:z+h}
    return tuple(p for p in sorted(n, reverse=True) for _ in range(n[p]))


def middle_inverse(u):
    kr1.decode_columns(u)
    n = Counter(u)
    if set(n) - {12,10,8,6,3,1} or n[8] != 1 or not 4 <= n[10] <= 19 or n[6] > 2:
        raise ValueError('outside middle-band image language')
    y, r = n[10]-2, n[6]
    k = (2*y + 6) // 3
    q = n[12]+k
    h = 12*k - 8*y - 12 - 2*r
    z = n[1]-h
    if z < 0:
        raise ValueError('missing mandatory ones')
    x, t = 3*q+r, n[3]
    return kr1.ClusterData(4, 0, (x,x+t,x+t+y,x+t+y+z), ())


def y2_forward(c):
    """Candidate for the ENTIRE first missing slab y=2, all x,t,z>=0."""
    if c.a != 4 or c.b != 0 or c.mu[2]-c.mu[1] != 2:
        raise ValueError('expected a4,b0,y2')
    x, t, z = c.mu[0], c.mu[1]-c.mu[0], c.mu[3]-c.mu[2]
    q, r = divmod(x, 2)
    if r:
        n = {8:q+2, 6:1, 3:t, 1:z+2}
    elif q:
        n = {8:q+1, 6:2, 3:t, 1:z}
    elif t == 0:
        n = {10:1, 9:1, 1:z+1}
    elif t == 1:
        n = {10:2, 3:1, 1:z}
    elif t in (2,3) and z >= 5:
        n = {10:1, 9:2, 3:t-2, 1:z-2}
    else:
        n = {10:2, 6:1, 3:t-2, 1:z}
    return tuple(p for p in sorted(n, reverse=True) for _ in range(n[p]))


def y2_inverse(u):
    kr1.decode_columns(u)
    n, S = Counter(u), set(u)
    if S <= {8,6,3,1} and n[8] >= 2 and n[6] == 2:
        x, t, z = 2*(n[8]-1), n[3], n[1]
    elif S <= {8,6,3,1} and n[8] >= 2 and n[6] == 1 and n[1] >= 2:
        x, t, z = 2*(n[8]-2)+1, n[3], n[1]-2
    elif S <= {10,9,1} and n[10] == n[9] == 1 and n[1] >= 1:
        x, t, z = 0, 0, n[1]-1
    elif S <= {10,3,1} and n[10] == 2 and n[3] == 1:
        x, t, z = 0, 1, n[1]
    elif S <= {10,6,3,1} and n[10] == 2 and n[6] == 1:
        x, t, z = 0, n[3]+2, n[1]
        if t in (2,3) and z >= 5:
            raise ValueError('carried tail belongs to a different language')
    elif S <= {10,9,3,1} and n[10] == 1 and n[9] == 2 and n[3] <= 1 and n[1] >= 3:
        x, t, z = 0, n[3]+2, n[1]+2
    else:
        raise ValueError('outside y2 image')
    return kr1.ClusterData(4, 0, (x,x+t,x+t+2,x+t+2+z), ())
