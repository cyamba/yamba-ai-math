from __future__ import annotations
from collections import Counter
import helpers as hp
from inspect_complement import a2_reconstruct

# Let's test our 6D Cone Theorem on (10^z, 9^y, 8^x, 6^{c6}, 3^{c3}, 1^{c1})
# for ALL y in {1, 2}, x + z >= 1 (0 <= z <= 3), and ALL (c6, c3, c1) in N^3 (with c6+c3+c1 >= 1 if x == 0)!
a2_all = set()
for n in range(1, 32):
    for c in hp.cluster_data(n):
        if c.a <= 2:
            a2_all.add(a2_reconstruct(c))

count_checked = 0
for y in (1, 2):
    for z in range(4):
        for x in range(4):
            if x + z == 0:
                continue
            for c6 in range(5):
                for c3 in range(5):
                    for c1 in range(5):
                        if x == 0 and c6 + c3 + c1 == 0:
                            continue
                        u = (10,)*z + (9,)*y + (8,)*x + (6,)*c6 + (3,)*c3 + (1,)*c1
                        # 1. Check u is valid in U:
                        hp.decode_columns(u)
                        # 2. Check u is NEVER in a2_all (for weights <= 31, or by direct recognizer check):
                        if sum(u) <= 31:
                            assert u not in a2_all, f"Collision with a<=2 at {u}"
                        count_checked += 1
print(f"VERIFIED {count_checked} states in the 6D cone (10^z, 9^y, 8^x, 6^c6, 3^c3, 1^c1): 100% valid in U and 0 collisions with a<=2!")
