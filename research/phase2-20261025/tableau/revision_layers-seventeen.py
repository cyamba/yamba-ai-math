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


def leg_insert(h,leg,label):
    i=0
    while i<len(leg) and tb.lt_p(h,leg[i],label):i+=1
    return leg[:i]+(label,)+leg[i:]


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
    elif level==5:
        if shape!=(2,2,1,1):return None
        labels=source[0]+source[1]
        chain=tuple(sorted(labels,key=lambda x:sum(tb.lt_p(h,y,x) for y in labels)))
        if not all(tb.lt_p(h,x,y) for x,y in zip(chain,chain[1:])):return None
        leg=(source[2][0],source[3][0])
        for label in reversed(chain[1:-1]):leg=leg_insert(h,leg,label)
        target=((chain[0],chain[-1]),)+tuple((x,) for x in leg);tag='21111'
    elif level in (6,7,8):
        if shape!=(2,2,1,1):return None
        (u,v),(a,b),(c,),(d,)=source
        if level==6:
            if not tb.lt_p(h,v,b):return None
            endpoint=b;leg=leg_insert(h,(a,c,d),v)
        else:
            endpoint=c if level==7 else d
            crossed=(u,v,a,b) if level==7 else (u,v,a,b,c)
            if not tb.lt_p(h,u,endpoint) or not all(comp(h,endpoint,x) for x in crossed):return None
            leg=(a,d if level==7 else c)
            leg=leg_insert(h,leg,b)
            leg=leg_insert(h,leg,v)
        target=((u,endpoint),)+tuple((x,) for x in leg);tag='21111'
    elif level==9:
        if shape!=(2,2,1,1):return None
        (u,v),(a,b),(c,),(d,)=source
        if not (tb.lt_p(h,v,b) and tb.lt_p(h,a,d) and tb.lt_p(h,c,d)):return None
        target=((u,v,b),(a,d),(c,));tag='321'
    elif level==10:
        if shape!=(2,2,1,1):return None
        (u,v),(a,b),(c,),(d,)=source
        if not (v<b and not comp(h,v,b) and tb.lt_p(h,u,b)):return None
        leg=(a,c,d);i=0
        while i<len(leg) and tb.lt_p(h,leg[i],v):i+=1
        if i==len(leg) or comp(h,leg[i],v) or not leg[i]<v:return None
        i+=1
        while i<len(leg) and tb.lt_p(h,leg[i],v):i+=1
        leg=leg[:i]+(v,)+leg[i:]
        target=((u,b),)+tuple((x,) for x in leg);tag='21111'
    elif level==11:
        if shape!=(2,2,1,1):return None
        (u,v),(a,b),(c,),(d,)=source
        if not (tb.lt_p(h,v,b) and tb.lt_p(h,a,d) and tb.lt_p(h,c,d)):return None
        arm=chain_insert(h,(u,v,b),d)
        if arm is None:return None
        target=(arm,(a,),(c,));tag='411'
    elif level==12:
        if shape!=(2,2,1,1):return None
        (u,v),(a,b),(c,),(d,)=source
        if not (tb.lt_p(h,u,a) and comp(h,v,a)):return None
        leg=leg_insert(h,(c,d),b)
        leg=leg_insert(h,leg,v)
        target=((u,a),)+tuple((x,) for x in leg);tag='21111'
    elif level==13:
        if shape!=(2,2,1,1):return None
        (u,v),(a,b),(c,),(d,)=source
        if not (tb.lt_p(h,v,b) and tb.lt_p(h,a,c)):return None
        arm=chain_insert(h,(u,v,b),c)
        if arm is None:return None
        target=(arm,(a,),(d,));tag='411'
    elif level==14:
        if shape!=(2,2,1,1):return None
        (u,v),(a,b),(c,),(d,)=source
        if not (tb.lt_p(h,u,a) and tb.lt_p(h,c,d) and all(comp(h,v,x) for x in (a,b,d))):return None
        arm=chain_insert(h,(u,a,b),d)
        if arm is None:return None
        target=(arm,(v,),(c,));tag='411'
    elif level==15:
        if shape!=(2,2,1,1):return None
        (u,v),(a,b),(c,),(d,)=source
        if not (tb.lt_p(h,u,a) and tb.lt_p(h,v,d) and tb.lt_p(h,c,d)
                and comp(h,v,a) and comp(h,v,b)):return None
        target=((u,a,b),(v,d),(c,));tag='321'
    elif level==16:
        if shape!=(2,2,1,1):return None
        (u,v),(a,b),(c,),(d,)=source
        if not (tb.lt_p(h,u,a) and tb.lt_p(h,a,v) and tb.lt_p(h,c,b)):return None
        target=((u,a,v),(c,b),(d,));tag='321'
    elif level==17:
        if shape!=(2,2,1,1):return None
        (u,v),(a,b),(c,),(d,)=source
        delta=sum((1 if y>x else -1) for x,y in ((a,c),(v,b),(v,c)) if not comp(h,x,y))
        if delta:return None
        target=((u,c,b),(a,v),(d,));tag='321'
    else:raise ValueError('unknown fixed layer')
    return (tag,target) if tb.validates(h,target) else None


@lru_cache(None)
def preimages(h,tag,target,level):
    expected={1:'21111',2:'321',3:'321',4:'411',5:'21111',6:'21111',7:'21111',8:'21111',9:'321',10:'21111',11:'411',12:'21111',13:'411',14:'411',15:'321',16:'321',17:'321'}[level]
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
    elif level==4:
        arm,(c,),(d,)=target
        candidates=[]
        for selected in combinations(range(4),2):
            top=tuple(x for i,x in enumerate(arm) if i in selected)
            pair=tuple(x for i,x in enumerate(arm) if i not in selected)
            candidates.append((top,pair,(c,),(d,)))
    elif level==5:
        arm=target[0];leg=tuple(r[0] for r in target[1:]);candidates=[]
        for picked in combinations(range(4),2):
            middles=tuple(leg[i] for i in picked)
            chain=arm[:1]+middles+arm[1:]
            if not all(tb.lt_p(h,x,y) for x,y in zip(chain,chain[1:])):continue
            other=tuple(leg[i] for i in range(4) if i not in picked)
            for top_slots in combinations(range(4),2):
                top=tuple(x for i,x in enumerate(chain) if i in top_slots)
                pair=tuple(x for i,x in enumerate(chain) if i not in top_slots)
                candidates.append((top,pair,(other[0],),(other[1],)))
    elif level in (6,10):
        (u,b)=target[0];leg=tuple(r[0] for r in target[1:]);candidates=[]
        for i,v in enumerate(leg):
            a,c,d=leg[:i]+leg[i+1:]
            candidates.append(((u,v),(a,b),(c,),(d,)))
    elif level in (7,8):
        (u,endpoint)=target[0];leg=tuple(r[0] for r in target[1:]);candidates=[]
        for i,v in enumerate(leg):
            for j,b in enumerate(leg):
                if i==j:continue
                a,other=tuple(x for k,x in enumerate(leg) if k not in (i,j))
                c,d=(endpoint,other) if level==7 else (other,endpoint)
                candidates.append(((u,v),(a,b),(c,),(d,)))
    elif level==9:
        (u,v,b),(a,d),(c,)=target
        candidates=[((u,v),(a,b),(c,),(d,))]
    elif level==11:
        arm,(a,),(c,)=target;candidates=[]
        for i,d in enumerate(arm):
            u,v,b=arm[:i]+arm[i+1:]
            candidates.append(((u,v),(a,b),(c,),(d,)))
    elif level==13:
        arm,(a,),(d,)=target;candidates=[]
        for i,c in enumerate(arm):
            u,v,b=arm[:i]+arm[i+1:]
            candidates.append(((u,v),(a,b),(c,),(d,)))
    elif level==14:
        arm,(v,),(c,)=target;candidates=[]
        for i,d in enumerate(arm):
            u,a,b=arm[:i]+arm[i+1:]
            candidates.append(((u,v),(a,b),(c,),(d,)))
    elif level==15:
        (u,a,b),(v,d),(c,)=target
        candidates=[((u,v),(a,b),(c,),(d,))]
    elif level==16:
        (u,a,v),(c,b),(d,)=target
        candidates=[((u,v),(a,b),(c,),(d,))]
    elif level==17:
        (u,c,b),(a,v),(d,)=target
        candidates=[((u,v),(a,b),(c,),(d,))]
    else:
        (u,a)=target[0];leg=tuple(r[0] for r in target[1:]);candidates=[]
        for i,v in enumerate(leg):
            for j,b in enumerate(leg):
                if i==j:continue
                c,d=tuple(x for k,x in enumerate(leg) if k not in (i,j))
                candidates.append(((u,v),(a,b),(c,),(d,)))
    for source in candidates:
        if (tb.validates(h,source) and forward(h,source,level-1) is None
                and prescribed(h,source,level)==(tag,target)):
            result.append(source)
    return tuple(result)


@lru_cache(None)
def forward(h,source,level=17):
    if level==0:return base.forward(h,source)
    previous=forward(h,source,level-1)
    if previous is not None:return previous
    out=prescribed(h,source,level)
    if out is None:return None
    antecedents=preimages(h,*out,level)
    return out if antecedents and antecedents[0]==source else None


@lru_cache(None)
def inverse(h,tag,target,level=17):
    if level==0:return base.inverse(h,tag,target)
    previous=inverse(h,tag,target,level-1)
    if previous is not None:return previous
    antecedents=preimages(h,tag,target,level)
    return antecedents[0] if antecedents else None
