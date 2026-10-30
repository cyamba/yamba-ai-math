"""Prepared exact finite algebra for the reflected major-energy interface."""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from fractions import Fraction
import hashlib
import importlib.util
from itertools import product
import json
import math
from pathlib import Path
import platform
import sys
import time

AUTHOR_STATEMENT_INSTANTIATED = True
FROZEN_STATEMENT_SHA256 = 'eb76660af2f2ccb2ac003fdf835d2b05c325435d7600ed9e7f98448eb32da80b'
HELPER_SHA256 = '498798fd996b211cf5d1f1b3bea47b101fcc720061d9b2133c1a9d5df92e28af'


def load_algebra():
    path = Path(__file__).resolve().parents[1] / 'complement-ratios-20261029' / 'ratio_checks.py'
    if hashlib.sha256(path.read_bytes()).hexdigest() != HELPER_SHA256:
        raise SystemExit('Frozen cyclotomic helper hash mismatch.')
    spec = importlib.util.spec_from_file_location('energy_cyclotomic_helper', path)
    module = importlib.util.module_from_spec(spec)
    old_flag = sys.dont_write_bytecode
    try:
        sys.dont_write_bytecode = True
        spec.loader.exec_module(module)
    finally:
        sys.dont_write_bytecode = old_flag
    return module


def require(condition, failures, kind, **values):
    if not condition:
        failures.append({'type': kind, **values})


def gaussian(real=0, imaginary=0):
    return Fraction(real), Fraction(imaginary)


def gadd(a, b):
    return a[0] + b[0], a[1] + b[1]


def gmul(a, b):
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]


def gscale(a, value):
    return a[0] * value, a[1] * value


def gnorm(a):
    return a[0] ** 2 + a[1] ** 2


class ExactRoots:
    def __init__(self, order, algebra):
        self.order = order
        self.algebra = algebra

    def scalar(self, value):
        return [Fraction(value)]

    def root(self, exponent):
        polynomial = [0] * ((exponent % self.order) + 1)
        polynomial[-1] = 1
        return self.algebra.residue(polynomial, self.order)

    def add(self, *values):
        answer = [0]
        for value in values:
            answer = self.algebra.add(answer, value)
        return answer

    def neg(self, value):
        return [-x for x in value]

    def subtract(self, left, right):
        return self.add(left, self.neg(right))

    def scale(self, value, scalar):
        return self.algebra.trim([x * scalar for x in value])

    def multiply(self, left, right):
        return self.algebra.multiply(left, right, self.order)

    def conjugate(self, value):
        answer = [0]
        for i, coefficient in enumerate(value):
            answer = self.add(answer, self.scale(self.root(-i), coefficient))
        return answer

    def norm(self, value):
        return self.multiply(value, self.conjugate(value))

    def gaussian(self, value):
        assert self.order % 4 == 0
        return self.add(self.scalar(value[0]), self.scale(self.root(self.order // 4), value[1]))


def unit_characters(q):
    """Construct every character by extending along a subgroup chain."""
    units = [a for a in range(q) if math.gcd(a, q) == 1]
    identity = 1 % q
    orders = []
    for a in units:
        value, order = a % q, 1
        while value != identity:
            value = value * a % q
            order += 1
        orders.append(order)
    exponent = math.lcm(*orders)
    subgroup = {identity}
    characters = [{identity: 0}]
    while len(subgroup) < len(units):
        generator = next(a for a in units if a not in subgroup)
        power, relative_order = generator, 1
        while power not in subgroup:
            power = power * generator % q
            relative_order += 1
        new_characters = []
        for character in characters:
            for value in range(exponent):
                if relative_order * value % exponent != character[power]:
                    continue
                extension = {}
                for old in subgroup:
                    current = old
                    for j in range(relative_order):
                        extension[current] = (character[old] + j * value) % exponent
                        current = current * generator % q
                new_characters.append(extension)
        characters = new_characters
        subgroup = set(characters[0])
    return units, exponent, characters


def fiber_checks(smoke, failures, algebra):
    H_values = [4, 6] if smoke else [2, 4, 6, 8, 10, 12, 14, 18, 20]
    k_values = [2, 3] if smoke else [1, 2, 3, 4]
    counts = defaultdict(int)
    domains = []
    for H, k in product(H_values, k_values):
        q = k * H
        units, exponent, characters = unit_characters(q)
        base_units, base_exponent, base_characters = unit_characters(H)
        require(len(characters) == len(units), failures, 'character_count', q=q)
        for character in characters:
            require(all(character[a * b % q] == (character[a] + character[b]) % exponent
                        for a, b in product(units, repeat=2)), failures, 'character_homomorphism', q=q)
            counts['characters'] += 1
        kernel = [a for a in units if a % H == 1 % H]
        predicted_size = Fraction(k)
        for p in set(algebra.factors(k)):
            if H % p:
                predicted_size *= 1 - Fraction(1, p)
        fibers = {a: [u for u in units if u % H == a] for a in base_units}
        require(all(len(fiber) == predicted_size == len(kernel) for fiber in fibers.values()),
                failures, 'unit_reduction_kernel', H=H, k=k)
        restrictions = {}
        for character in characters:
            restrictions.setdefault(tuple(character[w] for w in kernel), character)
        require(len(restrictions) == len(kernel), failures, 'kernel_character_extension', H=H, k=k)
        counts['unit_reductions'] += 1
        counts['noncoprime_kH'] += math.gcd(k, H) > 1
        root_order = math.lcm(q, exponent, 4)
        ring = ExactRoots(root_order, algebra)
        psi_characters = list(restrictions.values())
        for a, fiber in fibers.items():
            representative = min(fiber)
            coefficients = []
            for psi in psi_characters:
                terms = [ring.root(representative * w * (root_order // q) -
                                   psi[w] * (root_order // exponent)) for w in kernel]
                coefficient = ring.scale(ring.add(*terms), Fraction(1, len(kernel)))
                coefficients.append(coefficient)
                squares = ring.add(*(ring.norm(ring.subtract(terms[i], terms[j]))
                                     for i in range(len(terms)) for j in range(i + 1, len(terms))))
                require(ring.subtract([1], ring.norm(coefficient)) ==
                        ring.scale(squares, Fraction(1, len(kernel) ** 2)), failures,
                        'coefficient_bound_sum_of_squares', H=H, k=k, a=a)
                counts['coefficient_bound_certificates'] += 1
            require(ring.add(*(ring.norm(c) for c in coefficients)) == [1], failures,
                    'fiber_parseval', H=H, k=k, a=a)
            for u in fiber:
                expanded = ring.add(*(ring.multiply(c, ring.root((psi[u] - psi[representative]) *
                                                                  (root_order // exponent)))
                                      for c, psi in zip(coefficients, psi_characters)))
                require(expanded == ring.root(u * (root_order // q)), failures,
                        'fiber_fourier_reconstruction', H=H, k=k, a=a, u=u)
                counts['fiber_reconstructions'] += 1
            X = [ring.gaussian(gaussian(Fraction(a + j, j + 1), Fraction(j - a, j + 2)))
                 for j in range(len(coefficients))]
            effective = [ring.multiply(c, ring.root(-psi[representative] * (root_order // exponent)))
                         for c, psi in zip(coefficients, psi_characters)]
            linear = ring.add(*(ring.multiply(c, x) for c, x in zip(effective, X)))
            lhs = ring.subtract(ring.add(*(ring.norm(x) for x in X)), ring.norm(linear))
            rhs = ring.add(*(ring.norm(ring.subtract(
                ring.multiply(effective[i], ring.conjugate(X[j])),
                ring.multiply(effective[j], ring.conjugate(X[i]))))
                for i in range(len(X)) for j in range(i + 1, len(X))))
            require(lhs == rhs, failures, 'class_dependent_cauchy_certificate', H=H, k=k, a=a)
            source_gap = ring.subtract(ring.scale(ring.add(*(ring.norm(x) for x in X)), k), ring.norm(linear))
            require(source_gap == ring.add(rhs, ring.scale(ring.add(*(ring.norm(x) for x in X)), k - 1)),
                    failures, 'author_classwise_k_cauchy_5', H=H, k=k, a=a)
            counts['cauchy_certificates'] += 1
        class_values = {a: ring.gaussian(gaussian(Fraction(a, 3), Fraction(a % 3 - 1, 2))) for a in base_units}
        transformed = [ring.add(*(ring.multiply(class_values[a], ring.root(chi[a] * (root_order // base_exponent)))
                                 for a in base_units)) for chi in base_characters]
        base_parseval = ring.scale(ring.add(*(ring.norm(value) for value in transformed)), Fraction(1, len(base_characters)))
        require(base_parseval == ring.add(*(ring.norm(value) for value in class_values.values())),
                failures, 'base_class_Parseval_after_Cauchy', H=H, k=k)
        counts['base_class_Parseval_cases'] += 1
        for psi in psi_characters:
            products = {tuple((chi[u % H] * (exponent // base_exponent) + psi[u]) % exponent
                              for u in units) for chi in base_characters}
            require(len(products) == len(base_characters), failures, 'fixed_twist_injectivity', H=H, k=k)
            counts['fixed_twist_cases'] += 1
        domains.append({'H': H, 'k': k, 'q': q, 'unit_count': len(units), 'kernel_size': len(kernel),
                        'character_exponent': exponent, 'exact_root_order': root_order})
    # Both products are quadratic modulo 3 when the twist varies with chi.
    principal, quadratic = (0, 0), (0, 1)
    first = tuple((a + b) % 2 for a, b in zip(principal, quadratic))
    second = tuple((a + b) % 2 for a, b in zip(quadratic, principal))
    require(first == second and principal != quadratic, failures, 'varying_twist_collapse_negative_control')
    return {'counts': dict(counts), 'domains': domains,
            'negative_control': {'modulus': 3, 'chi1': principal, 'psi1': quadratic,
                                  'chi2': quadratic, 'psi2': principal, 'common_product': first}}


def normalization_checks(smoke, failures, algebra):
    counts = defaultdict(int)
    records = []
    for H in ([6] if smoke else [6, 10]):
        k, Y, M, N = 3, 2, 3, 2
        q = k * H
        units, exponent, full_characters = unit_characters(q)
        _, base_exponent, base_characters = unit_characters(H)
        _, marking_exponent, marking_characters = unit_characters(k)
        root_order = math.lcm(exponent, 4)
        ring = ExactRoots(root_order, algebra)
        psi = full_characters[-1]
        marking = [b for b in (5, 7, 11) if math.gcd(b, q) == 1]
        m_values = [m for m in (1, 5, 7) if math.gcd(m, q) == 1]
        n_values = [n for n in (1, 5) if math.gcd(n, q) == 1]
        V = sum((Fraction(1, b) for b in marking), Fraction())
        raw = [0]
        normalized = [0]
        raw_bilinear, normalized_bilinear = [0], [0]
        for sample, weight in enumerate((Fraction(1, 2), Fraction(1, 3), Fraction(1, 6))):
            independent = {frequency: [] for frequency in (0, 1, -1)}
            for chi in base_characters:
                def character(n, marking_twist=False):
                    phase = ((chi[n % H] * (exponent // base_exponent) + psi[n % q]) *
                             (root_order // exponent))
                    if marking_twist:
                        phase += marking_characters[-1][n % k] * (root_order // marking_exponent)
                    return ring.root(phase)
                for frequency in (0, 1, -1):
                    # Exact toy multiplicative phases; this is an algebraic
                    # surrogate, not a numerical evaluation of n^(it).
                    def phase(n):
                        return ring.root(frequency * len(algebra.factors(n)) * (root_order // 4))
                    Braw = ring.add(*(ring.multiply(ring.multiply(
                        ring.root(-sample * b * (root_order // 4)), character(b, True)), phase(b)) for b in marking))
                    Mraw = ring.add(*(ring.multiply(ring.multiply(
                        ring.gaussian(gaussian(Fraction(m, 3), Fraction(1, m))), character(m)), phase(m)) for m in m_values))
                    Nraw = ring.add(*(ring.multiply(ring.multiply(
                        ring.gaussian(gaussian(Fraction(n, 2), Fraction(-1, n))), character(n)), phase(n)) for n in n_values))
                    unscaled = ring.multiply(ring.multiply(Braw, Mraw), Nraw)
                    BMN = ring.scale(unscaled, Fraction(1, Y * M * N) / V)
                    independent[frequency].append((unscaled, BMN))
                    if frequency == 0:
                        factor = weight / len(base_characters)
                        raw = ring.add(raw, ring.scale(ring.norm(unscaled), factor / (Y * V ** 2)))
                        normalized = ring.add(normalized, ring.scale(ring.norm(BMN), factor))
                    counts['sample_character_products'] += 1
            left_values = [row[1] for row in independent[1]]
            right_values = [row[1] for row in independent[-1]]
            character_count = len(base_characters)
            left_energy = ring.scale(ring.add(*(ring.norm(value) for value in left_values)), Fraction(1, character_count))
            right_energy = ring.scale(ring.add(*(ring.norm(value) for value in right_values)), Fraction(1, character_count))
            inner = ring.scale(ring.add(*(ring.multiply(left, ring.conjugate(right))
                                         for left, right in zip(left_values, right_values))), Fraction(1, character_count))
            gap = ring.subtract(ring.multiply(left_energy, right_energy), ring.norm(inner))
            certificate = ring.scale(ring.add(*(ring.norm(ring.subtract(
                ring.multiply(left_values[i], right_values[j]), ring.multiply(left_values[j], right_values[i])))
                for i in range(character_count) for j in range(i + 1, character_count))), Fraction(1, character_count ** 2))
            require(gap == certificate, failures, 'two_independent_factor_Cauchy_certificate', H=H, sample=sample)
            for left, right in zip(independent[1], independent[-1]):
                raw_bilinear = ring.add(raw_bilinear, ring.scale(ring.multiply(left[0], ring.conjugate(right[0])),
                                                               weight / character_count / (Y * V ** 2)))
                normalized_bilinear = ring.add(normalized_bilinear, ring.scale(ring.multiply(left[1], ring.conjugate(right[1])),
                                                                             weight / character_count))
            counts['two_factor_cauchy_certificates'] += 1
        require(raw == ring.scale(normalized, Y * (M * N) ** 2), failures, 'normalized_arc_energy_prefactor', H=H)
        require(raw_bilinear == ring.scale(normalized_bilinear, Y * (M * N) ** 2), failures,
                'independent_bilinear_arc_prefactor', H=H)
        records.append({'H': H, 'k': k, 'Y': Y, 'M': M, 'N': N, 'V': V,
                        'prefactor': Y * (M * N) ** 2, 'raw_scaled_energy': raw, 'normalized_energy': normalized,
                        'raw_scaled_bilinear': raw_bilinear, 'normalized_bilinear': normalized_bilinear,
                        'phase_scope': 'Independent order4 multiplicative toy phases; no analytic Mellin or actual-coefficient energy test.'})
    n_limit = 100 if smoke else 5000
    Z_values = [3] if smoke else (2, 3, 5, 7)
    for n in range(1, n_limit + 1):
        factors = algebra.factors(n)
        divisors = [d for d in range(1, math.isqrt(n) + 1) if n % d == 0]
        divisors = sorted(set(divisors + [n // d for d in divisors]))
        for Z in Z_values:
            convolution = sum(algebra.mobius(d) for d in divisors
                              if all(p <= Z for p in algebra.factors(n // d)))
            direct = algebra.mobius(n) * all(p > Z for p in factors)
            require(convolution == direct, failures, 'smooth_mobius_convolution', n=n, Z=Z)
            counts['convolution_cases'] += 1
    length = 6 if smoke else 16
    for left in range(1, length + 1):
        for right in range(left, length + 1):
            coefficients = [gmul(gaussian((0, 1, 0, -1)[n % 4], (1, 0, -1, 0)[n % 4]),
                                 gaussian(Fraction(1, n + 1))) for n in range(left, right + 1)]
            weights = [Fraction(n * n + 1, 7) for n in range(left, right + 1)]
            partial, prefixes = gaussian(), []
            for value in coefficients:
                partial = gadd(partial, value)
                prefixes.append(partial)
            direct = gaussian()
            for value, weight in zip(coefficients, weights):
                direct = gadd(direct, gscale(value, weight))
            abel = gscale(prefixes[-1], weights[-1])
            for j in range(len(weights) - 1):
                abel = gadd(abel, gscale(prefixes[j], weights[j] - weights[j + 1]))
            variation = abs(weights[-1]) + sum(abs(weights[j + 1] - weights[j]) for j in range(len(weights) - 1))
            require(direct == abel, failures, 'discrete_real_weight_partial_summation', left=left, right=right)
            require(gnorm(direct) <= max(map(gnorm, prefixes)) * variation ** 2,
                    failures, 'partial_summation_variation_bound', left=left, right=right)
            counts['partial_summation_intervals'] += 1
    return {'counts': dict(counts), 'normalization_records': records,
            'scope': 'Exact finite prefactors and discrete coefficient algebra, not Mellin or analytic energy estimates.'}


def sparse_checks(smoke, failures, algebra):
    groups = ((3, 5, 7), (11, 13))
    counts = defaultdict(int)
    records = []
    for K in ([1] if smoke else [1, 2]):
        marking = [math.prod(draw) for draw in product(*groups[:K])]
        coefficients = {b: gaussian(Fraction(1, b), Fraction((i % 3) - 1, 2 * b))
                        for i, b in enumerate(marking)}
        one_norm = sum(map(gnorm, coefficients.values()), Fraction())
        for j in range(3 if smoke else 5):
            power_coefficients = defaultdict(lambda: gaussian())
            representation_norms = defaultdict(Fraction)
            multiplicities = Counter()
            for row in product(marking, repeat=j):
                u = math.prod(row)
                coefficient = gaussian(1)
                for b in row:
                    coefficient = gmul(coefficient, coefficients[b])
                power_coefficients[u] = gadd(power_coefficients[u], coefficient)
                representation_norms[u] += gnorm(coefficient)
                multiplicities[u] += 1
                counts['ordered_representations'] += 1
            bound = math.factorial(j) ** K
            for u, multiplicity in multiplicities.items():
                prime_counts = Counter(algebra.factors(u))
                exact_count = 1
                for group in groups[:K]:
                    require(sum(prime_counts[p] for p in group) == j, failures, 'band_prime_count', u=u, K=K, j=j)
                    exact_count *= math.factorial(j) // math.prod(math.factorial(prime_counts[p]) for p in group)
                require(multiplicity == exact_count <= bound, failures,
                        'repeated_prime_representation_count', u=u, K=K, j=j)
                require(gnorm(power_coefficients[u]) <= multiplicity * representation_norms[u] <=
                        bound * representation_norms[u], failures, 'sparse_coefficient_cauchy', u=u, K=K, j=j)
                counts['coefficient_cases'] += 1
            total = sum(map(gnorm, power_coefficients.values()), Fraction())
            require(total <= bound * one_norm ** j, failures, 'total_sparse_coefficient_bound', K=K, j=j)
            records.append({'K': K, 'j': j, 'distinct_products': len(multiplicities),
                            'factorial_bound': bound, 'sum_coefficient_squares': total,
                            'upper_bound': bound * one_norm ** j})
    repeated_u = (3 * 11) ** 2
    require(1 < math.factorial(2) ** 2 and Counter(algebra.factors(repeated_u)) == Counter({3: 2, 11: 2}),
            failures, 'repeated_prime_equality_negative_control')
    _, quadratic_order, modulo3_characters = unit_characters(3)
    quadratic = next(chi for chi in modulo3_characters if chi[2] != 0)
    product_character_exponent = quadratic[35 % 3]
    require(product_character_exponent == (quadratic[5 % 3] + quadratic[7 % 3]) % quadratic_order and
            product_character_exponent != 2 * product_character_exponent % quadratic_order,
            failures, 'character_at_product_not_raised_power_negative_control')
    return {'counts': dict(counts), 'records': records,
            'negative_control': {'K': 2, 'j': 2, 'u': repeated_u,
                                  'exact_representation_count': 1, 'factorial_upper_bound': 4,
                                  'character_product': {'modulus': 3, 'row': (5, 7), 'u': 35,
                                                        'correct_character_value': -1, 'wrong_squared_character_value': 1}}}


def encode(value):
    if isinstance(value, Fraction):
        return str(value)
    raise TypeError(type(value).__name__)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--smoke', action='store_true')
    parser.add_argument('--packet', type=Path, required=True)
    args = parser.parse_args()
    if not AUTHOR_STATEMENT_INSTANTIATED:
        raise SystemExit('Preparation only. Await the frozen author statement and actual main finite-check packet.')
    directory = Path(__file__).resolve().parent
    actual_source_hash = hashlib.sha256((directory / 'statement.md').read_bytes()).hexdigest()
    if actual_source_hash != FROZEN_STATEMENT_SHA256:
        raise SystemExit('Frozen statement hash mismatch.')
    packet = json.loads(args.packet.read_text(encoding='utf-8-sig'))
    if packet['step']['id'] != 'finite-check' or not packet.get('upstream'):
        raise SystemExit('Actual populated finite-check packet required.')
    algebra = load_algebra()
    started = time.perf_counter()
    failures = []
    comparisons = {'unit_fibers': fiber_checks(args.smoke, failures, algebra),
                   'normalization_convolution': normalization_checks(args.smoke, failures, algebra),
                   'sparse_representations': sparse_checks(args.smoke, failures, algebra)}
    result = {'mode': 'smoke' if args.smoke else 'bounded_final', 'passed': not failures,
              'runtime_seconds': time.perf_counter() - started, 'python': platform.python_version(),
              'platform': platform.platform(), 'helper_sha256': HELPER_SHA256,
              'code_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'statement_sha256': actual_source_hash,
              'packet_sha256': hashlib.sha256(args.packet.read_bytes()).hexdigest(),
              'comparisons': comparisons, 'failures': failures,
              'scope': 'Finite exact identities only; no zero-free, analytic norm, major-energy or Goldbach certification.'}
    if not args.smoke:
        (directory / 'finite-results.json').write_text(json.dumps(result, indent=2, default=encode) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2, default=encode))
    return 0 if not failures else 1


if __name__ == '__main__':
    raise SystemExit(main())
