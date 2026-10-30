"""Exact check of Lemma B (Smolensky under biased product measure via random restriction).

For h of degree <= d on {0,1}^Q, err_p(h) = Pr_{y~mu_p}[h(y) != (-1)^{|y|}].
Lemma B (proved in articles/sqrt-log-barrier.md):
   min_h err_p(h) >= E_{m ~ Bin(Q, 2p)} tail(m, d),   tail(m,d) = 2^{-m} sum_{i > floor(m/2)+d} C(m,i),
valid for 0 < p <= 1/2.  We compute the exact minimum by enumerating agreement sets (Q <= 4).
"""
import itertools
from fractions import Fraction as Fr
from math import comb
import numpy as np

def exact_min_err(Q, d, p):
    ys = list(itertools.product([0, 1], repeat=Q))
    w = [p ** sum(y) * (1 - p) ** (Q - sum(y)) for y in ys]
    par = np.array([(-1) ** sum(y) for y in ys], float)
    mons = [S for k in range(d + 1) for S in itertools.combinations(range(Q), k)]
    V = np.array([[np.prod([y[i] for i in S]) if S else 1 for S in mons] for y in ys], float)
    best = 1.0
    n = len(ys)
    for mask in range(1, 1 << n):
        idx = [i for i in range(n) if mask >> i & 1]
        err = 1 - sum(w[i] for i in idx)
        if err >= best - 1e-15:
            continue
        sol, *_ = np.linalg.lstsq(V[idx], par[idx], rcond=None)
        if np.allclose(V[idx] @ sol, par[idx], atol=1e-9):
            best = err
    return best

def tail(m, d):
    return sum(comb(m, i) for i in range(m // 2 + d + 1, m + 1)) / 2 ** m

def lemma_bound(Q, d, p):
    q = 2 * p
    return sum(comb(Q, m) * q ** m * (1 - q) ** (Q - m) * tail(m, d) for m in range(Q + 1))

ok = True
for Q in range(1, 5):
    for d in range(0, Q):
        for p in [0.5, 0.4, 1 / 3, 0.25, 0.1]:
            e = exact_min_err(Q, d, p); b = lemma_bound(Q, d, p)
            flag = e >= b - 1e-12
            ok &= flag
            print(f"Q={Q} d={d} p={p:.3f}  exact min err={e:.5f}  Lemma B bound={b:.5f}  {'OK' if flag else 'VIOLATED'}")
print("ALL OK" if ok else "SOME VIOLATION")
