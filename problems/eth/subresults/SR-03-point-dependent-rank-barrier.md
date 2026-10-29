# SR-03. A rank barrier for arbitrary point-dependent designs

**Status: proved and Lean-verified** (`EthConsequences.PointBarrier.point_dependent_barrier`,
`label_barrier`, `label_barrier_explicit` in
[`PointDependentBarrier.lean`](../lean/EthConsequences/PointDependentBarrier.lean); certificate
[`verification.json`](../lean/verification.json)). Checked numerically against the actual swap
matrices in [`matrix_validation.py`](../experiments/matrix_validation.py).
**Novelty: not verified** (see [RANKING.md](../RANKING.md#novelty-ledger)).
**Depends on the upstream theorem: no.**

Feeds: [ETH-A03](../01-algorithmic-core/ETH-A03-point-dependent-designs.md),
[ETH-A01](../01-algorithmic-core/ETH-A01-break-the-sqrt-log-barrier.md),
[ETH-A02](../01-algorithmic-core/ETH-A02-optimality-of-the-spectral-construction.md).

## Statement

Let $\mathcal B=[r]^Q\times[r]^Q$ (labels $u=(a_u,d_u)$), and let $P(T)$ be any
$\mathcal B\times\mathcal B$ matrix of rational polynomials with $\deg P<R$ and $P(0)=I$; it need
**not** lie in the swap algebra. Let $x_1,\dots,x_R$ be distinct nodes and let node $i$ use the
groups of position $\pi(i)\in[Q]$ (in the preprint $\pi(i)=i$). A point-dependent design splits
$P(x_i)=L_i+N_i$, where the local part satisfies
$L_i[u,w]\ne0\Rightarrow a_w(\pi(i))=d_u(\pi(i))$ and the measurements at node $i$ are at least
$c_i\ge\operatorname{rank}N_i$.

**Theorem.** For product sets $A=\prod_tS^A_t$, $B=\prod_tS^B_t\subseteq[r]^Q$ with
$S^A_{\pi(i)}\cap S^B_{\pi(i)}=\varnothing$ for every $i$,
$$|A|\,|B|\ \le\ \sum_{i=1}^R\operatorname{rank}N_i .$$
With $|S^A_t|=h$, $|S^B_t|=r-h$ at the $R$ distinct positions and $S^A_t=S^B_t=[r]$ elsewhere,
$$\max_i\frac{c_i}{D}\ \ge\ \frac1R\Big(\frac{h(r-h)}{r^2}\Big)^{R}
\ =\ \frac{4^{-R}}{R}\quad(r\text{ even},\ h=r/2).$$

*Proof.* Lagrange extrapolation from $R$ nodes is exact on polynomials of degree $<R$, entrywise:
$I=P(0)=\sum_i\lambda_iP(x_i)$ with $\lambda_i=\prod_{j\ne i}x_j/(x_j-x_i)$. Hence
$\sum_i\lambda_iN_i=I-\sum_i\lambda_iL_i$. Put $U=\{u:a_u\in A,\ d_u\in B\}$. For $u,w\in U$ and every
$i$, $a_w(\pi(i))\in S^A_{\pi(i)}$ and $d_u(\pi(i))\in S^B_{\pi(i)}$ differ, so $L_i[u,w]=0$. The
principal submatrix of $\sum_i\lambda_iN_i$ on $U$ is the identity, so
$|U|\le\operatorname{rank}\sum_i\lambda_iN_i\le\sum_i\operatorname{rank}N_i$. $\square$

The Lean proof follows these lines: `map_eval_zero_eq_sum` (entrywise Lagrange identity, reusing
`Subcube.eval_zero_eq_sum`), `card_le_sum_rank` (principal identity block plus subadditivity of
rank, `rank_add_le`, `rank_smul_le`, `rank_sum_le`), `label_barrier` (product sets via
`Fintype.piFinset`) and `label_barrier_explicit` (the count
$|H|^R(r-|H|)^Rr^{2(Q-R)}$).

## How the three barriers compare

| Design class | Lower bound on measurements per node, $c/D$ | Achieved by | Source |
| --- | --- | --- | --- |
| One matrix $C$ for all nodes (preprint) | $\Pr[X\ge k+R]\Pr[X\le k]$, Gaussian: forces $R\gtrsim\sqrt{Q\log(1/\varepsilon)}$ | $V_0f(W_0)$, optimal up to a constant factor in $R$ | [SR-01](SR-01-isoperimetric-rank-barrier.md) |
| Point-dependent, inside the swap algebra | $\frac{r-1}{r}\min(p,1-p)^{R-1}/R\approx2^{-R}$ | slab family: $\frac{r-1}{r}\cdot\frac1R$ for every $Q$ | [SR-02](SR-02-cube-polynomial-designs.md), [SR-04](SR-04-slab-construction.md) |
| Point-dependent, arbitrary auxiliary matrices | $(h(r-h)/r^2)^R/R\approx4^{-R}$ | (same constructions) | this note |

## Consequence for the method

The counting routine needs $c_t/D\le\tau/(3r)$ at every node, with $\tau\approx1/(r\log n)$ in the
preprint's regime. For single-matrix designs SR-01 turns this into $R\gtrsim\sqrt{Q\log(r\log n)}$,
which is exactly what produces the exponent $n/(\log n)^{1/2+o(1)}$. For point-dependent designs
SR-03 only forces
$$R\ \ge\ \log_4\frac{3r}{R\tau}\ \approx\ \log_4\big(r^2\log n\big),$$
a **logarithmic** requirement. Plugging $R=\Theta(\log\log n)$ into the three costs of the
preprint (Section 2.6) gives exponents as small as $n(\log\log n)^{O(1)}/\log n$. So the
$\sqrt{\log n}$ barrier is **not** implied by any rank argument of this kind: it is a property of
the single-matrix construction (SR-01), and whether point-dependent designs can approach the
exponential bound is the open problem
[ETH-A03](../01-algorithmic-core/ETH-A03-point-dependent-designs.md).

## Scope

The theorem covers every design built, like the preprint's Section 4, from auxiliary rows on
the label space $([r]\times[r])^Q$ with the group rule $a_w(t)=d_u(t)$, with arbitrary
node-dependent splittings. It does not cover designs whose locality pattern is not of this
product form, nor the tensor-contraction route of the preprint's Appendix C, whose square root
comes from a different count ([ETH-A04](../01-algorithmic-core/ETH-A04-tensor-mode-counting-barrier.md)).
