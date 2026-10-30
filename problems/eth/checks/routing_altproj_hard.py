import numpy as np, sys
from routing_minrank_experiment import pattern
def run(Q,R,r,k,seeds=8,iters=6000):
    P,D = pattern(Q,R,r); I=np.eye(D); best=1
    for sd in range(seeds):
        rng=np.random.default_rng(sd)
        A = I + rng.standard_normal((D,D))*P*rng.uniform(0.05,1.0)
        for it in range(iters):
            U,s,Vt=np.linalg.svd(A); Ak=(U[:,:k]*s[:k])@Vt[:k]
            A=np.where(P,Ak,I)
        s=np.linalg.svd(A,compute_uv=False); best=min(best,s[k]/s[0])
    return best
for (Q,R,r,k) in [(2,2,3,8),(3,2,2,9)]:
    print(Q,R,r,"rank",k,"best normalized sigma_{k+1}:",run(Q,R,r,k),flush=True)
