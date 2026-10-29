from __future__ import annotations
from collections import Counter
import helpers as hp
from inspect_complement import a2_reconstruct

rem_by_n = {}
for n in range(1, 31):
    us = sorted(hp.weighted_columns(w) for w in hp.weighted_partitions(n))
    a2_imgs = {a2_reconstruct(c) for c in hp.cluster_data(n) if c.a <= 2}
    rem_by_n[n] = [u for u in us if u not in a2_imgs]

# Let's define the exact "+1 continuation" map `step_one(u)` on U_rem:
# Normally `step_one(u) = u + (1,)`.
# Except on the dead-end families where `u + (1,)` was claimed by a=2:
# 1. `u = (9,) + (6,)*q` (q >= 1): `step_one(u) = (10,) + (6,)*q`!
# 2. `u = (10,) + (6,)*(2+q) + (3,)*r` (q >= 0, r in {0, 1}):
#    Look at weight 22+6q+3r+1 = 23+6q+3r:
#    For q=0, r=0 (u=(10, 6, 6), wt 22): step_one(u) = (12, 8, 3) (wt 23)!
#    For q=0, r=1 (u=(10, 6, 6, 3), wt 25): step_one(u) = (12, 8, 3, 3) (wt 26)!
#    For q=1, r=0 (u=(10, 6, 6, 6), wt 28): step_one(u) = (12, 8, 6, 3) (wt 29)!
#    WAIT A SECOND! Look at those three replacements for (10, 6, 6, 6^q, 3^r) + 1:
#    10 + 6 + 6 + 1 = 23 = 12 + 8 + 3!
#    So replacing (10, 6, 6) + (1,) by (12, 8, 3) works for ALL q >= 0, r in {0, 1}:
#    (10, 6, 6, 6^q, 3^r) + 1  --->  (12, 8, 6^q, 3^{r+1})!!
# HOLD EVERYTHING! Check that arithmetic:
# 10 + 6 + 6 + 1 = 23 = 12 + 8 + 3!
# And in (12, 8, 6^q, 3^{r+1}), the heights are:
# h(12)=7, h(8)=4, h(6)=3, h(3)=2!
# Consecutive height drops: 7-4 = 3 < 5, 4-3 = 1 < 5, 3-2 = 1 < 5, 2-0 = 2 < 5!
# And is (12, 8, 6^q, 3^{r+1}, 1^t) EVER in a2_imgs for ANY q >= 0, r >= 0, t >= 0?!
# NEVER! Because it has non-3-divisible marker {8: 1} AND max 3-divisible column 12 without 9!

def step_one(u: tuple[int, ...]) -> tuple[int, ...]:
    c = Counter(u)
    # Family 1 dead-end: (9, 6^q) for q >= 1
    if c[9] == 1 and c[6] >= 1 and len(u) == 1 + c[6]:
        return (10,) + (6,) * c[6]
    # Family 2 dead-end: (10, 6^{2+q}, 3^r) for q >= 0, r in {0, 1}
    if c[10] == 1 and c[6] >= 2 and c[3] in (0, 1) and len(u) == 1 + c[6] + c[3]:
        q = c[6] - 2
        r = c[3]
        return (12, 8) + (6,) * q + (3,) * (r + 1)
    return u + (1,)

# Let's test `step_one(u)` across ALL n = 9..29!
for n in range(9, 30):
    imgs = [step_one(u) for u in rem_by_n[n]]
    assert len(set(imgs)) == len(imgs), f"Collision in step_one at n={n}"
    for v in imgs:
        assert v in rem_by_n[n + 1], f"step_one({u}) = {v} not in rem_by_n[{n+1}]"
print("VERIFIED: step_one(u) is a 100% injective, valid map U_rem[n] -> U_rem[n+1] for ALL n = 9..29!")

# Now let's print the EXACT primitive cores `prim_U[n] = rem_by_n[n] \ step_one(rem_by_n[n-1])`
# alongside `prim_C[n] = {c in C(a>=3)[n] : mu[-1] == mu[-2]}`!
for n in range(9, 27):
    prev_imgs = {step_one(u) for u in rem_by_n[n - 1]} if n > 9 else set()
    prim_u = [u for u in rem_by_n[n] if u not in prev_imgs]
    prim_c = [c for c in hp.cluster_data(n) if c.a >= 3 and c.mu[-1] == c.mu[-2]]
    assert len(prim_u) == len(prim_c), f"Mismatch at n={n}: {len(prim_u)} vs {len(prim_c)}"
    print(f"=== n={n:2d}: |prim_C| = |prim_U| = {len(prim_c):2d} ===")
    for c, u in zip(prim_c, prim_u):
        # Print c in difference coordinates d_a = mu[0], d_{a-1} = mu[1]-mu[0], ...
        diffs = [c.mu[0]] + [c.mu[i] - c.mu[i-1] for i in range(1, c.a - 1)]
        print(f"  a={c.a} b={c.b} diffs={tuple(diffs)} nu={c.nu}  <-->  {u}")
