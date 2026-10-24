"""Distinct critic reconstruction; no constructed KR object exceeds the gate.

C is generated using independent weighted gap compositions. A/B are filtered
from ordinary partitions. U is generated directly using decoded flat paths.
Maps under review are exercised, but never used to define these four censuses.
The arbitrary-large-b tail is deliberately not instantiated.
"""
import argparse
from collections import Counter
import hashlib
import importlib.util
import json
from math import isqrt
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(BASE / 'kr-sectors'))
import bridge as m
import extension as ext
import reductions as red
import rr003_cluster_merge as gap
import rr003_stockhofe as stock
sys.path.insert(0, str(BASE / 'recursive-lift'))
import triadic as tri


def ordinary(n, low=1):
    if not n:
        yield ()
    for v in range(low, n + 1):
        for tail in ordinary(n - v, v):
            yield (v,) + tail


def a_valid(p):
    return (all(p[i + 2] - p[i] >= 3 for i in range(len(p) - 2))
            and all(y - x > 1 or (x + y) % 3 == 0 for x, y in zip(p, p[1:])))


def compositions(costs, budget):
    if not costs:
        yield ()
        return
    c, *rest = costs
    for count in range(budget // c + 1):
        for tail in compositions(rest, budget - count * c):
            yield (count,) + tail


def arm(ds):
    out, total = [], 0
    for d in reversed(ds):
        total += d
        out.append(total)
    return tuple(out)


def c_census(bound):
    result = set()
    for a in range(isqrt(bound) + 1):
        for b in range(isqrt(bound // 3) + 1):
            base = a*a + 3*a*b + 3*b*b
            if base > bound:
                continue
            costs = tuple(range(1, a+1)) + tuple(range(3, 3*b+1, 3))
            for ds in compositions(costs, bound-base):
                result.add(m.kr1.ClusterData(a, b, arm(ds[:a]), arm(ds[a:])))
    return result


def f(h):
    return 9 * (h // 5) + (0, 1, 3, 6, 8)[h % 5]


def u_census(bound):
    result = {()}
    def visit(hs, remaining):
        h = hs[-1]
        if h <= 4:
            result.add(tuple(map(f, hs)))
        for nxt in range(max(1, h-4), h+1):
            if f(nxt) <= remaining:
                visit(hs+(nxt,), remaining-f(nxt))
    h = 1
    while f(h) <= bound:
        visit((h,), bound-f(h))
        h += 1
    return result


def parts_cohort(p):
    return 'distinct' if len(p) == len(set(p)) else 'repeated'


def reverse_reduction_language(cs, bound):
    admitted = set()
    counts = Counter()
    for child in cs:
        if child.a not in (1, 2, 3) or not child.b:
            continue
        a, remaining = child.a+2, bound-child.weight
        if a == 5 and child.mu[0] % 4:
            continue
        for k in range(child.b):
            phases = range(3) if a == 5 else (0,)
            for phase in phases:
                fixed = a-1 + 3*k + (4*phase if a == 5 else 0)
                unit = {3:2, 4:4, 5:5}[a]
                for d in range(max(0, (remaining-fixed)//unit+1)):
                    boundary = (d, phase, k) if a == 5 else (d,k)
                    parent = red.inverse(child, boundary)
                    assert parent.weight <= bound and parent in cs
                    actual_child, actual_boundary, excess = red.forward(parent)
                    assert (actual_child, actual_boundary) == (child, boundary)
                    assert excess == fixed+unit*d
                    assert parent.weight == child.weight+excess
                    assert parent not in admitted
                    admitted.add(parent)
                    counts[a] += 1
    wanted = {c for c in cs if c.a in (3,4,5)}
    assert admitted == wanted
    return dict(counts)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('bound', type=int, choices=(12,30,40))
    bound = ap.parse_args().bound
    cs, us = c_census(bound), u_census(bound)
    all_a, all_b = set(), set()
    for n in range(bound+1):
        for p in ordinary(n):
            if a_valid(p):
                all_a.add(p)
            if all(v % 9 in {1,3,6,8} for v in p):
                all_b.add(p)
    assert len(cs) == len(us) == len(all_a) == len(all_b)
    assert {gap.gap_to_cluster(p) for p in all_a} == cs
    assert {stock.residue_to_columns(p) for p in all_b} == us
    for p in all_a:
        assert gap.cluster_to_gap(gap.gap_to_cluster(p)) == p
    for p in all_b:
        assert stock.columns_to_residue(stock.residue_to_columns(p)) == p
    old, new, aux, retained = {}, {}, {}, {}
    cohorts = {name:Counter() for name in ('full_A','full_B','H1_A','H1_B','H2_A','H2_B')}
    for p in all_a:
        cohorts['full_A'][parts_cohort(p)] += 1
    for p in all_b:
        cohorts['full_B'][parts_cohort(p)] += 1
    max_h1_steps = 0
    max_depth = 0
    tree_images = set()
    for c in cs:
        assert c.weight <= bound
        tc = tri.C(c.a,c.b,c.mu,c.nu)
        tree = tri.encode(tc)
        assert tri.decode(tree) == tc and tri.tree_weight(tree) == c.weight
        assert tree not in tree_images
        tree_images.add(tree)
        max_depth = max(max_depth, tri.depth(tree))
        if c.a:
            ds = tuple(reversed(tuple(x-y for x,y in zip(c.mu,(0,)+c.mu[:-1]))))
            assert sum((i+1)*x for i,x in enumerate(ds)) == sum(c.mu)
        if m.domain(c):
            u, length = m.h1_forward(c,steps=True)
            assert u in us and sum(u) == c.weight and u not in old
            assert m.h1_inverse(u) == c
            old[u] = c
            max_h1_steps = max(max_h1_steps,length)
            for key,p in (('H1_A',gap.cluster_to_gap(c)),('H1_B',stock.columns_to_residue(u))):
                cohorts[key][parts_cohort(p)] += 1
            if m.retained_domain(c):
                fu = m.f1_forward(c)
                assert fu == u and fu not in retained
                retained[fu] = c
        if ext.extended_domain(c):
            u = ext.forward(c)
            assert u in us and u not in new and sum(u) == c.weight
            assert ext.inverse(u) == c
            if c in old.values():
                assert old[u] == c
            if not m.domain(c):
                assert ext.plane(c) and not ext.tail(c)
                assert u not in old and ext.plane_inverse(u) == c
            new[u] = c
            au = ext.auxiliary_forward(c)
            assert au in us and au not in aux and ext.auxiliary_inverse(au) == c
            aux[au] = c
            for key,p in (('H2_A',gap.cluster_to_gap(c)),('H2_B',stock.columns_to_residue(u))):
                cohorts[key][parts_cohort(p)] += 1
    reverse_old, reverse_new = {}, {}
    for u in us:
        for name, inv, fwd, census in (('H1',m.h1_inverse,m.h1_forward,reverse_old),
                                        ('H2',ext.inverse,ext.forward,reverse_new)):
            try:
                c = inv(u)
            except m.Outside:
                continue
            assert c in cs and fwd(c) == u and c.weight == sum(u)
            census[u] = c
    assert old == reverse_old and new == reverse_new
    assert old.items() <= new.items()
    grammar = set(t for n in range(bound+1) for t in tri.grammar_exact(n))
    assert grammar == tree_images
    reductions = reverse_reduction_language(cs,bound)
    missing = sorted((c for c in cs if not ext.extended_domain(c)),key=lambda c:(c.weight,c.a,c.b,c.mu,c.nu))
    rejected = sorted(us-new.keys(),key=lambda u:(sum(u),u))
    expected_missing = m.kr1.ClusterData(4,0,(0,0,1,1),()) if bound >= 18 else None
    assert (missing[0] if missing else None) == expected_missing
    assert (rejected[0] if rejected else None) == ((10,8) if bound >= 18 else None)
    # Literal invalidity rejection is checked at the API boundary, no invalid
    # object here has ordinary weight greater than the active gate.
    invalid_u = ((0,), (2,), (1,3), (9,))
    for u in invalid_u:
        if sum(u) <= bound:
            for inv in (m.h1_inverse,ext.inverse):
                try:
                    inv(u)
                except ValueError:
                    pass
                else:
                    raise AssertionError(('invalid U accepted',u,inv.__name__))
    out={'bound':bound,'independent_censuses':{k:len(v) for k,v in [('C',cs),('U',us),('A',all_a),('B',all_b)]},
         'H1':len(old),'H2':len(new),'H2_rejected':len(us)-len(new),
         'cohorts':{k:dict(v) for k,v in cohorts.items()},
         'independent_reverse_reduction_language':reductions,
         'independent_grammar_trees':len(grammar),'max_depth':max_depth,'max_H1_forward_steps':max_h1_steps,
         'first_missing_C':str(missing[0]) if missing else None,
         'first_rejected_U':rejected[0] if rejected else None,
         'above40_tail_objects_constructed':0,'status':'finite reconstruction pass; universal tail assessed symbolically'}
    dest=HERE / f'kr-independent-result-{bound}.json'
    if dest.exists():
        raise FileExistsError(dest)
    dest.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out))


if __name__ == '__main__':
    main()
