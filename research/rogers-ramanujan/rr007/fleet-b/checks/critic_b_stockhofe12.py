"""Bounded audit of the actual RR003 endpoint only; no legacy test imports."""
import json
import sys
from pathlib import Path
sys.path.insert(0,str(Path('research/rogers-ramanujan/checks').resolve()))
import rr003_stockhofe as endpoint

N=12
alpha=(0,1,3,6,8)
def f(h):
    q,r=divmod(h,5)
    return 9*q+alpha[r]
heights=tuple(h for h in range(1,5*N+1) if f(h)<=N)
U=set()
def flat(tail,left):
    U.add(tuple(f(h) for h in tail[:-1]))
    for h in heights:
        if f(h)<=left and 0<=h-tail[0]<=4:
            flat((h,)+tail,left-f(h))
flat((0,),N)
B=set()
parts=tuple(x for x in range(1,N+1) if x%9 in (1,3,6,8))
def residue(p,left,minimum):
    B.add(p)
    for x in parts:
        if minimum<=x<=left: residue(p+(x,),left-x,x)
residue((),N,1)
image=set()
for u in U:
    b=endpoint.columns_to_residue(u)
    assert b in B and endpoint.residue_to_columns(b)==u and sum(u)==sum(b)<=N
    image.add(b)
for b in B:
    u=endpoint.residue_to_columns(b)
    assert u in U and endpoint.columns_to_residue(u)==b and sum(u)==sum(b)<=N
assert image==B
report={'bound':N,'status':'passed','U':len(U),'B':len(B),
        'U_distinct':sum(len(set(u))==len(u) for u in U),
        'U_repeated':sum(len(set(u))<len(u) for u in U),
        'B_distinct':sum(len(set(b))==len(b) for b in B),
        'B_repeated':sum(len(set(b))<len(b) for b in B),
        'max_actual_weight':max(map(sum,U|B)),
        'scope':'actual RR003 Stockhofe endpoint; separate RR007 critic pilot12',
        'imports':'endpoint module and its definition-only kr1 dependency; no legacy tests'}
Path('.runs/rr007/critic-b-stockhofe-12.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report))
