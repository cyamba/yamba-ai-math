"""RR003 repaired restricted recursive construction, author-only assurance.

Exactly zero, one or two copies of part 1, plus arbitrary residue parts
that are divisible by three. Uses classical Glaisher and the explicit
cluster endpoint; not a complete KR1 bijection or a novel endpoint claim.
"""
import kr1
import rr003_recursive as recursive
import rr003_cluster_merge as clusters


class OutsideSmallCharge(ValueError):
    pass


def source_supported(parts):
    return (kr1.is_residue(parts) and parts.count(1)<=2
            and all(x==1 or x%3==0 for x in parts))


def residue_to_gap(parts):
    if not source_supported(parts):
        raise OutsideSmallCharge('restricted source requires at most two ones and all other parts divisible by three')
    t=parts.count(1)
    core=recursive.glaisher_three(tuple(x for x in parts if x!=1))
    if t==0:
        return core
    c=clusters.gap_to_cluster(core)
    if c.a:
        c=kr1.ClusterData(c.a,c.b,c.mu[:-1]+(c.mu[-1]+t,),c.nu)
    else:
        c=kr1.ClusterData(1,c.b,(t-1,),tuple(x-1 for x in c.nu))
    return clusters.cluster_to_gap(c)


def gap_to_residue(parts):
    if not kr1.is_gap(parts):
        raise ValueError('expected actual ascending KR1 gap partition')
    if all(x%3==0 for x in parts):
        return recursive.unglaisher_three(parts)
    c=clusters.gap_to_cluster(parts)
    if c.a==1 and c.mu[0] in (0,1):
        t=c.mu[0]+1
        lowered=kr1.ClusterData(0,c.b,(),tuple(x+1 for x in c.nu))
    elif c.a:
        t=(c.mu[-1]-c.a-1)%3
        if t not in (1,2):
            raise OutsideSmallCharge('last single has the wrong recovered residue')
        mu=c.mu[:-1]+(c.mu[-1]-t,)
        try:
            lowered=kr1.ClusterData(c.a,c.b,mu,c.nu)
        except ValueError as exc:
            raise OutsideSmallCharge('last mu cannot be lowered intrinsically') from exc
    else:
        raise OutsideSmallCharge('no recoverable single charge')
    core=clusters.cluster_to_gap(lowered)
    if any(x%3 for x in core):
        raise OutsideSmallCharge('recovered core is outside the classical three-divisible sector')
    return (1,)*t+recursive.unglaisher_three(core)
