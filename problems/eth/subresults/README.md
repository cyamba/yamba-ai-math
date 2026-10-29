# Subresults of the `eth` set

Each file states one result with its status label (repository vocabulary: **established**,
**proved**, **conjecture**, **empirical**, **unverified**, **refuted**), its assurance (informal
proof, exact computation, Lean declaration in [`../lean/`](../lean/)), its dependence on the
upstream theorem, and the problems it feeds. Novelty is **not verified** for any of them; the
checks done so far are in the [novelty ledger](../RANKING.md#novelty-ledger). The ranking of the
subresults is in [RANKING.md](../RANKING.md#subresults-ranked).

| ID | Result | Status | Assurance | Upstream theorem needed |
| --- | --- | --- | --- | --- |
| [SR-01](SR-01-isoperimetric-rank-barrier.md) | Isoperimetric rank barrier for the preprint's template (rows (2.16), (4.10) from an $R$-admissible pair): $c/D\gtrsim e^{-\Theta(R^2/Q)}$; $V_0f(W_0)$ is optimal within the template up to a constant in $R$ | proved | Lean core (`RankBarrier.lean`), tail estimates informal | No |
| [SR-02](SR-02-cube-polynomial-designs.md) | Swap-algebra designs (outside the template, with node-dependent or single measurement matrices) are the cube polynomial problem CP(Q, R); subcube obstruction; small cases | proved; table empirical | Reduction informal and checked by masking actual matrices; obstruction in Lean (`SubcubeObstruction.lean`); small cases optimal within a coefficient box, five certified exactly | No |
| [SR-03](SR-03-point-dependent-rank-barrier.md) | Rank barrier for arbitrary point-dependent designs: $c_t/D\ge(h(r-h)/r^2)^R/R$ | proved | Lean (`PointDependentBarrier.lean`) | No |
| [SR-04](SR-04-slab-construction.md) | Global formulas and the slab family: bad fraction $\le1/R$ for every $Q$ ($c/D\le2/R$ with one matrix); leaving the template beats every template design by a factor of order $R$ for $Q\ge\frac98(R+2)^2$ and large $R$; improvement criterion $C>3$ (zero rows dropped) or $C>4$ (preprint's count) | proved | Lean for the cube-level statements (`SlabDesign.lean`); corollary, comparison and criterion informal | No |
| [SR-05](SR-05-stress-duality-and-products.md) | Stress duality (exact feasibility criterion), size of obstructions, weakness of relaxations, products of designs | proved | Lean for soundness and products (`StressDuality.lean`); completeness informal | No |
| [SR-06](SR-06-galactic-thresholds.md) | Explicit constants: the analysed bound beats $2^n$ from $\log_2n\le1.6\times10^5$, Grover from $\le1.8\times10^6$, PPSZ from $\le4\times10^6$ (parameter searches), and never before $\log_2n\approx3\times10^4$ | empirical | Exact evaluation of the preprint's cost bound | No (evaluates its cost model) |
| [SR-07](SR-07-graded-counting-bounded-density.md) | Exact Max-$k$-SAT histograms, weight enumerators and partition functions at bounded density | proved conditionally | Identities in Lean (`GradedCounting.lean`); reduction to Theorem C.1 informal | Yes (Theorem C.1) |
| [SR-08](SR-08-corrections-to-gemini-summaries.md) | Twenty corrections to the two seed summaries | established against the inspected preprint | Preprint at level T, Lean or exact computation where marked | No |
| [SR-09](SR-09-coverage-map.md) | Coverage map: which ETH-hard problems become subexponential, and the open boundary | proved conditionally | Reductions informal; bibliography at level T or A | Yes (Theorem 1.1) |
| [SR-10](SR-10-touched-vertices-barrier-criterion.md) | What an improvement forces: exponent $e$ needs $R\le eQ/3$ and touched measure $\le e/24$ (zero rows dropped; $\le e^2/12$ under the preprint's count); a touched-set bound $c/R$ (or $c/R^2$ under the preprint's count) for $R\le c_0\sqrt Q$ implies the square-root barrier; vertex-deletion form | proved (conjecture marked) | Informal; cost-model statements as in SR-04 | No |
| [SR-11](SR-11-subcube-identities-characterize-defects.md) | The subcube identities $\sum_{e\in\Gamma}\lambda^T_{t(e)}d_e=2^R$ characterize the defect functions of families: CP(Q, R) is a sparse solution of an explicit linear system, and every obstruction is a combination of subcube stresses | proved | Necessity in Lean (`subcube_identity`); sufficiency informal, checked exactly on 557 edge sets | No |

Dependencies: SR-01 → SR-02 → {SR-03, SR-04, SR-05, SR-10, SR-11}; SR-04, SR-05, SR-10 and SR-11 feed
[ETH-A03](../01-algorithmic-core/ETH-A03-point-dependent-designs.md); SR-06 feeds ETH-A06, ETH-F02 and
ETH-F03; SR-07 and SR-09 feed the counting and fine-grained problems.
