"""Prepared exact finite checks for the reflected TypeII pairing interface."""
from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction
import hashlib
from itertools import combinations, permutations, product
import json
import math
from pathlib import Path
import platform
import time

AUTHOR_STATEMENT_INSTANTIATED = True
FROZEN_STATEMENT_SHA256 = 'f93c024abd19699640e90bb5680306432c2bb71600acd77a0b66024a6658645b'


def gaussian(real=0, imaginary=0):
    return Fraction(real), Fraction(imaginary)


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def multiply(a, b):
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]


def scale(a, value):
    return a[0] * value, a[1] * value


def conjugate(a):
    return a[0], -a[1]


def norm_squared(a):
    return a[0] ** 2 + a[1] ** 2


def sum_gaussian(values):
    answer = gaussian()
    for value in values:
        answer = add(answer, value)
    return answer


def mobius_positive(n):
    assert n >= 1
    answer, divisor = 1, 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            n //= divisor
            answer = -answer
            if n % divisor == 0:
                return 0
        divisor += 1
    return -answer if n > 1 else answer


def alpha(m):
    return gaussian(Fraction(m % 5 - 2, 3), Fraction(m % 3 - 1, 2))


def beta(n):
    return gaussian(Fraction(n % 4 - 1, 2), Fraction(n % 5 - 2, 3))


def require(condition, failures, kind, **values):
    if not condition:
        failures.append({'type': kind, **values})


def signed_cofactor_checks(smoke, failures):
    moduli = [8, 10] if smoke else range(2, 31, 2)
    factor_limit = 6 if smoke else 12
    group_families = [((3, 5, 7),)]
    if not smoke:
        group_families.append(((3, 5), (7, 11)))
    totals = defaultdict(int)
    examples = []
    for H in moduli:
        factors = [m for m in range(1, factor_limit + 1) if math.gcd(m, H) == 1]
        for source_groups in group_families:
            groups = [tuple(p for p in group if H % p) for group in source_groups]
            if any(not group for group in groups):
                totals['empty_punctured_group'] += 1
                continue
            V = math.prod(sum((Fraction(1, p) for p in group), Fraction()) for group in groups)
            selected = [math.prod(draw) for draw in product(*groups)]
            Y = min(selected)
            buckets = defaultdict(list)
            for a, m, n in product(selected, factors, factors):
                totals['unit_products'] += 1
                require(H != m * n, failures, 'unit_h_zero', H=H, m=m, n=n)
                if (H - m * n) % a:
                    continue
                h = (H - m * n) // a
                require(h != 0, failures, 'included_h_zero', H=H, a=a, m=m, n=n)
                eta = Fraction(1 + a % 3, 3)
                coefficient = scale(multiply(alpha(m), beta(n)), eta / V)
                buckets[h].append((a, m, n, coefficient))
                totals['integer_cofactor_records'] += 1
            amplitudes = {h: sum_gaussian(row[3] for row in rows) for h, rows in buckets.items()}
            Qpos = sum((norm_squared(value) for h, value in amplitudes.items() if h > 0), Fraction())
            Qneg = sum((norm_squared(value) for h, value in amplitudes.items() if h < 0), Fraction())
            Qall = sum((norm_squared(value) for value in amplitudes.values()), Fraction())
            expanded = gaussian()
            for h, rows in buckets.items():
                for left, right in product(rows, repeat=2):
                    a, m, n, z = left
                    b, r, s, w = right
                    expanded = add(expanded, multiply(z, conjugate(w)))
                    require(b * m * n - a * r * s == H * (b - a), failures,
                            'cofactor_implies_determinant', H=H, h=h, left=left[:3], right=right[:3])
                    require(abs(Fraction(b - a, Y)) <= 3, failures, 'raw_psi_plateau', H=H, Y=Y, a=a, b=b)
                    totals['quadratic_pairs'] += 1
            require(expanded == gaussian(Qall), failures, 'quadratic_expansion', H=H, groups=groups)
            require(Qall == Qpos + Qneg and Qpos <= Qall, failures, 'signed_square_split', H=H)
            band_primes = {p for group in groups for p in group}
            target = sum_gaussian(scale(value, mobius_positive(h) * Fraction(1, 4) **
                                       sum(h % p == 0 for p in band_primes))
                                  for h, value in amplitudes.items() if h > 0)
            count_bound = (H - 1) // Y
            require(norm_squared(target) <= count_bound * Qpos, failures, 'positive_cauchy', H=H, Y=Y)
            require(norm_squared(target) <= (H // Y) * Qpos <= Fraction(H, Y) * Qall,
                    failures, 'author_positive_cauchy', H=H, Y=Y)
            totals['square_and_cauchy_cases'] += 1
            if Qneg and len(examples) < 3:
                examples.append({'H': H, 'groups': groups, 'Qpositive': Qpos, 'Qnegative': Qneg})
    determinant_limit = 6 if smoke else 16
    for H, a, b, x, y in product(moduli, (3, 5, 7, 15), (3, 5, 7, 15),
                                  range(1, determinant_limit + 1), range(1, determinant_limit + 1)):
        if math.gcd(a, b) != 1:
            continue
        if math.gcd(x * y, H) != 1:
            continue
        determinant = b * x - a * y == H * (b - a)
        equal_integer_cofactor = ((H - x) % a == 0 and (H - y) % b == 0 and
                                 (H - x) // a == (H - y) // b != 0)
        require(determinant == equal_integer_cofactor, failures, 'coprime_equivalence',
                H=H, a=a, b=b, x=x, y=y)
        totals['coprime_equivalence_cases'] += 1
    coefficients = [gaussian(1), gaussian(0, 1), gaussian(Fraction(1, 2), Fraction(-2, 3))]
    for am, ar, bn, bs in product(coefficients, repeat=4):
        fP = multiply(conjugate(am), bs)
        fQ = multiply(conjugate(ar), bn)
        actual = multiply(conjugate(fP), fQ)
        expected = multiply(multiply(am, conjugate(ar)), multiply(bn, conjugate(bs)))
        require(actual == expected, failures, 'endpoint_conjugation')
        totals['conjugation_cases'] += 1
    shared = {'H': 8, 'a': 3, 'b': 3, 'mn': 7, 'rs': 7, 'cofactor': Fraction(1, 3)}
    require(3 * 7 - 3 * 7 == 8 * (3 - 3) and (8 - 7) % 3 != 0,
            failures, 'missing_shared_prime_counterexample')
    wrong = multiply(conjugate(gaussian(0, 1)), gaussian(1))
    require(wrong != gaussian(0, 1), failures, 'missing_conjugation_counterexample')
    require((8 - 3 * 5) // 7 == -1 and all(math.gcd(v, 8) == 1 for v in (3, 5, 7)),
            failures, 'missing_negative_cofactor_example')
    require(6 == 2 * 3 and math.gcd(2 * 3, 6) != 1, failures, 'omitted_units_h_zero_negative_control')
    require(2 == 1 * 2 and (2 - 1) % 3 != 0, failures, 'author_small_support_witnesses')
    return {'counts': dict(totals), 'negative_square_examples': examples,
            'negative_controls': {'shared_prime': shared,
                                  'author_shared_prime': {'H': 2, 'a': 3, 'b': 3, 'mn': 1, 'rs': 1, 'cofactor': Fraction(1, 3)},
                                  'omitted_units_h_zero': {'H': 6, 'm': 2, 'n': 3},
                                  'author_omitted_units_h_zero': {'H': 2, 'a': 3, 'm': 1, 'n': 2},
                                  'negative_h': {'H': 8, 'a': 7, 'm': 3, 'n': 5, 'h': -1},
                                  'wrong_conjugation': {'actual': wrong, 'expected': gaussian(0, 1)}}}


def endpoint_checks(smoke, failures):
    moduli = [14] if smoke else range(10, 31, 2)
    parameters = [(1, 1, 3, 3)] if smoke else [(1, 1, 3, 3), (2, 2, 2, 3)]
    counts = defaultdict(int)
    occupancy = []
    max_cell_distance = 0
    for H, (d0, Y, M, N) in product(moduli, parameters):
        U, V = d0 * Y * M, N
        delta = Fraction(H, d0 * Y * M * M)
        x = M * N
        for a, b in product((3, 5, 7), repeat=2):
            if math.gcd(a * b, H) != 1:
                continue
            row_counts, column_counts = defaultdict(int), defaultdict(int)
            for k, ell in product(range(1, 4 * x + 1), repeat=2):
                if (b * k - a * ell) % H == 0:
                    row_counts[k] += 1
                    column_counts[ell] += 1
                    counts['comparison_congruence_pairs'] += 1
            degree_bound = math.ceil(Fraction(4 * x, H))
            require(max(row_counts.values(), default=0) <= degree_bound <= 4 and
                    max(column_counts.values(), default=0) <= degree_bound,
                    failures, 'comparison_row_column_degree', H=H, a=a, b=b, x=x)
            counts['comparison_degree_cases'] += 1
        for t in range(-4 * H, 4 * H + 1):
            root_order = H // math.gcd(H, t)
            reduced_step = 0 if root_order == 1 else (t // math.gcd(H, t)) % root_order
            phase_counts = defaultdict(int)
            for branch in range(H):
                phase_counts[branch * reduced_step % root_order] += 1
            # Geometric sums of order>1 vanish at a primitive root of that
            # order. For order1 the sum is H and branch measure is 1/H.
            require(set(phase_counts) == set(range(root_order)) and
                    set(phase_counts.values()) == {H // root_order},
                    failures, 'full_pullback_branch_geometric_sum', H=H, t=t)
            require((root_order == 1) == (t % H == 0), failures, 'full_pullback_surviving_branch', H=H, t=t)
            if root_order == 1:
                require(Fraction(sum(phase_counts.values()), H) == 1,
                        failures, 'full_pullback_no_extra_H_factor', H=H, t=t)
            counts['full_pullback_branch_certificates'] += 1
        for D in range(d0, 2 * d0):
            if math.gcd(D, H) != 1:
                continue
            points = [(u, v) for u in range(U, 2 * U) for v in range(V, 2 * V)
                      if u % D == 0 and math.gcd(u, v) == math.gcd(u, H) == math.gcd(v, H) == 1]
            sectors = {P: P[1] * pow(P[0], -1, H) % H for P in points}
            cells = {P: Fraction(P[1], P[0]) // delta for P in points}
            populated = defaultdict(int)
            for P in points:
                u, v = P
                complement = (-H * pow(v, -1, u)) % u
                last_entry = (H + v * complement) // u
                require(0 <= complement < u and u * last_entry - v * complement == H,
                        failures, 'canonical_determinant_H_complement', H=H, P=P)
                w = (v - sectors[P] * u) // H
                require(v == sectors[P] * u + H * w and math.gcd(u, w) == 1,
                        failures, 'primitive_sector_inverse', H=H, P=P)
                populated[(sectors[P], cells[P])] += 1
                counts['canonical_complements_and_sector_maps'] += 1
            maximum = max(populated.values(), default=0)
            occupancy.append({'H': H, 'D': D, 'parameters': (d0, Y, M, N), 'points': len(points),
                              'max_cell_occupancy': maximum, 'ratio_to_1_plus_UV_over_H':
                              Fraction(maximum, 1) / (1 + Fraction(U * V, H))})
            for P in points:
                det_multiplicities = defaultdict(int)
                for Q in points:
                    determinant = P[0] * Q[1] - P[1] * Q[0]
                    require(determinant % D == 0, failures, 'D_determinant_divisibility')
                    t = determinant // D
                    same_sector = sectors[P] == sectors[Q]
                    require((t % H == 0) == same_sector, failures, 'sector_equivalence', H=H, D=D, P=P, Q=Q)
                    counts['sector_pairs'] += 1
                    if same_sector and abs(t) <= 2 * H * Y:
                        distance = abs(cells[P] - cells[Q])
                        max_cell_distance = max(max_cell_distance, distance)
                        bound = math.ceil(Fraction(2 * D, d0)) + 1
                        require(distance <= bound, failures, 'slope_neighbor', H=H, D=D, P=P, Q=Q)
                        require(abs(Fraction(P[1], P[0]) - Fraction(Q[1], Q[0])) <=
                                Fraction(2 * D, d0) * delta, failures, 'slope_distance')
                        det_multiplicities[determinant] += 1
                        counts['window_neighbor_pairs'] += 1
                require(max(det_multiplicities.values(), default=0) <= 1, failures,
                        'primitive_fixed_determinant_multiplicity', H=H, D=D, P=P)
                require(len(det_multiplicities) <= 2 * (2 * D * Y) + 1,
                        failures, 'determinant_value_count', H=H, D=D, P=P)
            counts['endpoint_boxes'] += 1
    # The second coordinate need not be invertible in a first-coordinate-unit sector.
    require(math.gcd(1, 6) == 1 and math.gcd(2, 6) != 1, failures, 'both_unit_negative_control')
    B = ((1, 1), (1, -1))
    masked = tuple(tuple(B[i][j] * ((3, 5)[i] * (3, 5)[j] < 22) for j in range(2)) for i in range(2))
    x = (1, 1)
    full_norm = sum(sum(B[i][j] * x[j] for j in range(2)) ** 2 for i in range(2))
    mask_norm = sum(sum(masked[i][j] * x[j] for j in range(2)) ** 2 for i in range(2))
    require(full_norm == 4 and mask_norm == 5, failures, 'entrywise_mask_negative_control')
    return {'counts': dict(counts), 'max_cell_distance': max_cell_distance,
            'occupancy_diagnostics_only': occupancy,
            'negative_controls': {'both_unit_restriction': {'H': 6, 'primitive_point': (1, 2), 'sector': 2},
                                  'entrywise_mask': {'H': 22, 'coordinates': (3, 5), 'B': B,
                                                     'masked': masked, 'x': x,
                                                     'full_squared_norm': full_norm, 'masked_squared_norm': mask_norm}}}


def padding_checks(smoke, failures):
    base_groups = ((3, 5, 7, 11), (13, 17, 19, 23))
    moduli = [6] if smoke else (6, 10, 22)
    group_counts = [1] if smoke else (1, 2)
    J_values = range(2) if smoke else range(3)
    counts = defaultdict(int)
    masses = []
    for H, K, J in product(moduli, group_counts, J_values):
        groups = [tuple(p for p in group if H % p) for group in base_groups[:K]]
        normalizers = [sum((Fraction(1, p) for p in group), Fraction()) for group in groups]
        Vproduct = math.prod(normalizers)
        full_mass = Fraction(1)
        ordered_groups = []
        subset_groups = []
        union_bound = Fraction()
        for group, V in zip(groups, normalizers):
            draws = list(product(group, repeat=J))
            single_mass = sum((math.prod(Fraction(1, p) / V for p in draw) for draw in draws), Fraction())
            require(single_mass == 1, failures, 'normalized_harmonic_mass', H=H, K=K, J=J)
            full_mass *= single_mass
            a, b = group[:2]
            allowed = tuple(p for p in group if p not in (a, b))
            ordered_groups.append(list(permutations(allowed, J)))
            subset_groups.append(list(combinations(allowed, J)))
            ordered_single = sum((math.prod(Fraction(1, p) / V for p in row)
                                  for row in ordered_groups[-1]), Fraction())
            unordered_single = sum((math.prod(Fraction(1, p) / V for p in row)
                                    for row in subset_groups[-1]), Fraction())
            require(ordered_single == math.factorial(J) * unordered_single, failures,
                    'per_group_ordered_unordered_factorial', H=H, K=K, J=J, group=group)
            union_bound += J * sum((Fraction(1, p) / V for p in (a, b)), Fraction())
            union_bound += math.comb(J, 2) * sum(((Fraction(1, p) / V) ** 2 for p in group), Fraction())
            counts['nonzero_J2_group_factorials'] += J == 2 and ordered_single > 0
            counts['single_group_mass_cases'] += 1
        ordered_mass = Fraction()
        dyads = defaultdict(Fraction)
        for rows in product(*ordered_groups):
            D = math.prod(p for row in rows for p in row)
            d0 = 1 << (D.bit_length() - 1)
            require(d0 <= D < 2 * d0, failures, 'dyadic_half_open', D=D, d0=d0)
            ordered_mass += Fraction(1, D) / Vproduct ** J
            dyads[d0] += Fraction(d0, D)
            state_fresh_weight = Fraction(1, D) / Vproduct ** (J + 2)
            draw_weight = math.prod(Fraction(1, p) / V
                                    for row, V in zip(rows, normalizers) for p in row) / Vproduct ** 2
            require(state_fresh_weight == draw_weight, failures, 'author_weight_identity_16', H=H, K=K, J=J)
            counts['good_ordered_padding'] += 1
        unordered_mass = sum((Fraction(1, math.prod(p for row in rows for p in row)) / Vproduct ** J
                              for rows in product(*subset_groups)), Fraction())
        require(ordered_mass == math.factorial(J) ** K * unordered_mass, failures,
                'ordered_unordered_factorial', H=H, K=K, J=J)
        rebuilt = sum((value / d0 / Vproduct ** J for d0, value in dyads.items()), Fraction())
        require(rebuilt == ordered_mass, failures, 'dyadic_d0_over_D', H=H, K=K, J=J)
        require(0 <= ordered_mass <= full_mass == 1, failures, 'excluded_padding_mass', H=H, K=K, J=J)
        require(1 - ordered_mass <= union_bound, failures, 'finite_padding_union_bound', H=H, K=K, J=J)
        delta = gaussian(Fraction(H + K, J + 1), Fraction(K - J, 3))
        reassembled = sum_gaussian(scale(delta, value / d0 / Vproduct ** (J + 2))
                                   for d0, value in dyads.items())
        require(reassembled == scale(delta, ordered_mass / Vproduct ** 2), failures,
                'author_reassembly_17_per_endpoint_pair', H=H, K=K, J=J)
        masses.append({'H': H, 'K': K, 'J': J, 'V': normalizers,
                       'full_mass': full_mass, 'good_mass': ordered_mass, 'omitted_mass': 1 - ordered_mass,
                       'explicit_union_bound': union_bound,
                       'ordered_to_unordered_factor': math.factorial(J) ** K,
                       'dyadic_blocks': sorted(dyads)})
        for group in groups:
            for subset in combinations(group, J + 1):
                direct = list(permutations(subset))
                distinguished = [(a,) + shared for a in subset
                                 for shared in permutations(tuple(p for p in subset if p != a))]
                require(sorted(direct) == sorted(distinguished), failures, 'distinguished_list_bijection')
                require(len(direct) == math.factorial(J + 1), failures, 'active_list_factorial')
                nonsymmetric = lambda row: sum((i + 1) * p for i, p in enumerate(row))
                left = sum(nonsymmetric(row) for row in direct)
                right = sum(nonsymmetric(row) for row in distinguished)
                require(left == right, failures, 'ordered_list_test_function')
                invariant_average = Fraction(sum(math.prod(row) for row in direct), math.factorial(J + 1))
                require(invariant_average == math.prod(subset), failures, 'invariant_f_list_symmetrization')
                counts['active_list_cases'] += 1
        counts['padding_cases'] += 1
    V = Fraction(1, 3) + Fraction(1, 5) + Fraction(1, 7)
    valid = 2 * Fraction(1, 3 * 5) / V ** 2
    wrong_unordered = valid / 2
    require(valid != wrong_unordered and valid < 1, failures, 'factorial_and_exclusion_negative_control')
    return {'counts': dict(counts), 'exact_masses': masses,
            'negative_controls': {'missing_J_factorial': {'J': 2, 'correct_ordered_mass': valid,
                                                         'wrong_unordered_mass': wrong_unordered},
                                  'exclusion_mass_not_one': {'group': (3, 5, 7),
                                                             'allowed_distinct_ordered': ((3, 5), (5, 3)),
                                                             'mass': valid}}}


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
        raise SystemExit('Preparation only. Await the frozen author statement and actual finite-check packet.')
    directory = Path(__file__).resolve().parent
    statement = directory / 'statement.md'
    actual_source_hash = hashlib.sha256(statement.read_bytes()).hexdigest()
    if actual_source_hash != FROZEN_STATEMENT_SHA256:
        raise SystemExit('Frozen statement hash mismatch.')
    packet = json.loads(args.packet.read_text(encoding='utf-8-sig'))
    if packet['step']['id'] != 'finite-check' or not packet.get('upstream'):
        raise SystemExit('Actual populated finite-check packet required.')
    started = time.perf_counter()
    failures = []
    comparisons = {'signed_cofactors': signed_cofactor_checks(args.smoke, failures),
                   'endpoint_geometry': endpoint_checks(args.smoke, failures),
                   'artificial_padding': padding_checks(args.smoke, failures)}
    result = {'mode': 'smoke' if args.smoke else 'bounded_final', 'passed': not failures,
              'runtime_seconds': time.perf_counter() - started,
              'python': platform.python_version(), 'platform': platform.platform(),
              'code_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'statement_sha256': actual_source_hash,
              'packet_sha256': hashlib.sha256(args.packet.read_bytes()).hexdigest(),
              'comparisons': comparisons, 'failures': failures,
              'scope': 'Finite exact algebra and bounded endpoint diagnostics only; no analytic norm, removal, TypeII or Goldbach certification.'}
    if not args.smoke:
        (directory / 'finite-results.json').write_text(json.dumps(result, indent=2, default=encode) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2, default=encode))
    return 0 if not failures else 1


if __name__ == '__main__':
    raise SystemExit(main())
