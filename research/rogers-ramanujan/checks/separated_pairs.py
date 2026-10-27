"""Exact safe image of the supplied unfinished KR1 pair compiler.

Descending tuples throughout; m is nu/3 from the supplied note. This is a
restricted cluster-to-gap endpoint, not a residue-to-gap KR1 bijection.
Written arguments: ../separated-2026-10-27/proof.md. No lookup/ranking is used.
"""

from dataclasses import dataclass


def _natural(value):
    return type(value) is int and value >= 0


def _decreasing_naturals(values, length):
    return (isinstance(values, tuple) and len(values) == length
            and all(_natural(x) for x in values)
            and all(x >= y for x, y in zip(values, values[1:])))


def quadratic(a, b):
    return a*a + 3*a*b + 3*b*b


@dataclass(frozen=True)
class SeparatedCluster:
    a: int
    b: int
    mu: tuple[int, ...]
    m: tuple[int, ...]

    def __post_init__(self):
        if not (_natural(self.a) and _natural(self.b)
                and _decreasing_naturals(self.mu, self.a)
                and _decreasing_naturals(self.m, self.b)):
            raise ValueError('expected descending exact-length natural coordinates')

    @property
    def weight(self):
        return quadratic(self.a, self.b) + sum(self.mu) + 3*sum(self.m)

    @property
    def dimension(self):
        return self.a + 2*self.b

    @property
    def admitted(self):
        return (self.a == 0 or self.b == 0
                or self.mu[-1] >= (3*self.m[0]+1)//2)


def is_gap(parts):
    """Literal descending KR1 predicates, including the empty tuple."""
    return (isinstance(parts, tuple)
            and all(type(p) is int and p > 0 for p in parts)
            and all(x >= y for x, y in zip(parts, parts[1:]))
            and all(x-y > 1 or (x+y) % 3 == 0
                    for x, y in zip(parts, parts[1:]))
            and all(parts[i]-parts[i+2] >= 3 for i in range(len(parts)-2)))


def literal_compile(cluster):
    """The supplied formula, with inert carry/pass removed; may return INVALID gaps."""
    if not isinstance(cluster, SeparatedCluster):
        raise ValueError('expected SeparatedCluster')
    a, b = cluster.a, cluster.b
    result = [3*b+2*(a-i)-1+mu for i, mu in enumerate(cluster.mu)]
    for i, m in enumerate(cluster.m):
        j = b-i
        q, r = divmod(m, 2)
        result.extend((3*j-1+3*q+r, 3*j-2+3*q+2*r))
    return tuple(result)


def compile_separated(cluster):
    """Forward bijection on precisely the safe domain; rejects unsafe coordinates."""
    if not isinstance(cluster, SeparatedCluster) or not cluster.admitted:
        raise ValueError('coordinates violate the separated boundary inequality')
    return literal_compile(cluster)


def split_atoms(parts):
    """Unique descending close-pair/singleton atomization of an actual gap."""
    if not is_gap(parts):
        raise ValueError('expected a descending KR1 gap partition')
    atoms = []
    i = 0
    while i < len(parts):
        if i+1 < len(parts) and parts[i]-parts[i+1] <= 1:
            atoms.append(('P', parts[i:i+2]))
            i += 2
        else:
            atoms.append(('S', parts[i:i+1]))
            i += 1
    return tuple(atoms)


def is_separated(parts):
    if not is_gap(parts):
        return False
    pair_seen = False
    for kind, _ in split_atoms(parts):
        if kind == 'P':
            pair_seen = True
        elif pair_seen:
            return False
    return True


def extract_separated(parts):
    """Intrinsic inverse, rejecting gap partitions outside S^a P^b."""
    if not is_separated(parts):
        raise ValueError('gap atom word is not S^a P^b')
    atoms = split_atoms(parts)
    singles = [values[0] for kind, values in atoms if kind == 'S']
    pairs = [values for kind, values in atoms if kind == 'P']
    a, b = len(singles), len(pairs)
    mu = tuple(value-3*b-2*(a-i)+1 for i, value in enumerate(singles))
    m = tuple((sum(values)-6*(b-i)+3)//3 for i, values in enumerate(pairs))
    result = SeparatedCluster(a, b, mu, m)
    if not result.admitted:
        raise AssertionError('inverse violated proved boundary condition')
    return result


def bounded_partitions(weight, length, ceiling=None):
    """Descending natural tuples of exact padded length, with prescribed sum."""
    if length == 0:
        if weight == 0:
            yield ()
        return
    ceiling = weight if ceiling is None else min(ceiling, weight)
    for head in range(ceiling, (weight+length-1)//length-1, -1):
        for tail in bounded_partitions(weight-head, length-1, head):
            yield (head,)+tail


def clusters(weight):
    a = 0
    while quadratic(a, 0) <= weight:
        b = 0
        while quadratic(a, b) <= weight:
            rest = weight-quadratic(a, b)
            for m_weight in range(rest//3+1):
                for mu in bounded_partitions(rest-3*m_weight, a):
                    for m in bounded_partitions(m_weight, b):
                        yield SeparatedCluster(a, b, mu, m)
            b += 1
        a += 1


def gap_partitions(weight, prefix=()):
    """Independent literal target enumeration, pruned only by gap predicates."""
    if weight == 0:
        yield prefix
        return
    upper = min(weight, prefix[-1] if prefix else weight)
    for part in range(upper, 0, -1):
        if prefix and prefix[-1]-part <= 1 and (prefix[-1]+part) % 3:
            continue
        if len(prefix) >= 2 and prefix[-2]-part < 3:
            continue
        yield from gap_partitions(weight-part, prefix+(part,))


def separated_series(a, b, maximum):
    """Coefficients of the positive rational formula, by subset-gap expansion."""
    base = quadratic(a, b)
    result = [0]*(maximum+1)
    for mask in range(1 << b):
        chosen = [i+1 for i in range(b) if mask & (1 << i)]
        exponent = base + 3*sum(chosen) + a*((3*len(chosen)+1)//2)
        if exponent <= maximum:
            result[exponent] += 1
    for part in (*range(1, a+1), *(6*i+3*a for i in range(1, b+1))):
        for weight in range(part, maximum+1):
            result[weight] += result[weight-part]
    return result
