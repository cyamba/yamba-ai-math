"""Four fixed local extension layers; no global family enumeration or state.

Each layer prescribes one candidate target for each source. It is admitted
only off previous images and for its first local entrywise antecedent.
"""
from functools import lru_cache
from itertools import combinations
import revision_local as base
from structural import tb


def comp(h,a,b):
    return tb.lt_p(h,a,b) or tb.lt_p(h,b,a)


def chain_insert(h,arm,label):
    if not all(comp(h,x,label) for x in arm):return None
    i=sum(tb.lt_p(h,x,label) for x in arm)
    out=arm[:i]+(label,)+arm[i:]
    return out if all(tb.lt_p(h,x,y) for x,y in zip(out,out[1:])) else None


def prescribed(h,source,level):
    shape=tuple(map(len,source))
    if level==1:
        if shape!=(3,1,1,1):return None
        u,label,w=source[0]
        tail=tuple(r[0] for r in source[1:]);i=0
        while i<len(tail) and tb.lt_p(h,tail[i],label):i+=1
        target=((u,w),)+tuple((x,) for x in tail[:i]+(label,)+tail[i:])
        tag='21111'
    elif level in (2,3):
        if shape!=(2,2,1,1):return None
        arm,pair,(c,),(d,)=source
        label=c if level==2 else d
        crossed=pair if level==2 else pair+(c,)
        if not all(comp(h,label,x) for x in crossed):return None
        newarm=chain_insert(h,arm,label)
        if newarm is None:return None
        target=(newarm,pair,(d if level==2 else c,));tag='321'
    elif level==4:
        if shape!=(2,2,1,1):return None
        arm,pair,(c,),(d,)=source
        for label in pair:
            arm=chain_insert(h,arm,label)
            if arm is None:return None
        target=(arm,(c,),(d,));tag='411'
    else:raise ValueError('unknown fixed layer')
    return (tag,target) if tb.validates(h,target) else None


@lru_cache(None)
def preimages(h,tag,target,level):
    expected={1:'21111',2:'321',3:'321',4:'411'}[level]
    if tag!=expected or inverse(h,tag,target,level-1) is not None:return ()
    result=[]
    if level==1:
        arm=target[0];leg=tuple(r[0] for r in target[1:])
        u,w=arm
        candidates=[((u,label,w),)+tuple((x,) for x in leg[:i]+leg[i+1:])
                    for i,label in enumerate(leg)]
    elif level in (2,3):
        arm,pair,(last,)=target
        candidates=[]
        for i,label in enumerate(arm):
            rest=arm[:i]+arm[i+1:]
            leg=(label,last) if level==2 else (last,label)
            candidates.append((rest,pair,(leg[0],),(leg[1],)))
    else:
        arm,(c,),(d,)=target
        candidates=[]
        for selected in combinations(range(4),2):
            top=tuple(x for i,x in enumerate(arm) if i in selected)
            pair=tuple(x for i,x in enumerate(arm) if i not in selected)
            candidates.append((top,pair,(c,),(d,)))
    for source in candidates:
        if (tb.validates(h,source) and forward(h,source,level-1) is None
                and prescribed(h,source,level)==(tag,target)):
            result.append(source)
    return tuple(result)


@lru_cache(None)
def forward(h,source,level=4):
    if level==0:return base.forward(h,source)
    previous=forward(h,source,level-1)
    if previous is not None:return previous
    out=prescribed(h,source,level)
    if out is None:return None
    antecedents=preimages(h,*out,level)
    return out if antecedents and antecedents[0]==source else None


@lru_cache(None)
def inverse(h,tag,target,level=4):
    if level==0:return base.inverse(h,tag,target)
    previous=inverse(h,tag,target,level-1)
    if previous is not None:return previous
    antecedents=preimages(h,tag,target,level)
    return antecedents[0] if antecedents else None
