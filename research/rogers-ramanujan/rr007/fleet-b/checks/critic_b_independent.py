"""Distinct critic's literal finite pilot. No author/legacy imports."""
import json
from pathlib import Path

N = 12
A = (0, 1, 3, 6, 8)
Z = (0, 0, 0)
def eps(x, y): return int(x < y)
def cost(p): return 9*p[0] + A[p[1]] + A[p[2]]
def base(x, y):
    n,i,j=x; q,l,m=y
    return eps(i,j)+2*eps(j,l)+eps(l,m)
def corr(x,y,star):
    n,i,j=x; q,l,m=y
    if j==l==0 and i and m: return eps(i,m)
    if i==0 and j and l and m and eps(j,l): return -1
    if j==0 and i and l and m and not eps(i,l): return -1
    if m==0 and j and l and not eps(j,l) and (i or not star): return 1
    if l==0 and i and j and m and eps(j,m): return 1
    return 0
def ordered(x,y,star): return x[0]-y[0]>=base(x,y)+2*corr(x,y,star)
def words(parts, tail, adj, w):
    result=set()
    def step(v,budget):
        result.add(v)
        for p in parts:
            c=w(p)
            if c<=budget and (not v or adj(p,v[0])):
                step((p,)+v,budget-c)
    step(tail,N)
    return result

# Literal primary heights; terminal height is fixed at zero.
def hc(h):
    q,r=divmod(h,5)
    return 9*q+A[r]
height_parts=tuple(h for h in range(1,5*N+1) if hc(h)<=N)
u_padded=words(height_parts,(0,),lambda h,k:0<=h-k<=4,hc)
U={v[:-1] for v in u_padded}

# The independent F2 generator knows only secondary parity and flat energies.
all_secondary=tuple((n,i,j) for n in range(N//9+1) for i in range(5) for j in range(5)
                    if n>=eps(i,j) and (n-eps(i,j))%2==0 and 0<cost((n,i,j))<=N)
F=words(all_secondary,(Z,),lambda x,y:x[0]-y[0]==base(x,y),cost)
reg_parts=tuple(p for p in all_secondary if p[1:]!=(0,0))
R=words(reg_parts,(Z,),lambda x,y:ordered(x,y,False),cost)
T=words(reg_parts,(Z,),lambda x,y:ordered(x,y,True),cost)

def lift(u):
    prim=[divmod(h,5) for h in u]
    # Pad to the next EVEN length with at least two ground zeros.
    prim.extend([(0,0)]*(2+len(u)%2))
    return tuple((p[0]+q[0],p[1],q[1]) for p,q in zip(prim[::2],prim[1::2]))
def unlift(v):
    h=[]
    for n,i,j in v:
        lo=(n-eps(i,j))//2
        h.extend((5*(lo+eps(i,j))+i,5*lo+j))
    while h and h[-1]==0: h.pop()
    return tuple(h)
assert {lift(u) for u in U}==F
for u in U:
    assert unlift(lift(u))==u and sum(map(hc,u))==sum(map(cost,lift(u)))<=N
for v in F:
    assert lift(unlift(v))==v and sum(map(cost,v))==sum(map(hc,unlift(v)))<=N

# Literal C and the exact B2 image. Do not use the KR1 A endpoint.
def wt(c):
    a,b,mu,nu=c
    return a*a+3*a*b+3*b*b+sum(mu)+3*sum(nu)
def vectors(k,budget,minimum=0):
    if not k:
        yield ()
    else:
        for x in range(minimum,budget//k+1):
            for z in vectors(k-1,budget-x,x): yield (x,)+z
C=set()
for a in range(N+1):
    for b in range(N+1):
        q=a*a+3*a*b+3*b*b
        if q>N: continue
        for mu in vectors(a,N-q):
            for nu in vectors(b,(N-q-sum(mu))//3): C.add((a,b,mu,nu))
def cone(c):
    a,b,mu,nu=c
    return (a,b)==(0,0) or (a,b) in ((1,0),(0,1),(1,1)) or (
        (a,b)==(2,0) and (mu[0]==0 or mu[0]%3!=0)) or (
        (a,b)==(3,0) and (mu[1]-mu[0])%3!=2) or (
        (a,b)==(4,0) and mu[0]%2==0 and (mu[2]-mu[1])%3==0)
I={c for c in C if cone(c)}
empty=(0,0,(),())
def bc(v):
    m,n,t,s=v
    if m>1:
        k=2*m-4
        return (4,0,(k,k+t,k+t+3*n,k+t+3*n+s),())
    if m==1:
        if t: return (3,0,(t-1,t+3*n,t+3*n+s),())
        return (2,0,(2+3*n,2+3*n+s),())
    if n:
        if t: return (3,0,(t-1,t+3*n-4,t+3*n-4+s),())
        return (2,0,(3*n-2,3*n-2+s),())
    if not t: return empty if not s else (1,0,(s-1,),())
    if not s: return (0,1,(),(t-1,))
    if t==1: return (2,0,(0,s-1),())
    return (1,1,(s-1,),(t-2,))
def cb(c):
    a,b,x,y=c
    if a+b==0: return (0,0,0,0)
    if a==0: return (0,0,y[0]+1,0)
    if a==1 and b==0: return (0,0,0,x[0]+1)
    if b==1: return (0,0,y[0]+2,x[0]+1)
    if a==2:
        k=x[0]
        if k==0: return (0,0,1,x[1]+1)
        if k%3==1: return (0,(k+2)//3,0,x[1]-k)
        return (1,(k-2)//3,0,x[1]-k)
    if a==3:
        d=x[1]-x[0]
        return ((0,d//3+1,x[0]+1,x[2]-x[1]) if d%3==0 else
                (1,(d-1)//3,x[0]+1,x[2]-x[1]))
    return (x[0]//2+2,(x[2]-x[1])//3,x[1]-x[0],x[3]-x[2])
B={(m,n,t,s) for m in range(N//8+1) for n in range(N//6+1)
   for t in range(N//3+1) for s in range(N+1) if 8*m+6*n+3*t+s<=N}
def bw(v): return sum(x*y for x,y in zip(v,(8,6,3,1)))
assert {bc(v) for v in B}==I
for v in B: assert cb(bc(v))==v and bw(v)==wt(bc(v))<=N
for c in I: assert bc(cb(c))==c and wt(c)==bw(cb(c))<=N

# Intrinsic R20 is generated from the entire printed R2 domain above.
R0={v for v in R if all(p[0]==0 for p in v)}
def bzero(b):
    seq=[i for i,k in zip((4,3,2,1),b) for _ in range(k)]
    out=[]
    if len(seq)%2: out.append((0,seq.pop(0),0))
    out.extend((0,i,j) for i,j in zip(seq[::2],seq[1::2]))
    return tuple(out)+(Z,)
def zerob(v):
    seq=[i for p in v[:-1] for i in p[1:] if i]
    assert seq==sorted(seq,reverse=True)
    return tuple(seq.count(i) for i in (4,3,2,1))
assert {bzero(b) for b in B}==R0
for b in B: assert zerob(bzero(b))==b and sum(map(cost,bzero(b)))==bw(b)<=N
for v in R0: assert bzero(zerob(v))==v and bc(zerob(v)) in I

# Mixed types represented by ('P',raw,c,0) and ('S',raw,i,j).
def mw(p): return 9*p[1]+A[p[2]]+A[p[3]]
def madj(x,y):
    t,n,i,j=x; z,q,l,m=y; d=n-q
    if t==z=='P': return d>eps(i,l)
    if t=='P': return d>=eps(i,l)+eps(l,m)
    if z=='P': return d>eps(i,j)+eps(j,l)
    return d>=eps(i,j)+2*eps(j,l)+eps(l,m)
mixedparts=tuple([('P',n,c,0) for n in range(N//9+1) for c in range(1,5)
                  if 9*n+A[c]<=N]+[('S',n,i,j) for n,i,j in all_secondary if i and j])
M=words(mixedparts,(),madj,mw)
def mt(v):
    out=[]
    for kind,n,i,j in v:
        out.append((n,i,j) if kind=='S' else (n,0,i) if n%2 else (n,i,0))
    return tuple(out)+(Z,)
def tm(v):
    return tuple(('S',n,i,j) if i*j else ('P',n,i+j,0) for n,i,j in v[:-1])
assert {mt(v) for v in M}==T
for v in M: assert tm(mt(v))==v and sum(map(mw,v))==sum(map(cost,mt(v)))<=N
for v in T: assert mt(tm(v))==v and sum(map(cost,v))==sum(map(mw,tm(v)))<=N

witness=((1,0,1),(0,1,0),Z)
assert witness in F and witness in T and witness not in R
def nonground(v): return tuple(i for p in v for i in p[1:] if i)
assert not any(sum(p[0] for p in v)==1 and nonground(v)==(1,1) for v in R)
assert (('P',1,1,0),('P',0,1,0)) in M

report={'bound':N,'status':'passed','independent_U':len(U),'independent_F2':len(F),
        'independent_B0':len(B),'independent_C':len(C),'independent_cone':len(I),
        'independent_R20':len(R0),'independent_M':len(M),'independent_R2star':len(T),
        'independent_printed_R2':len(R),'source_witness_weight':sum(map(cost,witness)),
        'distinct_U':sum(len(set(u))==len(u) for u in U),
        'repeated_U':sum(len(set(u))<len(u) for u in U),
        'distinct_B0':sum(max(b)<=1 for b in B),'repeated_B0':sum(max(b)>1 for b in B),
        'distinct_M':sum(len(set(m))==len(m) for m in M),
        'repeated_M':sum(len(set(m))<len(m) for m in M),
        'max_actual_weight':max([sum(map(hc,u)) for u in U]+[wt(c) for c in C]+
                                [sum(map(cost,v)) for v in F|R|T]),
        'imports':'standard library only; no author/legacy executable imports',
        'scope':'finite evidence only; independent ordinary proof review recorded separately'}
Path('.runs/rr007/critic-b-independent-12.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report))
