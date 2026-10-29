"""Exact n6 test and collision-fiber diagnostic for the reserved refinement."""
from collections import Counter,defaultdict
import json
from pathlib import Path
from revision_local import (tb,forward,inverse,demote,local_preimages,old_inverse,
                            triangle_source)


def run():
    totals, failures, rows, remaining = Counter(), [], [], []
    fiber_hist = Counter()
    for h in tb.hessenberg_vectors(6):
        counts,images,unhandled = Counter(),{},[]
        for shape in ((5,1),(4,2),(3,1,1,1),(2,2,1,1)):
            for source in tb.tableaux(h,shape):
                counts['negative_sources']+=1
                out=forward(h,source)
                if out is None:
                    counts['unhandled']+=1
                    counts['unhandled_'+str(shape)]+=1
                    k=demote(h,source)
                    pre=local_preimages(h,k)
                    witness={'h':h,'source':source,'degree':tb.inv_g(h,source),
                             'demoted':k,'reserved_target':old_inverse(h,'21111',k) is not None,
                             'local_preimages':pre}
                    unhandled.append(witness)
                    remaining.append(witness)
                    continue
                tag,target=out
                counts['mapped']+=1
                counts['mapped_'+str(shape)]+=1
                if not tb.validates(h,target):
                    failures.append({'kind':'invalid_target','h':h,'source':source,'out':out})
                if tb.inv_g(h,source)!=tb.inv_g(h,target):
                    failures.append({'kind':'changed_degree','h':h,'source':source,'out':out})
                if inverse(h,tag,target)!=source:
                    failures.append({'kind':'wrong_inverse','h':h,'source':source,'out':out})
                if out in images:
                    failures.append({'kind':'collision','h':h,'source':source,'prior':images[out],'out':out})
                images[out]=source
        for tag,shape in (('row0',(6,)),('row1',(6,)),('411',(4,1,1)),('321',(3,2,1)),
                          ('21111',(2,1,1,1,1))):
            for target in tb.tableaux(h,shape):
                source=inverse(h,tag,target)
                if source is not None:
                    counts['recognized_images']+=1
                    if forward(h,source)!=(tag,target) or not tb.validates(h,source):
                        failures.append({'kind':'false_image_recognition','h':h,'target':target,'tag':tag})
                if ((tag,target) in images)!=(source is not None):
                    failures.append({'kind':'image_language_mismatch','h':h,'target':target,'tag':tag})
                if tag=='21111':
                    fiber_hist[len(local_preimages(h,target))]+=1
        totals.update(counts)
        rows.append({'h':h,**counts})
    return {'status':'finite_exact_passed' if not failures else 'failed','n':6,
            'totals':totals,'hessenberg_vectors':len(rows),'failures':failures,
            'local_fiber_histogram':dict(sorted(fiber_hist.items())),
            'remaining':remaining,'all_results':rows}


if __name__=='__main__':
    result=run()
    Path(__file__).with_name('revision-results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('remaining','all_results')},indent=2))
    if result['remaining']:
        print(json.dumps({'first_remaining':result['remaining'][0]},indent=2))
    raise SystemExit(bool(result['failures']))
