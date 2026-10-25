"""Independent protocol obligations for the final local refinement.

Enumerations below are verification only. The imported map and inverse do
not import this file, generate tableau families, or consult saved results.
"""
from collections import Counter
from pathlib import Path
import json
import revision_check as protocol
import revision_layers as layers
from cancellation import moved_labels
from structural import forward as original, triangle_source

protocol.forward=layers.forward
protocol.inverse=layers.inverse
result=protocol.run()
stats=Counter(); layer_counts=Counter(); witnesses=[]
for h in layers.tb.hessenberg_vectors(6):
    for shape in ((5,1),(4,2),(3,1,1,1),(2,2,1,1)):
        for s in layers.tb.tableaux(h,shape):
            out=layers.forward(h,s)
            if out is None:continue
            move=moved_labels(s,out[1]);stats['moved_'+str(move)]+=1
            if move>3:witnesses.append({'kind':'outside_frozen_family2','h':h,'source':s,'out':out})
            for level in range(23):
                if layers.forward(h,s,level) is not None:
                    layer_counts[level]+=1;break
            old=None
            if shape==(5,1):old=original(h,'hook',s)
            elif shape==(4,2):old=original(h,'two',s)
            elif shape==(2,2,1,1):
                branch=triangle_source(h,s)
                if branch is not None:old=original(h,branch,s)
            if old is not None:
                stats['original_assignments']+=1
                if out!=old:witnesses.append({'kind':'changed_original_assignment','h':h,'source':s})
    for tag,shape in (('row0',(6,)),('row1',(6,)),('411',(4,1,1)),('321',(3,2,1)),('21111',(2,1,1,1,1))):
        for target in layers.tb.tableaux(h,shape):
            stats['positive_occurrences']+=1
            stats['positive_'+tag]+=1
            if layers.inverse(h,tag,target) is None:stats['unmatched_positive_occurrences']+=1
result['additional_protocol_counts']=dict(stats)
result['first_assigned_layer_counts']=dict(sorted(layer_counts.items()))
result['failures'].extend(witnesses)
result['status']='finite_exact_passed' if not result['failures'] and not result['remaining'] else 'failed'
Path(__file__).with_name('revision-final-results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ('remaining','all_results')},indent=2))
raise SystemExit(result['status']!='finite_exact_passed')
