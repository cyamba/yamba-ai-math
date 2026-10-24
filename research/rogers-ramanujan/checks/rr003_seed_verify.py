"""Frozen RR003 auxiliary source-seed checks on actual P2/P3 partitions."""
import argparse,hashlib,json
from pathlib import Path
import kr1
import rr003_recursive_seed as maps
ROOT=Path(__file__).resolve().parents[3]


def require(condition,message):
    if not condition:
        raise AssertionError(message)


def verify(ceiling):
    if type(ceiling) is not int or not 0<=ceiling<=30:
        raise ValueError('ceiling in [0,30] required')
    freeze_path=ROOT/'research/rogers-ramanujan/rr003/recursive-source-seed-freeze.json'
    sources=json.loads(freeze_path.read_text())['frozen_sha256']
    for name,digest in sources.items():
        require(hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest,('frozen source changed',name))
    rows=[];count=0
    for n in range(ceiling+1):
        ordinary=tuple(kr1.ordinary_partitions(n))
        p3={p for p in ordinary if all(x%9 in (3,4,5,6) for x in p)}
        p2={p for p in ordinary if all(x%9 in (2,3,6,7) for x in p)}
        supported={p for p in p3 if all(x%3==0 or x in (4,5) for x in p)}
        expected={p for p in p2 if all(x%3==0 or x in (2,7) for x in p)
                  and p.count(3)>=p.count(7)+p.count(2)%2}
        images=set()
        for source in supported:
            target=maps.inject(source)
            require(target in expected and sum(target)==n,('validity/weight',source,target))
            require(target not in images,('collision',source,target))
            require(maps.recover(target)==source,('source round trip',source,target))
            images.add(target);count+=1
        require(images==expected,('missing restricted image',n))
        for target in expected:
            source=maps.recover(target)
            require(source in supported and maps.inject(source)==target,('target round trip',target,source))
        for source in p3-supported:
            require(not maps.source_supported(source),('unsupported source accepted',source))
        for target in p2-expected:
            require(not maps.target_supported(target),('unsupported target accepted',target))
        rows.append({'weight':n,'actual_P3':len(p3),'actual_P2':len(p2),'restricted_images':len(images)})
    return {'program':'RR003','status':'restricted_auxiliary_seed_checks_passed_full_KR1_unresolved',
            'ceiling':ceiling,'source_round_trips':count,'target_round_trips':count,
            'assurance':'universal author argument and finite checks; separate review outstanding',
            'novelty':'unverified','cases':rows,'source_sha256':sources}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--ceiling',type=int,default=12)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    if args.output.exists():
        parser.error('refusing to overwrite evidence')
    report=verify(args.ceiling)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ('status','source_round_trips','target_round_trips')}))


if __name__=='__main__':
    main()
