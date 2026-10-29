# ETH-A02. Optimality of the single-matrix spectral construction

| Field | Value |
| --- | --- |
| Category | Algorithmic core |
| Source items | "YAMBA-378-06" (is $V_0f(W_0)$ the right choice?); preprint Section 2.7, Step 2 |
| Status | **Largely solved** by SR-01; constant factor and hypotheses open |
| Depends on the upstream theorem | No |
| Score (I/B/T/L/Lean) | 3 / 2 / 4 / 3 / 4, composite **3.0** |
| Subresults | [SR-01](../subresults/SR-01-isoperimetric-rank-barrier.md) (Lean `RankBarrier.barrier`, `barrier_threshold`) |

## Task

Among all pairs $(M_0,C)$ on labels $([r]\times[r])^Q$ with $M_0\xi=\xi$ on $\ker C$ and
$M_0[u,w]\ne0\Rightarrow|E_{u,w}|\le R-1$, determine the least $R$ for which $c\le\varepsilon D$ is
possible, up to $1+o(1)$.

## What is known

SR-01: $c\ge\operatorname{rank}(I-M_0)\ge|A||B|$ for Hamming-separated $A,B$, hence
$(R+1)^2\ge Qp_h(1-p_h)\ln\frac1{2(Q+1)\varepsilon}$, while the preprint achieves
$R\approx\sqrt{8Q\ln(2/\varepsilon)}$: optimal up to a factor of about 6 in $R$ when
$\ln(1/\varepsilon)\gg\ln Q$. Inside the swap algebra the rank is the exact identity
$\operatorname{rank}(I-M_0)=D\,\mu_p(g\ne\chi)$ (O'Donnell's Lemma 4.1 analogue), and the
sign-error bound of Aspnes–Beigel–Furst–Rudich gives the uniform-measure barrier.

## Open parts

1. The constant: is $R\sim\sqrt{2Q\ln(1/\varepsilon)}$ the truth (matching the Gaussian tail with the
   best symmetric interval)? Use binomial tail asymptotics on both sides.
2. Remove the hypothesis "every label used" from SR-01's Corollary 4 (method-level barrier).
3. Non-product locality: labels from a code or a group other than $([r]\times[r])^Q$; does an
   isoperimetric inequality of the same strength hold?

## Closest work

O'Donnell's exposition (2026-10-28, Lemma 4.1, level T); Aspnes, Beigel, Furst, Rudich,
Combinatorica 14 (1994), Thm 2.2 (level T); Haemers-type minrank lower bounds.

## Obstruction

Item 3 needs an isoperimetric inequality for the chosen geometry; for Cayley graphs of other
groups the analogue of the Hamming-ball separation may be weaker.

## Smallest falsifier

A non-swap $M_0$ on $([2]\times[2])^Q$ with $c/D$ below the SR-01 bound for some small $Q$ would
falsify the Lean-checked theorem (impossible); a family beating $\sqrt{8Q\ln(2/\varepsilon)}$ by a
constant factor is the realistic target.

## Resource boundary

Two agents (analysis, Lean extension of `RankBarrier.lean`), one review round.
