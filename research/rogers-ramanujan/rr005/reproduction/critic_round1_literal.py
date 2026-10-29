"""Independent RR005 critic: literal enumeration, no author-module imports."""
from collections import Counter
from functools import lru_cache
import hashlib, json
from pathlib import Path
BOUND = 30
ROOT = Path(__file__).resolve().parents[4]
frozen = json.loads((ROOT/'research/rogers-ramanujan/rr005/round-1-freeze.json').read_text())
for name, digest in frozen['source_sha256'].items():
    assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest() == digest, name
F = lambda h: 9*(h//5)+(0,1,3,6,8)[h%5]
H = {F(h): h for h in range(1, 2*BOUND+20)}
def uv(u):
    if any(x<=0 or x not in H for x in u) or tuple(sorted(u,reverse=True))!=u: return False
    hs=[H[x] for x in u]+[0]
    return all(0<=hs[i]-hs[i+1]<=4 for i in range(len(hs)-1))
def u1(u): return tuple(sorted(u+(1,),reverse=True))
def ul1(u):
    if 1 not in u: return None
    out=list(u); out.remove(1); out=tuple(out)
    return out if uv(out) else None
def ud(u): return uv(u) and (1 not in u or (u.count(1)==1 and len(u)>=2 and u[-2]==9))
def u3(u):
    assert ud(u)
    if 1 not in u: return tuple(sorted(u+(3,),reverse=True))
    out=list(u); out.remove(1); out.remove(9)
    return tuple(sorted(out+[10,3],reverse=True))
def ul3(u):
    assert ud(u)
    if 1 in u or 3 not in u: return None
    out=list(u); out.remove(3)
    if uv(tuple(out)): return tuple(out)
    if 10 not in out: return None
    out.remove(10); out=tuple(sorted(out+[9,1],reverse=True))
    return out if ud(out) else None
@lru_cache(None)
def uenum(n, upper=None, prev=None):
    if n==0: return ((),)
    upper=n if upper is None else min(n,upper)
    ans=[]
    for p,h in H.items():
        if p>upper or (prev is not None and not 0<=prev-h<=4): continue
        for tail in uenum(n-p,p,h):
            u=(p,)+tail
            if uv(u): ans.append(u)
    return tuple(ans)
def cw(c):
    a,b,m,v=c; return a*a+3*a*b+3*b*b+sum(m)+3*sum(v)
def cv(c):
    a,b,m,v=c
    return (a>=0 and b>=0 and len(m)==a and len(v)==b
            and all(isinstance(x,int) and x>=0 for x in m+v)
            and tuple(sorted(m))==m and tuple(sorted(v))==v)
def cd(c):
    a,b,m,v=c
    return cv(c) and (a==0 or (a==2 and m[0]==m[1]>=1) or (a>=3 and m[-2]==m[-1]))
def c1(c):
    a,b,m,v=c
    if a: return a,b,m[:-1]+(m[-1]+1,),v
    if not b: return 1,0,(0,),()
    if v[0]: return 1,b,(0,),tuple(x-1 for x in v)
    return 2,b-1,(0,0),v[1:]
def cl1(c):
    a,b,m,v=c
    if a and m[-1]>(m[-2] if a>1 else 0): return a,b,m[:-1]+(m[-1]-1,),v
    if a==1 and m==(0,): return 0,b,(),tuple(x+1 for x in v)
    if a==2 and m==(0,0): return 0,b+1,(),(0,)+v
    return None
def c3(c):
    assert cd(c)
    a,b,m,v=c
    if a==b==0: return 0,1,(),(0,)
    if b: return a,b,m,v[:-1]+(v[-1]+1,)
    if a==2: return 3,0,(0,m[0]-1,m[0]-1),()
    return a,0,m[:-3]+tuple(x+1 for x in m[-3:]),()
def cl3(c):
    assert cd(c)
    a,b,m,v=c
    if c==(0,1,(),(0,)): return 0,0,(),()
    if b and v[-1]>(v[-2] if b>1 else 0): return a,b,m,v[:-1]+(v[-1]-1,)
    if b==0 and a==3 and m[0]==0: return 2,0,(m[1]+1,m[1]+1),()
    if b==0 and a>=3 and m[-3]>(m[-4] if a>3 else 0): return a,0,m[:-3]+tuple(x-1 for x in m[-3:]),()
    return None
@lru_cache(None)
def vec(k,n,lo=0):
    if not k: return ((),) if n==0 else ()
    return tuple((x,)+t for x in range(lo,n//k+1) for t in vec(k-1,n-x,x))
def cenum(n):
    out=[]
    for a in range(n+1):
        for b in range(n+1):
            q=a*a+3*a*b+3*b*b
            if q>n: break
            for ns in range((n-q)//3+1):
                for v in vec(b,ns):
                    for m in vec(a,n-q-3*ns): out.append((a,b,m,v))
    return out
def nf(x,l1,l3):
    n1=n3=0
    while (y:=l1(x)) is not None: x=y; n1+=1
    while (y:=l3(x)) is not None: x=y; n3+=1
    return x,n1,n3
def rebuild(t,r1,r3):
    x,n1,n3=t
    for _ in range(n3): x=r3(x)
    for _ in range(n1): x=r1(x)
    return x
ru=((),(6,)); rc=((0,0,(),()),(2,0,(1,1),()))
counts=Counter(); extra={'U':None,'C':None}
for n in range(BOUND+1):
    us,cs=uenum(n),cenum(n)
    assert len(us)==len(set(us)) and len(cs)==len(set(cs))
    assert len(us)==len(cs), ('diagnostic count mismatch',n,len(us),len(cs))
    for tag,objs,valid,wt,root,r1,l1,r3,l3 in (
        ('U',us,uv,sum,ud,u1,ul1,u3,ul3), ('C',cs,cv,cw,cd,c1,cl1,c3,cl3)):
        seen1,seen3,seennf={},{},{}
        for x in objs:
            assert valid(x) and wt(x)==n
            assert (l1(x) is None)==root(x), ('D classification',tag,x)
            y=r1(x)
            assert valid(y) and wt(y)==n+1 and l1(y)==x, ('unit',tag,x,y)
            assert y not in seen1; seen1[y]=x
            if (z:=l1(x)) is not None: assert valid(z) and wt(z)==n-1 and r1(z)==x
            if root(x):
                y=r3(x)
                assert root(y) and wt(y)==n+3 and l3(y)==x, ('triple',tag,x,y)
                assert y not in seen3; seen3[y]=x
                if (z:=l3(x)) is not None: assert root(z) and wt(z)==n-3 and r3(z)==x
                elif x not in (ru if tag=='U' else rc) and extra[tag] is None: extra[tag]={'weight':n,'object':x}
                counts[tag+'_D']+=1
            t=nf(x,l1,l3)
            assert t not in seennf; seennf[t]=x
            assert wt(t[0])+t[1]+3*t[2]==n
            assert l1(t[0]) is None and l3(t[0]) is None
            assert rebuild(t,r1,r3)==x, ('normal roundtrip',tag,x,t)
            counts[tag]+=1
            roots=ru if tag=='U' else rc
            if t[0] in roots:
                target=((rc if tag=='U' else ru)[roots.index(t[0])],t[1],t[2])
                y=rebuild(target,c1 if tag=='U' else u1,c3 if tag=='U' else u3)
                other=nf(y,cl1 if tag=='U' else ul1,cl3 if tag=='U' else ul3)
                assert other==target and (cw(y) if tag=='U' else sum(y))==n
                counts[tag+'_restricted']+=1
                if tag=='U': assert set(x)<={1,3,6} and x.count(6)<=1
            elif tag=='U': assert not(set(x)<={1,3,6} and x.count(6)<=1)
for k in (1,2,7,1000):
    for a in (2,3,4,9):
        x=(a,0,(k,)*a,()); assert cd(x) and cl3(c3(x))==x
for x in ((9,1),(9,9,1),(17,9,1),(18,10,3)):
    assert ud(x) and ul3(u3(x))==x
print(json.dumps({'bound':BOUND,'frozen_hashes_match':True,'counts':dict(counts),'first_unmatched_roots':extra,'status':'passed; finite evidence only'},sort_keys=True))
