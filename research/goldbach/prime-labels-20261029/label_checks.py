"""Exact finite support, reconstruction and padding checks for LABELS-005."""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
from itertools import product
import json
import math
from pathlib import Path
import platform
import time

RHOS = (Fraction(1, 2), Fraction(2, 3), Fraction(3, 4))


def factors(n):
    result = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            result.append(d)
            n //= d
        d += 1
    if n > 1:
        result.append(n)
    return result


def mobius(n):
    fs = factors(n)
    return 0 if len(fs) != len(set(fs)) else (-1) ** len(fs)


def liouville(n):
    return (-1) ** len(factors(n))


def weight(n, groups, rho, distinct=True):
    fs = factors(n)
    relevant = set(fs) if distinct else fs
    answer = Fraction(1)
    for group in groups:
        mass = sum((Fraction(1, p) for p in group), Fraction(0))
        assert mass > 0
        count = sum(p in group for p in relevant)
        if count == 0:
            return Fraction(0)
        answer *= count * rho ** (count - 1) / mass
    return answer


def support_checks(limit, failures):
    groups = ({2, 3}, {5, 7}, {11, 13})
    z = 13
    rough_cases = 0
    for q in range(2, limit + 1):
        fs = factors(q)
        if fs[0] > z:
            for rho in RHOS:
                rough_cases += 1
                if weight(q, groups, rho) != 0:
                    failures.append({'type': 'small_group_rough_support', 'q': q, 'rho': str(rho)})
    capacity_cases = 0
    capacity_examples = []
    for cutoff, primes in ((2, [3, 5, 7, 11]), (3, [5, 7, 11, 13]), (5, [7, 11, 13, 17])):
        for k in range(1, 5):
            chosen = tuple({p} for p in primes[:k])
            maximum_n = cutoff ** k
            for q in range(1, maximum_n + 1):
                capacity_cases += 1
                if weight(q, chosen, Fraction(2, 3)) != 0:
                    failures.append({'type': 'group_capacity', 'z': cutoff, 'K': k, 'N': maximum_n, 'q': q})
            first_possible = math.prod(primes[:k])
            actual = weight(first_possible, chosen, Fraction(2, 3))
            if not first_possible > maximum_n or actual <= 0:
                failures.append({'type': 'group_capacity_boundary', 'z': cutoff, 'K': k})
            capacity_examples.append({'z': cutoff, 'K': k, 'N': maximum_n,
                'first_product_witness': first_possible, 'weight_at_product': str(actual)})
    # Distinct omega differs from total multiplicity already for 4 at rho=2/3.
    repeated_q, repeated_groups, repeated_rho = 4, ({2, 3},), Fraction(2, 3)
    distinct_value = weight(repeated_q, repeated_groups, repeated_rho)
    multiplicity_value = weight(repeated_q, repeated_groups, repeated_rho, distinct=False)
    if distinct_value == multiplicity_value:
        failures.append({'type': 'distinct_vs_total_witness'})
    return {'small_groups': [sorted(g) for g in groups], 'rough_cutoff': z,
        'rough_q_range': [2, limit], 'exact_rough_weight_cases': rough_cases,
        'rough_mean_square_error_from_one': '1 whenever the tested rough set is nonempty, since every source weight is exactly zero',
        'capacity_cases': capacity_cases, 'capacity_examples': capacity_examples,
        'distinct_vs_total_witness': {'q': repeated_q, 'group': [2, 3], 'rho': str(repeated_rho),
            'distinct_omega': 1, 'Omega': 2, 'source_weight': str(distinct_value),
            'incorrect_multiplicity_weight': str(multiplicity_value)}}


def solve_rational(matrix, target):
    size = len(matrix)
    augmented = [[Fraction(value) for value in row] + [Fraction(target[i])]
                 for i, row in enumerate(matrix)]
    for column in range(size):
        pivot = next(i for i in range(column, size) if augmented[i][column])
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        divisor = augmented[column][column]
        augmented[column] = [x / divisor for x in augmented[column]]
        for row in range(size):
            if row == column:
                continue
            multiple = augmented[row][column]
            augmented[row] = [a - multiple * b for a, b in zip(augmented[row], augmented[column])]
    return [row[-1] for row in augmented]


def reconstruction_checks(failures):
    # Diagnostic interpolants use a different rho grid from the final author.
    # The final author's coefficients are checked separately below.
    alphabet = (17, 19, 23)
    matrix = [[k * rho ** (k - 1) for rho in RHOS] for k in [1, 2, 3]]
    interpolants = {name: solve_rational(matrix, target) for name, target in
        {'odd': [1, 0, 1], 'liouville': [-1, 1, -1], 'prime': [1, 0, 0]}.items()}
    total_types = squarefree_types = 0
    first_repeated_failures = {}
    records = []
    for multiplicities in product(range(4), repeat=3):
        degree = sum(multiplicities)
        if degree not in (1, 2, 3):
            continue
        total_types += 1
        q = math.prod(p ** exponent for p, exponent in zip(alphabet, multiplicities))
        support = sum(exponent > 0 for exponent in multiplicities)
        squarefree = max(multiplicities) <= 1
        squarefree_types += squarefree
        # Explicit Omega-polynomials reconstruct all admissible multiplicity types.
        odd_polynomial = (degree - 2) ** 2
        lambda_polynomial = 1 - 2 * (degree - 2) ** 2
        prime_polynomial = Fraction((degree - 2) * (degree - 3), 2)
        truth = {'odd': degree % 2, 'liouville': (-1) ** degree, 'prime': int(degree == 1)}
        polynomial = {'odd': odd_polynomial, 'liouville': lambda_polynomial, 'prime': prime_polynomial}
        if polynomial != truth:
            failures.append({'type': 'Omega_polynomial', 'multiplicities': multiplicities})
        reconstructed = {name: sum(coefficient * support * rho ** (support - 1)
            for coefficient, rho in zip(coefficients, RHOS))
            for name, coefficients in interpolants.items()}
        for name in truth:
            if squarefree and reconstructed[name] != truth[name]:
                failures.append({'type': 'squarefree_label_reconstruction', 'name': name, 'q': q})
            if not squarefree and reconstructed[name] != truth[name] and name not in first_repeated_failures:
                first_repeated_failures[name] = {'q': q, 'multiplicities': list(multiplicities),
                    'Omega': degree, 'distinct_support': support,
                    'label_reconstruction': str(reconstructed[name]), 'true_value': truth[name]}
        records.append({'multiplicities': list(multiplicities), 'q': q, 'Omega': degree,
            'squarefree': squarefree, 'reconstruction': {k: str(v) for k, v in reconstructed.items()}, 'truth': truth})
    # Source normalization is exactly recoverable: coefficients for W=profile/V are V times those above.
    mass = sum((Fraction(1, p) for p in alphabet), Fraction(0))
    for degree in [1, 2, 3]:
        q = math.prod(alphabet[:degree])
        for name, coefficients in interpolants.items():
            value = sum(mass * coefficient * weight(q, (set(alphabet),), rho)
                for coefficient, rho in zip(coefficients, RHOS))
            expected = {'odd': degree % 2, 'liouville': (-1) ** degree, 'prime': int(degree == 1)}[name]
            if value != expected:
                failures.append({'type': 'normalized_label_interpolation', 'degree': degree, 'name': name})
    radical_witness = []
    for exponent in [1, 2, 3]:
        q = alphabet[0] ** exponent
        values = [weight(q, (set(alphabet),), rho) for rho in RHOS]
        if len(set(values)) != 1 or values[0] != 1 / mass:
            failures.append({'type': 'radical_invariance', 'q': q})
        radical_witness.append({'q': q, 'Omega': exponent, 'distinct_support': 1,
            'source_weights_at_all_three_rhos': [str(v) for v in values],
            'liouville': liouville(q), 'prime_indicator': int(exponent == 1)})
    author_rhos = (Fraction(1, 4), Fraction(1, 2), Fraction(3, 4))
    prime_coefficients = (Fraction(3), Fraction(-3), Fraction(1))
    odd_coefficients = (Fraction(17, 3), Fraction(-25, 3), Fraction(11, 3))
    author_type_checks = []
    for record in records:
        q, degree = record['q'], record['Omega']
        support = sum(exponent > 0 for exponent in record['multiplicities'])
        squarefree = record['squarefree']
        profiles = tuple(support * rho ** (support - 1) for rho in author_rhos)
        bare_prime = sum(c * h for c, h in zip(prime_coefficients, profiles))
        bare_phi = sum(c * h for c, h in zip(odd_coefficients, profiles))
        z_cells = tuple(mobius(q) * h for h in profiles)
        prime_reconstruction = -sum(c * z_value for c, z_value in zip(prime_coefficients, z_cells))
        odd_squarefree_reconstruction = -sum(c * z_value for c, z_value in zip(odd_coefficients, z_cells))
        expected_r = int(degree == 1)
        expected_e0 = int(degree == 2 and squarefree)
        expected_h0 = int(degree == 3 and squarefree)
        true_f = degree % 2
        square_indicator = int(degree == 2 and not squarefree)
        repeated_two_prime_indicator = int(degree == 3 and support == 2)
        if squarefree and (bare_prime != expected_r or bare_phi != true_f):
            failures.append({'type': 'author_bare_squarefree_formula', 'q': q})
        if prime_reconstruction != expected_r or odd_squarefree_reconstruction != true_f * int(squarefree):
            failures.append({'type': 'author_mu_reconstruction', 'q': q})
        if bare_phi != true_f + square_indicator - repeated_two_prime_indicator:
            failures.append({'type': 'author_bare_phi_corrections', 'q': q})
        for rho, z_value in zip(author_rhos, z_cells):
            if z_value != -expected_r + 2 * rho * expected_e0 - 3 * rho ** 2 * expected_h0:
                failures.append({'type': 'author_signed_cell_formula', 'q': q, 'rho': str(rho)})
        if z_cells[1] != mobius(q) + Fraction(expected_h0, 4):
            failures.append({'type': 'author_half_deweighting_signed', 'q': q})
        y_half = mobius(q) ** 2 * profiles[1]
        if y_half != int(squarefree) - Fraction(expected_h0, 4):
            failures.append({'type': 'author_half_deweighting_unsigned', 'q': q})
        author_type_checks.append({'q': q, 'Omega': degree, 'distinct_support': support,
            'squarefree': squarefree, 'bare_prime_interpolant': str(bare_prime),
            'bare_phi': str(bare_phi), 'mu_prime_reconstruction': str(prime_reconstruction),
            'mu_odd_squarefree_reconstruction': str(odd_squarefree_reconstruction),
            'Z_profiles': [str(z_value) for z_value in z_cells],
            'half_unsigned_weight': str(y_half)})
    profile_maxima = [max(k * rho ** (k - 1) for k in [1, 2, 3]) for rho in author_rhos]
    weighted_sup_cost = sum(abs(c) * value for c, value in zip(odd_coefficients, profile_maxima))
    if profile_maxima != [Fraction(1), Fraction(1), Fraction(27, 16)] or weighted_sup_cost != Fraction(323, 16):
        failures.append({'type': 'author_norm_cost'})
    return {'prime_alphabet': list(alphabet), 'admissible_multiplicity_types': total_types,
        'squarefree_types': squarefree_types, 'rho_values': [str(rho) for rho in RHOS],
        'rational_profile_interpolants': {name: [str(c) for c in coefficients] for name, coefficients in interpolants.items()},
        'profile_coefficient_l1_norms': {name: str(sum(abs(c) for c in coefficients)) for name, coefficients in interpolants.items()},
        'source_normalized_coefficient_l1_norms': {name: str(mass * sum(abs(c) for c in coefficients)) for name, coefficients in interpolants.items()},
        'reciprocal_prime_mass': str(mass), 'first_repeated_failures': first_repeated_failures,
        'radical_invariance_witness': radical_witness,
        'author_formulas_A1_through_A7': {'rho_values': [str(rho) for rho in author_rhos],
            'bare_prime_coefficients': [str(c) for c in prime_coefficients],
            'bare_odd_coefficients': [str(c) for c in odd_coefficients],
            'prime_coefficient_l1': str(sum(abs(c) for c in prime_coefficients)),
            'odd_coefficient_l1': str(sum(abs(c) for c in odd_coefficients)),
            'profile_sup_norms': [str(v) for v in profile_maxima],
            'odd_coefficient_weighted_sup_cost': str(weighted_sup_cost),
            'type_records': author_type_checks},
        'records': records, 'scope': 'The label profile depends on distinct support size. Equality with Omega reconstruction is asserted only for squarefree q. The explicit Omega polynomial itself works on every type of total degree<=3.'}


def padding_checks(failures):
    groups = ({2, 3}, {5, 7})
    ds = (10, 30)
    qs = (17, 19, 17 ** 2, 17 * 19)
    identity_cases = weight_cases = mixture_cases = normalized_cases = zero_cases = 0
    zero_witness = None
    for rho in RHOS:
        for d in ds:
            assert mobius(d) != 0
            for q in qs + (17 ** 3, 17 ** 2 * 19):
                assert math.gcd(d, q) == 1
                identity_cases += 1
                if mobius(d * q) != mobius(d) * mobius(q) or liouville(d * q) != liouville(d) * liouville(q):
                    failures.append({'type': 'padding_sign', 'D': d, 'q': q})
                weight_cases += 1
                if weight(d * q, groups, rho) != weight(d, groups, rho):
                    failures.append({'type': 'padding_label', 'D': d, 'q': q, 'rho': str(rho)})
        w1, w2 = (weight(d, groups, rho) for d in ds)
        raw_mixtures = ((Fraction(1), Fraction(0)), (w2 + 1, w1), (w2, w1))
        mixtures = tuple(tuple(g / sum(row) for g in row) for row in raw_mixtures)
        for coefficients in product((-1, 0, 1), repeat=len(qs)):
            for gamma in mixtures:
                for sign_name, sign in [('mobius', mobius), ('liouville', liouville)]:
                    original = sum(c * sign(q) for c, q in zip(coefficients, qs))
                    normalizer = sum(g * sign(d) * weight(d, groups, rho) for g, d in zip(gamma, ds))
                    padded = sum(g * sum(c * sign(d * q) * weight(d * q, groups, rho)
                        for c, q in zip(coefficients, qs)) for g, d in zip(gamma, ds))
                    mixture_cases += 1
                    if padded != normalizer * original:
                        failures.append({'type': 'padding_mixture', 'rho': str(rho), 'sign': sign_name})
                    if normalizer:
                        normalized_cases += 1
                        if padded / normalizer != original:
                            failures.append({'type': 'normalized_padding_mixture'})
                    else:
                        zero_cases += 1
                        if padded != 0:
                            failures.append({'type': 'zero_normalizer_padding'})
                        if original != 0 and zero_witness is None:
                            zero_witness = {'rho': str(rho), 'D_values': list(ds),
                                'padding_coefficients': [str(g) for g in gamma],
                                'q_values': list(qs), 'original_coefficients': list(coefficients),
                                'sign_function': sign_name, 'normalizer': str(normalizer),
                                'padded_sum': str(padded), 'original_sum': original}
    mobius_counterexample = None
    for d in range(2, 31):
        if mobius(d) == 0:
            continue
        for q in range(2, 31):
            if math.gcd(d, q) > 1 and mobius(d * q) != mobius(d) * mobius(q):
                candidate = {'D': d, 'q': q, 'mu_Dq': mobius(d * q), 'mu_D_times_mu_q': mobius(d) * mobius(q)}
                if mobius_counterexample is None or (d * q, d, q) < (mobius_counterexample['D'] * mobius_counterexample['q'], mobius_counterexample['D'], mobius_counterexample['q']):
                    mobius_counterexample = candidate
    lambda_unrestricted_cases = 0
    for d in range(1, 31):
        for q in range(1, 31):
            lambda_unrestricted_cases += 1
            if liouville(d * q) != liouville(d) * liouville(q):
                failures.append({'type': 'liouville_complete_multiplicativity', 'D': d, 'q': q})
    # Coprimality alone does not forbid a new label prime from appearing in q.
    separated_group = ({2, 3},)
    wrong_weight = {'D': 2, 'q': 3, 'rho': '2/3', 'coprime': True,
        'W_D': str(weight(2, separated_group, Fraction(2, 3))),
        'W_Dq': str(weight(6, separated_group, Fraction(2, 3)))}
    if wrong_weight['W_D'] == wrong_weight['W_Dq'] or zero_witness is None:
        failures.append({'type': 'required_counterexample_missing'})
    return {'coprime_sign_identity_cases': identity_cases, 'group_separated_weight_cases': weight_cases,
        'mixture_cases': mixture_cases, 'normalized_mixture_cases': normalized_cases,
        'zero_normalizer_cases': zero_cases, 'zero_normalizer_with_nonzero_original': zero_witness,
        'smallest_mobius_noncoprime_counterexample': mobius_counterexample,
        'unrestricted_liouville_cases': lambda_unrestricted_cases,
        'coprime_but_not_group_separated_weight_counterexample': wrong_weight,
        'scope': 'These are exact finite checks of multiplicativity and scalar transfer. Zero normalizer implies no conclusion about the original sum.'}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--support-limit', type=int, default=5000)
    parser.add_argument('--output', type=Path, default=Path(__file__).with_name('finite-results.json'))
    args = parser.parse_args()
    started = time.perf_counter()
    failures = []
    result = {'status': 'running', 'python': platform.python_version(), 'platform': platform.platform(),
        'processor': platform.processor() or 'unknown', 'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    result['support'] = support_checks(args.support_limit, failures)
    result['reconstruction'] = reconstruction_checks(failures)
    result['padding'] = padding_checks(failures)
    result['failures'] = failures
    result['status'] = 'passed_exact_algebra' if not failures else 'failed_exact_algebra'
    result['elapsed_seconds'] = time.perf_counter() - started
    result['inference_tokens'] = 'unknown'
    result['monetary_cost'] = 'unknown'
    args.output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'status': result['status'], 'seconds': result['elapsed_seconds'],
        'failures': len(failures), 'output': str(args.output.resolve())}))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
