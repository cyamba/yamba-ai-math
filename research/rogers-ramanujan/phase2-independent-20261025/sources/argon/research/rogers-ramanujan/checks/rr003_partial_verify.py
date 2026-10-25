"""Finite actual-domain checks of the RR003 restricted residue<->gap composition."""
import argparse
from datetime import datetime,timezone
import hashlib,json
from pathlib import Path
import time
import kr1
import rr003_partial as maps

ROOT=Path(__file__).resolve().parents[3]
PHASE=ROOT/'research/rogers-ramanujan/rr003'


def require(condition,message='RR003 partial composition check failed'):
    if not condition:
        raise AssertionError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify(ceiling):
    if type(ceiling) is not int or not 0<=ceiling<=30:
        raise ValueError('ceiling must be an integer in [0,30]')
    freeze_path=PHASE/'partial-composition-freeze.json'
    sources=dict(json.loads(freeze_path.read_text())['frozen_sha256'])
    for name,digest in sources.items():
        require(sha(ROOT/name)==digest,('frozen source changed',name))
    sources[str(Path(__file__).relative_to(ROOT))]=sha(Path(__file__))
    sources[str(freeze_path.relative_to(ROOT))]=sha(freeze_path)
    rows=[]
    totals={'residue_round_trips':0,'gap_round_trips':0}
    first_b=first_a=None
    for n in range(ceiling+1):
        actual_a=set(kr1.gap_partitions(n))
        actual_b=set(kr1.residue_partitions(n))
        expected_a={p for p in actual_a if len(p)-2*sum(y-x<=1 for x,y in zip(p,p[1:]))<=2}
        images=set()
        supported_b=set()
        for p in actual_b:
            try:
                a=maps.residue_to_gap(p)
            except maps.OutsideRestrictedDomain:
                if first_b is None:
                    first_b={'weight':n,'residue':p}
                continue
            require(a in expected_a and sum(a)==n,('validity/weight',p,a))
            require(a not in images,('collision',p,a))
            require(maps.gap_to_residue(a)==p,('B round trip',p,a))
            images.add(a)
            supported_b.add(p)
            totals['residue_round_trips']+=1
        require(images==expected_a,('missing restricted gap image',n))
        inverse_images=set()
        for a in actual_a:
            if a not in expected_a:
                if first_a is None:
                    first_a={'weight':n,'gap':a}
                try:
                    maps.gap_to_residue(a)
                except maps.OutsideRestrictedDomain:
                    continue
                raise AssertionError(('unsupported gap accepted',a))
            p=maps.gap_to_residue(a)
            require(p in actual_b and sum(p)==n,('inverse validity/weight',a,p))
            require(p not in inverse_images,('inverse collision',a,p))
            require(maps.residue_to_gap(p)==a,('A round trip',a,p))
            inverse_images.add(p)
            totals['gap_round_trips']+=1
        require(inverse_images==supported_b,('missing restricted residue image',n))
        rows.append({'weight':n,'actual_A':len(actual_a),'actual_B':len(actual_b),'restricted_images':len(images)})
    for name,digest in sources.items():
        require(sha(ROOT/name)==digest,('source changed during verification',name))
    return {'program':'RR003','stage':'final restricted endpoint composition','ceiling':ceiling,
            'status':'restricted_end_to_end_checks_passed_complete_KR1_unresolved',
            'assurance':'finite implementation checks plus universal author arguments; final extensions lack separate review',
            'full_bijection':'unresolved','novelty':'unverified','totals':totals,'cases':rows,
            'first_unsupported_residue':first_b,'first_uncovered_gap':first_a,'source_sha256':sources}


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
            report['required_completion_failure']='No universal U-C bridge or complete accepted residue-to-gap bijection'
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
