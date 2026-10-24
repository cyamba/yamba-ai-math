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
# Round-two checks reuse only the critic's independent literal definitions above.
for freeze_name in ('round-2-freeze.json', 'round-2-review-freeze.json'):
    data=json.loads((ROOT/'research/rogers-ramanujan/rr005'/freeze_name).read_text())
    for name,digest in data['source_sha256'].items():
        assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest, name

def eu(u): return ud(u) and ul3(u) is None
def ec(c): return cd(c) and cl3(c) is None

def utype(u):
    if not uv(u): return None
    if 1 not in u and 3 not in u: return 'A'
    if u.count(1)==1 and len(u)>=2 and u[-2]==9: return 'B'
    if u.count(3)!=1 or 1 in u: return None
    if 10 not in u and len(u)>=2 and u[-2]==9: return 'C0'
    if u.count(10)==1:
        above=[H[p] for p in u if H[p]>6]
        if above and min(above)==10: return 'C1'
    return None

def u6(u):
    assert eu(u) and sum(u)+6<=BOUND, ('computational domain cap',u)
    k=utype(u); out=list(u)
    replacements={'A':((),(6,)), 'B':((9,1),(10,6)),
                  'C0':((9,3),(12,6)), 'C1':((18,10,3),(19,12,6))}
    old,new=replacements[k]
    for p in old: out.remove(p)
    return tuple(sorted(out+list(new),reverse=True))

def ul6(u):
    assert eu(u) and sum(u)<=BOUND
    if 1 in u or 3 in u or 6 not in u: return None
    for expected,remove,add in (
        ('A',(6,),()), ('B',(10,6),(9,1)),
        ('C0',(12,6),(9,3)), ('C1',(19,12,6),(18,10,3))):
        out=list(u)
        try:
            for p in remove: out.remove(p)
        except ValueError: continue
        out=tuple(sorted(out+list(add),reverse=True))
        if uv(out) and utype(out)==expected: return out
    return None

def ec_explicit(c):
    if not cv(c): return False
    a,b,m,v=c
    nueq=(not b or v[-1]==(v[-2] if b>1 else 0))
    if a==b==0: return True
    if a==0: return b>=2 and v[-1]==v[-2]
    if a==2: return m[0]==m[1]>=1 and nueq
    if a>=3 and m[-2]==m[-1]:
        return nueq if b else a>=4 and m[-3]==m[-4]
    return False

def c6(c):
    assert ec(c) and cw(c)+6<=BOUND
    a,b,m,v=c
    if a==b==0: return 2,0,(1,1),()
    if a==0: return a,b,m,v[:-2]+tuple(x+1 for x in v[-2:])
    return a,b,m[:-2]+tuple(x+3 for x in m[-2:]),v

def cl6(c):
    assert ec(c) and cw(c)<=BOUND
    a,b,m,v=c
    if c==(2,0,(1,1),()): return 0,0,(),()
    if a==0 and b>=2 and v[-2]>(v[-3] if b>2 else 0):
        return a,b,m,v[:-2]+tuple(x-1 for x in v[-2:])
    if (a==2 and m[0]>=4) or (a>=3 and m[-2]-m[-3]>=3):
        return a,b,m[:-2]+tuple(x-3 for x in m[-2:]),v
    return None

def nf3(x,l1,l3,l6):
    y,n1,n3=nf(x,l1,l3); n6=0
    while (z:=l6(y)) is not None: y=z; n6+=1
    return y,n1,n3,n6

def build3(t,r1,r3,r6):
    x,n1,n3,n6=t
    for _ in range(n6): x=r6(x)
    return rebuild((x,n1,n3),r1,r3)

counts=Counter(); extra={'U':None,'C':None}; types=Counter()
for n in range(BOUND+1):
    us,cs=uenum(n),cenum(n)
    for tag,objs,valid,wt,ise,l1,l3,r1,r3,r6,l6,empty in (
        ('U',us,uv,sum,eu,ul1,ul3,u1,u3,u6,ul6,()),
        ('C',cs,cv,cw,ec,cl1,cl3,c1,c3,c6,cl6,(0,0,(),()))):
        seen={}; seen_normal={}
        for x in objs:
            assert valid(x) and wt(x)==n
            if tag=='U': assert eu(x)==(utype(x) is not None), ('U classification',x)
            else: assert ec(x)==ec_explicit(x), ('C classification',x)
            if ise(x):
                counts[tag+'_E']+=1
                if tag=='U': types[utype(x)]+=1
                if n+6<=BOUND:
                    y=r6(x)
                    assert ise(y) and wt(y)==n+6 and l6(y)==x, ('six forward',tag,x,y)
                    assert y not in seen; seen[y]=x
                    counts[tag+'_six_edges']+=1
                if (z:=l6(x)) is not None:
                    assert ise(z) and wt(z)==n-6 and r6(z)==x, ('six backward',tag,x,z)
                elif x!=empty and extra[tag] is None:
                    extra[tag]={'weight':n,'object':x}
            t=nf3(x,l1,l3,l6)
            assert t not in seen_normal; seen_normal[t]=x
            assert wt(t[0])+t[1]+3*t[2]+6*t[3]==n
            assert l1(t[0]) is None and l3(t[0]) is None and l6(t[0]) is None
            assert build3(t,r1,r3,r6)==x
            counts[tag]+=1
            if t[0]==empty:
                other_empty=(0,0,(),()) if tag=='U' else ()
                target=(other_empty,t[1],t[2],t[3])
                y=build3(target,c1 if tag=='U' else u1,c3 if tag=='U' else u3,c6 if tag=='U' else u6)
                assert (cw(y) if tag=='U' else sum(y))==n
                assert nf3(y,cl1 if tag=='U' else ul1,cl3 if tag=='U' else ul3,cl6 if tag=='U' else ul6)==target
                counts[tag+'_restricted']+=1
                if tag=='U':
                    assert set(x)<={1,3,6}
                    s,t3,m=x.count(1),x.count(3),x.count(6)
                    if m and not t3: assert y==(2,0,(3*m-2,3*m-2+s),())
                    elif m and t3: assert y==(3,0,(t3-1,3*m+t3-4,3*m+t3+s-4),())
            elif tag=='U': assert not(set(x)<={1,3,6})
# Only the two weight-30 sources of the written cost-eight collision are
# executed; their weight-38 common target is checked symbolically in review.
for x in ((2,2,(1,1),(0,0)),(3,1,(3,3,3),(0,))):
    assert cw(x)==30 and ec(x) and cl6(x) is None
assert types['C1']==0, 'C1 must remain symbolic under this cap'
print(json.dumps({'bound':BOUND,'all_computational_inputs_and_edge_endpoints_at_most':30,
                  'both_round_two_freezes_match':True,'counts':dict(counts),
                  'E_U_types':dict(types),'first_unmatched_F_roots':extra,
                  'status':'passed; C1 and cost-eight family reviewed symbolically only'},sort_keys=True))
