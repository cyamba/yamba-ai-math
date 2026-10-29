"""Reversible residue-lane check and exact third-carry falsifiers."""
from collections import Counter
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'checks'))
import kr1


def encode(parts):
    if not kr1.is_residue(parts):
        raise ValueError('not B')
    out=[]
    for s,m in Counter(parts).items():
        if s%9 in (1,8):
            q,r=divmod(m,4)
            out.extend([s]*(r%2)+[2*s]*(r//2)+[4*s]*q)
        else:
            out.extend([s]*m)
    return tuple(sorted(out))


def decode(parts):
    if any(type(s) is not int or s<=0 for s in parts):
        raise ValueError('invalid part')
    out=[]
    for s,m in Counter(parts).items():
        r=s%9
        if r in (1,8):
            if m>1: raise ValueError('first lane multiplicity')
            out.extend([s]*m)
        elif r in (2,7):
            if s%2 or m>1: raise ValueError('second lane')
            out.extend([s//2]*(2*m))
        elif r in (4,5):
            if s%4: raise ValueError('third lane')
            out.extend([s//4]*(4*m))
        elif r in (3,6):
            out.extend([s]*m)
        else:
            raise ValueError('multiple of nine')
    return tuple(sorted(out))


def repair(parts, pair):
    # Replace pairs only in the third lane; every output is uncolored.
    out=[]
    for value,m in Counter(encode(parts)).items():
        if value%9 in (4,5):
            s=value//4
            q,r=divmod(m,2)
            out.extend([value]*r)
            for _ in range(q):
                out.extend(pair(s))
        else:
            out.extend([value]*m)
    return tuple(sorted(out))



def paired_swap(parts):
    counts=Counter(parts)
    pairs=set()
    for n in counts:
        r=8 if n%9 in (1,8) else 2
        root=n
        exponent=0
        while root%r==0:
            root//=r
            exponent+=1
        lower=root*r**(exponent-exponent%2)
        pairs.add((lower,r*lower,r))
    result=counts.copy()
    for lower,upper,r in pairs:
        q,d=divmod(counts[lower],r)
        result[lower]=r*counts[upper]+d
        result[upper]=q
    return tuple(sorted(k for k,m in result.items() for _ in range(m)))

def main():
    nstates=0
    for n in range(41):
        for b in kr1.residue_partitions(n):
            assert decode(encode(b))==b and sum(encode(b))==n
            assert paired_swap(paired_swap(b))==b and sum(paired_swap(b))==n
            nstates+=1
    examples=[((1,)*8,(8,),lambda s:(8*s,)),
              ((10,)*8,(10,35,35),lambda s:(s,7*s)),
              ((8,)*8,(10,10,10,10,24),lambda s:(3*s,5*s)),
              ((1,)*8,(1,1,6),lambda s:(2*s,6*s))]
    for x,y,f in examples:
        assert kr1.is_residue(x) and kr1.is_residue(y)
        assert repair(x,f)==repair(y,f)
        print(x,y,'->',repair(x,f))
    assert encode((1,)*8)==(4,4) and not kr1.is_gap((4,4))
    assert repair((1,)*10,lambda s:(3*s,5*s))==(2,3,5)
    assert not kr1.is_gap((2,3,5))
    print(f'{nstates} lane round trips through weight 40')

if __name__=='__main__':
    main()
