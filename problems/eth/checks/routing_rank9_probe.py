import numpy as np
from routing_minrank_experiment import pattern
import os
S=os.environ.get("ETH_SCRATCH",".runs/eth/")+"/"
os.makedirs(S,exist_ok=True)
Q,R,r,k=3,2,2,9
P,D=pattern(Q,R,r); I=np.eye(D)
for sd in range(8):
    rng=np.random.default_rng(sd)
    A = I + rng.standard_normal((D,D))*P*rng.uniform(0.05,1.0)
    hist=[]
    for it in range(40000):
        U,s,Vt=np.linalg.svd(A); Ak=(U[:,:k]*s[:k])@Vt[:k]
        A=np.where(P,Ak,I)
        if it%10000==9999:
            s2=np.linalg.svd(A,compute_uv=False); hist.append((it+1, s2[k], np.abs(A).max(), s2[0]))
    print("seed",sd,[(h[0],f"{h[1]:.2e}",f"max|A|={h[2]:.3g}",f"s1={h[3]:.3g}") for h in hist],flush=True)
    if hist[-1][1]<1e-6:
        np.save(S+f"rank9_seed{sd}.npy",A)
