"""Exact audit of Argon's proposed cone reroutings. No core maps are changed.

Run without -O. Passing means the proposed repairs have been REFUTED by the
preserved collisions, and the stated finite capacity obstruction was reproduced.
"""
from __future__ import annotations

from dataclasses import asdict
import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'research/rogers-ramanujan/checks'))
import kr1
import rr004_multidim_cones as current


def run_audit():
    C = kr1.ClusterData
    cases = [
        ('weight31_option_B', C(5,0,(0,1,1,2,2),()),
         (10,9,9,3), C(4,0,(0,0,5,10),())),
        ('weight31_alternative', C(5,0,(0,1,1,2,2),()),
         (9,8,8,6), C(3,1,(0,2,2),(2,))),
        ('weight25_free_head', C(5,0,(0,0,0,0,0),()),
         (9,8,8), C(4,0,(0,3,3,3),())),
        ('weight37_pure_head', C(5,0,(0,1,1,5,5),()),
         (10,10,9,8), C(4,0,(2,5,7,7),())),
        ('weight41_step_one_patch', C(5,0,(0,1,2,6,7),()),
         (10,10,9,9,3), C(3,1,(1,2,2),(5,))),
    ]
    collisions = []
    for label, proposed_source, target, existing_source in cases:
        assert proposed_source != existing_source
        assert current.reconstruct_full(existing_source) == target
        assert proposed_source.weight == existing_source.weight == sum(target)
        kr1.decode_columns(target)
        collisions.append({
            'proposal': label,
            'proposed_source': asdict(proposed_source),
            'candidate_target': target,
            'existing_source': asdict(existing_source),
            'weight': sum(target),
            'status': 'refuted_if_other_assignments_are_retained',
        })
    # The PDF misidentifies the literal apex image as (19,12).
    actual_apex = C(5,0,(0,1,1,2,2),())
    assert current.reconstruct_full(actual_apex) == (18,10,3)
    # Exact, generous head capacity: even unused/reserved heads all count.
    W = 55
    head_labels = [(z,y,x) for z in range(4) for y in (1,2)
                   for x in range(W//8+1)
                   if x+z >= 1 and 10*z+9*y+8*x+int(x==0) <= W]
    source_apexes = [C(3,2,(0,r,r),(u,v)) for r in range(3)
                    for u in range(W//3+1) for v in range(u,W//3+1)
                    if 39+2*r+3*(u+v) <= W]
    assert len(source_apexes) == 30 and len(head_labels) == 29
    assert len(set(source_apexes)) == 30
    assert all(c.weight <= W for c in source_apexes)
    # Independent arithmetic check of the parent's fixed-alphabet theorem witness.
    k = 128
    M = (9*k*k+21*k+18)//2
    assert M == 75081 and 2**k > (M+1)**6
    return {
        'status': 'proposed_preservation_repairs_refuted',
        'assurance': 'explicit exact witnesses; finite counts support written proofs',
        'collisions': collisions,
        'actual_apex_image': {'cluster': asdict(actual_apex), 'image': (18,10,3)},
        'unique_head_capacity': {
            'maximum_weight': W, 'source_apex_count': len(source_apexes),
            'eligible_head_count': len(head_labels),
            'head_bounds': '0<=z<=3, y in {1,2}, x>=0, x+z>=1; min tail 1 if x=0',
            'source_family': 'a=3,b=2,mu=(0,r,r),r in {0,1,2},nu=(u,v),0<=u<=v',
            'scope': 'weight-preserving injective HEAD assignment with full unbounded increment octants',
        },
        'fixed_alphabet_witness': {'binary_increment_length': k, 'max_weight': M,
                                   'source_count': 2**k, 'generous_target_bound': (M+1)**6},
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    if not __debug__:
        raise SystemExit('Audit requires assertions; omit -O')
    report = json.dumps(run_audit(), indent=2) + '\n'
    if args.output:
        args.output.write_text(report)
    else:
        print(report, end='')
