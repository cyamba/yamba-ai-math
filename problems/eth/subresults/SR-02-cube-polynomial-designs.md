# SR-02. Swap-algebra designs beyond the preprint's template: the cube polynomial problem

**Status: proved** (reduction, Proposition 1, informal proof below, checked exactly on actual
matrices by [`matrix_validation.py`](../experiments/matrix_validation.py), which builds the full
matrices and masks their nonlocal entries; subcube obstruction, Proposition 2, **Lean-verified**
as `EthConsequences.Subcube.no_good_subcube`, and Proposition 2' as `card_good_directions_lt`, in
[`SubcubeObstruction.lean`](../lean/EthConsequences/SubcubeObstruction.lean)). The table of small
cases is **empirical**.
**Novelty: not verified** (closest-work check in [RANKING.md](../RANKING.md#novelty-ledger)).
**Depends on the upstream theorem: no.** It concerns the method of the preprint.

Feeds: [ETH-A03](../01-algorithmic-core/ETH-A03-point-dependent-designs.md),
[ETH-A01](../01-algorithmic-core/ETH-A01-break-the-sqrt-log-barrier.md). Builds on
[SR-01](SR-01-isoperimetric-rank-barrier.md); continued by
[SR-03](SR-03-point-dependent-rank-barrier.md), [SR-04](SR-04-slab-construction.md),
[SR-10](SR-10-touched-vertices-barrier-criterion.md) and
[SR-11](SR-11-subcube-identities-characterize-defects.md) (a local linear form of CP).

## Why leave the template

The preprint's construction (Section 2.7, Steps 1 to 3; Section 4.2) builds the replacement rows
(2.16), (4.10) from a pair $(M_0,C)$ subject to the two conditions (2.14), with one measurement
matrix $C$ for every node. [SR-01](SR-01-isoperimetric-rank-barrier.md) proves that **every** design
of this template pays the Gaussian price $c/D\gtrsim e^{-\Theta(R^2/Q)}$, the source of the
$\sqrt{\log n}$ in the exponent. The design definitions themselves (Definition 2.1, and
Definition 3.1 with matrices $C_{t,g}$ for every node $t$ and group $g$) ask for much less: at each
node, the nonlocal part of every replacement row must be determined by the measurements. This
subresult describes all designs whose auxiliary matrix lies in the algebra of commuting swaps,
with measurement matrices that may or may not depend on the node, as a problem on the cube.

## Setting

Labels $u=(a_u,d_u)\in[r]^Q\times[r]^Q$, $D=r^{2Q}$. $\Pi_s$ swaps the pair at position $s$;
for $S\subseteq[Q]$ put $\Pi_S=\prod_{s\in S}\Pi_s$. Each position splits $\mathbb Q^{[r]\times[r]}$
into the swap-symmetric part (dimension $r(r+1)/2$, including the $r$ diagonal pairs) and the
antisymmetric part (dimension $r(r-1)/2$), with $\{0,\pm1\}$ eigenvectors (preprint, Lemma 4.1).
An eigenvector has a type $\varepsilon\in\{0,1\}^Q$ ($\varepsilon_s=1$ for antisymmetric at $s$) and
$\Pi_S$ acts on it by the character $\chi_S(\varepsilon)=(-1)^{|S\cap\varepsilon|}$. Under the uniform
measure on labels, the type of a basis vector has the product law $\mu_p$ with
$p=\Pr[\varepsilon_s=1]=\frac{r-1}{2r}$.

A *swap design of degree $<R$* is a matrix polynomial $P(T)=\sum_{S}c_S(T)\,\Pi_S$ with
$P(0)=I$ and $\deg c_S<R$. At node $t$ the row of label $u$ may read freely the labels $w$ with
$a_w(t)=d_u(t)$ (preprint, Step 1); the rest of $P(x_t)$ is the *nonlocal part* $N_t$.

**Counting measurements.** Definition 3.1(3) counts rows after the split into groups,
$\sum_gc_{t,g}\le2\tau n$. Since $\operatorname{rank}N_t\le\sum_g\operatorname{rank}N_t^{(g)}\le\sum_gc_{t,g}$,
at least $\operatorname{rank}N_t$ rows are needed at node $t$. Conversely the $\{0,\pm1\}$
eigenvectors spanning the row space of $N_t$ suffice; each of them meets at most two groups at
node $t$, so they cost at most $2\operatorname{rank}N_t$ rows once zero rows are dropped (and $r$
times their number in the preprint's own count of $r$ rows per measurement). A **single**
measurement matrix serving every node needs $\dim\sum_t\operatorname{rowspace}N_t$ rows before the
split; restricting its rows to the groups of any node gives a valid design at that node.

## Proposition 1 (reduction to the cube)

Put $p_\varepsilon(T)=\sum_S c_S(T)\chi_S(\varepsilon)$ for $\varepsilon\in\{0,1\}^Q$. Then

1. $P(0)=I$ iff $p_\varepsilon(0)=1$ for all $\varepsilon$, and $\deg P<R$ iff $\deg p_\varepsilon<R$ for
   all $\varepsilon$ (the $c_S$ are the Fourier transforms of the $p_\varepsilon$);
2. for every node $t$, with $\varepsilon'$ ranging over types on $[Q]\setminus\{t\}$,
   $$\operatorname{rank}N_t=r(r-1)\sum_{\varepsilon'\ \text{bad}}m(\varepsilon'),\qquad
     m(\varepsilon')=\prod_{s\ne t}\Big(\tfrac{r(r+1)}2\Big)^{1-\varepsilon'_s}\Big(\tfrac{r(r-1)}2\Big)^{\varepsilon'_s},$$
   where the edge $\{\varepsilon',\varepsilon'+e_t\}$ of the cube is **bad** when
   $p_{\varepsilon'}(x_t)+p_{\varepsilon'+e_t}(x_t)\ne0$. Equivalently
   $\operatorname{rank}N_t/D=\frac{r-1}{r}\,\mu_p(\text{bad edges in direction }t)$.

*Proof.* Item 1 is Fourier inversion on $\{0,1\}^Q$. For item 2, the entry $(u,w)$ of $\Pi_S$
is nonzero only for $w=\mathrm{swap}_S(u)$. If $t\in S$ then $a_w(t)=d_u(t)$, so the entry is
local. If $t\notin S$ then $a_w(t)=a_u(t)$, which equals $d_u(t)$ exactly when $u$ is diagonal
at $t$. Hence $N_t=D_t\sum_{S\not\ni t}c_S(x_t)\Pi_S$ with $D_t$ the projector onto labels that
are off-diagonal at $t$. $D_t$ commutes with every swap, has rank $r(r-1)$ at position $t$, and
the remaining factor is diagonal in the product eigenbasis with eigenvalue
$\sum_{S\not\ni t}c_S(x_t)\chi_S(\varepsilon')=\tfrac12\big(p_{\varepsilon'}(x_t)+p_{\varepsilon'+e_t}(x_t)\big)$ on
the $m(\varepsilon')$ eigenvectors of type $\varepsilon'$. $\square$

**Validation.** `matrix_validation.py` builds the full matrices $P(x_t)$ for
$(r,Q,R)\in\{(2,3,2),(2,3,3),(3,2,2),(2,4,2),(2,4,3),(3,3,2)\}$ from the slab, window (centred at
$Qp$) and MILP-optimal families, keeps exactly the entries with $a_w(t)\ne d_u(t)$, and computes
the ranks modulo two 31-bit primes. Every rank equals the prediction. The script also reports
the rank of the stacked nonlocal parts, i.e. the size of a single measurement matrix for all
nodes: for the slab at $(2,4,3)$ with offset $0$ it is $42$ rows, against $18$ at each node
([results](../experiments/results/matrix_validation.json)). An independent masking check by the
separate review agrees.

**The preprint's construction in this language.** The preprint's rows (4.10) are not in the
swap algebra (the factor $\varphi_{u,w}$ depends on which positions of $u$ are diagonal), but at
every node their nonlocal parts coincide entrywise with those of the *window family*
$p_\varepsilon(T)=1-\sigma_\varepsilon f(|\varepsilon|)+\sigma_\varepsilon G(T,\varepsilon)$,
$\sigma_\varepsilon=(-1)^{|\varepsilon|}$, with the global formula $G$ of [SR-04](SR-04-slab-construction.md)
(checked by the separate review for $(r,Q,R)=(2,3,2),(2,4,2),(2,4,3),(3,3,2)$). An edge with both
weights in the interpolation window is good; for $R\ge3$ these are exactly the good edges in all
cases computed ($Q\le6$), while for $R=2$ the window family has further good edges, because $f$
is linear (its counts then equal the slab's, see the table). So the window family's bad
fraction is at most $\Pr[\mathrm{Bin}(Q-1,p)\notin\mathcal I']\le2e^{-R^2/(8Q)}$ (Hoeffding). Row
counts before the group split are comparable with the preprint's $c$ only up to constant
factors: at $(r,Q,R)=(2,4,3)$, $\operatorname{rank}N_t=20$ at each node, while the preprint's single
matrix has $\operatorname{rank}(I-M_0)=13$ rows before the split.

## The cube polynomial problem CP(Q, R)

> Attach to each vertex $v$ of $\{0,1\}^Q$ a polynomial $p_v$ of degree $<R$ with $p_v(0)=1$.
> Direction $t$ has a node $x_t$ (distinct, nonzero). Minimize
> $\beta=\max_t\beta_t$, $\beta_t=\mu(\{v:\ v_t=0,\ p_v(x_t)+p_{v+e_t}(x_t)\ne0\})$ (the measure of
> the lower endpoints, taken on the other coordinates).

The measure that matters is $\mu_p$ with $p=\frac{r-1}{2r}$, which tends to the uniform measure
as $r\to\infty$; the experiments below use the uniform measure. The optimum depends on the node
set (up to a common scaling, which is a symmetry). By Proposition 1, a family with value $\beta$
is a swap design with node-dependent measurements and $\operatorname{rank}N_t\le\frac{r-1}{r}\beta D$
at every node. With a single measurement matrix, the row count
$\dim\sum_t\operatorname{rowspace}N_t$ lies between $\max_t\operatorname{rank}N_t$ and $D$ times the
$\mu_p$-measure of the eigenvector types that touch a bad edge (compare the touched set of
[SR-10](SR-10-touched-vertices-barrier-criterion.md)).

Writing $p_v(T)=\sigma_v q_v(T)$ and $q_v(T)=\sigma_v+\sum_{k<R}c_k(v)T^k$, an edge from an even vertex
$v$ to $w=v+e_t$ is good iff $\langle\xi_t,c(w)-c(v)\rangle=2$ with $\xi_t=(x_t,\dots,x_t^{R-1})$: a
**direction network** on the cube in $\mathbb Q^{R-1}$ whose edge normals are points of the moment
curve. Generic direction networks of this size are rigid far below the cube's density; the
interest of CP is that very structured (non-generic) solutions exist (the window and slab
families make whole regions good).

## Proposition 2 (subcube obstruction; Lean)

For any $R$ distinct directions, every $R$-dimensional subcube in those directions contains a
bad edge. (`no_good_subcube`: Lagrange extrapolation $p(0)=\sum_i\ell_i(0)p(x_{t_i})$ summed over
the $2^R$ vertices; each inner sum over an edge class vanishes when all edges are good, while the
left side is $2^R\neq0$.)

**Proposition 2' (many bad directions; Lean).** In every $d$-dimensional subcube at most $R-1$
directions are entirely good, so bad edges occur in at least $d-R+1$ of its directions; for the
whole cube, in at least $Q-R+1$ directions. (`card_good_directions_lt`: $H=\sum_Bp_B$ has degree
$<R$, vanishes at the node of every entirely good direction, and $H(0)=2^d\ne0$.) A design
therefore cannot concentrate its measurements on a few nodes; this does not improve the bound
below, because the averaging over random subcubes is best at $d=R$.

**Corollary.** For every set $T$ of $R$ directions,
$\sum_{t\in T}\beta_t\ge\min(p,1-p)^{R-1}$, so $\max_t\beta_t\ge\min(p,1-p)^{R-1}/R$; for the
uniform cube this is $2^{1-R}/R$. (Each subcube's bad edge carries $\mu_p$-weight at least
$\min(p,1-p)^{R-1}$ times the weight of the subcube's base pattern; sum over bases.)

## Exact small cases

`cube_polynomial.py` searches CP(Q, R) for the nodes $x_t=t/Q$ ($t=1,\dots,Q$) and the uniform
measure with a mixed-integer program (HiGHS, 240 s per instance; polynomial coefficients boxed
by $|a|\le200$, big-M $10^4$), and **re-checks every reported good-edge set in exact rational
arithmetic**; it also computes the minimum subcube-hitting set (the relaxation behind
Proposition 2). Values are numbers of bad edges; "max" is the largest count in one direction,
out of $2^{Q-1}$. Every family reported is exactly verified, so every entry is an upper bound on
the optimum. Solver optimality and the solver's lower bounds hold **only within the coefficient
box** (exact solutions with coefficients above 2000 do occur, e.g. at $(6,5)$); entries marked
$\dagger$ were certified optimal exactly, with no box, by exhaustive search over hitting sets
([`certify_small.py`](../experiments/certify_small.py), written by the separate review). An entry
"$\le a\ [b]$" hit the time limit: $a$ is the best exactly verified family, $b$ the solver's
bound within the box. The window column gives the actual window family at its best position.

| Q | R | hitting, total / max | CP, total / max | slab, total / max | window family, total / max |
| --- | --- | --- | --- | --- | --- |
| 2 | 2 | 1 / 1 | 1 / 1 $\dagger$ | 2 / 1 | 2 / 1 |
| 3 | 2 | 3 / 1 | 4 / 2 $\dagger$ | 6 / 2 | 6 / 2 |
| 3 | 3 | 1 / 1 | 1 / 1 $\dagger$ | 3 / 1 | 3 / 1 |
| 4 | 2 | 8 / 2 | 12 / 4 | 16 / 4 | 16 / 4 |
| 4 | 3 | 3 / 1 | 4 / 1 $\dagger$ | 8 / 2 | 8 / 2 |
| 4 | 4 | 1 / 1 | 1 / 1 $\dagger$ | 4 / 1 | 4 / 1 |
| 5 | 2 | 24 / 5 | $\le32\ [25]$ / $\le7\ [5]$ | 40 / 8 | 40 / 8 |
| 5 | 3 | 8 / 2 | $\le14\ [8]$ / $\le4\ [2]$ | 25 / 5 | 30 / 6 |
| 5 | 4 | 3 / 1 | 4 / 1 | 10 / 2 | 10 / 2 |
| 5 | 5 | 1 / 1 | 1 / 1 | 5 / 1 | 5 / 1 |
| 6 | 2 | $\le60$ / 10 | $\le91\ [51]$ / $\le17\ [9]$ | 96 / 16 | 96 / 16 |
| 6 | 3 | $\le22$ / 4 | $\le60\ [9]$ / $\le12\ [2]$ | 60 / 10 | 72 / 12 |
| 6 | 4 | 8 / 2 | $\le18\ [4]$ / $\le5\ [1]$ | 36 / 6 | 42 / 7 |
| 6 | 5 | 3 / 1 | 4 / 1 | 12 / 2 | 12 / 2 |

For $\dagger$ entries the per-direction optimum follows from the certified total (at $(3,2)$,
four bad edges in three directions force two in one direction) and the families found. Raw data:
[`cube_polynomial.jsonl`](../experiments/results/cube_polynomial.jsonl) (one line per instance,
with the bad-edge lists of the families found) and the window counts in
[`matrix_validation.json`](../experiments/results/matrix_validation.json). Observations
(**empirical**, for these nodes only):

* **Realizability is a real constraint.** Certified at $(3,2)$ and $(4,3)$, where the exact
  optimum (4) exceeds the hitting optimum (3); the solver's bounds suggest the same at $(5,2)$.
* **For $R=Q-1$ the families found have 4 bad edges in total** ($Q=3,\dots,6$), and one per
  direction for $Q=4,5,6$ (two at $Q=3$), against $2Q$ for the slab; for $R=Q$ a single bad edge
  suffices.
* **The slab is beaten in every case with $3\le R\le Q-1$ that was searched**, e.g. one bad edge
  per direction at $(4,3)$ against two (certified), and $\le5$ against 6 at $(6,4)$.
* **$R=2$.** The slab's per-direction value $1/2$ is optimal for $Q\le3$ (certified) and is the
  best found at $Q=4$, but at $Q=5$ a family with at most 7 bad edges in every direction exists
  ($7/16<1/2$; re-checked by two independent exact eliminations). Whether this survives for
  generic nodes, and what happens as $Q$ grows, is open; for $R=2$ every 4-cycle has a bad edge,
  so the good edges form a $C_4$-free subgraph of the cube, and asymptotically at least
  $1-0.6068$ of the edges are bad (Balogh, Hu, Lidický, Liu,
  [arXiv:1201.0209](https://arxiv.org/abs/1201.0209), level T, reading list R059; Erdős conjectured
  the $C_4$-free density is $1/2$).

## What remains open

The exact growth of $\beta^*(Q,R)$ is the question of
[ETH-A03](../01-algorithmic-core/ETH-A03-point-dependent-designs.md). Known:
$\min(p,1-p)^{R-1}/R\le\beta^*(Q,R)\le\min\big(\tfrac1R,\ \beta_{\rm win}(Q,R)\big)$, where the
lower bound is Proposition 2, $1/R$ is the slab family of SR-04, and $\beta_{\rm win}$ is the
binomial tail of the window family (at most $2e^{-R^2/(8Q)}$ under the preprint's Step 5
conventions, Gaussian in $R/\sqrt Q$). Restricting a design on $Q+1$ directions to the two faces
$v_{Q+1}=0,1$ gives designs on the remaining $Q$ directions with the same nodes, so the
direction-averaged optimum over all node sets is non-decreasing in $Q$; for the maximum over
directions the same argument loses a factor $1/\min(p,1-p)$.
