from __future__ import annotations
from collections import Counter
import helpers as hp
from inspect_complement import a2_reconstruct, OutsideRestrictedDomain

def step_one(u: tuple[int, ...]) -> tuple[int, ...]:
    c = Counter(u)
    if c[9] == 1 and c[6] >= 1 and len(u) == 1 + c[6]:
        return (10,) + (6,) * c[6]
    if c[10] == 1 and c[6] >= 2 and c[3] in (0, 1) and len(u) == 1 + c[6] + c[3]:
        q = c[6] - 2
        r = c[3]
        return (12, 8) + (6,) * q + (3,) * (r + 1)
    return u + (1,)

def reconstruct_a3_b0(c: hp.ClusterData) -> tuple[int, ...]:
    assert c.a == 3 and c.b == 0
    d3 = c.mu[0]
    d2 = c.mu[1] - c.mu[0]
    d1 = c.mu[2] - c.mu[1]
    
    # First construct the primitive core (for d1 = 0):
    if d2 == 0:
        q, r = divmod(d3 + 3, 2)
        core = (6,) * q + (3,) * r
    elif d2 == 1:
        if d3 <= 1:
            core = (8,) + (3,) * (1 + d3)
        else:
            core = (8, 6) + (3,) * (d3 - 1)
    elif d2 == 2:
        if d3 <= 1:
            core = (10,) + (3,) * (1 + d3)
        else:
            core = (10, 6) + (3,) * (d3 - 1)
    elif d2 == 3:
        if d3 == 0:
            core = (9, 6)
        elif d3 <= 2:
            core = (10, 8) + (3,) * (d3 - 1)
        else:
            core = (10, 8, 6) + (3,) * (d3 - 3)
    else:
        q2, r2 = divmod(d2, 3)
        if r2 == 1:  # d2 = 3*q2 + 1 >= 4 (q2 >= 1)
            core = (9, 8) + (6,) * (q2 - 1) + (3,) * d3
        elif r2 == 2:  # d2 = 3*q2 + 2 >= 5 (q2 >= 1)
            if q2 == 1 and d3 == 0:
                core = (9, 9, 1)
            else:
                core = (10, 9) + (6,) * (q2 - 1) + (3,) * d3
        else:  # r2 == 0, d2 = 3*q2 >= 6 (q2 >= 2)
            core = (9, 9) + (6,) * (q2 - 2) + (3,) * (1 + d3)
            
    # Apply step_one d1 times:
    u = core
    for _ in range(d1):
        u = step_one(u)
    return u

# Let's test reconstruct_a3_b0 across ALL (a=3, b=0) states up to weight N = 35!
a2_all = set()
for n in range(1, 36):
    for c in hp.cluster_data(n):
        if c.a <= 2:
            a2_all.add(a2_reconstruct(c))

seen_a3_b0 = {}
for n in range(9, 36):
    for c in hp.cluster_data(n):
        if c.a == 3 and c.b == 0:
            u = reconstruct_a3_b0(c)
            # 1. Weight check:
            assert sum(u) == n, f"Weight mismatch for {c}: {sum(u)} != {n}"
            # 2. Validity in U check:
            hp.decode_columns(u)
            # 3. Disjointness from a <= 2 check:
            assert u not in a2_all, f"Collision with a<=2 at n={n}: {c} -> {u}"
            # 4. Mutual injectivity check:
            assert u not in seen_a3_b0, f"Internal collision at n={n}: {c} and {seen_a3_b0[u]} both -> {u}"
            seen_a3_b0[u] = c

print(f"SUCCESS! Verified ALL {len(seen_a3_b0)} states of (a=3, b=0) through weight N=35: 100% valid in U, 100% weight-preserving, 100% injective, and 0 collisions with a<=2!")
