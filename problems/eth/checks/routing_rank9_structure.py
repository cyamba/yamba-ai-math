import numpy as np, itertools
from routing_minrank_experiment import pattern
Q,R,r=3,2,2
P,D=pattern(Q,R,r)
import os
S=os.environ.get("ETH_SCRATCH",".runs/eth/")+"/"
os.makedirs(S,exist_ok=True)
# product eigenbasis of the swaps; per position basis over (a,d) in order 00,01,10,11
plus=[np.array([1,0,0,0.]),np.array([0,0,0,1.]),np.array([0,1,1,0.])/np.sqrt(2)]
minus=[np.array([0,1,-1,0.])/np.sqrt(2)]
labels=list(itertools.product(range(r),repeat=2*Q))
def pos_index(l,s): return 2*l[s]+l[Q+s]
basis=[];levels=[]
for choice in itertools.product(range(4),repeat=Q):
    vecs=[(plus+minus)[c] for c in choice]
    v=np.array([np.prod([vecs[s][pos_index(l,s)] for s in range(Q)]) for l in labels])
    basis.append(v); levels.append(sum(c==3 for c in choice))
B=np.array(basis).T; levels=np.array(levels)
for sd in [4,6,7]:
    A=np.load(S+f"rank9_seed{sd}.npy")
    U,s,Vt=np.linalg.svd(A); row=Vt[:9]; col=U[:,:9]
    Rb=row@B; Cb=col.T@B   # coordinates in eigenbasis
    print("seed",sd,"row-space weight by antisymmetric level:",[round(float((Rb[:,levels==j]**2).sum()),3) for j in range(Q+1)],
          " col-space:",[round(float((Cb[:,levels==j]**2).sum()),3) for j in range(Q+1)])
    M=np.eye(D)-A
    print("   max|M| on pattern:",round(float(np.abs(M[P]).max()),3)," nonzeros>1e-6:",int((np.abs(M)>1e-6).sum()), " pattern size:",int(P.sum()))
