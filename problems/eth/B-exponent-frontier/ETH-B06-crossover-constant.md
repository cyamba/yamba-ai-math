---
id: ETH-B06
source: YMB-ETH-04 ("Explicit crossover constant C_3 versus PPSZ")
category: exponent-frontier
status: open
---

# ETH-B06: Explicit constants and the crossover with PPSZ

## Question

For 3-SAT find explicit `C` with time `2^{C n log log n / sqrt(log n)}` (or the Lean exponent) and the
crossover `n*` beyond which it beats the best exponential algorithms: randomized PPSZ-type `O(1.307^n)`
(Jiang-Cai 2026 preprint, cited in the paper), deterministic `O(1.32793^n)` (Liu 2018).

## Notes

* The sheet's equation `C_3 n / log_2 n = 0.386 n` uses the wrong exponent; with `sqrt`:
  `C sqrt-scale`: solve `C (log log n)^2 / sqrt(log n) = log_2(1.307) ~ 0.386`.
* The paper's explicit parameters (`Q = floor(lambda / (128 nu))`, `D <= (2n)^{1/128}`, `R >= 32`,
  `6R <= Q`) already force `lambda = log_2 n` in the tens of thousands before the asymptotics engage, so
  `n*` is astronomically large (`log_2 n* > 10^4` is a safe guess; compute it).
* Useful output: a table of the three cost terms for `log_2 n in {10^3, ..., 10^9}` with the paper's
  constants, and the effect of the constant-factor gains available in [ETH-B03](ETH-B03-polynomial-row-routing.md).
