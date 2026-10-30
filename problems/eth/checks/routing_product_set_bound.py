"""Universal lower bound for the routing min-rank problem (ETH-B01/B03).

Split symbols [r] = X ⊔ Y at every position. Let
   A  = {a in [r]^Q : #{s : a(s) in X} >= ceil((Q+R)/2)},
   D' = {d in [r]^Q : #{s : d(s) in Y} >= ceil((Q+R)/2)}.
For a in A, d in D' the positions with a(s) in X and d(s) in Y number >= R, so Ham(d,a) >= R.
Hence on T = {u : a_u in A, d_u in D'} every entry M[u,w] of a pattern-supported M is 0, so
(I - M)[T,T] = I and rank(I - M) >= |T| for EVERY M (commutative or not).
This script (1) verifies the zero block exactly on the pattern, (2) compares |T|/D with the
commutative optimum's exceptional fraction for moderate parameters.
"""
import itertools, math
import numpy as np
from routing_minrank_experiment import pattern

def T_set(Q, R, r, X):
    labels = list(itertools.product(range(r), repeat=2 * Q))
    th = math.ceil((Q + R) / 2)
    return [i for i, l in enumerate(labels)
            if sum(l[s] in X for s in range(Q)) >= th and sum(l[Q + s] not in X for s in range(Q)) >= th]

for (Q, R, r) in [(2, 1, 2), (3, 1, 2), (4, 2, 2), (3, 2, 3), (4, 1, 3), (2, 1, 4)]:
    P, D = pattern(Q, R, r)
    for X in [set(range(k)) for k in range(1, r)]:
        T = T_set(Q, R, r, X)
        assert not P[np.ix_(T, T)].any(), "zero block violated"
    best = max(len(T_set(Q, R, r, set(range(k)))) for k in range(1, r))
    print(f"Q={Q} R={R} r={r} D={D}: zero block verified; best |T| = {best}")

def logbinom_tail(Q, t):  # log Pr[Bin(Q,1/2) >= t]
    vals = [math.lgamma(Q+1)-math.lgamma(i+1)-math.lgamma(Q-i+1) for i in range(t, Q+1)]
    m = max(vals); return m + math.log(sum(math.exp(v-m) for v in vals)) - Q*math.log(2)

print("\nAsymptotic comparison, r even, |X| = r/2 (fractions of D):")
print(f"{'Q':>5} {'R':>4} {'log10 lower(|T|/D)':>20} {'log10 comm. upper (interval)':>30}")
for Q in [64, 256, 1024]:
    for R in [int(2*math.sqrt(Q)), int(4*math.sqrt(Q))]:
        lo = 2*logbinom_tail(Q, math.ceil((Q+R)/2))
        # commutative: interval of R levels centred at Q/2 (p ~ 1/2): Pr[|Bin - Q/2| >= R/2]
        up = math.log(2) + logbinom_tail(Q, math.ceil(Q/2 + R/2))
        print(f"{Q:>5} {R:>4} {lo/math.log(10):20.2f} {up/math.log(10):30.2f}")
