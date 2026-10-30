#!/usr/bin/env python3
"""Exact finite checks for parity reflection and a prime-subset countermodel.
Requires Python 3 standard library. Does not prove any infinite statement.
"""
from math import isqrt
import platform
import sys

def factorize(n):
    factors=[]
    for p in range(2,isqrt(n)+1):
        while n%p==0:
            factors.append(p)
            n//=p
    if n>1: factors.append(n)
    return factors

def prime(n):
    return n >= 2 and len(factorize(n)) == 1

def floor_root(n,k):
    x = 0
    while (x+1)**k <= n: x += 1
    return x

def pair_counts(N, exponent_denominator, subset=None):
    z=floor_root(N,exponent_denominator)
    full={'PP':0,'PS':0,'SP':0,'SS':0}
    t=0
    for a in range(2,N-1):
        b=N-a
        fa,fb=factorize(a),factorize(b)
        if not fa or not fb or min(fa)<=z or min(fb)<=z: continue
        if subset is not None and any(p not in subset for p in fa+fb): continue
        if len(fa)>2 or len(fb)>2: continue
        ta='P' if len(fa)==1 else 'S'
        tb='P' if len(fb)==1 else 'S'
        full[ta+tb]+=1
        t+=(-1)**len(fa)
    return full,t

def main():
    checked=0
    for N in range(6,2001,2):
        d,t=pair_counts(N,3)
        assert t == d['SS']-d['PP'], (N,d,t)
        assert d['PS']==d['SP'], (N,d)
        checked+=1
    for k in range(1,(2000-8)//30+1):
        N=30*k+8
        assert not any(prime(p) and prime(N-p) and prime(N-p+2) for p in range(2,N-1)),N
    for N in (8,12):
        d,t=pair_counts(N,4)
        unordered_pp=(d['PP']+int(prime(N//2)) )//2
        fs=factorize(N//2)
        unordered_ss=(d['SS']+int(len(fs)==2 and min(fs)>floor_root(N,4)))//2
        assert unordered_pp==unordered_ss==1,(N,d)
    N=98
    prime_list={p for p in range(2,N) if prime(p)}
    reps=[(p,N-p) for p in sorted(prime_list) if N-p in prime_list]
    removed={max(p,q) for p,q in reps}
    model=prime_list-removed
    model_counts,t=pair_counts(N,3,model)
    assert 7 in model and model_counts['PP']==0 and model_counts['SS']>=1 and t>0
    print(f'Python {platform.python_version()}, platform {sys.platform}')
    print(f'cube-root reflection identity: {checked} even targets from 6 through 2000')
    print('adjacent-target progression 30k+8: exact checks through 2000 passed')
    print('quarter-root half-interval tie examples N=8 and N=12 passed')
    print('N=98: ordered prime pairs',reps)
    print('removed larger endpoints',sorted(removed))
    print('model counts',model_counts,'T_A=',t,'remaining semiprime square 49=7*7')
    print('These finite checks do not prove a statement for all N.')

if __name__ == '__main__': main()
