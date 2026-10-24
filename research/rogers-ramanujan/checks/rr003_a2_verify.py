"""Finite checks for frozen final RR003 author-only a<=2 revision.

No complete KR1 bijection is certified; --require-bijection always exits two.
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
import rr003_a2 as maps

ROOT=Path(__file__).resolve().parents[3]
PHASE=ROOT/'research/rogers-ramanujan/rr003'


def require(condition,message='RR003 author-only finite check failed'):
    if not condition:
        raise AssertionError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify(ceiling):
    if type(ceiling) is not int or not 0 <= ceiling <= 30:
        raise ValueError('ceiling must be an integer between zero and thirty')
    freeze_path=PHASE/'round-2-revision-freeze.json'
    freeze=json.loads(freeze_path.read_text())
    sources=dict(freeze['frozen_sha256'])
    for name,digest in sources.items():
        require(sha(ROOT/name)==digest,('frozen source changed',name))
    sources[str(Path(__file__).relative_to(ROOT))]=sha(Path(__file__))
    sources[str(freeze_path.relative_to(ROOT))]=sha(freeze_path)
    totals,rows=Counter(),[]
    missing_u=unsupported_c=None
    for n in range(ceiling+1):
        actual_u={kr1.weighted_columns(w) for w in kr1.weighted_partitions(n)}
        images=set()
        for c in kr1.cluster_data(n):
            if not maps.supported(c):
                if unsupported_c is None:
                    unsupported_c={'weight':n,'cluster':asdict(c)}
                continue
            u=maps.reconstruct_columns(c)
            require(u in actual_u and sum(u)==c.weight==n,('validity/weight',c,u))
            require(u not in images,('collision',c,u))
            require(maps.decompose_columns(u)==c,('C round trip',c,u))
            images.add(u)
            totals['cluster_round_trips']+=1
            if c.mu:
                raised=kr1.ClusterData(c.a,c.b,c.mu[:-1]+(c.mu[-1]+1,),c.nu)
                require(maps.reconstruct_columns(raised)==tuple(sorted(u+(1,),reverse=True)),('last mu',c))
                totals['unit_operations']+=1
            if c.a==2:
                raised=maps.raise_common_columns(u)
                require(sum(raised)==n+2 and maps.lower_common_columns(raised)==u,('common operation',c))
                kr1.decode_columns(raised)
                require(maps.decompose_columns(raised)==kr1.ClusterData(2,c.b,tuple(v+1 for v in c.mu),c.nu))
                totals['common_operations']+=1
            for j in range(1,c.b+1):
                raised=maps.raise_nu_columns(u,j)
                expected=kr1.ClusterData(c.a,c.b,c.mu,tuple(v+int(i>=c.b-j) for i,v in enumerate(c.nu)))
                require(sum(raised)==n+3*j and maps.decompose_columns(raised)==expected,('nu operation',c,j))
                kr1.decode_columns(raised)
                totals['nu_operations']+=1
        recognized=set()
        for u in actual_u:
            try:
                c=maps.decompose_columns(u)
            except maps.OutsideRestrictedDomain:
                if missing_u is None or n < missing_u['weight'] or (n==missing_u['weight'] and u<tuple(missing_u['columns'])):
                    missing_u={'weight':n,'columns':u}
                continue
            require(maps.supported(c) and c.weight==n,('inverse domain/weight',u,c))
            require(maps.reconstruct_columns(c)==u,('U round trip',u,c))
            recognized.add(u)
            totals['column_round_trips']+=1
        require(recognized==images,('restricted missing image',n))
        rows.append({'weight':n,'actual_U':len(actual_u),'restricted_C':len(images),'uncovered_U':len(actual_u)-len(images)})
    samples=[]
    # One literal structured sample for each exceptional/dense template branch.
    for k,b in ((4,1),(4,2),(4,3),(5,1),(5,2),(5,3),(5,4),(9,1),(9,2),(9,3),(9,4),(9,5),(9,6)):
        nu=tuple(range(b)) if b>1 else (3,)
        c=kr1.ClusterData(2,b,(k,k+2),nu)
        u=maps.reconstruct_columns(c)
        kr1.decode_columns(u)
        require(sum(u)==c.weight and maps.decompose_columns(u)==c,('direct template sample',c,u))
        require(maps.lower_common_columns(maps.raise_common_columns(u))==u,('direct common carry',c))
        samples.append({'cluster':asdict(c),'weight':c.weight,'columns':u})
        totals['direct_structured_samples']+=1
    for name,digest in sources.items():
        require(sha(ROOT/name)==digest,('source changed during verification',name))
    return {'program':'RR003','stage':'round-two final author revision','ceiling':ceiling,
            'status':'restricted_finite_checks_passed_full_bijection_unresolved',
            'assurance':'finite implementation checks; author-only written argument, no separate review of this extension',
            'full_bijection':'unresolved','novelty':'unverified','source_sha256':sources,
            'totals':dict(totals),'cases':rows,'first_uncovered_U':missing_u,'first_unsupported_C':unsupported_c,
            'direct_structured_samples_not_enumeration_sweep':samples}


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
    print(json.dumps(report if code==1 else {k:report[k] for k in ('status','elapsed_seconds','totals')}))
    return code


if __name__=='__main__':
    raise SystemExit(main())
