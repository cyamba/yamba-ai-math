"""Finite full-domain checks of the frozen attributed RR003 Stockhofe endpoint."""
import argparse
from datetime import datetime,timezone
import hashlib,json
from pathlib import Path
import time
import kr1
import rr003_stockhofe as maps

ROOT=Path(__file__).resolve().parents[3]
PHASE=ROOT/'research/rogers-ramanujan/rr003'


def require(condition,message='RR003 endpoint check failed'):
    if not condition:
        raise AssertionError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify(ceiling):
    if type(ceiling) is not int or not 0<=ceiling<=30:
        raise ValueError('ceiling must be an integer in [0,30]')
    freeze_path=PHASE/'endpoint-stockhofe-freeze.json'
    sources=dict(json.loads(freeze_path.read_text())['frozen_sha256'])
    for name,digest in sources.items():
        require(sha(ROOT/name)==digest,('frozen source changed',name))
    sources[str(Path(__file__).relative_to(ROOT))]=sha(Path(__file__))
    sources[str(freeze_path.relative_to(ROOT))]=sha(freeze_path)
    rows=[]
    totals={'column_round_trips':0,'residue_round_trips':0}
    for n in range(ceiling+1):
        actual_u={kr1.weighted_columns(w) for w in kr1.weighted_partitions(n)}
        actual_b=set(kr1.residue_partitions(n))
        images=set()
        for u in actual_u:
            p=maps.columns_to_residue(u)
            require(p in actual_b and sum(p)==sum(u)==n,('validity/weight',u,p))
            require(p not in images,('collision',u,p))
            require(maps.residue_to_columns(p)==u,('U round trip',u,p))
            images.add(p)
            totals['column_round_trips']+=1
        require(images==actual_b,('missing residue image',n))
        reverse_images=set()
        for p in actual_b:
            u=maps.residue_to_columns(p)
            require(u in actual_u and sum(u)==n,('inverse validity/weight',p,u))
            require(u not in reverse_images,('inverse collision',p,u))
            require(maps.columns_to_residue(u)==p,('residue round trip',p,u))
            reverse_images.add(u)
            totals['residue_round_trips']+=1
        require(reverse_images==actual_u,('missing column image',n))
        rows.append({'weight':n,'actual_U':len(actual_u),'actual_B':len(actual_b)})
    heights=(26,25,22,19,15,13,11,7,5,5,3)
    corrected_regular=(41,27,24,23,21,12,3)
    require(maps.flat_to_regular(heights)==corrected_regular,('published example units',))
    require(maps.regular_to_flat(corrected_regular)==heights,('published example inverse',))
    for malformed in ((5,), (6,1), (11,3), (1,2)):
        try:
            maps.flat_to_regular(malformed)
        except ValueError:
            pass
        else:
            raise AssertionError(('invalid flat input accepted',malformed))
    for name,digest in sources.items():
        require(sha(ROOT/name)==digest,('source changed during verification',name))
    return {'program':'RR003','stage':'attributed Stockhofe endpoint','ceiling':ceiling,
            'status':'finite_endpoint_checks_passed_full_KR1_bijection_unresolved',
            'attribution':'Stockhofe as presented by Andrews--Keith arXiv:2203.05202v2 section 2/Theorem 6',
            'assurance':'author-only written endpoint audit and finite checks, no separate review of this code',
            'full_bijection':'unresolved','novelty':'established construction, no novelty claim',
            'totals':totals,'cases':rows,'source_sha256':sources,
            'direct_published_example_not_sweep':{'heights':heights,'regular':corrected_regular}}


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
