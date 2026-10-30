"""Independent finite arithmetic checks; no claim about infinite Goldbach."""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import platform
import random
import time

ALPHAS = ((3, 10), (8, 25), (33, 100))
ETAS = (Fraction(3, 2), Fraction(2), Fraction(7, 3), Fraction(5, 2))


def tables(limit):
    spf = list(range(limit + 1))
    for p in range(2, math.isqrt(limit) + 1):
        if spf[p] == p:
            for n in range(p * p, limit + 1, p):
                if spf[n] == n:
                    spf[n] = p
    omega, mu = [0] * (limit + 1), [1] * (limit + 1)
    base = [0] * (limit + 1)
    for n in range(2, limit + 1):
        p, rem = spf[n], n // spf[n]
        omega[n] = omega[rem] + 1
        mu[n] = 0 if rem % p == 0 else -mu[rem]
        if rem == 1 or base[rem] == p:
            base[n] = p
    return spf, omega, mu, base


def trial_factors(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors


def rational_cutoff(n, numerator, denominator):
    target = n ** numerator
    low, high = 0, n + 1
    while high - low > 1:
        mid = (low + high) // 2
        if mid ** denominator <= target:
            low = mid
        else:
            high = mid
    assert low ** denominator <= target < (low + 1) ** denominator
    return low


def factor_from_table(n, spf):
    result = []
    while n > 1:
        result.append(spf[n])
        n //= spf[n]
    return result


def direct_counts(n, z):
    u = liouville = h = r = 0
    for p in range(2, n - 1):
        if len(trial_factors(p)) != 1:
            continue
        factors = trial_factors(n - p)
        if not factors or factors[0] <= z:
            continue
        u += 1
        liouville += (-1) ** len(factors)
        h += len(factors) == 3
        r += len(factors) == 1
    return [u, liouville, h, r]


def rough_checks(limit, failures):
    spf, omega, _, _ = tables(limit)
    primes = [p for p in range(2, limit + 1) if spf[p] == p]
    c2_truncated = math.prod(1 - 1 / (p - 1) ** 2 for p in primes if p > 2)
    records = {f'{a}/{b}': {'alpha': [a, b], 'targets': 0,
               'identity_failures': 0, 'max_omega_survivor': 0,
               'repeated_factor_H_occurrences': 0, 'prime_cube_H_occurrences': 0,
               'positive_H_targets': 0, 'H_total': 0, 'trial_cross_checks': 0,
               'max_H': {'H': -1}, 'max_normalized_ratio': {'ratio': -1}}
               for a, b in ALPHAS}
    for n in range(6, limit + 1, 2):
        cuts = [rational_cutoff(n, a, b) for a, b in ALPHAS]
        counts = [[0, 0, 0, 0] for _ in ALPHAS]
        repeated = [0] * len(ALPHAS)
        cubes = [0] * len(ALPHAS)
        max_omega = [0] * len(ALPHAS)
        for p in primes:
            if p >= n - 1:
                break
            q = n - p
            least = spf[q]
            multiplicity = omega[q]
            for index, z in enumerate(cuts):
                if least <= z:
                    continue
                cell = counts[index]
                cell[0] += 1
                cell[1] += -1 if multiplicity % 2 else 1
                cell[2] += multiplicity == 3
                cell[3] += multiplicity == 1
                max_omega[index] = max(max_omega[index], multiplicity)
                if multiplicity == 3:
                    factors = factor_from_table(q, spf)
                    repeated[index] += len(set(factors)) < 3
                    cubes[index] += factors[0] == factors[-1]
        distinct_n = set(factor_from_table(n, spf))
        sigma = 2 * c2_truncated * math.prod((p - 1) / (p - 2) for p in distinct_n if p > 2)
        for i, (a, b) in enumerate(ALPHAS):
            record = records[f'{a}/{b}']
            u, liouville, h, r = counts[i]
            record['targets'] += 1
            record['max_omega_survivor'] = max(record['max_omega_survivor'], max_omega[i])
            if 2 * r != u - liouville - 2 * h:
                record['identity_failures'] += 1
                failures.append({'type': 'rough_identity', 'N': n, 'alpha': [a, b], 'counts': counts[i]})
            if n <= 200:
                record['trial_cross_checks'] += 1
                direct = direct_counts(n, cuts[i])
                if direct != counts[i]:
                    failures.append({'type': 'trial_cross_check', 'N': n, 'alpha': [a, b], 'direct': direct, 'table': counts[i]})
            record['repeated_factor_H_occurrences'] += repeated[i]
            record['prime_cube_H_occurrences'] += cubes[i]
            record['positive_H_targets'] += h > 0
            record['H_total'] += h
            if h > record['max_H']['H']:
                record['max_H'] = {'N': n, 'H': h, 'cutoff': cuts[i]}
            epsilon = 1 / 3 - a / b
            scale = sigma * n / math.log(n) ** 2 * (epsilon + 1 / math.log(n)) ** 2
            ratio = max(0, h - len(distinct_n)) / scale
            if ratio > record['max_normalized_ratio']['ratio']:
                record['max_normalized_ratio'] = {'N': n, 'ratio': ratio, 'H': h,
                    'omega_N': len(distinct_n), 'cutoff': cuts[i]}
    return {'method': 'smallest-prime-factor table, exact rational-power integer roots; separate trial division through N=200',
            'range_even_N': [6, limit], 'records': records,
            'singular_series_for_empirical_ratios': {'twin_prime_product_truncated_at': limit,
                'product': c2_truncated, 'tail_relative_error_bound': 2 / (limit - 1),
                'note': 'Truncated singular series is an upper approximation. Ratios are descriptive floating-point values; no universal constant is tested.'}}


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def add_product_log(counter, coefficient, prime_base, argument):
    for p in trial_factors(argument):
        counter[tuple(sorted((prime_base, p)))] += coefficient


def normalized(counter):
    return {key: value for key, value in counter.items() if value}


def divisor_swap_checks(limit, failures):
    _, _, mu, base = tables(limit)
    checked = 0
    first_omission = None
    for n_target in range(4, limit + 1):
        for eta in ETAS:
            left, right, dropped = Counter(), Counter(), Counter()
            for n in range(1, n_target):
                if not base[n]:
                    continue
                h = n_target - n
                for d in divisors(h):
                    if d > eta:
                        add_product_log(left, -mu[h] ** 2 * mu[d], base[n], d)
            for k in range(1, n_target):
                if not k * eta < n_target - 1:
                    continue
                for n in range(1, n_target):
                    if not base[n] or (n_target - n) % k:
                        continue
                    coefficient = mu[k] * mu[n_target - n]
                    for dest in ([right, dropped] if n < n_target - eta * k else [dropped]):
                        add_product_log(dest, coefficient, base[n], k)
                        add_product_log(dest, -coefficient, base[n], n_target - n)
            checked += 1
            lnorm, rnorm, dnorm = normalized(left), normalized(right), normalized(dropped)
            if lnorm != rnorm:
                failures.append({'type': 'exact_divisor_swap', 'N': n_target, 'eta': str(eta),
                    'left': repr(lnorm), 'right': repr(rnorm)})
            if first_omission is None and lnorm != dnorm:
                signed = {repr(key): dropped[key] - left[key] for key in dropped.keys() | left.keys()
                          if dropped[key] != left[key]}
                first_omission = {'N': n_target, 'eta': str(eta), 'dropped_minus_correct_formal_log_product_coefficients': signed,
                    'interpretation': 'Each key (r,s) means log(r)*log(s). The recorded positive single monomial log(2)^2 proves the omitted-endpoint identity fails; a general nonzero formal polynomial would require separate analysis.'}
    return {'N_range': [4, limit], 'eta_values': [str(e) for e in ETAS], 'exact_cases': checked,
            'method': 'integer coefficient maps of formal prime-log quadratic monomials',
            'first_omitted_endpoint_counterexample': first_omission}


def phi(k):
    return sum(math.gcd(a, k) == 1 for a in range(1, k + 1))


def endpoint_checks(limit, failures):
    rng = random.Random(20261029)
    checked = 0
    max_ratio = {'ratio': 0}
    for n_target in range(6, limit + 1):
        f = [0] + [rng.randrange(-7, 8) for _ in range(n_target - 1)]
        for eta in ETAS:
            for k in range(1, n_target):
                if math.gcd(k, n_target) != 1 or not eta * k < n_target - 1:
                    continue
                admitted = [n for n in range(1, n_target) if n < n_target - eta * k]
                m = max(admitted, default=0)
                if not m:
                    continue
                ph = phi(k)
                discrepancy = Fraction(0)
                emax = Fraction(0)
                weighted = 0.0
                for n in admitted:
                    coefficient = Fraction(f[n] * (ph if n % k == n_target % k else 0) - f[n], ph)
                    discrepancy += coefficient
                    emax = max(emax, abs(discrepancy))
                    weighted += float(coefficient) * math.log(k / (n_target - n))
                bound = math.log((n_target - 1) / k) * float(emax)
                checked += 1
                excess = abs(weighted) - bound
                if excess > 1e-10 * max(1, bound):
                    failures.append({'type': 'numeric_endpoint_bound', 'N': n_target, 'eta': str(eta),
                        'k': k, 'weighted': weighted, 'bound': bound})
                ratio = abs(weighted) / bound if bound else 0
                if ratio > max_ratio['ratio']:
                    max_ratio = {'ratio': ratio, 'N': n_target, 'eta': str(eta), 'k': k,
                                 'weighted': weighted, 'bound': bound}
    return {'N_range': [6, limit], 'cases': checked, 'seed': 20261029,
            'method': 'exact Fraction partial discrepancies, floating logarithmic weights',
            'relative_tolerance': 1e-10, 'max_ratio': max_ratio,
            'limitation': 'Numerical finite evidence only; the analytic proof must come from Abel summation.'}


def boundary_witnesses(failures):
    # Exact rational discrepancy, with the one nonzero logarithmic weight explicit.
    full_discrepancy = Fraction(1) - Fraction(2, 2)
    moving_discrepancy = Fraction(1) - Fraction(1, 2)
    moving_weighted = -math.log(3) / 2
    bound = math.log(3) / 2
    if full_discrepancy != 0 or moving_discrepancy != Fraction(1, 2):
        failures.append({'type': 'sharpness_witness'})
    cubes = []
    for r in [3, 5, 7, 11, 13, 17, 19, 23]:
        n = r ** 3 + 3
        # alpha=(N-3)/(3N); positive integer powers decide the strict inequality.
        survives = r ** (3 * n) > n ** (n - 3)
        if not survives:
            failures.append({'type': 'adaptive_cube_witness', 'r': r, 'N': n})
        cubes.append({'r': r, 'N': n, 'prime_summand': 3, 'complement': r ** 3,
                      'epsilon': f'1/{n}', 'strict_roughness_exact': survives,
                      'H_lower_bound': 1})
    return {'endpoint_sharpness': {'N': 10, 'k': 3, 'eta': 2,
                'f_nonzero': {'1': 1, '8': 1}, 'full_discrepancy_exact': str(full_discrepancy),
                'moving_discrepancy_exact': str(moving_discrepancy),
                'moving_weighted_value': moving_weighted, 'bound': bound,
                'exact_formula': 'moving weighted discrepancy = -log(3)/2; bound=log(3)/2'},
            'adaptive_epsilon_cube_witnesses': cubes,
            'limitation': 'Finite witnesses illustrate the remainder issue; the asymptotic refutation requires the separate mathematical argument.'}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--limit', type=int, default=20000)
    parser.add_argument('--divisor-limit', type=int, default=160)
    parser.add_argument('--endpoint-limit', type=int, default=90)
    parser.add_argument('--output', type=Path, default=Path(__file__).with_name('finite-results.json'))
    args = parser.parse_args()
    started = time.perf_counter()
    failures = []
    result = {'status': 'running', 'python': platform.python_version(), 'platform': platform.platform(),
              'processor': platform.processor() or 'unknown', 'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    result['rough_counts'] = rough_checks(args.limit, failures)
    result['divisor_swap'] = divisor_swap_checks(args.divisor_limit, failures)
    result['endpoint_transfer'] = endpoint_checks(args.endpoint_limit, failures)
    result['boundary_witnesses'] = boundary_witnesses(failures)
    result['failures'] = failures
    result['status'] = 'passed_finite_checks' if not failures else 'failed_finite_checks'
    result['elapsed_seconds'] = time.perf_counter() - started
    result['inference_token_usage'] = 'unknown'
    result['monetary_cost'] = 'unknown'
    args.output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'status': result['status'], 'seconds': result['elapsed_seconds'],
                      'failures': len(failures), 'output': str(args.output.resolve())}))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
