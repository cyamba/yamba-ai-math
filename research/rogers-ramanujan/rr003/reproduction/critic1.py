from collections import Counter
from pathlib import Path
import hashlib,json,sys,time
ROOT=Path(__file__).resolve().parents[4]
sys.path.insert(0,str(ROOT/'research/rogers-ramanujan/checks'))
import kr1
import rr003_columns as author
START=time.monotonic()

def parts(n,upper=None):
    if n==0:
        yield ()
        return
    for x in range(min(n, upper if upper is not None else n),0,-1):
        for tail in parts(n-x,x): yield (x,)+tail

def height(x):
    q,r=divmod(x,9)
    for s,w in enumerate((0,1,3,6,8)):
        if r==w: return 5*q+s
    return None

def is_u(u):
    hs=tuple(height(x) for x in u)
    return all(h is not None and h>0 for h in hs) and all(0<=x-y<5 for x,y in zip(hs,hs[1:]+(0,)))

def vec(k,total,lo=0):
    if k==0:
        if total==0: yield ()
        return
    for x in range(lo,total//k+1):
        for rest in vec(k-1,total-x,x): yield (x,)+rest

def clusters(n):
    for a in range(3):
        for b in range(n+1):
            r=n-a*a-3*a*b-3*b*b
            if r<0: break
            for ns in range(r//3+1):
                for nu in vec(b,ns):
                    for mu in vec(a,r-3*ns):
                        if a<2 or mu[0]<=1: yield (a,b,mu,nu)

def forward(c):
    a,b,mu,nu=c
    u=[]
    for j in range(1,b+1):
        d=nu[b-j]-(nu[b-j-1] if b-j else 0)
        m=2+d-(a==0 and j==b)
        u.extend([3*j]*m)
    if a==1: u.extend([1]*(mu[0]+1))
    if a==2:
        u.extend([3*(b+1+mu[0])])
        u.extend([1]*(mu[1]+1-2*mu[0]))
    return tuple(sorted(u,reverse=True))

def inverse(u):
    if not is_u(u): raise ValueError('invalid')
    s=u.count(1)
    v=Counter(x//3 for x in u if x!=1)
    if any(x!=1 and x%3 for x in u): return None
    if not v:
        return (1,0,(s-1,),()) if s else (0,0,(),())
    L=max(v)
    if set(v)==set(range(1,L+1)) and all(v[j]>=2 for j in range(1,L)):
        if s==0: a,b,mu=0,L,()
        elif v[L]>1: a,b,mu=1,L,(s-1,)
        else: a,b,mu=2,L-1,(0,s-1)
    elif L>=2 and set(v)==set(range(1,L-1))|{L} and v[L]==1 and all(v[j]>=2 for j in range(1,L-1)):
        a,b,mu=2,L-2,(1,s+1)
    else: return None
    d=[v[j]-2+(a==0 and j==b) for j in range(1,b+1)]
    return a,b,mu,tuple(sum(d[b-i:]) for i in range(1,b+1))

checks=Counter(); rows=[]; missing=[]
for n in range(31):
    actual={p for p in parts(n) if is_u(p)}
    author_actual={kr1.weighted_columns(w) for w in kr1.weighted_partitions(n)}
    assert actual==author_actual,('actual-domain',n,actual^author_actual)
    cs=set(clusters(n))
    author_cs={(c.a,c.b,c.mu,c.nu) for c in kr1.cluster_data(n) if author.supported(c)}
    assert cs==author_cs,('cluster-domain',n,cs^author_cs)
    images={}
    for c in cs:
        u=forward(c)
        assert u in actual and sum(u)==n and inverse(u)==c,(c,u,inverse(u))
        assert u not in images,('collision',c,images[u],u)
        images[u]=c
        ac=kr1.ClusterData(*c)
        assert author.reconstruct_columns(ac)==u
        assert author.decompose_columns(u)==ac
        a,b,mu,nu=c
        for j in range(1,b+1):
            dnu=nu[:-j]+tuple(x+1 for x in nu[-j:])
            up=tuple(sorted(u+(3*j,),reverse=True))
            assert forward((a,b,mu,dnu))==up and is_u(up)
            assert inverse(up)==(a,b,mu,dnu)
            low=list(up);low.remove(3*j)
            assert tuple(low)==u
            checks['nu_operations']+=1
        if mu:
            mu2=mu[:-1]+(mu[-1]+1,)
            up=tuple(sorted(u+(1,),reverse=True))
            assert forward((a,b,mu2,nu))==up and inverse(up)==(a,b,mu2,nu)
            assert up[:-1]==u
            checks['mu_last_operations']+=1
        if a==2 and mu[0]==0:
            target=(a,b,(1,mu[1]+1),nu)
            v=list(u);v.remove(3*(b+1));v.remove(1);v.append(3*(b+2));v=tuple(sorted(v,reverse=True))
            assert is_u(v) and sum(v)==n+2 and forward(target)==v and inverse(v)==target
            w=list(v);w.remove(3*(b+2));w.extend([3*(b+1),1]);w=tuple(sorted(w,reverse=True))
            assert w==u
            checks['merge_split_operations']+=1
        checks['cluster_roundtrips']+=1
    recognized=set()
    for u in actual:
        c=inverse(u)
        if c is None:
            try: author.decompose_columns(u)
            except author.OutsideRestrictedDomain: pass
            else: raise AssertionError(('author false accept',u))
            if len(missing)<1:missing.append({'weight':n,'u':u})
        else:
            assert forward(c)==u and c in cs
            assert kr1.ClusterData(*c)==author.decompose_columns(u)
            recognized.add(u)
            checks['column_roundtrips']+=1
    assert set(images)==recognized
    rows.append({'n':n,'actual_U':len(actual),'restricted':len(images),'uncovered':len(actual)-len(images)})
assert is_u((8,)) and inverse((8,)) is None
assert not is_u((10,)) and not is_u((10,1)) and not is_u((11,3,3))
# Terminal and accepted malformed-domain controls.
for u in ((10,),(10,1),(11,),(3,1,3),(0,),(-1,)):
    try: author.decompose_columns(u)
    except ValueError: pass
    else: raise AssertionError(('accepted invalid U',u))
result={'verdict':'independent restricted checks passed; universal bridge incomplete','ceiling':30,'counts':dict(checks),'first_uncovered':missing,'at_30':rows[-1],'elapsed_seconds':time.monotonic()-START,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'rows':rows}
print(json.dumps(result,indent=2))
