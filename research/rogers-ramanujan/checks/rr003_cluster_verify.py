"""Finite frozen-candidate tests of the RR003 attributed cluster endpoint."""
import argparse
from dataclasses import asdict
from datetime import datetime,timezone
import hashlib,json
from pathlib import Path
import time
import kr1
import rr003_clusters as maps

ROOT=Path(__file__).resolve().parents[3]
PHASE=ROOT/'research/rogers-ramanujan/rr003'


def require(condition,message='cluster endpoint check failed'):
    if not condition:
        raise AssertionError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify(ceiling):
    if type(ceiling) is not int or not 0<=ceiling<=30:
        raise ValueError('ceiling must be an integer in [0,30]')
    freeze_path=PHASE/'endpoint-clusters-freeze.json'
    sources=dict(json.loads(freeze_path.read_text())['frozen_sha256'])
    for name,digest in sources.items():
        require(sha(ROOT/name)==digest,('frozen source changed',name))
    sources[str(Path(__file__).relative_to(ROOT))]=sha(Path(__file__))
    sources[str(freeze_path.relative_to(ROOT))]=sha(freeze_path)
    rows=[]
    totals={'cluster_round_trips':0,'gap_round_trips':0}
    for n in range(ceiling+1):
        actual_a=set(kr1.gap_partitions(n))
        actual_c=set(kr1.cluster_data(n))
        images=set()
        for c in actual_c:
            try:
                p=maps.cluster_to_gap(c)
                require(p in actual_a and sum(p)==c.weight==n,('validity/weight',asdict(c),p))
                require(p not in images,('collision',asdict(c),p))
                recovered=maps.gap_to_cluster(p)
                require(recovered==c,('C round trip',asdict(c),p,asdict(recovered)))
                images.add(p)
                totals['cluster_round_trips']+=1
            except (AssertionError,ValueError) as exc:
                return {'program':'RR003','status':'failed','ceiling':ceiling,'weight':n,
                        'direction':'cluster_to_gap_to_cluster','cluster':asdict(c),
                        'error':str(exc),'totals_before_failure':totals,'source_sha256':sources}
        require(images==actual_a,('missing gap image',n))
        for p in actual_a:
            try:
                c=maps.gap_to_cluster(p)
                require(c in actual_c and c.weight==n,('inverse validity/weight',p,asdict(c)))
                require(maps.cluster_to_gap(c)==p,('A round trip',p,asdict(c)))
                totals['gap_round_trips']+=1
            except (AssertionError,ValueError) as exc:
                return {'program':'RR003','status':'failed','ceiling':ceiling,'weight':n,
                        'direction':'gap_to_cluster_to_gap','gap':p,'error':str(exc),
                        'totals_before_failure':totals,'source_sha256':sources}
        rows.append({'weight':n,'actual_A':len(actual_a),'actual_C':len(actual_c)})
    for name,digest in sources.items():
        require(sha(ROOT/name)==digest,('source changed during verification',name))
    return {'program':'RR003','stage':'candidate attributed cluster endpoint','ceiling':ceiling,
            'status':'finite_candidate_endpoint_checks_passed_universal_conformance_unproved',
            'attribution':'Kursungoz arXiv:1808.01432v1 Theorem 7; uniform obstacle interpreter proposed here',
            'assurance':'finite implementation checks, no universal interpreter proof or separate semantic review',
            'full_bijection':'unresolved','novelty':'unverified, endpoint theorem established',
            'totals':totals,'cases':rows,'source_sha256':sources}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--ceiling',type=int,default=12)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    if args.output.exists():
        parser.error('refusing to overwrite evidence')
    start=time.monotonic()
    try:
        report=verify(args.ceiling)
        code=1 if report['status']=='failed' else 0
    except (AssertionError,ValueError,OSError,KeyError) as exc:
        report={'program':'RR003','status':'failed','error':str(exc)}
        code=1
    report['elapsed_seconds']=time.monotonic()-start
    report['finished_utc']=datetime.now(timezone.utc).isoformat()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report if code else {k:report[k] for k in ('status','elapsed_seconds','totals')}))
    return code


if __name__=='__main__':
    raise SystemExit(main())
