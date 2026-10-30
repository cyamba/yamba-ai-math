"""Find an EXACT rank-9 routing completion for (Q,R,r)=(3,2,2) by alternating projections
with progressive snapping of free entries to small rationals, then verify rank exactly (sympy).
Reduced form: rows = 'bad' indices u (Ham(d_u,a_u) >= 2); Z[u,w] = delta_uw off the pattern."""
import numpy as np, sympy as sp, itertools, json, sys
from fractions import Fraction
from routing_minrank_experiment import pattern
Q,R,r,k = 3,2,2,9
P,D = pattern(Q,R,r)
bad = [u for u in range(D) if not P[u,u]]
Pb = P[bad]                       # 32 x 64 pattern (True = free)
T = np.zeros((len(bad),D)); T[range(len(bad)),bad] = 1.0   # forced values off pattern
GRID = np.array([0,1,-1,2,-2,0.5,-0.5,3,-3,1.5,-1.5,4,-4])
def solve(seed, iters=4000):
    rng=np.random.default_rng(seed)
    free = Pb.copy(); fixedval = T.copy()
    Z = np.where(free, rng.standard_normal(Pb.shape), T)
    for rnd in range(200):
        for _ in range(iters if rnd==0 else 600):
            U,s,Vt=np.linalg.svd(Z,full_matrices=False); Zk=(U[:,:k]*s[:k])@Vt[:k]
            Z=np.where(free,Zk,fixedval)
        s=np.linalg.svd(Z,compute_uv=False)
        if s[k]/s[0]>1e-6 and rnd>0: return None
        if not free.any(): return Z
        # snap the free entry closest to the grid
        cand=np.where(free)
        vals=Z[cand]; dist=np.abs(vals[:,None]-GRID[None,:]); j=dist.min(1)
        order=np.argsort(j)[:max(1,len(order0:=j)//25)]
        for o in order:
            i,w=cand[0][o],cand[1][o]; g=GRID[dist[o].argmin()]
            free[i,w]=False; fixedval[i,w]=g; Z[i,w]=g
    return None
for seed in range(int(sys.argv[1]) if len(sys.argv)>1 else 12):
    Z=solve(seed)
    if Z is None: print("seed",seed,"failed",flush=True); continue
    Zq=sp.Matrix([[sp.Rational(Fraction(x).limit_denominator(4)) for x in row] for row in Z])
    rk=Zq.rank()
    ok=all((Zq[i,w]==(1 if w==bad[i] else 0)) for i in range(len(bad)) for w in range(D) if not Pb[i,w])
    print("seed",seed,"exact rank",rk,"constraints ok",ok,flush=True)
    if rk<=9 and ok:
        json.dump({"Q":Q,"R":R,"r":r,"bad_rows":bad,"Z":[[str(x) for x in row] for row in Zq.tolist()]},
                  open("routing_rank9_certificate.json","w"))
        print("CERTIFICATE WRITTEN"); break
