"""Frozen RR003 auxiliary P2/P3/cut actual-domain involution verification."""
import argparse,hashlib,json,time
from pathlib import Path
import kr1
import rr003_product_involution as maps
ROOT=Path(__file__).resolve().parents[3]


def require(condition,message):
    if not condition:
        raise AssertionError(message)


def literal_cut(j,parts):
    for x in parts:
        if x in (2,3) or x%9 not in (2,3,4,5,6,7):
            return False
        if x%9 in (2,7) and x//9>j:
            return False
        if x%9 in (4,5) and x//9<j:
            return False
    return True


def verify(ceiling):
    if type(ceiling) is not int or not 0<=ceiling<=30:
        raise ValueError('ceiling in [0,30] required')
    freeze_path=ROOT/'research/rogers-ramanujan/rr003/product-involution-freeze.json'
    sources=dict(json.loads(freeze_path.read_text())['frozen_sha256'])
    sources[str(Path(__file__).relative_to(ROOT))]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    sources['research/rogers-ramanujan/checks/kr1.py']=hashlib.sha256(Path(kr1.__file__).read_bytes()).hexdigest()
    for name,digest in sources.items():
        require(hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest,('frozen source changed',name))
    rows=[];total2=total3=totalk=totalsteps=maxsteps=0
    for n in range(ceiling+1):
        ordinary=tuple(kr1.ordinary_partitions(n))
        actual2={p for p in ordinary if all(x%9 in (2,3,6,7) for x in p)}
        actual3={p for p in ordinary if all(x%9 in (3,4,5,6) for x in p)}
        cuts={maps.Cut(j,d) for j in range((n-2)//9+1)
              for d in kr1.ordinary_partitions(n-9*j-2) if literal_cut(j,d)}
        expected={('P3',p) for p in actual3}|{('K',c) for c in cuts}
        images=set();inverse_images=set()
        for p in actual2:
            result,steps=maps.split_p2(p,audit=True,with_steps=True)
            require(result in expected,('invalid split endpoint',p,result))
            require(result not in images,('split collision',p,result))
            images.add(result)
            if result[0]=='P3':
                back,backsteps=maps.join_p3(result[1],audit=True,with_steps=True)
            else:
                back,backsteps=maps.join_cut(result[1],audit=True,with_steps=True)
            require(back==p,('P2 round trip',p,result,back))
            totalsteps+=steps+backsteps;maxsteps=max(maxsteps,steps,backsteps)
        require(images==expected,('missing P3/cut image',n))
        for kind,value in expected:
            p,steps=(maps.join_p3 if kind=='P3' else maps.join_cut)(value,audit=True,with_steps=True)
            require(p in actual2 and p not in inverse_images,('invalid/colliding join',kind,value,p))
            inverse_images.add(p)
            result,backsteps=maps.split_p2(p,audit=True,with_steps=True)
            require(result==(kind,value),('P3/cut round trip',kind,value,p,result))
            totalsteps+=steps+backsteps;maxsteps=max(maxsteps,steps,backsteps)
        require(inverse_images==actual2,('missing P2 image',n))
        total2+=len(actual2);total3+=len(actual3);totalk+=len(cuts)
        rows.append({'weight':n,'actual_P2':len(actual2),'actual_P3':len(actual3),'actual_K':len(cuts)})
    # Five explicit structured samples, not an enumeration sweep above30.
    witnesses=((3,5,5,21),(5,5,12,12),(3,3,5,23),(3,3,14,14),(3,5,12,14))
    witness_images=[]
    for p in witnesses:
        image,steps=maps.join_p3(p,audit=True,with_steps=True)
        back,backsteps=maps.split_p2(image,audit=True,with_steps=True)
        require(back==('P3',p) and sum(image)==34,('direct weight34 round trip',p,image,back))
        witness_images.append(image)
        totalsteps+=steps+backsteps;maxsteps=max(maxsteps,steps,backsteps)
    require(len(set(witness_images))==5,('direct weight34 collision',witness_images))
    return {'program':'RR003','status':'auxiliary_product_bijection_checks_passed_complete_KR1_unresolved',
            'ceiling':ceiling,'P2_round_trips':total2,'P3_round_trips':total3,'cut_round_trips':totalk,
            'maximum_walk_steps':maxsteps,'audited_walk_steps':totalsteps,'cases':rows,
            'assurance':'universal author finite-path argument; no separate semantic review',
            'novelty':'unverified','full_bijection':'unresolved',
            'complexity':'conservative exponential work bound exceeds preferred quartic; binding investigation limits unchanged',
            'direct_weight34_samples_not_sweep':{'sources':witnesses,'images':witness_images},'source_sha256':sources}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--ceiling',type=int,default=12)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    if args.output.exists():
        parser.error('refusing to overwrite evidence')
    start=time.monotonic()
    try:
        report=verify(args.ceiling);code=0
    except (AssertionError,ValueError,OSError,KeyError) as exc:
        report={'program':'RR003','status':'failed','error':str(exc)};code=1
    report['elapsed_seconds']=time.monotonic()-start
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report if code else {k:report[k] for k in ('status','P2_round_trips','P3_round_trips','cut_round_trips','maximum_walk_steps','elapsed_seconds')}))
    return code


if __name__=='__main__':
    raise SystemExit(main())
