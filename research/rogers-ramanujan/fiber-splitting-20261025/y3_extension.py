"""Second frozen variant: whole y=3 slab, composed without alternate images."""
from collections import Counter
import candidates
from composed import y2_domain, funded_domain


def y3_domain(c):
    return c.a == 4 and c.b == 0 and c.mu[2] - c.mu[1] == 3


def y3_forward(c):
    if not y3_domain(c):
        raise ValueError('expected a4,b0,y3')
    x, t, z = c.mu[0], c.mu[1]-c.mu[0], c.mu[3]-c.mu[2]
    q, r = divmod(x, 2)
    if x == 0:
        n = {12:1, 6:1, 3:t+1, 1:z+1}
    elif x == 1:
        n = {12:1, 8:1, 6:1, 3:t, 1:z}
    elif r == 0:
        n = {10:1, 8:q, 6:2, 3:t, 1:z}
    else:
        n = {10:2, 8:q, 6:1, 3:t, 1:z}
    return tuple(p for p in sorted(n, reverse=True) for _ in range(n[p]))


def y3_inverse(u):
    candidates.kr1.decode_columns(u)
    n, S = Counter(u), set(u)
    if S <= {12,6,3,1} and n[12] == n[6] == 1 and n[3] >= 1 and n[1] >= 1:
        x, t, z = 0, n[3]-1, n[1]-1
    elif S <= {12,8,6,3,1} and n[12] == n[8] == n[6] == 1:
        x, t, z = 1, n[3], n[1]
    elif S <= {10,8,6,3,1} and n[8] >= 1 and (n[10],n[6]) in ((1,2),(2,1)):
        x, t, z = 2*n[8]+n[10]-1, n[3], n[1]
    else:
        raise ValueError('outside exact y3 image')
    return candidates.kr1.ClusterData(4,0,(x,x+t,x+t+3,x+t+3+z),())


def funded_v2_domain(c):
    return funded_domain(c) and c.mu[2]-c.mu[1] >= 4


class ExtensionV2:
    def __init__(self, h3):
        self.h3 = h3

    def domain(self, c):
        return self.h3.domain(c) or y2_domain(c) or y3_domain(c) or funded_v2_domain(c)

    def forward(self, c):
        if self.h3.domain(c):
            return self.h3.forward(c)
        if y2_domain(c):
            return candidates.y2_forward(c)
        if y3_domain(c):
            return y3_forward(c)
        if funded_v2_domain(c):
            return candidates.middle_forward(c)
        raise self.h3.m.Outside('outside V2 restricted domain')

    def inverse(self, u):
        for operation in (candidates.y2_inverse, y3_inverse):
            try:
                return operation(u)
            except ValueError:
                pass
        try:
            source = candidates.middle_inverse(u)
            if not funded_v2_domain(source):
                raise ValueError('alternate y2/y3 encoding excluded from V2')
            return source
        except ValueError:
            return self.h3.inverse(u)
