"""Frozen restricted recursive-repair verification on actual RR003 A,B domains."""
import argparse
from datetime import datetime,timezone
import hashlib,json
from pathlib import Path
import time
import kr1
import rr003_recursive as failed
import rr003_small_charge as maps

ROOT=Path(__file__).resolve().parents[3]
PHASE=ROOT/'research/rogers-ramanujan/rr003'


def require(condition,message='restricted charge verification failed'):
    if not condition:
        raise AssertionError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify(ceiling):
    if type(ceiling) is not int or not 0<=ceiling<=30:
        raise ValueError('ceiling must be an integer in [0,30]')
    freeze_path=PHASE/'recursive-repair-freeze.json'
    sources=dict(json.loads(freeze_path.read_text())['frozen_sha256'])
    for name,digest in sources.items():
        require(sha(ROOT/name)==digest,('frozen source changed',name))
    sources[str(Path(__file__).relative_to(ROOT))]=sha(Path(__file__))
    sources[str(freeze_path.relative_to(ROOT))]=sha(freeze_path)
    rows=[]
    totals={'residue_round_trips':0,'gap_round_trips':0}
    first_uncovered=first_unsupported=None
    for n in range(ceiling+1):
        actual_a=set(kr1.gap_partitions(n))
        actual_b=set(kr1.residue_partitions(n))
        images=set()
        for p in actual_b:
            if not maps.source_supported(p):
                if first_unsupported is None:
                    first_unsupported={'weight':n,'residue':p}
                continue
            a=maps.residue_to_gap(p)
            require(a in actual_a and sum(a)==n,('validity/weight',p,a))
            require(a not in images,('collision',p,a))
            require(maps.gap_to_residue(a)==p,('B round trip',p,a))
            images.add(a)
            totals['residue_round_trips']+=1
        recognized=set()
        for a in actual_a:
            try:
                p=maps.gap_to_residue(a)
            except maps.OutsideSmallCharge:
                if first_uncovered is None:
                    first_uncovered={'weight':n,'gap':a}
                continue
            require(p in actual_b and maps.source_supported(p) and sum(p)==n,('inverse validity/weight',a,p))
            require(maps.residue_to_gap(p)==a,('A round trip',a,p))
            recognized.add(a)
            totals['gap_round_trips']+=1
        require(recognized==images,('restricted missing image',n))
        rows.append({'weight':n,'actual_A':len(actual_a),'actual_B':len(actual_b),'restricted_images':len(images)})
    cores=((3,3,6,9,9,12),(3,3,6,6,12,12))
    inputs=tuple((1,)+failed.unglaisher_three(c) for c in cores)
    outputs=tuple(maps.residue_to_gap(p) for p in inputs)
    require(outputs==((3,3,6,9,9,13),(1,2,4,5,7,12,12)),('repaired collision witnesses',outputs))
    require(all(maps.gap_to_residue(a)==p for a,p in zip(outputs,inputs)))
    require(sum(inputs[0])==sum(inputs[1])==43 and outputs[0]!=outputs[1])
    for name,digest in sources.items():
        require(sha(ROOT/name)==digest,('source changed during verification',name))
    return {'program':'RR003','stage':'mechanism B final author repair','ceiling':ceiling,
            'status':'restricted_charge_checks_passed_full_KR1_unresolved',
            'assurance':'universal author argument and finite checks; separate semantic review outstanding',
            'full_bijection':'unresolved','novelty':'unverified, Glaisher and cluster endpoint attributed',
            'totals':totals,'cases':rows,'first_uncovered_gap':first_uncovered,
            'first_unsupported_residue':first_unsupported,'source_sha256':sources,
            'direct_repaired_witness43_not_sweep':{'inputs':inputs,'outputs':outputs}}


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
        code=0
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
