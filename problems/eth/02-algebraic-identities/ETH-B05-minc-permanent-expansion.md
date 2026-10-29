# ETH-B05. Minc's permanent expansion and bounded-scope Taylor extraction

| Field | Value |
| --- | --- |
| Category | Algebraic identities (side exercise) |
| Source items | "Problem 5 (YAMBA-378-05): formalizing Minc's permanent jet identity" |
| Status | **Classical identity; not used by the preprint**; Lean open |
| Depends on the upstream theorem | No |
| Score (I/B/T/L/Lean) | 1 / 1 / 4 / 1 / 4, composite **1.9** |
| Subresults | none |

## Statement

For $v\times v$ matrices, $\operatorname{per}(X+Y)=\sum_{k}\sum_{|I|=|K|=k}\operatorname{per}(Y[I,K])\operatorname{per}(X[\bar I,\bar K])$.
Consequently, for $B(u)=B_0+uB_1+\dots$ with $u\mid\tilde B(u)=B(u)-B_0$, the coefficient of $u^j$
in $\operatorname{per}B(u)$ involves only $\operatorname{per}(\tilde B[I,K])$ with $|I|\le j$, so
the first $J$ Taylor coefficients need $\binom v{<J}^2$ minors.

## Correction

The preprint computes Taylor data by Boolean differences (Lemma 3.2, Lean
`boolean_differences`), not by permanent expansions; permanents enter only through Curticapean's
reduction for perfect matchings ([SR-08](../subresults/SR-08-corrections-to-gemini-summaries.md),
row 9).

## Lean plan

Expand $\prod_i(B_0+uB_1)_{\sigma(i),i}$ with `Finset.prod_add`, group by the set of indices
using $B_1$; avoid the full Laplace-type bijection by proving only the coefficient statement.

## Resource boundary

Optional; one Lean agent if capacity remains.
