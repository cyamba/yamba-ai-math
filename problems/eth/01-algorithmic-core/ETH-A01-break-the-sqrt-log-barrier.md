# ETH-A01. Break the $\sqrt{\log n}$ barrier, or prove it intrinsic

| Field | Value |
| --- | --- |
| Category | Algorithmic core |
| Source items | "Problem 6 / YAMBA-378-06" (sharpening the exponent); "YMB-ETH-02"; implicit in every consequence |
| Status | **Open.** Method-level barriers and reformulations proved (SR-01 to SR-05) |
| Depends on the upstream theorem | No for the barrier statements; yes for the algorithmic meaning |
| Score (I/B/T/L/Lean) | 5 / 5 / 2 / 5 / 3, composite **4.2** |
| Subresults | [SR-01](../subresults/SR-01-isoperimetric-rank-barrier.md) to [SR-05](../subresults/SR-05-stress-duality-and-products.md), [SR-10](../subresults/SR-10-touched-vertices-barrier-criterion.md), [SR-11](../subresults/SR-11-subcube-identities-characterize-defects.md) |

## Task

Give a deterministic algorithm for $\#3$-SAT on $n$ variables running in
$2^{n/(\log n)^{\alpha}}$ for some $\alpha>\frac12$, or prove that every algorithm of the preprint's
form (polynomial replacement forms, Taylor data at $Q$ nodes from fixed Boolean substitutions,
measurement separation into $r$ groups, Hermite recovery) needs exponent
$n/(\log n)^{1/2+o(1)}$.

## What is known

* The preprint achieves $n\log\log n/\sqrt{\log n}$ in general and $n/\sqrt{\log n}$ at bounded
  density ([SOURCE.md](../SOURCE.md)); the expositions of Kintali and O'Donnell discuss no
  barrier (literature check, 2026-10-29).
* **Designs of the preprint's template cannot do better** (SR-01): with replacement rows of the
  form (2.16), (4.10) built from an $R$-admissible pair, the degree must satisfy
  $R\gtrsim\sqrt{Q\log(1/\varepsilon)}$, which is what produces the square root, and the preprint's
  $V_0f(W_0)$ is optimal up to a constant factor in $R$.
* **Designs outside the template escape that barrier.** The slab family (SR-04) beats every
  template design by a factor of order $R$ once $Q\ge\frac98(R+2)^2$ and $R$ is large, with a single measurement matrix ($c/D\le2/R$) or
  node-dependent ones; the general rank bound for node-dependent designs is only $4^{-R}/R$
  (SR-03), compatible with exponent $n(\log\log n)^{O(1)}/\log n$. Inside the swap algebra the
  problem is the cube polynomial problem CP(Q, R) (SR-02, SR-11), see
  [ETH-A03](ETH-A03-point-dependent-designs.md).
* **Quantitative target** (SR-04): a CP family with bad fraction $\beta\le R^{-C}$ gives exponent
  $n(\log n)^{-(C-1)/(C+1)+o(1)}$ at $Q\approx R^{(C+1)/2}$ when zero measurement rows are dropped
  (beats the square root iff $C>3$), and $n(\log n)^{-(C-1)/(C+2)+o(1)}$ at $Q\approx R^{(C+2)/3}$
  under the preprint's own row count (iff $C>4$). Such a design must leave almost every vertex
  fully good (SR-10).
* The tensor route (Appendix D) has its own square root from a partition count
  ([ETH-A04](ETH-A04-tensor-mode-counting-barrier.md)).

## Closest work

Preprint Sections 2.6, 2.7, 4 and Appendix D (level T, read in full, no proof audit; R039). Alman–Williams interpolation of
$(-1)^j$ on an interval for rigidity upper bounds (arXiv:1611.05558, level T). Probabilistic
degree of parity over the reals is $\tilde\Theta(\sqrt{n\log(1/\varepsilon)})$ (Srinivasan, Tripathi,
Venkitesh, arXiv:1910.02465, level T): the same Gaussian law that SR-01 isolates.

## Obstruction

Both known routes pay a Gaussian/partition square root; any improvement must change *how*
locality is bought: point-dependent designs, non-product auxiliary geometries, or a recursion
that does not count modes by weight.

## Smallest falsifier and first experiment

An explicit family for CP(64, 8) with per-direction bad fraction below
$\min\{1/8,\ \beta_{\rm win}(64,8)\}$, verified exactly by
[`cube_polynomial.py`](../experiments/cube_polynomial.py)-style rational checks; or, for the
barrier side, a proof that $\beta^*(Q,R)\ge R^{-3}$ once $Q\ge R^{2+\delta}$ ($R^{-4}$ under the
preprint's own row count), or the touched-set bound of
[SR-10](../subresults/SR-10-touched-vertices-barrier-criterion.md).

## Resource boundary

One fleet iteration: 3 to 5 agents (construction, algebra of stresses, Lean, critic), exact
arithmetic only, no claim of an exponent improvement without a Lean-checked design lemma and a
separate review.
