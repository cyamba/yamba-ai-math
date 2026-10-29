"""Finite prescribed-map extension diagnostic within frozen move family2."""
from collections import Counter,defaultdict
import json
from pathlib import Path
from cancellation import signed_sectors,moved_labels,maximum_matching,serialize_object,tb
from revision_local import forward


def run():
    totals=Counter(); all_rows=[]; first_failure=None
    for h in tb.hessenberg_vectors(6):
        pos,neg,_,_=signed_sectors(6,(5,1))
        tabs={s['shape']:tuple(tb.tableaux(h,s['shape'])) for s in pos+neg}
        positives=[(i,t) for i,s in enumerate(pos) for t in tabs[s['shape']]]
        negatives=[(i,t) for i,s in enumerate(neg) for t in tabs[s['shape']]]
        pos_index={obj:obj for obj in positives}
        tags={'row0':0,'row1':1,'411':2,'321':3,'21111':4}
        fixed={}
        for src in negatives:
            out=forward(h,src[1])
            if out is not None:
                tag,target=out
                obj=(tags[tag],target)
                assert obj in pos_index
                fixed[src]=obj
        assert len(set(fixed.values()))==len(fixed)
        available=[t for t in positives if t not in set(fixed.values())]
        remaining=[s for s in negatives if s not in fixed]
        by_degree=defaultdict(list)
        for obj in available:
            by_degree[tb.inv_g(h,obj[1])].append(obj)
        adjacency={src:tuple(t for t in by_degree[tb.inv_g(h,src[1])]
                             if moved_labels(src[1],t[1])<=3) for src in remaining}
        mapping,failure=maximum_matching(adjacency,remaining)
        row={'h':h,'fixed':len(fixed),'remaining':len(remaining),
             'matched_remaining':len(mapping),'available_positive':len(available)}
        if failure is not None:
            row['failure']={
                'source':serialize_object(failure['source'],neg),
                'negative_vertices':[serialize_object(s,neg) for s in failure['negative_vertices']],
                'positive_neighbors':[serialize_object(t,pos) for t in failure['positive_neighbors']]}
            if first_failure is None:first_failure=row
        totals.update({k:v for k,v in row.items() if isinstance(v,int)})
        all_rows.append(row)
    return {'status':'finite_extension_passed' if first_failure is None else 'finite_extension_failed',
            'scope':'frozen <=3label family after fixing every revision local pair',
            'totals':totals,'first_failure':first_failure,'all_results':all_rows}


if __name__=='__main__':
    result=run()
    Path(__file__).with_name('revision-extension-results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='all_results'},indent=2))
