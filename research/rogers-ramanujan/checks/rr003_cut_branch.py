"""RR003 intrinsic first recursive branch K[-2] <-> a subset of P3.

Universal author argument in cut-branch.md; no separate semantic review.
This is a partial branch, not the complete KR1 bijection.
"""
from collections import Counter
import rr003_product_involution as products


class OutsideBranch(ValueError):
    pass


def _p3(parts):
    return (isinstance(parts,(tuple,list)) and all(type(x) is int and x>0 and x%9 in (3,4,5,6) for x in parts)
            and all(x<=y for x,y in zip(parts,parts[1:])))


def cut_to_p3(cut):
    if not products.is_cut(cut):
        raise ValueError('expected actual K cut')
    result=[3]*(3*cut.j)
    for x in cut.parts:
        if x%9==7:
            result.extend((x-3,3))
        elif x%9==2:
            result.extend((x-6,6))
        else:
            result.append(x)
    return tuple(sorted(result))


def p3_to_cut(parts):
    if not _p3(parts):
        raise ValueError('expected actual P3 residue partition')
    counts=Counter(parts)
    threes,sixes=counts[3],counts[6]
    j=lower_fours=0
    while True:
        lower=3*j+lower_fours
        if threes<lower:
            raise OutsideBranch('three-count lies in an interval gap')
        top=lower+counts[9*j+4]
        if threes<=top:
            break
        lower_fours+=counts[9*j+4]
        j+=1
    split=threes-lower
    lower_fives=sum(count for value,count in counts.items() if value%9==5 and value//9<j)
    if sixes<lower_fives:
        raise OutsideBranch('insufficient sixes to recover the lower five rows')
    result=[]
    for x in parts:
        if x==3:
            continue
        if x==6 and lower_fives:
            lower_fives-=1
            continue
        if x%9==4 and x//9<j:
            result.append(x+3)
        elif x==9*j+4 and split:
            result.append(x+3)
            split-=1
        elif x%9==5 and x//9<j:
            result.append(x+6)
        else:
            result.append(x)
    cut=products.Cut(j,tuple(sorted(result)))
    if not products.is_cut(cut):
        raise AssertionError('intrinsic branch reconstruction violated cut domain')
    return cut
