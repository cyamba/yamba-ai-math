"""Prepared exact finite prime-relative moment and weight-removal checks."""
from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction
import hashlib
from itertools import combinations, product
import json
import math
from pathlib import Path
import platform
import time

AUTHOR_STATEMENT_INSTANTIATED = True
FROZEN_STATEMENT_SHA256 = '22b1e94dff57c26ace239b82cf82f83aa06967338628cc14900fd911695fbda8'


def require(condition, failures, kind, **values):
    if not condition:
        failures.append({'type': kind, **values})


def gaussian(real=0, imaginary=0):
    return Fraction(real), Fraction(imaginary)


def gadd(a, b):
    return a[0] + b[0], a[1] + b[1]


def gscale(a, value):
    return a[0] * value, a[1] * value


def gnorm(a):
    return a[0] ** 2 + a[1] ** 2


def band_weight(selected, group, rho):
    V = sum((Fraction(1, p) for p in group), Fraction())
    if not V:
        raise ValueError('Punctured group has zero normalizer.')
    omega = sum(p in selected for p in group)
    return omega * rho ** (omega - 1) / V if omega else Fraction()


def band_mean(group, rho, probability):
    V = sum((Fraction(1, p) for p in group), Fraction())
    return sum((probability(p) * math.prod(1 - (1 - rho) * probability(q)
                                         for q in group if q != p) for p in group), Fraction()) / V


def band_expansion(selected, group, rho, R):
    V = sum((Fraction(1, p) for p in group), Fraction())
    u = sum(p in selected for p in group)
    polynomial = sum(((j + 1) * (rho - 1) ** j * math.comb(u, j + 1) / V
                      for j in range(R) if j + 1 <= u), Fraction())
    absolute_polynomial = sum(((j + 1) * (1 - rho) ** j * math.comb(u, j + 1) / V
                               for j in range(R) if j + 1 <= u), Fraction())
    remainder = ((R + 1) * (1 - rho) ** R * math.comb(u, R + 1) / V if R + 1 <= u else Fraction())
    true_upper_bound = 1 / ((1 - rho) ** 2 * V)
    return polynomial, absolute_polynomial, remainder, true_upper_bound


def model_checks(smoke, failures):
    families = [(((3, 5),), ((7, 11),), ((13, 17),)),
                (((3, 5), (7, 11)), ((13, 17), (19, 23)))]
    if smoke:
        families = [families[0][:2]]
    H_values = (2,) if smoke else (2, 6, 10)
    rhos = (Fraction(1, 2),) if smoke else (Fraction(1, 4), Fraction(1, 2), Fraction(3, 4))
    counts = defaultdict(int)
    records = []
    target_values = (gaussian(1), gaussian(-1), gaussian(0, 1), gaussian(0, -1),
                     gaussian(Fraction(3, 5), Fraction(4, 5)))
    for H, rho, source_family in product(H_values, rhos, families):
        family = [tuple(tuple(p for p in group if H % p) for group in copy) for copy in source_family]
        assert all(group for copy in family for group in copy)
        primes = sorted({p for copy in family for group in copy for p in group})
        q = {p: Fraction(1, p - 1) for p in primes}
        copy_count = len(family)
        closed_means = [math.prod(band_mean(group, rho, lambda p: q[p]) for group in copy) for copy in family]
        means, seconds, maxima = [Fraction()] * copy_count, [Fraction()] * copy_count, [Fraction()] * copy_count
        mixed = {(j, k): Fraction() for j in range(copy_count) for k in range(j + 1, copy_count)}
        rows = []
        mass = Fraction()
        for state in range(1 << len(primes)):
            selected = {p for index, p in enumerate(primes) if state >> index & 1}
            probability = math.prod(q[p] if p in selected else 1 - q[p] for p in primes)
            values = [math.prod(band_weight(selected, group, rho) for group in copy) for copy in family]
            rows.append((state, probability, values))
            mass += probability
            for j, value in enumerate(values):
                means[j] += probability * value
                seconds[j] += probability * value ** 2
                maxima[j] = max(maxima[j], value)
            for j, k in mixed:
                mixed[j, k] += probability * values[j] * values[k]
            terms = [(j,) for j in range(copy_count)] + list(mixed)
            for copies in terms:
                bands = [group for j in copies for group in family[j]]
                true = math.prod(band_weight(selected, group, rho) for group in bands)
                for R in (1, 2):
                    expansion = [band_expansion(selected, group, rho, R) for group in bands]
                    retained = math.prod(row[0] for row in expansion)
                    positive_error = sum((row[2] * math.prod(other[1] for other in expansion[:index]) *
                                          math.prod(other[3] for other in expansion[index + 1:])
                                          for index, row in enumerate(expansion)), Fraction())
                    require(abs(true - retained) <= positive_error, failures,
                            'author_multiband_positive_Taylor_error', H=H, state=state, copies=copies, R=R)
                    counts['single_and_mixed_positive_error_cases'] += 1
            counts['bernoulli_outcomes'] += 1
        require(mass == 1 and means == closed_means and all(value > 0 for value in means),
                failures, 'prime_relative_closed_mean', H=H, rho=rho, family=family)
        for (j, k), value in mixed.items():
            require(value == means[j] * means[k], failures, 'disjoint_mixed_moment', H=H, j=j, k=k)
            counts['cross_moment_cases'] += 1
        normalized_max = max(maxima[j] / means[j] for j in range(copy_count))
        for state, probability, values in rows:
            for j, value in enumerate(values):
                require(value ** 2 <= maxima[j] * value, failures, 'pointwise_diagonal_bound', H=H, state=state, j=j)
                counts['pointwise_diagonal_cases'] += 1
        for b in range(1, copy_count + 1):
            mean_bar, variance = Fraction(), Fraction()
            weighted_mass, weighted_variance, target_norm = Fraction(), Fraction(), Fraction()
            correlation = gaussian()
            for state, probability, values in rows:
                Wbar = sum((values[j] / means[j] for j in range(b)), Fraction()) / b
                mean_bar += probability * Wbar
                variance += probability * (Wbar - 1) ** 2
                measure = probability * (1 + Fraction(state % 5, 7))
                target = target_values[state % len(target_values)]
                require(gnorm(target) <= 1, failures, 'bounded_complex_target')
                weighted_mass += measure
                weighted_variance += measure * (Wbar - 1) ** 2
                target_norm += measure * gnorm(target)
                correlation = gadd(correlation, gscale(target, measure * (1 - Wbar)))
                counts['normalized_outcome_cases'] += 1
            diagonal_identity = sum((seconds[j] / means[j] ** 2 - 1 for j in range(b)), Fraction()) / b ** 2
            require(mean_bar == 1 and variance == diagonal_identity, failures,
                    'normalized_weight_variance_identity', H=H, rho=rho, b=b)
            require(variance <= (normalized_max - 1) / b, failures,
                    'finite_diagonal_variance_bound', H=H, rho=rho, b=b)
            require(gnorm(correlation) <= target_norm * weighted_variance <= weighted_mass * weighted_variance,
                    failures, 'positive_measure_complex_cauchy', H=H, rho=rho, b=b)
            counts['variance_and_weighted_cauchy_cases'] += 1
            records.append({'H': H, 'rho': rho, 'K': len(family[0]), 'b': b, 'means': means[:b],
                            'variance': variance, 'finite_constant_across_family_prefixes': normalized_max - 1,
                            'variance_upper_bound': (normalized_max - 1) / b,
                            'weighted_measure_mass': weighted_mass, 'weighted_variance': weighted_variance,
                            'complex_correlation': correlation, 'complex_cauchy_upper': weighted_mass * weighted_variance})
    actual = band_mean((3,), Fraction(1, 2), lambda p: Fraction(1, p - 1))
    wrong_integer = band_mean((3,), Fraction(1, 2), lambda p: Fraction(1, p))
    wrong_root = band_mean((3,), Fraction(1, 2), lambda p: Fraction(1, p + 1))
    require((actual, wrong_integer, wrong_root) == (Fraction(3, 2), Fraction(1), Fraction(3, 4)),
            failures, 'wrong_population_negative_controls')
    duplicate_variance = sum((Fraction(1, 2) * (value - 1) ** 2 for value in (0, 2)), Fraction())
    require(duplicate_variance == 1 and duplicate_variance > Fraction(1, 2), failures,
            'omitted_disjointness_negative_control')
    punctured = tuple(p for p in (3, 5) if 30 % p)
    require(not punctured and sum((Fraction(1, p) for p in punctured), Fraction()) == 0,
            failures, 'zero_normalizer_puncturing_control')
    thresholds = []
    for b in range(2, 11):
        even_diagonal_H = 2 ** b - 2
        require(even_diagonal_H < 2 ** b and not (2 ** b < 2 ** b), failures, 'fixed_threshold_diagonal_control', b=b)
        thresholds.append({'b': b, 'even_H': even_diagonal_H, 'E_b_H': 1, 'E_b_at_2_power_b': 0})
    return {'counts': dict(counts), 'records': records,
            'negative_controls': {'singleton_prime': 3, 'actual_prime_mean': actual,
                                  'wrong_integer_mean': wrong_integer, 'wrong_root_mean': wrong_root,
                                  'identical_copies': {'normalized_values': (0, 2), 'probabilities': (Fraction(1, 2), Fraction(1, 2)),
                                                       'b': 2, 'actual_variance': duplicate_variance,
                                                       'incorrect_independent_variance': Fraction(1, 2)},
                                  'zero_normalizer_group': {'H': 30, 'original': (3, 5), 'punctured': punctured},
                                  'fixed_threshold_illustration_only': {'definition': 'E_b(H)=1 if H<2^b else 0',
                                                                        'finite_diagonal': thresholds}}}


def taylor_crt_checks(smoke, failures):
    counts = defaultdict(int)
    u_limit, depth_limit = (4, 2) if smoke else (10, 5)
    for u, R, rho in product(range(u_limit + 1), range(1, depth_limit + 1),
                              (Fraction(1, 4), Fraction(1, 2), Fraction(3, 4))):
        true = u * rho ** (u - 1) if u else Fraction()
        polynomial = sum(((j + 1) * (rho - 1) ** j * math.comb(u, j + 1)
                          for j in range(R) if j + 1 <= u), Fraction())
        bound = ((R + 1) * (1 - rho) ** R * math.comb(u, R + 1) if R + 1 <= u else Fraction())
        require(abs(true - polynomial) <= bound and (-1) ** R * (true - polynomial) >= 0,
                failures, 'finite_taylor_positive_bound', u=u, R=R, rho=rho)
        counts['taylor_cases'] += 1
    crt_records = []
    original = ((3, 5, 7), (11, 13, 17))
    full_product = math.prod(p for group in original for p in group)
    for H in ((2,) if smoke else (2, 6, 10, 30)):
        groups = [tuple(p for p in group if H % p) for group in original]
        normalizers = [sum((Fraction(1, p) for p in group), Fraction()) for group in groups]
        for group, V in zip(groups, normalizers):
            for denominator in ('p', 'p_minus_1'):
                weights = [Fraction(1, p if denominator == 'p' else p - 1) for p in group]
                M = sum(weights, Fraction())
                require(M <= 1, failures, 'finite_reciprocal_mass_base', H=H, group=group, denominator=denominator)
                for R in range(1, depth_limit + 1):
                    for rho in (Fraction(1, 4), Fraction(1, 2), Fraction(3, 4)):
                        retained_mass = sum(((degree * (1 - rho) ** (degree - 1) / V) *
                                             sum((math.prod(row) for row in combinations(weights, degree)), Fraction())
                                             for degree in range(1, R + 1)), Fraction())
                        retained_upper = sum((degree * (1 - rho) ** (degree - 1) * M ** degree /
                                              (V * math.factorial(degree)) for degree in range(1, R + 1)), Fraction())
                        error_mass = (R + 1) * (1 - rho) ** R / V * sum(
                            (math.prod(row) for row in combinations(weights, R + 1)), Fraction())
                        error_upper = (R + 1) * (1 - rho) ** R * M ** (R + 1) / (V * math.factorial(R + 1))
                        require(retained_mass <= retained_upper and error_mass <= error_upper,
                                failures, 'author_normalized_reciprocal_Taylor_mass', H=H, group=group,
                                denominator=denominator, R=R, rho=rho)
                        counts['normalized_reciprocal_Taylor_mass_cases'] += 1
        retained = []
        for active_copies in ((0,), (1,), (0, 1)):
            for chosen in product(*(groups[j] for j in active_copies)):
                d = math.prod(chosen)
                phi = math.prod(p - 1 for p in chosen)
                reduced = [a for a in range(d) if math.gcd(a, d) == 1]
                satisfying = [a for a in reduced if all((H - a) % p == 0 for p in chosen)]
                probability = Fraction(len(satisfying), len(reduced))
                require(len(satisfying) == 1 and probability == Fraction(1, phi) ==
                        math.prod(Fraction(1, p - 1) for p in chosen), failures,
                        'retained_modulus_CRT_probability', H=H, chosen=chosen)
                require(math.gcd(H, d) == 1 and d < full_product and d <= 17 ** len(active_copies),
                        failures, 'retained_modulus_bound', H=H, d=d, chosen=chosen)
                coefficient = math.prod(1 / normalizers[j] for j in active_copies)
                retained.append({'copies': active_copies, 'chosen': chosen, 'd': d, 'coefficient': coefficient,
                                 'probability': probability, 'reduced_residue': satisfying[0]})
                counts['retained_CRT_moduli'] += 1
        crt_records.append({'H': H, 'punctured_groups': groups, 'retained_depth': 1,
                            'full_six_prime_product_not_used': full_product,
                            'max_retained_modulus': max(row['d'] for row in retained), 'retained': retained})
    unit_residues = [a for a in range(3) if math.gcd(a, 3) == 1]
    bad_probability = Fraction(sum((6 - a) % 3 == 0 for a in unit_residues), len(unit_residues))
    require(bad_probability == 0 and bad_probability != Fraction(1, 3 - 1), failures,
            'unpunctured_H_prime_negative_control')
    return {'counts': dict(counts), 'crt_records': crt_records,
            'negative_control': {'H': 6, 'retained_prime_if_not_punctured': 3,
                                  'actual_probability': bad_probability, 'incorrect_reduced_class_probability': Fraction(1, 2)}}


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
    source_hash = hashlib.sha256((directory / 'statement.md').read_bytes()).hexdigest()
    if source_hash != FROZEN_STATEMENT_SHA256:
        raise SystemExit('Frozen statement hash mismatch.')
    packet = json.loads(args.packet.read_text(encoding='utf-8-sig'))
    if packet['step']['id'] != 'finite-check' or not packet.get('upstream'):
        raise SystemExit('Actual populated finite-check packet required.')
    started = time.perf_counter()
    failures = []
    comparisons = {'prime_model_and_complex_cauchy': model_checks(args.smoke, failures),
                   'finite_taylor_and_reduced_CRT': taylor_crt_checks(args.smoke, failures)}
    result = {'mode': 'smoke' if args.smoke else 'bounded_final', 'passed': not failures,
              'runtime_seconds': time.perf_counter() - started, 'python': platform.python_version(),
              'platform': platform.platform(), 'code_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'statement_sha256': source_hash, 'packet_sha256': hashlib.sha256(args.packet.read_bytes()).hexdigest(),
              'comparisons': comparisons, 'failures': failures,
              'scope': 'Exact finite local models, positive-measure algebra and retained CRT classes only; no actual-prime asymptotic or Goldbach certification.'}
    if not args.smoke:
        (directory / 'finite-results.json').write_text(json.dumps(result, indent=2, default=encode) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2, default=encode))
    return 0 if not failures else 1


if __name__ == '__main__':
    raise SystemExit(main())
