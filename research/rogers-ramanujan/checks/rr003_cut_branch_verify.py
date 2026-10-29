"""Frozen RR003 K[-2]/P3 intrinsic branch verification; actual weights <=30."""
import argparse,hashlib,json
from collections import Counter
from pathlib import Path
import kr1
import rr003_product_involution as products
import rr003_second_product as second
import rr003_cut_branch as maps
ROOT=Path(__file__).resolve().parents[3]


def require(condition,message):
    if not condition:
        raise AssertionError(message)


def expected_branch(parts):
    counts=Counter(parts)
    t,s=counts[3],counts[6]
    return any(3*j+sum(c for x,c in counts.items() if x%9==4 and x//9<j)<=t
               <=3*j+sum(c for x,c in counts.items() if x%9==4 and x//9<j)+counts[9*j+4]
               and s>=sum(c for x,c in counts.items() if x%9==5 and x//9<j)
               for j in range(t//3+1))


def literal_cut(j,parts):
    return all(x not in (2,3) and x%9 in (2,3,4,5,6,7)
               and (x%9 not in (2,7) or x//9<=j)
               and (x%9 not in (4,5) or x//9>=j) for x in parts)


def verify(ceiling):
    if type(ceiling) is not int or not 2<=ceiling<=30:
        raise ValueError('actual cut-weight ceiling in [2,30] required')
    freeze_path=ROOT/'research/rogers-ramanujan/rr003/cut-branch-freeze.json'
    sources=json.loads(freeze_path.read_text())['frozen_sha256']
    for name,digest in sources.items():
        require(hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest,('frozen source changed',name))
    rows=[];total=0
    for n in range(ceiling-1):
        cuts={products.Cut(j,d) for j in range(n//9+1)
              for d in kr1.ordinary_partitions(n-9*j) if literal_cut(j,d)}
        actual={p for p in kr1.ordinary_partitions(n) if all(x%9 in (3,4,5,6) for x in p)}
        expected={p for p in actual if expected_branch(p)}
        images=set()
        for cut in cuts:
            image=maps.cut_to_p3(cut)
            require(image in expected and sum(image)==cut.weight-2==n,('validity/normalized weight',cut,image))
            require(image not in images,('collision',cut,image))
            require(maps.p3_to_cut(image)==cut,('cut round trip',cut,image))
            images.add(image);total+=1
        require(images==expected,('missing restricted image',n))
        for p in actual:
            if p in expected:
                cut=maps.p3_to_cut(p)
                require(cut in cuts and maps.cut_to_p3(cut)==p,('P3 round trip',p,cut))
            else:
                try:
                    maps.p3_to_cut(p)
                except maps.OutsideBranch:
                    continue
                raise AssertionError(('unrecognized missing sector accepted',p))
        rows.append({'cut_weight':n+2,'P3_weight':n,'actual_cuts':len(cuts),'actual_P3':len(actual),'restricted_images':len(images)})
    sample=products.Cut(3,(6,7,11,12,16,29,31,32,34))
    target=maps.cut_to_p3(sample)
    require(maps.p3_to_cut(target)==sample,('direct large cut sample',))
    # Two explicit L inputs, not a sweep above30 or a promoted map.
    left=second.Cut(0,(6,6,6,8,8,8));right=second.Cut(1,(11,11,11))
    require(second.is_cut(left) and second.is_cut(right) and left.weight==right.weight==49,('L collision inputs',))
    collision=(3,3,3,3,3,5,5,5,6,6,6)
    def corrected_failed_conversion(cut):
        result=[3]*(3*cut.j+2)
        for x in cut.parts:
            if x%9 in (7,8):
                result.extend((x-3,3))
            elif x%9 in (1,2):
                result.extend((x-6,6))
            else:
                result.append(x)
        return tuple(sorted(result))
    require(corrected_failed_conversion(left)==corrected_failed_conversion(right)==collision,('corrected L collision',))
    require(sum(collision)==48,('L collision weight',))
    literal_bad=(3,3,6,13)
    require(second.is_cut(second.Cut(0,(10,))) and sum(literal_bad)==25!=16,('literal next-level replacement weight failure',))
    return {'program':'RR003','status':'intrinsic_K_branch_checks_passed_complete_KR1_unresolved',
            'actual_cut_weight_ceiling':ceiling,'P3_weight_ceiling':ceiling-2,
            'cut_round_trips':total,'P3_round_trips':total,'cases':rows,
            'assurance':'universal author interval proof; no separate semantic review',
            'full_bijection':'unresolved','novelty':'unverified','source_sha256':sources,
            'direct_large_sample_not_sweep':{'cut_j':sample.j,'cut_parts':sample.parts,'image':target},
            'direct_corrected_failed_L_variant_not_sweep':{'source_weight':49,'normalized_source_weight':42,'target_weight':48,'image':collision}}


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
    print(json.dumps({k:report[k] for k in ('status','actual_cut_weight_ceiling','P3_weight_ceiling','cut_round_trips','P3_round_trips')}))


if __name__=='__main__':
    main()
