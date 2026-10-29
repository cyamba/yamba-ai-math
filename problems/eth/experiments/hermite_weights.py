#!/usr/bin/env python3
"""Hermite recovery weights at nodes 1..Q (problem ETH-B04).

The counting algorithm of openai/math result 378 recovers H(0) from the Taylor data
h_{t,r} = [z^r] H(t + z), 1 <= t <= Q, 0 <= r < J, of a polynomial H of degree < QJ:

    H(0) = sum_{t,r} w_{t,r} h_{t,r}.

We compute the weights exactly (rational linear algebra), compare them with the residue formula

    w_{t,r} = -Omega(0) [ (T-t)^{J-1-r} ] 1 / (T Omega_t(T)),
    Omega(T) = prod_s (T - s)^J,  Omega_t(T) = prod_{s != t} (T - s)^J,

and test the denominator claims: the source summary says lcm(1..Q)^(2J) clears all
denominators; we check whether lcm(1..Q)^J already does, and report the exact minimal power.

Usage: python3 hermite_weights.py --out results/hermite_weights.json
"""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path


def solve(mat, rhs):
    n = len(mat)
    a = [row[:] + [r] for row, r in zip(mat, rhs)]
    for c in range(n):
        piv = next(i for i in range(c, n) if a[i][c] != 0)
        a[c], a[piv] = a[piv], a[c]
        inv = 1 / a[c][c]
        a[c] = [x * inv for x in a[c]]
        for i in range(n):
            if i != c and a[i][c] != 0:
                f = a[i][c]
                a[i] = [x - f * y for x, y in zip(a[i], a[c])]
    return [a[i][n] for i in range(n)]


def weights_linear_algebra(Q: int, J: int):
    """Solve sum_{t,r} w_{t,r} [z^r](t+z)^k = 0^k for k < QJ."""
    idx = [(t, r) for t in range(1, Q + 1) for r in range(J)]
    n = len(idx)
    mat = [[Fraction(0)] * n for _ in range(n)]
    rhs = [Fraction(1 if k == 0 else 0) for k in range(n)]
    for k in range(n):
        for col, (t, r) in enumerate(idx):
            # [z^r](t+z)^k = C(k,r) t^(k-r)
            mat[k][col] = Fraction(math.comb(k, r) * t ** (k - r)) if r <= k else Fraction(0)
    sol = solve(mat, rhs)
    return dict(zip(idx, sol))


def series_inverse_prod(t: int, Q: int, J: int, order: int):
    """Coefficients of 1/(T * Omega_t(T)) in powers of u = T - t, up to u^order."""
    # 1/T = 1/(t+u) = sum (-1)^m u^m / t^(m+1)
    coeffs = [Fraction((-1) ** m, t ** (m + 1)) for m in range(order + 1)]
    for s in range(1, Q + 1):
        if s == t:
            continue
        # (T-s)^(-J) = (t-s+u)^(-J) = sum_k C(-J,k) u^k (t-s)^(-J-k)
        d = t - s
        factor = [Fraction(math.comb(J + k - 1, k) * (-1) ** k, 1) / Fraction(d) ** (J + k)
                  for k in range(order + 1)]
        coeffs = [sum(coeffs[i] * factor[m - i] for i in range(m + 1)) for m in range(order + 1)]
    return coeffs


def weights_residue(Q: int, J: int):
    omega0 = Fraction((-1) ** (Q * J) * math.factorial(Q) ** J)
    out = {}
    for t in range(1, Q + 1):
        ser = series_inverse_prod(t, Q, J, J - 1)
        for r in range(J):
            out[(t, r)] = -omega0 * ser[J - 1 - r]
    return out


def lcm_upto(Q: int) -> int:
    v = 1
    for i in range(1, Q + 1):
        v = v * i // math.gcd(v, i)
    return v


def minimal_power(ws, base: int) -> int:
    e = 0
    while any((w * base ** e).denominator != 1 for w in ws):
        e += 1
    return e


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, default=Path(__file__).parent / "results/hermite_weights.json")
    args = parser.parse_args()
    rows = []
    for Q in range(1, 8):
        for J in range(1, 6):
            if Q * J > 30:
                continue
            la = weights_linear_algebra(Q, J)
            rs = weights_residue(Q, J)
            agree = all(la[k] == rs[k] for k in la)
            L = lcm_upto(Q)
            ws = list(la.values())
            e_min = minimal_power(ws, L)
            max_num_bits = max(abs(w.numerator).bit_length() for w in ws)
            max_den_bits = max(w.denominator.bit_length() for w in ws)
            rows.append({"Q": Q, "J": J, "residue_formula_agrees": agree, "lcm": L,
                         "minimal_power_of_lcm_clearing_denominators": e_min,
                         "lcm_pow_J_suffices": e_min <= J, "lcm_pow_2J_suffices": e_min <= 2 * J,
                         "max_numerator_bits": max_num_bits, "max_denominator_bits": max_den_bits,
                         "QJ_log2Q": round(Q * J * math.log2(max(Q, 2)), 1),
                         "sum_of_weights_r0": str(sum(la[(t, 0)] for t in range(1, Q + 1)))})
            print(rows[-1])
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(rows, indent=1) + "\n")


if __name__ == "__main__":
    main()
