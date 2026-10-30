"""Start from converged numeric rank-9 completions; greedily force free entries to 0
(keeping rank <= 9 numerically) to expose an exact sparse structure."""
import numpy as np, sys
from routing_minrank_experiment import pattern
Q,R,r,k=3,2,2,9
P,D=pattern(Q,R,r); bad=[u for u in range(D) if not P[u,u]]
import os
S=os.environ.get("ETH_SCRATCH",".runs/eth/")+"/"
os.makedirs(S,exist_ok=True)
Pb=P[bad]; T=np.zeros((32,D)); T[range(32),bad]=1
def proj(Z,free,fixed,it):
    for _ in range(it):
        U,s,Vt=np.linalg.svd(Z,full_matrices=False); Z=np.where(free,(U[:,:k]*s[:k])@Vt[:k],fixed)
    s=np.linalg.svd(Z,compute_uv=False); return Z,s[k]/s[0]
for sd in [4,6,7]:
    Z=(np.eye(D)-(np.eye(D)-np.load(S+f"rank9_seed{sd}.npy")))[bad]  # rows of A
    free=Pb.copy(); fixed=T.copy()
    Z,res=proj(Z,free,fixed,50); print("seed",sd,"start residual",res,"free",free.sum())
    stalls=0
    while stalls<40:
        cand=np.argwhere(free); vals=np.abs(Z[free]); o=np.argsort(vals)
        trial_ok=False
        for idx in o[:20]:
            i,w=cand[idx]; f2=free.copy(); f2[i,w]=False
            Z2,res2=proj(np.where(f2,Z,fixed),f2,fixed,300)
            if res2<1e-9: free=f2; Z=Z2; trial_ok=True; break
        if not trial_ok: stalls+=40
    nz=np.abs(Z[free])>1e-9
    print("  remaining free entries:",int(free.sum()),"nonzero among them:",int(nz.sum()),"residual",proj(Z,free,fixed,10)[1],flush=True)
    np.save(S+f"rank9_sparse_seed{sd}.npy",np.where(free,Z,fixed)); np.save(S+f"rank9_free_seed{sd}.npy",free)
