# ETH-B04. Closed-form Hermite weights and bit lengths

| Field | Value |
| --- | --- |
| Category | Algebraic identities |
| Source items | "Problem 4 (YAMBA-378-04): high-order Hermite interpolation with explicit $\ell_1$ bit-length bounds" |
| Status | **Solved** (proof below, exact check for $Q\le7$, $J\le5$); Lean open |
| Depends on the upstream theorem | No |
| Score (I/B/T/L/Lean) | 2 / 1 / 5 / 2 / 4, composite **2.5** |
| Subresults | [`hermite_weights.py`](../experiments/hermite_weights.py), results in [`hermite_weights.json`](../experiments/results/hermite_weights.json); uniqueness is Lean `Hermite.eq_of_jets_eq` |

## Statement

Let $\Omega(T)=\prod_{s=1}^Q(T-s)^J$, $\Omega_t=\Omega/(T-t)^J$. For every $H$ of degree $<QJ$
with Taylor data $h_{t,r}=[z^r]H(t+z)$,
$$H(0)=\sum_{t=1}^Q\sum_{r<J}w_{t,r}h_{t,r},\qquad
w_{t,r}=-\Omega(0)\,[(T-t)^{J-1-r}]\frac1{T\,\Omega_t(T)},$$
and with $L=\operatorname{lcm}(1,\dots,Q)$,
$$L^{J-1-r}\,w_{t,r}\in\mathbb Z,\qquad|w_{t,r}|\le2^{O(QJ\log Q)} .$$

## Proof

Residues: $H/(T\Omega)$ has degree $\le-2$, so the residue at $0$, namely $H(0)/\Omega(0)$, is minus
the sum of the residues at $1,\dots,Q$, which gives the formula. Expanding
$1/T=\sum_m(-1)^m(T-t)^m/t^{m+1}$ and $(T-s)^{-J}=\sum_k\binom{-J}k(T-t)^k(t-s)^{-J-k}$, a typical
term of $w_{t,r}$ is $\pm\binom{J+k-1}k$-weighted
$$\frac{(Q!)^J}{t^{m+1}\prod_{s\ne t}(t-s)^{J+k_s}}
=\binom Qt^J\,\frac{t^{J-m-1}}{\prod_{s\ne t}(t-s)^{k_s}},\qquad m+\sum_sk_s=J-1-r,$$
using $t\prod_{s\ne t}|t-s|=t!(Q-t)!$. The denominator is a product of $J-1-r-m$ integers in
$[1,Q-1]$, so it divides $L^{J-1-r}$. $\square$ The exact computation confirms the formula
against direct linear algebra and the denominator bound for all $(Q,J)$ with $Q\le7$, $J\le5$,
$QJ\le30$; the source's bound $L^{2J}$ is correct but weak
([SR-08](../subresults/SR-08-corrections-to-gemini-summaries.md), row 8).

## Remaining questions

1. Lean: the residue identity via `Polynomial` division, or directly the uniqueness plus an
   explicit interpolant.
2. The tapered 2-adic version of Appendix C (Lemma C.4) is where bit lengths actually matter;
   optimize its loss term $\sum_jj^2/2^j=6$.

## Resource boundary

One agent; small.
