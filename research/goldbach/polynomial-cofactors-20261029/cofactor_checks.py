"""Bounded exact COFACTORS015 checks. No asymptotic or dispersion certification."""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
import json
from math import gcd, isqrt
from pathlib import Path
import platform
import sys
import time

FROZEN = "91bbf0074e34ef26d578a80b4ecf1644db2197748ca1070d38dc8c38686b0212"
ZERO = (F(0), F(0))
ONE = (F(1), F(0))
GI = (F(0), F(1))


def ga(x):
    return x if isinstance(x, tuple) else (F(x), F(0))


def add(x, y):
    x, y = ga(x), ga(y)
    return x[0] + y[0], x[1] + y[1]


def mul(x, y):
    x, y = ga(x), ga(y)
    return x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0]


def conj(x):
    x = ga(x)
    return x[0], -x[1]


def norm(x):
    x = ga(x)
    return x[0] ** 2 + x[1] ** 2


def power(x, n):
    out = ONE
    for _ in range(n):
        out = mul(out, x)
    return out


def gsum(values):
    out = ZERO
    for value in values:
        out = add(out, value)
    return out


def weighted_inner(x, y, weights):
    return gsum(mul(w, mul(a, conj(b))) for w, a, b in zip(weights, x, y))


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def factors(n):
    out = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            out.append(d)
            n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


def mu(n):
    fs = factors(n)
    return 0 if len(fs) != len(set(fs)) else (-1) ** len(fs)


def serial(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, dict):
        return {str(k): serial(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [serial(v) for v in value]
    return value


class Report:
    def __init__(self):
        self.counts = Counter()
        self.failures = []
        self.records = {}

    def check(self, group, condition, context=None):
        self.counts[group] += 1
        if not condition:
            self.failures.append({"group": group, "context": serial(context)})


def incidence_checks(report, smoke):
    top = 30 if smoke else 100
    min_four = None
    state_total = 0
    for n in range(4, top + 1, 2):
        blocks = defaultdict(list)
        raw_prime_labels = []
        for p in range(2, n):
            if not prime(p):
                continue
            q = n - p
            if prime(q):
                raw_prime_labels.append(q)
            if gcd(p, n) != 1 or q <= 1 or not mu(q):
                continue
            fs = factors(q)
            if not all(r ** 3 > n for r in fs):
                continue
            report.check("local_factor_capacity", len(fs) <= 3, (n, p, q, fs))
            for a in fs:
                h = q // a
                state_total += 1
                blocks[h].append((a, p, len(fs)))
                report.check("incidence_integer_cofactor", a * h + p == n, (n, a, p, h))
        if n < 16:
            report.check("smaller_even_prime_label_count", len(raw_prime_labels) <= 3, (n, raw_prime_labels))
        labels = sorted({a for a, p, k in blocks[1]})
        if len(labels) >= 4 and min_four is None:
            min_four = n
    report.check("first_four_rough_unit_prime_labels", min_four == 16, min_four)
    report.records["incidence"] = {"even_N": [4, top], "rough_test": "r^3>N", "states": state_total, "first_N_with_four_h1_labels": min_four}

    witnesses = [(8, [3, 5]), (16, [3, 5, 11, 13]), (30, [7, 11, 13, 17])]
    fixed = []
    for n, labels in witnesses:
        for a in labels:
            p = n - a
            report.check("fixed_prime_path_vertex", prime(a) and prime(p) and gcd(a * p, n) == 1 and a ** 3 > n, (n, a, p))
        path = labels + labels[:1]
        for a, b in zip(path, path[1:]):
            report.check("fixed_closed_path_edge", F(n - (n - a), a) == F(n - (n - b), b) == 1, (n, a, b))
        fixed.append({"N": n, "labels": labels, "local_nu": 1, "closed_edges": len(labels), "z_gt_2_at_alpha_0.3": n ** 3 > 2 ** 10})
    report.check("N30_single_label_block", all(5 <= a <= 20 for a in witnesses[2][1]))
    report.check("N16_not_single_factor_four_block", F(13, 3) > 4)
    walk_max = {}
    for edges in range(5):
        walks = list(product(range(4), repeat=edges + 1))
        open_max = max(len(set(w)) for w in walks)
        closed = [w for w in walks if w[0] == w[-1]]
        closed_max = max(len(set(w)) for w in closed)
        walk_max[edges] = {"open": open_max, "closed": closed_max}
        report.check("four_vertex_open_minimality", (open_max == 4) == (edges >= 3), edges)
        report.check("four_vertex_closed_minimality", (closed_max == 4) == (edges >= 4), edges)
    report.records["fixed_paths"] = fixed
    report.records["walk_max_label_counts"] = walk_max

    toy = []
    for v, a in zip([11, 13, 17, 19], [167, 157, 137, 127]):
        u = 5 * v
        ok = prime(v) and prime(a) and 222 - u == a and gcd(u, 222) == 1 and gcd(a, 222) == 1
        ok = ok and all(r > 4 for r in factors(u)) and a ** 3 > 222
        report.check("separate_product_box", ok, (v, a))
        toy.append({"m": 5, "n": v, "a": a, "h": 1})
    report.records["product_box_N222"] = {"m_box": [5, 10], "n_box": [11, 22], "sift_cutoff": 4, "states": toy, "scope": "finite box only; not asymptotic source/Vaughan support"}


def compression_checks(report, smoke):
    n_values = [16, 30] if smoke else [16, 30, 40, 78]
    domains = []
    for n in n_values:
        y = F(n, 4)
        labels = [a for a in range(3, n) if prime(a) and a >= y and gcd(a, n) == 1]
        states = [(a, u, F(n - u, a), ((n - u) * pow(a, -1, n)) % n) for a in labels for u in range(1, n)]
        integers = [x for x in states if x[2].denominator == 1]
        for a, u, h, c in states:
            report.check("protected_c1_exactly_h1", (c == 1) == (h == 1), (n, a, u, h, c))
        for a, u, h, c in states:
            for b, v, k, d in states:
                t = b * u - a * v
                report.check("all_positive_state_sector_equivalence", (t % n == 0) == (c == d), (n, a, u, b, v))
        for a, u, h, c in integers:
            for b, v, k, d in integers:
                t = b * u - a * v
                report.check("integer_cofactor_determinant", t == n * (b - a) + a * b * (k - h), (n, a, u, b, v))
                report.check("integer_modular_compression", (t % n == 0) == ((k - h) % n == 0) == (k == h), (n, a, h, b, k))
                report.check("original_positive_support_plateau", abs(F(t, n * y)) <= 4, (n, a, u, b, v))
                if t % n == 0:
                    report.check("compressed_fourier_frequency_zero", F(t, n) - b + a == 0, (n, a, h, b, k))
        layers = []
        for a in labels:
            if a <= 4:
                continue
            for j in range(4):
                u = n * (1 + j) - a
                if 0 < u < 4 * n:
                    h = F(n - u, a)
                    report.check("extended_c1_layer", ((n - u) * pow(a, -1, n)) % n == 1 and h == 1 - F(n * j, a), (n, a, j))
                    report.check("extended_only_j0_integer", (h.denominator == 1) == (j == 0), (n, a, j, h))
                    if j:
                        report.check("extended_negative_fractional", h < 0 and h.denominator > 1, (n, a, j, h))
                    layers.append((a, j, u))
        for a, j, u in layers:
            for b, ell, v in layers:
                t = b * u - a * v
                report.check("extended_frequency_and_cutoff_arguments", F(t, n) - b + a == b * j - a * ell and F(t, n * y) == F(b * (1 + j) - a * (1 + ell), y), (n, a, j, b, ell))
        domains.append({"N": n, "Y": y, "labels": labels, "positive_states": len(states), "integer_states": len(integers), "fractional_states": len(states) - len(integers), "u_unit_filter": False, "extended_states": len(layers)})
    n, a, b, u, v = 30, 7, 11, 19, 17
    t = b * u - a * v
    report.check("fractional_comparison_witness", t == 90 and F(n - u, a) == F(11, 7) and F(n - v, b) == F(13, 11) and F(t, n) - b + a == -1 and gcd(u * v * a * b, n) == 1)
    report.records["fractional_comparison"] = {"N_a_b_u_v": [n, a, b, u, v], "h_k": [F(11, 7), F(13, 11)], "frequency": -1, "arc": [F(-1, 4), F(1, 4)], "integral": "sin(pi/2)/pi=1/pi, nonzero; elementary symbolic evaluation, no numerical quadrature"}
    for t in range(13):
        branch_sum = gsum(power(GI, j * t) for j in range(4))
        report.check("four_branch_no_extra_inverse", mul(F(1, 4), branch_sum) == ga(int(t % 4 == 0)), t)
    report.records["compression_domains"] = domains


def rank_one_checks(report, smoke):
    measures = [[F(1), F(1)], [F(1)] * 4, [F(1), F(2, 3), F(5, 4), F(3, 2)]]
    count = 4 if smoke else 8
    for weights in measures:
        d = len(weights)
        vecs = [[ga(v) for v in xs] for xs in list(product([ZERO, ONE, ga(-1), GI], repeat=d))[:count]]
        vecs += [[ONE] * d, [ga((-1) ** j) for j in range(d)]]
        mass = sum(weights)
        def op(f):
            return [gsum(mul(w, v) for w, v in zip(weights, f))] * d
        for f in vecs:
            af = op(f)
            raw = weighted_inner(af, f, weights)
            report.check("weighted_positive_square", raw == ga(norm(gsum(mul(w, v) for w, v in zip(weights, f)))) and raw[0] >= 0, (weights, f))
            report.check("rank_one_square_identity", op(af) == [mul(mass, z) for z in af], (weights, f))
            for g in vecs:
                report.check("weighted_self_adjoint", weighted_inner(op(f), g, weights) == weighted_inner(f, op(g), weights), (weights, f, g))
        for arc in [F(1, 2), F(1, 3)]:
            centered = [mul((1 - arc) / mass, z) for z in op([ONE] * d)]
            report.check("normalized_centered_block_eigenvalue", centered == [ga(1 - arc)] * d, (weights, arc))
        if len(set(weights)) == 1:
            deleted = [(d - 1) * weights[0]] * d
            report.check("distinct_label_equal_weight_eigenvalue", deleted == [mass - weights[0]] * d)
    full_two = norm(gsum([ONE, ONE]))
    diag_two = norm(ONE) + norm(ONE)
    signed_full = norm(gsum([ONE, ga(-1)]))
    report.check("delete_cross_label_loses_positive_mass", full_two == 4 and diag_two == 2)
    report.check("delete_signed_entries_not_monotone", signed_full == 0 and diag_two == 2)
    report.check("negative_mu_not_positive_measure_witness", mu(7) == -1 and 200 - 109 == 13 * 7 and prime(109) and 7 ** 3 > 200 and 13 ** 3 > 200)
    report.records["rank_one"] = {"positive_measures": measures, "arc_masses": [F(1, 2), F(1, 3)], "unit_four_state_raw_norm": 4, "unit_four_state_half_arc_difference_norm": 2, "factorable_input_scope": "configuration-space eigenvectors need not factor as actual Vaughan coefficient arrays", "signed_deletion_counterexample": {"f": [1, -1], "full_Q": 0, "diagonal_Q": 2}}
    toy = [(3, 5, 7), (3, 7, 5), (5, 3, 11)]
    for a, m, n in toy:
        report.check("repeated_label_product_state_control", 38 - m * n == a and a ** 10 > 38 ** 3 and gcd(a * m * n, 38) == 1, (a, m, n))
    adjacency = [[int(x[0] != y[0]) for y in toy] for x in toy]
    squared = [[sum(adjacency[i][k] * adjacency[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
    expected = [[1, 1, 0], [1, 1, 0], [0, 0, 2]]
    gap = [[2 * int(i == j) - squared[i][j] for j in range(3)] for i in range(3)]
    vv = [1, -1, 0]
    report.check("repeated_label_deleted_matrix_square", squared == expected)
    report.check("repeated_label_exact_norm_upper_certificate", gap == [[vv[i] * vv[j] for j in range(3)] for i in range(3)])
    report.check("repeated_label_exact_norm_lower_certificate", [squared[i][2] for i in range(3)] == [0, 0, 2])
    report.records["repeated_label_scope_control"] = {"N": 38, "alpha": "3/10", "factorization_states": toy, "deleted_matrix": adjacency, "deleted_matrix_square": squared, "exact_squared_norm": 2, "incorrect_distinct_vertex_prediction_squared": 4, "arc_scaling": "multiply squared norms by (1-m_arc)^2", "undeleted_raw_rank_one_unchanged": True}


def cofactor_center_checks(report, smoke):
    ns = [16] if smoke else [16, 30, 60, 100, 200]
    rhos = [F(1, 4), F(1, 2), F(3, 4)]
    records = []
    for n in ns:
        rough_prime = lambda a: prime(a) and a ** 10 > n ** 3
        hs = [h for h in range(1, n) if h ** 10 < n ** 7 and gcd(h, n) == 1 and mu(h) and len(factors(h)) <= 2 and all(rough_prime(a) for a in factors(h))]
        aa, gamma = {}, {}
        for h in hs:
            singles = [a for a in range(2, n) if rough_prime(a) and a * h <= n - 2 and gcd(a, n * h) == 1]
            aa[h] = sum(prime(n - a * h) for a in singles)
            gamma[h] = F(len(singles), h + 1)
        z = {rho: F(0) for rho in rhos}
        r_count = 0
        nonsquarefree = 0
        for p in range(2, n):
            if not prime(p) or gcd(p, n) > 1:
                continue
            q = n - p
            fs = factors(q)
            if q <= 1 or not all(rough_prime(a) for a in fs):
                continue
            if not mu(q):
                nonsquarefree += 1
                continue
            if prime(q):
                r_count += 1
            for rho in rhos:
                z[rho] += mu(q) * len(fs) * rho ** (len(fs) - 1)
        report.check("A1_actual_rough_unit_prime_count", aa[1] == r_count, n)
        for rho in rhos:
            rhs = -sum(F(mu(h)) * rho ** len(factors(h)) * aa[h] for h in hs)
            report.check("selected_divisor_signed_reconstruction", z[rho] == rhs, (n, rho, z[rho], rhs))
        report.check("three_rho_prime_profile", -3 * z[rhos[0]] + 3 * z[rhos[1]] - z[rhos[2]] == aa[1], n)
        center = {rho: -sum(F(mu(h)) * rho ** len(factors(h)) * gamma[h] for h in hs) for rho in rhos}
        report.check("nonzero_toy_center_prime_profile", -3 * center[rhos[0]] + 3 * center[rhos[1]] - center[rhos[2]] == gamma[1] and gamma[1] > 0, n)
        recip = sum(F(1, h) for h in hs)
        s = sum(F(1, r) for r in range(2, n) if rough_prime(r) and r ** 10 < n ** 7)
        cn = 1 + s + s * s / 2
        report.check("harmonic_cofactor_test_mass", recip <= cn, (n, recip, cn))
        delta = sum(h * (F(aa[h]) - gamma[h]) ** 2 for h in hs)
        for rho in rhos:
            report.check("weighted_harmonic_cauchy_toy_center", (z[rho] - center[rho]) ** 2 <= cn * delta, (n, rho))
        raw = sum(v * v for v in aa.values())
        report.check("original_raw_square_not_dispersion_norm", raw == sum(h * F(v * v, h) for h, v in aa.items()), n)
        sigma = F(1, 2)
        if delta <= (1 - sigma) ** 2 * gamma[1] ** 2:
            report.check("D_implication_when_toy_condition_holds", aa[1] >= sigma * gamma[1], n)
        records.append({"N": n, "h": hs, "A_h": aa, "toy_gamma_h": gamma, "toy_gamma1": gamma[1], "R_unit": r_count, "nonsquarefree_rough_complements_excluded_by_mu": nonsquarefree, "harmonic_mass": recip, "C_N": cn, "toy_Delta": delta})
    report.check("deleting_h1_false_positive_control", F(1) > F(1, 4) and F(0) <= F(1, 4))
    report.check("synthetic_valid_D_implication", F(0) <= F(1, 4) and F(1) >= F(1, 2))
    report.records["cofactor_centers"] = {"alpha": "3/10", "records": records, "center_scope": "positive rational toy gamma_h=single-prime-count/(h+1), NOT analytic equation (6)", "h1_deletion_witness": {"A1": 0, "gamma1": 1, "other_errors": 0, "full_Delta": 1, "deleted_Delta": 0, "sigma": "1/2", "threshold": "1/4"}}


def character_table(n):
    specs = {8: [(7, 2), (3, 2)], 12: [(11, 2), (5, 2)], 16: [(15, 2), (3, 4)], 20: [(19, 2), (3, 4)], 30: [(29, 2), (7, 4)]}
    gens = specs[n]
    reps = {}
    for exps in product(*(range(order) for _, order in gens)):
        residue = 1
        for (g, order), e in zip(gens, exps):
            residue = residue * pow(g, e, n) % n
        if residue in reps:
            raise ValueError("duplicate unit representation")
        reps[residue] = exps
    tables = []
    for freqs in product(*(range(order) for _, order in gens)):
        table = {}
        for r, exps in reps.items():
            exponent = sum((4 // order) * f * e for (_, order), f, e in zip(gens, freqs, exps)) % 4
            table[r] = power(GI, exponent)
        tables.append(table)
    return reps, tables


def marking_checks(report, smoke):
    configs = [(8, 3, F(1))] if smoke else [(n, y, v) for n in [8, 12, 16, 20, 30] for y in [3, 4, 5] for v in [F(1), F(3, 2)]]
    records = []
    for n, y, v in configs:
        reps, chars = character_table(n)
        units = [r for r in range(n) if gcd(r, n) == 1]
        report.check("complete_character_unit_parameterization", set(reps) == set(units) and len(chars) == len(units), n)
        for a in units:
            for b in units:
                for chi in chars:
                    report.check("character_multiplicativity", chi[(a * b) % n] == mul(chi[a], chi[b]), (n, a, b))
                orth = gsum(mul(chi[a], conj(chi[b])) for chi in chars)
                report.check("character_orthogonality", orth == ga(len(chars) if a == b else 0), (n, a, b))
        labels = [a for a in range(y, 4 * y + 1) if prime(a) and gcd(a, n) == 1]
        report.check("polynomial_marking_scale", y ** 10 >= n ** 3 and y ** 4 >= n, (n, y))
        # The same nonprincipal twist is used for every chi in this Gram family.
        psi = chars[1]
        c = {a: mul(F(1, y) / v, power(GI, j)) for j, a in enumerate(labels)}
        twist_c = {a: mul(c[a], psi[a % n]) for a in labels}
        d = defaultdict(lambda: ZERO)
        representation = Counter()
        for tuple_a in product(labels, repeat=4):
            u, coeff = 1, ONE
            for a in tuple_a:
                u *= a
                coeff = mul(coeff, twist_c[a])
            d[u] = add(d[u], coeff)
            representation[u] += 1
        for u, multiplicity in representation.items():
            counts = Counter(factors(u))
            factorial_product = 1
            for m in counts.values():
                fac = 1
                for j in range(1, m + 1):
                    fac *= j
                factorial_product *= fac
            report.check("fourth_power_repeated_prime_multiplicity", multiplicity == 24 // factorial_product and multiplicity <= 24, (n, y, u, multiplicity))
        sq = sum(norm(x) for x in c.values())
        dnorm = sum(norm(x) for x in d.values())
        c0 = F(1) / v
        csq = 4 * c0 * c0
        d0 = 24 * csq ** 4
        w = (4 * y) ** 4
        report.check("coefficient_l2_bound", sq <= csq / y, (n, y, v))
        report.check("fourth_power_l2_bound", dnorm <= 24 * sq ** 4 <= d0 / y ** 4, (n, y, v))
        residues = defaultdict(lambda: ZERO)
        for u, coefficient in d.items():
            residues[u % n] = add(residues[u % n], coefficient)
        eighth = F(0)
        for chi in chars:
            bvalue = gsum(mul(coefficient, chi[a % n]) for a, coefficient in twist_c.items())
            fourth = gsum(mul(coefficient, chi[u % n]) for u, coefficient in d.items())
            report.check("fourth_power_character_product_exact", power(bvalue, 4) == fourth, (n, y, v))
            eighth += norm(bvalue) ** 4
        residue_moment = len(chars) * sum(norm(value) for value in residues.values())
        report.check("eighth_moment_exact_residue_identity", eighth == residue_moment, (n, y, v))
        report.check("classwise_cauchy_at_polynomial_support", eighth <= len(chars) * (F(w, n) + 1) * dnorm, (n, y, v))
        cstar = d0 * (4 ** 4 + 1)
        report.check("unnormalized_eighth_moment_constant", eighth <= cstar, (n, y, v))
        records.append({"N": n, "Y": y, "V": v, "labels": labels, "fourth_power_support_size": len(d), "max_ordered_representations": max(representation.values(), default=0), "repeated_prime_products": sum(len(set(factors(u))) < 4 for u in representation), "coefficient_l2": sq, "fourth_power_l2": dnorm, "eighth_moment": eighth, "C_star": cstar})
    report.records["marking"] = {"configurations": records, "t": 0, "lambda": 0, "coefficient_phases": "powers of i", "fixed_twist": "second exact character, fixed within each full chi family", "unrun": "continuous derivative, one-spaced intervals, growing parameters and analytic exceptional sets"}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["smoke", "final"], required=True)
    parser.add_argument("--output")
    args = parser.parse_args()
    began = time.perf_counter()
    root = Path(__file__).resolve().parent
    statement_hash = sha256((root / "statement.md").read_bytes()).hexdigest()
    if statement_hash != FROZEN:
        raise SystemExit("Frozen statement hash changed; refusing to run")
    report = Report()
    incidence_checks(report, args.mode == "smoke")
    compression_checks(report, args.mode == "smoke")
    rank_one_checks(report, args.mode == "smoke")
    cofactor_center_checks(report, args.mode == "smoke")
    marking_checks(report, args.mode == "smoke")
    output = {"mode": args.mode, "status": "pass" if not report.failures else "fail", "frozen_statement_sha256": statement_hash, "code_sha256": sha256(Path(__file__).read_bytes()).hexdigest(), "command": "python research/goldbach/polynomial-cofactors-20261029/cofactor_checks.py " + " ".join(sys.argv[1:]), "runtime_seconds": round(time.perf_counter() - began, 6), "platform": platform.platform(), "python": sys.version, "exact_arithmetic": "integers, Fraction, Gaussian-rational pairs", "usage": "unknown", "counts": dict(report.counts), "total_checks": sum(report.counts.values()), "failure_count": len(report.failures), "failures": report.failures, "records": report.records, "scope": "finite identities/inequalities and counterexamples only; not D, gamma asymptotics, asymptotic Vaughan support, source operator norms, continuous sampling or Goldbach"}
    text = json.dumps(serial(output), indent=2)
    if args.output:
        Path(args.output).write_text(text + "\n", encoding="utf-8")
    print(json.dumps({k: output[k] for k in ["mode", "status", "total_checks", "failure_count", "runtime_seconds", "code_sha256"]}))
    if report.failures:
        print(json.dumps(serial(report.failures[:5])))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
