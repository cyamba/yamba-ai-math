# ETH-B03. The orthogonal $\{0,\pm1\}$ eigenbasis of the swap operators

| Field | Value |
| --- | --- |
| Category | Algebraic identities (Lean target) |
| Source items | "Problem 3 (YAMBA-378-03): explicit orthogonal decomposition into $\{0,\pm1\}$ measurement rows" |
| Status | **Proved informally** (preprint Section 2.7, Step 2; Lemma 4.1); statement in the source is correct |
| Depends on the upstream theorem | No |
| Score (I/B/T/L/Lean) | 2 / 1 / 5 / 2 / 5, composite **2.6** |
| Subresults | used by [SR-02](../subresults/SR-02-cube-polynomial-designs.md) (rank computation), validated by [`matrix_validation.py`](../experiments/matrix_validation.py) |

## Statement

On $\mathbb Q^{[r]\times[r]}$ the swap $(a,b)\mapsto(b,a)$ has the orthogonal eigenbasis
$e_{aa}$, $e_{ab}+e_{ba}$ ($a<b$) with eigenvalue $+1$ ($r(r+1)/2$ vectors) and
$e_{ab}-e_{ba}$ ($a<b$) with eigenvalue $-1$ ($r(r-1)/2$ vectors). Tensor products over $Q$
positions give an orthogonal basis of $\mathbb Q^{([r]\times[r])^Q}$ with entries in $\{0,\pm1\}$,
squared norms $2^{w}$ ($w$ = number of off-diagonal factors), and exactly
$\binom Qj\big(\tfrac{r(r-1)}2\big)^j\big(\tfrac{r(r+1)}2\big)^{Q-j}$ vectors with $j$ antisymmetric
factors; each is a simultaneous eigenvector of all $\Pi_s$, so measurement rows taken from it
have $\ell_1$ norm at most $2^{Q}\le D$.

## Lean plan

Bijection $[r]\times[r]\simeq\mathrm{Diag}\sqcup\mathrm{Upper}\sqcup\mathrm{Upper}$, the $2\times2$
Hadamard block, `Matrix.kroneckerMap` for tensor powers; orthogonality via `Matrix.mul_transpose`
of the block-diagonal Hadamard matrix.

## Resource boundary

One Lean agent; pairs naturally with [ETH-B02](ETH-B02-swap-algebra-support-localization.md).
