"""RR005 contextual six-strip. The residual root bijection remains absent."""
from dataclasses import dataclass
import rr005_chains as ch
from kr1 import ClusterData


def u_kind(u):
    if not ch.e_u(u):
        raise ValueError('not E_U')
    if 1 in u:
        return 'B'
    if 3 not in u:
        return 'A'
    return 'C1' if 10 in u else 'C0'


def replace(u, remove, insert):
    parts = list(u)
    for v in remove:
        parts.remove(v)
    return tuple(sorted(parts + list(insert), reverse=True))


def r6_u(u):
    kind = u_kind(u)
    if kind == 'A':
        return tuple(sorted(u + (6,), reverse=True))
    if kind == 'B':
        return replace(u,(9,1),(10,6))
    if kind == 'C0':
        return replace(u,(9,3),(12,6))
    return replace(u,(18,10,3),(19,12,6))


def l6_u(u):
    if not ch.e_u(u):
        raise ValueError('not E_U')
    if 1 in u or 3 in u or 6 not in u:
        return None
    base = replace(u,(6,),())
    if ch.literal_u(base):
        return base
    for kind, removed, inserted in (
            ('B',(10,),(9,1)),
            ('C0',(12,),(9,3)),
            ('C1',(19,12),(18,10,3))):
        try:
            candidate = replace(base,removed,inserted)
        except ValueError:
            continue
        if ch.e_u(candidate) and u_kind(candidate) == kind:
            return candidate
    return None


def r6_c(c):
    if not ch.e_c(c):
        raise ValueError('not E_C')
    if c.a == 0:
        if c.b == 0:
            return ClusterData(2,0,(1,1),())
        return ClusterData(0,c.b,(),c.nu[:-2]+tuple(v+1 for v in c.nu[-2:]))
    return ClusterData(c.a,c.b,c.mu[:-2]+tuple(v+3 for v in c.mu[-2:]),c.nu)


def l6_c(c):
    if not ch.e_c(c):
        raise ValueError('not E_C')
    if c == ClusterData(2,0,(1,1),()):
        return ClusterData(0,0,(),())
    if c.a == 0:
        if c.b >= 2 and c.nu[-2] > (c.nu[-3] if c.b > 2 else 0):
            return ClusterData(0,c.b,(),c.nu[:-2]+tuple(v-1 for v in c.nu[-2:]))
        return None
    gap = c.mu[-2]-(c.mu[-3] if c.a > 2 else 0)
    if gap >= (4 if c.a == 2 else 3):
        return ClusterData(c.a,c.b,c.mu[:-2]+tuple(v-3 for v in c.mu[-2:]),c.nu)
    return None


def f_u(u):
    return ch.e_u(u) and l6_u(u) is None


def f_c(c):
    return ch.e_c(c) and l6_c(c) is None


@dataclass(frozen=True)
class SixForm:
    root: object
    n1: int
    n3: int
    n6: int

    def __post_init__(self):
        if any(type(n) is not int or n < 0 for n in (self.n1,self.n3,self.n6)):
            raise ValueError('counts must be nonnegative integers')


def _split(form, lower):
    root = form.root
    n6 = 0
    while (previous := lower(root)) is not None:
        root = previous
        n6 += 1
    return SixForm(root,form.n1,form.n3,n6)


def split_u(u):
    return _split(ch.split_u(u),l6_u)


def split_c(c):
    return _split(ch.split_c(c),l6_c)


def _join(form, predicate, raise6, join):
    if not isinstance(form,SixForm) or not predicate(form.root):
        raise ValueError('not a normal form with an F root')
    value = form.root
    for _ in range(form.n6):
        value = raise6(value)
    return join(ch.NormalForm(value,form.n1,form.n3))


def join_u(form):
    return _join(form,f_u,r6_u,ch.join_u)


def join_c(form):
    return _join(form,f_c,r6_c,ch.join_c)


def partial_u_to_c(u):
    form = split_u(u)
    if form.root != ():
        raise ValueError('outside the empty-F-root restricted correspondence')
    return join_c(SixForm(ClusterData(0,0,(),()),form.n1,form.n3,form.n6))


def partial_c_to_u(c):
    form = split_c(c)
    if form.root != ClusterData(0,0,(),()):
        raise ValueError('outside the empty-F-root restricted correspondence')
    return join_u(SixForm((),form.n1,form.n3,form.n6))
