"""Bounded consistency checks, not a U-C bijection or universal proof."""
from pathlib import Path
import sys
from collections import Counter
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'checks'))
import kr1


def encode(u):
    kr1.decode_columns(u)
    if not u:
        return ()
    counts = Counter(kr1.inverse_prefix(x) for x in u)
    return tuple(tuple(counts[5*k+r] for r in range(1, 6))
                 for k in range((max(counts)+4)//5))


def decode(blocks):
    if any(len(b) != 5 or any(type(x) is not int or x < 0 for x in b) or not any(b) for b in blocks):
        raise ValueError('invalid block')
    def prefix(b):
        return next(i for i, x in enumerate(b) if x)
    def suffix(b):
        return next(i for i, x in enumerate(reversed(b)) if x)
    if blocks and (prefix(blocks[0]) > 3 or any(suffix(x)+prefix(y)>3 for x,y in zip(blocks, blocks[1:]))):
        raise ValueError('invalid boundary')
    result = tuple(sorted((kr1.prefix_weight(5*k+r) for k,b in enumerate(blocks)
                           for r,m in enumerate(b,1) for _ in range(m)), reverse=True))
    kr1.decode_columns(result)
    return result


def word_counts(N):
    # State z is the count of zeros after the most recently selected height
    # (or after height zero if none has yet been selected).
    dp = [[0]*(N+1) for _ in range(4)]
    dp[0][0] = 1
    total = [1]+[0]*N
    for h in range(1, 5*N+1):
        w=kr1.prefix_weight(h)
        if w>N:
            break
        ndp = [[0]*(N+1) for _ in range(4)]
        for z in range(4):
            for n,c in enumerate(dp[z]):
                if not c:
                    continue
                if z<3:
                    ndp[z+1][n] += c
                for new in range(n+w,N+1,w):
                    ndp[0][new] += c
        for n in range(1,N+1):
            total[n] += ndp[0][n]
        dp=ndp
    return total


def main():
    N=60
    lhs=word_counts(N)
    rhs=kr1.cluster_counts(N)
    assert lhs==rhs
    count=0
    for n in range(31):
        for p in kr1.weighted_partitions(n):
            u=kr1.weighted_columns(p)
            assert decode(encode(u))==u
            count+=1
    assert decode(((1,0,0,0,0),))==(1,)
    try:
        decode(((1,0,0,0,0),(0,0,0,0,1)))
    except ValueError:
        pass
    else:
        raise AssertionError('invalid block boundary accepted')
    print(f'coefficient agreement through {N}; {count} object round trips through 30')

if __name__=='__main__':
    main()
