"""RR003 direct gap<->cluster merge, after Kurşungöz's cluster endpoint.

A universal author argument is in endpoint-cluster-merge.md. This form has
not received separate semantic review and is not the missing KR1 bridge.
"""
import kr1


def pair(level):
    quotient,residue=divmod(level,2)
    return (3*quotient+1,3*quotient+2) if residue==0 else (3*quotient+3,)*2


def left_bound(level):
    quotient,residue=divmod(level,2)
    return 3*quotient-1+residue


def right_bound(level):
    quotient,residue=divmod(level,2)
    return 3*quotient+4+2*residue


def cluster_to_gap(c):
    if not isinstance(c,kr1.ClusterData):
        raise ValueError('expected literal ClusterData')
    i=j=0
    result=[]
    while i<c.a or j<c.b:
        single=c.mu[i]+3*j+2*i+1 if i<c.a else None
        level=c.nu[j]+2*j+i if j<c.b else None
        if j==c.b or (i<c.a and single<=left_bound(level+1)):
            result.append(single)
            i+=1
        else:
            result.extend(pair(level))
            j+=1
    return tuple(result)


def gap_to_cluster(parts):
    if not kr1.is_gap(parts):
        raise ValueError('expected actual ascending KR1 gap partition')
    i=j=position=0
    mu=[]
    nu=[]
    while position<len(parts):
        if position+1<len(parts) and parts[position+1]-parts[position]<=1:
            adjacent=parts[position:position+2]
            level=sum(adjacent)//3-1
            if tuple(adjacent)!=pair(level):
                raise AssertionError('literal close pair has unrecognized form')
            nu.append(level-2*j-i)
            j+=1
            position+=2
        else:
            mu.append(parts[position]-3*j-2*i-1)
            i+=1
            position+=1
    return kr1.ClusterData(i,j,tuple(mu),tuple(nu))
