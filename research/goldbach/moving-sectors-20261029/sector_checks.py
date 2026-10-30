"""Prepared exact moving-sector checks; final author adaptation is required."""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import platform
import time

# Preparation gate. Change only after reading the final author packet and
# instantiating the complement-ratio and quantitative formulas it actually states.
AUTHOR_STATEMENT_INSTANTIATED = True
FROZEN_STATEMENT_SHA256 = '622e03bca08c00023894cfb98c892c7831a8aef6980cf00775aa6d7aa78291f9'


def extended_gcd(a, b):
    old_r, r, old_s, s, old_t, t = a, b, 1, 0, 0, 1
    while r:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    if old_r < 0:
        old_r, old_s, old_t = -old_r, -old_s, -old_t
    return old_r, old_s, old_t


def complement(position):
    u, v = position
    gcd, s, minus_r = extended_gcd(u, v)
    assert gcd == 1
    return (-minus_r, s)


def primitive(position):
    return math.gcd(*position) == 1


def sector(position, h):
    u, v = position
    assert math.gcd(u, h) == 1
    return v * pow(u, -1, h) % h


def forward(position, h, c):
    u, v = position
    assert (v - c * u) % h == 0
    return (u, (v - c * u) // h)


def inverse(position, h, c):
    u, w = position
    return (u, h * w + c * u)


def determinant(p, q):
    return p[0] * q[1] - p[1] * q[0]


def vector_checks(max_h, coordinate_bound, failures):
    position_cases = pair_cases = inverse_cases = both_unit_cases = complement_cases = divisor_cases = 0
    sector_populations = []
    for h in range(2, max_h + 1, 2):
        positions = [(u, v) for u in range(1, coordinate_bound + 1)
            for v in range(coordinate_bound + 1) if primitive((u, v)) and math.gcd(u, h) == 1]
        counts = [0] * h
        for p in positions:
            c = sector(p, h)
            counts[c] += 1
            image = forward(p, h, c)
            position_cases += 1
            if inverse(image, h, c) != p or not primitive(image) or image[0] != p[0]:
                failures.append({'type': 'forward_inverse_primitive', 'H': h, 'P': p, 'c': c})
            if Fraction(image[1], image[0]) != (Fraction(p[1], p[0]) - c) / h:
                failures.append({'type': 'rational_ratio', 'H': h, 'P': p, 'c': c})
            original_complement = complement(p)
            r, s = original_complement
            transformed_complement = (h * r, s - c * r)
            canonical_transformed_complement = complement(image)
            complement_cases += 1
            if determinant(p, original_complement) != 1 or determinant(image, transformed_complement) != 1:
                failures.append({'type': 'integral_complement', 'H': h, 'P': p, 'c': c})
            old_ratio = Fraction(r, p[0]) % 1
            new_ratio = Fraction(canonical_transformed_complement[0], image[0]) % 1
            if new_ratio != (h * old_ratio) % 1:
                failures.append({'type': 'complement_ratio_mod_one', 'H': h, 'P': p, 'c': c})
            for label in [2, 3, 5, 7, 11]:
                if (p[0] % label == 0) != (image[0] % label == 0):
                    failures.append({'type': 'first_coordinate_label', 'H': h, 'P': p})
            both_unit_cases += 1
            if (math.gcd(c, h) == 1) != (math.gcd(p[1], h) == 1):
                failures.append({'type': 'both_coordinate_unit_relation', 'H': h, 'P': p, 'c': c})
        for c in range(h):
            for u in range(1, coordinate_bound + 1):
                if math.gcd(u, h) != 1:
                    continue
                for w in range(-coordinate_bound, coordinate_bound + 1):
                    image = (u, w)
                    p = inverse(image, h, c)
                    inverse_cases += 1
                    if forward(p, h, c) != image or primitive(p) != primitive(image):
                        failures.append({'type': 'inverse_primitive_equivalence', 'H': h, 'c': c, 'image': image})
        for p in positions:
            cp = sector(p, h)
            for q in positions:
                cq = sector(q, h)
                shared_gcd = math.gcd(p[0], q[0])
                det = determinant(p, q)
                pair_cases += 1
                for d in range(1, shared_gcd + 1):
                    if shared_gcd % d:
                        continue
                    assert det % d == 0
                    t = det // d
                    divisor_cases += 1
                    if math.gcd(d, h) != 1 or ((t % h == 0) != (cp == cq)):
                        failures.append({'type': 'shared_divisor_sector_equivalence', 'H': h, 'P': p, 'Q': q, 'D': d, 't': t})
                p_image, q_image = forward(p, h, cp), forward(q, h, cq)
                # For different sector maps the cross term must be retained.
                scaled = det + (cp - cq) * p[0] * q[0]
                if scaled % h or determinant(p_image, q_image) != scaled // h:
                    failures.append({'type': 'mixed_sector_determinant', 'H': h, 'P': p, 'Q': q})
                if cp == cq and determinant(p_image, q_image) * h != det:
                    failures.append({'type': 'same_sector_determinant_scaling', 'H': h, 'P': p, 'Q': q})
        sector_populations.append({'H': h, 'admissible_positions': len(positions), 'by_sector': counts})
    return {'H_even_range': [2, max_h], 'coordinate_bound': coordinate_bound,
        'position_cases': position_cases, 'inverse_lattice_cases': inverse_cases,
        'ordered_pair_cases': pair_cases, 'both_coordinate_unit_cases': both_unit_cases,
        'ordered_pair_shared_divisor_cases': divisor_cases,
        'integral_complement_cases': complement_cases,
        'sector_populations': sector_populations}


def trim(polynomial):
    while len(polynomial) > 1 and polynomial[-1] == 0:
        polynomial.pop()
    return polynomial


def subtract(a, b):
    out = [0] * max(len(a), len(b))
    for i, value in enumerate(a):
        out[i] += value
    for i, value in enumerate(b):
        out[i] -= value
    return trim(out)


def polynomial_division(dividend, divisor):
    remainder = trim(list(dividend))
    divisor = trim(list(divisor))
    assert divisor[-1] == 1
    quotient = [0] * max(1, len(remainder) - len(divisor) + 1)
    while len(remainder) >= len(divisor) and remainder != [0]:
        degree = len(remainder) - len(divisor)
        coefficient = remainder[-1]
        quotient[degree] += coefficient
        for i, value in enumerate(divisor):
            remainder[i + degree] -= coefficient * value
        trim(remainder)
    return trim(quotient), trim(remainder)


CYCLOTOMIC = {1: [-1, 1]}


def cyclotomic(n):
    if n not in CYCLOTOMIC:
        polynomial = [-1] + [0] * (n - 1) + [1]
        for divisor in range(1, n):
            if n % divisor == 0:
                polynomial, remainder = polynomial_division(polynomial, cyclotomic(divisor))
                assert remainder == [0]
        CYCLOTOMIC[n] = polynomial
    return CYCLOTOMIC[n]


def residue(polynomial, order):
    return polynomial_division(polynomial, cyclotomic(order))[1]


def exponential_numerator(arcs, frequency, order):
    """Numerator of integral exp(2*pi*i*t*x)dx, omitting 2*pi*i*t."""
    polynomial = [0] * order
    for left, right in arcs:
        a, b = left * order, right * order
        assert a.denominator == b.denominator == 1
        polynomial[(frequency * b.numerator) % order] += 1
        polynomial[(frequency * a.numerator) % order] -= 1
    return trim(polynomial)


def fourier_checks(max_h, failures):
    base_arcs = ((Fraction(0), Fraction(1, 10)),
                 (Fraction(2, 5), Fraction(1, 2)),
                 (Fraction(9, 10), Fraction(1)))
    base_measure = sum(right - left for left, right in base_arcs)
    orthogonality_cases = integral_cases = zero_cases = 0
    for h in range(2, max_h + 1, 2):
        pulled = tuple(((left + j) / h, (right + j) / h)
                       for j in range(h) for left, right in base_arcs)
        measure = sum(right - left for left, right in pulled)
        if measure != base_measure:
            failures.append({'type': 'pullback_measure', 'H': h})
        order = 10 * h
        for t in range(-2 * h, 2 * h + 1):
            geometric = [0] * h
            for j in range(h):
                geometric[(t * j) % h] += 1
            expected = [h] if t % h == 0 else [0]
            orthogonality_cases += 1
            if residue(geometric, h) != expected:
                failures.append({'type': 'exact_character_orthogonality', 'H': h, 't': t})
            if t == 0:
                zero_cases += 1
                continue
            lhs = exponential_numerator(pulled, t, order)
            integral_cases += 1
            if t % h:
                difference = lhs
            else:
                # Denominators are t on the left and t/H on the right.
                rhs = exponential_numerator(base_arcs, t // h, order)
                difference = subtract(lhs, [h * coefficient for coefficient in rhs])
            if residue(difference, order) != [0]:
                failures.append({'type': 'pullback_fourier_identity', 'H': h, 't': t})
    omitted = exponential_numerator(((Fraction(0), Fraction(1, 2)),), 1, 2)
    omitted_residue = residue(omitted, 2)
    if omitted_residue != [-2]:
        failures.append({'type': 'omitted_pullback_counterexample'})
    return {'base_arcs': [[str(a), str(b)] for a, b in base_arcs],
        'base_measure': str(base_measure), 'character_orthogonality_cases': orthogonality_cases,
        'nonzero_fourier_integral_cases': integral_cases, 'zero_frequency_cases': zero_cases,
        'method': 'Exact integer polynomial remainders modulo cyclotomic polynomials; rational interval endpoints and Jacobian factors.',
        'omitted_pullback_witness': {'H': 2, 'frequency': 1, 'base_arc': ['0', '1/2'],
            'unpulled_integral_numerator_mod_Phi2': omitted_residue,
            'interpretation': 'The unpulled integral has numerator -2 and is nonzero, even though H does not divide frequency.'}}


def omitted_hypothesis_checks(failures):
    inverse_image = inverse((2, 1), 2, 0)
    if inverse_image != (2, 2) or not primitive((2, 1)) or primitive(inverse_image):
        failures.append({'type': 'nonunit_inverse_primitivity_witness'})
    p, q, h = (2, 1), (4, 1), 2
    d = math.gcd(p[0], q[0])
    det = determinant(p, q)
    t = det // d
    if not primitive(p) or not primitive(q) or det % h != 0 or t % h == 0:
        failures.append({'type': 'nonunit_denominator_witness'})
    nonunit_sector = sector((1, 2), 2)
    if nonunit_sector != 0:
        failures.append({'type': 'sector_need_not_be_unit'})
    arc = ((Fraction(0), Fraction(1, 16)), (Fraction(15, 16), Fraction(1)))
    example_h, example_p, example_q = 6, (5, 1), (7, 1)
    example_b, example_a = 5, 7
    example_t = determinant(example_p, example_q)
    frequency = example_t - example_h * (example_b - example_a)
    ordinary_arc_residue = residue(exponential_numerator(arc, frequency, 16), 16)
    pulled = tuple(((a + j) / example_h, (b + j) / example_h)
                   for j in range(example_h) for a, b in arc)
    pullback_residue = residue(exponential_numerator(pulled, frequency, 96), 96)
    if example_t != -2 or frequency != 10 or ordinary_arc_residue == [0] or pullback_residue != [0]:
        failures.append({'type': 'ordinary_centered_arc_does_not_split'})
    return {'inverse_without_unit_first_coordinate': {'H': 2, 'c': 0,
        'transformed_primitive': [2, 1], 'inverse_nonprimitive': list(inverse_image)},
        'shared_divisor_without_unit': {'H': h, 'P': list(p), 'Q': list(q), 'D': d,
            'determinant': det, 't': t, 'H_divides_determinant': True, 'H_divides_t': False},
        'first_unit_does_not_force_sector_unit': {'H': 2, 'P': [1, 2], 'sector': nonunit_sector},
        'ordinary_arc_centered_kernel_cross_sector_witness': {'H': example_h,
            'P': list(example_p), 'Q': list(example_q), 'a': example_a, 'b': example_b,
            't': example_t, 'frequency_t_minus_H_b_minus_a': frequency,
            'sector_P': sector(example_p, example_h), 'sector_Q': sector(example_q, example_h),
            'arc': '[-1/16,1/16] modulo one',
            'ordinary_fourier_numerator_mod_Phi16': ordinary_arc_residue,
            'full_pullback_fourier_numerator_mod_Phi96': pullback_residue}}


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


def mobius(n):
    sign = 1
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            n //= divisor
            sign = -sign
            if n % divisor == 0:
                return 0
        divisor += 1
    if n > 1:
        sign = -sign
    return sign


def totient(h):
    return sum(math.gcd(value, h) == 1 for value in range(1, h + 1))


def coprime_interval_count(lower, upper, scale, h):
    lo, hi = (lower + scale - 1) // scale, upper // scale
    direct = sum(math.gcd(value, h) == 1 for value in range(lo, hi + 1))
    inclusion = 0
    for divisor in range(1, h + 1):
        if h % divisor == 0:
            factor = scale * divisor
            inclusion += mobius(divisor) * (upper // factor - (lower + factor - 1) // factor + 1)
    assert direct == inclusion
    return direct


def density_checks(max_h, failures):
    primes = [p for p in range(2, 32) if prime_factors(p) == [p]]
    reciprocal_zeta_finite = math.prod(Fraction(p * p - 1, p * p) for p in primes)
    records = []
    for h in range(2, max_h + 1, 2):
        allowed = [p for p in primes if h % p]
        terms = [(1, 1)]
        for p in allowed:
            terms += [(d * p, -sign) for d, sign in list(terms)]
        exact_mu_sum = sum((Fraction(sign, d * d) for d, sign in terms), Fraction(0))
        phi_ratio = Fraction(totient(h), h)
        kappa_u = phi_ratio * exact_mu_sum
        kappa_b = phi_ratio ** 2 * exact_mu_sum
        expected_u = reciprocal_zeta_finite * math.prod(Fraction(p, p + 1) for p in prime_factors(h))
        expected_b = reciprocal_zeta_finite * math.prod(Fraction(p - 1, p + 1) for p in prime_factors(h))
        if kappa_u != expected_u or kappa_b != expected_b or phi_ratio * kappa_u != kappa_b:
            failures.append({'type': 'finite_euler_density_identity', 'H': h})
        records.append({'H': h, 'squarefree_divisor_terms': len(terms),
            'finite_mobius_sum': str(exact_mu_sum), 'finite_kappa_u': str(kappa_u),
            'finite_kappa_b': str(kappa_b), 'phi_over_H': str(phi_ratio)})
    return {'prime_cutoff': 31, 'records': records,
        'assurance': 'Exact finite Euler-product identities. These finite products are not substituted for the infinite zeta constant in an asymptotic theorem.'}


def shoelace_area(vertices):
    return abs(sum(vertices[i][0] * vertices[(i + 1) % len(vertices)][1]
        - vertices[(i + 1) % len(vertices)][0] * vertices[i][1]
        for i in range(len(vertices)))) / 2


def prepared_box_counts(max_h, smoke, failures):
    """Exact Mobius counts; big-O ratios are explicitly diagnostic only."""
    records = []
    exact_mobius_cases = edge_group_cases = 0
    max_edge_group = {'count': 0}
    max_sector_error_ratio = {'ratio': 0.0}
    max_both_error_ratio = {'ratio': 0.0}
    us = [1] if smoke else [1, 2, 3]
    vs = [1, 3] if smoke else [1, 3, 8]
    for h in range(2, max_h + 1, 2):
        for u_scale in us:
            for v_scale in vs:
                b_bound = min(16 * u_scale, 2 * v_scale)
                phi_ratio = Fraction(totient(h), h)
                tau_h = 2 ** len(prime_factors(h))
                mobius_sector_counts = [0] * h
                mobius_both = 0
                finite_mu_sum = Fraction(0)
                for g in range(1, b_bound + 1):
                    if math.gcd(g, h) != 1:
                        continue
                    mu_g = mobius(g)
                    if not mu_g:
                        continue
                    finite_mu_sum += Fraction(mu_g, g * g)
                    count_u = coprime_interval_count(u_scale, 16 * u_scale, g, h)
                    count_v = coprime_interval_count(v_scale, 2 * v_scale, g, h)
                    mobius_both += mu_g * count_u * count_v
                    for u0 in range((u_scale + g - 1) // g, 16 * u_scale // g + 1):
                        if math.gcd(u0, h) != 1:
                            continue
                        inverse_u = pow(u0, -1, h)
                        for v0 in range((v_scale + g - 1) // g, 2 * v_scale // g + 1):
                            mobius_sector_counts[v0 * inverse_u % h] += mu_g
                primitive_sector_counts = [0] * h
                all_sector_points = [[] for _ in range(h)]
                primitive_images = [[] for _ in range(h)]
                direct_both = 0
                for u in range(u_scale, 16 * u_scale + 1):
                    for v in range(v_scale, 2 * v_scale + 1):
                        for c in range(h):
                            if (v - c * u) % h == 0:
                                all_sector_points[c].append((u, (v - c * u) // h))
                        if math.gcd(u, h) == 1 and primitive((u, v)):
                            c = sector((u, v), h)
                            primitive_sector_counts[c] += 1
                            primitive_images[c].append(forward((u, v), h, c))
                            direct_both += math.gcd(v, h) == 1
                if direct_both != mobius_both or direct_both != sum(primitive_sector_counts[c] for c in range(h) if math.gcd(c, h) == 1):
                    failures.append({'type': 'aggregate_both_unit_mobius_count', 'H': h, 'U': u_scale, 'V': v_scale})
                both_main = 15 * u_scale * v_scale * phi_ratio ** 2 * finite_mu_sum
                both_tail = Fraction(15 * u_scale * v_scale, b_bound) * phi_ratio ** 2
                both_diagnostic = None
                if u_scale >= 2 and v_scale >= 2:
                    error_scale = tau_h * (u_scale + v_scale) * math.log(2 * b_bound) + tau_h ** 2 * b_bound + u_scale * v_scale / b_bound
                    both_diagnostic = float(abs(direct_both - both_main) + both_tail) / error_scale
                    if both_diagnostic > max_both_error_ratio['ratio']:
                        max_both_error_ratio = {'ratio': both_diagnostic, 'H': h, 'U': u_scale, 'V': v_scale}
                for c in range(h):
                    corners = [(Fraction(u), Fraction(v - c * u, h))
                        for u, v in [(u_scale, v_scale), (16 * u_scale, v_scale),
                                     (16 * u_scale, 2 * v_scale), (u_scale, 2 * v_scale)]]
                    area = shoelace_area(corners)
                    expected_area = Fraction(15 * u_scale * v_scale, h)
                    if area != expected_area:
                        failures.append({'type': 'parallelogram_area', 'H': h, 'c': c})
                    all_count = primitive_count = 0
                    for u in range(u_scale, 16 * u_scale + 1):
                        if math.gcd(u, h) != 1:
                            continue
                        for v in range(v_scale, 2 * v_scale + 1):
                            if (v - c * u) % h:
                                continue
                            all_count += 1
                            primitive_count += primitive((u, v))
                            image = forward((u, v), h, c)
                            if not Fraction(v_scale - c * u, h) <= image[1] <= Fraction(2 * v_scale - c * u, h):
                                failures.append({'type': 'exact_parallelogram_membership', 'H': h, 'c': c, 'u': u, 'v': v})
                    minimum_y, maximum_y = min(p[1] for p in corners), max(p[1] for p in corners)
                    bounding_area = 15 * u_scale * (maximum_y - minimum_y)
                    if bounding_area / area != 1 + Fraction(15 * c * u_scale, v_scale):
                        failures.append({'type': 'bounding_rectangle_area_ratio', 'H': h, 'c': c})
                    exact_mobius_cases += 1
                    if primitive_count != mobius_sector_counts[c] or primitive_count != primitive_sector_counts[c]:
                        failures.append({'type': 'sector_exact_mobius_count', 'H': h, 'c': c, 'U': u_scale, 'V': v_scale})
                    for p_image in primitive_images[c]:
                        determinant_groups = {}
                        for q_image in all_sector_points[c]:
                            edge_group_cases += 1
                            value = determinant(p_image, q_image)
                            determinant_groups[value] = determinant_groups.get(value, 0) + 1
                        group_max = max(determinant_groups.values(), default=0)
                        if group_max > 17:
                            failures.append({'type': 'exact_edge_bound_17', 'H': h, 'c': c, 'P_image': p_image, 'count': group_max})
                        if group_max > max_edge_group['count']:
                            max_edge_group = {'count': group_max, 'H': h, 'c': c, 'U': u_scale, 'V': v_scale, 'P_image': list(p_image)}
                    main = Fraction(15 * u_scale * v_scale, h) * phi_ratio * finite_mu_sum
                    tail = Fraction(15 * u_scale * v_scale, h * b_bound) * phi_ratio
                    sector_diagnostic = None
                    if u_scale >= 2 and v_scale >= 2:
                        scale = (u_scale + tau_h * v_scale / h) * math.log(2 * b_bound) + b_bound + u_scale * v_scale / (h * b_bound)
                        sector_diagnostic = float(abs(primitive_count - main) + tail) / scale
                        if sector_diagnostic > max_sector_error_ratio['ratio']:
                            max_sector_error_ratio = {'ratio': sector_diagnostic, 'H': h, 'c': c, 'U': u_scale, 'V': v_scale}
                    records.append({'H': h, 'c': c, 'U': u_scale, 'V': v_scale,
                        'lattice_count_first_coordinate_unit': all_count,
                        'primitive_lattice_count': primitive_count,
                        'parallelogram_area': str(area), 'vertical_slice_width': str(Fraction(v_scale, h)),
                        'bounding_rectangle_area': str(bounding_area),
                        'bounding_rectangle_to_parallelogram_area': str(bounding_area / area),
                        'finite_mobius_sum': str(finite_mu_sum),
                        'sector_main_from_finite_mobius_sum': str(main), 'sector_infinite_series_tail_bound': str(tail),
                        'aggregate_both_unit_count': direct_both, 'aggregate_finite_main': str(both_main),
                        'aggregate_infinite_series_tail_bound': str(both_tail),
                        'sector_error_ratio_diagnostic': sector_diagnostic,
                        'aggregate_error_ratio_diagnostic': both_diagnostic})
    return {'domains': len(records), 'exact_sector_mobius_cases': exact_mobius_cases,
        'edge_pair_evaluations': edge_group_cases, 'max_exact_determinant_group': max_edge_group,
        'max_sector_error_ratio_diagnostic': max_sector_error_ratio,
        'max_both_error_ratio_diagnostic': max_both_error_ratio, 'records': records,
        'assurance': 'Mobius reconstructions and geometric factors are exact. Ratios involving logarithmic big-O scales are diagnostics only and do not certify an asymptotic implied constant.'}


def author_specific_checks(failures):
    # Preparation only: author statement is not yet available. This prevents an
    # accidental run from being reported as the completed dependent stage.
    if not AUTHOR_STATEMENT_INSTANTIATED:
        raise RuntimeError('Final author statement and populated finite-check packet have not been instantiated.')
    statement = Path(__file__).with_name('statement.md')
    actual_hash = hashlib.sha256(statement.read_bytes()).hexdigest()
    if actual_hash != FROZEN_STATEMENT_SHA256:
        raise RuntimeError('Author statement differs from the frozen input.')
    packet_path = Path(__file__).resolve().parents[3] / '.runs/goldbach-sectors-006-manual-20261029/packets/finite-check.json'
    packet = json.loads(packet_path.read_text(encoding='utf-8'))
    if any(upstream['result'] is None for upstream in packet['upstream']):
        raise RuntimeError('Dependent finite-check packet lacks a completed upstream statement.')
    return {'status': 'author statement instantiated', 'statement_sha256': actual_hash,
        'formulas_checked': 'T_c, integral complement (5), shared-divisor quotient (3), full pullback (2), exact Mobius count identities behind (7)-(8), density relation, geometry and edge bound17',
        'asymptotic_estimate_limit': 'No finite run validates big-O asymptotics or the analytic cancellation source theorem.'}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--smoke', action='store_true')
    parser.add_argument('--output', type=Path, default=Path(__file__).with_name('finite-results.json'))
    args = parser.parse_args()
    failures = []
    author_record = author_specific_checks(failures)
    started = time.perf_counter()
    max_h = 6 if args.smoke else 30
    coordinate_bound = 5 if args.smoke else 12
    result = {'status': 'running', 'python': platform.python_version(), 'platform': platform.platform(),
        'processor': platform.processor() or 'unknown', 'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'author_specific': author_record}
    result['vectors'] = vector_checks(max_h, coordinate_bound, failures)
    result['fourier'] = fourier_checks(max_h, failures)
    result['omitted_hypotheses'] = omitted_hypothesis_checks(failures)
    result['finite_euler_densities'] = density_checks(max_h, failures)
    result['boxes'] = prepared_box_counts(max_h, args.smoke, failures)
    result['failures'] = failures
    result['status'] = 'passed_exact_sector_checks' if not failures else 'failed_exact_sector_checks'
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
