"""RR005 intrinsic chain reductions, NOT a complete KR1 bijection.

No enumeration or saved transcript is used by these maps.
"""
from dataclasses import dataclass
from kr1 import ClusterData


def literal_u(u):
    if not isinstance(u, tuple) or any(type(v) is not int or v <= 0 for v in u):
        return False
    if any(x < y for x, y in zip(u, u[1:])):
        return False
    h = []
    residues = (0, 1, 3, 6, 8)
    for value in u:
        q, r = divmod(value, 9)
        if r not in residues:
            return False
        h.append(5*q + residues.index(r))
    return all(0 <= x-y <= 4 for x, y in zip(h, h[1:] + [0]))


def require_u(u):
    if not literal_u(u):
        raise ValueError('not literal U')


def d_u(u):
    return literal_u(u) and (1 not in u or (u.count(1) == 1 and len(u) > 1 and u[-2] == 9))


def d_c(c):
    return isinstance(c, ClusterData) and (c.a == 0 or
        (c.a == 2 and c.mu[0] == c.mu[1] and c.mu[0] >= 1) or
        (c.a >= 3 and c.mu[-2] == c.mu[-1]))


def r1_u(u):
    require_u(u)
    return u + (1,)


def l1_u(u):
    require_u(u)
    if u and u[-1] == 1 and literal_u(u[:-1]):
        return u[:-1]
    return None


def r1_c(c):
    if not isinstance(c, ClusterData):
        raise ValueError('not C')
    if c.a:
        return ClusterData(c.a, c.b, c.mu[:-1] + (c.mu[-1]+1,), c.nu)
    if not c.b:
        return ClusterData(1, 0, (0,), ())
    if c.nu[0]:
        return ClusterData(1, c.b, (0,), tuple(x-1 for x in c.nu))
    return ClusterData(2, c.b-1, (0, 0), c.nu[1:])


def l1_c(c):
    if not isinstance(c, ClusterData):
        raise ValueError('not C')
    if c.a and c.mu[-1] > (c.mu[-2] if c.a > 1 else 0):
        return ClusterData(c.a, c.b, c.mu[:-1] + (c.mu[-1]-1,), c.nu)
    if c.a == 1 and c.mu == (0,):
        return ClusterData(0, c.b, (), tuple(x+1 for x in c.nu))
    if c.a == 2 and c.mu == (0, 0):
        return ClusterData(0, c.b+1, (), (0,) + c.nu)
    return None


def r3_u(u):
    if not d_u(u):
        raise ValueError('not D_U')
    if 1 not in u:
        return tuple(sorted(u + (3,), reverse=True))
    parts = list(u)
    parts.remove(9)
    parts.remove(1)
    return tuple(sorted(parts + [10, 3], reverse=True))


def l3_u(u):
    if not d_u(u):
        raise ValueError('not D_U')
    if 1 in u or 3 not in u:
        return None
    parts = list(u)
    parts.remove(3)
    candidate = tuple(parts)
    if literal_u(candidate):
        return candidate
    if 10 not in parts:
        return None
    parts.remove(10)
    candidate = tuple(sorted(parts + [9, 1], reverse=True))
    return candidate if d_u(candidate) else None


def r3_c(c):
    if not d_c(c):
        raise ValueError('not D_C')
    if c.b:
        return ClusterData(c.a, c.b, c.mu, c.nu[:-1] + (c.nu[-1]+1,))
    if c.a == 0:
        return ClusterData(0, 1, (), (0,))
    if c.a == 2:
        return ClusterData(3, 0, (0, c.mu[0]-1, c.mu[0]-1), ())
    return ClusterData(c.a, 0, c.mu[:-3] + tuple(x+1 for x in c.mu[-3:]), ())


def l3_c(c):
    if not d_c(c):
        raise ValueError('not D_C')
    if c == ClusterData(0, 1, (), (0,)):
        return ClusterData(0, 0, (), ())
    if c.b:
        if c.nu[-1] > (c.nu[-2] if c.b > 1 else 0):
            return ClusterData(c.a, c.b, c.mu, c.nu[:-1] + (c.nu[-1]-1,))
        return None
    if c.a == 3 and c.mu[0] == 0:
        k = c.mu[1]+1
        return ClusterData(2, 0, (k, k), ())
    if c.a >= 3 and c.mu[-3] > (c.mu[-4] if c.a > 3 else 0):
        return ClusterData(c.a, 0, c.mu[:-3] + tuple(x-1 for x in c.mu[-3:]), ())
    return None


@dataclass(frozen=True)
class NormalForm:
    root: object
    n1: int
    n3: int

    def __post_init__(self):
        if any(type(n) is not int or n < 0 for n in (self.n1, self.n3)):
            raise ValueError('normal-form counts must be nonnegative integers')


def e_u(u):
    return d_u(u) and l3_u(u) is None


def e_c(c):
    return d_c(c) and l3_c(c) is None


def _split(value, lower1, lower3):
    n1 = n3 = 0
    while (previous := lower1(value)) is not None:
        value = previous
        n1 += 1
    while (previous := lower3(value)) is not None:
        value = previous
        n3 += 1
    return NormalForm(value, n1, n3)


def split_u(u):
    return _split(u, l1_u, l3_u)


def split_c(c):
    return _split(c, l1_c, l3_c)


def _join(form, predicate, raise1, raise3):
    if not isinstance(form, NormalForm) or not predicate(form.root):
        raise ValueError('not a normal form with an E root')
    value = form.root
    for _ in range(form.n3):
        value = raise3(value)
    for _ in range(form.n1):
        value = raise1(value)
    return value


def join_u(form):
    return _join(form, e_u, r1_u, r3_u)


def join_c(form):
    return _join(form, e_c, r1_c, r3_c)


def partial_u_to_c(u):
    form = split_u(u)
    if form.root == ():
        root = ClusterData(0, 0, (), ())
    elif form.root == (6,):
        root = ClusterData(2, 0, (1, 1), ())
    else:
        raise ValueError('outside the two-root restricted correspondence')
    return join_c(NormalForm(root, form.n1, form.n3))


def partial_c_to_u(c):
    form = split_c(c)
    if form.root == ClusterData(0, 0, (), ()):
        root = ()
    elif form.root == ClusterData(2, 0, (1, 1), ()):
        root = (6,)
    else:
        raise ValueError('outside the two-root restricted correspondence')
    return join_u(NormalForm(root, form.n1, form.n3))
