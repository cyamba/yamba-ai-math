"""Prepared exact Kloosterman, inverse-interval and ratio checks for RATIOS-007."""
from __future__ import annotations

import argparse
import cmath
from collections import Counter, defaultdict
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import platform
import time

AUTHOR_STATEMENT_INSTANTIATED = True
FROZEN_STATEMENT_SHA256 = 'dbd7f89da164cf2dba56a9b6ef877d083e936d3caee912e70390218e0a6a6699'


def trim(polynomial):
    while len(polynomial) > 1 and polynomial[-1] == 0:
        polynomial.pop()
    return polynomial


def add(a, b):
    result = [0] * max(len(a), len(b))
    for i, coefficient in enumerate(a):
        result[i] += coefficient
    for i, coefficient in enumerate(b):
        result[i] += coefficient
    return trim(result)


def subtract(a, b):
    return add(a, [-coefficient for coefficient in b])


def divide(dividend, divisor):
    remainder = trim(list(dividend))
    assert divisor[-1] == 1
    quotient = [0] * max(1, len(remainder) - len(divisor) + 1)
    while len(remainder) >= len(divisor) and remainder != [0]:
        degree = len(remainder) - len(divisor)
        coefficient = remainder[-1]
        quotient[degree] += coefficient
        for i, value in enumerate(divisor):
            remainder[i + degree] -= coefficient * value
        trim(remainder)
    return trim(quotient), remainder


CYCLOTOMIC = {1: [-1, 1]}
K_CACHE = {}


def cyclotomic(m):
    if m not in CYCLOTOMIC:
        polynomial = [-1] + [0] * (m - 1) + [1]
        for d in range(1, m):
            if m % d == 0:
                polynomial, remainder = divide(polynomial, cyclotomic(d))
                assert remainder == [0]
        CYCLOTOMIC[m] = polynomial
    return CYCLOTOMIC[m]


def residue(polynomial, m):
    return divide(polynomial, cyclotomic(m))[1]


def multiply(a, b, m):
    polynomial = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            polynomial[i + j] += x * y
    return residue(polynomial, m)


def units(m):
    return [x for x in range(m) if math.gcd(x, m) == 1]


def phi(m):
    return len(units(m))


def factors(m):
    out = []
    d = 2
    while d * d <= m:
        while m % d == 0:
            out.append(d)
            m //= d
        d += 1
    if m > 1:
        out.append(m)
    return out


def mobius(m):
    fs = factors(m)
    return 0 if len(fs) != len(set(fs)) else (-1) ** len(fs)


def rad_divisors(m):
    terms = [(1, 1)]
    for p in sorted(set(factors(m))):
        terms += [(d * p, -sign) for d, sign in list(terms)]
    return terms


def tau3(m):
    return math.prod((exponent + 1) * (exponent + 2) // 2 for exponent in Counter(factors(m)).values())


def kloosterman(m, h, k):
    key = (m, h % m, k % m)
    if key not in K_CACHE:
        polynomial = [0] * m
        for x in units(m):
            polynomial[(h * x + k * pow(x, -1, m)) % m] += 1
        K_CACHE[key] = residue(polynomial, m)
    return K_CACHE[key]


def ramanujan(m, k):
    common = math.gcd(m, k)
    return sum(d * mobius(m // d) for d in range(1, common + 1) if common % d == 0)


def complete_checks(max_modulus, failures):
    records = []
    orbit_cases = elimination_cases = kernel_input_cases = 0
    for m in range(2, max_modulus + 1):
        unit_values = units(m)
        inverses = {x: pow(x, -1, m) for x in unit_values}
        pair_classes = defaultdict(list)
        for x1 in unit_values:
            for x2 in unit_values:
                pair_classes[((x1 + x2) % m, (inverses[x1] + inverses[x2]) % m)].append((x1, x2))
        collisions = sum(len(pairs) ** 2 for pairs in pair_classes.values())
        for pairs in pair_classes.values():
            for x1, x2 in pairs:
                for x3, x4 in pairs:
                    elimination_cases += 1
                    if (x1 + x2) * (x3 - x1) * (x3 - x2) % m:
                        failures.append({'type': 'collision_elimination', 'm': m, 'quadruple': [x1, x2, x3, x4]})
        fibers = Counter()
        for x1 in range(m):
            for x2 in range(m):
                for x3 in range(m):
                    kernel_input_cases += 1
                    fibers[((x1 + x2) % m, (x3 - x1) % m, (x3 - x2) % m)] += 1
        max_fiber = max(fibers.values())
        product_triples = sum(math.gcd(a * b, m) for a in range(m) for b in range(m))
        if max_fiber != math.gcd(2, m) or max_fiber > 2 or collisions > 2 * product_triples or product_triples > m * m * tau3(m):
            failures.append({'type': 'collision_count_bound', 'm': m})
        moment = [0]
        for h in range(m):
            for k in range(m):
                value = kloosterman(m, h, k)
                conjugate = kloosterman(m, -h, -k)
                norm_squared = multiply(value, conjugate, m)
                moment = residue(add(moment, multiply(norm_squared, norm_squared, m)), m)
                orbit = {(a * h % m, pow(a, -1, m) * k % m) for a in unit_values}
                expected_orbit = phi(m // math.gcd(h, k, m))
                orbit_cases += 1
                if len(orbit) != expected_orbit or any(kloosterman(m, hh, kk) != value for hh, kk in orbit):
                    failures.append({'type': 'unit_scaling_orbit', 'm': m, 'h': h, 'k': k})
        expected_moment = [m * m * collisions]
        if moment != expected_moment:
            failures.append({'type': 'complete_fourth_moment', 'm': m, 'actual': moment, 'expected': expected_moment})
        for k in range(m):
            if kloosterman(m, 0, k) != [ramanujan(m, k)]:
                failures.append({'type': 'ramanujan_divisor_formula', 'm': m, 'k': k})
        records.append({'m': m, 'unit_count': len(unit_values), 'collision_count': collisions,
            'complete_fourth_moment': moment[0] if len(moment) == 1 else moment,
            'max_linear_map_fiber': max_fiber, 'product_divisibility_triples': product_triples,
            'tau3': tau3(m), 'collision_upper': 2 * m * m * tau3(m)})
    return {'modulus_range': [2, max_modulus], 'records': records,
        'unit_orbit_cases': orbit_cases, 'collision_elimination_cases': elimination_cases,
        'linear_map_input_cases': kernel_input_cases,
        'method': 'Exact integer cyclotomic arithmetic and finite collision/orbit enumeration.'}


def raw_inverse_interval(m, coefficient, lower, upper):
    polynomial = [0] * m
    for w in range(lower, upper + 1):
        if math.gcd(w, m) == 1:
            polynomial[(coefficient * pow(w, -1, m)) % m] += 1
    return trim(polynomial)


def interval_completion(m, coefficient, lower, upper):
    total = [0]
    for h in range(m):
        fourier_indicator = [0] * m
        for w in range(lower, upper + 1):
            fourier_indicator[(-h * w) % m] += 1
        total = residue(add(total, multiply(residue(fourier_indicator, m), kloosterman(m, h, coefficient), m)), m)
    return total


def incomplete_checks(max_h, max_u, max_v, ks, failures):
    cases = completion_cases = divisor_terms = long_divisor_cases = empty_divisor_cases = shared_frequency_cases = 0
    records = []
    max_error_ratio = {'ratio': 0.0}
    for h in range(2, max_h + 1, 2):
        terms = rad_divisors(h)
        phi_ratio = sum((Fraction(sign, d) for d, sign in terms), Fraction(0))
        if phi_ratio != Fraction(phi(h), h):
            failures.append({'type': 'coprime_divisor_density', 'H': h})
        for u in range(2, max_u + 1):
            if math.gcd(u, h) != 1:
                continue
            for v_scale in range(2, max_v + 1):
                for k in ks:
                    direct = [0] * u
                    for v in range(v_scale, 2 * v_scale + 1):
                        if math.gcd(v, u * h) == 1:
                            direct[(-k * h * pow(v, -1, u)) % u] += 1
                    expanded = [0]
                    for d, sign in terms:
                        divisor_terms += 1
                        long_divisor_cases += d > v_scale
                        coefficient = -k * h * pow(d, -1, u)
                        if math.gcd(coefficient, u) != math.gcd(k, u):
                            failures.append({'type': 'moving_multiplier_gcd', 'H': h, 'u': u, 'd': d, 'k': k})
                        lower, upper = (v_scale + d - 1) // d, 2 * v_scale // d
                        empty_divisor_cases += lower > upper
                        inner = raw_inverse_interval(u, coefficient, lower, upper)
                        expanded = add(expanded, [sign * x for x in inner])
                        if h <= 10 and u <= 10 and v_scale <= 4 and k == 1:
                            completion_cases += 1
                            completed = interval_completion(u, coefficient, lower, upper)
                            if completed != residue([u * x for x in inner], u):
                                failures.append({'type': 'exact_interval_completion', 'H': h, 'u': u, 'd': d, 'V': v_scale})
                    cases += 1
                    if trim(list(direct)) != trim(list(expanded)) or residue(direct, u) != residue(expanded, u):
                        failures.append({'type': 'incomplete_coprime_expansion', 'H': h, 'u': u, 'V': v_scale, 'k': k})
                    center = Fraction(v_scale, u) * phi_ratio * ramanujan(u, k)
                    shared_frequency_cases += math.gcd(k, u) > 1
                    numerical_sum = sum(coefficient * cmath.exp(2j * math.pi * exponent / u)
                                        for exponent, coefficient in enumerate(direct))
                    c_u = (2 * tau3(u) * u / phi(u)) ** Fraction(1, 4)
                    scale = len(terms) * c_u * u ** 0.75 * math.gcd(k, u) ** 0.25 * math.log(2 * u)
                    error_ratio = abs(numerical_sum - float(center)) / scale
                    if error_ratio > max_error_ratio['ratio']:
                        max_error_ratio = {'ratio': error_ratio, 'H': h, 'u': u, 'V': v_scale, 'k': k}
                    records.append({'H': h, 'u': u, 'V': v_scale, 'k': k,
                        'exact_cyclotomic_sum': residue(direct, u), 'author_fixed_u_center': str(center),
                        'numerical_error_scale_ratio_diagnostic': error_ratio})
    no_unit = {'u': 2, 'H': 2, 'k': 1,
        'complete_actual': kloosterman(2, 0, -2), 'claimed_unit_center': ramanujan(2, 1)}
    if no_unit['complete_actual'] == [no_unit['claimed_unit_center']]:
        failures.append({'type': 'missing_unit_counterexample'})
    different_h = {'u': 3, 'H_values': [2, 4], 'interval_v': [1, 2], 'k': 1}
    values = []
    for h in different_h['H_values']:
        raw = [0] * 3
        for v in range(1, 3):
            if math.gcd(v, 3 * h) == 1:
                raw[(-h * pow(v, -1, 3)) % 3] += 1
        values.append(residue(raw, 3))
    different_h['exact_sums'] = values
    if values[0] == values[1]:
        failures.append({'type': 'same_gcd_incomplete_sums_counterexample'})
    filtered, unfiltered = [0] * 3, [0] * 3
    for v in range(2, 5):
        if math.gcd(v, 3) == 1:
            exponent = -2 * pow(v, -1, 3) % 3
            unfiltered[exponent] += 1
            if math.gcd(v, 2) == 1:
                filtered[exponent] += 1
    if residue(filtered, 3) != [0] or residue(unfiltered, 3) != [-1]:
        failures.append({'type': 'omitted_v_coprimality_witness'})
    return {'cases': cases, 'exact_completion_cases': completion_cases,
        'divisor_terms': divisor_terms, 'terms_with_d_above_V': long_divisor_cases,
        'empty_divisor_intervals': empty_divisor_cases,
        'frequency_cases_with_nonunit_k': shared_frequency_cases,
        'max_fixed_u_error_scale_ratio_diagnostic': max_error_ratio,
        'records': records, 'omitted_unit_H_witness': no_unit,
        'same_gcd_does_not_mean_equal_incomplete_sum': different_h,
        'omitted_v_coprimality_witness': {'H': 2, 'u': 3, 'V': 2, 'k': 1,
            'filtered_exact_sum': residue(filtered, 3), 'unfiltered_exact_sum': residue(unfiltered, 3)},
        'assurance': 'Exact expansions, completion and coefficient gcds. Numerical error-scale ratios do not certify asymptotic or absolute implied constants.'}


def empirical_discrepancy(ratios):
    if not ratios:
        return {'count': 0, 'grid_discrepancy': None, 'star_discrepancy': None, 'circular_interval_discrepancy': None}
    count = len(ratios)
    ordered = sorted(ratios)
    grid_deviations = [Fraction(sum(theta < Fraction(j, 20) for theta in ratios), count) - Fraction(j, 20) for j in range(21)]
    grid = max(abs(deviation) for deviation in grid_deviations)
    positive = max(Fraction(i, count) - theta for i, theta in enumerate(ordered, 1))
    negative = max(theta - Fraction(i - 1, count) for i, theta in enumerate(ordered, 1))
    star = max(positive, negative)
    circular = positive + negative
    grid_circular = max(grid_deviations) - min(grid_deviations)
    assert grid <= star <= circular <= min(Fraction(1), 2 * star)
    assert grid_circular <= circular
    return {'count': count, 'grid_discrepancy': str(grid), 'star_discrepancy': str(star),
        'grid_circular_interval_discrepancy': str(grid_circular),
        'circular_interval_discrepancy': str(circular)}


def interval_count_multiples(lower, upper, d):
    return upper // d - (lower + d - 1) // d + 1


def exact_mass_checks(h, u_scale, v_scale, actual_count, failures):
    first_width = 15 * u_scale
    phi_ratio = Fraction(phi(h), h)
    weighted_phi_sum = Fraction(0)
    exact_total = 0
    fixed_u_cases = 0
    tau_h = len(rad_divisors(h))
    for u in range(u_scale, 16 * u_scale + 1):
        if math.gcd(u, h) != 1:
            continue
        direct = sum(math.gcd(v, u * h) == 1 for v in range(v_scale, 2 * v_scale + 1))
        expanded = sum(sign * interval_count_multiples(v_scale, 2 * v_scale, d)
                       for d, sign in rad_divisors(u * h))
        center = v_scale * Fraction(phi(u), u) * phi_ratio
        tau_u = sum(u % d == 0 for d in range(1, u + 1))
        if direct != expanded or abs(direct - center) > tau_h * tau_u:
            failures.append({'type': 'exact_fixed_u_mass', 'H': h, 'u': u, 'V': v_scale})
        exact_total += direct
        weighted_phi_sum += Fraction(phi(u), u)
        fixed_u_cases += 1
    expanded_weighted = Fraction(0)
    finite_mu_sum = Fraction(0)
    for d in range(1, 16 * u_scale + 1):
        if math.gcd(d, h) != 1:
            continue
        mu_d = mobius(d)
        count = sum(math.gcd(m, h) == 1 for m in range((u_scale + d - 1) // d, 16 * u_scale // d + 1))
        expanded_weighted += Fraction(mu_d * count, d)
        finite_mu_sum += Fraction(mu_d, d * d)
    if exact_total != actual_count or expanded_weighted != weighted_phi_sum:
        failures.append({'type': 'exact_global_mass_expansion', 'H': h, 'U': u_scale, 'V': v_scale})
    finite_kappa_b = phi_ratio ** 2 * finite_mu_sum
    finite_main = first_width * v_scale * finite_kappa_b
    tail = Fraction(first_width * v_scale, 16 * u_scale) * phi_ratio ** 2
    return {'fixed_u_cases': fixed_u_cases, 'exact_total': exact_total,
        'weighted_phi_sum': str(weighted_phi_sum), 'finite_mobius_sum': str(finite_mu_sum),
        'finite_kappa_b_main': str(finite_main), 'infinite_series_tail_bound': str(tail),
        'assurance': 'Mass and finite Mobius identities are exact. Infinite density approximation and big-O asymptotics are not certified by this finite record.'}


def primitive_ratio_checks(max_h, smoke, ks, failures):
    records = []
    u_values = [2] if smoke else [2, 3]
    v_values = [2, 3] if smoke else [2, 3, 5]
    phase_cases = complement_cases = nonempty_cases = 0
    for h in range(2, max_h + 1, 2):
        for u_scale in u_values:
            for v_scale in v_values:
                ratios = []
                by_u = defaultdict(list)
                for u in range(u_scale, 16 * u_scale + 1):
                    if math.gcd(u, h) != 1:
                        continue
                    for v in range(v_scale, 2 * v_scale + 1):
                        if math.gcd(u, v) != 1 or math.gcd(v, h) != 1:
                            continue
                        complement_c = -pow(v, -1, u)
                        complement_d = (1 + v * complement_c) // u
                        complement_cases += 1
                        if u * complement_d - v * complement_c != 1:
                            failures.append({'type': 'primitive_complement', 'H': h, 'u': u, 'v': v})
                        theta = Fraction(h * complement_c, u) % 1
                        ratios.append(theta)
                        by_u[u].append(v)
                for k in ks:
                    direct_phases = Counter((k * theta) % 1 for theta in ratios)
                    grouped = Counter()
                    for u, vs in by_u.items():
                        raw = [0] * u
                        for v in range(v_scale, 2 * v_scale + 1):
                            if math.gcd(v, u * h) == 1:
                                raw[(-k * h * pow(v, -1, u)) % u] += 1
                        for exponent, coefficient in enumerate(raw):
                            if coefficient:
                                grouped[Fraction(exponent, u)] += coefficient
                    phase_cases += 1
                    if direct_phases != grouped:
                        failures.append({'type': 'primitive_ratio_fixed_u_phase_sum', 'H': h, 'U': u_scale, 'V': v_scale, 'k': k})
                mass_record = exact_mass_checks(h, u_scale, v_scale, len(ratios), failures)
                discrepancy = empirical_discrepancy(ratios)
                nonempty_cases += bool(ratios)
                numerical_fourier = {}
                for k in [1, 2]:
                    value = sum(cmath.exp(2j * math.pi * float((k * theta) % 1)) for theta in ratios)
                    numerical_fourier[k] = abs(value)
                discrepancy_diagnostics = []
                if ratios:
                    for j in [2, 3]:
                        rhs = j ** -0.5 + sum(numerical_fourier[k] / (k * len(ratios)) for k in range(1, j))
                        discrepancy_diagnostics.append({'J': j,
                            'circular_discrepancy_to_rhs_ratio': float(Fraction(discrepancy['circular_interval_discrepancy'])) / rhs})
                records.append({'H': h, 'U': u_scale, 'V': v_scale,
                    'discrepancy': discrepancy, 'exact_mass': mass_record,
                    'discrepancy_bound_scale_diagnostics': discrepancy_diagnostics})
    return {'records': records, 'exact_phase_sum_cases': phase_cases,
        'primitive_complement_cases': complement_cases,
        'nonempty_population_cases': nonempty_cases,
        'assurance': 'Rational phase multisets, mass expansions and empirical discrepancies are exact. Numerical discrepancy-bound scale ratios are diagnostics, not analytic theorem verification.'}


def author_specific_checks():
    if not AUTHOR_STATEMENT_INSTANTIATED:
        raise RuntimeError('Preparation only: final author formulas and populated finite-check packet are pending.')
    statement = Path(__file__).with_name('statement.md')
    actual_hash = hashlib.sha256(statement.read_bytes()).hexdigest()
    if actual_hash != FROZEN_STATEMENT_SHA256:
        raise RuntimeError('Author statement differs from frozen input.')
    packet_path = Path(__file__).resolve().parents[3] / '.runs/goldbach-ratios-007-manual-20261029/packets/finite-check.json'
    packet = json.loads(packet_path.read_text(encoding='utf-8'))
    if any(upstream['result'] is None for upstream in packet['upstream']):
        raise RuntimeError('Dependent packet lacks the completed statement.')
    return {'statement_sha256': actual_hash,
        'actual_formulas_instantiated': 'Complete fourth moment/orbit bound inputs, fixed-u Mobius and finite completion identities, Ramanujan center, common-frequency factors, exact mass expansion and normalized circular discrepancy.'}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--smoke', action='store_true')
    parser.add_argument('--output', type=Path, default=Path(__file__).with_name('finite-results.json'))
    args = parser.parse_args()
    author = author_specific_checks()
    started = time.perf_counter()
    failures = []
    max_modulus, max_h, max_u, max_v = (6, 6, 6, 4) if args.smoke else (18, 20, 16, 8)
    ks = [-1, 1, 3] if args.smoke else [-2, -1, 1, 2, 3]
    result = {'status': 'running', 'python': platform.python_version(), 'platform': platform.platform(),
        'processor': platform.processor() or 'unknown', 'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'author_input': author}
    result['complete_kloosterman'] = complete_checks(max_modulus, failures)
    result['incomplete_inverse'] = incomplete_checks(max_h, max_u, max_v, ks, failures)
    result['primitive_ratios'] = primitive_ratio_checks(max_h, args.smoke, ks, failures)
    result['failures'] = failures
    result['status'] = 'passed_exact_ratio_checks' if not failures else 'failed_exact_ratio_checks'
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
