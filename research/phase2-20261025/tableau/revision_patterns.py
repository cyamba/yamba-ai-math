"""Discovery-only: position patterns of still-available <=3label targets."""
from collections import Counter,defaultdict
import json
from pathlib import Path
from cancellation import signed_sectors,moved_labels,tb
from revision_layers import forward,inverse

def run():
    counts=Counter();examples={};remaining=[]
    for h in tb.hessenberg_vectors(6):
        pos,neg,_,_=signed_sectors(6,(5,1))
        tags={0:'row0',1:'row1',2:'411',3:'321',4:'21111'}
        available=[]
        for i,s in enumerate(pos):
            for t in tb.tableaux(h,s['shape']):
                if inverse(h,tags[i],t) is None:available.append((tags[i],t,tb.inv_g(h,t)))
        for s in neg:
            for source in tb.tableaux(h,s['shape']):
                if forward(h,source) is not None:continue
                word=sum(source,());location={x:i for i,x in enumerate(word)}
                used=set();allowed=[]
                for tag,t,degree in available:
                    if degree!=tb.inv_g(h,source) or moved_labels(source,t)>3:continue
                    pattern=(tag,tuple(map(len,t)),tuple(location[x] for row in t for x in row))
                    if pattern not in used:
                        counts[pattern]+=1;used.add(pattern)
                        examples.setdefault(pattern,{'h':h,'source':source,'target':t})
                    allowed.append(pattern)
                remaining.append({'h':h,'source':source,'allowed_patterns':allowed})
    top=[{'pattern':p,'coverage':c,'example':examples[p]} for p,c in counts.most_common(25)]
    return {'remaining_sources':len(remaining),'distinct_patterns':len(counts),'top':top,'sources':remaining}

if __name__=='__main__':
    r=run();Path(__file__).with_name('revision-pattern-discovery.json').write_text(json.dumps(r,indent=2)+'\n')
    print(json.dumps({k:v for k,v in r.items() if k!='sources'},indent=2))
