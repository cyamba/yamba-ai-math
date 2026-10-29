"""Test local descent-staircase and multi-marker involution for C_n words."""
from itertools import combinations, product

def stair(word, delta):
    j=[]; prev=0
    for t,z in enumerate(word):
        descent=t>0 and word[t-1]=='b' and z=='a'
        cur=(j[-1] if j else 0)+delta[t]+int(descent)
        j.append(cur)
    return tuple(j)

def invert(word,j):
    return tuple(z-(j[t-1] if t else 0)-int(t>0 and word[t-1]=='b' and word[t]=='a') for t,z in enumerate(j))

def toggle(word,delta,marks):
    N=len(word); m=len(marks)
    for i in range(m):
        idx=N-(i+1)
        if marks[i] or delta[idx]:
            d=list(delta);b=list(marks)
            if b[i]: b[i]=0;d[idx]+=1
            else: b[i]=1;d[idx]-=1
            return tuple(d),tuple(b)
    return None

def weight(word,j,marks):
    n=word.count('|'); c=9*n+9; layer=0; total=9*sum(j)+9*sum((i+1)*b for i,b in enumerate(marks))
    for z in word:
        if z=='|':layer+=1
        else:
            r=3*n+4+3*layer
            total+=r if z=='a' else c-r
    return total

if __name__=='__main__':
  checks=0
  for n in (3,6):
    m=n//3
    for P in range(3):
      N=n+P
      for cuts in combinations(range(N),n):
       for colors in product('ab',repeat=P):
        it=iter(colors); word=tuple('|' if i in cuts else next(it) for i in range(N))
        for d in product(range(2),repeat=N):
         j=stair(word,d)
         assert invert(word,j)==d
         for b in product(range(2),repeat=m):
          v=toggle(word,d,b)
          if v is None:
           assert not any(b) and not any(d[N-m:])
          else:
           d2,b2=v
           assert toggle(word,d2,b2)==(d,b)
           assert weight(word,j,b)==weight(word,stair(word,d2),b2)
           assert sum(b)%2!=sum(b2)%2
          checks+=1
  print('word-staircase marker states checked:',checks)
