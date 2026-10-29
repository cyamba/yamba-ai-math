# ETH-B02. The commuting swap algebra and support localization

| Field | Value |
| --- | --- |
| Category | Algebraic identities (Lean target) |
| Source items | "Problem 2 (YAMBA-378-02): involution algebra of commuting swaps and support localization" |
| Status | **Proved informally** (preprint Lemmas 4.2, 4.3); Lean open |
| Depends on the upstream theorem | No |
| Score (I/B/T/L/Lean) | 2 / 1 / 5 / 3 / 5, composite **2.7** |
| Subresults | [SR-02](../subresults/SR-02-cube-polynomial-designs.md) (eigenvalue calculus used there) |

## Statement

Let $\pi_1,\dots,\pi_Q$ be commuting involutions in a $\mathbb Q$-algebra, $V_0=\prod_s\pi_s$ and
$W_0=\frac12\sum_s(1-\pi_s)$. Then for every polynomial $f$ of degree $\le d$,
$$V_0f(W_0)\in\operatorname{span}\Big\{\prod_{s\notin S}\pi_s:\ |S|\le d\Big\}.$$
For the swaps $\Pi_s$ on labels $([r]\times[r])^Q$, the matrix $\prod_{s\notin S}\Pi_s$ has entry
$(u,w)$ nonzero only if $a_w(s)=d_u(s)$ for every $s\notin S$, so $M_0=V_0f(W_0)$ satisfies the
support condition $|E_{u,w}|\le\deg f$.

## Proof sketch (for Lean)

$W_0\prod_{s\notin S}\pi_s=\frac12\sum_t\big(\prod_{s\notin S}\pi_s-\prod_{s\notin S\triangle\{t\}}\pi_s\big)$
since $\pi_t^2=1$; induct on $j$ for $V_0W_0^j$, then take linear combinations. The joint
eigenvalue picture: on a simultaneous eigenvector with sign pattern $\varepsilon$,
$\prod_{s\notin S}\pi_s$ acts by $\chi_{[Q]\setminus S}(\varepsilon)$.

## Correction

The source calls $\mathbb Q[\mathbb Z_2^Q]$ "isomorphic to the incidence/Möbius algebra of the
Boolean lattice"; both are isomorphic to $\mathbb Q^{2^Q}$ as algebras, which is true and
uninformative. The useful statement is the span lemma above.

## Lean plan

Abstract commutative ring with commuting involutions; `Finset.induction` on $j$; then the
concrete action on `Fin Q → Fin r × Fin r` and a support lemma in the style of
[`RankBarrier.lean`](../lean/EthConsequences/RankBarrier.lean).

## Resource boundary

One Lean agent, one iteration.
