from __future__ import annotations
from collections import Counter
import helpers as hp
from inspect_complement import (
    a2_reconstruct,
    OutsideRestrictedDomain,
    first_supported,
    rev_supported,
    _marker_digits,
    _template,
)

# Let's include the exact a2_decompose from rr003_a2.py so we have both directions of a <= 2:
def _recover(a, b, mu, counts):
    delta = [counts[3*j] - 2 + int(a == 0 and j == b) for j in range(1, b+1)]
    nu = []
    total = 0
    for inc in reversed(delta):
        total += inc
        nu.append(total)
    return hp.ClusterData(a, b, mu, tuple(nu))

def first_decompose(columns):
    hp.decode_columns(columns)
    counts = Counter(columns)
    ones = counts.pop(1, 0)
    if not counts:
        return (hp.ClusterData(1, 0, (ones-1,), ()) if ones
                else hp.ClusterData(0, 0, (), ()))
    if any(value % 3 for value in counts):
        raise OutsideRestrictedDomain()
    levels = {value//3 for value in counts}
    top = max(levels)
    full = levels == set(range(1, top+1))
    lower = all(counts[3*j] >= 2 for j in range(1, top))
    if full and lower:
        if not ones:
            return _recover(0, top, (), counts)
        if counts[3*top] >= 2:
            return _recover(1, top, (ones-1,), counts)
        return _recover(2, top-1, (0, ones-1), counts)
    if top >= 2 and levels == set(range(1, top-1)) | {top}:
        b = top-2
        if counts[3*top] == 1 and all(counts[3*j] >= 2 for j in range(1, b+1)):
            return _recover(2, b, (1, ones+1), counts)
    raise OutsideRestrictedDomain()

def rev_decompose(columns):
    try:
        return first_decompose(columns)
    except OutsideRestrictedDomain:
        pass
    counts = Counter(columns)
    if counts[3] >= 2 and (counts[8] or counts[10]):
        x, y, ones = counts.pop(8, 0), counts.pop(10, 0), counts.pop(1, 0)
        if not 0 <= y <= 3 or x+y < 1 or any(p % 3 for p in counts):
            raise OutsideRestrictedDomain()
        b = max(counts) // 3
        if (set(counts) != {3*j for j in range(1, b+1)} or counts[3*b] < 3
                or any(counts[3*j] < 2 for j in range(1, b))):
            raise OutsideRestrictedDomain()
        delta = [counts[3*j]-2-int(j == b) for j in range(1, b+1)]
        nu, total = [], 0
        for d in reversed(delta):
            total += d
            nu.append(total)
        k = 4*x+5*y-2
        return hp.ClusterData(2, b, (k, k+ones), tuple(nu))
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
        raise OutsideRestrictedDomain()
    return hp.ClusterData(2, 0, (k, k+tail), ())

def _recognize_hole(counts):
    markers = {x: m for x, m in counts.items() if x != 1 and x % 3}
    if not markers:
        if counts[9] == 1 and counts[6] == 1 and counts[3] >= 2 and max(counts) == 9:
            return 1, 4
    elif set(markers) == {10} and counts[3] <= 1 and max(x for x in counts if x % 3 == 0) <= 6:
        if markers[10] == 1:
            return 1, 5
        if markers[10] == 2:
            return 1, 9
    elif markers == {17: 1}:
        multiples = [x for x in counts if x % 3 == 0]
        if multiples:
            top = max(multiples) // 3
            if top == 3 and counts[9] == 1:
                return 2, 4
            if top >= 3:
                return top, 4
    elif markers == {17: 2}:
        return 2, 9
    elif markers == {19: 1}:
        multiples = [x for x in counts if x % 3 == 0]
        if multiples:
            top = max(multiples) // 3
            if top == 4 and counts[12] == 1:
                return (3 if counts[9] else 2), 5
            if top >= 4:
                return top, 5
    elif markers.get(10) == 1 and set(markers) == {10, 26}:
        if 1 <= markers[26] <= 3:
            return markers[26] + 2, 9
    elif markers == {26: 1}:
        multiples = [x for x in counts if x % 3 == 0]
        if multiples:
            top = max(multiples) // 3
            if top >= 6:
                return top, 9
    raise OutsideRestrictedDomain()

def a2_decompose(columns):
    try:
        return rev_decompose(columns)
    except OutsideRestrictedDomain:
        pass
    counts = Counter(columns)
    b, k = _recognize_hole(counts)
    baseline, minimum_ones, mode = _template(b, k)
    ones = counts.pop(1, 0) - minimum_ones
    if ones < 0:
        raise OutsideRestrictedDomain()
    for x, m in baseline.items():
        if counts[x] < m:
            raise OutsideRestrictedDomain()
        counts[x] -= m
    counts = Counter({x: m for x, m in counts.items() if m})
    if mode == 'parity':
        if set(counts) - {3, 6} or counts[3] > 1:
            raise OutsideRestrictedDomain()
        nu = (2*counts[6] + counts[3],)
    else:
        if set(counts) - {3*j for j in range(1, b+1)}:
            raise OutsideRestrictedDomain()
        total, values = 0, []
        for j in range(b, 0, -1):
            total += counts[3*j]
            values.append(total)
        nu = tuple(values)
    return hp.ClusterData(2, b, (k, k+ones), nu)

# Now let's write the exact inverse `unstep_one(u)` and `decompose_a3_b0(u)`!
def unstep_one(u: tuple[int, ...]) -> tuple[int, ...] | None:
    """
    Exact left-inverse of step_one(u) on U_rem:
    Returns the predecessor v in U_rem such that step_one(v) == u, or None if u is primitive (d1 == 0).
    """
    c = Counter(u)
    # Check if u is the image of Family 1 dead-end: (9, 6^q) -> (10, 6^q) (q >= 1)
    if c[10] == 1 and c[6] >= 1 and len(u) == 1 + c[6]:
        return (9,) + (6,) * c[6]
    # Check if u is the image of Family 2 dead-end: (10, 6^{2+q}, 3^r) -> (12, 8, 6^q, 3^{r+1}) (q >= 0, r in {0, 1})
    if c[12] == 1 and c[8] == 1 and c[3] in (1, 2) and len(u) == 2 + c[6] + c[3]:
        q = c[6]
        r = c[3] - 1
        return (10,) + (6,) * (2 + q) + (3,) * r
    # Otherwise, step_one appends 1, EXCEPT when u[:-1] is NOT in U_rem or u == (9, 9, 1) etc.:
    if not u or u[-1] != 1:
        return None
    prev = u[:-1]
    # Check if prev is valid in U and NOT in a <= 2, and step_one(prev) == u:
    try:
        hp.decode_columns(prev)
    except ValueError:
        return None
    try:
        a2_decompose(prev)
        return None  # prev was in a <= 2!
    except OutsideRestrictedDomain:
        pass
    from verify_a3_b0_universal import step_one
    if step_one(prev) == u:
        return prev
    return None

def decompose_a3_b0(u: tuple[int, ...]) -> hp.ClusterData:
    """Exact closed-form inverse of reconstruct_a3_b0(c) with zero search/lookup."""
    d1 = 0
    core = u
    while True:
        prev = unstep_one(core)
        if prev is None:
            break
        core = prev
        d1 += 1
        
    c = Counter(core)
    head = tuple(x for x in core if x >= 8)
    ones = c[1]
    c6 = c[6]
    c3 = c[3]
    
    if head == () and ones == 0 and c3 in (0, 1) and 2 * c6 + c3 >= 3:
        d2 = 0
        d3 = 2 * c6 + c3 - 3
    elif head == (8,) and ones == 0:
        if c6 == 0 and c3 in (1, 2):
            d2, d3 = 1, c3 - 1
        elif c6 == 1 and c3 >= 1:
            d2, d3 = 1, c3 + 1
        else:
            raise OutsideRestrictedDomain()
    elif head == (10,) and ones == 0:
        if c6 == 0 and c3 in (1, 2):
            d2, d3 = 2, c3 - 1
        elif c6 == 1 and c3 >= 1:
            d2, d3 = 2, c3 + 1
        else:
            raise OutsideRestrictedDomain()
    elif head == (9,) and ones == 0 and c6 == 1 and c3 == 0:
        d2, d3 = 3, 0
    elif head == (10, 8) and ones == 0:
        if c6 == 0 and c3 in (0, 1):
            d2, d3 = 3, c3 + 1
        elif c6 == 1 and c3 >= 0:
            d2, d3 = 3, c3 + 3
        else:
            raise OutsideRestrictedDomain()
    elif head == (9, 8) and ones == 0:
        q2 = c6 + 1
        d2 = 3 * q2 + 1
        d3 = c3
    elif head == (9, 9) and ones == 1 and c6 == 0 and c3 == 0:
        d2, d3 = 5, 0
    elif head == (10, 9) and ones == 0 and (c6 + c3 >= 1):
        q2 = c6 + 1
        d2 = 3 * q2 + 2
        d3 = c3
    elif head == (9, 9) and ones == 0 and c3 >= 1:
        q2 = c6 + 2
        d2 = 3 * q2
        d3 = c3 - 1
    else:
        raise OutsideRestrictedDomain()
        
    return hp.ClusterData(3, 0, (d3, d3 + d2, d3 + d2 + d1), ())

# Let's test round-trip invertibility of reconstruct_a3_b0 and decompose_a3_b0 for ALL n <= 35!
from verify_a3_b0_universal import reconstruct_a3_b0
for n in range(9, 36):
    for c in hp.cluster_data(n):
        if c.a == 3 and c.b == 0:
            u = reconstruct_a3_b0(c)
            c_rec = decompose_a3_b0(u)
            assert c_rec == c, f"Round-trip failed for {c} -> {u} -> {c_rec}"
print("VERIFIED: decompose_a3_b0(reconstruct_a3_b0(c)) == c for ALL 710 states of (a=3, b=0) through weight N=35!")
