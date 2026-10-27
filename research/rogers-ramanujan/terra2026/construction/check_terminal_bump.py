"""Independent bounded semantic test of n=3 terminal bump, not a proof."""
from itertools import product
from collections import Counter


def forward(k, layer2, terminal):
    k1,k2,t=k
    assert 0<=k1<=k2<=t
    assert all(k2<=j<=t and col in (0,1) and v>0 for (j,col),v in layer2.items())
    assert all(j>=t and col in (0,1) and v>0 for (j,col),v in terminal.items())
    L=Counter(layer2); T=Counter(terminal)
    if T:
        j=max(j for j,col in T)
        col=max(col for jj,col in T if jj==j)
        T[j,col]-=1
        if not T[j,col]: del T[j,col]
        T[j+1,col]+=1
        return (k,L,T)
    return ((k1,k2,t+1),L,T)


def inverse(k,layer2,terminal):
    k1,k2,t=k
    L=Counter(layer2); T=Counter(terminal)
    if T:
        j=max(j for j,col in T)
        at=[(col,v) for (jj,col),v in T.items() if jj==j]
        if j<=t or sum(v for col,v in at)!=1: return None
        col=at[0][0]
        if col==0 and T.get((j-1,1),0)>0: return None
        T[j,col]-=1
        del T[j,col]
        T[j-1,col]+=1
        return (k,L,T)
    if t<=k2 or L.get((t,0),0) or L.get((t,1),0): return None
    return ((k1,k2,t-1),L,T)


def tup(s):
    k,L,T=s
    return (k,tuple(sorted(L.items())),tuple(sorted(T.items())))


def main():
    seen={}; count=0
    for k1 in range(3):
      for k2 in range(k1,3):
       for t in range(k2,3):
        lk=[(j,c) for j in range(k2,t+1) for c in (0,1)]
        tk=[(j,c) for j in range(t,t+3) for c in (0,1)]
        # Every binary occupation combination in the actual 2-layer finite window.
        for bits in product((0,1), repeat=len(lk)+len(tk)):
            L=Counter({x:v for x,v in zip(lk,bits[:len(lk)]) if v})
            T=Counter({x:v for x,v in zip(tk,bits[len(lk):]) if v})
            source=((k1,k2,t),L,T)
            target=forward(*source)
            assert tup(inverse(*target))==tup(source)
            key=tup(target)
            if key in seen: assert seen[key]==tup(source)
            seen[key]=tup(source)
            count+=1
    # Minimal obstruction when the inverse omits the color-tie test.
    bad=(((0,0,0)),Counter(),Counter({(1,0):1,(0,1):1}))
    assert inverse(*bad) is None
    print(f'{count} negative states: exact inverse, unique images; tie obstruction confirmed')

if __name__=='__main__':
    main()
