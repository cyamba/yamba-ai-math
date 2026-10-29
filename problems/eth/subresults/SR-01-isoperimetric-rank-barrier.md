# SR-01. Isoperimetric rank barrier for the preprint's template of designs

**Status: proved** (informal proof below; the combinatorial and linear-algebraic core is
**Lean-verified** in [`RankBarrier.lean`](../lean/EthConsequences/RankBarrier.lean), certificate
[`verification.json`](../lean/verification.json)). The binomial-tail estimates in Corollary 3 are
standard and proved here informally.
**Novelty: not verified.** The source appeared on 2026-10-26; no prior barrier for this
construction was found in the literature check of 2026-10-29 (see the
[novelty ledger](../RANKING.md#novelty-ledger) and
[SR-08](SR-08-corrections-to-gemini-summaries.md)).
**Depends on the upstream theorem: no.** The statement concerns the method, not the truth of
ETH being false.

**Closest work (checked 2026-10-29).** Inside the swap algebra the rank of $I-M_0$ is an
identity: R. O'Donnell's exposition of the preprint (2026-10-28,
[PDF](https://www.cs.cmu.edu/~odonnell/some_eth_false_exposition.pdf), Lemma 4.1) shows
$\operatorname{rank}(J-F_g)=2^n\Pr_x[g(x)\ne\chi(x)]$, and for the uniform measure the sign-error
bound of Aspnes, Beigel, Furst and Rudich (Combinatorica 14, 1994, Thm 2.2) then gives the
Gaussian barrier for swap-algebra matrices. Theorem 1 below needs neither the swap algebra nor
the uniform measure: it holds for **every** matrix $M_0$ with the Hamming support condition. The
underlying principle (an untouched identity minor bounds the rank from below) is classical;
we found no prior statement for this construction. Inspection level for the two cited works: T
(read through our literature check, not yet by us in full).

Feeds: [ETH-A01](../01-algorithmic-core/ETH-A01-break-the-sqrt-log-barrier.md),
[ETH-A02](../01-algorithmic-core/ETH-A02-optimality-of-the-spectral-construction.md).
Continued by [SR-02](SR-02-cube-polynomial-designs.md) to [SR-05](SR-05-stress-duality-and-products.md),
which show that the barrier is specific to the preprint's **template** (replacement rows (2.16),
(4.10) built from a pair $(M_0,C)$ with the two conditions (2.14)): the slab family of
[SR-04](SR-04-slab-construction.md), a swap-algebra design outside the template, beats it with a
single measurement matrix as well as with node-dependent ones (finding of the separate review,
2026-10-29).

## Setting (preprint Section 2.7, Step 2, and Section 4.2)

Fix integers $r\ge2$, $Q\ge1$, $R\ge1$. Auxiliary labels are
$u=(a_u,d_u)\in\mathcal B=[r]^Q\times[r]^Q$, so $D=|\mathcal B|=r^{2Q}$. For $u,w\in\mathcal B$
put $E_{u,w}=\{t\in[Q]: a_w(t)\ne d_u(t)\}$, so $|E_{u,w}|=\operatorname{dist}_H(d_u,a_w)$.

A pair $(M_0,C)$ with $M_0\in\mathbb Q^{\mathcal B\times\mathcal B}$ and
$C\in\mathbb Q^{c\times\mathcal B}$ is **$R$-admissible** when

1. (kernel) $M_0\xi=\xi$ for every $\xi\in\ker C$, and
2. (support) $M_0[u,w]\ne0\Rightarrow|E_{u,w}|\le R-1$.

These are exactly the two conditions (2.14) of the preprint, and the rows below are its (2.16). Condition 2 is what makes the
replacement rows $\langle\vec P_u(T),\vec\zeta\rangle=((I-M_0)\vec\zeta)_u+\sum_wM_0[u,w]
\prod_{s\in E_{u,w}}(1-T/s)\zeta_w$ have degree at most $R-1$; condition 1 is what makes
$(I-M_0)\vec\zeta$ a function of the $c$ measurements $C\vec\zeta$. The preprint requires
$c\le D\tau/(3r)$ and takes $M_0=V_0f(W_0)$, achieving
$c=D\Pr[\mathrm{Bin}(Q,p)\notin\mathcal I]\le2De^{-R^2/(8Q)}$ with $p=(r-1)/(2r)$.

## Theorem 1 (rank barrier)

If $(M_0,C)$ is $R$-admissible and $A,B\subseteq[r]^Q$ satisfy
$\operatorname{dist}_H(a,b)\ge R$ for all $a\in A$, $b\in B$, then

$$c\ \ge\ \operatorname{rank}(I-M_0)\ \ge\ |A|\cdot|B|.$$

*Proof.* By condition 1, $\ker C\subseteq\ker(I-M_0)$, so by rank and nullity
$\operatorname{rank}(I-M_0)\le\operatorname{rank}C\le c$. Let
$U=\{u: a_u\in A,\ d_u\in B\}$. For $u,w\in U$,
$|E_{u,w}|=\operatorname{dist}_H(d_u,a_w)\ge R$, so $M_0[u,w]=0$ by condition 2. Hence the
principal submatrix of $I-M_0$ on $U$ is the identity and
$\operatorname{rank}(I-M_0)\ge|U|=|A||B|$. $\square$

Lean: `EthConsequences.RankBarrier.barrier` (labels `Label r Q`, any field `K`).

## Corollary 2 (binomial form)

Let $h=\lfloor r/2\rfloor$ and $X\sim\mathrm{Bin}(Q,h/r)$. For every integer $k$,

$$\frac{c}{D}\ \ge\ \Pr[X\ge k+R]\cdot\Pr[X\le k].$$

*Proof.* Fix $H\subseteq[r]$ with $|H|=h$ and let $N_H(a)=|\{t:a(t)\in H\}|$. Positions with
$a(t)\in H$, $b(t)\notin H$ are disagreements, so $\operatorname{dist}_H(a,b)\ge
N_H(a)-N_H(b)$ (Lean: `count_le_count_add_hammingDist`). Take $A=\{N_H\ge k+R\}$,
$B=\{N_H\le k\}$; under the uniform measure on $[r]^Q$, $N_H\sim X$. Divide Theorem 1 by
$D=r^{2Q}$. $\square$ Lean: `barrier_threshold` (in counting form).

## Corollary 3 (necessary degree; the construction is optimal up to a constant factor)

If $c\le\varepsilon D$ then

$$(R+1)^2\ \ge\ Q\,p_h(1-p_h)\,\ln\frac{1}{2(Q+1)\varepsilon},\qquad p_h=\frac{\lfloor r/2\rfloor}{r}\in[\tfrac13,\tfrac12],$$

so in particular $R\ge\sqrt{\tfrac29\,Q\ln\frac{1}{2(Q+1)\varepsilon}}-1$ (when
$\lceil Qp_h\rceil+R\le Q$; otherwise $R>Q/2-1$).

*Proof.* Take $k=\lceil Qp_h\rceil$; a binomial median lies in
$\{\lfloor Qp_h\rfloor,\lceil Qp_h\rceil\}$, so $\Pr[X\le k]\ge\frac12$. For $m=k+R\le Q$,
$\Pr[X\ge m]\ge\Pr[X=m]=\binom Qm p^m(1-p)^{Q-m}\ge\frac{1}{Q+1}e^{-Q\,\mathrm{KL}(m/Q\,\|\,p)}$
(the type-class bound), and $\mathrm{KL}(q\|p)\le\frac{(q-p)^2}{p(1-p)}$ (the
$\chi^2$ bound). With $m-Qp\le R+1$ this gives
$\varepsilon\ge\frac{1}{2(Q+1)}\exp\!\big(-\frac{(R+1)^2}{Qp(1-p)}\big)$. $\square$

**Comparison.** The preprint needs $c\le D\tau/(3r)$ and achieves it with
$R\approx\sqrt{8Q\ln(6r/\tau)}$. Corollary 3 forces
$R\gtrsim\sqrt{\tfrac29 Q\ln\frac{3r}{2(Q+1)\tau}}$. So **among all matrices satisfying the
two conditions, $V_0f(W_0)$ is optimal up to a constant factor in $R$**: about $6$ when
$\ln(r/\tau)\gg\ln Q$, and about $\sqrt{72}\approx8.5$ in the preprint's own regime, where
$r/\tau=r^2\lambda$ and $\ln(r/\tau)\approx2\ln Q$. No cleverer choice of $M_0$, even a non-symmetric
one outside the swap algebra, improves the exponent **within this template**; designs outside it
can do better (SR-04).

## Corollary 4 (method-level barrier, under the preprint's accounting)

Consider the counting routine of Proposition 3.4 instantiated by the Section 4 construction
with an arbitrary $R$-admissible pair, $h$ label copies, and $rhc$ group measurement rows
(the preprint's accounting), applied to a bounded-occurrence formula with $M\ge n$
occurrences. Assume every auxiliary label is used by some occurrence (an assumption of ours: the
preprint's Lemma 4.5 bounds the largest label multiplicity but does not make every label used;
the assumption forces $D\le M\le3n$, i.e. $Q\le\log_r(3n)/2$). Then the routine examines at least

$$2^{\Omega(n/\sqrt{\log n})}$$

Boolean vectors.

*Proof sketch.* Three lower bounds hold simultaneously. (a) Taylor data: the routine
enumerates all $C_q\ge\binom nq2^q\ge2^q$ pairs $U\subseteq E$, $|E|\le q$, with
$q=\lfloor MR'/Q\rfloor$ and row degree $R'=R-1$, so the cost is at least $2^{n(R-1)/Q}$.
(b) Measurements: $h\ge M/D$ by pigeonhole, so the rows number $rhc\ge rMc/D\ge
rM\Pr[X\ge k+R]\Pr[X\le k]$ and each row has at least three possible values (when it is not
identically zero), giving at least $3^{\Omega(rn\Pr[X\ge k+R])}$ tuples. (c) Groups: some group
has at least $n/r$ variables. If $r\le\sqrt{\log n}$, (c) gives $2^{n/\sqrt{\log n}}$. Otherwise
$Q\le\log(3n)/\log\log n$; if $R-1\ge\sqrt Q$ then (a) gives
$2^{n/\sqrt Q}\ge2^{n\sqrt{\log\log n/\log 3n}}$; if $R\le\sqrt Q+1$ then
$\Pr[X\ge\lceil Qp\rceil+R]$ is bounded below by an absolute constant (for $Q$ beyond an
absolute threshold, by the central limit theorem with Berry and Esseen's rate), and (b) gives
$2^{\Omega(rn)}$. $\square$

The hypothesis "every label used" is where a fleet should probe first: with sparse label
sets the forced-identity argument still applies to every $R$-separated set of used labels,
and in the sparse regime almost all used labels are pairwise separated, so the measurement
rank becomes $\Theta(n)$. A fully hypothesis-free version over arbitrary schedules is open
(ETH-A02).

## What the barrier does not cover

* **Designs outside the template.** Theorem 1 needs rows of the form (2.16), with all of
  $I-M_0$ measured and $M_0$ supported on Hamming-close pairs. A general swap-algebra design
  $P(T)=\sum_Sc_S(T)\Pi_S$ need not have this form: the slab family of SR-04 has $c/D\le2/R$ with
  one measurement matrix for all nodes, for every $Q$, beating Corollary 3 once
  $Q\ge\frac98(R+2)^2$. For node-dependent designs (Definitions 2.1 and 3.1 allow them) the
  forced-identity argument only gives $c_t/D\gtrsim4^{-R}/R$ (SR-03). Whether the true answer is Gaussian
  ($e^{-\Theta(R^2/Q)}$) or exponential ($2^{-\Theta(R)}$) in $R$ is the cube polynomial
  problem of [SR-02](SR-02-cube-polynomial-designs.md). An exponential answer would give an
  exponent of order $n(\log\log n)^{O(1)}/\log n$ for the overview algorithm (see the derivation
  in [SR-04](SR-04-slab-construction.md#why-this-does-not-yet-improve-the-algorithm)).
* **The tensor-contraction route (Appendix D).** Its square root has a different source
  (a partition count of 2-adic modes); see
  [ETH-A04](../01-algorithmic-core/ETH-A04-tensor-mode-counting-barrier.md).
* **Different auxiliary geometry.** Any construction whose locality pattern is not "agree in
  all but $R-1$ coordinates of a product space" escapes Theorem 1 as stated.
