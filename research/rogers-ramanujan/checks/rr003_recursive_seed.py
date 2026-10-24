"""RR003 mechanism-B auxiliary seed injection, not a KR1 bijection.

Source: P3 residues 3,4,5,6 mod9, with non-three parts only 4,5.
Target: an intrinsically recognized subset of P2 residues 2,3,6,7 mod9.
Universal author proof in recursive-source-seed.md; no separate review.
"""

class OutsideSeedDomain(ValueError):
    pass


def _partition(parts,residues):
    return (isinstance(parts,(tuple,list)) and all(type(x) is int and x>0 and x%9 in residues for x in parts)
            and all(x<=y for x,y in zip(parts,parts[1:])))


def source_supported(parts):
    return _partition(parts,{3,4,5,6}) and all(x%3==0 or x in (4,5) for x in parts)


def target_supported(parts):
    if not _partition(parts,{2,3,6,7}) or any(x%3 and x not in (2,7) for x in parts):
        return False
    return parts.count(3)>=parts.count(7)+parts.count(2)%2


def inject(parts):
    if not source_supported(parts):
        raise OutsideSeedDomain('source requires P3 with only 4,5 as non-three parts')
    x,y=parts.count(4),parts.count(5)
    q,r=divmod(y,2)
    core=tuple(v for v in parts if v%3==0)
    return tuple(sorted(core+(2,)*(2*x+r)+(3,)*(q+r)+(7,)*q))


def recover(parts):
    if not target_supported(parts):
        raise OutsideSeedDomain('target lacks a recoverable seed branch')
    twos,q=parts.count(2),parts.count(7)
    r=twos%2
    x,y=(twos-r)//2,2*q+r
    core=list(v for v in parts if v%3==0)
    for _ in range(q+r):
        core.remove(3)
    return tuple(sorted(tuple(core)+(4,)*x+(5,)*y))
