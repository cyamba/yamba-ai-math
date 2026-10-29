"""Classify what the preserved naive-carry falsifier actually refutes."""
import importlib.util
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('critic_final',HERE/'kr-final-check.py')
mod=importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
b=mod.base
cs=sorted(b.c_census(40),key=lambda c:(c.weight,c.a,c.b,c.mu,c.nu))
checked=0
collisions=[]
for c in cs:
    if c.a!=4 or c.b or c.mu[1]!=c.mu[2]:
        continue
    x,t,z=c.mu[0],c.mu[1]-c.mu[0],c.mu[3]-c.mu[2]
    q,r=divmod(x,2)
    if r or t<3:
        continue
    u=(8,)*(q+2)+(3,)*t+(1,)*z
    assert sum(u)==c.weight<=40
    checked+=1
    try:
        old=b.m.h1_inverse(u)
    except b.m.Outside:
        continue
    collisions.append({'source':str(c),'U':u,'H1_source':str(old)})
u=(8,8,3,3,3)
aux=b.m.g_inverse(u)
assert aux==b.m.kr1.ClusterData(2,1,(6,6),(0,))
try:
    b.m.h1_inverse(u)
except b.m.Outside:
    h1_rejects=True
else:
    h1_rejects=False
assert h1_rejects
out={'bound':40,'naive_even_sources_with_t_at_least_three':checked,
     'actual_H1_intersections':collisions,'preserved_weight25_U':u,
     'preserved_weight25_auxiliary_g_source':str(aux),
     'preserved_weight25_H1_rejects':h1_rejects,
     'interpretation':'The named weight25 witness refutes disjointness from auxiliary g; by itself it does not refute extension of H1.'}
dest=HERE/'kr-final-naive-audit.json'
if dest.exists():
    raise FileExistsError(dest)
dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
