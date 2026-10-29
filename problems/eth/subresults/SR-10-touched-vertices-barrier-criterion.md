# SR-10. What an exponent improvement forces: almost every vertex fully good

**Status: proved** (Lemma 1, Proposition 2, Corollary 3, Lemma 4 and Proposition 5, informal
proofs below; Proposition 2 and Corollary 3 are statements about the preprint's cost accounting,
like the improvement criterion of [SR-04](SR-04-slab-construction.md)). The touched-set
conjecture and the structure conjecture at the end are **conjectures**.
**Novelty: not verified** (see [RANKING.md](../RANKING.md#novelty-ledger)).
**Depends on the upstream theorem: no.**

Feeds: [ETH-A03](../01-algorithmic-core/ETH-A03-point-dependent-designs.md), the pinned target
[ETH001](../targets/ETH001.md). Setting and notation: [SR-02](SR-02-cube-polynomial-designs.md)
(the cube polynomial problem CP(Q, R), families $(p_v)$, bad edges, the product measure
$\mu_p$ with $p=\frac{r-1}{2r}$, and $\beta=\max_t\beta_t$).

## Why this matters

SR-04 says what a better design would have to achieve; this note says what such a design would
have to **look like**. In the regime where an improvement could happen, a design must make
almost every vertex of the cube *fully good* (all $Q$ of its edges good), while the
deformation degree stays below $\sqrt Q$. That turns the open problem into a clean structural
question about the few vertices that touch bad edges. A lower bound on their measure of order
$1/R$ (what the slab family attains) would prove that swap designs, with or without node
dependence, cannot beat the square root; under the preprint's own row count, even $R^{-2}$ would
suffice.

## Definitions

For a family, the **touched set** $W$ is the set of vertices incident to at least one bad edge,
and the **fully good set** is $A=\{0,1\}^Q\setminus W$. All edges at a vertex of $A$ are good, so
every bad edge has both endpoints in $W$.

## Lemma 1 (bad edges versus touched vertices)

For every family and every product measure, $\mu_p(W)\le\sum_t\beta_t\le Q\beta$.

*Proof.* The bad edges in direction $t$ have endpoints $\varepsilon'\oplus\{t\mapsto0\}$ and
$\varepsilon'\oplus\{t\mapsto1\}$ of total measure $(1-p)\mu'(\varepsilon')+p\,\mu'(\varepsilon')=\mu'(\varepsilon')$,
so the endpoints of the bad edges in direction $t$ have measure exactly $\beta_t$. Take the union
over $t$. $\square$

## Proposition 2 (what a design with exponent $e$ needs)

Consider the overview algorithm with swap designs whose measurements may depend on the node,
costed by the preprint's display (2.11) under its constraints (2.17) ($12D^2\le M\le3n$) and
$c_t/D\le\tau/(3r)$, and let $e=n^{-1}\log_2(\text{time})$ be the resulting exponent per
variable, $\lambda=\log_2n$. Rows can be counted in two ways ([SR-04](SR-04-slab-construction.md#why-this-does-not-yet-improve-the-algorithm)):
**(A)** the preprint's count, which forces $\tau\ge3(r-1)\beta$, and **(B)** the count with zero rows
dropped, as Definition 3.1(3) allows, which needs only $\tau\ge6\beta$. In both cases
$$R\ \le\ \frac{(e+1/n)\,Q}{3},\qquad Q\ \le\ \frac{\lambda-2}{4\log_2r}\ <\ \frac\lambda4,$$
and
$$\text{(A)}\quad\mu_p(W)\ \le\ Q\beta\ \le\ \frac{e^2}{12},\qquad\qquad
\text{(B)}\quad\mu_p(W)\ \le\ Q\beta\ \le\ \frac{e}{24}.$$

*Proof.* The Taylor term is at least its top summand $2^q\binom nq\ge2^q$ with
$q=\lfloor3nR/Q\rfloor$, so $e\ge3R/Q-1/n$. The constraint $12D^2\le M\le3n$ with $D=r^{2Q}$ gives
$4Q\log_2r\le\lambda-2$. The measurement term is at least $2\tau\log_2D=4\tau Q\log_2r$. In case (A),
the group term gives $2/r\le e$, so $r-1\ge r/2\ge1/e$, and $4\tau Q\log_2r\ge12(r-1)\beta Q\ge12Q\beta/e$;
hence $Q\beta\le e^2/12$. In case (B), $4\tau Q\log_2r\ge24\beta Q$, so $Q\beta\le e/24$. Lemma 1
finishes. $\square$

So an exponent $e=\lambda^{-\alpha}$ with $\alpha>\frac12$ needs $R\le\lambda^{1-\alpha}<\sqrt Q$ (up to
constants) and a touched set of measure at most $\lambda^{-2\alpha}$ (A) or $\lambda^{-\alpha}$ (B):
**almost every vertex must be fully good.** The slab family ([SR-04](SR-04-slab-construction.md)) is
far from this: its touched set is the two levels on either side of every slab boundary, of measure
about $2/R$. The window family meets it, but only with $R\gtrsim\sqrt{Q\log Q}$.

## Corollary 3 (a barrier criterion)

> **Touched-set conjecture** $\mathrm{TS}(f)$. Every family for CP(Q, R) with $R\le c_0\sqrt Q$ has
> $\mu_p(W)\ge f(R)$, for every $p\in[\frac14,\frac12]$.

Then, up to the negligible $1/n$ terms:

1. under count (A), $\mathrm{TS}(c/R^2)$ implies $e\ge\min\big(6c_0,(1728c)^{1/4}\big)\lambda^{-1/2}$;
2. under count (B), $\mathrm{TS}(c/R)$ implies $e\ge\min\big(6c_0,\sqrt{288c}\big)\lambda^{-1/2}$, while
   $\mathrm{TS}(c/R^2)$ implies only $e\ge\min\big(c_1,(3456c)^{1/3}\big)\lambda^{-2/3}$ for a constant $c_1>0$
   depending on $c_0$.

In the first two cases the method cannot beat $2^{\Theta(n/\sqrt{\log n})}$ with swap designs.

*Proof.* Let $\kappa$ be the stated minimum in case 1 and suppose $e<\kappa\lambda^{-1/2}$. Since
$\lambda\ge4Q$, $e<\kappa/(2\sqrt Q)$, and Proposition 2 gives $R\le eQ/3<\kappa\sqrt Q/6\le c_0\sqrt Q$, so
the conjecture applies: $c/R^2\le\mu_p(W)\le e^2/12$, i.e. $e^2R^2\ge12c$. But $eR\le e^2Q/3<\kappa^2/12$,
so $e^2R^2<\kappa^4/144\le12c$, a contradiction. Case 2 with $f=c/R$ is the same computation with
$c/R\le e/24$, i.e. $eR\ge24c$, against $eR<\kappa^2/12\le24c$. With $f=c/R^2$ under (B):
$c/R^2\le e/24$ and $R\le eQ/3\le e\lambda/12$ give $e^3\lambda^2\ge3456c$; the range condition
$R\le c_0\sqrt Q$ holds automatically once $e\le c_1\lambda^{-2/3}$ and $\lambda$ is large. $\square$

So the calibration depends on the row count. Under the preprint's count a lower bound $c/R^2$,
far weaker than the slab's $2/R$, already gives the square-root barrier. Under the sharper count
the conjecture must be slab-tight, $\mu_p(W)\ge c/R$, to give the square root, and $c/R^2$ only
gives $\lambda^{-2/3}$. Families with $\mu_p(W)\le R^{-1-\eta}$ at $R\le Q^{1/2}$ (with balanced
per-direction counts) are what an improvement under the sharper count requires.

## Lemma 4 (vertex-deletion form)

Call a vertex set $U$ **deletable** if the induced subgraph of the cube on the complement of $U$
can be made entirely good: there are $p_v$ ($v\notin U$) of degree $<R$ with $p_v(0)=1$ and every
edge between two vertices outside $U$ good. Let $\nu^*(Q,R)$ be the least $\mu_p(U)$ over deletable
sets. Then
$$\nu^*\ \le\ \min_{\text{families}}\mu_p(W)\ \le\ Q\,\beta^*\qquad\text{and}\qquad
\beta^*\ \le\ \frac{\nu^*}{\min(p,1-p)}.$$

*Proof.* The touched set of a family is deletable, since every edge outside it is good. Lemma 1
gives the middle inequality. Conversely, extend a family on the complement of a deletable $U$ by
$p_u=1$ on $U$; every bad edge then touches $U$, each vertex of $U$ has one edge in direction $t$,
and that edge has measure $\mu_p(u)/p$ or $\mu_p(u)/(1-p)$. $\square$

So, up to a factor $Q$, CP(Q, R) is the problem of deleting as few vertices as possible so that the
rest of the cube carries one good family. By stress duality ([SR-05](SR-05-stress-duality-and-products.md)),
$U$ is deletable exactly when no stress with nonzero total lives on the edges outside $U$.

## Proposition 5 (what deletion must at least do)

1. A deletable set meets every $R$-dimensional subcube (otherwise that subcube is entirely good,
   contradicting the subcube obstruction of SR-02). More strongly, for a family, the touched set
   contains an edge of every $R$-dimensional subcube: a subcube with at most an independent set of
   touched vertices has all its edges at fully good vertices.
2. For $R=2$, two fully good vertices are never at distance 2 (the square through them would be
   entirely good), so a neighbourhood $N(z)$ contains at most one fully good vertex, and
   $\mu(A)\le1/Q$ for the uniform measure: for linear polynomials almost every vertex is touched.
3. Both conditions are combinatorial, and combinatorics alone cannot prove the conjecture: the
   set $U'=U\cup N(U)$ for a vertex set $U$ of density $2^{-R/2+o(R)}$ meeting every $R$-subcube
   (Alon; Ellis, Ivan and Leader; reading list R045, R046) satisfies condition 1 for families,
   with measure at most $(Q+1)2^{-R/2+o(R)}$. Whether such a set is the touched set of an actual
   family is the realizability question of [ETH-A03](../01-algorithmic-core/ETH-A03-point-dependent-designs.md),
   now seen to be the heart of the matter: a "yes" for $R\le Q^{1/2}$ with the measure above
   refutes the touched-set conjecture in the strongest way.

## A route to the conjecture (conjectural steps marked)

1. **Structure (conjecture).** If $C$ is a connected set of fully good vertices, then there is a
   global formula $F$ (SR-04, Lemma 1, with polynomial coefficients $\gamma_S(T)$ of degree
   $<R-|S|$) such that $p_v=\sigma_vF(\cdot,v)$ on $C$. This is true for the whole cube (the Fourier
   argument of [SR-04](SR-04-slab-construction.md#lemma-1-global-formulas-never-fail-on-an-edge)) and
   locally: on every entirely good $d$-subcube with $d<R$, and with the top mixed difference
   forced on every entirely good $(R-1)$-subcube.
2. **Thinness (proved, given 1).** Then parity agrees on $C$ with a polynomial of degree $<R$, so
   by the sign-error bound of Aspnes, Beigel, Furst and Rudich (R043) $C$ has measure at most that
   of the middle $R$ levels, about $R\sqrt{2/(\pi Q)}$, which is below $1$ for $R\le c_0\sqrt Q$.
3. **Isoperimetry (conjecture).** Every set on which parity agrees with a polynomial of degree
   $<R$ has edge boundary at least $c\,|C|\,Q/R$, as the middle $R$ levels do. Summed over the
   components of $A$, and divided by the $Q$ edges of a touched vertex, this would give
   $\mu(W)\ge c'/R$, the slab's value, and hence the conjecture with room to spare.

Measure alone does not suffice in step 3: Voronoi-type cells of measure $R/\sqrt Q$ have much
smaller boundaries, but they are Hamming-ball-like and parity needs degree equal to their radius
on them, so they are not admissible pieces.
