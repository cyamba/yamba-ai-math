from __future__ import annotations
from collections import Counter, defaultdict
from itertools import permutations
import helpers as hp

def conjugate(shape: tuple[int, ...]) -> tuple[int, ...]:
    if not shape:
        return ()
    return tuple(sum(1 for r in shape if r > j) for j in range(shape[0]))

# Wait: what is the relationship between two states (beta, tab) and (beta', tab')?
# Notice that in every state (beta, tab), tab has shape mu(beta), so its columns have lengths mu'_0, mu'_1, ..., mu'_{n-1}.
# Wait: what about the ROWS of tab?
# In a P-tableau T of shape mu:
# - Each row is a strict P-chain!
# - Wait: when we reblock the same row word w(T) into a different shape nu, why does that preserve inv_G(T)??
# WAIT A SECOND!
# Does same-word reblocking ALWAYS preserve inv_G(T)?
# NO! Hold on! In inv_G(h, rows), inv_G depends on WHICH ROW each vertex u is in (`row_of[v] < row_of[u]`), NOT just on the concatenated word, UNLESS the vertices that change relative row are comparable in P (non-edges of G)!
# Let's check when reblocking or 3D sliding preserves inv_G(h, rows)!

def cho_huh_slide_B(h, tab):
    """
    Apply Cho-Huh's comparable-prefix slide B (Theorem 4.1) to the last 2-cell row of tab.
    If tab has shape (2^k, 1^r) with k >= 1:
    Let last 2-cell row be (a, b) at index k-1, followed by singletons c_1, ..., c_r.
    Let C = longest prefix of (c_1, ..., c_r) with c_i <_P b.
    Map to shape (2^{k-1}, 1^{r+2}) by replacing (a, b), C, D with (a,), C, (b,), D.
    """
    lengths = [len(r) for r in tab]
    if 2 not in lengths or max(lengths) > 2:
        return None
    # last 2-cell row
    k = max(i for i, l in enumerate(lengths) if l == 2)
    a, b = tab[k]
    suffix = [r[0] for r in tab[k+1:]]
    p_len = 0
    while p_len < len(suffix) and hp.lt_p(h, suffix[p_len], b):
        p_len += 1
    C = [(x,) for x in suffix[:p_len]]
    D = [(x,) for x in suffix[p_len:]]
    new_tab = tab[:k] + ((a,),) + tuple(C) + ((b,),) + tuple(D)
    if hp.validates(h, new_tab) and hp.inv_g(h, new_tab) == hp.inv_g(h, tab):
        return new_tab
    return None

# What if a <_P c_i <_P b (the height >= 3 case where Cho-Huh's B collides)?
# Look at our 3D Ferrers diagram insight:
# When we slide b along the 3rd axis (z-axis) over C = (c_1, ..., c_p) where c_i <_P b:
# Case 1 (2D / Height-2 fibre): a is NOT <_P c_1 (so (a, c_1, b) is NOT a 3-chain in P).
#   Then unfolding the z-axis onto the y-axis gives (a,), c_1, ..., c_p, (b,), D in shape (2^{k-1}, 1^{r+2}),
#   and b is STILL the FIRST singleton after (a,) that is >_P a! So B is uniquely invertible on this fibre!
# Case 2 (3D / Height >= 3 fibre): a <_P c_1 <_P b IS a 3-chain in P!
#   Because (a, c_1, b) is a 3-chain in P, where does a 3-chain live?
#   It has length 3 along the x-axis (a row of length >= 3, like mu=(3,2) or (3,1,1) or (4,1))!
#   Wait: let's check for T_2 = ((1,2), (3,5), (4,)) (where a=3, b=5, c_1=4, and 3 <_P 4 <_P 5):
#   Instead of unfolding (3, 4, 5) vertically into singletons (3,), (4,), (5,) (which collides with T_1 = ((1,2), (3,4), (5,))),
#   in 3D we rotate the 3-chain (3, 4, 5) (or promote 5 into row 1) into a wider shape!
#   Let's check ALL states of mu=(2,2,1) across all 65 Hessenberg vectors where Cho-Huh's B collides!

for h in hp.hessenberg_vectors(5):
    tabs_221 = list(hp.tableaux(h, (2, 2, 1)))
    by_image = defaultdict(list)
    for t in tabs_221:
        img = cho_huh_slide_B(h, t)
        assert img is not None, f"B failed on {h}, {t}"
        by_image[img].append(t)
    collisions = {img: ts for img, ts in by_image.items() if len(ts) > 1}
    if collisions:
        # Check which t in ts has a <_P c_1 <_P b!
        for img, ts in collisions.items():
            has_3chain = []
            no_3chain = []
            for t in ts:
                a, b = t[1]
                c1 = t[2][0]
                if hp.lt_p(h, a, c1) and hp.lt_p(h, c1, b):
                    has_3chain.append(t)
                else:
                    no_3chain.append(t)
            if len(no_3chain) != 1:
                print(f"Surprise at h={h}: no_3chain={no_3chain}, has_3chain={has_3chain}")
print("Checked all 65 Hessenberg vectors for 3-chain separation of B collisions in (2,2,1)!")
