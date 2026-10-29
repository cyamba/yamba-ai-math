# SR-04. Global formulas and the slab construction: point dependence provably helps

**Status: proved and Lean-verified** ([`SlabDesign.lean`](../lean/EthConsequences/SlabDesign.lean):
`G_edge`, `natDegree_G_le`, `G_eval_zero`, `exists_gamma`, `slab_edge_good`, `slab_eval_zero`,
`slab_natDegree`, `slab_design_bound`; certificate [`verification.json`](../lean/verification.json)).
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
$\mu_p(\text{bad in direction }t)\le1/R$ for every product measure.

**Corollary (swap designs).** By [SR-02](SR-02-cube-polynomial-designs.md), Proposition 1,
there is a point-dependent swap design of degree $<R$ with
$c_t/D\le\frac{r-1}{r}\cdot\frac1R$ at every node, for every $Q$.

## Point dependence provably helps

[SR-01](SR-01-isoperimetric-rank-barrier.md) shows that **every** single-matrix design needs
$c/D\ge\Pr[X\ge k+R]\Pr[X\le k]$ with $X\sim\mathrm{Bin}(Q,p_h)$, $p_h=\lfloor r/2\rfloor/r\in[\frac13,\frac12]$.
Take $k=\lceil Qp_h\rceil$, so $\Pr[X\le k]\ge\frac12$. If $Q\ge\frac98(R+2)^2$ then
$k+R\le Qp_h+2\sigma$ with $\sigma=\sqrt{Qp_h(1-p_h)}\ge\sqrt{2Q/9}$, and the Berry–Esseen theorem gives
$\Pr[X\ge Qp_h+2\sigma]\ge\Phi(-2)-O(1/\sigma)\ge0.02$ for $Q$ beyond an absolute constant. Hence
**every single-matrix design has $c/D\ge0.01$ once $Q\ge\frac98(R+2)^2$ and $Q$ is large**, while
the slab family has $c/D\le1/R$ for every $Q$. In that regime point dependence wins by a factor
of order $R$ over every single-matrix construction, the preprint's included.

## Why this does not yet improve the algorithm

The counting routine needs $c_t/D\lesssim1/(r^2\log n)$, polynomially small in $\log n$, while the
slab gives $1/R$ and $R$ must stay below $Q/r\ll\log n$. A family with
$\beta\le R^{-C}$ in the regime $Q\approx R^{(C+2)/3}$ would give, through the preprint's three
costs, the exponent $n\,(\log n)^{-\frac{C-1}{C+2}+o(1)}$; this beats $n/(\log n)^{1/2+o(1)}$
exactly when $C>4$. (Derivation: with $\tau=3rR^{-C}$, the measurement term forces
$R^C\gtrsim r^2\log n$; the Taylor term $\frac RQ\log\frac QR$ with $Q\approx\log n/\log r$ balances the
group term $1/r$ at $r\approx(\log n)^{(C-1)/(C+2)}$ up to $\log\log n$ factors.)

## Exact optima versus the slab

The exact optima of CP(Q, R) (table in [SR-02](SR-02-cube-polynomial-designs.md#exact-small-cases))
show that the slab is optimal for $R=2$ (per-direction value $1/2$) but not for $R\ge3$: at
$(Q,R)=(4,3)$ the optimum has one bad edge per direction against two for the slab. The optimal
families found are not unions of global formulas on level sets. This is the first concrete
hint that better-than-slab point-dependent designs exist; whether their advantage grows with
$R$ is the question of [ETH-A03](../01-algorithmic-core/ETH-A03-point-dependent-designs.md).
