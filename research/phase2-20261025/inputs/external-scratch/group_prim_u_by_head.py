from __future__ import annotations
from collections import Counter, defaultdict
import helpers as hp
from inspect_complement import a2_reconstruct
from inspect_a3_a4_exact import step_one

rem_by_n = {}
for n in range(1, 31):
    us = sorted(hp.weighted_columns(w) for w in hp.weighted_partitions(n))
    a2_imgs = {a2_reconstruct(c) for c in hp.cluster_data(n) if c.a <= 2}
    rem_by_n[n] = [u for u in us if u not in a2_imgs]

prim_u_all = []
for n in range(9, 31):
    prev_imgs = {step_one(u) for u in rem_by_n[n - 1]} if n > 9 else set()
    for u in rem_by_n[n]:
        if u not in prev_imgs:
            prim_u_all.append((n, u))

# Group each u in prim_u_all by (head >= 8, trailing 1s) vs (count of 6s, count of 3s)!
by_head = defaultdict(list)
for n, u in prim_u_all:
    head = tuple(x for x in u if x >= 8)
    ones = sum(1 for x in u if x == 1)
    c6 = sum(1 for x in u if x == 6)
    c3 = sum(1 for x in u if x == 3)
    by_head[(head, ones)].append((n, c6, c3, 2 * c6 + c3))

for (head, ones), items in sorted(by_head.items(), key=lambda kv: kv[1][0][0]):
    print(f"Head={head}, ones={ones} (first at n={items[0][0]}):")
    for n, c6, c3, m in items:
        print(f"  n={n:2d}: 6^{c6} 3^{c3}  (2*c6+c3 = {m})")
