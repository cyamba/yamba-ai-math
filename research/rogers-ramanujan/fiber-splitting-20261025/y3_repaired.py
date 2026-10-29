"""Third frozen variant: repair the refuted x=0 branch using six languages.

The earlier y3_extension.py is retained as a REFUTED discovery artifact.
This module must be evaluated on its own exact source and image domains.
"""
from collections import Counter
import candidates
from composed import y2_domain
import y3_extension as rejected_v2


def y3_forward(c):
    if not rejected_v2.y3_domain(c):
        raise ValueError('expected a4,b0,y3')
    if c.mu[0] >= 1:
        return rejected_v2.y3_forward(c)
    t, z = c.mu[1], c.mu[3]-c.mu[2]
    if t == 0 and z <= 1:
        n = {8:2, 6:1, 1:z}
    elif t == 0:
        n = {9:2, 6:1, 1:z-2}
    elif t == 1 and z == 0:
        n = {8:2, 6:1, 3:1}
    elif t == 1:
        n = {10:2, 3:2, 1:z-1}
    elif t == 2:
        n = {9:3, 1:z+1}
    else:
        n = {12:1, 9:2, 3:t-3, 1:z+1}
    return tuple(p for p in sorted(n,reverse=True) for _ in range(n[p]))


def y3_inverse(u):
    candidates.kr1.decode_columns(u)
    n, S = Counter(u), set(u)
    if S <= {8,6,3,1} and n[8] == 2 and n[6] == 1:
        if n[3] == 0 and n[1] <= 1:
            t, z = 0, n[1]
        elif n[3] == 1 and n[1] == 0:
            t, z = 1, 0
        else:
            raise ValueError('outside y3 uncarried small boundary')
    elif S <= {9,6,1} and n[9] == 2 and n[6] == 1:
        t, z = 0, n[1]+2
    elif S <= {10,3,1} and n[10] == n[3] == 2:
        t, z = 1, n[1]+1
    elif S <= {9,1} and n[9] == 3 and n[1] >= 1:
        t, z = 2, n[1]-1
    elif S <= {12,9,3,1} and n[12] == 1 and n[9] == 2 and n[1] >= 1:
        t, z = n[3]+3, n[1]-1
    else:
        source = rejected_v2.y3_inverse(u)
        if source.mu[0] == 0:
            raise ValueError('refuted x0 language is excluded')
        return source
    return candidates.kr1.ClusterData(4,0,(0,t,t+3,t+3+z),())


class ExtensionV3:
    def __init__(self, h3):
        self.h3 = h3

    def domain(self, c):
        return self.h3.domain(c) or y2_domain(c) or rejected_v2.y3_domain(c) or rejected_v2.funded_v2_domain(c)

    def forward(self, c):
        if self.h3.domain(c):
            return self.h3.forward(c)
        if y2_domain(c):
            return candidates.y2_forward(c)
        if rejected_v2.y3_domain(c):
            return y3_forward(c)
        if rejected_v2.funded_v2_domain(c):
            return candidates.middle_forward(c)
        raise self.h3.m.Outside('outside V3 restricted domain')

    def inverse(self, u):
        for operation in (candidates.y2_inverse, y3_inverse):
            try:
                return operation(u)
            except ValueError:
                pass
        try:
            source = candidates.middle_inverse(u)
            if not rejected_v2.funded_v2_domain(source):
                raise ValueError('alternate y2/y3 funded encodings excluded')
            return source
        except ValueError:
            return self.h3.inverse(u)
