from __future__ import annotations
import sys
from collections import Counter

sys.path.insert(0, "/Users/christopheryamba/YambaCode/Math/yamba-ai-math-rogers-ramanujan/research/rogers-ramanujan/checks")
import kr1, rr003_a2

OutsideRestrictedDomain = rr003_a2.OutsideRestrictedDomain

def step_one_v2(u: tuple[int, ...]) -> tuple[int, ...]:
    c = Counter(u)
    # 1. (9, 6^q) -> (10, 6^q) for q >= 1
    if c[9] == 1 and c[6] >= 1 and len(u) == 1 + c[6]:
        return (10,) + (6,) * c[6]
    # 2. (10, 6^{2+q}, 3^r) -> (12, 8, 6^q, 3^{r+1}) for q >= 0, r in {0, 1}
    if c[10] == 1 and c[6] >= 2 and c[3] in (0, 1) and len(u) == 1 + c[6] + c[3]:
        q = c[6] - 2
        r = c[3]
        return (12, 8) + (6,) * q + (3,) * (r + 1)
    # 3. (10, 10, 6^{1+q}, 3^r, 1^4) -> (10, 9, 9, 6^q, 3^{r+1}) for q >= 0, r in {0, 1}
    if c[10] == 2 and c[6] >= 1 and c[3] in (0, 1) and c[1] == 4 and len(u) == 2 + c[6] + c[3] + 4:
        q = c[6] - 1
        r = c[3]
        return (10, 9, 9) + (6,) * q + (3,) * (r + 1)
    # 4. (17, 9, 6, 3^{1+r}) -> (17, 10, 6, 3^{1+r}) for r >= 0
    if c[17] == 1 and c[9] == 1 and c[6] == 1 and c[3] >= 1 and len(u) == 3 + c[3]:
        return (17, 10, 6) + (3,) * c[3]
    # 5. (19, 12, 6) -> (17, 12, 6, 3)
    if u == (19, 12, 6):
        return (17, 12, 6, 3)
    return u + (1,)

def reconstruct_a3_b0_v2(c: kr1.ClusterData) -> tuple[int, ...]:
    d3 = c.mu[0]
    d2 = c.mu[1] - c.mu[0]
    d1 = c.mu[2] - c.mu[1]

    if d2 == 0:
        q, r = divmod(d3 + 3, 2)
        core = (6,) * q + (3,) * r
    elif d2 == 1:
        core = (8,) + (3,) * (1 + d3) if d3 <= 1 else (8, 6) + (3,) * (d3 - 1)
    elif d2 == 2:
        core = (10,) + (3,) * (1 + d3) if d3 <= 1 else (10, 6) + (3,) * (d3 - 1)
    elif d2 == 3:
        if d3 == 0:
            core = (9, 6)
        elif d3 <= 2:
            core = (10, 8) + (3,) * (d3 - 1)
        else:
            core = (10, 8, 6) + (3,) * (d3 - 3)
    else:
        q2, r2 = divmod(d2, 3)
        if r2 == 1:
            core = (9, 8) + (6,) * (q2 - 1) + (3,) * d3
        elif r2 == 2:
            if q2 == 1 and d3 == 0:
                core = (9, 9, 1)
            else:
                core = (10, 9) + (6,) * (q2 - 1) + (3,) * d3
        else:
            if q2 >= 4 and d3 >= 1:
                core = (10, 9, 9, 8) + (6,) * (q2 - 4) + (3,) * (d3 - 1)
            else:
                core = (9, 9) + (6,) * (q2 - 2) + (3,) * (1 + d3)

    u = core
    for _ in range(d1):
        u = step_one_v2(u)
    return u

# Verify across all n = 0..40 that step_one_v2 has ZERO dead ends and is 100% injective on U_rem2!
u_rem2 = {}
for n in range(0, 41):
    us = set(kr1.weighted_columns(w) for w in kr1.weighted_partitions(n))
    cs = list(kr1.cluster_data(n))
    used_u = set()
    for c in cs:
        if c.a <= 2:
            u = rr003_a2.reconstruct_columns(c)
            assert u in us and u not in used_u
            used_u.add(u)
        elif c.a == 3 and c.b == 0:
            u = reconstruct_a3_b0_v2(c)
            assert u in us and u not in used_u
            used_u.add(u)
    u_rem2[n] = sorted(us - used_u)

prim_u = {}
for n in range(0, 41):
    if n == 0:
        prim_u[0] = u_rem2[0]
        continue
    u_set = set(u_rem2[n])
    imgs = set()
    for prev in u_rem2[n - 1]:
        img = step_one_v2(prev)
        assert img in u_set, f"n={n-1}->{n}: step_one_v2({prev}) = {img} not in u_rem2[{n}]"
        assert img not in imgs, f"n={n-1}->{n}: step_one_v2 collision at {img}"
        imgs.add(img)
    prim_u[n] = sorted(u_set - imgs)

print("100% VERIFIED: step_one_v2 is a UNIVERSAL injection U_rem2[n-1] -> U_rem2[n] across ALL 0 <= n <= 40 with ZERO dead ends and ZERO collisions!")
