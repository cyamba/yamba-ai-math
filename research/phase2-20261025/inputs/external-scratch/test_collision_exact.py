from __future__ import annotations
from collections import defaultdict
import helpers as hp

for h in hp.hessenberg_vectors(5):
    tabs_221 = list(hp.tableaux(h, (2, 2, 1)))
    tabs_32 = list(hp.tableaux(h, (3, 2)))
    tabs_2111 = list(hp.tableaux(h, (2, 1, 1, 1)))
    
    # Group by B-image in F_{2111}
    by_B = defaultdict(list)
    for t in tabs_221:
        (u, v), (a, b), (c,) = t
        if hp.lt_p(h, c, b):
            img = ((u, v), (a,), (c,), (b,))
        else:
            img = ((u, v), (a,), (b,), (c,))
        assert img in tabs_2111 and hp.inv_g(h, img) == hp.inv_g(h, t)
        by_B[img].append(t)
        
    # Check every fiber with >1 element (a collision of B!)
    for img, ts in by_B.items():
        if len(ts) > 1:
            assert len(ts) == 2, f"Fiber size {len(ts)} at {h}"
            # One has c <_P b (which is T = ((u,v),(a,b),(c,))), the other has b not <_P c (which is T' = ((u,v),(a,c),(b,)))
            t_slide = [t for t in ts if hp.lt_p(h, t[2][0], t[1][1])][0]
            t_stay = [t for t in ts if not hp.lt_p(h, t[2][0], t[1][1])][0]
            (u, v), (a, b), (c,) = t_slide
            assert t_stay == ((u, v), (a, c), (b,))
            # Since t_stay is valid in F_{221}, we AUTOMATICALLY have a <_P c and c not <_P v!
            # Now check how t_slide or t_stay maps into F_{32} with the SAME inv_g!
            k = hp.inv_g(h, t_slide)
            cands_32 = [t32 for t32 in tabs_32 if hp.inv_g(h, t32) == k]
            # Check specific formulas:
            # Formula A: ((u, v, b), (a, c)) (when v <_P b)
            # Formula B: ((a, c, b), (u, v)) (when u not <_P a and v not <_P c)
            # Formula C: ((u, c, b), (a, v)) (when u <_P c and v not <_P c and a <_P v)
            fA = ((u, v, b), (a, c))
            fB = ((a, c, b), (u, v))
            fC = ((u, c, b), (a, v))
            matches = [f for f in (fA, fB, fC) if f in cands_32]
            if not matches:
                print(f"No match at h={h}, t_slide={t_slide}, k={k}, cands_32={cands_32}")
print("Verified all B-collisions across all 65 Hessenberg vectors!")
