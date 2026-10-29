from __future__ import annotations
from collections import Counter
import helpers as hp
from inspect_complement import a2_reconstruct

# Let's check which heads H (with all parts >= 8) generate universal 3D cones H + (6^{c6}, 3^{c3}, 1^{c1}) in U_rem!
#Wait: when is H + (6^{c6}, 3^{c3}, 1^{c1}) valid in \mathcal{U}?
# Let h_min = inverse_prefix(H[-1]) be the height of the last column of H.
# Provided H itself has consecutive height drops <= 4:
# - If h_min <= 4 (i.e., H[-1] == 8, since D(8) = 4):
#   Then H + (6^{c6}, 3^{c3}, 1^{c1}) is VALID FOR ALL (c6, c3, c1) in N^3 (including c6=c3=c1=0)!
# - If h_min == 5 (i.e., H[-1] == 9, since D(9) = 5):
#   Then H + (6^{c6}, 3^{c3}, 1^{c1}) is VALID FOR ALL (c6, c3, c1) != (0, 0, 0) (since D(6)=3, D(3)=2, D(1)=1 all have 5 - D <= 4)!
# - If h_min in {6, 7} (i.e., H[-1] in {10, 12}, since D(10)=6, D(12)=7):
#   Then H + (6^{c6}, 3^{c3}, 1^{c1}) is VALID FOR ALL c6 + c3 >= 1 (if H[-1]==10, since 6-2=4) or c6 >= 1 (if H[-1]==12, since 7-3=4)!

# Let's enumerate all valid heads H (columns >= 8) of weight <= 30 and check their exact (c6, c3, c1) domains in U_rem!
rem_by_n = {}
for n in range(1, 31):
    us = sorted(hp.weighted_columns(w) for w in hp.weighted_partitions(n))
    a2_imgs = {a2_reconstruct(c) for c in hp.cluster_data(n) if c.a <= 2}
    rem_by_n[n] = set(us) - a2_imgs

heads = set()
for n in range(9, 31):
    for u in rem_by_n[n]:
        head = tuple(x for x in u if x >= 8)
        heads.add(head)

for head in sorted(heads, key=lambda h: (sum(h), h)):
    wt_h = sum(head)
    h_last = hp.inverse_prefix(head[-1]) if head else 0
    print(f"Head {str(head):18s} (wt={wt_h:2d}, D_last={h_last})")
