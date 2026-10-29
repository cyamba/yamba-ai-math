from __future__ import annotations
from collections import defaultdict
import helpers as hp

# Wait: at n=5, lam=(4, 1), what is the DJT formula?
# [e_{4,1}] X_G = (F_{2111} + F_{32} + F_{41}) - (F_{221} + F_{311} + 2 F_5).
# Let's check across ALL 65 Hessenberg vectors at n=5:
# We already have Phi_{221} : T_P(2, 2, 1) -> T_P(2, 1, 1, 1) \sqcup T_P(3, 2) (100% injective!).
# What about T_P(3, 1, 1) and the 2 copies of T_P(5)?
# Notice that T_P(5) is only non-empty when h = (1, 2, 3, 4, 5) (the total order, where P_h has a 5-chain (1,2,3,4,5))!
# Wait: what about T_P(3, 1, 1)?
# In T = ((u, v, w), (a,), (b,)) in T_P(3, 1, 1):
# Look at how T = ((u, v, w), (a,), (b,)) is a HOOK shape (3, 1, 1)!
# Can T_P(3, 1, 1) map into the remaining unused elements of T_P(2, 1, 1, 1) \sqcup T_P(3, 2) \sqcup T_P(4, 1)?
# Wait: even simpler!
# Look at T = ((u, v, w), (a,), (b,)) in T_P(3, 1, 1):
# If a <_P b, then (a, b) is a 2-chain! When is ((u, v, w), (a, b)) a valid tableau in T_P(3, 2)?
# Whenever b not <_P v!
# And what if b <_P v or a not <_P b?
# Look at sliding w out of row 1 (hook slide into T_P(2, 1, 1, 1), just like Cho-Huh's B on row 1 (u, v, w) -> (u, v) + singletons!), OR inserting a or b into row 1 to get T_P(4, 1)!
# Let's check on all 65 Hessenberg vectors at n=5!

for h in hp.hessenberg_vectors(5):
    # Check that at every inv degree k, total positive >= total negative
    pos_2111 = list(hp.tableaux(h, (2, 1, 1, 1)))
    pos_32 = list(hp.tableaux(h, (3, 2)))
    pos_41 = list(hp.tableaux(h, (4, 1)))
    neg_221 = list(hp.tableaux(h, (2, 2, 1)))
    neg_311 = list(hp.tableaux(h, (3, 1, 1)))
    neg_5 = list(hp.tableaux(h, (5,)))
    
    # Check how many h have neg_311 non-empty:
    if neg_311:
        # Let's see which h have neg_311 non-empty
        pass

h_with_311 = [h for h in hp.hessenberg_vectors(5) if list(hp.tableaux(h, (3, 1, 1)))]
h_with_221_d3 = [h for h in hp.hessenberg_vectors(5) if any(
    hp.lt_p(h, t[2][0], t[1][1]) and hp.lt_p(h, t[1][0], t[2][0]) and not hp.lt_p(h, t[2][0], t[0][1])
    for t in hp.tableaux(h, (2, 2, 1))
)]
print(f"Out of 65 Hessenberg vectors: {len(h_with_311)} have T_P(3,1,1) != empty; {len(h_with_221_d3)} have B-collisions in T_P(2,2,1).")
