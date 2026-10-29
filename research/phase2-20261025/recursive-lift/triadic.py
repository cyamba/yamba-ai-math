"""Exact C-side grammar from RR007 R6; this is not a U/C bijection.

No enumeration is called by encode, decode, step, unstep, or tree_weight.
The independently enumerated grammar language is used only for verification.
"""
from dataclasses import dataclass
from functools import lru_cache
from itertools import product
from math import isqrt


@dataclass(frozen=True)
class C:
    a: int
    b: int
    mu: tuple
    nu: tuple

    def __post_init__(self):
        if type(self.a) is not int or type(self.b) is not int or min(self.a, self.b) < 0:
            raise ValueError('nonnegative integer dimensions required')
        for arm, size in ((self.mu, self.a), (self.nu, self.b)):
            if (not isinstance(arm, tuple) or len(arm) != size
                    or any(type(x) is not int or x < 0 for x in arm)
                    or any(x > y for x, y in zip(arm, arm[1:]))):
                raise ValueError('ascending exact-length nonnegative arms required')

    @property
    def weight(self):
        return self.a ** 2 + 3 * self.a * self.b + 3 * self.b ** 2 + sum(self.mu) + 3 * sum(self.nu)


EMPTY = C(0, 0, (), ())


@dataclass(frozen=True)
class Boundary:
    residue: int
    nonthree_gaps: tuple
    trits: tuple


@dataclass(frozen=True)
class Node:
    boundary: Boundary
    child: object  # Node or None; None is the unique (0,0) terminal.


def gaps(arm):
    previous = (0,) + arm[:-1]
    return tuple(reversed(tuple(x - y for x, y in zip(arm, previous))))


def arm_from_gaps(delta):
    out, current = [], 0
    for value in reversed(delta):
        current += value
        out.append(current)
    return tuple(out)


def step(source):
    """Nonrecursive exact digit division; terminal has no outgoing edge."""
    if not isinstance(source, C) or source == EMPTY:
        raise ValueError('nonterminal C required')
    c, residue = divmod(source.a, 3)
    delta = gaps(source.mu)
    nonthree = tuple(x for i, x in enumerate(delta, 1) if i % 3)
    quotient_trit = tuple(divmod(delta[3 * j - 1], 3) for j in range(1, c + 1))
    eta = arm_from_gaps(tuple(e for e, _ in quotient_trit))
    child = C(source.b, c, source.nu, eta)
    boundary = Boundary(residue, nonthree, tuple(t for _, t in quotient_trit))
    return boundary, child


def unstep(boundary, child):
    if not isinstance(boundary, Boundary) or not isinstance(child, C):
        raise ValueError('typed boundary and child C required')
    residue, nonthree, trits = boundary.residue, boundary.nonthree_gaps, boundary.trits
    if type(residue) is not int or not 0 <= residue < 3:
        raise ValueError('residue outside 0..2')
    a, b = 3 * child.b + residue, child.a
    if a == b == 0:
        raise ValueError('empty-above-empty node is forbidden')
    if (not isinstance(nonthree, tuple) or len(nonthree) != a - child.b
            or any(type(x) is not int or x < 0 for x in nonthree)
            or not isinstance(trits, tuple) or len(trits) != child.b
            or any(type(x) is not int or not 0 <= x < 3 for x in trits)):
        raise ValueError('incorrect gap count, trit count, or digit range')
    e = gaps(child.nu)
    boundary_iter = iter(nonthree)
    delta = tuple(3 * e[i // 3 - 1] + trits[i // 3 - 1]
                  if i % 3 == 0 else next(boundary_iter) for i in range(1, a + 1))
    return C(a, b, arm_from_gaps(delta), child.mu)


def residual_weight(boundary, child):
    parent = unstep(boundary, child)  # validates the intrinsic language.
    r, c, b = boundary.residue, child.b, child.a
    positions = tuple(i for i in range(1, parent.a + 1) if i % 3)
    return (r * r + 3 * r * (b + 2 * c)
            + sum(i * x for i, x in zip(positions, boundary.nonthree_gaps))
            + sum(3 * j * t for j, t in enumerate(boundary.trits, 1)))


def encode(source):
    if source == EMPTY:
        return None
    boundary, child = step(source)
    return Node(boundary, encode(child))


def decode(tree):
    if tree is None:
        return EMPTY
    if not isinstance(tree, Node):
        raise ValueError('Node or terminal required')
    return unstep(tree.boundary, decode(tree.child))


def tree_weight(tree):
    if tree is None:
        return 0
    child = decode(tree.child)
    return 3 * tree_weight(tree.child) + residual_weight(tree.boundary, child)


def depth(tree):
    return 0 if tree is None else 1 + depth(tree.child)


@lru_cache(None)
def ascending_arms(length, total, minimum=0):
    """Direct C enumerator used only by verification, not by either map."""
    if not length:
        return ((),) if total == 0 else ()
    return tuple((first,) + tail for first in range(minimum, total // length + 1)
                 for tail in ascending_arms(length - 1, total - first, first))


def c_exact(weight):
    for a in range(isqrt(weight) + 1):
        for b in range(isqrt(weight // 3) + 1):
            remaining = weight - a * a - 3 * a * b - 3 * b * b
            if remaining < 0:
                continue
            for nu_sum in range(remaining // 3 + 1):
                for mu in ascending_arms(a, remaining - 3 * nu_sum):
                    for nu in ascending_arms(b, nu_sum):
                        yield C(a, b, mu, nu)


def bounded_gaps(costs, remaining):
    """Enumerate a weighted independent boundary composition exactly."""
    if not costs:
        if not remaining:
            yield ()
        return
    first, *rest = costs
    for value in range(remaining // first + 1):
        for tail in bounded_gaps(rest, remaining - first * value):
            yield (value,) + tail


@lru_cache(None)
def grammar_exact(weight):
    """Independent recursive language generator, not encode(c_exact)."""
    if weight == 0:
        return (None,)
    answer = []
    for child_weight in range(weight // 3 + 1):
        for child_tree in grammar_exact(child_weight):
            child = decode(child_tree)
            b, c = child.a, child.b
            for r in range(3):
                a = 3 * c + r
                if a == b == 0:
                    continue
                base = 3 * child_weight + r * r + 3 * r * (b + 2 * c)
                if base > weight:
                    continue
                positions = tuple(i for i in range(1, a + 1) if i % 3)
                for trits in product(range(3), repeat=c):
                    remaining = weight - base - sum(3 * j * t for j, t in enumerate(trits, 1))
                    if remaining < 0:
                        continue
                    for delta in bounded_gaps(positions, remaining):
                        answer.append(Node(Boundary(r, delta, trits), child_tree))
    return tuple(answer)
