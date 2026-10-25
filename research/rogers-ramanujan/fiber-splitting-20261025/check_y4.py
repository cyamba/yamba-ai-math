"""Bounded test of the frozen Y4 candidate and exact composed image."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import signal
import sys
import time
import candidates as c
import y3_repaired as v3
import y4_extension as v4


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--h3-root',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    args = ap.parse_args()
    started = time.perf_counter()
    signal.alarm(30)
    loc=args.h3_root/'research/phase2-20261025/kr-sectors'
    sys.path.insert(0,str(loc))
    spec=importlib.util.spec_from_file_location('y4_h3',loc/'revision-v3-bridge.py')
    h3=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(h3)
    ext=v4.ExtensionV4(h3)
    import rr003_cluster_merge as gap
    import rr003_stockhofe as product

    grid={}
    for x in range(18):
        for t in range(10):
            for z in range(11):
                source=c.kr1.ClusterData(4,0,(x,x+t,x+t+4,x+t+4+z),())
                u=ext.forward(source)
                c.kr1.decode_columns(u)
                assert ext.inverse(u)==source and sum(u)==source.weight and u not in grid
                grid[u]=source
                for inverse in (h3.inverse,c.y2_inverse,v3.y3_inverse):
                    try:
                        inverse(u)
                    except ValueError:
                        pass
                    else:
                        raise AssertionError(('retained_image_collision',source,u))
    stress=0
    for x,t,z in ((1001,1000,999),(1002,1000,999),(0,1000,999),
                  (0,0,10000),(0,1,10000),(0,2,10000),(1,1000,999)):
        source=c.kr1.ClusterData(4,0,(x,x+t,x+t+4,x+t+4+z),())
        u=ext.forward(source)
        assert ext.inverse(u)==source and sum(u)==source.weight
        stress+=1
    images={}
    old_count=new_count=0
    old_ext=v3.ExtensionV3(h3)
    for n in range(41):
        for source in c.kr1.cluster_data(n):
            if not ext.domain(source):
                continue
            u=ext.forward(source)
            assert ext.inverse(u)==source and u not in images
            images[u]=source
            if old_ext.domain(source):
                assert old_ext.forward(source)==u
                old_count+=1
            else:
                new_count+=1
                a,b=gap.cluster_to_gap(source),product.columns_to_residue(u)
                assert c.kr1.is_gap(a) and c.kr1.is_residue(b)
                assert gap.gap_to_cluster(a)==source and product.residue_to_columns(b)==u
                assert sum(a)==sum(b)==source.weight
    accepted=set()
    for n in range(41):
        for wp in c.kr1.weighted_partitions(n):
            u=c.kr1.weighted_columns(wp)
            try:
                source=ext.inverse(u)
            except ValueError:
                continue
            assert ext.domain(source) and ext.forward(source)==u and images[u]==source
            accepted.add(u)
    assert accepted==set(images)
    for y,x in ((2,9),(3,12),(4,12)):
        source=c.kr1.ClusterData(4,0,(x,x,x+y,x+y),())
        try:
            ext.inverse(c.middle_forward(source))
        except ValueError:
            pass
        else:
            raise AssertionError('alternate funded image admitted')
    funded=0
    for y in range(5,18):
        k=(2*y+6)//3
        for q in (k,k+1,k+20):
            for r in range(3):
                for t,z in ((0,0),(2,5),(100,100)):
                    x=3*q+r
                    source=c.kr1.ClusterData(4,0,(x,x+t,x+t+y,x+t+y+z),())
                    u=ext.forward(source)
                    assert ext.inverse(u)==source and sum(u)==source.weight
                    funded+=1
    signal.alarm(0)
    result={'status':'V4_restricted_checks_pass_full_KR1_unresolved',
            'elapsed_seconds':time.perf_counter()-started,
            'y4_grid':{'x':[0,17],'t':[0,9],'z':[0,10],'checked':len(grid),'distinct':len(grid)},
            'stress_cases':stress,
            'through_weight40':{'V3_preserved':old_count,'new_y4':new_count,'combined':len(images),
                                'exactly_recognized_targets':len(accepted),'all_C_U':5461},
            'funded_y5_to17_cases':funded,'alternate_funded_y2_y3_y4_targets_rejected':True,
            'candidate_sha256':hashlib.sha256(Path(v4.__file__).read_bytes()).hexdigest(),
            'discovery_not_held_out':True}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
