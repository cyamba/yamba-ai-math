"""Independent, deliberately small exact coloring oracle.

For a natural unit interval graph encoded by its Hessenberg vector ``h``,
``elementary_expansion(h)`` computes the chromatic quasisymmetric function
directly from proper colorings, then changes from monomials to elementary
symmetric functions by rational Gaussian elimination.  It uses no tableaux,
Jacobi--Trudi identities, or sign-reversing involution.

Coefficients are tuples in increasing powers of q.  Partition indices are
weakly decreasing tuples.  Zero coefficients are omitted.  The algorithm is
intended for small instances (in particular n <= 5), not asymptotic evidence.
"""

from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations


def _hessenberg(h):
    h = tuple(h)
    n = len(h)
    if any(type(value) is not int for value in h):
        raise ValueError("Hessenberg entries must be integers")
    if any(not i + 1 <= value <= n for i, value in enumerate(h)):
        raise ValueError("Hessenberg entries must satisfy i <= h_i <= n")
    if any(a > b for a, b in zip(h, h[1:])):
        raise ValueError("Hessenberg vector must be weakly increasing")
    return h


def graph_edges(h):
    """Return 0-based edges (i,j), i<j<=h_i, from a 1-based vector."""
    h = _hessenberg(h)
    return tuple((i, j) for i, bound in enumerate(h) for j in range(i + 1, bound))


@lru_cache(maxsize=None)
def partitions(n):
    """All partitions of n in reverse lexicographic order, including () at 0."""
    if type(n) is not int or n < 0:
        raise ValueError("partition size must be a nonnegative integer")

    def generate(remaining, largest):
        if remaining == 0:
            yield ()
        for first in range(min(remaining, largest), 0, -1):
            for tail in generate(remaining - first, first):
                yield (first,) + tail

    return tuple(generate(n, n))


def _trim(poly):
    result = list(poly)
    while result and result[-1] == 0:
        result.pop()
    return tuple(result)


def named_monomial_coefficient(h, multiplicities):
    """Coefficient of x_1^a_1 ... x_k^a_k, without assuming symmetry."""
    h = _hessenberg(h)
    n = len(h)
    multiplicities = tuple(multiplicities)
    if any(type(value) is not int or value <= 0 for value in multiplicities):
        raise ValueError("color multiplicities must be positive integers")
    if sum(multiplicities) != n:
        raise ValueError("color multiplicities must sum to the vertex count")
    edges = graph_edges(h)
    earlier_neighbors = tuple(
        tuple(i for i, j in edges if j == vertex) for vertex in range(n)
    )
    remaining = list(multiplicities)
    assigned = []
    counts = Counter()

    def visit(vertex, asc):
        if vertex == n:
            counts[asc] += 1
            return
        neighbors = earlier_neighbors[vertex]
        for color, available in enumerate(remaining):
            if not available or any(assigned[i] == color for i in neighbors):
                continue
            extra = sum(assigned[i] < color for i in neighbors)
            assigned.append(color)
            remaining[color] -= 1
            visit(vertex + 1, asc + extra)
            remaining[color] += 1
            assigned.pop()

    visit(0, 0)
    return _trim(counts.get(degree, 0) for degree in range(len(edges) + 1))


def monomial_coefficients(h):
    """Coefficients of x_1^mu_1 ... x_k^mu_k for every partition mu.

    Colors are the ordered integers 0,...,k-1.  A coloring contributes
    q^asc, where asc counts edges (i,j) with i<j and color(i)<color(j).
    For these graphs the chromatic quasisymmetric function is symmetric;
    each returned coefficient therefore is its monomial-basis coefficient.
    """
    h = _hessenberg(h)
    return {mu: named_monomial_coefficient(h, mu) for mu in partitions(len(h))}


@lru_cache(maxsize=None)
def elementary_monomial_coefficient(shape, exponents):
    """Coefficient of a single named monomial in e_shape.

    This expands each elementary factor as a sum over subsets of the named
    colors.  Exponents never exceed the target, so the finite computation
    does not rely on any symmetric-function change-of-basis formula.
    """
    shape, exponents = tuple(shape), tuple(exponents)
    if sum(shape) != sum(exponents):
        return 0
    k = len(exponents)
    states = {(0,) * k: 1}
    for size in shape:
        if size > k:
            return 0
        next_states = Counter()
        for subset in combinations(range(k), size):
            indicator = tuple(int(i in subset) for i in range(k))
            for powers, coefficient in states.items():
                new_powers = tuple(a + b for a, b in zip(powers, indicator))
                if all(a <= b for a, b in zip(new_powers, exponents)):
                    next_states[new_powers] += coefficient
        states = next_states
    return states.get(exponents, 0)


@lru_cache(maxsize=None)
def _inverse_elementary_matrix(n):
    shapes = partitions(n)
    count = len(shapes)
    # Rows index named monomials; columns index elementary products.
    matrix = [
        [Fraction(elementary_monomial_coefficient(shape, exponents)) for shape in shapes]
        + [Fraction(int(i == j)) for j in range(count)]
        for i, exponents in enumerate(shapes)
    ]
    for column in range(count):
        pivot = next((row for row in range(column, count) if matrix[row][column]), None)
        if pivot is None:
            raise ArithmeticError("singular elementary-to-monomial matrix")
        matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
        divisor = matrix[column][column]
        matrix[column] = [entry / divisor for entry in matrix[column]]
        for row in range(count):
            if row == column:
                continue
            factor = matrix[row][column]
            if factor:
                matrix[row] = [
                    a - factor * b for a, b in zip(matrix[row], matrix[column])
                ]
    return tuple(tuple(row[count:]) for row in matrix)


def elementary_expansion(h):
    """Compute the complete finite-degree e expansion by exact colorings."""
    h = _hessenberg(h)
    n = len(h)
    shapes = partitions(n)
    monomials = monomial_coefficients(h)
    inverse = _inverse_elementary_matrix(n)
    degrees = len(graph_edges(h)) + 1
    result = {}
    for shape, inverse_row in zip(shapes, inverse):
        polynomial = []
        for degree in range(degrees):
            coefficient = sum(
                factor * (monomials[mu][degree] if degree < len(monomials[mu]) else 0)
                for mu, factor in zip(shapes, inverse_row)
            )
            if coefficient.denominator != 1:
                raise ArithmeticError("nonintegral elementary coefficient")
            polynomial.append(coefficient.numerator)
        polynomial = _trim(polynomial)
        if polynomial:
            result[shape] = polynomial
    return result
