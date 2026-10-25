"""Final distinct KR review; independent finite domain/image reconstruction.

Uses the initial critic's own C/U/A/B census algorithms. No high-gap or
high-b source is instantiated; all literal objects stay within the gate.
"""
import argparse
from collections import Counter
import importlib.util
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
BASE=HERE.parent


def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


base=load('kr_critic_independent',HERE/'kr-independentcheck.py')
h=load('h3_final',BASE/'kr-sectors/revision-v3-bridge.py')


def expected_domain(c):
    old=(c.a<=2 or (c.a==3 and c.b==0))
    plane=(c.a in (4,5) and c.b==0 and len(set(c.mu[:-1]))==1)
    tail=(c.a==3 and c.b>=49 or c.a==4 and c.b>=65 or c.a==5 and c.b>=79)
    extra=(c.a==4 and c.b==0 and (c.mu[2]-c.mu[1] in (0,1) or c.mu[2]-c.mu[1]>=18))
    return old or plane or tail or extra


def new_inverse(u):
    """Reconstruct six head languages independently of author inverse code."""
    n,S=Counter(u),set(u)
    y=None
    if S <= {12,8,3,1} and n[12]==1 and n[8]>=1:
        x,t,z,y=2*n[8]-1,n[3],n[1],0
    elif S <= {8,3,1} and n[8]>=2 and n[3]<=2:
        x,t,z,y=2*(n[8]-2),n[3],n[1],0
    elif S <= {12,10,8,3,1} and n[12]==n[10]==1 and n[3]>=1:
        x,t,z,y=2*n[8],n[3]+2,n[1],0
    elif S <= {12,9,8,3,1} and n[12]==n[9]==1 and n[1]>=1:
        x,t,z,y=2*n[8]+1,n[3],n[1]-1,1
    elif S <= {10,8,3,1} and n[10]==1 and n[8]>=1 and n[3]<=2:
        x,t,z,y=2*(n[8]-1),n[3],n[1],1
    elif S <= {12,9,8,6,3,1} and n[12]==n[9]==n[6]==1:
        x,t,z,y=2*n[8],n[3]+3,n[1],1
    if y is None:
        raise base.m.Outside('not an independently admitted low slab')
    return base.m.kr1.ClusterData(4,0,(x,x+t,x+t+y,x+t+y+z),())


def height(v):
    q,r=divmod(v,9)
    return 5*q+(0,1,3,6,8).index(r)


def quotient(u):
    return tuple(base.f(height(v)//3) for v in u if height(v)//3)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('bound',type=int,choices=(12,30,40))
    bound=ap.parse_args().bound
    cs,us=base.c_census(bound),base.u_census(bound)
    all_a,all_b=set(),set()
    for n in range(bound+1):
        for p in base.ordinary(n):
            if base.a_valid(p):
                all_a.add(p)
            if all(v%9 in {1,3,6,8} for v in p):
                all_b.add(p)
    assert len(cs)==len(us)==len(all_a)==len(all_b)
    mapped={}
    cohorts={k:Counter() for k in ('full_A','full_B','H3_A','H3_B')}
    for p in all_a:
        cohorts['full_A'][base.parts_cohort(p)]+=1
    for p in all_b:
        cohorts['full_B'][base.parts_cohort(p)]+=1
    preserved=0
    additions=Counter()
    target_only=0
    a4_all=a4_accepted=0
    for c in cs:
        assert c.weight<=bound and h.domain(c)==expected_domain(c)
        if c.a==4 and c.b==0:
            a4_all+=1
        if not expected_domain(c):
            continue
        u=h.forward(c)
        assert u in us and u not in mapped and sum(u)==c.weight
        assert h.inverse(u)==c
        assert not h.high_gap(c) and not base.ext.tail(c)
        if c.a==4 and c.b==0:
            a4_accepted+=1
        if base.ext.extended_domain(c):
            assert base.ext.forward(c)==u
            preserved+=1
        else:
            assert new_inverse(u)==c
            y=c.mu[2]-c.mu[1]
            additions[y]+=1
            try:
                base.ext.inverse(u)
            except base.m.Outside:
                pass
            else:
                raise AssertionError(('new target intersects H2',c,u))
        a=base.gap.cluster_to_gap(c)
        b=base.stock.columns_to_residue(u)
        assert a in all_a and base.gap.gap_to_cluster(a)==c and sum(a)==c.weight
        assert b in all_b and base.stock.residue_to_columns(b)==u and sum(b)==c.weight
        cohorts['H3_A'][base.parts_cohort(a)]+=1
        cohorts['H3_B'][base.parts_cohort(b)]+=1
        mapped[u]=c
    accepted={}
    qchildren=[]
    minimum_three=None
    for u in us:
        try:
            expect=new_inverse(u)
        except base.m.Outside:
            try:
                expect=base.ext.inverse(u)
            except base.m.Outside:
                expect=None
        try:
            c=h.inverse(u)
        except base.m.Outside:
            assert expect is None
        else:
            assert c==expect and c in cs and h.forward(c)==u and mapped[u]==c
            accepted[u]=c
        n=Counter(u)
        if set(u)<={10,8,3,1} and n[10]==n[8]==1 and n[3]<=1:
            t,z=n[3],n[1]
            child=base.m.g_inverse(u)
            assert child==base.m.kr1.ClusterData(3,0,(t+1,t+4,t+4+z),())
            v=base.m.f1_forward(child)
            assert v==(12,6)+(3,)*t+(1,)*z and sum(v)==sum(u)
            for inv in (base.m.g_inverse,base.m.h1_inverse):
                try:
                    inv(v if inv is base.m.g_inverse else u)
                except base.m.Outside:
                    pass
                else:
                    raise AssertionError('target-only component failed to reject')
            target_only+=1
        q=quotient(u)
        assert q in us
        if q:
            assert height(q[-1])<=2
            hs=tuple(map(height,u))
            if height(q[-1])==2:
                count=sum(v>=3 for v in hs)
                assert hs[count-1]==6 and hs[count]==2
        assert q!=(6,)
        if q==(3,):
            item=(sum(u),u)
            minimum_three=min(minimum_three,item) if minimum_three else item
    assert accepted==mapped
    if bound>=13:
        assert minimum_three==(13,(10,3))
    else:
        assert minimum_three is None
    p9=base.tri.C(3,0,(0,0,0),())
    _,c9=base.tri.step(p9)
    assert c9==base.tri.C(0,1,(),(0,))
    cc9=base.m.kr1.ClusterData(c9.a,c9.b,c9.mu,c9.nu)
    assert base.m.g2.reconstruct_columns(cc9)==base.m.h1_forward(cc9)==(3,)
    assert not any(sum(u)==9 and quotient(u)==(3,) for u in us)
    if bound>=18:
        p18=base.tri.C(0,2,(),(1,1))
        _,c18=base.tri.step(p18)
        assert c18==base.tri.C(2,0,(1,1),())
        cc18=base.m.kr1.ClusterData(c18.a,c18.b,c18.mu,c18.nu)
        assert base.m.g2.reconstruct_columns(cc18)==base.m.h1_forward(cc18)==(6,)
    missing=sorted((c for c in cs if not expected_domain(c)),key=lambda c:(c.weight,c.a,c.b,c.mu,c.nu))
    rejected=sorted(us-mapped.keys(),key=lambda u:(sum(u),u))
    if bound>=20:
        assert missing[0]==base.m.kr1.ClusterData(4,0,(0,0,2,2),())
        assert rejected[0]==(10,9,1)
    else:
        assert not missing and not rejected
    out={'bound':bound,'all_C_U_A_B':len(cs),'H3_mapped':len(mapped),'H3_rejected':len(rejected),
         'H2_assignments_preserved':preserved,'new_y_classes':dict(additions),
         'a4_b0':{'all':a4_all,'accepted':a4_accepted},
         'cohorts':{k:dict(v) for k,v in cohorts.items()},
         'target_only_q0_t0_1_cases':target_only,
         'child3_minimum_parent':minimum_three,
         'corrected_child_terminal_bound':2,'child6_range_exclusion_verified':True,
         'first_missing_C':str(missing[0]) if missing else None,
         'first_rejected_U':rejected[0] if rejected else None,
         'high_gap_and_high_b_sources_constructed':0,
         'status':'independent finite reconstruction; universal proofs separately reviewed'}
    dest=HERE/f'kr-final-result-{bound}.json'
    if dest.exists():
        raise FileExistsError(dest)
    dest.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out))


if __name__=='__main__':
    main()
