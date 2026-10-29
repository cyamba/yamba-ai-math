# Source result: openai/math family 378, "The Exponential Time Hypothesis is False"

**Status in this repository: unverified upstream claim with an upstream Lean formalization.**
The result was released on 2026-10-26 in [openai/math](https://github.com/openai/math). Its
`history.md` states that an independent working group led by Russell Impagliazzo, Ramamohan
Paturi and Ryan Williams will examine and explain the proof. Until that review reports, every
problem in this folder treats the theorem as a working hypothesis. Results in
[subresults/](subresults/README.md) that concern the *method* (barriers, reformulations,
constants) do not depend on the theorem being correct.

Inspected primary sources, with the inspection levels of the
[reading list](../../references/reading-list.md#exponential-time-hypothesis-consequences)
(entries R039 and R040). Level **T** here means that the cited sections were read in full from
the local copy at upstream commit `7ef5c0cc5`; it is **not** a proof audit, and the upstream Lean
development was not rebuilt here (that is problem
[ETH-G03](07-formalization/ETH-G03-audit-the-upstream-formalization.md)). Theorem, display and appendix
numbers in this folder follow `paper.pdf` (and its LaTeX, which has the same structure); a first
draft used shifted numbers, corrected on 2026-10-29 after the separate review.

| Item | Location in openai/math (commit of 2026-10-26) | Inspection |
| --- | --- | --- |
| Preprint, 67 pages | `preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/paper.pdf` and its LaTeX in `build/` | T: Sections 1 and 2 (overview), Section 3 statements, Section 4.1 to 4.3 (matrix construction), Appendices C and D read in full; other sections at statement level |
| Lean scope note | `lean/docs/378.md` | T |
| Comparator statement | `lean/ComparatorChallenges/SubexponentialSAT.lean` | A (located, not read line by line) |
| Formal top-level declaration | `OAI.Algorithms.SubexponentialSAT.SqrtLogSpace.exact_count_and_sat` in `lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/Final.lean` (from `lean/formalization.yaml`) | A |

## The theorem

For each fixed clause width $k\ge 2$ there is a deterministic algorithm that, given a $k$-CNF $F$
with $n\ge 20$ variables and $m$ clauses, computes the exact number $\#F$ of satisfying
assignments in

$$(n+m)^{O_k(1)}\,2^{O_k(n\log\log n/\sqrt{\log n})}$$

bit operations and $(n+m)^{O_k(1)}$ bits of space. For fixed density $m\le Dn$ the time is
$(n+m)^{O_{k,D}(1)}\,2^{O_{k,D}(n/\sqrt{\log n})}$ (preprint, Theorem 1.1).

The Lean formalization proves the weaker exponent
$\rho(n)=n(\log\log n)^2/\sqrt{\log n}$ for a multi-tape machine on canonically encoded inputs,
with $(L+1)^{O_k(1)}$ visited tape cells, $L$ the encoding length (`lean/docs/378.md`).

**The exponent is $n/(\log n)^{1/2+o(1)}$, not $n/\log n$.** This is the single most important
correction to the two Gemini summaries attached to the original request (see the
[corrections ledger](subresults/SR-08-corrections-to-gemini-summaries.md)).

Stated consequences in the preprint: refutation of ETH, #ETH, SETH, Gap-ETH and NSETH for fixed
width (Section 1.1.1); subexponential counting of independent sets, proper $q$-colorings and
perfect matchings (Corollary 1.3); arbitrarily accurate subexponential approximation of
Max-$k$-SAT (Corollary 1.2); a circuit lower bound $C_L(n)>c\,n\sqrt{\log n}$ for some
$L\in\mathrm{E}^{\mathrm{NP}}$ (Corollary 1.4); inversion of Boolean maps with constant output
locality (Corollary C.2).

## The mechanism in one page

We write the bounded-occurrence version (each clause has at most 3 literals, each variable at
most 3 occurrences, $M=\sum_e|I_e|\le 3n$). General formulas reduce to it, or to counting common
zeros of sparse $\mathbb F_2$ polynomial systems (Sections 2.8, 2.9, 5).

1. **Direct polynomial.** $\#F=\sum_{x\in\{0,1\}^n}\prod_e\Phi_e(x)$ with
   $\Phi_e=1-\prod_{v\in I_e}(1-L_{e,v}(X_v))$, total degree at most $M$.
2. **Deformation.** Replace each occurrence $X_v$ in clause $e$ by a linear form
   $\langle\vec P_{e,v}(T),\vec X\rangle$ with $\vec P_{e,v}(0)=\delta_v$ and
   $\deg\vec P_{e,v}\le R$. Then $H(T)=\sum_x\prod_e\Phi_e(\ldots)$ has $H(0)=\#F$ and
   $\deg H\le MR$.
3. **Separation at nodes** $t=1,\ldots,Q$. An $(r,\tau,D)$-design at each node (Definition 2.1;
   general form Definition 3.1, where groups and matrices $C_{t,g}$ may depend on the node): $r$ groups of size at most
   $2n/r$, at most $2\tau n$ integer measurements of $\ell_1$ norm at most $D$, and each
   transformed clause depends, once the measurements are fixed, only on its assigned group.
   Then $H(t)=\sum_{\vec y}\prod_g B_{t,g}(\vec y)$ costs $(2D+1)^{2\tau n}2^{2n/r}$.
4. **Taylor data.** $H$ is recovered by Hermite interpolation from $q+1$ Taylor coefficients at
   each node, $q=\lfloor 3nR/Q\rfloor$; each coefficient is assembled from fixed Boolean
   substitutions by inclusion and exclusion over $E\subseteq[n]$, $|E|\le q$
   (Lemma 3.3, "Boolean differences").
5. **Three costs** (display (2.11)). $2^{O(n[(R/Q)\log(2Q/R)+\tau\log(2D+1)+1/r])}$.
6. **The matrix construction (Section 2.7, Section 4).** Auxiliary labels
   $\mathcal B=([r]\times[r])^Q$, $D=r^{2Q}$. Commuting swaps $\Pi_s$, complete swap
   $V_0=\prod_s\Pi_s$, $W_0=\tfrac12\sum_s(I-\Pi_s)$, and $M_0=V_0f(W_0)$ where $f$ has degree
   $R-1$ and interpolates $(-1)^j$ on $R$ consecutive integers around $Qp$,
   $p=(r-1)/(2r)$. Then $M_0[u,w]\ne0$ only if $|E_{u,w}|\le R-1$ (Lemma 4.2), and $I-M_0$ is
   measured by $c_{\mathcal B}\le D\Pr[\mathrm{Bin}(Q,p)\notin\mathcal I]\le 2De^{-R^2/(8Q)}$ rows of a
   $\{0,\pm1\}$ eigenbasis (Lemma 4.1). The replacement rows (2.16), (4.10) are built from the pair
   $(M_0,C)$ subject to the two conditions (2.14); we call such designs the preprint's *template*.
7. **Parameters.** $r\asymp\sqrt{\log n}/(\log\log n)^2$, $Q\asymp\log n/\log\log n$,
   $R\asymp\sqrt{\log n}$, $D=r^{2Q}\le(2n)^{1/128}$. The exponent is
   $O(n(\log\log n)^2/\sqrt{\log n})$.
8. **Sharper route (Appendix D).** A recursive Boolean tensor contraction with a Cauchy
   deformation, 2-adic "modes", and tapered Hermite multiplicities contracts any bounded-degree
   network with $s$ wires in $2^{O(s/\sqrt{\log s})}$ time. The square root reappears as a
   partition count $\exp(O(\sqrt{Mp_t/D}))=\exp(O(M/\sqrt u))$ with $u=\Theta(\log s)$
   valuation levels.

Where the square root comes from, and whether it can be removed, is the subject of
[ETH-A01](01-algorithmic-core/ETH-A01-break-the-sqrt-log-barrier.md),
[SR-01](subresults/SR-01-isoperimetric-rank-barrier.md) and
[SR-02](subresults/SR-02-cube-polynomial-designs.md).
