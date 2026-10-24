from collections import Counter
from pathlib import Path
from math import isqrt
import hashlib,json,sys,time
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[4]
sys.path.insert(0,str(ROOT/'research/rogers-ramanujan/checks'))
import kr1
import rr003_revision as author
import rr003_recursive as rec
START=time.monotonic()
freeze=json.loads((ROOT/'research/rogers-ramanujan/rr003/round-2-freeze.json').read_text())
for name,digest in freeze['frozen_sha256'].items(): assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest,name
# Independently written round-one formulas and literal actual-U predicate.
exec(Path(__file__).with_name('critic1.py').read_text().split('checks=Counter(); rows=[]; missing=[]')[0].replace('import rr003_columns as author','import rr003_columns as old_author').replace('START=time.monotonic()',''))
import rr003_revision as author

def all_clusters(n):
    for a in range(isqrt(n)+1):
        for b in range(isqrt(n//3)+1):
            r=n-a*a-3*a*b-3*b*b
            if r<0: continue
            for ns in range(r//3+1):
                for nu in vec(b,ns):
                    for mu in vec(a,r-3*ns): yield a,b,mu,nu

def support(c):
    a,b,mu,nu=c
    return a<=1 or a==2 and (b==0 or mu[0] not in (4,5,9))

def fwd(c):
    a,b,mu,nu=c
    if a<=1 or a==2 and mu[0]<=1:return forward(c)
    if not support(c):return None
    k,v=mu;t=v-k
    if b==0:
        j,r=divmod(k-2,3)
        u=[6]*j+[1]*(t+(r==1))+([8] if r==0 else [9] if r==1 else [9,3])
    else:
        y=(k+2)%4;x=(k+2-5*y)//4
        assert x>=0 and 0<=y<=3 and x+y>0
        u=[8]*x+[10]*y+[1]*t+[3*b]
        for q in range(1,b+1):
            d=nu[b-q]-(nu[b-q-1] if b-q else 0)
            u.extend([3*q]*(2+d))
    return tuple(sorted(u,reverse=True))

def inv(u):
    old=inverse(u)
    if old is not None:return old
    s=u.count(1);m=Counter(v for v in u if v!=1)
    if m[3]>=2 and (m[8] or m[10]):
        x=m.pop(8,0);y=m.pop(10,0)
        if y>3 or any(v%3 for v in m):return None
        b=max(m)//3
        if set(m)!=set(range(3,3*b+1,3)) or m[3*b]<3 or any(m[3*j]<2 for j in range(1,b)):return None
        ds=[m[3*j]-2-(j==b) for j in range(1,b+1)]
        nu=tuple(sum(ds[b-i:]) for i in range(1,b+1))
        k=4*x+5*y-2
        return 2,b,(k,k+s),nu
    j=m.pop(6,0)
    if m=={8:1}:k,t=3*j+2,s
    elif m=={9:1} and s>=1:k,t=3*j+3,s-1
    elif m=={9:1,3:1}:k,t=3*j+4,s
    else:return None
    return 2,0,(k,k+t),()

def changed(u,rem,add):
    v=list(u)
    for x in rem:v.remove(x)
    return tuple(sorted(v+list(add),reverse=True))

def next_rule(c,u):
    a,b,(k,v),nu=c
    if b==0:
        if k==0:return changed(u,(3,1),(6,))
        if k==1:return changed(u,(6,),(8,))
        rem,add=(((8,),(9,1)),((1,),(3,)),((9,3),(8,6)))[(k-2)%3]
        return changed(u,rem,add)
    if k==0:return changed(u,(3*(b+1),1),(3*(b+2),))
    if k==1:return changed(u,(3*(b+2),),(3*b,8))
    y=(k+2)%4;x=(k+2-5*y)//4
    if y==3:return changed(u,(10,)*3,(8,)*4)
    if x:return changed(u,(8,),(10,))
    return None

counts=Counter();first_u=first_c=None;last=None
for n in range(31):
    actual={p for p in parts(n) if is_u(p)}
    assert actual=={kr1.weighted_columns(w) for w in kr1.weighted_partitions(n)}
    cs=set(all_clusters(n));assert cs=={(c.a,c.b,c.mu,c.nu) for c in kr1.cluster_data(n)}
    images={}
    for c in cs:
        ac=kr1.ClusterData(*c)
        assert support(c)==author.supported(ac)
        if not support(c):
            if first_c is None:first_c=(n,c)
            continue
        u=fwd(c)
        assert u in actual and sum(u)==n and inv(u)==c,(c,u,inv(u))
        assert u not in images,('collision',c,images[u],u)
        images[u]=c
        assert author.reconstruct_columns(ac)==u and author.decompose_columns(u)==ac
        counts['C_roundtrips']+=1
        a,b,mu,nu=c
        if a!=2:continue
        k,v=mu;up=(a,b,(k+1,v+1),nu)
        raise_func=author.raise_common_mixed_columns if b else author.raise_common_columns
        lower_func=author.lower_common_mixed_columns if b else author.lower_common_columns
        if support(up):
            expected=next_rule(c,u)
            assert expected==fwd(up) and is_u(expected) and sum(expected)==n+2
            assert raise_func(u)==expected and lower_func(expected)==u and inv(expected)==up
            counts['mixed_common_carries' if b else 'zero_pair_common_carries']+=1
        else:
            assert next_rule(c,u) is None
            try:raise_func(u)
            except author.OutsideRestrictedDomain:counts['unsupported_successor_rejected']+=1
            else:raise AssertionError(('unsupported successor accepted',c))
        if k>0:
            down=(a,b,(k-1,v-1),nu)
            if support(down):
                lower=lower_func(u)
                assert lower==fwd(down) and raise_func(lower)==u
                counts['lower_branches']+=1
            else:
                try:lower_func(u)
                except author.OutsideRestrictedDomain:counts['unsupported_predecessor_rejected']+=1
                else:raise AssertionError(('unsupported predecessor accepted',c))
    recognized=set()
    for u in actual:
        c=inv(u)
        try:ac=author.decompose_columns(u)
        except author.OutsideRestrictedDomain:ac=None
        if c is None:
            assert ac is None
            if first_u is None:first_u=(n,u)
        else:
            assert fwd(c)==u and ac==kr1.ClusterData(*c)
            recognized.add(u);counts['U_roundtrips']+=1
    assert set(images)==recognized
    last={'n':n,'actual_U':len(actual),'restricted':len(images),'uncovered':len(actual)-len(images)}
# Explicit high-k witnesses, not an enumeration sweep above 30.
high=[]
for c in ((2,1,(13,13),(0,)),(2,1,(13,16),(2,)),(2,2,(13,13),(0,2)),(2,1,(14,14),(0,)),(2,1,(17,18),(1,))):
    u=fwd(c);assert is_u(u) and inv(u)==c and author.decompose_columns(u)==kr1.ClusterData(*c)
    assert author.reconstruct_columns(kr1.ClusterData(*c))==u
    a,b,(k,v),nu=c;up=(a,b,(k+1,v+1),nu)
    raised=next_rule(c,u)
    assert raised==fwd(up) and author.raise_common_mixed_columns(u)==raised
    assert author.lower_common_mixed_columns(raised)==u and inv(raised)==up
    if k==13:assert u.count(10)==3 and raised.count(8)==4 and not raised.count(10)
    high.append({'C':c,'U':u,'raised_U':raised,'weight':sum(u)})
# Literal independent gap/residue predicates and grammar.
def gap(p):
    return all(x<=y for x,y in zip(p,p[1:])) and all(p[i+2]-p[i]>=3 for i in range(len(p)-2)) and all(y-x>1 or (x+y)%3==0 for x,y in zip(p,p[1:]))
def residue(p):return all(x%9 in (1,3,6,8) for x in p)
tails=((),(1,),(1,2),(1,3),(2,),(3,),(3,3))
links=tuple(frozenset(j for j,r in enumerate(tails) if gap(t+tuple(x+3 for x in r))) for t in tails)
assert links==rec.LINKS
for i,t in enumerate(tails):
    for j,r in enumerate(tails):
        expected=t+tuple(x+3 for x in r)
        if j in links[i]:assert rec.gap_unstrip(i,r)==expected
        else:
            try:rec.gap_unstrip(i,r)
            except ValueError:pass
            else:raise AssertionError(('forbidden link',i,j))
        counts['links_checked']+=1

def glaisher(p):
    out=[]
    for v,m in Counter(p).items():
        power=1
        while m:
            d=m%3;m//=3;out.extend([v*power]*d);power*=3
    return tuple(sorted(out))
def unglaisher(p):
    out=[]
    for x in p:
        m=1
        while x%9==0:x//=3;m*=3
        out.extend([x]*m)
    return tuple(sorted(out))
def insert(p):
    cs=Counter(x//3 for x in p);i=0;total=sum(p)+1;trace=[]
    while True:
        assert all(0<=m<=2 for j,m in cs.items() if j)
        assert 3*i+1+sum(3*j*m for j,m in cs.items() if j)==total
        if i>0 and cs[i]>0:
            cs[i]-=1;cs[i-1]+=1;i+=1;trace.append('single')
        elif cs[i+1]==2:
            cs[i+1]=0
            if i:cs[i]+=2
            i+=2;trace.append('double')
        else:break
        assert i>=2 and cs[i-1]<=1
        assert 3*i+1<=total
    assert cs[i]==0 and cs[i+1]<=1
    out=tuple(sorted([3*i+1]+[3*j for j,m in cs.items() if j for _ in range(m)]))
    assert gap(out) and sum(out)==total
    return out,trace
seen_insert={}
for n in range(31):
    ps={p[::-1] for p in parts(n)}
    aa={p for p in ps if gap(p)};bb={p for p in ps if residue(p)}
    assert aa==set(kr1.gap_partitions(n)) and bb==set(kr1.residue_partitions(n))
    for p in aa:
        t=tuple(x for x in p if x<=3);r=tuple(x-3 for x in p if x>3);i=tails.index(t)
        assert gap(r) and tails.index(tuple(x for x in r if x<=3)) in links[i]
        assert rec.gap_strip(p)==(i,r) and rec.gap_unstrip(i,r)==p
        assert sum(p)==sum(t)+sum(r)+3*len(r)
        counts['gap_grammar_roundtrips']+=1
        if all(x%3==0 for x in p):
            b=unglaisher(p)
            assert residue(b) and glaisher(b)==p and rec.unglaisher_three(p)==b
            counts['Glaisher_A_roundtrips']+=1
            if n+1<=30:
                out,trace=insert(p)
                assert rec.refuted_insert_one(p)==out
                assert out not in seen_insert or seen_insert[out]==p
                seen_insert[out]=p;counts['insertion_small_cores']+=1
    for p in bb:
        ds=tuple(p.count(x) for x in (1,3,6,8));r=tuple(x-9 for x in p if x>9)
        assert residue(r) and rec.residue_strip(p)==(ds,r) and rec.residue_unstrip(ds,r)==p
        assert sum(p)==sum(x*m for x,m in zip((1,3,6,8),ds))+sum(r)+9*len(r)
        counts['residue_grammar_roundtrips']+=1
        if all(x%3==0 for x in p):
            a=glaisher(p)
            assert gap(a) and sum(a)==n and unglaisher(a)==p and rec.glaisher_three(p)==a
            counts['Glaisher_B_roundtrips']+=1
P=(3,3,6,9,9,12);Q=(3,3,6,6,12,12)
p,pt=insert(P);q,qt=insert(Q)
assert p==q==(3,6,9,9,16) and P!=Q and pt==['double','single','single','single'] and qt==['double','single','double']
assert rec.refuted_insert_one(P)==p and rec.refuted_insert_one(Q)==q
assert rec.unglaisher_three(P)==(3,)*8+(6,12)
assert rec.unglaisher_three(Q)==(3,3,6,6,12,12)
result={'verdict':'restricted extension supported; universal objective incomplete; insertion refuted','counts':dict(counts),'first_uncovered_U':first_u,'first_unsupported_C':first_c,'at_30':last,'high_k_direct_witnesses':high,'insertion_collision':{'cores':(P,Q),'image':p,'rule_words':(pt,qt)},'elapsed_seconds':time.monotonic()-START,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
print(json.dumps(result,indent=2))
