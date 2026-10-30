"""Prepared exact finite identities for the even reflected Type I interface."""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from fractions import Fraction
import hashlib
from itertools import combinations, product
import json
import math
from pathlib import Path
import platform
import time

AUTHOR_STATEMENT_INSTANTIATED = True
FROZEN_STATEMENT_SHA256 = 'f810cce2f92073af5244e673b0afdad6d6a1d624b22f4df422468bd61a174db2'


def factors(n):
    assert n >= 1
    result, p = [], 2
    while p * p <= n:
        while n % p == 0:
            result.append(p)
            n //= p
        p += 1
    if n > 1:
        result.append(n)
    return result


def mobius(n):
    fs = factors(n)
    return 0 if len(fs) != len(set(fs)) else (-1) ** len(fs)


def divisors(n):
    small = [d for d in range(1, math.isqrt(n) + 1) if n % d == 0]
    return sorted(set(small + [n // d for d in small]))


def rough(n, Z):
    return all(p > Z for p in factors(n))


def require(condition, failures, kind, **values):
    if not condition:
        failures.append({'type': kind, **values})


def add_log(answer, vector, scalar=1):
    for p, coefficient in vector.items():
        answer[p] += scalar * coefficient
        if answer[p] == 0:
            del answer[p]
    return answer


def log_vector(n):
    return dict(Counter(factors(n)))


def mangoldt_vector(n):
    fs = factors(n)
    return {fs[0]: 1} if fs and len(set(fs)) == 1 else {}


def c_vector(n, V):
    answer = defaultdict(Fraction)
    for ell in divisors(n):
        if ell > V:
            add_log(answer, mangoldt_vector(ell))
    return dict(answer)


def reflected_weight(n, H):
    if not 1 <= n < H:
        return Fraction()
    w = H - n
    primes = (3, 7)
    eligible = [p for p in primes if H % p]
    V = sum((Fraction(1, p) for p in eligible), Fraction())
    omega = sum(w % p == 0 for p in eligible)
    if omega == 0 or V == 0:
        return Fraction()
    return mobius(w) * omega * Fraction(1, 2) ** (omega - 1) / V


def convolution_checks(smoke, failures):
    limit = 60 if smoke else 500
    cutoffs = (1, 2) if smoke else (1, 2, 3, 5)
    Z_values = (3,) if smoke else (2, 3, 5, 11)
    counts = defaultdict(int)
    for n, U, V in product(range(1, limit + 1), cutoffs, cutoffs):
        initial = mangoldt_vector(n) if n <= V else {}
        first, second, third = defaultdict(Fraction), defaultdict(Fraction), defaultdict(Fraction)
        for d in divisors(n):
            if d <= U:
                add_log(first, log_vector(n // d), mobius(d))
                for ell in divisors(n // d):
                    if ell <= V:
                        add_log(second, mangoldt_vector(ell), mobius(d))
            if d > U and n // d > V:
                add_log(third, c_vector(n // d, V), mobius(d))
        answer = defaultdict(Fraction, initial)
        add_log(answer, first)
        add_log(answer, second, -1)
        add_log(answer, third)
        require(dict(answer) == mangoldt_vector(n), failures, 'vaughan_convolution', n=n, U=U, V=V)
        for Z in Z_values:
            sifted = defaultdict(Fraction)
            if n <= V:
                add_log(sifted, mangoldt_vector(n), rough(n, Z))
            for d in divisors(n):
                if d <= U:
                    add_log(sifted, log_vector(n // d), mobius(d) * rough(d, Z) * rough(n // d, Z))
                    for ell in divisors(n // d):
                        if ell <= V:
                            add_log(sifted, mangoldt_vector(ell),
                                    -mobius(d) * rough(d * ell, Z) * rough(n // (d * ell), Z))
                if d > U and n // d > V:
                    add_log(sifted, c_vector(n // d, V), mobius(d) * rough(d, Z) * rough(n // d, Z))
            expected = defaultdict(Fraction)
            add_log(expected, mangoldt_vector(n), rough(n, Z))
            require(dict(sifted) == dict(expected), failures, 'sifted_vaughan_convolution', n=n, U=U, V=V, Z=Z)
            counts['sifted_coefficients'] += 1
        coefficient = c_vector(n, V)
        logn = log_vector(n)
        require(all(0 <= value <= logn[p] for p, value in coefficient.items()), failures, 'cV_log_coefficient_bound', n=n, V=V)
        counts['vaughan_coefficients'] += 1
    factor_limit = 10 if smoke else 40
    for m, n, Z in product(range(1, factor_limit + 1), range(1, factor_limit + 1), Z_values):
        require(rough(m * n, Z) == rough(m, Z) * rough(n, Z), failures, 'rough_complete_multiplicativity', m=m, n=n, Z=Z)
        counts['multiplicative_cases'] += 1
    corrections = []
    cases = [(13, 3, 26, 'constant')]
    if not smoke:
        cases += [(260, 11, 390, 'reflected'), (260, 11, 520, 'reflected')]
    for y, Z, endpoint, weight_kind in cases:
        H = 2 * y
        prime_sum, sifted, removed_small, higher_all, higher_large = [defaultdict(Fraction) for _ in range(5)]
        U = 1
        while (U + 1) ** 5 <= y:
            U += 1
        require(U ** 5 <= y < (U + 1) ** 5, failures, 'exact_fifth_root_cutoff', y=y, U=U)
        T1, T2, T3 = [defaultdict(Fraction) for _ in range(3)]
        for n in range(y + 1, endpoint + 1):
            weight = Fraction(1) if weight_kind == 'constant' else reflected_weight(n, H)
            for d in divisors(n):
                if d <= U:
                    add_log(T1, log_vector(n // d), mobius(d) * rough(d, Z) * rough(n // d, Z) * weight)
                    for ell in divisors(n // d):
                        if ell <= U:
                            add_log(T2, mangoldt_vector(ell), mobius(d) * rough(d * ell, Z) *
                                    rough(n // (d * ell), Z) * weight)
                if d > U and n // d > U:
                    add_log(T3, c_vector(n // d, U), mobius(d) * rough(d, Z) * rough(n // d, Z) * weight)
            fs = factors(n)
            if len(fs) == 1:
                add_log(prime_sum, {n: 1}, weight)
            value = mangoldt_vector(n)
            if not value:
                continue
            base = next(iter(value))
            add_log(sifted, value, rough(n, Z) * weight)
            if base <= Z:
                add_log(removed_small, value, weight)
            if len(fs) >= 2:
                add_log(higher_all, value, weight)
                if base > Z:
                    add_log(higher_large, value, weight)
        restored = defaultdict(Fraction, sifted)
        add_log(restored, removed_small)
        add_log(restored, higher_all, -1)
        require(dict(restored) == dict(prime_sum), failures, 'both_prime_power_corrections', y=y, Z=Z, endpoint=endpoint)
        summed_convolution = defaultdict(Fraction, T1)
        add_log(summed_convolution, T2, -1)
        add_log(summed_convolution, T3)
        require(dict(summed_convolution) == dict(sifted), failures,
                'actual_partial_dyad_T1_T2_T3', y=y, Z=Z, endpoint=endpoint, U=U)
        require(reflected_weight(H, H) == 0, failures, 'reflected_positive_endpoint')
        corrections.append({'H': H, 'y': y, 'Z': Z, 'endpoint': endpoint, 'weight': weight_kind,
                            'U_V_exact_floor_fifth_root': U, 'T1': dict(T1), 'T2': dict(T2), 'T3': dict(T3),
                            'small_base_restoration': dict(removed_small), 'all_higher_power_removal': dict(higher_all),
                            'large_base_higher_powers': dict(higher_large)})
        counts['prime_correction_cases'] += 1
    require(rough(16, 3) == 0 and rough(25, 3) == 1 and mangoldt_vector(16) == {2: 1}
            and mangoldt_vector(25) == {5: 1}, failures, 'both_prime_power_categories_negative_control')
    require(rough(9, 2) == 1 and mangoldt_vector(9) == {3: 1} and len(factors(9)) == 2,
            failures, 'author_second_prime_power_correction_witness')
    return {'counts': dict(counts), 'prime_power_correction_records': corrections,
            'negative_controls': {'small_base_power': 16, 'large_base_power': 25, 'Z': 3,
                                  'author_second_correction': {'n': 9, 'Z': 2, 'sifted_mangoldt': {3: 1}, 'prime_only': {}},
                                  'positivity_endpoint': {'H': 520, 'n': 520, 'F': reflected_weight(520, 520)}}}


def expansion_checks(smoke, failures):
    counts = defaultdict(int)
    u_limit, depth_limit = (6, 3) if smoke else (20, 8)
    for u, R, rho, V in product(range(u_limit + 1), range(1, depth_limit + 1),
                                  (Fraction(1, 4), Fraction(1, 2), Fraction(3, 4)),
                                  (Fraction(1, 3), Fraction(7, 11))):
        exact = u * rho ** (u - 1) / V if u else Fraction()
        polynomial = sum(((j + 1) * (rho - 1) ** j * math.comb(u, j + 1) / V
                          for j in range(R) if j + 1 <= u), Fraction())
        remainder = exact - polynomial
        positive_bound = ((R + 1) * (1 - rho) ** R * math.comb(u, R + 1) / V
                          if R + 1 <= u else Fraction())
        require((-1) ** R * remainder >= 0 and abs(remainder) <= positive_bound,
                failures, 'finite_taylor_remainder', u=u, R=R, rho=rho, V=V)
        counts['taylor_cases'] += 1
    for u, R in product(range(u_limit + 1), range(depth_limit + 1)):
        truncated = sum((-1) ** j * math.comb(u, j) for j in range(min(R, u) + 1))
        target = int(u == 0)
        bound = math.comb(u, R + 1) if R + 1 <= u else 0
        require(abs(truncated - target) <= bound and (-1) ** R * (truncated - target) >= 0,
                failures, 'bonferroni_positive_error', u=u, R=R)
        counts['bonferroni_cases'] += 1
    primes = (3, 5, 7, 11)
    for denominator in ('p', 'p_minus_1'):
        weights = [Fraction(1, p if denominator == 'p' else p - 1) for p in primes]
        total = sum(weights, Fraction())
        for degree in range(6):
            mass = sum((math.prod(row) for row in combinations(weights, degree)), Fraction())
            require(mass <= total ** degree / math.factorial(degree), failures,
                    'positive_reciprocal_coefficient_mass', denominator=denominator, degree=degree)
            counts['reciprocal_mass_cases'] += 1
    v_limit = 40 if smoke else 200
    for A, v in product((1, 3, 5, 7, 15, 21, 35, 105), range(1, v_limit + 1)):
        allowed = set(factors(A))
        rhs = mobius(A) * sum(mobius(v // b) for b in divisors(v) if set(factors(b)) <= allowed)
        require(mobius(A * v) == rhs, failures, 'smooth_power_mobius_identity', A=A, v=v)
        counts['smooth_power_cases'] += 1
    wrong = mobius(3) * sum(mobius(9 // b) for b in divisors(9)
                            if set(factors(b)) <= {3} and mobius(b) != 0)
    require(wrong == 1 and mobius(27) == 0, failures, 'squarefree_b_negative_control')
    return {'counts': dict(counts), 'negative_control': {'A': 3, 'v': 9, 'correct': 0, 'squarefree_b_only': wrong,
                                                        'essential_prime_power_b': 9}}


def residue_checks(smoke, failures):
    H_values = (6, 8, 18) if smoke else range(2, 101, 2)
    q_values = (1, 5, 11) if smoke else (1, 5, 7, 11, 13)
    small = (1, 3, 5) if smoke else (1, 3, 5, 7, 15, 21)
    b_limit, j_limit = (9, 7) if smoke else (25, 15)
    counts = defaultdict(int)
    for H, q, r, d in product(H_values, q_values, small, small):
        if math.gcd(q, H) != 1 or math.gcd(d, r * H) != 1:
            continue
        if q > 1 and min(factors(q)) <= max(factors(r * d), default=1):
            continue
        g = math.gcd(r, H)
        modulus = q * r // g
        allowed = set(factors(d * g))
        for b in range(1, b_limit + 1):
            if not set(factors(b)) <= allowed:
                continue
            require(math.gcd(d * b, modulus) == math.gcd(H // g, modulus) == 1,
                    failures, 'reduced_inverse_exists', H=H, q=q, r=r, d=d, b=b, g=g)
            residue = (H // g) * pow(d * b, -1, modulus) % modulus
            odd_residue = residue if residue % 2 else residue + modulus
            require(math.gcd(odd_residue, 2 * modulus) == 1, failures, 'odd_class_reduced', H=H, q=q, r=r, d=d, b=b)
            direct = []
            denominator = d * g * b
            for j in range(1, j_limit + 1, 2):
                w = H - q * r * j
                if w > 0 and w % denominator == 0:
                    t = w // denominator
                    require(t % (2 * modulus) == odd_residue and t % 2 == 1,
                            failures, 'reflected_reduced_class', H=H, q=q, r=r, d=d, b=b, j=j, t=t)
                    direct.append(t)
                    counts['positive_reflected_solutions'] += 1
            lower = max(1, -(-(H - q * r * j_limit) // denominator))
            upper = (H - q * r) // denominator
            reverse = [t for t in range(lower, upper + 1) if t % (2 * modulus) == odd_residue]
            require(sorted(direct) == reverse and direct == sorted(direct, reverse=True), failures,
                    'reversed_interval_bijection', H=H, q=q, r=r, d=d, b=b)
            counts['residue_parameter_cases'] += 1
            counts['b_shares_g_cases'] += math.gcd(b, g) > 1
            counts['modulus_one_before_oddness'] += modulus == 1
    # Finite witnesses keep each hypothesis and the reflected orientation visible.
    require(78 - 11 * 3 == 5 * 3 * 3 and math.gcd(3, 3) > 1, failures, 'shared_b_g_allowed_witness')
    require(math.gcd(9, 33) == 3 and math.gcd(1, 22) == 1, failures, 'omitted_g_nonreduced_witness')
    require(math.gcd(10 * pow(3, -1, 5) % 5, 5) != 1, failures, 'noncoprime_q_negative_control')
    require(math.gcd(7 * 3, 5 * 9 // math.gcd(9, 6)) != 1, failures, 'nonsquarefree_r_negative_control')
    require(all((8 - 5 * 3 * j) % 3 != 0 for j in range(1, 16, 2)), failures, 'common_r_d_impossible')
    require(2 - 1 * 1 * 2 == 0 and 2 % 2 == 0, failures, 'zero_even_j_excluded')
    require(32 - 2 == 3 * 10 and 2 % 2 == 10 % 2 == 0 and math.gcd(3, 32) == 1,
            failures, 'author_undoubled_class_parity_witness')
    require((32 * pow(3, -1, 2)) % 2 == 0, failures, 'wrong_even_residue_doubled_directly')
    require((78 - 5, 78 - 15) == (73, 63) and (78 + 5, 78 + 15) == (83, 93),
            failures, 'reflected_sign_order_negative_control')
    margin = Fraction(19, 40) - Fraction(2, 5)
    epsilon = Fraction(1, 100)
    require(margin == Fraction(3, 40) and margin > epsilon, failures, 'rational_BV_exponent_margin')
    scale_records = []
    for s, B in product((16, 32, 64), range(1, 9)):
        # y=2^(200s); log y <=200s since log2<1. These compare only
        # explicit rational bounds, not an analytic theorem's validity.
        ratio = 2 ** (13 * s - 1)
        log_power_upper = (200 * s) ** B
        require(ratio >= log_power_upper, failures, 'finite_retained_modulus_log_power', s=s, B=B)
        scale_records.append({'s': s, 'B': B, 'ratio_power_of_2': 13 * s - 1,
                               'log_power_upper_bound': log_power_upper})
        counts['finite_log_power_cases'] += 1
    return {'counts': dict(counts), 'exponent_margin': margin, 'retained_subpower_epsilon': epsilon,
            'finite_log_power_records': scale_records,
            'negative_controls': {'omitted_g': {'H': 78, 'q': 11, 'r': 3, 'd': 5,
                                               'unextracted_residue': 9, 'unextracted_modulus': 33},
                                  'b_may_share_g': {'H': 78, 'q': 11, 'r': 3, 'd': 5, 'g': 3, 'b': 3, 'j': 1, 't': 1},
                                  'nonsquarefree_r': {'H': 6, 'q': 5, 'r': 9, 'd': 7, 'b': 3},
                                  'noncoprime_q': {'H': 10, 'q': 5, 'r': 1, 'd': 3},
                                  'sign_and_order': {'H': 78, 'q': 5, 'j': (1, 3),
                                                      'reflected_t': (73, 63), 'wrong_plus_t': (83, 93)},
                                  'zero_endpoint': {'H': 2, 'q': 1, 'r': 1, 'j': 2, 'w': 0},
                                  'author_undoubled_parity': {'H': 32, 'q': 1, 'r': 1, 'd': 3, 'g': 1,
                                                            'b': 1, 'j': 2, 't': 10, 'wrong_doubled_residue': 0,
                                                            'correct_odd_class_modulo_2': 1}}}


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
    source_hash = hashlib.sha256((directory / 'statement.md').read_bytes()).hexdigest()
    if source_hash != FROZEN_STATEMENT_SHA256:
        raise SystemExit('Frozen statement hash mismatch.')
    packet = json.loads(args.packet.read_text(encoding='utf-8-sig'))
    if packet['step']['id'] != 'finite-check' or not packet.get('upstream'):
        raise SystemExit('Actual populated finite-check packet required.')
    started = time.perf_counter()
    failures = []
    comparisons = {'convolution_and_corrections': convolution_checks(args.smoke, failures),
                   'finite_expansions': expansion_checks(args.smoke, failures),
                   'reduced_reflected_class': residue_checks(args.smoke, failures)}
    result = {'mode': 'smoke' if args.smoke else 'bounded_final', 'passed': not failures,
              'runtime_seconds': time.perf_counter() - started, 'python': platform.python_version(),
              'platform': platform.platform(), 'code_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'statement_sha256': source_hash,
              'packet_sha256': hashlib.sha256(args.packet.read_bytes()).hexdigest(),
              'comparisons': comparisons, 'failures': failures,
              'scope': 'Exact finite coefficients and residue classes only; no BV, Mellin, asymptotic Type I or Goldbach certification.'}
    if not args.smoke:
        (directory / 'finite-results.json').write_text(json.dumps(result, indent=2, default=encode) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2, default=encode))
    return 0 if not failures else 1


if __name__ == '__main__':
    raise SystemExit(main())
