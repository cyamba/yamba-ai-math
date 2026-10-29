#!/usr/bin/env python3
"""Explicit constants for the counting algorithm of openai/math result 378 (subresult SR-05).

We evaluate the three costs of the preprint's overview algorithm (Section 2.6, display (2.9)):

    Taylor data      sum_{j <= q} 2^j C(n, j),   q = floor(3 n R / Q)
    measurements     (2D + 1)^(2 tau n)
    one group        2^(2n / r)

for the bounded-occurrence 3-CNF setting (n variables, at most 3 occurrences each), ignoring
polynomial factors, and report the exponent e = log2(time) / n as a function of
lambda = log2(n). Two parameter regimes:

  * "preprint": the explicit choices (2.12): r = floor(sqrt(lam)/nu^2), Q = floor(lam/(128 nu)),
    R = 4 ceil(sqrt(lam)), tau = 1/(r lam), D = r^(2Q), with lam = ceil(log2 n),
    nu = ceil(log2 lam), together with the validity conditions stated there
    (r >= 2, R >= 32, 6R <= Q, 12 D^2 <= n, 2 Q r^2 <= n).
  * "optimized": the best integer choice of (r, Q, R) subject to the same structural
    constraints, using the exact binomial tail of the interpolation window
    (c/D = Pr[Bin(Q, p) not in I], p = (r-1)/(2r)) and tau = 3 r c / D.

For each regime we find the smallest lambda at which e drops below 1 (beats exhaustive
search), 1/2 (beats Grover's quadratic speedup, 2^(n/2)) and log2(1.30704) (beats the
PPSZ bound of Hertli for 3-SAT). These are thresholds for the analysed cost bound, not
for any implementation; the bounds of the preprint's general k-CNF reduction and of its
Appendix C are larger still (see the appendix-C check at the end).

Usage: python3 galactic_thresholds.py --out results/galactic_thresholds.json
"""

from __future__ import annotations

import argparse
import json
import math
from functools import lru_cache
from pathlib import Path

LOG2_PPSZ = math.log2(1.30704)


def h2(x: float) -> float:
    if x <= 0 or x >= 1:
        return 0.0
    return -x * math.log2(x) - (1 - x) * math.log2(1 - x)


def taylor_bits_per_n(rho: float) -> float:
    """(1/n) log2 sum_{j <= rho n} 2^j C(n, j), asymptotically."""
    # maximizer of j + log2 C(n,j) is j = 2n/3; the sum is 3^n beyond it
    if rho >= 2 / 3:
        return math.log2(3)
    return rho + h2(rho)


@lru_cache(maxsize=None)
def window_tail(Q: int, R: int, r: int) -> float:
    """Pr[Bin(Q, p) outside the R consecutive integers centred at Qp], p = (r-1)/(2r)."""
    p = (r - 1) / (2 * r)
    a0 = math.floor(Q * p - (R - 1) / 2)
    lo, hi = max(a0, 0), min(a0 + R - 1, Q)
    # log-space binomial pmf
    logp, logq = math.log(p), math.log1p(-p)

    def pmf(j: int) -> float:
        return math.exp(math.lgamma(Q + 1) - math.lgamma(j + 1) - math.lgamma(Q - j + 1)
                        + j * logp + (Q - j) * logq)

    # sum the two tails directly (no cancellation); terms decay geometrically away from lo/hi
    total = 0.0
    for j in range(lo - 1, -1, -1):
        term = pmf(j)
        total += term
        if term < total * 1e-18:
            break
    for j in range(hi + 1, Q + 1):
        term = pmf(j)
        total += term
        if term < total * 1e-18:
            break
    return total


def exponent(lam: float, r: int, Q: int, R: int, tau: float) -> float:
    rho = 3 * R / Q
    log2D = 2 * Q * math.log2(r)
    meas = 2 * tau * (log2D + 1)  # log2(2D+1) <= log2 D + 1
    group = 2 / r
    return taylor_bits_per_n(rho) + meas + group


def preprint_params(lam: int) -> dict:
    nu = math.ceil(math.log2(lam))
    r = math.floor(math.sqrt(lam) / nu ** 2)
    Q = math.floor(lam / (128 * nu))
    R = 4 * math.ceil(math.sqrt(lam))
    valid = r >= 2 and R >= 32 and 6 * R <= Q
    # 12 D^2 <= n  <=>  log2 12 + 4 Q log2 r <= lam ; 2 Q r^2 <= n
    if valid:
        valid = math.log2(12) + 4 * Q * math.log2(r) <= lam and math.log2(2 * Q * r * r) <= lam
    out = {"lambda": lam, "nu": nu, "r": r, "Q": Q, "R": R, "valid": valid}
    if valid:
        tau = 1 / (r * lam)
        out["tau"] = tau
        out["exponent"] = exponent(lam, r, Q, R, tau)
        # the preprint's required tail bound 2 e^{-R^2/(8Q)} <= tau/(3r)
        out["tail_condition"] = 2 * math.exp(-R * R / (8 * Q)) <= tau / (3 * r)
    return out


def optimized(lam: float, r_values=None) -> dict:
    """Best feasible (r, Q, R) at log2 n = lam under the structural constraints."""
    best = None
    r_values = r_values or [2, 3, 4, 5, 6, 8, 10, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96, 128,
                            160, 192, 256, 384, 512, 768, 1024]
    for r in r_values:
        qmax = math.floor((lam - math.log2(12)) / (4 * math.log2(r)))
        if qmax < 2:
            continue
        # scan Q on a geometric grid up to qmax, R on a grid
        qs = sorted({qmax} | {max(2, int(qmax * f)) for f in (0.25, 0.4, 0.55, 0.7, 0.85, 1.0)})
        for Q in qs:
            if math.log2(2 * Q * r * r) > lam:
                continue
            lo, hi = 1, Q + 1
            # tail decreases in R; find the R minimizing the exponent by scanning a grid
            for R in sorted({max(1, int(Q * f)) for f in
                             (0.002, 0.004, 0.006, 0.008, 0.01, 0.013, 0.016, 0.02, 0.025, 0.03,
                              0.04, 0.05, 0.06, 0.08, 0.1, 0.13, 0.16, 0.2, 0.25)}):
                if R > hi or R < lo:
                    continue
                tail = window_tail(Q, R, r) if Q <= 200000 else 2 * math.exp(-R * R / (8 * Q))
                tau = 3 * r * tail * r / (r - 1)  # c/D = (r-1)/r * tail <= tau/(3r)
                e = exponent(lam, r, Q, R, tau)
                if best is None or e < best["exponent"]:
                    best = {"lambda": lam, "r": r, "Q": Q, "R": R, "tau": tau,
                            "window_tail": tail, "exponent": e,
                            "taylor": taylor_bits_per_n(3 * R / Q),
                            "measurements": 2 * tau * (2 * Q * math.log2(r) + 1),
                            "groups": 2 / r}
    return best or {"lambda": lam, "exponent": None}


def first_crossing(fn, targets, lam_grid):
    hits = {}
    prev = None
    for lam in lam_grid:
        res = fn(lam)
        e = res.get("exponent")
        if e is None:
            continue
        for name, target in targets.items():
            if name not in hits and e < target:
                hits[name] = res
        prev = res
        if len(hits) == len(targets):
            break
    return hits, prev


def appendix_c_threshold() -> dict:
    """Appendix C requires lambda^{4/5} <= u_0 = floor(eps * lambda), eps = 1/(128*1024)."""
    eps = 1 / (128 * 1024)
    # lambda^{1/5} >= 1/eps  <=>  lambda >= eps^{-5}
    lam_min = (1 / eps) ** 5
    return {"epsilon": eps, "condition": "lambda^(4/5) <= floor(eps*lambda)",
            "lambda_min": lam_min, "log2_lambda_min": math.log2(lam_min),
            "meaning": "the Appendix C parameter inequalities can hold only when log2(s) >= 2^85"}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path,
                        default=Path(__file__).parent / "results/galactic_thresholds.json")
    args = parser.parse_args()
    targets = {"beats_2^n": 1.0, "beats_grover_2^(n/2)": 0.5, "beats_ppsz_1.30704^n": LOG2_PPSZ}

    # preprint regime: lambda integer; validity starts around 2^34
    pre_grid = [int(2 ** (k / 8)) for k in range(8 * 20, 8 * 64)]
    pre_hits, _ = first_crossing(preprint_params, targets, pre_grid)
    first_valid = next((preprint_params(l) for l in pre_grid if preprint_params(l)["valid"]), None)

    opt_grid = [int(10 ** (k / 20)) for k in range(20 * 3, 20 * 12)]
    opt_hits, _ = first_crossing(optimized, targets, opt_grid)

    samples = {f"1e{k}": optimized(10 ** k) for k in range(4, 13)}
    report = {
        "description": __doc__.strip().splitlines()[0],
        "preprint_first_valid": first_valid,
        "preprint_crossings": pre_hits,
        "optimized_crossings": opt_hits,
        "optimized_samples": samples,
        "appendix_c": appendix_c_threshold(),
        "log2_ppsz": LOG2_PPSZ,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=1) + "\n")
    print(json.dumps({"first_valid": first_valid,
                      "preprint": {k: (v["lambda"], round(v["exponent"], 4)) for k, v in pre_hits.items()},
                      "optimized": {k: (v["lambda"], round(v["exponent"], 4), v["r"], v["Q"], v["R"])
                                    for k, v in opt_hits.items()},
                      "appendix_c": report["appendix_c"]["log2_lambda_min"]}, indent=1))
    for k, v in samples.items():
        print(k, {kk: (round(vv, 4) if isinstance(vv, float) else vv) for kk, vv in v.items()})


if __name__ == "__main__":
    main()
