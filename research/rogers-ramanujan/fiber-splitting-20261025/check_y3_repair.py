"""Bounded checks for frozen V3; preserves the rejected V2 collision."""
import argparse
from dataclasses import asdict
import hashlib
import importlib.util
import json
from pathlib import Path
import signal
import sys
import time

import candidates as c
import y3_extension as v2
import y3_repaired as v3


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--h3-root', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    started = time.perf_counter()
    signal.alarm(30)
    loc = args.h3_root/'research/phase2-20261025/kr-sectors'
    sys.path.insert(0,str(loc))
    spec = importlib.util.spec_from_file_location('v3_h3',loc/'revision-v3-bridge.py')
    h3 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(h3)
    ext = v3.ExtensionV3(h3)
    import rr003_cluster_merge as gap
    import rr003_stockhofe as product

    old = c.kr1.ClusterData(3,0,(2,5,6),())
    new = c.kr1.ClusterData(4,0,(0,0,3,3),())
    collision = (12,6,3,1)
    assert h3.forward(old) == v2.y3_forward(new) == collision
    assert v2.ExtensionV2(h3).inverse(collision) == new != old
    assert ext.forward(old) == collision and ext.inverse(collision) == old
    assert ext.forward(new) == (8,8,6) and ext.inverse((8,8,6)) == new

    grid = {}
    for x in range(18):
        for t in range(10):
            for z in range(11):
                source = c.kr1.ClusterData(4,0,(x,x+t,x+t+3,x+t+3+z),())
                u = ext.forward(source)
                c.kr1.decode_columns(u)
                assert sum(u) == source.weight and ext.inverse(u) == source
                assert u not in grid
                grid[u] = source
                for inverse in (h3.inverse,c.y2_inverse):
                    try:
                        inverse(u)
                    except ValueError:
                        pass
                    else:
                        raise AssertionError(('old_or_y2_collision',source,u))

    stress = 0
    for x,t,z in ((1001,1000,999),(1002,1000,999),(0,1000,999),
                  (0,0,10000),(0,1,10000),(0,2,10000),(1,1000,999)):
        source = c.kr1.ClusterData(4,0,(x,x+t,x+t+3,x+t+3+z),())
        u = ext.forward(source)
        assert ext.inverse(u) == source and sum(u) == source.weight
        stress += 1

    images = {}
    counts = {'H3_preserved':0,'new_y2':0,'new_y3':0}
    all_count = 0
    first_missing = None
    for n in range(41):
        for source in c.kr1.cluster_data(n):
            all_count += 1
            if not ext.domain(source):
                if first_missing is None:
                    first_missing = {'weight':n,'C':asdict(source)}
                continue
            u = ext.forward(source)
            assert ext.inverse(u) == source and u not in images
            images[u] = source
            if h3.domain(source):
                assert h3.forward(source) == u
                counts['H3_preserved'] += 1
            elif v3.y2_domain(source):
                counts['new_y2'] += 1
            else:
                counts['new_y3'] += 1
            a,b = gap.cluster_to_gap(source), product.columns_to_residue(u)
            assert c.kr1.is_gap(a) and c.kr1.is_residue(b)
            assert gap.gap_to_cluster(a) == source and product.residue_to_columns(b) == u
            assert sum(a) == sum(b) == source.weight
    recognized = set()
    for n in range(41):
        for wp in c.kr1.weighted_partitions(n):
            u = c.kr1.weighted_columns(wp)
            try:
                source = ext.inverse(u)
            except ValueError:
                continue
            assert ext.domain(source) and ext.forward(source) == u and images[u] == source
            recognized.add(u)
    assert recognized == set(images)

    for y,x in ((2,9),(3,12)):
        source = c.kr1.ClusterData(4,0,(x,x,x+y,x+y),())
        alternate = c.middle_forward(source)
        try:
            ext.inverse(alternate)
        except ValueError:
            pass
        else:
            raise AssertionError(('alternate_funded_image_accepted',source,alternate))
    funded = 0
    for y in range(4,18):
        k = (2*y+6)//3
        for q in (k,k+1,k+20):
            for r in range(3):
                for t,z in ((0,0),(2,5),(100,100)):
                    x = 3*q+r
                    source = c.kr1.ClusterData(4,0,(x,x+t,x+t+y,x+t+y+z),())
                    u = ext.forward(source)
                    assert ext.inverse(u) == source and sum(u) == source.weight
                    funded += 1
    signal.alarm(0)
    result = {
        'status':'V3_restricted_checks_pass_full_KR1_unresolved',
        'elapsed_seconds':time.perf_counter()-started,
        'rejected_V2_witness':{'old':asdict(old),'new':asdict(new),'output':collision,'weight':22},
        'V3_retains_old_witness_and_repairs_new':True,
        'y3_grid':{'x':[0,17],'t':[0,9],'z':[0,10],'checked':len(grid),'distinct':len(grid)},
        'large_parameter_stress_cases':stress,
        'through_weight40':dict(counts,all_C_U=all_count,combined=len(images),
                               exactly_recognized_targets=len(recognized),first_missing=first_missing),
        'alternate_funded_y2_y3_targets_rejected':True,
        'funded_y4_to17_composition_cases':funded,
        'V3_sha256':hashlib.sha256(Path(v3.__file__).read_bytes()).hexdigest(),
        'discovery_not_held_out':True,
    }
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
