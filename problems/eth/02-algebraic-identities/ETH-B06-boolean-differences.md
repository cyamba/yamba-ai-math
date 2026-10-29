# ETH-B06. Boolean differences: Taylor data from fixed substitutions

| Field | Value |
| --- | --- |
| Category | Algebraic identities |
| Source items | Preprint Lemma 3.2 (implicit in "Stage 4: Taylor jet extraction") |
| Status | **Solved and Lean-verified** (combinatorial core) |
| Depends on the upstream theorem | No |
| Score (I/B/T/L/Lean) | 2 / 1 / 4 / 4 / 5, composite **2.6** |
| Subresults | Lean [`BooleanDifferences.lean`](../lean/EthConsequences/BooleanDifferences.lean): `mobius_insert`, `mobius_inversion`, `boolean_differences` |

## Statement (Lean)

If every $g_x$ has Möbius coefficients vanishing above size $q$, then
$$\sum_xg_x(x)=\sum_{|E|\le q}\sum_{U\subseteq E}(-1)^{|E\setminus U|}\sum_{x\supseteq E}g_x(U),$$
the identity behind the preprint's equation (3.6): each Taylor coefficient of $H(t+z)$ is a
signed sum of $\sum_{j\le q}2^j\binom nj$ restricted sums with the formal input fixed.

## Next step

Feed into [ETH-G01](../07-formalization/ETH-G01-decouple-algebraic-core.md): state the full
counting routine (Proposition 3.3) with an abstract design and prove its output equals the
count, combining this lemma, measurement separation and Hermite uniqueness.

## Resource boundary

Closed; reuse.
