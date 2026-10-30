---
id: ETH-A01
source: YAMBA-378-01 (sheet "10 consequences", Problem 1); preprint Sec. 2.6 Step 2 and Sec. 4
category: algebraic-core
status: solved (Lean)
score: see ../RANKING.md
---

# ETH-A01: Shifted Newton parity interpolant and its exact defect

## Statement

For `a, b in N` let `f_{a,b}(z) = (-1)^a sum_{j=0}^{b} (-2)^j C(z-a, j)`, a polynomial of degree `b`.
Writing `z = a + k` and `S(b,k) = sum_{j<=b} (-2)^j C(k,j)` we have `f_{a,b}(a+k) = (-1)^a S(b,k)`.

1. Interval identity: `f_{a,b}(z) = (-1)^z` for `z in {a, ..., a+b}`.
2. Exact defect off the interval.
3. Optimality of the interval length for the given degree.

## Results

| Claim | Status | Where |
| --- | --- | --- |
| `(-1)^k S(b,k) = 1` for `0 <= k <= b` | **proved, Lean** | `neg_one_pow_mul_S_of_le` |
| `S(b,k+1) = -S(b,k) - (-2)^{b+1} C(k,b)` | **proved, Lean** | `S_succ_right` |
| `(-1)^k S(b,k) - 1 = -(-2)^{b+1} sum_{m<k} (-1)^{m+1} C(m,b)` | **proved, Lean** | `defect_telescope` |
| First defect: `(-1)^{b+1} S(b,b+1) - 1 = -2^{b+1}` | **proved, Lean** | `first_defect` |
| Sheet formula `Delta(k) = (-1)^a (-2)^{b+1} C(k-1,b)` | **refuted, Lean** (`b=0, k=2`) | `pdf_defect_claim_false` |
| No polynomial of degree `< R` equals `eps (-1)^i` at `R+1` consecutive points | **proved, Lean** | `no_low_degree_parity_match` |

All in [lean/EthProblems/ParityInterpolant.lean](../lean/EthProblems/ParityInterpolant.lean); exact
numerical cross-check in [checks/parity_interpolant_check.py](../checks/parity_interpolant_check.py).

## Why it matters

The last theorem says the paper's interval length `R` for a degree `R-1` interpolant is the maximum possible.
Any improvement of the exponent must therefore change *what* is interpolated (non-consecutive agreement sets,
non-symmetric or non-commutative operators), not just pick a cleverer univariate `f`. This is the
one-dimensional shadow of the barrier in [ETH-B01](../B-exponent-frontier/ETH-B01-sqrt-log-barrier.md).

The defect formula controls entry sizes of `M_0` off the interval, relevant to the bit-length bounds in the
preprint's Appendix E: `|f_{a,b}(a+k)| <= 2^{b+1} C(k, b)` follows from the telescoped sum.

## Next steps (small)

* Lean: package `f_{a,b}` over `Z` with integer arguments `z` (generalised binomials) and prove the interval
  identity in that form.
* Lean: the coefficient bound `|f_{a,b}(a+k)| <= sum_{m<k} 2^{b+1} C(m,b) = 2^{b+1} C(k, b+1)`.
