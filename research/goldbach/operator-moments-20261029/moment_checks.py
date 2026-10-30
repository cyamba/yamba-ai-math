"""Prepared exact finite algebra for the auxiliary signed moment audit."""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
import hashlib
from itertools import permutations, product
import json
import math
from pathlib import Path
import platform
import time

AUTHOR_STATEMENT_INSTANTIATED = True
FROZEN_STATEMENT_SHA256 = '0e0e38bdb4f3b000bd67f385d5c32da1bb59fbd22790d1ddb31a8d10ead3e7ca'


def partitions(n):
    current = [()]
    for index in range(n):
        next_values = []
        for partition in current:
            for block_index in range(len(partition)):
                changed = list(partition)
                changed[block_index] = changed[block_index] + (index,)
                next_values.append(tuple(changed))
            next_values.append(partition + ((index,),))
        current = next_values
    return current


def labels_from_partition(partition, n):
    values = [0] * n
    for label, block in enumerate(partition):
        for index in block:
            values[index] = label
    return values


def active_runs(mask, n):
    return sum(bool(mask >> j & 1) and (j == 0 or not (mask >> (j - 1) & 1)) for j in range(n))


def prime_average(lines, active, eta, line_count):
    answer = Fraction(0)
    for line in range(line_count):
        term = Fraction(1)
        for j, value in enumerate(lines):
            if active >> j & 1:
                term *= value == line
            else:
                term *= 1 - eta[j] * (value == line)
        answer += term
    return answer / line_count


def damping_checks(smoke, failures):
    lengths = [3] if smoke else [3, 5]
    parameters = [(Fraction(1, 4), Fraction(1, 2), Fraction(3, 4))]
    if not smoke:
        parameters.append((Fraction(4, 9), Fraction(2, 3), Fraction(5, 6)))
    primes = [3] if smoke else [3, 5, 11]
    mass = Fraction(1, 3) + Fraction(1, 5) + Fraction(1, 11)
    inactive_cases = active_cases = telescoping_cases = normalization_cases = theta_cases = 0
    for n in lengths:
        for rho, square_root, theta in parameters:
            q = [square_root] + [rho] * (n - 2) + [square_root]
            eta = [1 - value for value in q]
            assert theta ** 2 > square_root
            for value in q:
                theta_cases += 1
                if theta * (value / theta ** 2) * theta != value:
                    failures.append({'type': 'retained_theta_cancellation'})
                if (-(1 - value) * mass / theta) * theta != -(1 - value) * mass:
                    failures.append({'type': 'appended_theta_cancellation'})
                if theta * (-(1 - value) / theta) != -(1 - value):
                    failures.append({'type': 'removed_theta_cancellation'})
            for p in primes:
                line_count = p + 1
                b_prime = 1 - sum(eta) / line_count
                assert b_prime > 0
                nu = 1 / (mass * line_count * b_prime)
                for equality_pattern in partitions(n):
                    if len(equality_pattern) > line_count:
                        continue
                    lines = labels_from_partition(equality_pattern, n)
                    lhs = prime_average(lines, 0, eta, line_count)
                    expanded = b_prime
                    for a in range(n):
                        for c in range(a + 1, n):
                            term = eta[a] * eta[c] * (lines[a] == lines[c])
                            for j in range(a + 1, c):
                                term *= 1 - eta[j] * (lines[j] == lines[a])
                            expanded += term / line_count
                    inactive_cases += 1
                    if lhs != expanded:
                        failures.append({'type': 'inactive_prime_interval_expansion', 'n': n, 'p': p, 'rho': str(rho), 'lines': lines})
                    for active in range(1, 1 << n):
                        active_cases += 1
                        indices = [j for j in range(n) if active >> j & 1]
                        a, c = min(indices), max(indices)
                        common = all(lines[j] == lines[a] for j in indices)
                        direct = prime_average(lines, active, eta, line_count)
                        active_formula = Fraction(0)
                        if common:
                            active_formula = Fraction(1, line_count)
                            for j in range(n):
                                if not (active >> j & 1):
                                    active_formula *= 1 - eta[j] * (lines[j] == lines[a])
                            prefix = math.prod(1 - eta[j] * (lines[j] == lines[a]) for j in range(a))
                            prefix_expanded = Fraction(1)
                            for h in range(a):
                                prefix_expanded -= eta[h] * (lines[h] == lines[a]) * math.prod(
                                    1 - eta[j] * (lines[j] == lines[a]) for j in range(h + 1, a))
                            suffix = math.prod(1 - eta[j] * (lines[j] == lines[a]) for j in range(c + 1, n))
                            suffix_expanded = Fraction(1)
                            for h in range(c + 1, n):
                                suffix_expanded -= eta[h] * (lines[h] == lines[a]) * math.prod(
                                    1 - eta[j] * (lines[j] == lines[a]) for j in range(c + 1, h))
                            telescoping_cases += 1
                            if prefix != prefix_expanded or suffix != suffix_expanded:
                                failures.append({'type': 'active_prefix_suffix', 'n': n, 'active': active, 'lines': lines})
                        if direct != active_formula:
                            failures.append({'type': 'active_prime_factor', 'n': n, 'active': active, 'lines': lines})
                        kappa = active_runs(active, n)
                        normalized = direct / b_prime * mass ** -kappa
                        formula = Fraction(0)
                        if common:
                            inactive_product = math.prod(1 - eta[j] * (lines[j] == lines[a])
                                for j in range(n) if not (active >> j & 1))
                            formula = nu * mass ** -(kappa - 1) * inactive_product
                        normalization_cases += 1
                        if normalized != formula:
                            failures.append({'type': 'active_run_V_normalization', 'n': n, 'active': active, 'lines': lines})
    endpoint_true = prime_average([0, 1, 2], 0,
        [Fraction(1, 2), Fraction(3, 4), Fraction(1, 2)], 4)
    endpoint_wrong = 1 - Fraction(3 * 3, 4 * 4)
    if endpoint_true != Fraction(9, 16) or endpoint_wrong != Fraction(7, 16):
        failures.append({'type': 'endpoint_q_negative_control'})
    run_eta = [Fraction(1, 2), Fraction(3, 4), Fraction(1, 2)]
    run_b = 1 - sum(run_eta) / 4
    run_factor = prime_average([0, 1, 0], 5, run_eta, 4)
    run_correct = run_factor / run_b * mass ** -2
    run_wrong = run_factor / run_b * mass ** -1
    if run_correct == run_wrong:
        failures.append({'type': 'active_runs_negative_control'})
    return {'inactive_cases': inactive_cases, 'active_cases': active_cases,
        'prefix_suffix_cases': telescoping_cases, 'active_run_normalization_cases': normalization_cases,
        'theta_local_cases': theta_cases, 'reciprocal_prime_mass': str(mass),
        'endpoint_factor_witness': {'p': 3, 'rho': '1/4', 'projective_labels': [0, 1, 2],
            'correct_factor': str(endpoint_true), 'wrong_all_q_equal_rho_factor': str(endpoint_wrong)},
        'active_run_normalization_witness': {'active_indices': [0, 2], 'runs': 2,
            'correct_normalized_factor': str(run_correct), 'wrong_one_run_factor': str(run_wrong)},
        'scope': 'Finite per-prime algebra, not the full signed G/E path identity or a norm estimate.'}


def permutation_cycles(permutation):
    seen = set()
    cycles = []
    for start in range(len(permutation)):
        if start in seen:
            continue
        cycle = []
        index = start
        while index not in seen:
            seen.add(index)
            cycle.append(index)
            index = permutation[index]
        if len(cycle) >= 2:
            cycles.append(tuple(sorted(cycle)))
    return tuple(sorted(cycles))


def distinct_checks(max_n, failures):
    pattern_active_cases = permutation_cases = collection_cases = direct_baseline_cases = 0
    rank_records = []
    for n in range(max_n + 1):
        full_partitions = partitions(n)
        collections = [tuple(block for block in partition if len(block) >= 2) for partition in full_partitions]
        cycle_counts = Counter(permutation_cycles(permutation) for permutation in permutations(range(n)))
        permutation_cases += math.factorial(n)
        rank_weights = Counter()
        descriptions = []
        for collection in collections:
            rank = sum(len(block) - 1 for block in collection)
            weight = math.prod(math.factorial(len(block) - 1) for block in collection)
            mask = sum(1 << index for block in collection for index in block)
            collection_cases += 1
            if cycle_counts[collection] != weight or mask.bit_count() > 2 * rank:
                failures.append({'type': 'permutation_cycle_factor', 'n': n, 'collection': collection})
            rank_weights[rank] += weight
            descriptions.append((collection, mask, (-1) ** rank * weight))
        for rank, weight in rank_weights.items():
            if weight > n ** (2 * rank):
                failures.append({'type': 'rank_weight_bound', 'n': n, 'rank': rank, 'weight': weight})
        for equality_pattern in full_partitions:
            values = labels_from_partition(equality_pattern, n)
            accumulated = [0] * (1 << n)
            for collection, mask, signed_weight in descriptions:
                if all(len({values[index] for index in block}) == 1 for block in collection):
                    accumulated[mask] += signed_weight
            subset_sum = accumulated[:]
            for bit in range(n):
                for mask in range(1 << n):
                    if mask >> bit & 1:
                        subset_sum[mask] += subset_sum[mask ^ (1 << bit)]
            for active in range(1 << n):
                selected = [values[index] for index in range(n) if active >> index & 1]
                expected = int(len(selected) == len(set(selected)))
                pattern_active_cases += 1
                if subset_sum[active] != expected:
                    failures.append({'type': 'distinct_active_identity', 'n': n, 'values': values, 'active': active})
                if n <= 4:
                    direct_baseline_cases += 1
                    direct = sum(signed for collection, mask, signed in descriptions if mask & active == mask
                        and all(len({values[index] for index in block}) == 1 for block in collection))
                    if direct != subset_sum[active]:
                        failures.append({'type': 'distinct_subset_sum_baseline', 'n': n})
        rank_records.append({'n': n, 'rank_weights': {str(rank): value for rank, value in sorted(rank_weights.items())}})
    inactive_wrong = sum((-1) ** sum(len(block) - 1 for block in partition if len(block) >= 2)
        * math.prod(math.factorial(len(block) - 1) for block in partition if len(block) >= 2)
        for partition in partitions(2))
    if inactive_wrong != 0:
        failures.append({'type': 'inactive_status_negative_control'})
    character_cases = 0
    for difference in range(-11, 12):
        counts = [0] * 17
        for j in range(17):
            counts[j * difference % 17] += 1
        character_cases += 1
        expected = [17] + [0] * 16 if difference == 0 else [1] * 17
        if counts != expected:
            failures.append({'type': 'finite_torus_orthogonality_factor', 'difference': difference})
    return {'max_indices': max_n, 'equality_pattern_active_cases': pattern_active_cases,
        'enumerated_permutations': permutation_cases, 'collection_cases': collection_cases,
        'direct_baseline_cases': direct_baseline_cases, 'rank_records': rank_records,
        'exact_cyclic_orthogonality_cases': character_cases,
        'inactive_index_negative_control': {'n': 2, 'active_indices': [0], 'equal_assigned_values': True,
            'correct_distinct_indicator': 1, 'wrong_result_without_active_status': inactive_wrong},
        'scope': 'Exact distinctness/cycle/rank combinatorics only; no large-rank operator estimate follows.'}


def gaussian_add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def gaussian_scale(a, scalar):
    return (a[0] * scalar, a[1] * scalar)


def phase(values, marks):
    if any(index >= len(values) for index, coefficient in marks):
        return (Fraction(0), Fraction(0))
    exponent = sum(coefficient * values[index] for index, coefficient in marks) % 4
    return [(Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)),
            (Fraction(-1), Fraction(0)), (Fraction(0), Fraction(-1))][exponent]


def tuple_checks(max_length, failures):
    alphabet = (2, 3, 5)
    weight_vectors = ((Fraction(1, 7), Fraction(2, 7), Fraction(3, 7)),
                      (Fraction(1, 5), Fraction(1, 3), Fraction(1, 2)))
    phase_specs = ((), ((0, 1), (1, -1)), ((0, 1), (3, -1)))
    sym_cache = {}
    identity_cases = tuple_cases = norm_cases = measure_cases = 0
    mass_records = []
    for length in range(max_length + 1):
        tuple_values = list(product(alphabet, repeat=length))
        index_permutations = list(permutations(range(length)))
        for weights in weight_vectors:
            nu = dict(zip(alphabet, weights))
            total_memory = total_active = Fraction(0)
            mass_by_multiset = Counter()
            for values in tuple_values:
                raw_weight = math.prod((nu[p] for p in values), start=Fraction(1))
                memory_weight = raw_weight / math.factorial(length)
                total_active += raw_weight
                total_memory += memory_weight
                mass_by_multiset[tuple(sorted(values))] += memory_weight
                tuple_cases += 1
            s = sum(weights)
            measure_cases += 1
            if total_active != s ** length or total_memory != s ** length / math.factorial(length):
                failures.append({'type': 'active_memory_total_measure', 'length': length})
            for multiset, actual in mass_by_multiset.items():
                counts = Counter(multiset)
                expected = math.prod(nu[p] ** count / math.factorial(count) for p, count in counts.items())
                if actual != expected:
                    failures.append({'type': 'repeated_tuple_factorial_measure', 'length': length, 'tuple': multiset})
            for marks in phase_specs:
                lhs = [(Fraction(0), Fraction(0)) for _ in range(3)]
                rhs = [(Fraction(0), Fraction(0)) for _ in range(3)]
                for values in tuple_values:
                    key = (tuple(sorted(values)), marks)
                    if key not in sym_cache:
                        total = (Fraction(0), Fraction(0))
                        for permutation in index_permutations:
                            total = gaussian_add(total, phase(tuple(values[index] for index in permutation), marks))
                        sym_cache[key] = gaussian_scale(total, Fraction(1, math.factorial(length)))
                    symmetrized = sym_cache[key]
                    norm_cases += 1
                    if symmetrized[0] ** 2 + symmetrized[1] ** 2 > 1:
                        failures.append({'type': 'symmetrized_phase_bound', 'tuple': values})
                    test_values = [Fraction(1), Fraction(sum(values) - 3 * length),
                                   Fraction(math.prod(values), 1 + sum(p * p for p in values))]
                    weight = math.prod((nu[p] for p in values), start=Fraction(1)) / math.factorial(length)
                    raw_phase = phase(values, marks)
                    for index, test_value in enumerate(test_values):
                        lhs[index] = gaussian_add(lhs[index], gaussian_scale(symmetrized, weight * test_value))
                        rhs[index] = gaussian_add(rhs[index], gaussian_scale(raw_phase, weight * test_value))
                for index in range(3):
                    identity_cases += 1
                    if lhs[index] != rhs[index]:
                        failures.append({'type': 'memory_tuple_symmetrization', 'length': length, 'marks': marks, 'test': index})
            mass_records.append({'length': length, 'prime_weights': [str(value) for value in weights],
                's': str(s), 'active_mass': str(total_active), 'fixed_line_appended_memory_mass': str(total_memory)})
    # Exact nonsymmetric-F counterexample on two alphabet values, l=2.
    nonsym_lhs = nonsym_rhs = (Fraction(0), Fraction(0))
    for values in product([2, 3], repeat=2):
        direct_phase = phase(values, ((0, 1), (1, -1)))
        swapped_phase = phase(values[::-1], ((0, 1), (1, -1)))
        symmetric_phase = gaussian_scale(gaussian_add(direct_phase, swapped_phase), Fraction(1, 2))
        nonsym_lhs = gaussian_add(nonsym_lhs, gaussian_scale(symmetric_phase, Fraction(values[0], 8)))
        nonsym_rhs = gaussian_add(nonsym_rhs, gaussian_scale(direct_phase, Fraction(values[0], 8)))
    if nonsym_lhs != (Fraction(5, 8), Fraction(0)) or nonsym_rhs != (Fraction(5, 8), Fraction(1, 8)):
        failures.append({'type': 'missing_nonsymmetric_test_witness'})
    wrong_unordered_mass = sum(Fraction(1, 8) for values in [(2, 2), (2, 3), (3, 3)])
    return {'max_length': max_length, 'ordered_tuple_cases': tuple_cases,
        'symmetrization_identity_cases': identity_cases, 'phase_norm_cases': norm_cases,
        'total_measure_cases': measure_cases, 'mass_records': mass_records,
        'nonsymmetric_F_negative_control': {'alphabet': [2, 3], 'length': 2, 'prime_weights': ['1/2', '1/2'],
            'phase': 'i^(p1-p2)', 'test_F': 'p1', 'symmetrized_weighted_sum': [str(x) for x in nonsym_lhs],
            'raw_weighted_sum': [str(x) for x in nonsym_rhs]},
        'unordered_factorial_negative_control': {'alphabet': [2, 3], 'weights': ['1/2', '1/2'],
            'length': 2, 'correct_ordered_memory_mass': '1/2',
            'wrong_unordered_with_same_factorial_mass': str(wrong_unordered_mass)},
        'scope': 'Exact Gaussian-rational phase and tuple algebra. No analytic phase-inserted G/E norm is certified.'}


def full_pair_memory_checks(failures):
    nu = {2: Fraction(1, 7), 3: Fraction(2, 7)}
    alphabet = tuple((p, line) for p in [2, 3] for line in range(p + 1))
    full_mass = sum(nu[p] for p, line in alphabet)
    prime_mass = sum(nu.values())
    records = []
    tuple_cases = 0
    marks = ((0, 1), (1, -1))
    for length in range(4):
        total = Fraction(0)
        grouped_mass = Counter()
        lhs = rhs = (Fraction(0), Fraction(0))
        sym_cache = {}
        index_permutations = list(permutations(range(length)))
        for values in product(alphabet, repeat=length):
            tuple_cases += 1
            weight = math.prod((nu[p] for p, line in values), start=Fraction(1)) / math.factorial(length)
            total += weight
            key = tuple(sorted(values))
            grouped_mass[key] += weight
            if key not in sym_cache:
                average = (Fraction(0), Fraction(0))
                for permutation in index_permutations:
                    average = gaussian_add(average, phase(tuple(values[index][0] for index in permutation), marks))
                sym_cache[key] = gaussian_scale(average, Fraction(1, math.factorial(length)))
            test = Fraction(1 + sum(p + 2 * line for p, line in values))
            lhs = gaussian_add(lhs, gaussian_scale(sym_cache[key], weight * test))
            rhs = gaussian_add(rhs, gaussian_scale(phase(tuple(p for p, line in values), marks), weight * test))
        expected = full_mass ** length / math.factorial(length)
        if total != expected or lhs != rhs:
            failures.append({'type': 'full_pair_memory_measure_symmetry', 'length': length})
        for multiset, actual in grouped_mass.items():
            expected_multiset = math.prod((nu[pair[0]] ** count / math.factorial(count)
                for pair, count in Counter(multiset).items()), start=Fraction(1))
            if actual != expected_multiset:
                failures.append({'type': 'full_pair_memory_repetition_measure', 'length': length})
        records.append({'length': length, 'full_memory_mass': str(total),
            'symmetric_phase_sum': [str(x) for x in lhs]})
    return {'full_pair_alphabet_size': len(alphabet), 'ordered_pair_tuple_cases': tuple_cases,
        'lambda_X': str(full_mass), 'prime_choice_mass_s': str(prime_mass), 'records': records,
        'normalization_negative_control': 'lambda(X)=11/7 differs from s=3/7 because every projective line is a memory atom.',
        'scope': 'Full pair-memory lambda measure, distinct from the fixed-current-line appended prime-tuple measure.'}


def author_specific_checks():
    if not AUTHOR_STATEMENT_INSTANTIATED:
        raise RuntimeError('Preparation only: final frozen definitions and populated packet are pending.')
    statement = Path(__file__).with_name('statement.md')
    actual = hashlib.sha256(statement.read_bytes()).hexdigest()
    if actual != FROZEN_STATEMENT_SHA256:
        raise RuntimeError('Frozen author input changed.')
    packet_path = Path(__file__).resolve().parents[3] / '.runs/goldbach-moments-010-manual-20261029/packets/finite-check.json'
    packet = json.loads(packet_path.read_text(encoding='utf-8'))
    if any(upstream['result'] is None for upstream in packet['upstream']):
        raise RuntimeError('Dependent packet lacks the completed author result.')
    return {'statement_sha256': actual,
        'covered_author_finite_identities': 'q endpoints and b-prime/nu normalization; per-prime factor(16), inactive ghost interval and active-run lifetimes; local theta cancellations; distinctness identity(19), cycle and rank weights; tuple phase symmetry and factorial measures.',
        'limited_coverage': 'No full operational G/E history enumeration, G-adjoint Schur proof, memory-tail asymptotic, analytic edge norm(15), model moment(6), or arithmetic replacement(22) is validated by these finite checks.'}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--smoke', action='store_true')
    parser.add_argument('--output', type=Path, default=Path(__file__).with_name('finite-results.json'))
    args = parser.parse_args()
    author = author_specific_checks()
    started = time.perf_counter()
    failures = []
    result = {'status': 'running', 'python': platform.python_version(), 'platform': platform.platform(),
        'processor': platform.processor() or 'unknown', 'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'author_input': author}
    result['per_prime_damping'] = damping_checks(args.smoke, failures)
    result['distinct_prime_combinatorics'] = distinct_checks(3 if args.smoke else 6, failures)
    result['memory_tuple_symmetrization'] = tuple_checks(3 if args.smoke else 6, failures)
    result['full_pair_memory'] = full_pair_memory_checks(failures)
    result['failures'] = failures
    result['status'] = 'passed_exact_moment_combinatorics' if not failures else 'failed_exact_moment_combinatorics'
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
