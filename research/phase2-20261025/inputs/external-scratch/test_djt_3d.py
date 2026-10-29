from __future__ import annotations
from collections import Counter, defaultdict
from itertools import permutations
import helpers as hp

# Let's inspect all DJT configurations (shape, sigma, T) for n=5 total order, lam=(4,1)
#Wait: in DJT, s_mu = det(e_{mu'_i - i + sigma(i)})_{1 <= i <= m} where m = mu_1 (or padded to n).
# Wait: if we pad mu' with zeros to length n, let's see what happens!
# If mu' = (c_1, c_2, ..., c_n) with c_j = 0 for j > mu_1:
# Then for any sigma in S_n, alpha_i = c_i - i + sigma(i).
# Wait: does det_{1 <= i,j <= n}(e_{c_i - i + j}) equal det_{1 <= i,j <= mu_1}(e_{c_i - i + j})?
# YES! Because for i > mu_1, c_i = 0, so the matrix is block upper-triangular with 1s on the diagonal (e_0 = 1) and 0s below the diagonal (e_{<0} = 0)!
# That means padding mu' with zeros to length m (say m = len(lam) or m = n) adds NO extra terms!
# Even better: what if we fix the ordered tuple alpha = (lam_1, lam_2, ..., lam_m) (or sum over distinct permutations of lam)?
# Wait: let's check both!

def get_djt_states(h, lam):
    n = len(h)
    lam_sorted = tuple(sorted((x for x in lam if x > 0), reverse=True))
    states = []
    for shape in hp.partitions(n):
        cols = tuple(sum(x > j for x in shape) for j in range(shape[0]))
        for sigma in permutations(range(len(cols))):
            alpha = tuple(cols[i] - i + sigma[i] for i in range(len(cols)))
            if any(x < 0 for x in alpha):
                continue
            if tuple(sorted((x for x in alpha if x > 0), reverse=True)) != lam_sorted:
                continue
            invs = sum(sigma[i] > sigma[j] for i in range(len(sigma)) for j in range(i+1, len(sigma)))
            sign = (-1) ** invs
            for t in hp.tableaux(h, shape):
                states.append((shape, cols, sigma, alpha, sign, hp.inv_g(h, t), t))
    return states

h_total = (1, 2, 3, 4, 5)
states = get_djt_states(h_total, (4, 1))
print(f"Total states for n=5 total order, lam=(4,1): {len(states)}")
for sh, cols, sig, alpha, sgn, inv, t in states:
    print(f"  shape={str(sh):12s} cols={str(cols):15s} sigma={str(sig):15s} alpha={str(alpha):15s} sign={sgn:+d} T={t}")
