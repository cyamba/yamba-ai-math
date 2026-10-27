"""Separate critic's bounded checks; no imports from the author's implementation."""
from collections import Counter, defaultdict
from itertools import product
import json
import time


def partitions(n, maximum=None):
    if n == 0:
        yield ()
        return
    if maximum is None:
        maximum = n
    for head in range(min(n, maximum), 0, -1):
        for tail in partitions(n-head, head):
            yield (head,) + tail


def padded(n, length):
    for p in partitions(n):
        if len(p) <= length:
            yield p + (0,) * (length-len(p))


def gap(p):
    return (all(x > 0 for x in p)
            and all(x >= y for x, y in zip(p, p[1:]))
            and all(x-y > 1 or (x+y) % 3 == 0
                    for x, y in zip(p, p[1:]))
            and all(p[i]-p[i+2] >= 3 for i in range(len(p)-2)))


def compile_source(a, b, mu, m):
    result = [3*b + 2*(a-i)-1 + v for i, v in enumerate(mu)]
    for i, v in enumerate(m):
        j = b-i
        # Work directly from m parity, not author's helper functions.
        t = j + v//2
        result.extend((3*t, 3*t) if v % 2 else (3*t-1, 3*t-2))
    return tuple(result)


def inverse_separated(p):
    atoms = []
    i = 0
    while i < len(p):
        if i+1 < len(p) and p[i]-p[i+1] <= 1:
            atoms.append(('P', p[i:i+2]))
            i += 2
        else:
            atoms.append(('S', p[i]))
            i += 1
    word = ''.join(a[0] for a in atoms)
    if 'PS' in word:
        return None
    a = word.count('S')
    b = word.count('P')
    mu = tuple(atoms[i][1]-3*b-2*(a-i)+1 for i in range(a))
    m = tuple((sum(atoms[a+i][1])-6*(b-i)+3)//3 for i in range(b))
    return a, b, mu, m


def generating_coefficients(a, b, limit):
    base = a*a+3*a*b+3*b*b
    coeff = [0]*(limit+1)
    for eps in product((0,1), repeat=b):
        shift = base+3*sum((i+1)*v for i,v in enumerate(eps))
        shift += a*((3*sum(eps)+1)//2)
        if shift <= limit:
            coeff[shift] += 1
    for part in list(range(1,a+1)) + [6*i+3*a for i in range(1,b+1)]:
        for n in range(part,limit+1):
            coeff[n] += coeff[n-part]
    return coeff


def main():
    start = time.monotonic()
    limit = 36
    target_limit = 30
    source_counts = defaultdict(lambda: [0]*(limit+1))
    images = defaultdict(set)
    raw_seen = {}
    states = valid = 0
    first_bad = None
    for n in range(limit+1):
        for a in range(limit+1):
            for b in range(limit+1):
                base = a*a+3*a*b+3*b*b
                if base > n:
                    break
                for m_total in range((n-base)//3+1):
                    mu_total = n-base-3*m_total
                    for mu in padded(mu_total,a):
                        for m in padded(m_total,b):
                            states += 1
                            c = (a,b,mu,m)
                            p = compile_source(*c)
                            assert sum(p) == n and len(p) == a+2*b
                            assert p not in raw_seen, (c,raw_seen.get(p),p)
                            raw_seen[p] = c
                            admitted = not a or not b or mu[-1] >= (3*m[0]+1)//2
                            assert gap(p) == admitted, (c,p)
                            if admitted:
                                valid += 1
                                source_counts[(a,b)][n] += 1
                                assert inverse_separated(p) == c
                                images[n].add(p)
                            elif first_bad is None:
                                first_bad = {'weight':n, 'source':c, 'output':p}
    gap_count = separated_count = 0
    for n in range(target_limit+1):
        targets = set()
        for p in partitions(n):
            if gap(p):
                gap_count += 1
                c = inverse_separated(p)
                if c is not None:
                    separated_count += 1
                    assert compile_source(*c) == p
                    targets.add(p)
        assert targets == images[n], n
    sectors = 0
    for a in range(limit+1):
        for b in range(limit+1):
            if a*a+3*a*b+3*b*b > limit:
                break
            assert generating_coefficients(a,b,limit) == source_counts[(a,b)], (a,b)
            sectors += 1
    report = {'source_weight_bound':limit, 'target_weight_bound':target_limit,
              'source_states':states, 'valid_sources':valid,
              'gap_targets':gap_count, 'separated_targets':separated_count,
              'sector_generating_functions':sectors,
              'first_invalid':first_bad,
              'elapsed_seconds':time.monotonic()-start,
              'result':'all bounded checks pass; not a universal proof'}
    print(json.dumps(report,indent=2))


if __name__ == '__main__':
    main()
