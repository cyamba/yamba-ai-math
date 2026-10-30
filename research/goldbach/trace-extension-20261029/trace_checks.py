"""Prepared exact Fraction trace and determinant-H enlargement checks."""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import importlib.util
from itertools import combinations, permutations, product
import json
import math
from pathlib import Path
import platform
import sys
import time

AUTHOR_STATEMENT_INSTANTIATED = True
FROZEN_STATEMENT_SHA256 = '44336ee22423b7a63550ff3b49ca394a9e12af1971eb04ac7c8e455a116a4b3d'
ARITHMETIC_HELPER_SHA256 = '498798fd996b211cf5d1f1b3bea47b101fcc720061d9b2133c1a9d5df92e28af'
ARITHMETIC = None


def arithmetic_helper():
    global ARITHMETIC
    if ARITHMETIC is None:
        path = Path(__file__).resolve().parent.parent / 'complement-ratios-20261029/ratio_checks.py'
        if hashlib.sha256(path.read_bytes()).hexdigest() != ARITHMETIC_HELPER_SHA256:
            raise RuntimeError('Frozen arithmetic helper changed.')
        spec = importlib.util.spec_from_file_location('trace009_frozen_arithmetic', path)
        module = importlib.util.module_from_spec(spec)
        previous = sys.dont_write_bytecode
        sys.dont_write_bytecode = True
        try:
            spec.loader.exec_module(module)
        finally:
            sys.dont_write_bytecode = previous
        ARITHMETIC = module
    return ARITHMETIC


def matrix(rows):
    return [[Fraction(value) for value in row] for row in rows]


def identity(n):
    return matrix([[int(i == j) for j in range(n)] for i in range(n)])


def multiply(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a):
    return [list(row) for row in zip(*a)]


def add(a, b):
    return [[x + y for x, y in zip(row_a, row_b)] for row_a, row_b in zip(a, b)]


def scale(a, value):
    return [[value * x for x in row] for row in a]


def power(a, exponent):
    result = identity(len(a))
    for _ in range(exponent):
        result = multiply(result, a)
    return result


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def adjoint(a, weights):
    return [[a[j][i] * weights[j] / weights[i] for j in range(len(a))] for i in range(len(a))]


def determinant(a):
    if len(a) == 1:
        return a[0][0]
    return sum((-1) ** j * a[0][j] * determinant([row[:j] + row[j + 1:] for row in a[1:]])
               for j in range(len(a)))


def quadratic(a, vector, weights):
    return sum(vector[i] * weights[i] * a[i][j] * vector[j]
               for i in range(len(vector)) for j in range(len(vector)))


def vector_outer(vector, weights):
    return [[vector[i] * vector[j] * weights[j] for j in range(len(vector))]
            for i in range(len(vector))]


def trace_checks(smoke, failures):
    entry_sets = [(-1, 0, 1)] * 4
    choices = list(product(*entry_sets))
    if smoke:
        choices = choices[:9] + [(1, 0, 0, 1)]
    cases = 0
    for entries in choices:
        b = matrix([entries[:2], entries[2:]])
        for weights in [(Fraction(1), Fraction(1)), (Fraction(1), Fraction(2))]:
            full_positive = multiply(b, adjoint(b, weights))
            for mask in product([0, 1], repeat=2):
                projection = matrix([[mask[0], 0], [0, mask[1]]])
                compressed = multiply(multiply(projection, b), projection)
                compressed_positive = multiply(compressed, adjoint(compressed, weights))
                for r in [1, 2, 3]:
                    cases += 1
                    lhs = trace(power(compressed_positive, r))
                    rhs = trace(power(full_positive, r))
                    if lhs > rhs:
                        failures.append({'type': 'Schatten_trace_compression', 'entries': list(entries),
                            'weights': [str(w) for w in weights], 'mask': list(mask), 'R': r,
                            'lhs': str(lhs), 'rhs': str(rhs)})
    b = matrix([[1, 0, 1], [2, 0, -2], [0, 0, 0]])
    projection = matrix([[1, 0, 0], [0, 1, 0], [0, 0, 0]])
    compressed = multiply(multiply(projection, b), projection)
    a_pos = multiply(compressed, transpose(compressed))
    b_pos = multiply(b, transpose(b))
    pointwise_witness = []
    for r in [1, 2, 3]:
        aa, bb = power(a_pos, r), power(b_pos, r)
        if trace(aa) > trace(bb):
            failures.append({'type': 'counterexample_trace_should_still_contract', 'R': r})
        pointwise_witness.append({'R': r, 'compressed_e0_diagonal': str(aa[0][0]),
            'full_e0_diagonal': str(bb[0][0]), 'compressed_trace': str(trace(aa)), 'full_trace': str(trace(bb))})
    if not Fraction(pointwise_witness[1]['compressed_e0_diagonal']) > Fraction(pointwise_witness[1]['full_e0_diagonal']):
        failures.append({'type': 'missing_pointwise_projection_counterexample'})
    author_b = matrix([[1, 0, Fraction(1, 2)], [1, 0, -2], [0, 0, 0]])
    author_compressed = multiply(multiply(projection, author_b), projection)
    author_small = power(multiply(author_compressed, transpose(author_compressed)), 2)
    author_full = power(multiply(author_b, transpose(author_b)), 2)
    if author_small[0][0] != 2 or author_full[0][0] != Fraction(25, 16):
        failures.append({'type': 'author_pointwise_counterexample'})
    endpoint_projection = matrix([[Fraction(1, 2), Fraction(-1, 2)],
                                  [Fraction(-1, 2), Fraction(1, 2)]])
    endpoint_only_witness = []
    for r in [1, 2, 3]:
        t = power(endpoint_projection, r)
        value = quadratic(t, [Fraction(1), Fraction(1)], [Fraction(1), Fraction(1)])
        if value != 0 or trace(t) != 1:
            failures.append({'type': 'endpoint_moment_does_not_control_trace', 'R': r})
        endpoint_only_witness.append({'R': r, 'endpoint_moment': str(value), 'trace': str(trace(t))})
    root_cases = psd_minor_cases = root_moment_cases = 0
    weight_vector = [Fraction(1), Fraction(2), Fraction(3), Fraction(5)]
    coefficient_choices = list(product([-1, 0, 1], repeat=4))
    if smoke:
        coefficient_choices = coefficient_choices[:9]
    c = matrix([[1, -1, 0, 1], [0, 1, 1, 0], [1, 0, -1, 0], [0, 1, 0, 1]])
    positive = multiply(c, adjoint(c, weight_vector))
    for a, b0, c0, d in coefficient_choices:
        vectors = [[Fraction(a), Fraction(b0), Fraction(0), Fraction(0)],
                   [Fraction(0), Fraction(0), Fraction(c0), Fraction(d)]]
        norms = [sum(w * x * x for w, x in zip(weight_vector, vector)) for vector in vectors]
        m_bound = max(norms)
        sum_outer = add(vector_outer(vectors[0], weight_vector), vector_outer(vectors[1], weight_vector))
        difference = add(scale(identity(4), m_bound), scale(sum_outer, -1))
        weighted_form = [[weight_vector[i] * difference[i][j] for j in range(4)] for i in range(4)]
        root_cases += 1
        for size in range(1, 5):
            for subset in combinations(range(4), size):
                psd_minor_cases += 1
                if determinant([[weighted_form[i][j] for j in subset] for i in subset]) < 0:
                    failures.append({'type': 'root_weight_M_bound', 'coefficients': [a, b0, c0, d], 'subset': list(subset)})
        for r in [1, 2, 3]:
            t = power(positive, r)
            lhs = sum(quadratic(t, vector, weight_vector) for vector in vectors)
            trace_identity = trace(multiply(t, sum_outer))
            rhs = m_bound * trace(t)
            root_moment_cases += 1
            if lhs != trace_identity or lhs > rhs:
                failures.append({'type': 'root_moment_trace_bound', 'R': r, 'coefficients': [a, b0, c0, d]})
    overlap = vector_outer([Fraction(1), Fraction(0)], [Fraction(1), Fraction(1)])
    overlap_sum = add(overlap, overlap)
    if overlap_sum[0][0] != 2:
        failures.append({'type': 'overlapping_frame_witness'})
    return {'signed_matrix_trace_cases': cases, 'root_weight_families': root_cases,
        'exact_PSD_principal_minors': psd_minor_cases, 'root_moment_trace_cases': root_moment_cases,
        'pointwise_projection_deletion_witness': {'B': [[1, 0, 1], [2, 0, -2], [0, 0, 0]],
            'projection_diagonal': [1, 1, 0], 'powers': pointwise_witness},
        'author_pointwise_witness': {'R': 2, 'compressed_diagonal': str(author_small[0][0]),
            'full_diagonal': str(author_full[0][0])},
        'endpoint_moment_vs_trace_witness': endpoint_only_witness,
        'overlapping_fibers_witness': {'root_vectors': [[1, 0], [1, 0]], 'each_squared_norm': 1,
            'M': 1, 'sum_outer_e0_quadratic': 2,
            'interpretation': 'Without disjoint fibers, the maximum individual norm alone cannot bound the sum of outer products.'},
        'assurance': 'Exact finite Fraction matrix checks; the general operator proof requires separate substantive review.'}


def gram_and_list_checks(failures):
    weights = [Fraction(1), Fraction(2), Fraction(3), Fraction(5)]
    b = matrix([[1, -1, 0, 1], [0, 1, 1, 0], [1, 0, -1, 0], [0, 1, 0, 1]])
    positive = multiply(b, adjoint(b, weights))
    roots = [[Fraction(1), Fraction(1), Fraction(0), Fraction(0)],
             [Fraction(0), Fraction(0), Fraction(1), Fraction(-1)]]
    gram_cases = pairing_cases = 0
    for mask in [(1, 0), (0, 1), (1, 1)]:
        projection = matrix([[int(i == j) * mask[i // 2] for j in range(4)] for i in range(4)])
        family = [roots[i] for i in range(2) if mask[i]]
        for r in [1, 2, 3]:
            t = power(positive, r)
            gram = [[sum(x[i] * weights[i] * t[i][j] * y[j] for i in range(4) for j in range(4))
                     for y in family] for x in family]
            gram_cases += 1
            for size in range(1, len(family) + 1):
                for subset in combinations(range(len(family)), size):
                    if determinant([[gram[i][j] for j in subset] for i in subset]) < 0:
                        failures.append({'type': 'restricted_endpoint_Gram_PSD', 'mask': mask, 'R': r})
            d_e = trace(gram)
            for alpha in product([-1, 0, 1], repeat=len(family)):
                f = [sum(Fraction(a) * vector[i] for a, vector in zip(alpha, family)) for i in range(4)]
                for raw_g in [(1, -1, 1, 0), (0, 1, -1, 1)]:
                    g = [Fraction(raw_g[i]) * mask[i // 2] for i in range(4)]
                    bg = [sum(b[i][j] * g[j] for j in range(4)) for i in range(4)]
                    compressed_b = multiply(multiply(projection, b), projection)
                    pbg = [sum(compressed_b[i][j] * g[j] for j in range(4)) for i in range(4)]
                    pairing = sum(f[i] * weights[i] * bg[i] for i in range(4))
                    compressed_pairing = sum(f[i] * weights[i] * pbg[i] for i in range(4))
                    norm_f = sum(weights[i] * f[i] ** 2 for i in range(4))
                    norm_g = sum(weights[i] * g[i] ** 2 for i in range(4))
                    raised_rhs = norm_g ** r * norm_f ** (r - 1) * d_e * sum(a * a for a in alpha)
                    pairing_cases += 1
                    if pairing != compressed_pairing or abs(pairing) ** (2 * r) > raised_rhs:
                        failures.append({'type': 'restricted_Gram_pairing_8a', 'mask': mask, 'R': r, 'alpha': alpha})
    groups = ([2, 3, 5], [7, 11, 13])
    masses = [sum((Fraction(1, p) for p in group), Fraction(0)) for group in groups]
    list_cases = state_cases = 0
    examples = []
    for masks in product(range(8), repeat=2):
        selected = [[p for j, p in enumerate(group) if masks[i] >> j & 1] for i, group in enumerate(groups)]
        u = math.prod(p for group in selected for p in group)
        for m in [1, 2, 3]:
            lists = [list(permutations(group, m)) for group in selected]
            state_count = sum(1 for _ in product(*lists))
            state_cases += state_count
            falling = [math.prod(range(len(group) - m + 1, len(group) + 1)) if len(group) >= m else 0 for group in selected]
            weight = math.prod(mass ** -m for mass in masses)
            actual = state_count * weight
            formula = math.prod(falling) * weight
            list_cases += 1
            if actual != formula or any(min(group) ** len(chosen) > u for group, chosen in zip(groups, selected)):
                failures.append({'type': 'ordered_list_endpoint_factor', 'masks': masks, 'm': m})
            if state_count and len(examples) < 6:
                examples.append({'u': u, 'm': m, 'n_i': [len(group) for group in selected],
                    'state_count': state_count, 'squared_endpoint_norm': str(actual)})
    return {'restricted_Gram_PSD_cases': gram_cases, 'exact_raised_pairing_cases': pairing_cases,
        'ordered_list_factor_cases': list_cases, 'enumerated_list_states': state_cases,
        'group_masses': [str(value) for value in masses], 'list_examples': examples,
        'assurance': 'Exact finite Gram and falling-factorial formulas. No large-L harmless-root asymptotic is inferred from finite examples.'}


def extended_gcd(a, b):
    old_r, r, old_x, x, old_y, y = a, b, 1, 0, 0, 1
    while r:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_x, x = x, old_x - quotient * x
        old_y, y = y, old_y - quotient * y
    if old_r < 0:
        old_r, old_x, old_y = -old_r, -old_x, -old_y
    return old_r, old_x, old_y


def phi(n):
    return sum(math.gcd(x, n) == 1 for x in range(n))


def enlarged_inverse(h, u, v, r):
    assert math.gcd(u, r) == 1 and (h + v * r) % u == 0
    d = (h + v * r) // u
    gcd, a, b = extended_gcd(u, r)
    assert gcd == 1
    sector = (a * v + b * d) % h
    assert (v - sector * u) % h == 0 and (d - sector * r) % h == 0
    w, s = (v - sector * u) // h, (d - sector * r) // h
    return sector, w, s, d


def enlargement_checks(max_h, max_u, max_v, failures):
    forward_cases = reverse_cases = multiplicity_cases = nonunit_h_cases = 0
    multiplicity_witnesses = []
    for h in range(2, max_h + 1, 2):
        forward_map = {}
        by_original = Counter()
        for sector in range(h):
            for u in range(2, max_u + 1):
                for v in range(1, max_v + 1):
                    if (v - sector * u) % h:
                        continue
                    w = (v - sector * u) // h
                    if math.gcd(u, w) != 1:
                        continue
                    r = -pow(w, -1, u) % u
                    s = (1 + w * r) // u
                    d = sector * r + h * s
                    key = (u, v, r)
                    forward_cases += 1
                    if key in forward_map or u * d - v * r != h or math.gcd(u, r) != 1:
                        failures.append({'type': 'enlarged_forward', 'H': h, 'sector': sector, 'u': u, 'v': v, 'r': r})
                    forward_map[key] = (sector, w, s, d)
                    by_original[(u, v)] += 1
        reverse_keys = set()
        for u in range(2, max_u + 1):
            for v in range(1, max_v + 1):
                for r in range(u):
                    if math.gcd(u, r) != 1 or (v * r + h) % u:
                        continue
                    reverse_cases += 1
                    nonunit_h_cases += math.gcd(h, u) > 1
                    inverse = enlarged_inverse(h, u, v, r)
                    sector, w, s, d = inverse
                    if math.gcd(u, w) != 1 or u * s - w * r != 1 or forward_map.get((u, v, r)) != inverse:
                        failures.append({'type': 'enlarged_inverse', 'H': h, 'u': u, 'v': v, 'r': r})
                    reverse_keys.add((u, v, r))
                expected = 0
                g = math.gcd(h, u)
                if math.gcd(v, u) == g:
                    expected = phi(u) // phi(u // g)
                multiplicity_cases += 1
                if by_original[(u, v)] != expected:
                    failures.append({'type': 'original_pair_multiplicity', 'H': h, 'u': u, 'v': v,
                        'actual': by_original[(u, v)], 'expected': expected})
                if expected > 1 and len(multiplicity_witnesses) < 10:
                    multiplicity_witnesses.append({'H': h, 'u': u, 'v': v, 'multiplicity': expected})
        if reverse_keys != set(forward_map):
            failures.append({'type': 'enlarged_forward_inverse_sets', 'H': h})
    witness = enlarged_inverse(6, 3, 3, 1)
    if witness != (3, -1, 0, 3):
        failures.append({'type': 'H6_nonunit_enlarged_witness'})
    author_two = [enlarged_inverse(2, 4, 2, r) for r in [1, 3]]
    if author_two != [(1, -1, 0, 1), (0, 1, 1, 2)]:
        failures.append({'type': 'author_H2_two_preimages'})
    return {'forward_root_cases': forward_cases, 'inverse_triple_cases': reverse_cases,
        'original_pair_multiplicity_cases': multiplicity_cases, 'nonunit_H_mod_u_roots': nonunit_h_cases,
        'multiplicity_witnesses': multiplicity_witnesses,
        'H6_u3_v3_r1_witness': {'H': 6, 'sector': witness[0], 'image': [3, witness[1]],
            'matrix': [[3, 1], [3, witness[3]]], 'kernel_mod3': [1, 0],
            'contrast': 'Allowed by enlargement; excluded by the original both-unit population.'},
        'author_H2_u4_v2_two_roots': [{'r': r, 'sector': value[0], 'image': [4, value[1]], 'd': value[3]}
            for r, value in zip([1, 3], author_two)]}


def prime_factors(n):
    out = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


def line_from_row(u, r, p):
    u, r = u % p, r % p
    assert u or r
    return (1, -u * pow(r, -1, p) % p) if r else (0, 1)


def all_lines(p):
    return [(0, 1)] + [(1, t) for t in range(p)]


def prescription(u, r, s):
    return tuple(line_from_row(u, r, p) for p in prime_factors(s))


def key_text(key):
    return '|'.join(f'{a},{b}' for a, b in key)


def complete_root_densities(max_h, moduli, failures):
    records = []
    cases = sharing_h_cases = 0
    for s in moduli:
        keys = list(product(*(all_lines(p) for p in prime_factors(s))))
        for h in range(2, min(max_h, 12) + 1, 2):
            counter = Counter()
            for u in range(s):
                for r in range(s):
                    if math.gcd(u, r, s) != 1:
                        continue
                    key = prescription(u, r, s)
                    for v in range(s):
                        for d in range(s):
                            if (u * d - v * r - h) % s == 0:
                                counter[key] += 1
            for key in keys:
                cases += 1
                sharing_h_cases += math.gcd(s, h) > 1
                if counter[key] != s * phi(s):
                    failures.append({'type': 'enlarged_complete_line_density', 'H': h, 'S': s, 'key': key_text(key)})
            records.append({'H': h, 'S': s, 'determinant_is_unit_mod_S': math.gcd(h, s) == 1,
                'matrices_with_unimodular_first_row': sum(counter.values()),
                'prescriptions': len(keys), 'count_each': s * phi(s)})
    return {'records': records, 'prescription_cases': cases,
        'prescriptions_with_S_sharing_H': sharing_h_cases,
        'assurance': 'The first row is unimodular; the matrix need not be invertible when S shares H.'}


def enlarged_box_counts(max_h, moduli, smoke, failures):
    intervals = ((Fraction(0), Fraction(1)), (Fraction(0), Fraction(1, 3)),
                 (Fraction(1, 3), Fraction(2, 3)), (Fraction(2, 3), Fraction(1)))
    us, vs = ([2], [2]) if smoke else ([2, 3], [2, 3, 5])
    records = []
    aggregate_cases = partition_cases = 0
    max_error_ratio = {'ratio': 0.0}
    for h in range(2, max_h + 1, 2):
        for u_scale in us:
            for v_scale in vs:
                triples = []
                for u in range(u_scale, 16 * u_scale):
                    for r in range(u):
                        if math.gcd(u, r) != 1:
                            continue
                        for v in range(v_scale, 2 * v_scale):
                            if (v * r + h) % u == 0:
                                triples.append((u, v, r))
                for s in moduli:
                    keys = list(product(*(all_lines(p) for p in prime_factors(s))))
                    counters = []
                    for left, right in intervals:
                        counter = Counter()
                        unweighted = 0
                        for u, v, r in triples:
                            if left <= Fraction(r, u) < right:
                                counter[prescription(u, r, s)] += 1
                                unweighted += 1
                        aggregate_cases += 1
                        if sum(counter[key] for key in keys) != unweighted:
                            failures.append({'type': 'enlarged_root_aggregation', 'H': h, 'S': s, 'U': u_scale, 'V': v_scale})
                        counters.append(counter)
                        main = 15 * u_scale * v_scale * float(right - left) * (6 / math.pi ** 2) / len(keys)
                        sigma = sum(d ** -0.75 for d in range(1, h + 1) if h % d == 0)
                        eta = Fraction(1, 16)
                        error_scale = (sigma * u_scale ** float(Fraction(7, 4) + eta) + v_scale) * math.log(2 * u_scale) ** 2
                        for key in keys:
                            ratio = abs(counter[key] - main) / error_scale
                            if ratio > max_error_ratio['ratio']:
                                max_error_ratio = {'ratio': ratio, 'H': h, 'S': s, 'U': u_scale, 'V': v_scale,
                                    'I3': [str(left), str(right)], 'prescription': key_text(key), 'eta': str(eta)}
                    for key in keys:
                        partition_cases += 1
                        if counters[0][key] != sum(counters[j][key] for j in [1, 2, 3]):
                            failures.append({'type': 'enlarged_ratio_partition', 'H': h, 'S': s, 'key': key_text(key)})
                    records.append({'H': h, 'S': s, 'U': u_scale, 'V': v_scale,
                        'root_triples': len(triples),
                        'counts_by_prescription': [{key_text(key): count for key, count in counter.items()} for counter in counters]})
    return {'records': records, 'aggregate_interval_cases': aggregate_cases,
        'prescription_partition_cases': partition_cases,
        'max_candidate_error_scale_ratio_diagnostic': max_error_ratio,
        'assurance': 'Exact enlarged-root counts and half-open partitions; candidate asymptotic error is not certified.'}


def enlarged_fourier_checks(max_h, failures):
    arithmetic = arithmetic_helper()
    gcd_cases = pair_cases = j_zero_cases = nonunit_h_pair_cases = zero_complete_coefficients = 0
    for h_target in range(2, max_h + 1, 2):
        for u in range(2, 13):
            for h_frequency in range(u):
                for j in range(u):
                    gcd_cases += 1
                    actual = math.gcd(h_frequency, j * h_target, u)
                    bound = math.gcd(h_target, u) * math.gcd(j, u)
                    if actual > bound or bound % actual:
                        failures.append({'type': 'nonunit_complete_gcd_cost', 'H': h_target, 'u': u, 'h': h_frequency, 'j': j})
    intervals = ((Fraction(0), Fraction(1)), (Fraction(1, 3), Fraction(2, 3)),
                 (Fraction(1, 3), Fraction(1, 3)))
    first_h_zero_boundary = None
    for h_target in range(2, min(max_h, 6) + 1, 2):
        for u in range(2, 7):
            for r_modulus in [1, 3]:
                if math.gcd(u, r_modulus) != 1:
                    continue
                for rho in range(r_modulus):
                    for interval in intervals:
                        candidates = [r for r in range(u) if interval[0] <= Fraction(r, u) < interval[1]
                                      and (r - rho * u) % r_modulus == 0]
                        a_u = sum(math.gcd(r, u) == 1 for r in candidates)
                        fhat = []
                        ghat = []
                        for frequency in range(u):
                            fraw, graw = [0] * u, [0] * u
                            for r in candidates:
                                fraw[-frequency * r % u] += 1
                            for v in [2, 3]:
                                graw[-frequency * v % u] += 1
                            fhat.append(arithmetic.residue(fraw, u))
                            ghat.append(arithmetic.residue(graw, u))
                        direct = sum(math.gcd(r, u) == 1 and (v * r + h_target) % u == 0
                                     for r in candidates for v in [2, 3])
                        total, j_zero, h_zero_nonzero_j = [0], [0], [0]
                        for h_frequency in range(u):
                            for j in range(u):
                                coefficient = -j * h_target
                                zero_complete_coefficients += j > 0 and coefficient % u == 0
                                term = arithmetic.multiply(fhat[h_frequency], ghat[j], u)
                                term = arithmetic.multiply(term, arithmetic.kloosterman(u, h_frequency, coefficient), u)
                                total = arithmetic.residue(arithmetic.add(total, term), u)
                                if j == 0:
                                    j_zero = arithmetic.residue(arithmetic.add(j_zero, term), u)
                                if h_frequency == 0 and j:
                                    h_zero_nonzero_j = arithmetic.residue(arithmetic.add(h_zero_nonzero_j, term), u)
                        pair_cases += 1
                        j_zero_cases += 1
                        nonunit_h_pair_cases += math.gcd(h_target, u) > 1
                        if total != [u * u * direct] or j_zero != [u * 2 * a_u]:
                            failures.append({'type': 'enlarged_double_fourier', 'H': h_target, 'u': u,
                                'R': r_modulus, 'rho': rho, 'interval': [str(x) for x in interval]})
                        if first_h_zero_boundary is None and h_zero_nonzero_j != [0]:
                            first_h_zero_boundary = {'H': h_target, 'u': u, 'R': r_modulus, 'rho': rho,
                                'I3': [str(x) for x in interval], 'h_zero_nonzero_j_numerator': h_zero_nonzero_j,
                                'pair_count': direct, 'A_u': a_u}
    if math.gcd(0, 2 * 2, 4) != 4 or math.gcd(2, 4) != 2:
        failures.append({'type': 'missing_nonunit_factor_witness'})
    return {'complete_gcd_cases': gcd_cases, 'exact_pair_count_cases': pair_cases,
        'exact_j_zero_cases': j_zero_cases, 'pair_cases_nonunit_H_mod_u': nonunit_h_pair_cases,
        'nonzero_j_with_zero_complete_coefficient': zero_complete_coefficients,
        'h_zero_nonzero_j_witness': first_h_zero_boundary,
        'unit_bound_cannot_be_copied_witness': {'H': 2, 'u': 4, 'h': 0, 'j': 2,
            'actual_gcd_h_jH_u': 4, 'unit_formula_gcd_j_u': 2, 'correct_product_bound': 4},
        'arithmetic_helper_sha256': ARITHMETIC_HELPER_SHA256,
        'assurance': 'Exact bounded Fourier and gcd checks, including zero/nonunit coefficient cases; no analytic exponent is certified.'}


def author_specific_checks():
    if not AUTHOR_STATEMENT_INSTANTIATED:
        raise RuntimeError('Preparation only: final author formulas and populated packet are pending.')
    statement = Path(__file__).with_name('statement.md')
    actual = hashlib.sha256(statement.read_bytes()).hexdigest()
    if actual != FROZEN_STATEMENT_SHA256:
        raise RuntimeError('Frozen author input changed.')
    packet_path = Path(__file__).resolve().parents[3] / '.runs/goldbach-trace-009-manual-20261029/packets/finite-check.json'
    packet = json.loads(packet_path.read_text(encoding='utf-8'))
    if any(upstream['result'] is None for upstream in packet['upstream']):
        raise RuntimeError('Dependent packet lacks the frozen author result.')
    return {'statement_sha256': actual, 'arithmetic_helper_sha256': ARITHMETIC_HELPER_SHA256,
        'actual_formulas': 'Weighted Schatten traces, disjoint-fiber frame bound, restricted ambient Gram pairing, list falling factors, enlarged root bijection/multiplicity, first-row line densities and nonunit-H Fourier completion.'}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--smoke', action='store_true')
    parser.add_argument('--output', type=Path, default=Path(__file__).with_name('finite-results.json'))
    args = parser.parse_args()
    author = author_specific_checks()
    started = time.perf_counter()
    failures = []
    max_h, max_u, max_v = (6, 6, 6) if args.smoke else (20, 12, 12)
    moduli = [2, 3] if args.smoke else [2, 3, 5, 6, 15]
    result = {'status': 'running', 'python': platform.python_version(), 'platform': platform.platform(),
        'processor': platform.processor() or 'unknown', 'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'author_input': author}
    result['trace_and_root_vectors'] = trace_checks(args.smoke, failures)
    result['Gram_and_list_factors'] = gram_and_list_checks(failures)
    result['enlargement'] = enlargement_checks(max_h, max_u, max_v, failures)
    result['complete_root_densities'] = complete_root_densities(max_h, moduli, failures)
    result['enlarged_boxes'] = enlarged_box_counts(max_h, moduli, args.smoke, failures)
    result['enlarged_fourier'] = enlarged_fourier_checks(2 if args.smoke else 20, failures)
    result['failures'] = failures
    result['status'] = 'passed_exact_trace_enlargement_checks' if not failures else 'failed_exact_trace_enlargement_checks'
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
