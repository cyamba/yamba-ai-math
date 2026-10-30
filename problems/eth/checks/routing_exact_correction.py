"""Exact search for a rank-(c-1) routing matrix by a one-step correction of the
commutative optimum (Q=3, R=2, r=2).  All arithmetic is over Q (sympy).

K = ker(I - M_c) where M_c = V0 f(W0) is the commutative optimum.  A correction N supported
on the pattern P with N K = 0 and N x = (I - M_c) x for some x not in K yields
rank(I - M_c - N) = rank(I - M_c) - 1.  Row u of N must lie in W_u = K^perp ∩ span{e_w: w in P_u}.
"""
import itertools
import sympy as sp
from routing_minrank_experiment import pattern

Q, R, r = 3, 2, 2
P, D = pattern(Q, R, r)
labels = list(itertools.product(range(r), repeat=2 * Q))
idx = {l: i for i, l in enumerate(labels)}

def swap_at(l, s):
    a, d = list(l[:Q]), list(l[Q:])
    a[s], d[s] = d[s], a[s]
    return tuple(a + d)

def perm_matrix(fn):
    M = sp.zeros(D, D)
    for l in labels:
        M[idx[l], idx[fn(l)]] = 1
    return M

Pi = [perm_matrix(lambda l, s=s: swap_at(l, s)) for s in range(Q)]
I = sp.eye(D)
V0 = Pi[0] * Pi[1] * Pi[2]
W0 = sum(((I - Pi[s]) / 2 for s in range(Q)), sp.zeros(D, D))
# f(j) = (-1)^j on the interval {0,1}: f(j) = 1 - 2j, degree 1 = R-1
Mc = V0 * (I - 2 * W0)
assert all(Mc[i, j] == 0 or P[i, j] for i in range(D) for j in range(D)), "support violated"
A = I - Mc
print("rank(I - M_c) =", A.rank())
K = A.nullspace()                    # basis of ker(I - M_c)
Kmat = sp.Matrix.hstack(*K)
Kperp = Kmat.T.nullspace()            # basis of K^perp (dimension c)
Kp = sp.Matrix.hstack(*Kperp)         # D x c
c = Kp.shape[1]
# W_u = {Kp z : (Kp z)_w = 0 for w not in P_u}
Z_rows, Wdims = [], []
for u in range(D):
    off = [w for w in range(D) if not P[u, w]]
    sub = Kp.extract(off, list(range(c)))
    ns = sub.nullspace()
    Wdims.append(len(ns))
    if len(ns) == 0:
        Z_rows.append(u)
print("rows with W_u = 0:", len(Z_rows), " distribution of dim W_u:",
      {d: Wdims.count(d) for d in set(Wdims)})
# need x (mod K) with ((I - M_c) x)_u = 0 for u in Z_rows, x not in K.  Parametrise x = Kp y.
Ax = (A * Kp).extract(Z_rows, list(range(c)))
sol = Ax.nullspace()
print("dimension of admissible x (mod K):", len(sol))
