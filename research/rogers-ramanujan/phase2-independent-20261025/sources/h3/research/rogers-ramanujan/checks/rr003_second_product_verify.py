"""Frozen RR003 packet/P1/L actual-domain involution verification."""
import argparse,hashlib,json,time
from pathlib import Path
import kr1
import rr003_second_product as maps
ROOT=Path(__file__).resolve().parents[3]


def require(condition,message):
    if not condition:
        raise AssertionError(message)


def literal_cut(j,parts):
    for x in parts:
        r=x%9
        if r in (3,6):
            if x==3:
                return False
        elif r==7:
            if x//9>j:
                return False
        elif r==2:
            if x<11 or (x-11)//9>j:
                return False
        elif r==8:
            if x//9<j:
                return False
        elif r==1:
            if x<10 or (x-10)//9<j:
                return False
        else:
            return False
    return True


def verify(ceiling):
    if type(ceiling) is not int or not 0<=ceiling<=30:
        raise ValueError('ceiling in [0,30] required')
    freeze_path=ROOT/'research/rogers-ramanujan/rr003/second-product-freeze.json'
    sources=dict(json.loads(freeze_path.read_text())['frozen_sha256'])
    sources[str(Path(__file__).relative_to(ROOT))]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    sources['research/rogers-ramanujan/checks/kr1.py']=hashlib.sha256(Path(kr1.__file__).read_bytes()).hexdigest()
    for name,digest in sources.items():
        require(hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest,('frozen source changed',name))
    ordinary={n:tuple(kr1.ordinary_partitions(n)) for n in range(ceiling+1)}
    p2={n:{p for p in ordinary[n] if all(x%9 in (2,3,6,7) for x in p)} for n in range(ceiling+1)}
    rows=[];totalpacket=total1=totall=totalsteps=maxsteps=0
    for n in range(ceiling+1):
        packets={maps.Packet(e,p) for e in (0,1) if n>=e for p in p2[n-e]}
        actual1={p for p in ordinary[n] if all(x%9 in (1,3,6,8) for x in p)}
        require(actual1==set(kr1.residue_partitions(n)),('P1 generator disagreement',n))
        cuts={maps.Cut(j,d) for j in range((n-7)//9+1)
              for d in ordinary[n-9*j-7] if literal_cut(j,d)}
        expected={('P1',p) for p in actual1}|{('L',c) for c in cuts}
        images=set();inverse_images=set()
        for packet in packets:
            result,steps=maps.split_packet(packet,audit=True,with_steps=True)
            require(result in expected and result not in images,('invalid/colliding packet split',packet,result))
            images.add(result)
            back,backsteps=(maps.join_p1 if result[0]=='P1' else maps.join_cut)(result[1],audit=True,with_steps=True)
            require(back==packet,('packet round trip',packet,result,back))
            totalsteps+=steps+backsteps;maxsteps=max(maxsteps,steps,backsteps)
        require(images==expected,('missing P1/L image',n))
        for kind,value in expected:
            packet,steps=(maps.join_p1 if kind=='P1' else maps.join_cut)(value,audit=True,with_steps=True)
            require(packet in packets and packet not in inverse_images,('invalid/colliding join',kind,value,packet))
            inverse_images.add(packet)
            result,backsteps=maps.split_packet(packet,audit=True,with_steps=True)
            require(result==(kind,value),('P1/L round trip',kind,value,packet,result))
            totalsteps+=steps+backsteps;maxsteps=max(maxsteps,steps,backsteps)
        require(inverse_images==packets,('missing packet image',n))
        totalpacket+=len(packets);total1+=len(actual1);totall+=len(cuts)
        rows.append({'weight':n,'actual_packets':len(packets),'actual_P1':len(actual1),'actual_L':len(cuts)})
    return {'program':'RR003','status':'second_auxiliary_product_checks_passed_complete_KR1_unresolved',
            'ceiling':ceiling,'packet_round_trips':totalpacket,'P1_round_trips':total1,'cut_round_trips':totall,
            'maximum_walk_steps':maxsteps,'audited_walk_steps':totalsteps,'cases':rows,
            'assurance':'universal author finite-path argument; no separate semantic review',
            'novelty':'unverified','full_bijection':'unresolved',
            'complexity':'conservative exponential work bound exceeds preferred quartic; binding investigation limits unchanged',
            'source_sha256':sources}


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
    print(json.dumps(report if code else {k:report[k] for k in ('status','packet_round_trips','P1_round_trips','cut_round_trips','maximum_walk_steps','elapsed_seconds')}))
    return code


if __name__=='__main__':
    raise SystemExit(main())
