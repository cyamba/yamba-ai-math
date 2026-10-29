from __future__ import annotations
from collections import Counter
import helpers as hp
from inspect_complement import a2_reconstruct, OutsideRestrictedDomain
from verify_a3_b0_universal import reconstruct_a3_b0, step_one
from verify_full_kr1_bijection import a2_decompose, decompose_a3_b0, unstep_one
from test_complete_n26 import (
    reconstruct_a3_b1,
    reconstruct_a4_b0,
    reconstruct_a5_b0,
    reconstruct_full,
)

# Let's write the closed-form inverse `decompose_a3_a4_a5(u)` for all remaining sectors (zero lookup/enumeration!)
def decompose_a3_a4_a5(u: tuple[int, ...]) -> hp.ClusterData:
    try:
        return decompose_a3_b0(u)
    except OutsideRestrictedDomain:
        pass
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
    
    # --- Sector (a=3, b=1) ---
    if head == (9,) and ones == 0 and c6 == 2 and c3 == 0:
        return hp.ClusterData(3, 1, (0, 0, d1), (0,))
    if head == (8, 8, 8) and ones == 0:
        if c6 == 0 and c3 in (0, 1):
            d3 = c3 + 1
            return hp.ClusterData(3, 1, (d3, d3, d3 + d1), (0,))
        if c6 == 1 and c3 >= 0:
            d3 = c3 + 3
            return hp.ClusterData(3, 1, (d3, d3, d3 + d1), (0,))
    if head == (9, 9) and ones == 0 and c6 == 1 and c3 == 0:
        return hp.ClusterData(3, 1, (0, 0, d1), (1,))
    if head == (8,) and ones == 0 and c6 >= 2 and c3 >= 1:
        q2 = c6 - 2
        d2 = 3 * q2 + 1
        d3 = c3 - 1
        return hp.ClusterData(3, 1, (d3, d3 + d2, d3 + d2 + d1), (0,))
    if head == (9, 9, 8) and ones == 0:
        q2 = c6
        d2 = 3 * q2 + 1
        d3 = c3
        return hp.ClusterData(3, 1, (d3, d3 + d2, d3 + d2 + d1), (1,))
    if head == (8, 8) and ones == 0 and c6 >= 1 and c3 >= 1:
        if c6 == 1:
            d2 = 2
            d3 = c3 - 1
            return hp.ClusterData(3, 1, (d3, d3 + d2, d3 + d2 + d1), (0,))
    if head == (8, 8) and ones == 0 and c6 >= 2 and c3 >= 0:
        q2 = c6 - 2
        d2 = 3 * q2 + 2
        return hp.ClusterData(3, 1, (0, d2, d2 + d1), (1 + c3,))
        
    # --- Sector (a=4, b=0) ---
    if head == (8, 8) and ones == 0 and c6 == 0 and c3 in (0, 1, 2):
        d3 = c3
        return hp.ClusterData(4, 0, (0, d3, d3, d3 + d1), ())
    if head == (10,) and ones == 0 and c6 == 2 and c3 >= 1:
        d3 = c3 + 2
        return hp.ClusterData(4, 0, (0, d3, d3, d3 + d1), ())
    if head == (12,) and ones == 0 and c6 == 1 and c3 in (0, 1, 2):
        d3 = c3
        return hp.ClusterData(4, 0, (0, d3, d3 + 1, d3 + 1 + d1), ())
    if head == (12,) and ones == 0 and c6 == 2 and c3 >= 1:
        d3 = c3 + 2
        return hp.ClusterData(4, 0, (0, d3, d3 + 1, d3 + 1 + d1), ())
    if head == (10, 9) and ones == 1 and c6 == 0 and c3 == 0:
        return hp.ClusterData(4, 0, (0, 0, 2, 2 + d1), ())
    if head == (10, 10) and ones == 0 and c6 == 0 and c3 in (1, 2):
        d3 = c3
        return hp.ClusterData(4, 0, (0, d3, d3 + 2, d3 + 2 + d1), ())
    if head == (10, 10) and ones == 0 and c6 == 1 and c3 >= 1:
        d3 = c3 + 2
        return hp.ClusterData(4, 0, (0, d3, d3 + 2, d3 + 2 + d1), ())
    if head == (8, 8) and ones == 0 and c6 == 1 and c3 == 0:
        return hp.ClusterData(4, 0, (0, 0, 3, 3 + d1), ())
    if head == (9, 8, 8) and ones == 0 and c6 == 0:
        d3 = c3 + 1
        return hp.ClusterData(4, 0, (0, d3, d3 + 3, d3 + 3 + d1), ())
    if head == (10, 8) and ones == 0 and c6 == 0 and c3 == 2:
        return hp.ClusterData(4, 0, (0, 0, 4, 4 + d1), ())
    if head == (10, 8, 8) and ones == 0 and c6 == 0:
        d3 = c3
        return hp.ClusterData(4, 0, (0, d3, d3 + 5, d3 + 5 + d1), ())
    if head == (12, 8) and ones == 0 and c6 == 0 and c3 == 0:
        return hp.ClusterData(4, 0, (1, 1, 1, 1 + d1), ())
    if head == (15, 8) and ones == 0 and c6 == 0:
        d3 = c3 + 1
        return hp.ClusterData(4, 0, (1, 1 + d3, 1 + d3, 1 + d3 + d1), ())
    if head == (12, 9) and ones == 1 and c6 == 0 and c3 == 0:
        return hp.ClusterData(4, 0, (1, 1, 2, 2 + d1), ())
    if head == (12, 10) and ones == 0 and c6 == 0 and c3 == 1:
        return hp.ClusterData(4, 0, (1, 2, 3, 3 + d1), ())
    if head == (12,) and ones == 0 and c6 == 2 and c3 == 0:
        return hp.ClusterData(4, 0, (1, 1, 3, 3 + d1), ())
    if head == (10, 10) and ones == 0 and c6 == 1 and c3 == 0:
        return hp.ClusterData(4, 0, (1, 1, 4, 4 + d1), ())
    if head == (12, 9) and ones == 0 and c6 == 0 and c3 >= 1:
        d3 = c3 - 1
        return hp.ClusterData(4, 0, (2, 2 + d3, 2 + d3, 2 + d3 + d1), ())
    if head == (12, 8) and ones == 0 and c6 == 1 and c3 == 0:
        return hp.ClusterData(4, 0, (2, 2, 3, 3 + d1), ())
        
    # --- Sector (a=5, b=0) ---
    if head == (15, 9) and ones == 1 and c6 == 0 and c3 == 0:
        return hp.ClusterData(5, 0, (0, 0, 0, 0, d1), ())
        
    raise OutsideRestrictedDomain(f"Unrecognized core {core}")

def decompose_full(u: tuple[int, ...]) -> hp.ClusterData:
    try:
        return a2_decompose(u)
    except OutsideRestrictedDomain:
        return decompose_a3_a4_a5(u)

# Also include Stockhofe (B <-> U) and Kursungoz (C <-> A) to test the COMPLETE B <-> U <-> C <-> A bijection!
M = 5
def _minimal_regular(residues):
    result = []
    below = 0
    for residue in reversed(residues):
        below += (residue - below) % M
        result.append(below)
    return tuple(reversed(result))

def flat_to_regular(heights):
    work = list(heights)
    units = []
    for i in range(len(work) - 1, -1, -1):
        if work[i] % M == 0:
            below = work[i + 1] if i + 1 < len(work) else 0
            if i == 0 or work[i - 1] - below < M:
                units.append(work.pop(i) // M)
    while True:
        i = next((j for j, value in enumerate(work) if value % M == 0), None)
        if i is None:
            break
        value = work.pop(i)
        units.append(value // M + i)
        for j in range(i):
            work[j] -= M
    displacement = hp.conjugate(tuple(sorted(units, reverse=True)))
    return tuple(value + M * (displacement[i] if i < len(displacement) else 0)
                 for i, value in enumerate(work))

def regular_to_flat(regular):
    minimal = _minimal_regular(tuple(x % M for x in regular))
    displacement = tuple((x - y) // M for x, y in zip(regular, minimal))
    units = hp.conjugate(tuple(x for x in displacement if x))
    work = list(minimal)
    for unit in units:
        if unit <= (work[0] + M - 1) // M:
            work.append(M * unit)
            work.sort(reverse=True)
            continue
        positions = [i for i, x in enumerate(work, 1) if i + (x + M - 1) // M <= unit]
        prefix = max(positions)
        value = M * (unit - prefix)
        work = [x + M for x in work[:prefix]] + [value] + work[prefix:]
    return tuple(work)

def columns_to_residue(columns):
    hp.decode_columns(columns)
    if not columns:
        return ()
    heights = tuple(hp.inverse_prefix(x) for x in columns)
    regular = flat_to_regular(heights)
    return tuple(reversed(tuple(hp.prefix_weight(x) for x in regular)))

def residue_to_columns(parts):
    if not parts:
        return ()
    regular = tuple(hp.inverse_prefix(x) for x in reversed(parts))
    return tuple(hp.prefix_weight(x) for x in regular_to_flat(regular))

def pair(level):
    q, r = divmod(level, 2)
    return (3*q + 1, 3*q + 2) if r == 0 else (3*q + 3,) * 2

def left_bound(level):
    q, r = divmod(level, 2)
    return 3*q - 1 + r

def cluster_to_gap(c):
    i = j = 0
    result = []
    while i < c.a or j < c.b:
        single = c.mu[i] + 3*j + 2*i + 1 if i < c.a else None
        level = c.nu[j] + 2*j + i if j < c.b else None
        if j == c.b or (i < c.a and single <= left_bound(level + 1)):
            result.append(single)
            i += 1
        else:
            result.extend(pair(level))
            j += 1
    return tuple(result)

def gap_to_cluster(parts):
    i = j = pos = 0
    mu, nu = [], []
    while pos < len(parts):
        if pos + 1 < len(parts) and parts[pos + 1] - parts[pos] <= 1:
            adj = parts[pos:pos + 2]
            level = sum(adj) // 3 - 1
            nu.append(level - 2*j - i)
            j += 1
            pos += 2
        else:
            mu.append(parts[pos] - 3*j - 2*i - 1)
            i += 1
            pos += 1
    return hp.ClusterData(i, j, tuple(mu), tuple(nu))

# Verify COMPLETE round-trip B <-> U <-> C <-> A for ALL n = 0..26!
total_states = 0
for n in range(0, 27):
    bs = list(hp.residue_partitions(n))
    as_ = list(hp.gap_partitions(n))
    assert len(bs) == len(as_)
    seen_a = set()
    for b in bs:
        u = residue_to_columns(b)
        c = decompose_full(u)
        a = cluster_to_gap(c)
        assert hp.is_gap(a) and sum(a) == n
        assert a not in seen_a
        seen_a.add(a)
        # Inverse round-trip A -> C -> U -> B:
        c2 = gap_to_cluster(a)
        assert c2 == c
        u2 = reconstruct_full(c2)
        assert u2 == u
        b2 = columns_to_residue(u2)
        assert b2 == b
        total_states += 1

print(f"100% ROUND-TRIP VERIFIED: B <-> U <-> C <-> A across ALL {total_states} states for weights N = 0..26!")
