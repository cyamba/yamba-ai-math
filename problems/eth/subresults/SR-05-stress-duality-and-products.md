# SR-05. Stress duality for the cube polynomial problem, and products of designs

**Status: proved.** The soundness half of the duality and the product lemma are
**Lean-verified** in [`StressDuality.lean`](../lean/EthConsequences/StressDuality.lean)
(`stress_total_eq_zero`, `moment_collapse`, `sum_edgeW`, `product_edge_good`,
`natDegree_product_le`, `product_eval_zero`); the completeness half is finite-dimensional
linear-algebra duality, proved informally below.
**Novelty: not verified** (see [RANKING.md](../RANKING.md#novelty-ledger)).
**Depends on the upstream theorem: no.**

Feeds: [ETH-A03](../01-algorithmic-core/ETH-A03-point-dependent-designs.md). Setting:
[SR-02](SR-02-cube-polynomial-designs.md).

## Theorem 1 (stress duality)

Fix distinct nonzero nodes $x_1,\dots,x_Q$ and $R\ge1$. Put $\xi_t=(x_t,x_t^2,\dots,x_t^{R-1})$.
For a set $G$ of edges of $\{0,1\}^Q$, a **stress** on $G$ is a weighting $w:G\to\mathbb Q$ such
that at every vertex $v$
$$\sum_{t:\ e(v,t)\in G}w_{e(v,t)}\,\xi_t=0 .$$
Then the following are equivalent:

1. there is a family $(p_v)$ with $\deg p_v<R$, $p_v(0)=1$, in which every edge of $G$ is good;
2. every stress on $G$ has total weight $\sum_{e\in G}w_e=0$.

*Proof of 1 ⇒ 2 (Lean: `stress_total_eq_zero`).* Vanishing moments give, for each vertex,
$\sum_tw_{e(v,t)}p_v(x_t)=\big(\sum_tw_{e(v,t)}\big)p_v(0)$ (`moment_collapse`). Sum over $v$.
The right side is $2\sum_ew_e$. On the left each edge $e=\{u,u+e_t\}$ contributes
$w_e\,(p_u(x_t)+p_{u+e_t}(x_t))=0$ (`sum_edgeW`).

*Proof of 2 ⇒ 1.* Write the conditions as a linear system in the coefficients of the $p_v$:
$\mathrm{ev}_0(p_v)=1$ and $\mathrm{ev}_{x_t}(p_u)+\mathrm{ev}_{x_t}(p_{u+e_t})=0$ for $e\in G$. It
is unsolvable iff some combination of the equations has zero left side and nonzero right
side. A multiplier $w_e$ per edge and $z_v$ per vertex has zero left side iff, at every vertex,
$z_v\mathrm{ev}_0+\sum_tw_{e(v,t)}\mathrm{ev}_{x_t}=0$ on polynomials of degree $<R$, which reads
$\sum_tw_{e(v,t)}x_t^k=0$ for $1\le k<R$ and $z_v=-\sum_tw_{e(v,t)}$. Its right side is
$\sum_vz_v=-2\sum_ew_e$. $\square$

**Sharper form.** [SR-11](SR-11-subcube-identities-characterize-defects.md) shows that only
combinations of subcube stresses are needed: $G$ is infeasible iff some combination of the
stresses below, with nonzero total, vanishes on every edge outside $G$.

**Examples.** The $R$-subcube in directions $T$ carries the stress $w_e=\lambda_{t(e)}$, the
Lagrange weights $\lambda_t=\prod_{s\in T\setminus t}x_s/(x_s-x_t)$, with total
$2^{R-1}\sum_t\lambda_t=2^{R-1}\ne0$; this is SR-02's subcube obstruction. Global formulas
([SR-04](SR-04-slab-construction.md)) show which regions carry no stress with nonzero total.

**Corollary 1 (size of obstructions).** Any $R-1$ of the vectors $\xi_t$ are linearly
independent (Vandermonde), so at every vertex touched by a nonzero stress at least $R$ incident
edges carry weight. A subgraph of the cube with minimum degree $\ge R$ has at least $2^R$
vertices (split along a coordinate: each side keeps minimum degree $\ge R-1$; induct). Hence
every obstruction has at least $2^R$ vertices and $R2^{R-1}$ edges.

**Corollary 2 (relaxations are exponentially weak).** Both natural relaxations of CP(Q, R)
give only exponentially small lower bounds on the bad fraction:

* the fractional relaxation over all obstructions has value at most $1/(R2^{R-1})$ of the edges,
  by Corollary 1 (put weight $1/(R2^{R-1})$ on every edge);
* the hitting relaxation (bad edges must meet every $R$-subcube) has value at most
  $2^{-R/2+o(R)}$: take all edges at a vertex set meeting every $R$-subcube of density
  $2^{-R/2+o(R)}$ (N. Alon, *Erasure list-decodable codes and Turán hypercube problems*, Finite
  Fields Appl. 100 (2024) 102513, [arXiv:2403.16319](https://arxiv.org/abs/2403.16319),
  Prop. 1.1; Ellis, Ivan, Leader, [arXiv:2401.16289](https://arxiv.org/abs/2401.16289),
  Thms 7 and 9).

So **any polynomial lower bound $\beta^*\ge R^{-O(1)}$ must exploit integrality**: the fractional
relaxation is exponentially small even over all obstructions, the algebraic ones included, and
the integral relaxation by subcubes alone is exponentially small too. What remains is the
integral hitting problem for algebraic obstructions, which by
[SR-11](SR-11-subcube-identities-characterize-defects.md) are combinations of subcube stresses. Conversely, a construction reaching the hitting value
$2^{-R/2+o(R)}$ would need the vertex set of such a hitting family to separate the cube into
regions carrying no stress with nonzero total, which global formulas cannot do on their own
(the exact disagreement of a degree-$(R-1)$ polynomial with parity on $\{0,1\}^Q$ is at least
$\sum_{i\le\lfloor(Q-R)/2\rfloor}\binom Qi$, a binomial tail, because exact agreement implies sign
agreement and the sign-error bound of Aspnes, Beigel, Furst and Rudich, Combinatorica 14
(1994), Thm 2.2, applies; inspection level T, from our literature check).

## Theorem 2 (products of designs)

Let $(p_v)$ be a family on $Q_1$ directions with degree $<R_1$ and $(s_u)$ a family on $Q_2$
other directions with degree $<R_2$, with distinct nodes. Then $p_{(v,u)}=p_v\,s_u$ is a family
on $Q_1+Q_2$ directions with degree $<R_1+R_2-1$, $p_{(v,u)}(0)=1$, and an edge in a direction
of the first block is good whenever its projection is good for $(p_v)$
(`product_edge_good`: $(p+p')(y)=0\Rightarrow(ps)(y)+(p's)(y)=0$). Hence
$$\beta^*(Q_1+Q_2,\ R_1+R_2-1)\ \le\ \max\big(\beta^*(Q_1,R_1),\ \beta^*(Q_2,R_2)\big)$$
for the per-direction objective, where each $\beta^*$ refers to the node block actually used
(the optimum depends on the node set, up to scaling); the bad edges of the product are
contained in those of its factors.

**Consequences.** Products preserve the ratio $Q/R$ (up to the $-1$) and the bad fraction. So
the relevant asymptotic quantity is the best bad fraction $\beta$ as a function of $R$ at a
fixed ratio $\rho=Q/R$: the window family gives $e^{-\Theta(R/\rho)}$, and the question of
[ETH-A03](../01-algorithmic-core/ETH-A03-point-dependent-designs.md) is whether some family
gives $e^{-cR}$ with $c$ independent of $\rho$. Small exact optima (e.g. one bad edge per direction
at $(Q,R)=(4,3)$, [SR-02](SR-02-cube-polynomial-designs.md#exact-small-cases)) can be
multiplied to give, for instance, $\beta\le1/8$ at $(Q,R)=(4m,2m+1)$ for every $m$ (uniform
measure). Scaling all nodes by a common factor is a symmetry ($p_v(T)\mapsto p_v(T/c)$), so the
$(4,3)$ family for the nodes $t/4$ gives families for the pairwise disjoint blocks
$\{5^jt/4:t=1,\dots,4\}$, $j=0,\dots,m-1$. (The separate review also checked the blocks
$\{5,\dots,8\}$, $\{9,\dots,12\}$, $\{13,\dots,16\}$ and $\{101,\dots,104\}$ directly.)
