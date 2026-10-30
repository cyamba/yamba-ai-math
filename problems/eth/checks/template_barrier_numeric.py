"""Numerical companion to the sqrt(log n) template barrier (article: sqrt-log-barrier.md).

Cost model of the swap-interpolation template (exponent divided by n, constants dropped):
    E = (R/Q) * ln(e*Q/R)  +  tau * ln(2*r^(2Q)+1)  +  1/r
Constraint (measurement accounting, paper Sec. 2.6 Step 4): rows = r*h*c with c >= eps*D and
h >= max(1, n/D) (pigeonhole over D labels), and rows <= 2*tau*n, so
    eps_min(Q, R-1, p_r) * r * max(D, n) <= 2 * tau * n,   p_r = (r-1)/(2r),
where eps_min is lower-bounded by Lemma B (biased Smolensky via restriction).
We minimise E over integer r, Q, R and real tau and compare with
    loglog n / sqrt(log n)   (barrier)   and   (loglog n)^2 / sqrt(log n)  (paper, interpolation route).
"""
import math
from functools import lru_cache

def log_tail(m, d):
    # log of 2^-m * sum_{i > m//2 + d} C(m,i)
    lo = m // 2 + d + 1
    if lo > m: return -math.inf
    terms = [math.lgamma(m+1)-math.lgamma(i+1)-math.lgamma(m-i+1) for i in range(lo, m+1)]
    mx = max(terms); return mx + math.log(sum(math.exp(t-mx) for t in terms)) - m*math.log(2)

@lru_cache(maxsize=None)
def log_lemmaB(Q, d, p):
    q = 2*p; best = -math.inf; vals=[]
    for m in range(Q+1):
        lt = log_tail(m, d)
        if lt == -math.inf: continue
        lb = math.lgamma(Q+1)-math.lgamma(m+1)-math.lgamma(Q-m+1)+m*math.log(q)+(Q-m)*math.log(1-q)+lt
        vals.append(lb)
    if not vals: return -math.inf
    mx=max(vals); return mx+math.log(sum(math.exp(v-mx) for v in vals))

def min_cost(lnn):
    best=(math.inf,None)
    for r in range(2, 120):
        p=(r-1)/(2*r)
        for Q in range(2, 260):
            lnD=2*Q*math.log(r)
            if lnD > 3*lnn: break
            for R in range(2, Q+1):
                le=log_lemmaB(Q, R-1, p)
                if le==-math.inf: le=-1e9
                # tau >= eps*r*D/(2n)
                ln_tau=le+math.log(r)+max(lnD,lnn)-math.log(2)-lnn
                tau=math.exp(min(ln_tau,0.0))
                if ln_tau>0: continue
                E=(R/Q)*math.log(math.e*Q/R)+tau*(lnD+math.log(2))+1/r
                if E<best[0]: best=(E,(r,Q,R,tau))
                if R/Q*math.log(math.e*Q/R) > best[0]: break
    return best

print(f"{'log2 n':>8} {'min E':>9} {'barrier lnln/sqrt(ln)':>22} {'ratio':>7} {'(lnln)^2/sqrt(ln)':>18}  argmin (r,Q,R)")
for k in [64, 256]:
    lnn=k*math.log(2)
    E,arg=min_cost(lnn)
    b=math.log(lnn)/math.sqrt(lnn); b2=math.log(lnn)**2/math.sqrt(lnn)
    print(f"{k:>8} {E:9.4f} {b:22.4f} {E/b:7.2f} {b2:18.4f}  {arg[:3]}")
