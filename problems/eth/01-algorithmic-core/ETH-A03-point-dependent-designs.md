# ETH-A03. Point-dependent designs: the cube polynomial problem CP(Q, R)

| Field | Value |
| --- | --- |
| Category | Algorithmic core |
| Source items | New (this iteration); refines "YAMBA-378-06" and the $\sqrt{\log}$ question |
| Status | **Open.** Reformulation, bounds, constructions and small exact optima proved |
| Depends on the upstream theorem | No |
| Score (I/B/T/L/Lean) | 5 / 5 / 3 / 5 / 4, composite **4.5** (top of [RANKING.md](../RANKING.md)) |
| Subresults | [SR-02](../subresults/SR-02-cube-polynomial-designs.md), [SR-03](../subresults/SR-03-point-dependent-rank-barrier.md), [SR-04](../subresults/SR-04-slab-construction.md), [SR-05](../subresults/SR-05-stress-duality-and-products.md) |

## Problem

For each vertex $v$ of $\{0,1\}^Q$ choose $p_v\in\mathbb Q[T]$ with $\deg p_v<R$ and $p_v(0)=1$.
Direction $t$ has a node $x_t$ (distinct, nonzero). The edge $\{v,v+e_t\}$ is bad when
$p_v(x_t)+p_{v+e_t}(x_t)\ne0$. Determine
$$\beta^*(Q,R)=\min_{(p_v)}\ \max_t\ \Pr_v[\{v,v+e_t\}\text{ bad}],$$
for the uniform measure and for the product measure $\mu_p$, $p=\frac{r-1}{2r}$ (the measure of the
algorithm). By SR-02 a family with value $\beta$ is a point-dependent swap design whose node-$t$
measurement count is $\frac{r-1}r\beta D$.

## Known

| Bound | Value | Source |
| --- | --- | --- |
| Lower, any family | $\min(p,1-p)^{R-1}/R$ (uniform: $2^{1-R}/R$) | subcube obstruction, Lean `no_good_subcube` |
| Lower, any design (not only swap) | $(h(r-h)/r^2)^R/R$ | SR-03, Lean `label_barrier_explicit` |
| Upper, preprint window | $\approx2e^{-R^2/(8Q)}$ | preprint Step 5 |
| Upper, slab family | $1/R$ for every $Q$ | SR-04, Lean `slab_design_bound` |
| Upper, products | $\beta^*(Q_1+Q_2,R_1+R_2-1)\le\max\beta^*$ | SR-05, Lean `product_edge_good` |
| Feasibility criterion | good set feasible iff every $\xi$-stress has zero total | SR-05 |
| Small exact optima | $Q\le5$ exact or near-exact, $Q=6$ partial | [`cube_polynomial.py`](../experiments/cube_polynomial.py) |

## The decisive questions

1. **Breakthrough direction.** Is there $C>4$ and a family with $\beta\le R^{-C}$ at
   $Q\approx R^{(C+2)/3}$? Then the counting algorithm runs in
   $2^{n(\log n)^{-(C-1)/(C+2)+o(1)}}$ (SR-04), beating the preprint. Exponential decay
   $\beta\le2^{-cR}$ would give $2^{n(\log\log n)^{O(1)}/\log n}$.
2. **Barrier direction.** Prove $\beta^*(Q,R)\ge R^{-4-o(1)}$ for $Q\ge R^{2+\delta}$. By SR-05 this
   cannot come from subcube hitting (the hitting relaxation is $\le2^{-R/2+o(R)}$ by Alon and by
   Ellis–Ivan–Leader) nor from fractional obstruction packing ($\le2^{1-R}/R$): it must use the
   algebra of the moment curve.
3. **Realizing Turán constructions.** Alon's and Ellis–Ivan–Leader's vertex sets of density
   $2^{-R/2+o(R)}$ meeting every $R$-subcube are built layer by layer from daisy-free families.
   Is the set of edges at such a vertex set the bad set of some polynomial family? A "yes" for
   a single moderate $R$ already beats the slab.
4. **Exact small cases.** Push exact optima to $Q=7,8$ (symmetry-reduced MILP, column
   generation over stresses) and fit $\beta^*(Q,R)$ against $1/R$, $R^{-2}$, $2^{-R/2}$. The MILP
   data so far ([SR-02](../subresults/SR-02-cube-polynomial-designs.md#exact-small-cases)) beat the
   slab in every solved case with $3\le R\le Q-1$, and at $(Q,R)=(5,2)$ with nodes $t/5$.

## Closest work

Hypercube Turán problems: Alon, Krech, Szabó, SIAM J. Discrete Math. 21 (2007); Ellis, Ivan,
Leader, arXiv:2401.16289; Alon, Finite Fields Appl. 100 (2024), arXiv:2403.16319; for $R=2$ the
$C_4$-free density bound of Balogh, Hu, Lidický, Liu, arXiv:1201.0209 (all level T, reading list
R044 to R046 and R059). Offner's vertex version is credited by Ellis, Ivan and Leader but was
not inspected. Direction networks and stresses in rigidity theory (generic theory does not
apply: normals lie on the moment curve and repeat per direction). No prior work on
point-dependent designs for the preprint was found.

## Obstruction

The feasibility of a good-edge set is a global linear-algebra condition (SR-05), so local
combinatorial constructions must be certified exactly; the regime that matters ($Q\gg R^2$) is
far beyond exhaustive search.

## Smallest falsifier

For question 2: an exactly verified family for some $(Q,R)$ with $Q\ge R^{2.5}$ and
$\beta<R^{-4}$. For question 1: a proof that every family with $Q\ge R^3$ has $\beta\ge c/R^2$.

## Resource boundary

One iteration of a 4-agent fleet (constructor, exact verifier, algebraist on stresses, Lean
formalizer) plus a separate critic; compute budget a few CPU-hours of MILP/linear algebra; every
claimed family checked in exact rational arithmetic and its key lemma in Lean.
