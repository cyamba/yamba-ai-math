"""RR003 frozen classical three-divisible column-sector checks; no full bridge."""
import argparse
import hashlib,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]
sys.path.insert(0,str(ROOT/'research/rogers-ramanujan/checks'))
import kr1
import rr003_cluster_merge as clusters


def require(condition,message):
    if not condition:
        raise AssertionError(message)


def forward(u):
    kr1.decode_columns(u)
    if any(x%3 for x in u):
        raise ValueError('outside U3')
    return tuple(3*x for x in reversed(kr1.conjugate(tuple(x//3 for x in u))))


def inverse(a):
    if not kr1.is_gap(a) or any(x%3 for x in a):
        raise ValueError('outside A3')
    return tuple(3*x for x in kr1.conjugate(tuple(x//3 for x in reversed(a))))


def direct_coordinates(u):
    kr1.decode_columns(u)
    if any(x%3 for x in u):
        raise ValueError('outside U3')
    levels=tuple(x//3 for x in u)
    singles=pairs=0
    mu=[];nu=[]
    for i,(x,y) in enumerate(zip(levels,levels[1:]+(0,)),1):
        if x-y==1:
            mu.append(3*i-3*pairs-2*singles-1)
            singles+=1
        elif x-y==2:
            nu.append(2*i-1-2*pairs-singles)
            pairs+=1
        else:
            require(x==y,('invalid scaled drop',u,i))
    return kr1.ClusterData(singles,pairs,tuple(mu),tuple(nu))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--ceiling',type=int,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    if not 0<=args.ceiling<=30 or args.output.exists():
        parser.error('ceiling in [0,30] and a new output path required')
    freeze_path=ROOT/'research/rogers-ramanujan/rr003/three-divisible-freeze.json'
    sources=json.loads(freeze_path.read_text())['frozen_sha256']
    for name,digest in sources.items():
        require(hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest,('frozen source changed',name))
    rows=[];count=0
    for n in range(args.ceiling+1):
        us={kr1.weighted_columns(w) for w in kr1.weighted_partitions(n) if all(x%3==0 for x in kr1.weighted_columns(w))}
        actual_a={a for a in kr1.gap_partitions(n) if all(x%3==0 for x in a)}
        images=set()
        for u in us:
            a=forward(u)
            require(a in actual_a and inverse(a)==u,('forward/inverse',u,a))
            c=direct_coordinates(u)
            require(c==clusters.gap_to_cluster(a) and c.weight==n,('intrinsic coordinates',u,c,a))
            raised=u+(3,)
            raised_c=direct_coordinates(raised)
            expected=(1,0) if not u else ((c.a,c.b) if u[-1]==3 else (c.a+2,c.b-1))
            require((raised_c.a,raised_c.b)==expected and raised_c.weight==n+3,('coupled operation',u,c,raised_c))
            require(inverse(forward(raised))==raised,('operation reverse',raised))
            images.add(a);count+=1
        require(images==actual_a and all(forward(inverse(a))==a for a in actual_a),('missing image',n))
        rows.append({'weight':n,'actual_U3':len(us),'actual_A3':len(actual_a)})
    a,b=5,3
    gap=tuple(x for j in range(1,b+1) for x in (3*j,3*j))+tuple(3*(b+i) for i in range(1,a+1))
    u=inverse(gap)
    require(direct_coordinates(u)==kr1.ClusterData(a,b,tuple(range(2,a+2)),(1,)*b),('all-parameter family sample',))
    report={'program':'RR003','status':'classical_sector_finite_checks_passed_full_bridge_unresolved','ceiling':args.ceiling,
            'assurance':'universal classical conjugation argument and author coordinates, no separate review of this specialization',
            'column_round_trips':count,'gap_round_trips':count,'coupled_operations':count,'cases':rows,
            'direct_all_parameter_sample_not_sweep':{'a':a,'b':b,'gap':gap,'columns':u},'source_sha256':sources}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ('status','column_round_trips','gap_round_trips','coupled_operations')}))


if __name__=='__main__':
    main()
