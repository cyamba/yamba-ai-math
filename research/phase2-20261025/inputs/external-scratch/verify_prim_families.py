from __future__ import annotations
from collections import Counter, defaultdict
import helpers as hp
from inspect_complement import a2_reconstruct

# Wait: what if instead of keeping the unreviewed author-only patch `_template(b, k)` in `rr003_a2.py`
# (which was explicitly marked in `rr003_a2.py` line 1 as "UNREVIEWED author-only revision" and stole (9,6,3,3) and (10,6,6,1)),
# OR keeping `rr003_a2.py` intact, we check BOTH:
# 1. How a clean global multi-dimensional construction works across ALL (a, b), AND
# 2. How the exact complement of `rr003_a2.py` works!

# First, let's check the exact complement of `rr003_a2.py` up to n=30 when we account for the (9, 6^q) -> (10, 6^q, 1^{d_1-1}) carry!
rem_by_n = {}
for n in range(1, 31):
    us = sorted(hp.weighted_columns(w) for w in hp.weighted_partitions(n))
    a2_imgs = {a2_reconstruct(c) for c in hp.cluster_data(n) if c.a <= 2}
    rem_by_n[n] = [u for u in us if u not in a2_imgs]

# Let's define the "+1 continuation" step `next_one(u)` on U_rem:
# Normally, `next_one(u) = u + (1,)`.
# When is `u + (1,)` NOT in U_rem?
for n in range(9, 30):
    for u in rem_by_n[n]:
        u1 = u + (1,)
        if u1 not in rem_by_n[n + 1]:
            print(f"n={n:2d}: u={u} -> u+(1,)={u1} is in a2_imgs!")

print("\nNow let's check which elements of rem_by_n[n+1] have NO predecessor u in rem_by_n[n] with u+(1,) == v:")
for n in range(9, 28):
    from_prev = {u + (1,) for u in rem_by_n[n] if (u + (1,)) in rem_by_n[n + 1]}
    dead_ends = [u for u in rem_by_n[n] if (u + (1,)) not in rem_by_n[n + 1]]
    new_starts = [v for v in rem_by_n[n + 1] if v not in from_prev]
    prim_c = [c for c in hp.cluster_data(n + 1) if c.a >= 3 and c.mu[-1] == c.mu[-2]]
    if dead_ends or len(new_starts) != len(prim_c):
        print(f"n->{n+1}: dead_ends={dead_ends}, |new_starts|={len(new_starts)}, |prim_c|={len(prim_c)}")
        print(f"   new_starts={new_starts}")
