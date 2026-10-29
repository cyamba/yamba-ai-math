# SR-02. Point-dependent designs in the swap algebra: the cube polynomial problem

**Status: proved** (reduction, Proposition 1, informal proof below, validated exactly on small
matrices by [`matrix_validation.py`](../experiments/matrix_validation.py); subcube obstruction,
Proposition 2, **Lean-verified** as `EthConsequences.Subcube.no_good_subcube` in
[`SubcubeObstruction.lean`](../lean/EthConsequences/SubcubeObstruction.lean)).
**Novelty: not verified** (closest-work check in [RANKING.md](../RANKING.md#novelty-ledger)).
**Depends on the upstream theorem: no.** It concerns the method of the preprint.

Feeds: [ETH-A03](../01-algorithmic-core/ETH-A03-point-dependent-designs.md),
[ETH-A01](../01-algorithmic-core/ETH-A01-break-the-sqrt-log-barrier.md). Builds on
[SR-01](SR-01-isoperimetric-rank-barrier.md); continued by
[SR-03](SR-03-point-dependent-rank-barrier.md) and [SR-04](SR-04-slab-construction.md).

## Why point dependence matters

The preprint's Definition 3.1 (an $(r,\tau,D)$-design *at* $t$) lets the measurement matrices
depend on the evaluation node $t$. Its construction (Section 2.7, Step 2; Section 4.2) uses one
matrix $C$ for every node, and SR-01 proves that **every** single-matrix construction on the
label space $([r]\times[r])^Q$ pays the Gaussian price $c/D\gtrsim e^{-\Theta(R^2/Q)}$, which is
exactly the source of the $\sqrt{\log n}$ in the exponent. This subresult reformulates the
point-dependent version inside the algebra of commuting swaps as a clean problem on the cube.

## Setting

Labels $u=(a_u,d_u)\in[r]^Q\times[r]^Q$, $D=r^{2Q}$. $\Pi_s$ swaps the pair at position $s$;
for $S\subseteq[Q]$ put $\Pi_S=\prod_{s\in S}\Pi_s$. Each position splits $\mathbb Q^{[r]\times[r]}$
into the swap-symmetric part (dimension $r(r+1)/2$, including the $r$ diagonal pairs) and the
antisymmetric part (dimension $r(r-1)/2$), with $\{0,\pm1\}$ eigenvectors (preprint, Step 2).
An eigenvector has a type $\varepsilon\in\{0,1\}^Q$ ($\varepsilon_s=1$ for antisymmetric at $s$) and
$\Pi_S$ acts on it by the character $\chi_S(\varepsilon)=(-1)^{|S\cap\varepsilon|}$. Under the uniform
measure on labels, the type of a basis vector has the product law $\mu_p$ with
$p=\Pr[\varepsilon_s=1]=\frac{r-1}{2r}$.

A *swap design of degree $<R$* is a matrix polynomial $P(T)=\sum_{S}c_S(T)\,\Pi_S$ with
$P(0)=I$ and $\deg c_S<R$. At node $t$ the row of label $u$ may read freely the labels $w$ with
$a_w(t)=d_u(t)$ (preprint, Step 1); the rest of $P(t)$ is the *nonlocal part* $N_t$, and the
measurements needed at $t$ are at least $\operatorname{rank}N_t$ (and this many $\{0,\pm1\}$
rows suffice, by the eigenbasis).

## Proposition 1 (reduction to the cube)

Put $p_\varepsilon(T)=\sum_S c_S(T)\chi_S(\varepsilon)$ for $\varepsilon\in\{0,1\}^Q$. Then

1. $P(0)=I$ iff $p_\varepsilon(0)=1$ for all $\varepsilon$, and $\deg P<R$ iff $\deg p_\varepsilon<R$ for
   all $\varepsilon$ (the $c_S$ are the Fourier transforms of the $p_\varepsilon$);
2. for every node $t$, with $\varepsilon'$ ranging over types on $[Q]\setminus\{t\}$,
   $$\operatorname{rank}N_t=r(r-1)\sum_{\varepsilon'\ \text{bad}}m(\varepsilon'),\qquad
     m(\varepsilon')=\prod_{s\ne t}\Big(\tfrac{r(r+1)}2\Big)^{1-\varepsilon'_s}\Big(\tfrac{r(r-1)}2\Big)^{\varepsilon'_s},$$
   where the edge $\{\varepsilon',\varepsilon'+e_t\}$ of the cube is **bad** when
   $p_{\varepsilon'}(t)+p_{\varepsilon'+e_t}(t)\ne0$. Equivalently
   $\operatorname{rank}N_t/D=\frac{r-1}{r}\,\mu_p(\text{bad edges in direction }t)$.

*Proof.* Item 1 is Fourier inversion on $\{0,1\}^Q$. For item 2, the entry $(u,w)$ of $\Pi_S$
is nonzero only for $w=\mathrm{swap}_S(u)$. If $t\in S$ then $a_w(t)=d_u(t)$, so the entry is
local. If $t\notin S$ then $a_w(t)=a_u(t)$, which equals $d_u(t)$ exactly when $u$ is diagonal
at $t$. Hence $N_t=D_t\sum_{S\not\ni t}c_S(t)\Pi_S$ with $D_t$ the projector onto labels that
are off-diagonal at $t$. $D_t$ commutes with every swap, has rank $r(r-1)$ at position $t$, and
the remaining factor is diagonal in the product eigenbasis with eigenvalue
$\sum_{S\not\ni t}c_S(t)\chi_S(\varepsilon')=\tfrac12\big(p_{\varepsilon'}(t)+p_{\varepsilon'+e_t}(t)\big)$ on
the $m(\varepsilon')$ eigenvectors of type $\varepsilon'$. $\square$

**Validation.** `matrix_validation.py` builds $P(T)$ for $(r,Q,R)\in\{(2,3,2),(2,3,3),(3,2,2),
(2,4,2),(2,4,3),(3,3,2)\}$ from the slab, window and MILP-optimal families and computes
$\operatorname{rank}N_t$ exactly (modulo two 31-bit primes). Every rank equals the prediction
([results](../experiments/results/matrix_validation.json)).

**The preprint's construction in this language.** $M_0=V_0f(W_0)$ gives the *window family*:
$p_\varepsilon(T)=1-\sigma_\varepsilon f(|\varepsilon|)+\sigma_\varepsilon G(T,\varepsilon)$ with
$\sigma_\varepsilon=(-1)^{|\varepsilon|}$ and the global formula $G$ of [SR-04](SR-04-slab-construction.md).
An edge is good iff both of its weights lie in the interpolation window $\mathcal I$, so the bad
fraction is $\Pr[\mathrm{Bin}(Q-1,p)\notin\mathcal I']\approx e^{-R^2/(8Q)}$, matching
$c=D\Pr[W\notin\mathcal I]$ in the preprint.

## The cube polynomial problem CP(Q, R)

> Attach to each vertex $v$ of $\{0,1\}^Q$ a polynomial $p_v$ of degree $<R$ with $p_v(0)=1$.
> Direction $t$ has a node $x_t$ (distinct, nonzero). Minimize
> $\beta=\max_t\mu(\{v:\ p_v(x_t)+p_{v+e_t}(x_t)\ne0\})$.

By Proposition 1, a family with value $\beta$ is a point-dependent swap design whose node-$t$
measurement count is $c_t\le\frac{r-1}{r}\beta D$. Writing
$p_v(T)=\sigma_v q_v(T)$ and $q_v(T)=\sigma_v+\sum_{k<R}c_k(v)T^k$, an edge from an even vertex $v$
to $w=v+e_t$ is good iff $\langle\xi_t,c(w)-c(v)\rangle=2$ with $\xi_t=(x_t,\dots,x_t^{R-1})$: a
**direction network** on the cube in $\mathbb Q^{R-1}$ whose edge normals are points of the moment
curve. Generic direction networks of this size are rigid far below the cube's density; the
interest of CP is that very structured (non-generic) solutions exist (the window and slab
families make whole regions good).

## Proposition 2 (subcube obstruction; Lean)

For any $R$ distinct directions, every $R$-dimensional subcube in those directions contains a
bad edge. (`no_good_subcube`: Lagrange extrapolation $p(0)=\sum_i\ell_i(0)p(x_{t_i})$ summed over
the $2^R$ vertices with signs; each inner sum over an edge class vanishes when all edges are
good, while the left side is $2^R\neq0$.)

**Corollary.** For every set $T$ of $R$ directions,
$\sum_{t\in T}\beta_t\ge\min(p,1-p)^{R-1}$, so $\max_t\beta_t\ge\min(p,1-p)^{R-1}/R$; for the
uniform cube this is $2^{1-R}/R$. (Each subcube's bad edge carries $\mu_p$-weight at least
$\min(p,1-p)^{R-1}$ times the weight of the subcube's base pattern; sum over bases.)

## Exact small cases

`cube_polynomial.py` computes the optimum of CP(Q, R) for the nodes $x_t=t/Q$ ($t=1,\dots,Q$) and
the uniform measure by a mixed-integer program (HiGHS, 240 s per instance), and **re-checks every
reported good-edge set in exact rational arithmetic**; it also computes the minimum
subcube-hitting set (the relaxation behind Proposition 2). Values are numbers of bad edges;
"max" is the largest count in one direction, out of $2^{Q-1}$. An entry "$\le a\ [b]$" hit the
time limit: $a$ is the best exactly verified family, $b$ the solver's proven lower bound.

| Q | R | hitting, total / max | CP optimum, total / max | slab, total / max | window, total / max |
| --- | --- | --- | --- | --- | --- |
| 2 | 2 | 1 / 1 | 1 / 1 | 2 / 1 | 2 / 1 |
| 3 | 2 | 3 / 1 | 4 / 2 | 6 / 2 | 6 / 2 |
| 3 | 3 | 1 / 1 | 1 / 1 | 3 / 1 | 3 / 1 |
| 4 | 2 | 8 / 2 | 12 / 4 | 16 / 4 | 20 / 5 |
| 4 | 3 | 3 / 1 | 4 / 1 | 8 / 2 | 8 / 2 |
| 4 | 4 | 1 / 1 | 1 / 1 | 4 / 1 | 4 / 1 |
| 5 | 2 | 24 / 5 | $\le32\ [25]$ / $\le7\ [5]$ | 40 / 8 | 50 / 10 |
| 5 | 3 | 8 / 2 | $\le14\ [8]$ / $\le4\ [2]$ | 25 / 5 | 30 / 6 |
| 5 | 4 | 3 / 1 | 4 / 1 | 10 / 2 | 10 / 2 |
| 5 | 5 | 1 / 1 | 1 / 1 | 5 / 1 | 5 / 1 |
| 6 | 2 | $\le60$ / 10 | $\le91\ [51]$ / $\le17\ [9]$ | 96 / 16 | 132 / 22 |
| 6 | 3 | $\le22$ / 4 | $\le60\ [9]$ / $\le12\ [2]$ | 60 / 10 | 72 / 12 |
| 6 | 4 | 8 / 2 | $\le18\ [4]$ / $\le5\ [1]$ | 36 / 6 | 42 / 7 |
| 6 | 5 | 3 / 1 | 4 / 1 | 12 / 2 | 12 / 2 |

Raw data: [`cube_polynomial.jsonl`](../experiments/results/cube_polynomial.jsonl) (one line per
instance, with the bad-edge lists of the families found). Observations (**empirical**, for these
nodes only):

* **Realizability is a real constraint.** At $(5,2)$ the proven lower bound 25 exceeds the
  hitting optimum 24, and at $(3,2),(4,2),(4,3),(5,4),(6,5)$ the optimum exceeds the hitting value.
* **For $R=Q-1$ the optimum is 4 bad edges in total and 1 per direction** ($Q=3,\dots,6$), against
  $2Q$ for the slab; for $R=Q$ it is a single bad edge.
* **The slab is beaten in every case with $3\le R\le Q-1$ that was solved**, e.g. one bad edge per
  direction at $(4,3)$ against two, and $\le5$ against 6 at $(6,4)$.
* **$R=2$.** The per-direction optimum equals the slab value $1/2$ for $Q\le4$, but at $Q=5$ a
  family with exactly 7 bad edges in every direction exists ($7/16<1/2$; good set re-checked by an
  independent exact elimination). Whether this survives for generic nodes, and what happens as
  $Q$ grows, is open; for $R=2$ every 4-cycle has a bad edge, so the good edges form a
  $C_4$-free subgraph of the cube, and asymptotically at least $1-0.6068$ of the edges are bad
  (Balogh, Hu, Lidický, Liu, [arXiv:1201.0209](https://arxiv.org/abs/1201.0209), level T, reading
  list R059; Erdős conjectured the $C_4$-free density is $1/2$).

## What remains open

The exact growth of $\beta^*(Q,R)$ is the question of
[ETH-A03](../01-algorithmic-core/ETH-A03-point-dependent-designs.md). Known:
$\min(p,1-p)^{R-1}/R\le\beta^*(Q,R)\le\min\big(\tfrac1R,\ \beta_{\rm win}(Q,R)\big)$, where the
lower bound is Proposition 2, $1/R$ is the slab family of SR-04, and $\beta_{\rm win}$ is the
binomial tail of the preprint's window family (at most $2e^{-R^2/(8Q)}$ under the preprint's
Step 5 conventions, Gaussian in $R/\sqrt Q$). Restricting a design on $Q+1$ directions to the two
faces $v_{Q+1}=0,1$ and averaging shows that the direction-averaged optimum is non-decreasing in
$Q$; for the maximum over directions the same argument loses a factor $1/\min(p,1-p)$.
