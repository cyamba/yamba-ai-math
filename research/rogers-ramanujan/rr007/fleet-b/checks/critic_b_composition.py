"""Exact unchanged A3 composed with actual reviewed A/C and U/B endpoints.

Implementation/cohort evidence only. Run from repository root under the
active meter. Bound30 needs root approval after the unchanged pilot12.
No new mathematical rule, candidate, or high-weight legacy test is defined.
"""
import argparse
from collections import Counter
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

ROOT=Path.cwd()
BASE=Path('research/rogers-ramanujan/rr007/fleet-b')
def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def load(name,path):
    spec=importlib.util.spec_from_file_location(name,ROOT/path)
    obj=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj
freeze=json.loads((BASE/'composition-freeze.json').read_text())
for path,h in freeze['pinned_files'].items(): assert sha(path)==h,(path,'pin mismatch')
sys.path.insert(0,str(ROOT/'research/rogers-ramanujan/checks'))
import kr1
import rr003_cluster_merge as ac
import rr003_stockhofe as ub
a3=load('rr007_critic_a_literal',Path('research/rogers-ramanujan/rr007/fleet-a/checks/critic-a-literal.py'))

def ctuple(c): return (c.a,c.b,c.mu,c.nu)
def cobject(c): return kr1.ClusterData(*c)
def gap(p):
    return (all(type(x) is int and x>0 for x in p)
            and tuple(sorted(p))==p
            and all(p[i+2]-p[i]>=3 for i in range(len(p)-2))
            and all(y-x>1 or (x+y)%3==0 for x,y in zip(p,p[1:])))
def residue(p):
    return (all(type(x) is int and x>0 and x%9 in (1,3,6,8) for x in p)
            and tuple(sorted(p))==p)
def enumerate_a(bound):
    out=set()
    def visit(p,left):
        out.add(p)
        for x in range(p[-1] if p else 1,left+1):
            q=p+(x,)
            if gap(q): visit(q,left-x)
    visit((),bound)
    return out
def enumerate_b(bound):
    out=set()
    def visit(p,left):
        out.add(p)
        for x in range(p[-1] if p else 1,left+1):
            if x%9 in (1,3,6,8): visit(p+(x,),left-x)
    visit((),bound)
    return out
def forward(a):
    c=ctuple(ac.gap_to_cluster(a))
    if a3.ctag(c) is None: raise ValueError('outside unchanged A3 domain')
    u=a3.c_to_u(c)
    return ub.columns_to_residue(u)
def inverse(b):
    u=ub.residue_to_columns(b)
    if not a3.utags(u): raise ValueError('outside unchanged A3 image')
    c=a3.u_to_c(u)
    return ac.cluster_to_gap(cobject(c))
def cohort(p): return 'distinct' if len(set(p))==len(p) else 'repeated'

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('bound',type=int,choices=(12,30))
    n=ap.parse_args().bound
    aa,bb=enumerate_a(n),enumerate_b(n)
    domain=set(); image=set(); inverse_domain=set(); inverse_image=set()
    joint=Counter(); branches=Counter(); weights=Counter()
    rows=[]
    for a in sorted(aa,key=lambda p:(sum(p),p)):
        c=ctuple(ac.gap_to_cluster(a))
        assert a3.literal_c(c) and a3.cw(c)==sum(a)<=n
        assert ac.cluster_to_gap(cobject(c))==a
        if a3.ctag(c) is None: continue
        u=a3.c_to_u(c)
        assert a3.literal_u(u) and a3.u_to_c(u)==c
        assert len(a3.utags(u))==1
        b=forward(a)
        assert residue(b) and b in bb and inverse(b)==a
        assert sum(a)==a3.cw(c)==sum(u)==sum(b)<=n
        domain.add(a); image.add(b)
        joint[cohort(a)+'/'+cohort(b)]+=1
        branches[a3.ctag(c)]+=1
        weights[str(sum(a))]+=1
        rows.append({'weight':sum(a),'A':a,'B':b,'C':c,'U':u,
                     'branch':a3.ctag(c),'A_cohort':cohort(a),'B_cohort':cohort(b)})
    for b in bb:
        u=ub.residue_to_columns(b)
        assert a3.literal_u(u) and sum(u)==sum(b)<=n
        assert ub.columns_to_residue(u)==b
        if not a3.utags(u): continue
        assert len(a3.utags(u))==1
        c=a3.u_to_c(u)
        assert a3.literal_c(c) and a3.cw(c)==sum(u)<=n
        assert a3.ctag(c) is not None and a3.c_to_u(c)==u
        a=inverse(b)
        assert gap(a) and a in aa and forward(a)==b
        assert ctuple(ac.gap_to_cluster(a))==c
        assert sum(a)==sum(b)<=n
        inverse_domain.add(b); inverse_image.add(a)
    assert inverse_domain==image and inverse_image==domain
    assert len(domain)==len(image)==len(rows)
    report={'bound':n,'status':'empirical_partial_composition_pass',
            'all_literal_A':len(aa),'all_literal_B':len(bb),'partial_each':len(domain),
            'literal_A_cohorts':dict(Counter(cohort(a) for a in domain)),
            'literal_B_cohorts':dict(Counter(cohort(b) for b in image)),
            'joint_A_B_cohorts':dict(sorted(joint.items())),
            'all_literal_A_cohorts':dict(Counter(cohort(a) for a in aa)),
            'all_literal_B_cohorts':dict(Counter(cohort(b) for b in bb)),
            'branches':dict(sorted(branches.items())),
            'partial_by_weight':dict(sorted(weights.items(),key=lambda kv:int(kv[0]))),
            'max_actual_input_output_weight':max(map(sum,aa|bb)),
            'max_actual_intermediate_weight':max(row['weight'] for row in rows),
            'literal_distinctness_preserved':all(row['A_cohort']==row['B_cohort'] for row in rows),
            'scope':'exact unchanged reviewed A3, actual RR003 endpoints; no full KR1 claim',
            'checker_sha256':sha(Path(__file__)),
            'pinned_files':freeze['pinned_files']}
    out=Path(f'.runs/rr007/critic-b-composition-{n}.json')
    rawrows=Path(f'.runs/rr007/critic-b-composition-{n}-rows.json')
    if out.exists() or rawrows.exists(): raise FileExistsError('pilot outputs already exist')
    out.write_text(json.dumps(report,indent=2)+'\n')
    rawrows.write_text(json.dumps(rows,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k!='pinned_files'}))
if __name__=='__main__': main()
