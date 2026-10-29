"""Focused regression for composition, including the critic's weight-56 witness."""
import argparse
from dataclasses import asdict
import hashlib
import importlib.util
import json
from pathlib import Path
import signal
import sys
import time

import candidates
from composed import Extension


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--h3-root', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    started = time.perf_counter()
    signal.alarm(30)
    location = args.h3_root / 'research/phase2-20261025/kr-sectors'
    sys.path.insert(0, str(location))
    spec = importlib.util.spec_from_file_location('composed_h3', location/'revision-v3-bridge.py')
    h3 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(h3)
    ext = Extension(h3)

    # The alternate y2 target must not be recognized by the composed inverse.
    witness = candidates.kr1.ClusterData(4, 0, (9,9,11,11), ())
    alternate = candidates.middle_forward(witness)
    assert ext.forward(witness) == candidates.y2_forward(witness)
    try:
        ext.inverse(alternate)
    except h3.m.Outside:
        pass
    else:
        raise AssertionError('critic witness still admitted')

    images, old = {}, 0
    for n in range(41):
        for source in candidates.kr1.cluster_data(n):
            if not ext.domain(source):
                continue
            u = ext.forward(source)
            assert ext.inverse(u) == source and u not in images
            assert sum(u) == source.weight
            images[u] = source
            if h3.domain(source):
                assert u == h3.forward(source)
                old += 1
    recognized = set()
    for n in range(41):
        for wp in candidates.kr1.weighted_partitions(n):
            u = candidates.kr1.weighted_columns(wp)
            try:
                source = ext.inverse(u)
            except h3.m.Outside:
                continue
            assert ext.domain(source) and ext.forward(source) == u
            assert images[u] == source
            recognized.add(u)
    assert recognized == set(images)

    funded = 0
    for y in range(3,18):
        k = (2*y+6)//3
        for q in (k,k+1,k+20):
            for r in range(3):
                for t,z in ((0,0),(2,5),(100,100)):
                    x = 3*q+r
                    source = candidates.kr1.ClusterData(4,0,(x,x+t,x+t+y,x+t+y+z),())
                    u = ext.forward(source)
                    assert ext.inverse(u) == source and sum(u) == source.weight
                    funded += 1
    signal.alarm(0)
    result = {
        'status':'restricted_composition_passes_full_KR1_unresolved',
        'elapsed_seconds':time.perf_counter()-started,
        'critic_weight56_alternate_rejected':True,
        'critic_witness_C':asdict(witness),
        'through_weight40':{'H3_preserved':old,'combined':len(images),
                            'exactly_recognized_targets':len(recognized)},
        'funded_composition_cases':funded,
        'composed_sha256':hashlib.sha256(Path(__file__).with_name('composed.py').read_bytes()).hexdigest(),
        'discovery_not_held_out':True,
    }
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
