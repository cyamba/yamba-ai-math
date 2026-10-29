# ETH-A04. The tensor-contraction route: mode counting and its square root

| Field | Value |
| --- | --- |
| Category | Algorithmic core |
| Source items | Preprint Appendix D (sharper route); implicit in "YMB-ETH-02" |
| Status | **Open** |
| Depends on the upstream theorem | No (concerns the method) |
| Score (I/B/T/L/Lean) | 4 / 3 / 2 / 3 / 2, composite **3.0** |
| Subresults | none yet; constants in [SR-06](../subresults/SR-06-galactic-thresholds.md) |

## Task

Appendix D contracts a Boolean tensor network with $s$ wires in $2^{O(s/\sqrt{\log s})}$. At a
call with $M$ wires and $u=\Theta(\log s/2^d)$ retained 2-adic levels, the number of children is
the number of mode monomials of total weight below the working precision $p_t$:
$$\exp\big(O(\sqrt{Mp_t/D})\big)=\exp\big(O(M/\sqrt u)\big),\qquad p_t=O(MD/u),\quad
\#\{\text{modes of each weight}\}\le6M/D .$$
Find a modification giving $\exp(O(M/u^{\alpha}))$ with $\alpha>\frac12$, or prove that the
square root is forced for this route.

## Levers

1. **Mode weights.** A mode of index $b$ has 2-adic weight $b+1$ from the geometric expansion
   of the Cauchy kernel. Mahler (binomial) expansions $f(j)=\sum_b\Delta^bf(0)\binom jb$ have
   $v_2(\Delta^bf)\approx v_2(b!)+b-i\approx2b$: weights about $2b$, a constant-factor gain only.
   Superlinear weights would change the partition count from $e^{\sqrt{Np}}$ to
   $e^{O(N^{2/3}p^{1/3})}$ or better.
2. **Precision.** The tapered Hermite loss is $\Theta(hD_t)$ with $h=\Theta(M/u)$; node sets in
   unramified extensions make differences units but destroy the valuation-indexed grouping.
3. **Hybrid.** Use point-dependent designs ([ETH-A03](ETH-A03-point-dependent-designs.md))
   for the local step and the recursion for bookkeeping.

## Closest work

Preprint Appendix D (level T: D.1 to D.4 read in full, no proof audit; R039). Partition asymptotics (Hardy–Ramanujan type)
explain the square root exactly: $N$ variables of each weight $1,2,\dots$ and budget $p$ give
$\exp(\Theta(\sqrt{Np}))$ monomials.

## Obstruction

Any expansion whose $b$-th term costs $O(b)$ powers of two and has $\Theta(M/D)$ variables per
weight gives the same count; a barrier proof would have to show that weights cannot grow faster
because of how tiles meet groups.

## Smallest falsifier

A valid expansion of $1/(T-y_0+x-2^{i+1}j)$ around tile bases with $\Omega(b\log b)$ 2-adic weight
in the $b$-th term and $O(M/D)$ variables per weight.

## Resource boundary

Two agents (2-adic analysis, numerical check of valuations), one critic; no Lean until a
statement stabilizes.
