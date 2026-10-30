"""Prepared exact determinant-H projective-root checks for ROOTS-008."""
from __future__ import annotations

import argparse
from collections import Counter
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
FROZEN_STATEMENT_SHA256 = '42d72d988c7e82e71b2de7a901b5bb17708a7e61053017fc1fbf46c340b89dcf'
ARITHMETIC_HELPER_SHA256 = '498798fd996b211cf5d1f1b3bea47b101fcc720061d9b2133c1a9d5df92e28af'
ARITHMETIC = None


def arithmetic_helper():
    global ARITHMETIC
    if ARITHMETIC is None:
        path = Path(__file__).resolve().parent.parent / 'complement-ratios-20261029/ratio_checks.py'
        if hashlib.sha256(path.read_bytes()).hexdigest() != ARITHMETIC_HELPER_SHA256:
            raise RuntimeError('Frozen exact arithmetic helper changed.')
        spec = importlib.util.spec_from_file_location('roots008_frozen_arithmetic', path)
        module = importlib.util.module_from_spec(spec)
        previous = sys.dont_write_bytecode
        sys.dont_write_bytecode = True
        try:
            spec.loader.exec_module(module)
        finally:
            sys.dont_write_bytecode = previous
        ARITHMETIC = module
    return ARITHMETIC


def prime_factors(n):
    result = []
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            result.append(divisor)
            while n % divisor == 0:
                n //= divisor
        divisor += 1
    if n > 1:
        result.append(n)
    return result


def phi(n):
    return sum(math.gcd(value, n) == 1 for value in range(n))


def line_from_row(u, c, p):
    """Kernel vector (c,-u), normalized to (1,t) or (0,1)."""
    u, c = u % p, c % p
    if u == c == 0:
        raise ValueError('Zero row has a two-dimensional kernel, not a projective line.')
    if c:
        return (1, -u * pow(c, -1, p) % p)
    return (0, 1)


def all_lines(p):
    return [(0, 1)] + [(1, t) for t in range(p)]


def prescription(u, c, s):
    return tuple(line_from_row(u, c, p) for p in prime_factors(s))


def key_text(key):
    return '|'.join(f'{a},{b}' for a, b in key)


def decode_prescription(s, key):
    q = r = 1
    rho = 0
    for p, line in zip(prime_factors(s), key):
        if line == (1, 0):
            q *= p
            continue
        x, y = line
        assert y % p != 0
        target = -x * pow(y, -1, p) % p
        step = (target - rho) * pow(r, -1, p) % p
        rho += r * step
        r *= p
    assert q * r == s and 0 <= rho < r
    return q, r, rho


def satisfies_reduced_prescription(u, c, q, r, rho):
    return u % q == 0 and math.gcd(u, r) == 1 and (c - rho * u) % r == 0


def ceiling(value):
    return -((-value.numerator) // value.denominator)


def progression_count(left, right, residue, modulus):
    return ceiling((right - residue) / modulus) - ceiling((left - residue) / modulus)


def canonical_c_mass(u, r, rho, interval):
    assert math.gcd(u, r) == 1
    left, right = interval[0] * u, interval[1] * u
    candidates = [c for c in range(u) if left <= c < right and (c - rho * u) % r == 0]
    direct = sum(math.gcd(c, u) == 1 for c in candidates)
    expanded = 0
    nonzero_divisors = 0
    for e in range(1, u + 1):
        if u % e:
            continue
        mu_e = arithmetic_helper().mobius(e)
        nonzero_divisors += mu_e != 0
        residue = 0 if r == 1 else e * (rho * u * pow(e, -1, r) % r)
        expanded += mu_e * progression_count(left, right, residue, e * r)
    center = (interval[1] - interval[0]) * Fraction(phi(u), r)
    return direct, expanded, center, nonzero_divisors, candidates


def canonical_matrix(h, u, v):
    assert math.gcd(u, v) == 1
    c = -h * pow(v, -1, u) % u
    d = (h + v * c) // u
    assert 0 <= c < u and h + v * c == u * d
    return u, c, v, d


def algebra_checks(max_h, max_u, max_v, failures):
    cases = local_cases = 0
    entry_zero_counts = Counter()
    entry_zero_witnesses = {}
    for h in range(2, max_h + 1, 2):
        for u in range(2, max_u + 1):
            for v in range(1, max_v + 1):
                if math.gcd(u, v) != 1 or math.gcd(u * v, h) != 1:
                    continue
                u0, c, v0, d = canonical_matrix(h, u, v)
                cases += 1
                if u0 * d - v0 * c != h or math.gcd(u0, c) != 1:
                    failures.append({'type': 'canonical_matrix', 'H': h, 'u': u, 'v': v})
                for p in [3, 5, 7]:
                    if h % p == 0:
                        continue
                    local_cases += 1
                    kernel = line_from_row(u0, c, p)
                    if (u0 * kernel[0] + c * kernel[1]) % p:
                        failures.append({'type': 'local_projective_kernel', 'H': h, 'p': p, 'u': u, 'v': v})
                    if u0 * d - v0 * c == 0 or (u0 * d - v0 * c) % p == 0:
                        failures.append({'type': 'local_invertibility', 'H': h, 'p': p})
                    for name, value in [('u', u0), ('c_H', c), ('v', v0), ('d_H', d)]:
                        if value % p == 0:
                            entry_zero_counts[name] += 1
                            entry_zero_witnesses.setdefault(name, {'H': h, 'p': p,
                                'matrix': [[u0, c], [v0, d]], 'kernel': list(kernel)})
                    if u0 % p == 0 and (c % p == 0 or kernel != (1, 0)):
                        failures.append({'type': 'p_divides_u_horizontal_kernel', 'H': h, 'p': p, 'u': u, 'v': v})
    omitted_unit_matrix = canonical_matrix(2, 2, 1)
    if math.gcd(omitted_unit_matrix[0], omitted_unit_matrix[1]) == 1:
        failures.append({'type': 'omitted_unit_first_row_primitivity_witness'})
    omitted_gcd_cases = 0
    horizontal = 0
    for u in range(2, max_u + 1):
        for v in range(1, max_v + 1):
            if math.gcd(u, v) != 1 or math.gcd(u * v, 6) != 1:
                continue
            _, c, _, _ = canonical_matrix(6, u, v)
            omitted_gcd_cases += 1
            horizontal += line_from_row(u, c, 3) == (1, 0)
    if horizontal:
        failures.append({'type': 'omitted_gcd_S_H_horizontal_witness'})
    return {'canonical_matrix_cases': cases, 'local_kernel_cases': local_cases,
        'zero_entry_counts': dict(entry_zero_counts), 'zero_entry_witnesses': entry_zero_witnesses,
        'omitted_unit_first_coordinate': {'H': 2, 'u': 2, 'v': 1,
            'matrix': [[omitted_unit_matrix[0], omitted_unit_matrix[1]], [omitted_unit_matrix[2], omitted_unit_matrix[3]]],
            'first_row_gcd': math.gcd(omitted_unit_matrix[0], omitted_unit_matrix[1])},
        'omitted_coprime_S_H_witness': {'H': 6, 'S': 3, 'prescribed_line': [1, 0],
            'tested_admitted_positions': omitted_gcd_cases, 'actual_horizontal_count': horizontal,
            'reason': 'u is a unit modulo H, hence nonzero modulo3; a horizontal kernel would require u=0 modulo3.'}}


def complete_matrix_checks(max_h, moduli, failures):
    records = []
    matrix_cases = prescription_cases = 0
    for s in moduli:
        primes = prime_factors(s)
        all_prescriptions = list(product(*(all_lines(p) for p in primes)))
        for h in range(2, max_h + 1, 2):
            if math.gcd(s, h) != 1:
                continue
            counter = Counter()
            for u in range(s):
                for c in range(s):
                    if math.gcd(u, c, s) != 1:
                        continue
                    key = prescription(u, c, s)
                    for v in range(s):
                        for d in range(s):
                            if (u * d - v * c - h) % s == 0:
                                matrix_cases += 1
                                counter[key] += 1
            expected_total = s ** 3 * math.prod(Fraction(p * p - 1, p * p) for p in primes)
            expected_each = s * phi(s)
            if sum(counter.values()) != expected_total:
                failures.append({'type': 'complete_determinant_matrix_total', 'S': s, 'H': h})
            for key in all_prescriptions:
                prescription_cases += 1
                if counter[key] != expected_each:
                    failures.append({'type': 'complete_projective_line_density', 'S': s, 'H': h, 'prescription': key_text(key), 'count': counter[key]})
            records.append({'S': s, 'H': h, 'matrix_count': sum(counter.values()),
                'prescriptions': len(all_prescriptions), 'count_each': expected_each,
                'uniform_probability': str(Fraction(1, len(all_prescriptions)))})
    return {'records': records, 'matrix_cases': matrix_cases,
        'prescription_cases': prescription_cases,
        'assurance': 'Complete finite residue counts only; no real-box asymptotic is inferred.'}


RATIO_INTERVALS = ((Fraction(0), Fraction(1)), (Fraction(0), Fraction(1, 3)),
    (Fraction(1, 3), Fraction(2, 3)), (Fraction(2, 3), Fraction(1)),
    (Fraction(1, 4), Fraction(3, 4)))


def in_interval(value, interval):
    return interval[0] <= value < interval[1]


def box_checks(max_h, moduli, smoke, failures):
    records = []
    u_scales = [2] if smoke else [2, 3]
    v_scales = [2] if smoke else [2, 3, 5]
    normalized_boxes = [((Fraction(1), Fraction(16)), (Fraction(1), Fraction(2)))]
    if not smoke:
        normalized_boxes.append(((Fraction(1), Fraction(4)), (Fraction(1), Fraction(3, 2))))
    aggregate_cases = partition_cases = local_cases = line_reduction_cases = 0
    mass_cache = {}
    max_error_scale = {'ratio': 0.0}
    for h in range(2, max_h + 1, 2):
        for s in moduli:
            if math.gcd(s, h) != 1:
                continue
            all_prescriptions = list(product(*(all_lines(p) for p in prime_factors(s))))
            for u_scale in u_scales:
                for v_scale in v_scales:
                    for i1, i2 in normalized_boxes:
                        points = []
                        for u in range(u_scale, 16 * u_scale):
                            if not in_interval(Fraction(u, u_scale), i1):
                                continue
                            for v in range(v_scale, 2 * v_scale):
                                if not in_interval(Fraction(v, v_scale), i2) or math.gcd(u, v) != 1 or math.gcd(u * v, h) != 1:
                                    continue
                                _, c, _, _ = canonical_matrix(h, u, v)
                                points.append((u, v, c, Fraction(c, u)))
                        counters = []
                        totals = []
                        for key in all_prescriptions:
                            q, r, rho = decode_prescription(s, key)
                            for u, v, c, ratio in points:
                                line_reduction_cases += 1
                                if (prescription(u, c, s) == key) != satisfies_reduced_prescription(u, c, q, r, rho):
                                    failures.append({'type': 'Q_R_line_reduction', 'H': h, 'S': s, 'u': u, 'c': c, 'prescription': key_text(key)})
                            for u in range(u_scale, 16 * u_scale):
                                if not in_interval(Fraction(u, u_scale), i1) or u % q or math.gcd(u, h * r) != 1:
                                    continue
                                for interval in RATIO_INTERVALS:
                                    cache_key = (u, r, rho, interval)
                                    if cache_key not in mass_cache:
                                        direct, expanded, center, divisor_count, _ = canonical_c_mass(u, r, rho, interval)
                                        if direct != expanded or abs(direct - center) > divisor_count:
                                            failures.append({'type': 'canonical_c_mobius_mass', 'u': u, 'R': r, 'rho': rho, 'interval': [str(x) for x in interval]})
                                        mass_cache[cache_key] = {'u': u, 'R': r, 'rho': rho,
                                            'I3': [str(x) for x in interval], 'A_u': direct,
                                            'exact_mobius_sum': expanded, 'center_L3_phi_over_R': str(center),
                                            'rounding_error_bound': divisor_count}
                        for i3 in RATIO_INTERVALS:
                            counter = Counter()
                            unweighted = 0
                            for u, v, c, ratio in points:
                                if not in_interval(ratio, i3):
                                    continue
                                unweighted += 1
                                local_cases += 1
                                counter[prescription(u, c, s)] += 1
                            aggregate_cases += 1
                            if sum(counter[key] for key in all_prescriptions) != unweighted:
                                failures.append({'type': 'aggregate_root_prescriptions', 'H': h, 'S': s, 'U': u_scale, 'V': v_scale})
                            counters.append(counter)
                            totals.append(unweighted)
                            kappa_approx = 6 / math.pi ** 2 * math.prod((p - 1) / (p + 1) for p in prime_factors(h))
                            main_approx = u_scale * v_scale * float((i1[1] - i1[0]) * (i2[1] - i2[0]) * (i3[1] - i3[0])) * kappa_approx / len(all_prescriptions)
                            eta = Fraction(1, 16)
                            scale = (2 ** len(prime_factors(h))) * (u_scale ** float(Fraction(7, 4) + eta) + v_scale) * math.log(2 * u_scale) ** 2
                            for key in all_prescriptions:
                                error_ratio = abs(counter[key] - main_approx) / scale
                                if error_ratio > max_error_scale['ratio']:
                                    max_error_scale = {'ratio': error_ratio, 'H': h, 'S': s, 'U': u_scale, 'V': v_scale,
                                        'I3': [str(x) for x in i3], 'prescription': key_text(key), 'eta': str(eta)}
                        for key in all_prescriptions:
                            partition_cases += 1
                            if counters[0][key] != sum(counters[j][key] for j in [1, 2, 3]):
                                failures.append({'type': 'ratio_interval_partition', 'H': h, 'S': s, 'prescription': key_text(key)})
                        records.append({'H': h, 'S': s, 'U': u_scale, 'V': v_scale,
                            'I1': [str(x) for x in i1], 'I2': [str(x) for x in i2],
                            'ratio_interval_totals': totals,
                            'counts_by_prescription': [{key_text(key): count for key, count in counter.items()} for counter in counters]})
    return {'records': records, 'aggregate_interval_cases': aggregate_cases,
        'prescription_partition_cases': partition_cases, 'root_assignment_cases': local_cases,
        'Q_R_line_reduction_cases': line_reduction_cases,
        'canonical_c_mass_cases': len(mass_cache), 'canonical_c_mass_records': list(mass_cache.values()),
        'max_candidate_asymptotic_error_scale_ratio_diagnostic': max_error_scale,
        'ratio_intervals': [[str(a), str(b)] for a, b in RATIO_INTERVALS],
        'endpoint_convention': 'Author half-open intervals, including the rational1/3 and2/3 boundaries.',
        'assurance': 'Finite exact aggregation, Mobius masses and ratio counts. Candidate asymptotic error-scale ratios are numerical diagnostics, not proof of a uniform error constant or exponent.'}


def double_fourier_checks(max_h, failures):
    arithmetic = arithmetic_helper()
    cases = j_zero_cases = h_zero_nonzero_j_cases = empty_interval_cases = gcd_cases = 0
    first_nonzero_h_zero_term = None
    intervals = ((Fraction(0), Fraction(1)),
                 (Fraction(1, 3), Fraction(2, 3)),
                 (Fraction(1, 3), Fraction(1, 3)))
    for h_target in range(2, min(max_h, 6) + 1, 2):
        for s in [3, 5]:
            if math.gcd(h_target, s) != 1:
                continue
            for key in product(*(all_lines(p) for p in prime_factors(s))):
                q, r, rho = decode_prescription(s, key)
                for u in range(2, 9):
                    if u % q or math.gcd(u, h_target * r) != 1:
                        continue
                    for interval in intervals:
                        a_u, expanded, center, divisor_count, c_values = canonical_c_mass(u, r, rho, interval)
                        if a_u != expanded:
                            failures.append({'type': 'double_fourier_A_u_input', 'u': u, 'R': r})
                        fhat = []
                        for h_frequency in range(u):
                            raw = [0] * u
                            for c in c_values:
                                raw[-h_frequency * c % u] += 1
                            fhat.append(arithmetic.residue(raw, u))
                        for b, mu_b in arithmetic.rad_divisors(h_target):
                            left, right = Fraction(2, b), Fraction(4, b)
                            w_values = list(range(ceiling(left), ceiling(right)))
                            empty_interval_cases += not w_values
                            a_b = -h_target * pow(b, -1, u) % u
                            if math.gcd(b, u * s) != 1 or math.gcd(a_b, u) != 1:
                                failures.append({'type': 'double_fourier_unit_coefficient', 'H': h_target, 'b': b, 'u': u})
                            ghat = []
                            for j in range(u):
                                raw = [0] * u
                                for w in w_values:
                                    raw[-j * w % u] += 1
                                ghat.append(arithmetic.residue(raw, u))
                            direct = sum(w * c % u == a_b for c in c_values for w in w_values)
                            total, j_zero, h_zero_nonzero_j = [0], [0], [0]
                            for h_frequency in range(u):
                                for j in range(u):
                                    gcd_cases += 1
                                    if math.gcd(h_frequency, j * a_b, u) != math.gcd(h_frequency, j, u):
                                        failures.append({'type': 'double_fourier_complete_gcd', 'u': u, 'j': j, 'h': h_frequency})
                                    value = arithmetic.multiply(fhat[h_frequency], ghat[j], u)
                                    value = arithmetic.multiply(value, arithmetic.kloosterman(u, h_frequency, j * a_b), u)
                                    total = arithmetic.residue(arithmetic.add(total, value), u)
                                    if j == 0:
                                        j_zero = arithmetic.residue(arithmetic.add(j_zero, value), u)
                                    if h_frequency == 0 and j:
                                        h_zero_nonzero_j_cases += 1
                                        h_zero_nonzero_j = arithmetic.residue(arithmetic.add(h_zero_nonzero_j, value), u)
                            cases += 1
                            j_zero_cases += 1
                            if total != [u * u * direct] or j_zero != [u * len(w_values) * a_u]:
                                failures.append({'type': 'double_fourier_pair_identity', 'H': h_target, 'S': s, 'u': u,
                                    'b': b, 'I3': [str(x) for x in interval], 'direct': direct,
                                    'fourier_numerator': total, 'j_zero_numerator': j_zero})
                            if first_nonzero_h_zero_term is None and h_zero_nonzero_j != [0]:
                                first_nonzero_h_zero_term = {'H': h_target, 'S': s, 'prescription': key_text(key),
                                    'u': u, 'b': b, 'I3': [str(x) for x in interval],
                                    'h_zero_nonzero_j_numerator': h_zero_nonzero_j,
                                    'pair_count': direct, 'integer_w_count': len(w_values), 'A_u': a_u}
    if first_nonzero_h_zero_term is None:
        failures.append({'type': 'missing_h_zero_nonzero_j_witness'})
    return {'exact_pair_count_cases': cases, 'exact_j_zero_cases': j_zero_cases,
        'h_zero_nonzero_j_terms': h_zero_nonzero_j_cases, 'complete_gcd_cases': gcd_cases,
        'empty_w_intervals': empty_interval_cases,
        'nonzero_h_zero_j_boundary_witness': first_nonzero_h_zero_term,
        'method': 'Exact integer cyclotomic arithmetic from the frozen RATIOS-007 helper; no prior files changed.'}


def author_specific_checks():
    if not AUTHOR_STATEMENT_INSTANTIATED:
        raise RuntimeError('Preparation only: final frozen statement and populated packet are pending.')
    statement = Path(__file__).with_name('statement.md')
    actual = hashlib.sha256(statement.read_bytes()).hexdigest()
    if actual != FROZEN_STATEMENT_SHA256:
        raise RuntimeError('Frozen author statement changed.')
    packet_path = Path(__file__).resolve().parents[3] / '.runs/goldbach-roots-008-manual-20261029/packets/finite-check.json'
    packet = json.loads(packet_path.read_text(encoding='utf-8'))
    if any(upstream['result'] is None for upstream in packet['upstream']):
        raise RuntimeError('Dependent packet lacks its frozen statement result.')
    return {'statement_sha256': actual, 'arithmetic_helper_sha256': ARITHMETIC_HELPER_SHA256,
        'actual_formulas': 'Half-open canonical determinant-H roots; Q/R reduction; canonical-c Mobius masses; complete local line density; exact double Fourier including both zero-frequency boundaries.'}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--smoke', action='store_true')
    parser.add_argument('--output', type=Path, default=Path(__file__).with_name('finite-results.json'))
    args = parser.parse_args()
    author = author_specific_checks()
    started = time.perf_counter()
    failures = []
    max_h, max_u, max_v = (6, 8, 8) if args.smoke else (20, 30, 20)
    moduli = [3, 5] if args.smoke else [3, 5, 7, 15]
    result = {'status': 'running', 'python': platform.python_version(), 'platform': platform.platform(),
        'processor': platform.processor() or 'unknown', 'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'author_input': author}
    result['canonical_matrices'] = algebra_checks(max_h, max_u, max_v, failures)
    result['complete_residue_counts'] = complete_matrix_checks(min(max_h, 12), moduli, failures)
    result['finite_boxes'] = box_checks(max_h, moduli, args.smoke, failures)
    result['double_fourier'] = double_fourier_checks(2 if args.smoke else 6, failures)
    result['failures'] = failures
    result['status'] = 'passed_exact_root_checks' if not failures else 'failed_exact_root_checks'
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
