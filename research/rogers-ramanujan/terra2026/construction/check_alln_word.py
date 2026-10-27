"""Independent finite test of root's all-n cut-word sign-reversing involution."""
from itertools import product


def eps(word):
    return tuple(int(i>0 and word[i-1]=='b' and x=='a') for i,x in enumerate(word))


def decode(word,delta):
    strict=eps(word); j=0; seq=[]
    for e,d in zip(strict,delta):
        j+=e+d
        seq.append(j)
    cuts=[]; layers=[[]]
    for symbol,j in zip(word,seq):
        if symbol=='|': cuts.append(j); layers.append([])
        else: layers[-1].append((j,symbol))
    return tuple(cuts),tuple(tuple(layer) for layer in layers)


def encode(cuts,layers):
    word=[]; indices=[]
    for i,layer in enumerate(layers):
        for j,color in sorted(layer):
            word.append(color); indices.append(j)
        if i<len(cuts):
            word.append('|'); indices.append(cuts[i])
    word=tuple(word); es=eps(word); old=0; delta=[]
    for e,j in zip(es,indices):
        delta.append(j-old-e); old=j
    assert min(delta,default=0)>=0
    return word,tuple(delta)


def weight(word,delta,marks,n):
    cuts,layers=decode(word,delta)
    base=9*sum(cuts)
    for i,layer in enumerate(layers):
        for j,c in layer:
            base+=9*j+(3*n+4+3*i if c=='a' else 6*n+5-3*i)
    return base+sum(9*h for h in marks)


def toggle(delta,marks,m):
    d=list(delta); marks=set(marks); N=len(d)
    for h in range(1,m+1):
        idx=N-h
        if h in marks:
            marks.remove(h); d[idx]+=1
            return tuple(d),frozenset(marks)
        if d[idx]:
            marks.add(h); d[idx]-=1
            return tuple(d),frozenset(marks)
    return None


def main():
    count=0
    for n in (3,4,6):
      m=n//3
      for N in range(n,n+3):
       for word in product(('|','a','b'),repeat=N):
        if word.count('|')!=n: continue
        for delta in product((0,1,2),repeat=N):
         assert encode(*decode(word,delta))==(word,delta)
         for mask in range(1<<m):
          marks=frozenset(h for h in range(1,m+1) if mask & (1<<(h-1)))
          out=toggle(delta,marks,m)
          if out is None:
            assert not marks and all(delta[N-h]==0 for h in range(1,m+1))
          else:
            newd,newmarks=out
            assert toggle(newd,newmarks,m)==(delta,marks)
            assert (len(marks)-len(newmarks))%2
            assert weight(word,delta,marks,n)==weight(word,newd,newmarks,n)
          count+=1
    print(f'{count} cut-word states: coordinate round-trip, weight, sign, inverse, survivors')

if __name__=='__main__':
    main()
