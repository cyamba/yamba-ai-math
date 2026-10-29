"""Frozen third-slab candidate; final scope determined by separate review."""
from collections import Counter
import candidates as c
import y3_repaired as v3


def y4_domain(source):
    return source.a == 4 and source.b == 0 and source.mu[2]-source.mu[1] == 4


def y4_forward(source):
    if not y4_domain(source):
        raise ValueError('expected a4,b0,y4')
    x,t,z = source.mu[0],source.mu[1]-source.mu[0],source.mu[3]-source.mu[2]
    q,r = divmod(x,2)
    if x == 0:
        if t == 0 and z == 0:
            n = {12:1,9:1,3:1}
        elif t == 0:
            n = {9:1,8:2,1:z-1}
        elif t == 1:
            n = {10:1,9:1,8:1,1:z}
        elif t == 2:
            n = {12:1,10:1,8:1,1:z}
        elif t == 3:
            n = {10:3,3:1,1:z}
        else:
            n = {12:1,9:2,6:1,3:t-4,1:z}
    elif x == 1:
        n = {12:1,10:1,6:1,3:t,1:z}
    elif r == 0:
        if t <= 2:
            n = {10:2,8:q,3:t,1:z+4}
        elif t == 3:
            n = {10:3,8:q,1:z+3}
        else:
            n = {10:2,8:q,6:2,3:t-4,1:z+4}
    elif t == 0:
        n = {10:1,9:2,8:q,1:z}
    elif t == 1:
        n = {10:2,9:1,8:q,1:z+2}
    elif t == 2:
        n = {10:3,8:q,3:1,1:z+1}
    else:
        n = {10:3,8:q,6:1,3:t-3,1:z+1}
    return tuple(p for p in sorted(n,reverse=True) for _ in range(n[p]))


def y4_inverse(u):
    c.kr1.decode_columns(u)
    n,S = Counter(u),set(u)
    if u == (12,9,3):
        x,t,z = 0,0,0
    elif S <= {9,8,1} and n[9] == 1 and n[8] == 2:
        x,t,z = 0,0,n[1]+1
    elif S <= {10,9,8,1} and n[10] == n[9] == n[8] == 1:
        x,t,z = 0,1,n[1]
    elif S <= {12,10,8,1} and n[12] == n[10] == n[8] == 1:
        x,t,z = 0,2,n[1]
    elif S <= {10,3,1} and n[10] == 3 and n[3] == 1:
        x,t,z = 0,3,n[1]
    elif S <= {12,9,6,3,1} and n[12] == n[6] == 1 and n[9] == 2:
        x,t,z = 0,n[3]+4,n[1]
    elif S <= {12,10,6,3,1} and n[12] == n[10] == n[6] == 1:
        x,t,z = 1,n[3],n[1]
    elif S <= {10,8,3,1} and n[10] == 2 and n[8] >= 1 and n[3] <= 2 and n[1] >= 4:
        x,t,z = 2*n[8],n[3],n[1]-4
    elif S <= {10,8,1} and n[10] == 3 and n[8] >= 1 and n[1] >= 3:
        x,t,z = 2*n[8],3,n[1]-3
    elif S <= {10,8,6,3,1} and n[10] == n[6] == 2 and n[8] >= 1 and n[1] >= 4:
        x,t,z = 2*n[8],n[3]+4,n[1]-4
    elif S <= {10,9,8,1} and n[10] == 1 and n[9] == 2 and n[8] >= 1:
        x,t,z = 2*n[8]+1,0,n[1]
    elif S <= {10,9,8,1} and n[10] == 2 and n[9] == 1 and n[8] >= 1 and n[1] >= 2:
        x,t,z = 2*n[8]+1,1,n[1]-2
    elif S <= {10,8,3,1} and n[10] == 3 and n[8] >= 1 and n[3] == 1 and n[1] >= 1:
        x,t,z = 2*n[8]+1,2,n[1]-1
    elif S <= {10,8,6,3,1} and n[10] == 3 and n[6] == 1 and n[8] >= 1 and n[1] >= 1:
        x,t,z = 2*n[8]+1,n[3]+3,n[1]-1
    else:
        raise ValueError('outside exact y4 image')
    return c.kr1.ClusterData(4,0,(x,x+t,x+t+4,x+t+4+z),())


def funded_final(source):
    return v3.rejected_v2.funded_v2_domain(source) and source.mu[2]-source.mu[1] >= 5


class ExtensionV4:
    def __init__(self,h3):
        self.h3 = h3

    def domain(self,source):
        return (self.h3.domain(source) or v3.y2_domain(source) or
                v3.rejected_v2.y3_domain(source) or y4_domain(source) or funded_final(source))

    def forward(self,source):
        if self.h3.domain(source):
            return self.h3.forward(source)
        if v3.y2_domain(source):
            return c.y2_forward(source)
        if v3.rejected_v2.y3_domain(source):
            return v3.y3_forward(source)
        if y4_domain(source):
            return y4_forward(source)
        if funded_final(source):
            return c.middle_forward(source)
        raise self.h3.m.Outside('outside V4 restricted domain')

    def inverse(self,u):
        for inverse in (c.y2_inverse,v3.y3_inverse,y4_inverse):
            try:
                return inverse(u)
            except ValueError:
                pass
        try:
            source = c.middle_inverse(u)
            if not funded_final(source):
                raise ValueError('alternate funded y2/y3/y4 images excluded')
            return source
        except ValueError:
            return self.h3.inverse(u)
