"""RR003 explicit obstacle interpreter for the attributed Kurşungöz endpoint.

Candidate implementation, not a fresh universal endpoint proof. See the
frozen endpoint-clusters.md; a finite pass must not promote proof assurance.
"""
import kr1


class EndpointObstruction(ValueError):
    pass


def _pair(level):
    if level<0:
        raise EndpointObstruction('negative pair level')
    q,r=divmod(level,2)
    return (3*q+1,3*q+2) if r==0 else (3*q+3,3*q+3)


def _parts(atoms):
    return tuple(x for kind,label,level in atoms for x in ((level,) if kind=='s' else _pair(level)))


def _move(atoms,label,direction):
    work=list(atoms)
    index=next(i for i,(kind,name,value) in enumerate(work) if kind=='p' and name==label)
    kind,name,level=work[index]
    work[index]=(kind,name,level+direction)
    while not kr1.is_gap(_parts(work)):
        adjacent=index+direction
        if not 0<=adjacent<len(work) or work[adjacent][0]!='s':
            raise EndpointObstruction('pair obstacle is not a single cluster')
        single=work[adjacent]
        pair=work[index]
        moved_single=('s',single[1],single[2]-3*direction)
        moved_pair=('p',pair[1],pair[2]+direction)
        if direction==1:
            work[index:index+2]=[moved_single,moved_pair]
        else:
            work[index-1:index+1]=[moved_pair,moved_single]
        index=adjacent
    return work


def cluster_to_gap(c):
    if not isinstance(c,kr1.ClusterData):
        raise ValueError('expected literal ClusterData')
    atoms=[('p',j,2*j) for j in range(c.b)]
    atoms += [('s',j,3*c.b+2*j+1+c.mu[j]) for j in range(c.a)]
    for j in range(c.b-1,-1,-1):
        for _ in range(c.nu[j]):
            atoms=_move(atoms,j,1)
    return _parts(atoms)


def gap_to_cluster(parts):
    if not kr1.is_gap(parts):
        raise ValueError('expected actual ascending KR1 gap partition')
    atoms=[]
    i=a=b=0
    while i<len(parts):
        if i+1<len(parts) and parts[i+1]-parts[i]<=1:
            pair=(parts[i],parts[i+1])
            level=sum(pair)//3-1
            if _pair(level)!=pair:
                raise EndpointObstruction('unrecognized adjacent cluster')
            atoms.append(('p',b,level))
            b+=1
            i+=2
        else:
            atoms.append(('s',a,parts[i]))
            a+=1
            i+=1
    nu=[]
    for j in range(b):
        moves=0
        while True:
            level=next(value for kind,name,value in atoms if kind=='p' and name==j)
            if level==2*j:
                break
            if level<2*j:
                raise EndpointObstruction('backward move passed the required base pair')
            atoms=_move(atoms,j,-1)
            moves+=1
        nu.append(moves)
    if any(kind!='p' or name!=j for j,(kind,name,value) in enumerate(atoms[:b])):
        raise EndpointObstruction('backward pairs did not reach the initial base positions')
    singles=[value for kind,name,value in atoms if kind=='s']
    mu=tuple(value-(3*b+2*j+1) for j,value in enumerate(singles))
    return kr1.ClusterData(a,b,mu,tuple(nu))
