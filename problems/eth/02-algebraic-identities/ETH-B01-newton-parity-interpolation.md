# ETH-B01. Shifted Newton parity interpolation and its off-window defect

| Field | Value |
| --- | --- |
| Category | Algebraic identities |
| Source items | "Problem 1 (YAMBA-378-01): Shifted Newton-basis parity interpolation and exact binomial tail identity" |
| Status | **Solved and Lean-verified**; two claims of the source corrected |
| Depends on the upstream theorem | No |
| Score (I/B/T/L/Lean) | 2 / 1 / 5 / 3 / 5, composite **2.7** |
| Subresults | Lean [`ParityInterpolation.lean`](../lean/EthConsequences/ParityInterpolation.lean): `S_of_le`, `S_succ`, `defect_eq`, `alternating_sum_bounds`, `abs_defect_le` |

## Statement

For $S(k,b)=\sum_{j=0}^b(-2)^j\binom kj$ the Newton interpolant of $(-1)^j$ on
$\{a,\dots,a+b\}$ is $f_{a,b}(a+k)=(-1)^aS(k,b)$, and

* $S(k,b)=(-1)^k$ for $0\le k\le b$ (exactness on the window);
* $S(k+1,b)=-S(k,b)+2(-2)^b\binom kb$ (first-order recurrence);
* $(-1)^kS(k,b)-1=(-1)^{b+1}2^{b+1}\sum_{m<k}(-1)^m\binom mb$ (closed defect);
* $\bigl|(-1)^kS(k,b)-1\bigr|\le2^{b+1}\binom{k-1}b$ for $k\ge1$.

All four are kernel-checked.

## Corrections

The source states $S(k,b)+S(k-1,b)=1+(-2)^b\binom{k-1}b$ (false at $b=1,k=2$) and the defect
$(-1)^a(-2)^{b+1}\binom{k-1}b$ (false at $b=1,k=3$); see
[SR-08](../subresults/SR-08-corrections-to-gemini-summaries.md), rows 6 and 7.

## Remaining questions

1. The defect controls the $\ell_1$ norm of exceptional measurement rows only through the
   number of eigenvectors off the window; the bound above is not needed for the algorithm's
   correctness. Use it instead to quantify robustness of the window family under perturbations.
2. A $q$-analogue for interpolation on Gaussian binomials (no current use).

## Closest work

Alman–Williams interpolation lemma for $(-1)^j$ on an interval (arXiv:1611.05558, level T);
Alman–Guan–Padaki, SODA 2023, Thm 3.7 (level T).

## Resource boundary

Closed for the next iteration; keep as a regression test of the Lean library.
