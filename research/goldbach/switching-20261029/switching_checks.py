"""Independent finite identities and scoped switching-coefficient certificates."""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import platform
import time

BETAS = (Fraction(1, 8), Fraction(1, 6), Fraction(1, 5))
ALPHAS = (Fraction(3, 10), Fraction(8, 25), Fraction(33, 100))


def prime_tables(limit):
    spf = list(range(limit + 1))
    for p in range(2, math.isqrt(limit) + 1):
        if spf[p] == p:
            for n in range(p * p, limit + 1, p):
                if spf[n] == n:
                    spf[n] = p
    omega = [0] * (limit + 1)
    for n in range(2, limit + 1):
        omega[n] = 1 + omega[n // spf[n]]
    primes = [p for p in range(2, limit + 1) if spf[p] == p]
    return spf, omega, primes


def trial_factors(n):
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


def exact_cutoff(n, exponent):
    target = n ** exponent.numerator
    low, high = 0, n + 1
    while high - low > 1:
        middle = (low + high) // 2
        if middle ** exponent.denominator <= target:
            low = middle
        else:
            high = middle
    assert low ** exponent.denominator <= target < (low + 1) ** exponent.denominator
    return low


def finite_identities(limit, failures):
    spf, omega, primes = prime_tables(limit)
    exponents = BETAS + ALPHAS
    pair_cases = parity_cases = trial_cases = 0
    q_equals_r = repeated = dividing_n = 0
    first_q_equals_r = first_repeated = first_dividing_n = None
    max_c = {'count': 0}
    for n in range(6, limit + 1, 2):
        cutoffs = {str(e): exact_cutoff(n, e) for e in exponents}
        u = {str(e): 0 for e in exponents}
        e_count = {str(e): 0 for e in ALPHAS}
        f = {str(e): 0 for e in ALPHAS}
        for p in primes:
            if p >= n - 1:
                break
            q = n - p
            for exponent in exponents:
                key = str(exponent)
                if spf[q] > cutoffs[key]:
                    u[key] += 1
            for exponent in ALPHAS:
                key = str(exponent)
                if spf[q] > cutoffs[key]:
                    e_count[key] += omega[q] == 2
                    f[key] += omega[q] % 2 == 1
                    if omega[q] > 3:
                        failures.append({'type': 'alpha_classification', 'N': n, 'alpha': key, 'q': q})
        # Independent switching enumeration factors q first, and tests p afterwards.
        c = {}
        for r in primes:
            if r > max(cutoffs[str(a)] for a in ALPHAS):
                break
            count = 0
            for m in range(1, (n - 2) // r + 1):
                if m != 1 and spf[m] < r:
                    continue
                p = n - r * m
                if p < 2 or spf[p] != p:
                    continue
                count += 1
                witness = {'N': n, 'r': r, 'm': m, 'p': p, 'q': r * m}
                if m == 1:
                    q_equals_r += 1
                    if first_q_equals_r is None:
                        first_q_equals_r = witness
                if m % r == 0:
                    repeated += 1
                    if first_repeated is None:
                        first_repeated = witness
                if n % r == 0:
                    dividing_n += 1
                    if p != r:
                        failures.append({'type': 'dividing_target_exception', **witness})
                    if first_dividing_n is None:
                        first_dividing_n = witness
            c[r] = count
            if count > max_c['count']:
                max_c = {'N': n, 'r': r, 'count': count}
        for beta in BETAS:
            for alpha in ALPHAS:
                lower, upper = cutoffs[str(beta)], cutoffs[str(alpha)]
                removed = sum(count for r, count in c.items() if lower < r <= upper)
                pair_cases += 1
                if u[str(alpha)] != u[str(beta)] - removed:
                    failures.append({'type': 'switching_identity', 'N': n, 'beta': str(beta), 'alpha': str(alpha),
                        'U_alpha': u[str(alpha)], 'U_beta': u[str(beta)], 'removed': removed})
        for alpha in ALPHAS:
            key = str(alpha)
            parity_cases += 1
            if f[key] != u[key] - e_count[key]:
                failures.append({'type': 'parity_identity', 'N': n, 'alpha': key, 'F': f[key], 'U': u[key], 'E': e_count[key]})
        if n <= 100:
            direct_u = {str(e): 0 for e in exponents}
            direct_c = {}
            for p in range(2, n - 1):
                if len(trial_factors(p)) != 1:
                    continue
                factors = trial_factors(n - p)
                if not factors:
                    continue
                for exponent in exponents:
                    key = str(exponent)
                    if factors[0] > cutoffs[key]:
                        direct_u[key] += 1
                if factors[0] <= max(cutoffs[str(a)] for a in ALPHAS):
                    direct_c[factors[0]] = direct_c.get(factors[0], 0) + 1
            trial_cases += 1
            if direct_u != u or any(direct_c.get(r, 0) != count for r, count in c.items()):
                failures.append({'type': 'trial_division_cross_check', 'N': n,
                    'direct_U': direct_u, 'table_U': u, 'direct_C': direct_c, 'switching_C': c})
    return {'range_even_N': [6, limit], 'beta_values': [str(b) for b in BETAS],
        'alpha_values': [str(a) for a in ALPHAS], 'switching_identity_cases': pair_cases,
        'parity_identity_cases': parity_cases, 'independent_trial_cross_checks': trial_cases,
        'C_r_q_equals_r_occurrences': q_equals_r, 'C_r_repeated_factor_occurrences': repeated,
        'C_r_dividing_target_occurrences': dividing_n,
        'first_q_equals_r': first_q_equals_r, 'first_repeated_factor': first_repeated,
        'first_dividing_target': first_dividing_n, 'max_C_r': max_c,
        'method': 'Exact rational-power integer roots, independent least-factor enumeration q=r*m, SPF primality, separate direct trial division through N=100.'}


def log_enclosure(x, terms=50):
    """Exact rational enclosure using the atanh series and geometric tail."""
    assert x > 0
    y = (x - 1) / (x + 1)
    power = y
    total = Fraction(0)
    for j in range(terms):
        total += 2 * power / (2 * j + 1)
        power *= y * y
    tail = 2 * abs(y) ** (2 * terms + 1) / ((2 * terms + 1) * (1 - y * y))
    return total - tail, total + tail


def simpson(function, lo, hi, intervals):
    assert intervals % 2 == 0
    h = (hi - lo) / intervals
    weighted = function(lo) + function(hi)
    weighted += 4 * sum(function(lo + h * j) for j in range(1, intervals, 2))
    weighted += 2 * sum(function(lo + h * j) for j in range(2, intervals, 2))
    return h * weighted / 3


def coefficient_checks(failures):
    # The lower term and integrated upper term have these coefficients in the
    # basis log(beta), log(d-beta), log(alpha), log(d-alpha), after multiplying by d/2.
    lower = {'log(beta)': -1, 'log(d-beta)': 1, 'log(alpha)': 0, 'log(d-alpha)': 0}
    integral = {'log(beta)': -1, 'log(d-beta)': 1, 'log(alpha)': 1, 'log(d-alpha)': -1}
    difference = {name: lower[name] - integral[name] for name in lower}
    expected = {'log(beta)': 0, 'log(d-beta)': 0, 'log(alpha)': -1, 'log(d-alpha)': 1}
    if difference != expected:
        failures.append({'type': 'symbolic_beta_cancellation'})
    # Exact endpoint inequalities certify the entire scoped family, independently of grid samples.
    d_max, alpha_min = Fraction(1, 2), Fraction(3, 10)
    x_upper = d_max / alpha_min - 1
    log_upper = x_upper - 1
    universal_coefficient_upper = 2 / d_max * log_upper
    assert x_upper == Fraction(2, 3)
    assert log_upper == Fraction(-1, 3)
    assert universal_coefficient_upper == Fraction(-4, 3)
    concrete_d, concrete_alpha, concrete_beta = Fraction(49, 100), Fraction(3, 10), Fraction(1, 5)
    concrete_lower_argument = (concrete_d - concrete_beta) / concrete_beta
    concrete_integral_argument = concrete_alpha * (concrete_d - concrete_beta) / (concrete_beta * (concrete_d - concrete_alpha))
    concrete_margin_argument = concrete_lower_argument / concrete_integral_argument
    concrete_rational_upper = 2 / concrete_d * (concrete_margin_argument - 1)
    assert concrete_lower_argument == Fraction(29, 20)
    assert concrete_integral_argument == Fraction(87, 38)
    assert concrete_margin_argument == Fraction(19, 30)
    assert concrete_rational_upper == Fraction(-220, 147)
    records = []
    max_quad_error = {'absolute_error': 0.0}
    ds = (Fraction(7, 20), Fraction(2, 5), Fraction(9, 20), Fraction(49, 100), Fraction(1, 2))
    ratios = (Fraction(1, 4), Fraction(1, 3), Fraction(2, 5), Fraction(49, 100))
    for d in ds:
        for alpha in ALPHAS:
            for ratio in ratios:
                beta = d * ratio
                assert d / 4 <= beta < d / 2 < alpha < d
                lower_s = d / beta
                assert 2 < lower_s <= 4
                # Piecewise legal cutoff is checked exactly at both sides of its sole breakpoint.
                for t in {beta, alpha, min(alpha, max(beta, d / 3))}:
                    cutoff = min(t, (d - t) / 2)
                    parameter = (d - t) / cutoff
                    assert 2 <= parameter <= 3
                    assert Fraction(2) / (parameter * cutoff * t) == Fraction(2) / (t * (d - t))
                d_float, a_float, b_float = float(d), float(alpha), float(beta)
                lower_value = 2 * math.log(d_float / b_float - 1) / d_float
                def integrand(t):
                    cutoff = min(t, (d_float - t) / 2)
                    parameter = (d_float - t) / cutoff
                    scaled_upper_sieve = 2 / parameter
                    return scaled_upper_sieve / (cutoff * t)
                coarse = simpson(integrand, b_float, a_float, 2000)
                fine = simpson(integrand, b_float, a_float, 4000)
                numerical_margin = lower_value - fine
                exact_x = (d - alpha) / alpha
                closed = 2 * math.log(float(exact_x)) / d_float
                low_log, high_log = log_enclosure(exact_x)
                low_margin, high_margin = 2 * low_log / d, 2 * high_log / d
                if high_margin >= 0:
                    failures.append({'type': 'rational_negativity', 'd': str(d), 'alpha': str(alpha)})
                error = abs(numerical_margin - closed)
                if error > 1e-8 * max(1, abs(closed)):
                    failures.append({'type': 'coefficient_quadrature', 'd': str(d), 'alpha': str(alpha), 'beta': str(beta), 'error': error})
                if error > max_quad_error['absolute_error']:
                    max_quad_error = {'absolute_error': error, 'd': str(d), 'alpha': str(alpha), 'beta': str(beta)}
                records.append({'d': str(d), 'alpha': str(alpha), 'beta': str(beta),
                    'lower_s': str(lower_s), 'closed_coefficient': closed, 'numerical_coefficient': numerical_margin,
                    'coarse_fine_integral_difference': abs(coarse - fine),
                    'rational_enclosure_lower': str(low_margin), 'rational_enclosure_upper': str(high_margin),
                    'negative_certified': high_margin < 0, 'd_half_is_algebraic_boundary_only': d == Fraction(1, 2)})
    certificate = {'scope': {'d': 'alpha<d<=1/2; source analytic use requires d<1/2',
        'alpha': '3/10<=alpha<1/3', 'beta': 'd/4<=beta<d/2'},
        'conditional_imports': 'Uses exactly the proposed linear-sieve coefficient formulas and legal cutoff density; does not certify their analytic application or error sums.',
        'legal_cutoff': 'u(t)=min(t,(d-t)/2)',
        'effective_upper_integrand': 'exp(-gamma)F((d-t)/u(t))/(u(t)*t)=2/[t(d-t)]',
        'symbolic_lower_basis_coefficients_times_d_over_2': lower,
        'symbolic_integral_basis_coefficients_times_d_over_2': integral,
        'symbolic_difference_times_d_over_2': difference,
        'closed_coefficient': '(2/d)*log((d-alpha)/alpha)',
        'universal_sign_certificate': {'x_positive': 'd>alpha', 'x_upper': str(x_upper),
            'inequality': 'log(x)<=x-1<=-1/3', 'coefficient_upper': str(universal_coefficient_upper),
            'conclusion': 'coefficient<=-4/3<0 throughout the scoped family, independently of beta'},
        'concrete_author_case': {'d': str(concrete_d), 'alpha': str(concrete_alpha), 'beta': str(concrete_beta),
            'lower_log_argument': str(concrete_lower_argument), 'integral_log_argument': str(concrete_integral_argument),
            'quotient_margin_log_argument': str(concrete_margin_argument), 'rational_coefficient_upper': str(concrete_rational_upper),
            'numerical_coefficient': float(2 / concrete_d) * math.log(float(concrete_margin_argument))},
        'rational_log_certificate_method': 'log(x)=2*sum_{j>=0}y^(2j+1)/(2j+1), y=(x-1)/(x+1); 50 terms and exact geometric tail bound',
        'grid_records': records}
    diagnostic = {'cases': len(records), 'all_rational_upper_bounds_negative': all(r['negative_certified'] for r in records),
        'max_quadrature_error': max_quad_error, 'simpson_subdivisions': [2000, 4000], 'numerical_relative_tolerance': 1e-8,
        'beta_scan_limitation': 'The universal conclusion comes from symbolic cancellation and rational inequalities; the scan is a diagnostic only.'}
    return diagnostic, certificate


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--limit', type=int, default=5000)
    parser.add_argument('--output', type=Path, default=Path(__file__).with_name('finite-results.json'))
    parser.add_argument('--certificate', type=Path, default=Path(__file__).with_name('coefficient-certificate.json'))
    args = parser.parse_args()
    started = time.perf_counter()
    failures = []
    output = {'status': 'running', 'python': platform.python_version(), 'platform': platform.platform(),
        'processor': platform.processor() or 'unknown', 'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    output['finite_identities'] = finite_identities(args.limit, failures)
    diagnostic, certificate = coefficient_checks(failures)
    output['coefficient_diagnostics'] = diagnostic
    output['failures'] = failures
    output['status'] = 'passed_scoped_checks' if not failures else 'failed_scoped_checks'
    output['elapsed_seconds'] = time.perf_counter() - started
    output['inference_tokens'] = 'unknown'
    output['monetary_cost'] = 'unknown'
    args.output.write_text(json.dumps(output, indent=2) + '\n', encoding='utf-8')
    args.certificate.write_text(json.dumps(certificate, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'status': output['status'], 'seconds': output['elapsed_seconds'], 'failures': len(failures),
        'output': str(args.output.resolve()), 'certificate': str(args.certificate.resolve())}))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
