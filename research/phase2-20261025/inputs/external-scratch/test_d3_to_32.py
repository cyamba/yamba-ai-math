from __future__ import annotations
from collections import defaultdict
import helpers as hp

# Let's check for ALL 65 Hessenberg vectors at n=5:
# For T = ((u, v), (a, b), (c,)) in F_{221} that lies in D_{>= 3} (meaning c <_P b AND a <_P c, so a <_P c <_P b):
# How does T map into F_{32}?
# Wait: in T = ((u, v), (a, b), (c,)), we know:
# 1. u <_P v (row 1 is a P-chain)
# 2. a <_P c <_P b (since T in D_{>= 3})
# 3. a not <_P u, and b not <_P v (column condition between row 1 and row 2 of T)
# 4. c not <_P a (automatically true since a <_P c)
# Wait: what if we form a tableau of shape (3, 2) from {u, v, a, b, c}?
# Look at the two natural candidates in F_{32}:
# Candidate 1 (Promote b to row 1, put c after a in row 2):
#   ((u, v, b), (a, c))!
#   Wait: when is ((u, v, b), (a, c)) a valid P-tableau of shape (3, 2)?
#   - Row 2 is (a, c), which is a valid P-chain because a <_P c!
#   - Column 1 is (u, a), which has no descent because a not <_P u (from T)!
#   - Column 2 is (v, c): does c not <_P v hold?
#     In P_h, b not <_P v means v <= h(b), and a <_P c <_P b... wait: if v <_P b holds, then ((u, v, b), (a, c)) has row 1 = (u, v, b)!
#   - What if v is NOT <_P b (meaning b not <_P v and v not <_P b, or wait: in T, b not <_P v is ALWAYS true! What if v <_P b is false)?
#     Wait: if v <_P b is false, can (a, c, b) be Row 1 and (u, v) be Row 2, i.e., ((a, c, b), (u, v))?!
#     HOLD ON! Look at ((a, c, b), (u, v)):
#     - Row 1 is (a, c, b), which is ALREADY a 3-chain a <_P c <_P b!
#     - Row 2 is (u, v), which is ALREADY a 2-chain u <_P v!
#     - Check the column conditions of ((a, c, b), (u, v)):
#       We need u not <_P a and v not <_P c!
#     Let's test on all 65 Hessenberg vectors at n=5!

for h in hp.hessenberg_vectors(5):
    tabs_221 = list(hp.tableaux(h, (2, 2, 1)))
    tabs_32 = list(hp.tableaux(h, (3, 2)))
    d3_tabs = [t for t in tabs_221 if hp.lt_p(h, t[1][0], t[2][0]) and hp.lt_p(h, t[2][0], t[1][1])]
    if not d3_tabs:
        continue
    # Group by inv_g
    d3_by_inv = defaultdict(list)
    for t in d3_tabs:
        d3_by_inv[hp.inv_g(h, t)].append(t)
    t32_by_inv = defaultdict(list)
    for t in tabs_32:
        t32_by_inv[hp.inv_g(h, t)].append(t)
    for k, ts in d3_by_inv.items():
        if len(ts) > len(t32_by_inv[k]):
            print(f"Deficit at h={h}, inv={k}: |D_{{>=3}}|={len(ts)} > |F_32|={len(t32_by_inv[k])}")
        # Check specific maps into t32_by_inv[k]
        for t in ts:
            (u, v), (a, b), (c,) = t
            cand1 = ((u, v, b), (a, c))
            cand2 = ((a, c, b), (u, v))
            c1_ok = cand1 in t32_by_inv[k]
            c2_ok = cand2 in t32_by_inv[k]
            if not (c1_ok or c2_ok):
                print(f"Neither cand1 nor cand2 worked for h={h}, t={t}, inv={k}; available 32: {t32_by_inv[k]}")
print("Tested D_{>=3} -> F_{32} across all 65 Hessenberg vectors!")
