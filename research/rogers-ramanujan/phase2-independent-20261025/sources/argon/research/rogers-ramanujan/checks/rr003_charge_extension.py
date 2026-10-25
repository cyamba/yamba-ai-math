"""RR003 restricted extension: arbitrary ones with a separated ternary core.

Exact proof/domain: charge-separated-core.md. Author-only assurance, no
complete KR1 bijection. The earlier frozen small-charge map is retained.
"""
import kr1
import rr003_recursive as classical
import rr003_cluster_merge as clusters
import rr003_small_charge as small

OutsideRestrictedDomain=small.OutsideSmallCharge


def _core(parts):
    if not kr1.is_residue(parts) or any(x!=1 and x%3 for x in parts):
        raise OutsideRestrictedDomain('only ones and three-divisible residue parts are supported')
    t=parts.count(1)
    core=classical.glaisher_three(tuple(x for x in parts if x!=1))
    return t,clusters.gap_to_cluster(core)


def _separated(t,c):
    return t>=4 and (not c.mu or c.mu[0]>=t) and (not c.nu or c.nu[0]>=2)


def source_supported(parts):
    if small.source_supported(parts):
        return True
    try:
        t,c=_core(parts)
    except OutsideRestrictedDomain:
        return False
    return (t==3 and not c.a and not c.b) or _separated(t,c)


def residue_to_gap(parts):
    if small.source_supported(parts):
        return small.residue_to_gap(parts)
    t,c=_core(parts)
    if t==3 and not c.a and not c.b:
        return (1,2)
    if not _separated(t,c):
        raise OutsideRestrictedDomain('unresolved charge/core boundary: need t>=4, mu_min>=t and nu_min>=2')
    raised=kr1.ClusterData(c.a+2,c.b,(0,t-4)+tuple(x-4 for x in c.mu),tuple(x-2 for x in c.nu))
    return clusters.cluster_to_gap(raised)


def gap_to_residue(parts):
    try:
        return small.gap_to_residue(parts)
    except OutsideRestrictedDomain:
        pass
    if tuple(parts)==(1,2):
        return (1,1,1)
    c=clusters.gap_to_cluster(parts)
    if c.a<2 or c.mu[0]!=0:
        raise OutsideRestrictedDomain('no separated-core charge marker')
    t=c.mu[1]+4
    original=kr1.ClusterData(c.a-2,c.b,tuple(x+4 for x in c.mu[2:]),tuple(x+2 for x in c.nu))
    core=clusters.cluster_to_gap(original)
    if any(x%3 for x in core):
        raise OutsideRestrictedDomain('separated-core reconstruction is not three-divisible')
    return (1,)*t+classical.unglaisher_three(core)
