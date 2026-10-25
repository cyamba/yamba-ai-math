from __future__ import annotations
import sys
from collections import Counter

sys.path.insert(0, "/Users/christopheryamba/YambaCode/Math/yamba-ai-math-rogers-ramanujan/research/rogers-ramanujan/checks")
import kr1, rr003_a2, rr004_multidim_cones as rr4
from inspect_phase2_gaps import reconstruct_a3_b0_univ

# Compute U_rem2[n] = U[n] \ (Im(a<=2) U Im(a=3, b=0)) for n = 0..40
u_rem2 = {}
c_rem2 = {}
for n in range(0, 41):
    us = set(kr1.weighted_columns(w) for w in kr1.weighted_partitions(n))
    cs = list(kr1.cluster_data(n))
    used_u = set()
    rem_c = []
    for c in cs:
        if c.a <= 2:
            used_u.add(rr003_a2.reconstruct_columns(c))
        elif c.a == 3 and c.b == 0:
            used_u.add(reconstruct_a3_b0_univ(c))
        else:
            rem_c.append(c)
    u_rem2[n] = sorted(us - used_u)
    c_rem2[n] = rem_c
    assert len(u_rem2[n]) == len(c_rem2[n])

# Now check how many primitive C states (d1 = mu[-1] - mu[-2] == 0) exist at each n!
for n in range(21, 41):
    prim_c = [c for c in c_rem2[n] if c.mu[-1] == c.mu[-2]]
    print(f"n={n:2d}: total rem={len(c_rem2[n]):3d}, primitive C (d1=0)={len(prim_c):2d} | breakdown: {Counter((c.a, c.b) for c in prim_c)}")
