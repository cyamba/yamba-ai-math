from __future__ import annotations
from collections import Counter
import helpers as hp

case_counts = Counter()
for h in hp.hessenberg_vectors(5):
    for t in hp.tableaux(h, (2, 2, 1)):
        (u, v), (a, b), (c,) = t
        if hp.lt_p(h, c, b) and hp.lt_p(h, a, c) and not hp.lt_p(h, c, v):
            k = hp.inv_g(h, t)
            c1 = ((u, v, b), (a, c))
            c2 = ((a, c, b), (u, v))
            c3 = ((u, c, b), (a, v))
            v1 = hp.validates(h, c1, (3, 2)) and hp.inv_g(h, c1) == k
            v2 = hp.validates(h, c2, (3, 2)) and hp.inv_g(h, c2) == k
            v3 = hp.validates(h, c3, (3, 2)) and hp.inv_g(h, c3) == k
            case_counts[(v1, v2, v3)] += 1
            if not v1:
                print(f"h={h}, t={t}: v1={v1}, v2={v2}, v3={v3}")
print("Case counts (v1, v2, v3):", case_counts)
