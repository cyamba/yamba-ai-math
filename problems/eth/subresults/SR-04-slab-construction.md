# SR-04. Global formulas and the slab construction: leaving the template provably helps

**Status: proved.** The cube-level statements (Lemmas 1 and 2 and the slab theorem) are
**Lean-verified** ([`SlabDesign.lean`](../lean/EthConsequences/SlabDesign.lean): `G_edge`,
`natDegree_G_le`, `G_eval_zero`, `exists_gamma`, `slab_edge_good`, `slab_eval_zero`,
`slab_natDegree`, `slab_design_bound`; certificate [`verification.json`](../lean/verification.json));
the corollary on swap designs, the comparison with template designs and the improvement
criterion are proved informally.
The good-edge sets of the slab family are re-checked in exact arithmetic by
[`cube_polynomial.py`](../experiments/cube_polynomial.py), and the induced swap matrices by
[`matrix_validation.py`](../experiments/matrix_validation.py).
**Novelty: not verified** (see [RANKING.md](../RANKING.md#novelty-ledger)).
**Depends on the upstream theorem: no.**

Feeds: [ETH-A03](../01-algorithmic-core/ETH-A03-point-dependent-designs.md),
[ETH-A01](../01-algorithmic-core/ETH-A01-break-the-sqrt-log-barrier.md).

## Lemma 1 (global formulas never fail on an edge)

For coefficients $\gamma_S$ ($S\subseteq[Q]$) and distinct nonzero nodes $x_t$ put
$$G(T,\varepsilon)=\sum_S\gamma_S\,\chi_S(\varepsilon)\prod_{s\in S}\Big(1-\frac T{x_s}\Big).$$
Then $G(x_t,\varepsilon)=G(x_t,\varepsilon+e_t)$ for every vertex and direction,
$\deg_TG\le\max\{|S|:\gamma_S\ne0\}$, and $G(0,\varepsilon)=\sum_S\gamma_S\chi_S(\varepsilon)$.

*Proof.* Terms with $t\in S$ vanish at $T=x_t$; terms with $t\notin S$ have
$\chi_S(\varepsilon+e_t)=\chi_S(\varepsilon)$. $\square$

So a single global formula of degree $<R$ makes **every** edge good for the family
$p_\varepsilon=\sigma_\varepsilon G(\cdot,\varepsilon)$, $\sigma_\varepsilon=(-1)^{|\varepsilon|}$; the only defect is the
normalization $p_\varepsilon(0)=\sigma_\varepsilon g(\varepsilon)$, where $g=\sum_S\gamma_S\chi_S$ has Fourier degree
$<R$. The preprint's $M_0=V_0f(W_0)$ is the case $g(\varepsilon)=f(|\varepsilon|)$; it fixes the
normalization by a constant correction off the window, which makes those edges bad.

## Lemma 2 (symmetric polynomials have low Fourier degree)

Over a field of characteristic zero, if $\deg f\le d$ then $\varepsilon\mapsto f(|\varepsilon|)$ lies in the
span of the characters $\chi_S$ with $|S|\le d$ (`exists_gamma`). The Lean proof shows that
multiplication by $|\varepsilon|=\sum_s\frac{1-\chi_{\{s\}}(\varepsilon)}2$ raises the degree by at most one,
using $\chi_{\{s\}}\chi_S=\chi_{S\triangle\{s\}}$.

## Theorem (slab construction)

Fix $R\ge1$ and an offset $s_0$. Cut the weights $0,\dots,Q$ into slabs
$\{w:\lfloor(w+s_0)/R\rfloor=k\}$ of at most $R$ consecutive values. On slab $k$ let $f_k$ be the
interpolant of $(-1)^w$ (degree $<R$, `slabPoly`), $\gamma^{(k)}$ its Fourier coefficients
(Lemma 2), and put $p_\varepsilon=\sigma_\varepsilon G_{\gamma^{(k)}}(\cdot,\varepsilon)$ for $|\varepsilon|$ in slab $k$. Then
$\deg p_\varepsilon<R$, $p_\varepsilon(0)=\sigma_\varepsilon f_k(|\varepsilon|)=1$, every edge inside a slab is good
(Lemma 1), and for some $s_0<R$
$$\#\{\text{bad edges in direction }t\}\ \le\ \frac{2^{Q-1}}{R}\qquad\text{for every }t\text{ and every }Q$$
(`slab_design_bound`). The same averaging over $s_0$ gives
$\mu_p(\text{bad in direction }t)\le1/R$ for every product measure with identical coordinate
laws, such as $\mu_p$. (It fails for unequal laws: at $Q=R=2$ with coordinate laws $0.9$ and
$0.1$ both offsets have a direction with bad measure $0.9$.)

**Corollary (swap designs).** By [SR-02](SR-02-cube-polynomial-designs.md), Proposition 1,
there is a swap design of degree $<R$ with node-dependent measurements and
$\operatorname{rank}N_t/D\le\frac{r-1}{r}\cdot\frac1R$ at every node, for every $Q$. **One measurement
matrix also suffices** (separate review, checked on explicit matrices): the bad slab edges join
weights $m$ and $m+1$ with $m+1+s_0\equiv0\pmod R$, so every nonlocal row lies in the span of the
eigenvectors whose type has weight $\equiv-s_0-1$ or $-s_0\pmod R$; a single matrix $C$ whose rows
span these eigenvectors serves every node, and averaging over $s_0$ gives $c/D\le2/R$, for every
$Q$. Point dependence saves at most a factor $2r/(r-1)\le4$ here.

## Leaving the template provably helps

[SR-01](SR-01-isoperimetric-rank-barrier.md) shows that **every** design of the preprint's template
(rows (2.16), (4.10) built from an $R$-admissible pair) needs
$c/D\ge\Pr[X\ge k+R]\Pr[X\le k]$ with $X\sim\mathrm{Bin}(Q,p_h)$, $p_h=\lfloor r/2\rfloor/r\in[\frac13,\frac12]$.
Take $k=\lceil Qp_h\rceil$, so $\Pr[X\le k]\ge\frac12$. If $Q\ge\frac98(R+2)^2$ then
$k+R\le Qp_h+2\sigma$ with $\sigma=\sqrt{Qp_h(1-p_h)}\ge\sqrt{2Q/9}$, and the Berry–Esseen theorem gives
$\Pr[X\ge Qp_h+2\sigma]\ge\Phi(-2)-O(1/\sigma)\ge0.02$ for $Q$ beyond an absolute constant. Hence
**every template design has $c/D\ge0.01$ once $Q\ge\frac98(R+2)^2$ and $Q$ is large**, while the
slab family, a swap design outside the template, has $c/D\le2/R$ with one measurement matrix and
$\operatorname{rank}N_t/D\le\frac{r-1}{rR}$ with node-dependent ones, for every $Q$. In that regime
leaving the template wins by a factor of order $R$ over every template construction, the
preprint's included; whether the measurements depend on the node matters only by a constant
factor for the slab. (An earlier version of this note attributed the gain to point dependence;
the separate review of 2026-10-29 showed that a single matrix already achieves it.) At
$Q=2\times10^5$, $R=400$, $r=2$ the single-matrix slab needs $c/D\le0.0049$, below the template
bound $0.0347$ of SR-01 (separate review).

## Why this does not yet improve the algorithm

The counting routine needs node measurements polynomially small in $\log n$, while the slab gives
$1/R$ and $R$ must stay below $Q/r\ll\log n$. Suppose families with $\beta\le R^{-C}$ (measured by
$\mu_p$, $p=\frac{r-1}{2r}$, which tends to the uniform measure in this regime) exist at
$Q\approx R^{\alpha}$. Through the preprint's three costs (display (2.11)) with
$Q\approx\lambda/(4\log_2r)$, $\lambda=\log_2n$, the exponent depends on how measurement rows are counted:

* **(A) the preprint's count** ($r$ rows per measurement after the split, zero rows included;
  $\tau\ge3(r-1)\beta$): exponent $n(\log n)^{-\min(\alpha-1,\,(C-\alpha)/2)/\alpha+o(1)}$, best at
  $\alpha=(C+2)/3$, giving $n(\log n)^{-\frac{C-1}{C+2}+o(1)}$, which beats $n/(\log n)^{1/2+o(1)}$
  exactly when $C>4$;
* **(B) zero rows dropped**, as Definition 3.1(3) allows (each eigenvector row meets at most two
  groups at a node, so $\tau\ge6\beta$ suffices): exponent
  $n(\log n)^{-\min(\alpha-1,\,C-\alpha)/\alpha+o(1)}$, best at $\alpha=(C+1)/2$, giving
  $n(\log n)^{-\frac{C-1}{C+1}+o(1)}$, which beats the square root exactly when $C>3$; for example
  $C=4$ at $Q\approx R^{5/2}$ gives $n(\log n)^{-3/5}$.

(Derivation. Write $R=\lambda^b$. For (A) the measurement term is about $3r\lambda\beta$ and the group
term $2/r$; with $r=\lambda^a$ the Taylor term $\frac RQ\log\frac QR\approx\lambda^{b-1}$ balances the group
term at $b=1-a$, and the measurement term is at most the group term when $bC\ge2a+1$, so
$a\le\frac{C-1}{C+2}$. For (B) the measurement term is about $6\lambda\beta=6\lambda^{1-bC}$, independent of
$r$, so $r$ can be taken polynomially large and the exponent is
$\lambda^{-\min(1-b,\,bC-1)}$, maximal at $b=\frac2{C+1}$. With $b=1/\alpha$ these are the two formulas
above. The separate review re-derived (A) from display (2.11) and the preprint's count, and (B)
from Definition 3.1.)

## Exact optima versus the slab

The small cases of CP(Q, R) (table in [SR-02](SR-02-cube-polynomial-designs.md#exact-small-cases))
show the slab beaten in every case searched with $3\le R\le Q-1$: at $(Q,R)=(4,3)$ a family has one
bad edge per direction against two for the slab (certified exactly). For $R=2$ the slab's
per-direction value $1/2$ is optimal for $Q\le3$ but is beaten at $Q=5$ ($7/16$, nodes $t/5$).
The families found are not unions of global formulas on level sets. Whether their advantage
grows with $R$ is the question of [ETH-A03](../01-algorithmic-core/ETH-A03-point-dependent-designs.md).
