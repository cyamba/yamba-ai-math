"""Explicit bidegree-preserving local surgery; exhaustive finite sanity check only."""

def forward(a,b,c):
    if min(a,b,c)<0: raise ValueError('nonnegative multiplicities required')
    X,Y=a+2*c,b+c
    r=X%2
    p=max(0,(min(X,Y)-r)//2+1)
    if c<p:
        f=r+2*c
        return (0,Y-f,(X-f)//2,f,0)
    g=(X-1-Y)%2+2*(c-p)
    return (1,0,(X-1-Y-g)//2,Y-g,g)

def backward(tag, d, e, f, g):
    if min(d,e,f,g)<0 or tag not in (0,1): raise ValueError('invalid digits')
    if tag == 0:
        if g: raise ValueError('unmarked branch cannot contain 7')
        X=2*e+f; Y=d+f; c=(f-X%2)//2
    else:
        if d: raise ValueError('marked branch cannot contain 3')
        X=1+2*e+f+2*g; Y=f+g
        r=X%2; p=max(0,(min(X,Y)-r)//2+1)
        c=p+(g-(X-1-Y)%2)//2
    a=X-2*c; b=Y-c
    if min(a,b,c)<0 or forward(a,b,c)!=(tag,d,e,f,g): raise ValueError('invalid state')
    return a,b,c

if __name__=='__main__':
    checked=0
    for a in range(30):
      for b in range(30):
       for c in range(30):
        out=forward(a,b,c)
        assert min(out)>=0
        assert backward(*out)==(a,b,c)
        tag,d,e,f,g=out
        assert a+2*c==tag+2*e+f+2*g
        assert b+c==d+f+g
        checked+=1
    for tag in range(2):
     for d in range(10):
      for e in range(10):
       for f in range(10):
        for g in range(10):
         if (tag==0 and g!=0) or (tag==1 and d!=0): continue
         out=(tag,d,e,f,g)
         assert forward(*backward(*out))==out
    print('checked',checked,'source triples and both output branches with bounded coordinates')
