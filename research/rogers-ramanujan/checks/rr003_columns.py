"""RR003 frozen restricted C<->U formulas; NOT a complete KR1 bijection.

Mathematical domains/proof: ../rr003/round-1-proposal.md. No enumeration,
ranking, search, or execution history is used by these maps.
"""
from collections import Counter
import kr1


class OutsideRestrictedDomain(ValueError):
    """A valid object outside the proved restricted construction."""


def supported(c):
    return isinstance(c, kr1.ClusterData) and (c.a <= 1 or c.a == 2 and c.mu[0] <= 1)


def reconstruct_columns(c):
    if not isinstance(c, kr1.ClusterData):
        raise ValueError('expected literal ClusterData')
    if not supported(c):
        raise OutsideRestrictedDomain('unresolved: a>=3 or a=2 with mu[0]>=2')
    delta = [c.nu[c.b-j] - (c.nu[c.b-j-1] if j < c.b else 0)
             for j in range(1, c.b+1)]
    counts = Counter()
    for j, increment in enumerate(delta, 1):
        counts[3*j] = 2 + increment - int(c.a == 0 and j == c.b)
    if c.a == 1:
        counts[1] = 1 + c.mu[0]
    elif c.a == 2 and c.mu[0] == 0:
        counts[3*(c.b+1)] += 1
        counts[1] = 1 + c.mu[1]
    elif c.a == 2:
        counts[3*(c.b+2)] += 1
        counts[1] = c.mu[1] - 1
    return tuple(x for x in sorted(counts, reverse=True) for _ in range(counts[x]))


def _recover(a, b, mu, counts):
    delta = [counts[3*j] - 2 + int(a == 0 and j == b) for j in range(1, b+1)]
    # nu_i = delta_b + ... + delta_(b-i+1), exact length including zeros.
    nu = []
    total = 0
    for increment in reversed(delta):
        total += increment
        nu.append(total)
    return kr1.ClusterData(a, b, mu, tuple(nu))


def decompose_columns(columns):
    kr1.decode_columns(columns)  # literal U domain, including the terminal step
    counts = Counter(columns)
    ones = counts.pop(1, 0)
    if not counts:
        return (kr1.ClusterData(1, 0, (ones-1,), ()) if ones
                else kr1.ClusterData(0, 0, (), ()))
    if any(value % 3 for value in counts):
        raise OutsideRestrictedDomain('unresolved non-three column residue')
    levels = {value//3 for value in counts}
    top = max(levels)
    full = levels == set(range(1, top+1))
    lower = all(counts[3*j] >= 2 for j in range(1, top))
    if full and lower:
        if not ones:
            return _recover(0, top, (), counts)
        if counts[3*top] >= 2:
            return _recover(1, top, (ones-1,), counts)
        return _recover(2, top-1, (0, ones-1), counts)
    if top >= 2 and levels == set(range(1, top-1)) | {top}:
        b = top-2
        if counts[3*top] == 1 and all(counts[3*j] >= 2 for j in range(1, b+1)):
            return _recover(2, b, (1, ones+1), counts)
    raise OutsideRestrictedDomain('unresolved column support or multiplicity')


def raise_nu_suffix(c, j):
    if not supported(c) or type(j) is not int or not 1 <= j <= c.b:
        raise ValueError('expected supported cluster and 1<=j<=b')
    return kr1.ClusterData(c.a, c.b, c.mu,
                           tuple(x + int(i >= c.b-j) for i, x in enumerate(c.nu)))


def raise_last_mu(c):
    if not supported(c) or not c.mu:
        raise ValueError('expected supported cluster with nonempty mu')
    return kr1.ClusterData(c.a, c.b, c.mu[:-1] + (c.mu[-1]+1,), c.nu)


def merge_raise(c):
    if not supported(c) or c.a != 2 or c.mu[0] != 0:
        raise ValueError('proved merge has domain a=2, mu[0]=0 only')
    return kr1.ClusterData(2, c.b, (1, c.mu[1]+1), c.nu)
