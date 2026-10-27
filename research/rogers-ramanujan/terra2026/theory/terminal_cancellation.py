"""Finite two-sided checks for q^9 marker cancellation in Xia C_n cut objects."""
from itertools import combinations_with_replacement, product

def encode(cut, cells, marked):
    return (tuple(cut), tuple(sorted((i,j,c,v) for (i,j,c),v in cells.items() if v)), marked)

def shift_negative(state):
    cut, raw, marked=state
    assert marked
    n=len(cut); cells={(i,j,c):v for i,j,c,v in raw}
    terminal=[(j,c) for (i,j,c),v in cells.items() if i==n and v]
    if terminal:
        j,c=max(terminal)
        cells[(n,j,c)]-=1
        cells[(n,j+1,c)]=cells.get((n,j+1,c),0)+1
    else:
        cut=cut[:-1]+(cut[-1]+1,)
    return encode(cut,cells,False)

def reverse_positive(state):
    cut,raw,marked=state
    assert not marked
    n=len(cut); cells={(i,j,c):v for i,j,c,v in raw}
    t=cut[-1]
    terminal=[(j,c,v) for (i,j,c),v in cells.items() if i==n and v]
    if terminal:
        j=max(j for j,c,v in terminal)
        top=[(c,v) for jj,c,v in terminal if jj==j]
        if j<=t or sum(v for c,v in top)!=1: return None
        c=top[0][0]
        if c==0 and cells.get((n,j-1,1),0): return None
        cells[(n,j,c)]-=1
        cells[(n,j-1,c)]=cells.get((n,j-1,c),0)+1
    else:
        if t<=cut[-2] or any(cells.get((n-1,t,c),0) for c in range(2)): return None
        cut=cut[:-1]+(t-1,)
    return encode(cut,cells,True)

def weight(state):
    cut,raw,marked=state; n=len(cut); c0=9*n+9
    val=9*sum(cut)+9*marked
    for i,j,c,v in raw:
        r=3*n+4+3*i
        val+=v*((r if c==0 else c0-r)+9*j)
    return val

if __name__=='__main__':
    n=3; count=0
    for cut in combinations_with_replacement(range(3),n):
        t=cut[-1]
        opts=[(n,j,c) for j in range(t,t+3) for c in range(2)]
        opts += [(n-1,t,c) for c in range(2)]
        for values in product(range(3),repeat=len(opts)):
            s=encode(cut,dict(zip(opts,values)),True)
            p=shift_negative(s)
            assert reverse_positive(p)==s
            assert weight(s)==weight(p)
            count+=1
    print('negative round trips checked:',count)
