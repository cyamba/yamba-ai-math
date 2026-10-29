"""Finite implementation checks for frozen RR003 round-two restricted results.

Exit zero means these restricted checks pass; --require-bijection exits two.
This executable cannot certify a universal theorem or novelty.
"""
import argparse
from collections import Counter
from dataclasses import asdict
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import time
import kr1
import rr003_revision as maps
import rr003_recursive as recursive

ROOT = Path(__file__).resolve().parents[3]
PHASE = ROOT/'research/rogers-ramanujan/rr003'


def require(condition, message='RR003 round-two finite check failed'):
    if not condition:
        raise AssertionError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify(ceiling):
    if type(ceiling) is not int or not 0 <= ceiling <= 30:
        raise ValueError('ceiling must be an integer between zero and thirty')
    freeze = json.loads((PHASE/'round-2-freeze.json').read_text())
    sources = dict(freeze['frozen_sha256'])
    for name, digest in sources.items():
        require(sha(ROOT/name) == digest, ('frozen source changed', name))
    sources[str(Path(__file__).relative_to(ROOT))] = sha(Path(__file__))
    sources[str((PHASE/'round-2-freeze.json').relative_to(ROOT))] = sha(PHASE/'round-2-freeze.json')
    totals, rows = Counter(), []
    missing_u = unsupported_c = None
    for n in range(ceiling+1):
        actual_u = {kr1.weighted_columns(w) for w in kr1.weighted_partitions(n)}
        images = set()
        for c in kr1.cluster_data(n):
            if not maps.supported(c):
                if unsupported_c is None:
                    unsupported_c = {'weight':n, 'cluster':asdict(c)}
                continue
            u = maps.reconstruct_columns(c)
            require(u in actual_u and sum(u) == c.weight == n, ('invalid/weight',c,u))
            require(u not in images, ('collision',c,u))
            images.add(u)
            require(maps.decompose_columns(u) == c, ('C round trip',c,u))
            totals['cluster_round_trips'] += 1
            if c.mu:
                raised_c = kr1.ClusterData(c.a,c.b,c.mu[:-1]+(c.mu[-1]+1,),c.nu)
                require(maps.reconstruct_columns(raised_c) == tuple(sorted(u+(1,),reverse=True)),
                        ('last mu operation',c))
                totals['unit_operations'] += 1
            for j in range(1,c.b+1):
                raised_c = kr1.ClusterData(c.a,c.b,c.mu,
                    tuple(v+int(i>=c.b-j) for i,v in enumerate(c.nu)))
                require(maps.reconstruct_columns(raised_c) == tuple(sorted(u+(3*j,),reverse=True)),
                        ('nu suffix operation',c,j))
                totals['nu_operations'] += 1
            if c.a == 2:
                raised_c = kr1.ClusterData(2,c.b,tuple(v+1 for v in c.mu),c.nu)
                if maps.supported(raised_c):
                    operation = maps.raise_common_mixed_columns if c.b else maps.raise_common_columns
                    reverse = maps.lower_common_mixed_columns if c.b else maps.lower_common_columns
                    raised_u = operation(u)
                    require(raised_u == maps.reconstruct_columns(raised_c), ('common carry',c))
                    require(sum(raised_u) == n+2 and reverse(raised_u) == u, ('common inverse',c))
                    totals['mixed_common_operations' if c.b else 'zero_pair_common_operations'] += 1
                else:
                    try:
                        maps.raise_common_mixed_columns(u)
                    except maps.OutsideRestrictedDomain:
                        totals['unresolved_carry_rejections'] += 1
                    else:
                        raise AssertionError(('unsupported carry silently accepted',c))
        recognized = set()
        for u in actual_u:
            try:
                c = maps.decompose_columns(u)
            except maps.OutsideRestrictedDomain:
                if missing_u is None or n < missing_u['weight'] or (n == missing_u['weight'] and u < tuple(missing_u['columns'])):
                    missing_u = {'weight':n,'columns':u}
                continue
            require(maps.supported(c) and c.weight == n, ('inverse domain/weight',u,c))
            require(maps.reconstruct_columns(c) == u, ('U round trip',u,c))
            recognized.add(u)
            totals['column_round_trips'] += 1
        require(recognized == images, ('restricted missing image',n))
        a, b = set(kr1.gap_partitions(n)), set(kr1.residue_partitions(n))
        for p in a:
            state, rest = recursive.gap_strip(p)
            require(recursive.gap_unstrip(state,rest) == p, ('gap grammar inverse',p))
            require(sum(p) == sum(recursive.TAILS[state])+sum(rest)+3*len(rest))
            totals['gap_grammar_round_trips'] += 1
        for p in b:
            counts, rest = recursive.residue_strip(p)
            require(recursive.residue_unstrip(counts,rest) == p, ('residue grammar inverse',p))
            require(sum(p) == sum(x*m for x,m in zip((1,3,6,8),counts))+sum(rest)+9*len(rest))
            totals['residue_grammar_round_trips'] += 1
        a3 = {p for p in a if all(v%3 == 0 for v in p)}
        b3 = {p for p in b if all(v%3 == 0 for v in p)}
        gimages = set()
        for p in b3:
            image = recursive.glaisher_three(p)
            require(image in a3 and image not in gimages and sum(image) == n, ('Glaisher validity/collision',p))
            require(recursive.unglaisher_three(image) == p, ('Glaisher source inverse',p))
            gimages.add(image)
            totals['glaisher_source_round_trips'] += 1
        require(gimages == a3, ('Glaisher missing image',n))
        for p in a3:
            require(recursive.glaisher_three(recursive.unglaisher_three(p)) == p)
            totals['glaisher_target_round_trips'] += 1
        rows.append({'weight':n,'actual_U':len(actual_u),'restricted_C':len(images),
                     'uncovered_U':len(actual_u)-len(images),'gap':len(a),'residue':len(b),
                     'glaisher_sector':len(a3)})
    for i, left in enumerate(recursive.TAILS):
        for j, right in enumerate(recursive.TAILS):
            require(kr1.is_gap(left+tuple(x+3 for x in right)) == (j in recursive.LINKS[i]),
                    ('link edge',i,j))
            totals['literal_link_checks'] += 1
    cores = ((3,3,6,9,9,12),(3,3,6,6,12,12))
    refuted = [recursive.refuted_insert_one(p,capture_trace=True) for p in cores]
    require(cores[0] != cores[1] and refuted[0][0] == refuted[1][0] == (3,6,9,9,16))
    require(all(kr1.is_gap(result[0]) and sum(result[0]) == 43 for result in refuted))
    residue_inputs = tuple(tuple(sorted((1,)+recursive.unglaisher_three(p))) for p in cores)
    require(residue_inputs[0] != residue_inputs[1] and all(kr1.is_residue(p) and sum(p) == 43 for p in residue_inputs))
    for name, digest in sources.items():
        require(sha(ROOT/name) == digest, ('source changed during verification',name))
    return {'program':'RR003','round':2,'ceiling':ceiling,'started_claim':'frozen before verification',
            'status':'restricted_finite_checks_passed_full_bijection_unresolved',
            'assurance':'finite empirical implementation check; written proofs and separate review required',
            'full_bijection':'unresolved','novelty':'unverified','source_sha256':sources,
            'totals':dict(totals),'cases':rows,'first_uncovered_U':missing_u,'first_unsupported_C':unsupported_c,
            'direct_refutation_not_enumeration_sweep':{'weight':43,'cores':cores,'residue_inputs':residue_inputs,
                                                       'outcomes_and_traces':refuted}}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--ceiling',type=int,default=12)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--require-bijection',action='store_true')
    args=parser.parse_args()
    if args.output.exists():
        parser.error('refusing to overwrite evidence')
    start=time.monotonic()
    try:
        report=verify(args.ceiling)
        code=2 if args.require_bijection else 0
        if code:
            report['required_completion_failure']='No universal bridge or complete residue-to-gap algorithms'
    except (AssertionError,ValueError,OSError,KeyError) as exc:
        report={'program':'RR003','status':'failed','error':str(exc)}
        code=1
    report['elapsed_seconds']=time.monotonic()-start
    report['finished_utc']=datetime.now(timezone.utc).isoformat()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report if code == 1 else {k:report[k] for k in ('status','elapsed_seconds','totals')}))
    return code


if __name__ == '__main__':
    raise SystemExit(main())
