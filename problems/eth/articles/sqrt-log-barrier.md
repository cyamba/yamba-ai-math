# Routing rigidity and the optimality of the interpolation route after the refutation of ETH

**Christopher Yamba** (Yamba AI Math Lab), with Claude (Anthropic) as research assistant.
Draft of 2026-10-30, revision 2 (after an internal referee pass; changes listed at the end).
Status: results proved here unless marked otherwise; core lemma machine-checked in Lean 4 with Mathlib.
**Novelty: NOT VERIFIED** (the source preprint appeared on 2026-10-25; the literature has not been searched
systematically).

## Abstract

OpenAI's preprint *The Exponential Time Hypothesis is False* (October 25, 2026) counts satisfying
assignments of $k$-CNFs in subexponential time by two methods. Its interpolation route, the one formalised in
Lean by OpenAI, replaces clause inputs by low-degree linear forms built from a matrix $M_0$ whose support is
constrained by a *routing* pattern, pays for the defect $I-M_0$ with integer measurements, and reaches exponent
$\rho(n)=n(\log\log n)^2/\sqrt{\log n}$. We prove that **every** matrix with this support pattern,
commutative or not, satisfies $\operatorname{rank}(I-M_0)\ge D\,e^{-O(1+R^2/Q)}$ for $R\le Q/6$, where $D$ is
the auxiliary dimension, $Q$ the number of interpolation nodes and $R-1$ the degree of the forms. The proof
is a zero-block argument on a product set of strings and its core is formally verified. Consequently every
instantiation of the interpolation template that measures on the full auxiliary space, as the preprint does,
has exponent $\Omega(\rho(n))$: **the interpolation route is optimal for its own template up to a constant
factor**. The swap construction is within a factor $\sqrt2$ of optimal in $R$. The preprint's other method
(recursive tensor contraction) reaches $n\log\log n/\sqrt{\log n}$ in general and $n/\sqrt{\log n}$ at bounded
density, so it necessarily leaves the template; we list which template assumptions remain open escapes:
node-dependent polynomial rows (where we prove only $\varepsilon\ge4^{-R}$ for even $r$), and measurement on
the used labels only (where type-balanced labelings defeat our argument).

## 1. Context

The preprint's Theorem 1 gives, for each fixed $k\ge2$, a deterministic algorithm computing $\#F$ for a
$k$-CNF $F$ in $(n+m)^{O_k(1)}2^{O_k(n\log\log n/\sqrt{\log n})}$ time and polynomial space, and
$2^{O_{k,D}(n/\sqrt{\log n})}$ when $m\le Dn$; both bounds are proved in its appendix by tensor contraction.
Sections 2 to 5 of the preprint give the *interpolation route* with exponent $O_k(\rho(n))$, which is what the
Lean formalisation (`lean/docs/378.md`) covers.

Two model-generated problem sheets that seeded this program asked whether a cleverer interpolating
polynomial (Chebyshev, Pade, Krawtchouk) could replace $\sqrt{\log n}$ by $\log n$ in the interpolation route.
We answer this negatively for the whole template and identify where the remaining freedom lies.

## 2. The interpolation template

We recall the structure (preprint Sec. 2.3 to 2.6). After sparsification and copying, the input is a 3-CNF on
$n$ variables with $M=\Theta(n)$ variable occurrences. Fix integers $r$ (groups), $Q$ (nodes), $R$ (degree
budget) and put $\mathcal B=([r]\times[r])^Q$, $D=|\mathcal B|=r^{2Q}$. An index $u\in\mathcal B$ is a pair of
strings $a_u,d_u\in[r]^Q$; at node $t$, coordinate $w$ belongs to group $a_w(t)$ and row $u$ is assigned to
group $d_u(t)$.

**Definition 1 (routing support).** $M\in K^{\mathcal B\times\mathcal B}$ is *routing-supported with defect
$R$* if $M[u,w]\neq0$ implies $\operatorname{Ham}(d_u,a_w)\le R-1$.

**Template.** Choose a routing-supported $M_0$ and a measurement matrix $C$ on the full auxiliary space whose
rows span the row space of $I-M_0$, so $c=\operatorname{rank}(I-M_0)$. Rows are
$$\langle P_u(T),\zeta\rangle=((I-M_0)\zeta)_u+\sum_{w}M_0[u,w]\prod_{s\in E_{u,w}}(1-T/s)\,\zeta_w,
\qquad E_{u,w}=\{t:a_w(t)\ne d_u(t)\}.$$
The coefficient of $\zeta_w$ is the single term $M_0[u,w]\prod_{s\in E_{u,w}}(1-T/s)$ of degree
$|E_{u,w}|$, so the degree budget $R-1$ is exactly Definition 1. Labels are assigned to occurrences with
multiplicity $h\ge\max(1,M/D)$ (pigeonhole), and the preprint uses $rhc$ group-restricted measurements. The
preprint's balance requirement is $12D^2\le M$, i.e. $D\lesssim\sqrt n$.

**Cost.** Up to polynomial factors the running time is the product of three enumerations (preprint,
"three costs"): Taylor data $\sum_{j\le q}2^j\binom nj$, where Hermite recovery from $Q$ nodes of a polynomial of
degree up to $M(R-1)$ needs $q\ge\lfloor n(R-1)/Q\rfloor$; measurement tuples $(2D+1)^{\text{rows}}$; and one
group $2^{\max_g|S_g|}\ge2^{n/r}$. With $\varepsilon=c/D$, the logarithm $E$ of the cost satisfies, for
$R\ge2$ and $(R-1)/Q\le1/e$,
$$E\ \ge\ \tfrac n2\,x\log\tfrac1x\ +\ \tfrac nr\ +\ \text{rows}\cdot\log3,\qquad x=\tfrac{R-1}{Q},\qquad
\text{rows}\ \ge\ r\,\varepsilon\,\max(D,n), \tag{1}$$
using $\binom nq\ge(n/q)^q$. (If $(R-1)/Q>1/e$ the Taylor factor alone is $2^{\Omega(n)}$.) Remark: only
$\sum_g\dim(\mathrm{Rs}|_{S_g})\ge\dim\mathrm{Rs}$ is forced in general; the factor $r$ in the row count is the
preprint's accounting, and the proof below goes through with $\log(1/\delta)$ in place of $\log(r/\delta)$
without it.

The preprint chooses $f(j)=(-1)^j$ on $R$ consecutive integers and $M_0=V_0f(W_0)$ in the algebra generated by
commuting swaps. The swap eigenvalue count is $\mathrm{Bin}(Q,p)$ with $p=(r-1)/(2r)$, so the sharp tail gives
$\varepsilon\approx e^{-R^2/(8Qp(1-p))}$ (the preprint's analysis states $2e^{-R^2/(8Q)}$).

## 3. Routing rigidity

**Theorem A (routing rigidity).** Let $M$ be routing-supported with defect $R$ over a field $K$. For every
partition $[r]=X\sqcup Y$ and all integers $k_1+k_2\ge Q+R$,
$$\operatorname{rank}(I-M)\ \ge\ \#\{u\in\mathcal B:\ |\{t:a_u(t)\in X\}|\ge k_1,\ |\{t:d_u(t)\in Y\}|\ge k_2\}.$$

*Proof.* Call the set on the right $T$. For $u,w\in T$ (including $u=w$) the sets $\{t:a_w(t)\in X\}$ and
$\{t:d_u(t)\in Y\}$ have sizes at least $k_1,k_2$ inside $[Q]$, so they meet in at least $R$ positions, at
each of which $a_w(t)\ne d_u(t)$. Hence $M[u,w]=0$, the principal submatrix $(I-M)[T,T]$ is the identity, and
rank does not increase under taking submatrices. $\square$

Formalised as `EthProblems.RoutingRigidity.rank_one_sub_ge_card_block`, with `hamming_ge_of_split` and
`card_le_rank_of_zero_block`, via Mathlib's `Matrix.rank_submatrix_le`.

**Corollary A.1.** Let $x_r=\lfloor r/2\rfloor/r\in[1/3,1/2]$ and $|X|=\lfloor r/2\rfloor$. For $R\le Q/6$,
$$\frac{\operatorname{rank}(I-M)}{D}\ \ge\ \Pr\big[\mathrm{Bin}(Q,x_r)\ge\lceil x_rQ+R/2\rceil\big]\cdot
\Pr\big[\mathrm{Bin}(Q,1-x_r)\ge\lceil(1-x_r)Q+R/2\rceil\big]\ \ge\ c_0\,e^{-C_0(R+2\sqrt Q+2)^2/Q}$$
with absolute constants (one can take $C_0=9/4$, and $c_0=1/32$ for $Q\ge25$).

*Proof.* $T$ is a product of a set of $a$-strings and a set of $d$-strings with the two stated densities. Use
the local bound $\Pr[\mathrm{Bin}(Q,x)=j]\ge(2Q)^{-1/2}e^{-Q\,\mathrm{KL}(j/Q\|x)}$, sum over the window
$j\in[k,k+\sqrt Q]$, and use $\mathrm{KL}(a\|x)\le(a-x)^2/(x(1-x))$ with $x(1-x)\ge2/9$. $\square$

In the regime $\sqrt Q\ll R\ll Q$ the lower bound has exponent $R^2/(4Q\,x_r(1-x_r))$ and the swap
construction $R^2/(8Q\,p(1-p))$; the ratio is $2p(1-p)/(x_r(1-x_r))\le2$, with equality for odd $r$. So no
routing-supported matrix, commutative or not, can improve $R$ at equal $\varepsilon$ by more than a factor
$\sqrt2+o(1)$. Exact zero-block checks: `checks/routing_product_set_bound.py`.

**Remark (eigenvalue view, sketch).** For $M_0$ in the commutative swap algebra, $M_0$ acts on the product
eigenvector with antisymmetric pattern $y\in\{0,1\}^Q$ by $(-1)^{|y|}h(y)$ with $\deg h\le R-1$, and a
biased Smolensky argument (restrict to the coordinates where a $\mathrm{Ber}(2p)$ coin is 1) suggests
$\Pr_{y\sim\mu_p}[h(y)\ne(-1)^{|y|}]\ge\mathbb E_{m\sim\mathrm{Bin}(Q,2p)}\,2^{-m}\sum_{i>\lfloor m/2\rfloor+R-1}\binom mi$.
We have checked this exactly for $Q\le4$ (`checks/smolensky_biased_check.py`); a written proof is not part
of this article. Theorem A supersedes it for our purposes.

## 4. Optimality of the interpolation route within its template

**Theorem B.** There are absolute constants $c,n_0>0$ such that for $n\ge n_0$, every instantiation of the
template of Section 2 (measurement on the full auxiliary space; any $r,Q,R$; any routing-supported $M_0$) has
$$E\ \ge\ c\,n\,\frac{(\log\log n)^2}{\sqrt{\log n}}\ =\ c\,\rho(n).$$
Since the preprint's interpolation route attains $O(\rho(n))$, it is optimal for its template up to a constant.

*Proof.* Put $\delta=E/n$ and assume $\delta\le\delta_0$ for a small absolute $\delta_0\le1/(6e)$.

*Step 1 (parameters).* By (1), $r\ge1/\delta$ and $x=(R-1)/Q\le1/e$ (else $E=\Omega(n)$). The case $R=1$ is
excluded because Corollary A.1 then gives $\varepsilon\ge c$ for an absolute $c$, while Step 2 forces
$\varepsilon\le\delta/r$. So $R\ge2$ and $R-1\ge R/2$; also $R\le Q/6$.

*Step 2 (measurement budget).* $r\varepsilon\max(D,n)\le\text{rows}\le\delta n$, so
$\log(1/\varepsilon)\ge\log(r/\delta)+\log(\max(D,n)/n)$.

*Step 3 (degree).* By Corollary A.1, $\log(1/\varepsilon)\le C_0(R+2\sqrt Q+2)^2/Q+\log(1/c_0)$. Since
$\log(r/\delta)\ge2\log(1/\delta_0)$ is large, the term $2\sqrt Q+2$ cannot carry the inequality, so
$R\ge c_1\sqrt{Q\log(r/\delta)}$.

*Step 4 (number of nodes).* If $D>n^2$ then $\log(1/\varepsilon)\ge\log(D/n)\ge\tfrac12\log D=Q\log r$, so
$R\ge c_1Q\sqrt{\log r}$, contradicting $R\le Q/6$ for $\delta_0$ small. Hence $D=r^{2Q}\le n^2$, i.e.
$Q\le\log n/\log r$. (With the preprint's balance requirement $D\lesssim\sqrt n$ this only improves constants.)

*Step 5 (optimisation).* From Steps 3 and 4,
$x\ge R/(2Q)\ge\tfrac{c_1}2\sqrt{\log(r/\delta)/Q}\ge\tfrac{c_1}2\,\log r/\sqrt{\log n}$. If
$r\le\sqrt{\log n}/(\log\log n)^2$ then $\delta\ge1/r\ge(\log\log n)^2/\sqrt{\log n}$. Otherwise
$\log r\ge\tfrac13\log\log n$ for large $n$, so $x\ge x_1:=\tfrac{c_1}6\log\log n/\sqrt{\log n}$. As
$x\mapsto x\log(1/x)$ increases on $(0,1/e]$,
$\delta\ge\tfrac12x_1\log(1/x_1)\ge c\,(\log\log n)^2/\sqrt{\log n}$. $\square$

**Reading.** Chebyshev, Pade or Krawtchouk choices of $f$, non-symmetric coefficients $\gamma_S$ and
non-commutative $M_0$ cannot improve the interpolation route beyond constants. The preprint's tensor-contraction
method does better ($n\log\log n/\sqrt{\log n}$ in general, $n/\sqrt{\log n}$ at bounded density, including on
the bounded-occurrence instances where the template runs). So it must violate at least one template
assumption: it uses a Cauchy deformation $W_{xy}(T)=\mathcal C(T)/(\mathcal C'(0)(T-(y-x)))$ on packets
rather than swap routing, a recursion, and recovery at a structured point set. Identifying exactly which
assumption it escapes is the natural next question (problem ETH-B04).

## 5. What the argument does not cover

**(a) Node-dependent rows.** The template needs less than the $M_0$ form: rows $P_u(T)$ with
$\deg P_u\le R-1$, $P_u(0)=e_u$ and, at each node $t$, agreement on the forbidden coordinates
$N_{t,u}=\{w:a_w(t)\ne d_u(t)\}$ with a vector $\rho_{u,t}$ of the measurement row space $\mathrm{Rs}$. The $M_0$
form is the special case where $\rho_{u,t}$ does not depend on $t$.

**Proposition C.** For general rows and even $r$, $\dim\mathrm{Rs}\ge D\,4^{-R}$ (for odd $r$,
$D\,(\lfloor r/2\rfloor\lceil r/2\rceil/r^2)^R$).

*Proof.* Fix $S_0\subseteq[Q]$ with $|S_0|=R$ and $T=\{u:a_u(t)\in X,\ d_u(t)\in Y\ \forall t\in S_0\}$. For
$u,w\in T$ and $t\in S_0$, $w\in N_{t,u}$, so $P_u(t)[w]=\rho_{u,t}[w]$. Lagrange interpolation at $S_0$ gives
$\delta_{uw}=\sum_{t\in S_0}\lambda_t\rho_{u,t}[w]$ with $\lambda_t$ independent of $w$, so
$\sigma_u=\sum_t\lambda_t\rho_{u,t}\in\mathrm{Rs}$ restricts to $e_u$ on $T$. $\square$

If the measurement spaces themselves may differ per node ($\mathrm{Rs}_t$), the same argument bounds
$\dim\sum_{t\in S_0}\mathrm{Rs}_t$, losing a factor $R$. If general rows could attain $\varepsilon=2^{-O(R)}$,
then $R\asymp\log\log n$, $Q\asymp\log n/\log r$, $r\asymp\log n/(\log\log n)^3$ and
$\tau\asymp(\log\log n)^3/(\log n)^2$ in the cost model give exponent $O(n(\log\log n)^3/\log n)$.

**(b) Measurement on used labels only.** The algorithm's design condition only constrains the transferred rows
on *filled* coordinates. What matters is $\operatorname{rank}((I-M_0)[U,U])$ for the set $U$ of labels actually
used, not $\operatorname{rank}(I-M_0)$. Theorem A's product blocks can miss $U$ entirely: for type-balanced
schedules, where every string uses each symbol exactly $Q/r$ times, every $a_u$ has exactly $x_rQ$ symbols in
$X$ and $T\cap U=\varnothing$. A barrier for this relaxation needs blocks adapted to type classes (product sets
over position subsets) or a new argument (problem ETH-B07).

## 6. Small cases

| $(Q,R,r)$ | $D$ | commutative optimum | non-commutative (numerical) | certified lower bound |
| --- | --- | --- | --- | --- |
| (2,2,2) | 16 | 1 | 1 | 1 |
| (3,2,2) | 64 | 10 | **9** | 8 |
| (3,3,2) | 64 | 1 | 1 | 1 |
| (2,2,3) | 81 | 9 | 9 (no lower rank found) | 8 |

These are the four cases we ran; we did not search all cases in a fixed order, so we make no "smallest
case" claim. The commutative optimum is computed exactly over the swap algebra. Lower bounds come from
maximum acyclic induced subgraphs of the support digraph (a triangular unit block), solved to optimality with
CP-SAT. The rank-9 completion for $(3,2,2)$ is **empirical**: three of eight alternating-projection runs
converge to $\sigma_{10}/\sigma_1\approx10^{-14}$ with entries bounded by 4.3; no exact certificate yet. A
one-step correction of the commutative optimum provably cannot reach rank 9 (no exceptional eigenvector is
supported inside any row's allowed set).

## 7. Machine-checked components

Lean 4 (v4.34.1) with Mathlib (rev `d13f23b7`), project `problems/eth/lean`, no `sorry`, axioms
`propext`, `Classical.choice`, `Quot.sound` only: Theorem A (`rank_one_sub_ge_card_block` and its two
lemmas); `no_low_degree_parity_match` (degree $<R$ cannot equal $\varepsilon(-1)^i$ on $R+1$ consecutive
points); and supporting identities of the preprint (parity interpolant and its exact defect, Hermite
uniqueness, Mobius inversion on the Boolean lattice, deformed partition function). Corollary A.1 and Theorem B
are not formalised.

## 8. Relation to prior work

The interval interpolation of $(-1)^j$ and the resulting low-rank approximations of Walsh-Hadamard type
matrices come from Alman and Williams, cited in the preprint; Dvir and Liu use Fourier sparsity for
non-rigidity. Theorem A is a rigidity statement in the opposite direction for a support-constrained family,
proved by a fooling-set argument. Smolensky's lemma underlies the remark in Section 3. We are not aware of
earlier lower bounds for the preprint's template, which is expected given its date.

## Revision notes

Revision 2 incorporates an internal referee pass: (i) the claim that both OpenAI routes sit at the barrier was
false and is removed (the tensor route beats the template); (ii) keeping the $\log(Q/R)$ factor of the Taylor
cost strengthens Theorem B from $n\log\log n/\sqrt{\log n}$ to $\Omega(\rho(n))$; (iii) the scope is restricted
to full-auxiliary measurement, with the used-label relaxation listed as open; (iv) constants, the balance
constraint, Proposition C for odd $r$ and the status of the eigenvalue remark are corrected.

## References

1. OpenAI, *The Exponential Time Hypothesis is False*, OpenAI Math Release preprint, October 25, 2026,
   `github.com/openai/math/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026`.
2. J. Alman and R. Williams, Probabilistic rank and matrix rigidity, STOC 2017.
3. Z. Dvir and A. Liu, Fourier and circulant matrices are not rigid, Theory of Computing 2020.
4. R. Smolensky, Algebraic methods in the theory of lower bounds for Boolean circuit complexity, STOC 1987.
5. T. M. Cover and J. A. Thomas, *Elements of Information Theory*, 2nd ed., Wiley 2006.
6. R. Impagliazzo, R. Paturi and F. Zane, Which problems have strongly exponential complexity?, JCSS 2001.
