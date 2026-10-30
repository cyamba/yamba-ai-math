"""Floating-point falsifier screening, followed by exact candidate recounts."""
from __future__ import annotations

import hashlib
import json
import math
import platform
import time
from pathlib import Path

import numpy as np


MAX_N = 100_000


def trial_factors(n: int) -> list[int]:
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


def cube_root(n: int) -> int:
    lo, hi = 0, 1
    while hi**3 <= n:
        hi *= 2
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if mid**3 <= n:
            lo = mid
        else:
            hi = mid
    return lo


def direct(n: int) -> dict:
    z = cube_root(n)
    pp = ss = signed = 0
    for a in range(z + 1, n - z):
        b = n - a
        fa, fb = trial_factors(a), trial_factors(b)
        if not fa or not fb or fa[0] <= z or fb[0] <= z:
            continue
        if len(fa) > 2 or len(fb) > 2:
            raise AssertionError((n, a, b, fa, fb))
        pp += len(fa) == len(fb) == 1
        ss += len(fa) == len(fb) == 2
        signed += (-1) ** len(fa)
    if signed != ss - pp:
        raise AssertionError((n, pp, ss, signed))
    return {"N": n, "cutoff": z, "PP": pp, "SS": ss, "T": signed}


def main() -> None:
    started = time.monotonic()
    spf = np.zeros(MAX_N + 1, dtype=np.int32)
    for p in range(2, math.isqrt(MAX_N) + 1):
        if spf[p] == 0:
            view = spf[p * p :: p]
            view[view == 0] = p
    prime = spf == 0
    prime[:2] = False
    positions = np.arange(MAX_N + 1)
    composite = spf > 0
    semiprime = np.zeros(MAX_N + 1, dtype=bool)
    semiprime[composite] = prime[positions[composite] // spf[composite]]
    cuts = [1] + [int(p) for p in np.flatnonzero(prime) if int(p) ** 3 <= MAX_N]
    length = 1 << (2 * MAX_N).bit_length()
    pp_values = np.full(MAX_N + 1, -1, dtype=np.int64)
    ss_values = np.full(MAX_N + 1, -1, dtype=np.int64)
    max_residual = 0.0
    blocks = []
    for index, cut in enumerate(cuts):
        lo = max(6, cut**3)
        hi = min(MAX_N, cuts[index + 1] ** 3 - 1 if index + 1 < len(cuts) else MAX_N)
        lo += lo % 2
        if lo > hi:
            continue
        inputs = (prime & (positions > cut), semiprime & (spf > cut))
        output = []
        for mask in inputs:
            transformed = np.fft.rfft(mask.astype(np.float64), n=length)
            convolved = np.fft.irfft(transformed * transformed, n=length)
            rounded = np.rint(convolved)
            max_residual = max(max_residual, float(np.max(np.abs(convolved - rounded))))
            output.append(rounded[lo : hi + 1 : 2].astype(np.int64))
        pp_values[lo : hi + 1 : 2] = output[0]
        ss_values[lo : hi + 1 : 2] = output[1]
        blocks.append({"prime_cutoff": cut, "even_N_range": [lo, hi - hi % 2]})
    targets = np.arange(6, MAX_N + 1, 2)
    if np.any(pp_values[targets] < 0) or np.any(ss_values[targets] < 0):
        raise AssertionError("Missing screening block")
    small_checks = 0
    for n in range(6, 202, 2):
        row = direct(n)
        if row["PP"] != pp_values[n] or row["SS"] != ss_values[n]:
            raise AssertionError((row, int(pp_values[n]), int(ss_values[n])))
        small_checks += 1
    signed = ss_values[targets] - pp_values[targets]
    candidates = [int(n) for n in targets[signed >= 0]]
    confirmed = [direct(n) for n in candidates]
    result = {
        "mode": "floating-point candidate search with exact candidate recounts",
        "range_even_N": [6, MAX_N],
        "targets_screened": len(targets),
        "blocks": blocks,
        "fft_length": length,
        "maximum_rounding_residual": max_residual,
        "independent_small_trial_checks": small_checks,
        "numerical_nonnegative_candidates": candidates,
        "exact_candidate_recounts": confirmed,
        "largest_screened_T": int(signed.max()),
        "largest_screened_T_at_N_ge_1000": int(signed[targets >= 1000].max()),
        "python": platform.python_version(),
        "numpy": np.__version__,
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "elapsed_seconds": time.monotonic() - started,
        "limitation": "No infinite claim and no exact all-range convolution certification; a finite exception would not alone refute eventual negativity.",
    }
    destination = Path(__file__).with_name("sign-search-results.json")
    destination.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: result[key] for key in ["targets_screened", "numerical_nonnegative_candidates", "exact_candidate_recounts", "maximum_rounding_residual", "largest_screened_T", "elapsed_seconds"]}))


if __name__ == "__main__":
    main()
