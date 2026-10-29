"""Bounded diagnostics for frozen restricted maps; no discovery lookup map."""
import argparse
from collections import Counter
from dataclasses import asdict
import hashlib
import importlib.util
import json
from pathlib import Path
import signal
import sys
import time

import candidates as c


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--h3-root', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    started = time.perf_counter()
    signal.alarm(60)
    sys.path.insert(0, str(args.h3_root/'research/phase2-20261025/kr-sectors'))
    h3 = load('frozen_h3', args.h3_root/'research/phase2-20261025/kr-sectors/revision-v3-bridge.py')
    t = load('tableau_oracle', c.ROOT/'research/partitions/checks/tableaux.py')
    import rr003_cluster_merge as gap
    import rr003_stockhofe as product

    ordinary = []
    for n in range(5,9):
        h = tuple(range(1,n+1))
        source_shape = (2,2)+(1,)*(n-4)
        sources = list(t.tableaux(h,source_shape))
        images = {}
        fibers = Counter()
        for source in sources:
            u = c.ordinary_forward(source)
            assert t.validates(h,u) and c.ordinary_inverse(u) == source
            assert u not in images
            images[u] = source
            fibers[t.bubble_demote(h,source,1)] += 1
        accepted = set()
        positives = 0
        for sh in ((2,)+(1,)*(n-2),(3,2)+(1,)*(n-5)):
            for u in t.tableaux(h,sh):
                positives += 1
                try:
                    source = c.ordinary_inverse(u)
                except ValueError:
                    continue
                assert t.validates(h,source,source_shape)
                assert c.ordinary_forward(source) == u and images[u] == source
                accepted.add(u)
        assert accepted == set(images)
        ordinary.append({'n':n,'sources':len(sources),'positive_targets':positives,
                         'recognized_images':len(accepted),'max_bubble_fiber':max(fibers.values())})

    # This is a deliberate attempted variation, not a claim of P-generalization.
    naive_p_failure = None
    for h in t.hessenberg_vectors(5):
        seen = {}
        for source in t.tableaux(h,(2,2,1)):
            u = c.ordinary_forward(source)
            reason = None
            if not t.validates(h,u):
                reason = 'invalid_target'
            elif t.inv_g(h,u) != t.inv_g(h,source):
                reason = 'inversion_change'
            elif u in seen:
                reason = 'collision'
            if reason:
                naive_p_failure={'h':h,'source':source,'output':u,'reason':reason,
                                 'earlier_source':seen.get(u),
                                 'source_inv':t.inv_g(h,source),'output_inv':t.inv_g(h,u)}
                break
            seen[u] = source
        if naive_p_failure:
            break
    assert naive_p_failure is not None

    # Entire rectangular parameter grid, including every carry boundary.
    new_images = {}
    for x in range(18):
        for td in range(10):
            for z in range(11):
                source = c.kr1.ClusterData(4,0,(x,x+td,x+td+2,x+td+2+z),())
                u = c.y2_forward(source)
                c.kr1.decode_columns(u)
                assert sum(u) == source.weight and c.y2_inverse(u) == source
                assert u not in new_images
                new_images[u] = source
                try:
                    h3.inverse(u)
                except h3.m.Outside:
                    pass
                else:
                    raise AssertionError(('collision_with_H3',source,u))

    # Stress large values, without enumeration of targets at those weights.
    stress = 0
    for x,td,z in ((1001,1000,999),(1002,1000,999),(0,1000,999),(0,3,10000),(0,2,4),(0,2,5)):
        source = c.kr1.ClusterData(4,0,(x,x+td,x+td+2,x+td+2+z),())
        u = c.y2_forward(source)
        c.kr1.decode_columns(u)
        assert c.y2_inverse(u) == source and sum(u) == source.weight
        stress += 1

    funded = 0
    funded_max_weight = 0
    for y in range(3,18):
        k = (2*y+6)//3
        for q in range(k,k+6):
            for r in range(3):
                for td in (0,1,2,3,10):
                    for z in (0,1,4,13):
                        x = 3*q+r
                        source = c.kr1.ClusterData(4,0,(x,x+td,x+td+y,x+td+y+z),())
                        u = c.middle_forward(source)
                        c.kr1.decode_columns(u)
                        assert c.middle_inverse(u) == source and sum(u) == source.weight
                        try:
                            c.y2_inverse(u)
                        except ValueError:
                            pass
                        else:
                            raise AssertionError(('funded_y2_overlap',source,u))
                        try:
                            h3.inverse(u)
                        except h3.m.Outside:
                            pass
                        else:
                            raise AssertionError(('funded_H3_overlap',source,u))
                        funded += 1
                        funded_max_weight = max(funded_max_weight,source.weight)

    mapped, old_count, added_count = {}, 0, 0
    all_sources = [source for n in range(41) for source in c.kr1.cluster_data(n)]
    first_missing = None
    for source in all_sources:
        if source.a == 4 and source.b == 0 and source.mu[2]-source.mu[1] == 2:
            u = c.y2_forward(source)
            added_count += 1
        elif h3.domain(source):
            u = h3.forward(source)
            old_count += 1
        else:
            if first_missing is None:
                first_missing = source
            continue
        assert u not in mapped and sum(u) == source.weight
        mapped[u] = source
        try:
            back = c.y2_inverse(u)
        except ValueError:
            back = h3.inverse(u)
        assert back == source
        a,b = gap.cluster_to_gap(source),product.columns_to_residue(u)
        assert c.kr1.is_gap(a) and c.kr1.is_residue(b)
        assert gap.gap_to_cluster(a) == source and product.residue_to_columns(b) == u
        assert sum(a) == sum(b) == source.weight

    all_us = {c.kr1.weighted_columns(w) for n in range(41) for w in c.kr1.weighted_partitions(n)}
    assert len(all_us) == len(all_sources)
    recognized_new = set()
    for u in all_us:
        try:
            source = c.y2_inverse(u)
        except ValueError:
            continue
        assert c.y2_forward(source) == u and mapped[u] == source
        recognized_new.add(u)
    assert len(recognized_new) == added_count
    elapsed = time.perf_counter()-started
    signal.alarm(0)
    result={'status':'restricted_checks_pass_full_KR1_unresolved',
            'elapsed_seconds':elapsed,'ordinary_tableaux':ordinary,
            'naive_P_generalization_refuted':naive_p_failure,
            'y2_grid':{'x_range':[0,17],'t_range':[0,9],'z_range':[0,10],
                       'checked':len(new_images),'distinct_images':len(new_images)},
            'large_parameter_stress_cases':stress,
            'funded_y3_to_17':{'checked':funded,'max_tested_weight':funded_max_weight},
            'through_weight_40':{'all_C_U':len(all_sources),'H3_preserved':old_count,
                                'new_y2':added_count,'combined':len(mapped),
                                'new_inverse_exact_images':len(recognized_new),
                                'first_missing_C':asdict(first_missing)},
            'candidate_sha256':hashlib.sha256(Path(c.__file__).read_bytes()).hexdigest(),
            'test_script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'discovery_not_held_out':True}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
