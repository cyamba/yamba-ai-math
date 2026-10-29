"""RR003 final AUTHOR-ONLY revision: explicit restricted maps for every a<=2.

The additional hole templates have not received separate critic review.
No accepted global bridge, full KR1 bijection or novelty claim is made.
Proof and recognition contract: ../rr003/round-2-revision.md.
"""
from collections import Counter
import kr1
import rr003_revision as reviewed

OutsideRestrictedDomain = reviewed.OutsideRestrictedDomain


def supported(c):
    return isinstance(c, kr1.ClusterData) and c.a <= 2


def _template(b, k):
    """(fixed counts, minimum ones, free delta mode). No object lookup."""
    if k == 4:
        if b == 1:
            return Counter({9:1,6:1,3:2}), 0, 'ordinary'
        if b == 2:
            return Counter({17:1,9:1,6:1,3:1}), 1, 'ordinary'
        counts=Counter({3*j:2 for j in range(1,b+1)})
        counts[3*(b-2)] += 1
        counts[17] += 1
        return counts, 1, 'ordinary'
    if k == 5:
        if b == 1:
            return Counter({10:1,6:2}), 1, 'parity'
        if b == 2:
            return Counter({19:1,12:1,6:1}), 1, 'ordinary'
        if b == 3:
            return Counter({19:1,12:1,9:1,6:2,3:2}), 1, 'ordinary'
        counts=Counter({3*j:2 for j in range(1,b+1)})
        counts[3*(b-2)] += 1
        counts[19] += 1
        return counts, 1, 'ordinary'
    if k == 9:
        if b == 1:
            return Counter({10:2,6:1}), 5, 'parity'
        if b == 2:
            return Counter({17:2,9:1,3:1}), 0, 'ordinary'
        if b <= 5:
            # This is used only for b=3,4,5. The marker exponent encodes b.
            return Counter({26:b-2,18:1,10:1,3:1}), {3:10,4:11,5:18}[b], 'ordinary'
        counts=Counter({3*j:2 for j in range(1,b+1)})
        counts[3*(b-2)] += 1
        counts[26] += 1
        return counts, 2, 'ordinary'
    raise ValueError('template only for b>0 and k in {4,5,9}')


def reconstruct_columns(c):
    if reviewed.supported(c):
        return reviewed.reconstruct_columns(c)
    if not supported(c):
        raise OutsideRestrictedDomain('unresolved global sectors a>=3')
    k,v=c.mu
    counts, minimum_ones, mode = _template(c.b,k)
    if mode == 'parity':
        quotient,residue=divmod(c.nu[0],2)
        counts[6] += quotient
        counts[3] += residue
    else:
        for j in range(1,c.b+1):
            counts[3*j] += c.nu[c.b-j] - (c.nu[c.b-j-1] if j < c.b else 0)
    counts[1] += minimum_ones+v-k
    return tuple(x for x in sorted(counts,reverse=True) for _ in range(counts[x]))


def _recognize_hole(counts):
    markers={x:m for x,m in counts.items() if x != 1 and x%3}
    if not markers:
        if counts[9] == 1 and counts[6] == 1 and counts[3] >= 2:
            return 1,4
    elif set(markers) == {10} and counts[3] <= 1:
        if markers[10] == 1:
            return 1,5
        if markers[10] == 2:
            return 1,9
    elif markers == {17:1}:
        multiples=[x for x in counts if x%3 == 0]
        if multiples:
            top=max(multiples)//3
            if top == 3 and counts[9] == 1:
                return 2,4
            if top >= 3:
                return top,4
    elif markers == {17:2}:
        return 2,9
    elif markers == {19:1}:
        multiples=[x for x in counts if x%3 == 0]
        if multiples:
            top=max(multiples)//3
            if top == 4 and counts[12] == 1:
                return (3 if counts[9] else 2),5
            if top >= 4:
                return top,5
    elif markers.get(10) == 1 and set(markers) == {10,26}:
        if 1 <= markers[26] <= 3:
            return markers[26]+2,9
    elif markers == {26:1}:
        multiples=[x for x in counts if x%3 == 0]
        if multiples:
            top=max(multiples)//3
            if top >= 6:
                return top,9
    raise OutsideRestrictedDomain('valid U outside author-only a<=2 image')


def decompose_columns(columns):
    try:
        return reviewed.decompose_columns(columns)
    except OutsideRestrictedDomain:
        pass
    counts=Counter(columns)  # Actual U validity was checked by reviewed inverse.
    b,k=_recognize_hole(counts)
    baseline, minimum_ones, mode = _template(b,k)
    ones=counts.pop(1,0)-minimum_ones
    if ones < 0:
        raise OutsideRestrictedDomain('missing minimum ones')
    for x,m in baseline.items():
        if counts[x] < m:
            raise OutsideRestrictedDomain('missing template part')
        counts[x] -= m
    counts=Counter({x:m for x,m in counts.items() if m})
    if mode == 'parity':
        if set(counts)-{3,6} or counts[3] > 1:
            raise OutsideRestrictedDomain('invalid parity remainder')
        nu=(2*counts[6]+counts[3],)
    else:
        if set(counts)-{3*j for j in range(1,b+1)}:
            raise OutsideRestrictedDomain('unrecognized extra column')
        total,values=0,[]
        for j in range(b,0,-1):
            total += counts[3*j]
            values.append(total)
        nu=tuple(values)
    return kr1.ClusterData(2,b,(k,k+ones),nu)


def raise_common_columns(columns):
    c=decompose_columns(columns)
    if c.a != 2:
        raise ValueError('common operation needs a=2')
    return reconstruct_columns(kr1.ClusterData(2,c.b,tuple(x+1 for x in c.mu),c.nu))


def lower_common_columns(columns):
    c=decompose_columns(columns)
    if c.a != 2 or c.mu[0] == 0:
        raise ValueError('inverse common operation needs a=2,mu[0]>0')
    return reconstruct_columns(kr1.ClusterData(2,c.b,tuple(x-1 for x in c.mu),c.nu))


def raise_nu_columns(columns,j):
    c=decompose_columns(columns)
    if type(j) is not int or not 1 <= j <= c.b:
        raise ValueError('nu suffix index needs 1<=j<=b')
    return reconstruct_columns(kr1.ClusterData(c.a,c.b,c.mu,
                               tuple(x+int(i>=c.b-j) for i,x in enumerate(c.nu))))
