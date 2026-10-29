# ETH consequences: ranking for the next iteration

This file ranks the 37 problems and 11 subresults of the `eth` set so that the next iteration
can hand the most promising ones to fleets of agents. It was written on 2026-10-29 at the end
of the first iteration. Scores are judgments recorded with their rubric, not measurements;
re-score after every iteration. The upstream theorem is an **unverified claim** under external
review ([SOURCE.md](SOURCE.md)); problems marked "depends on the upstream theorem" inherit
that status.

## Rubric

Each problem file carries five scores from 1 to 5:

| Letter | Criterion | 5 means |
| --- | --- | --- |
| I | Impact if solved | Changes what is believed about the complexity of SAT or its consequences |
| B | Breakthrough potential | A solution would be a genuinely new theorem, not a routine corollary of the preprint |
| T | Tractability in one fleet iteration | A bounded team can plausibly settle it, or a well-defined part of it |
| L | Leverage | A solution unlocks several other problems or reusable tools |
| Lean | Fit for Lean and Mathlib | The statement and proof are finite, algebraic or combinatorial, and close to Mathlib |

**Composite** $=(3I+3B+2T+L+\mathrm{Lean})/10$, recomputed by script from the five scores (the
problem files were corrected to this formula on 2026-10-29). Ties are broken by $B$, then $T$.

## Tier 1: fleet-ready, with program contracts

### 1. Designs beyond the template and the square root (ETH-A03, 4.5; ETH-A01, 4.2): program [ETH001](../../programs/eth-point-dependent-designs.json)

**Why first.** It is the only route found to a better exponent for the method, and it is now a
clean finite problem with Lean-verified tools: designs of the preprint's own template provably
cannot beat the square root ([SR-01](subresults/SR-01-isoperimetric-rank-barrier.md)); swap-algebra
designs outside the template, with node-dependent or single measurement matrices, are exactly the
cube polynomial problem CP(Q, R) ([SR-02](subresults/SR-02-cube-polynomial-designs.md)), which has a
local linear form ([SR-11](subresults/SR-11-subcube-identities-characterize-defects.md)); the slab
family beats every template design in part of the parameter range
([SR-04](subresults/SR-04-slab-construction.md)); the general rank barrier leaves room down to
$4^{-R}/R$ ([SR-03](subresults/SR-03-point-dependent-rank-barrier.md)); feasibility has an exact dual
([SR-05](subresults/SR-05-stress-duality-and-products.md)); and an improvement would have to leave
almost every vertex fully good ([SR-10](subresults/SR-10-touched-vertices-barrier-criterion.md)).
Either outcome is publishable: a construction improves the exponent, a lower bound explains the
square root.

**Pinned completion statement:** [targets/ETH001.md](targets/ETH001.md) (hash in the program
contract; results for subclasses or small cases are `restricted` or `empirical`).

**The quantitative target** (SR-04): a family with per-direction bad fraction $\beta\le R^{-C}$
at $Q\approx R^{(C+1)/2}$ gives the exponent $n(\log n)^{-(C-1)/(C+1)+o(1)}$ when zero measurement
rows are dropped, beating $n/(\log n)^{1/2+o(1)}$ iff $C>3$; under the preprint's own row count
the threshold is $C>4$ at $Q\approx R^{(C+2)/3}$.

**Work packages for the fleet.**

| Package | Question | Smallest falsifier or first experiment |
| --- | --- | --- |
| Construction | Find families with $\beta$ well below $1/R$ at ratio $Q/R\ge R$: explain the small exact optima (one bad edge per direction at $R=Q-1$; the $(5,2)$ family with nodes $t/5$), generalize them, try soft region boundaries where neighbouring global formulas agree at the boundary nodes, and exploit special node sets | An exactly verified family with $Q\ge R^{2.5}$ and $\beta<R^{-3}$ |
| Lower bound | Prove the touched-set conjecture of [SR-10](subresults/SR-10-touched-vertices-barrier-criterion.md) (touched measure $\ge c/R$ when $R\le c_0\sqrt Q$, slab-tight, which gives the square-root barrier; $c/R^2$ suffices under the preprint's count), or $\beta^*(Q,R)\ge R^{-3-o(1)}$ for $Q\ge R^{2+\delta}$; first for region-based designs (good edges exactly inside the parts of a partition, one global formula per part), then in general; settle $R=2$ with generic nodes | A proof that every family with $Q\ge R^3$ has $\beta\ge c/R^2$ |
| Turán realizability | Is the edge set at an Alon or Ellis–Ivan–Leader vertex set (density $2^{-R/2+o(R)}$, meeting every $R$-subcube) the bad set of a polynomial family? | One moderate $R$ where it is, checked exactly |
| Exact data | Use the subcube system of [SR-11](subresults/SR-11-subcube-identities-characterize-defects.md) (edge variables only) for exact search; push exact optima to $Q=7,8$ (symmetry reduction, column generation over stresses) and fit $\beta^*$ against $1/R$, $R^{-2}$, $2^{-R/2}$ | A local-search run with an exact incremental oracle was started at the end of iteration 1; see [experiments/](experiments/README.md) |
| Lean | Formalize the rank formula of SR-02, Proposition 1 (now informal plus exact matrix checks), the sufficiency half of SR-11, and every new design lemma | `lake --wfail build` and a regenerated `verification.json` |

**Roles.** Constructor, exact verifier (rational arithmetic only), algebraist (stresses and
global formulas), Lean formalizer, and a separate critic. No exponent improvement is claimed
without a Lean-checked design lemma, a re-derived cost account and the critic's acceptance.

### 2. Counting at arbitrary density (ETH-C03, 3.4; ETH-C05, 3.4; ETH-C02, 3.0): program [ETH002](../../programs/eth-dense-graded-counting.json)

Bounded density is solved conditionally ([SR-07](subresults/SR-07-graded-counting-bounded-density.md)):
exact Max-$k$-SAT histograms and weight enumerators in $2^{O(n/\sqrt{\log n})}$. The open core is
whether the preprint's Theorem C.1 survives a second passive grading variable, which would give
the same at every density, and what that means for exact dense Max-2-SAT, where the best known
algorithm is still Williams's $O^*(2^{\omega n/3})$ with exponential space. Conditional on the
upstream theorem throughout. ETH-C05 (chromatic number, Hamiltonicity, dense permanents) has
the highest impact in the counting group but the lowest tractability; it should be attacked
only after the encoding boundary of [SR-09](subresults/SR-09-coverage-map.md) is sharpened.

### 3. Formal audit (ETH-G03, 3.3; ETH-G01, 3.0; ETH-A07, 2.0): program [ETH003](../../programs/eth-formal-audit.json)

Rebuild the upstream Lean development at a pinned commit, inventory what its top-level
statement says (machine model, encoding, exponent $n(\log\log n)^2/\sqrt{\log n}$, axioms), and
state the purely algebraic counting theorem it rests on, reusing the 47 verified declarations
of [`lean/`](lean/). This is the cheapest way to raise the assurance of everything conditional
in this folder, and it is independent of the external working group.

## Tier 2: next in line

| Problem | Composite | Why it waits |
| --- | --- | --- |
| [ETH-E02](05-circuits-proofs-space/ETH-E02-proof-complexity-of-the-algorithm.md) proof complexity of the algorithm | 3.3 | High novelty, but needs a precise proof system first |
| [ETH-D05](04-fine-grained/ETH-D05-planar-and-geometric-problems.md) planar and geometric problems | 3.2 | The source's claimed consequence is wrong; the real question (beating $2^{O(\sqrt n)}$) needs a new idea |
| [ETH-D08](04-fine-grained/ETH-D08-polylog-eth-and-surviving-lower-bounds.md) replacement hypotheses | 3.2 | Definitional; best done after the working group reports |
| [ETH-E01](05-circuits-proofs-space/ETH-E01-circuit-lower-bounds-williams-program.md) circuit lower bounds | 3.1 | An exponent improvement from Tier 1 feeds directly into it |
| [ETH-A04](01-algorithmic-core/ETH-A04-tensor-mode-counting-barrier.md) tensor mode counting | 3.0 | The Appendix C analogue of Tier 1; start once ETH001 has a verdict |
| [ETH-A06](01-algorithmic-core/ETH-A06-explicit-constants-and-crossover.md) explicit constants | 3.0 | Partly done ([SR-06](subresults/SR-06-galactic-thresholds.md)); improves automatically with Tier 1 |

## All problems, ranked

| Rank | Problem | Category | Composite | I / B / T / L / Lean | Status | Program |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | [ETH-A03](01-algorithmic-core/ETH-A03-point-dependent-designs.md) Designs beyond the preprint's template: the cube polynomial problem CP(Q, R) | Algorithmic core | **4.5** | 5 / 5 / 3 / 5 / 4 | **Open.** Reformulations, bounds, constructions and small exact optima proved; pinned target [ETH001](targets/ETH001.md) | ETH001 |
| 2 | [ETH-A01](01-algorithmic-core/ETH-A01-break-the-sqrt-log-barrier.md) Break the $\sqrt{\log n}$ barrier, or prove it intrinsic | Algorithmic core | **4.2** | 5 / 5 / 2 / 5 / 3 | **Open.** Method-level barriers and reformulations proved (SR-01 to SR-05) | ETH001 |
| 3 | [ETH-C03](03-counting/ETH-C03-max-sat-histogram.md) The exact Max-k-SAT clause histogram, and dense Max-2-SAT | Counting | **3.4** | 4 / 4 / 2 / 3 / 3 | **Solved conditionally at bounded density** (SR-07, Cor. A); **dense case open and important** | ETH002 |
| 4 | [ETH-C05](03-counting/ETH-C05-counting-beyond-linear-encodings.md) Beyond linear encodings: chromatic number, Hamiltonicity, dense permanents | Counting | **3.4** | 5 / 4 / 1 / 3 / 2 | **Open** | ETH002 |
| 5 | [ETH-E02](05-circuits-proofs-space/ETH-E02-proof-complexity-of-the-algorithm.md) Proof complexity: which proof systems capture the algorithm? | Circuits, proofs, space | **3.3** | 4 / 4 / 2 / 3 / 2 | **Open** |  |
| 6 | [ETH-G03](07-formalization/ETH-G03-audit-the-upstream-formalization.md) Audit the upstream Lean formalization | Formalization | **3.3** | 4 / 2 / 3 / 4 / 5 | **Open** | ETH003 |
| 7 | [ETH-D05](04-fine-grained/ETH-D05-planar-and-geometric-problems.md) Planar and geometric problems: can the algebra beat $2^{O(\sqrt n)}$? | Fine-grained complexity | **3.2** | 4 / 4 / 2 / 3 / 1 | **Open**; the source's claimed consequence is wrong |  |
| 8 | [ETH-D08](04-fine-grained/ETH-D08-polylog-eth-and-surviving-lower-bounds.md) Replacement hypotheses: polylog-ETH and the lower bounds that survive | Fine-grained complexity | **3.2** | 4 / 3 / 3 / 4 / 1 | **Open** (definitional and survey work) |  |
| 9 | [ETH-E01](05-circuits-proofs-space/ETH-E01-circuit-lower-bounds-williams-program.md) Circuit lower bounds through Williams's program | Circuits, proofs, space | **3.1** | 4 / 3 / 3 / 3 / 1 | **Conditional result in the preprint; improvement open** |  |
| 10 | [ETH-A04](01-algorithmic-core/ETH-A04-tensor-mode-counting-barrier.md) The tensor-contraction route: mode counting and its square root | Algorithmic core | **3.0** | 4 / 3 / 2 / 3 / 2 | **Open** |  |
| 11 | [ETH-A06](01-algorithmic-core/ETH-A06-explicit-constants-and-crossover.md) Explicit constants and the crossover with exhaustive search and PPSZ | Algorithmic core | **3.0** | 3 / 2 / 5 / 3 / 2 | **Partially solved** (SR-06); improvements open |  |
| 12 | [ETH-A02](01-algorithmic-core/ETH-A02-optimality-of-the-spectral-construction.md) Optimality of the spectral construction within the preprint's template | Algorithmic core | **3.0** | 3 / 2 / 4 / 3 / 4 | **Largely solved** by SR-01; constant factor and hypotheses open |  |
| 13 | [ETH-C02](03-counting/ETH-C02-weighted-counting-q-series.md) Weighted counting: the weight enumerator $Z_F(q)$, Max-Ones and exact-weight #SAT | Counting | **3.0** | 3 / 2 / 4 / 3 / 4 | **Solved conditionally at bounded density** (SR-07, Cor. B); **open at arbitrary density** | ETH002 |
| 14 | [ETH-G01](07-formalization/ETH-G01-decouple-algebraic-core.md) Decouple the algebraic counting core from the Turing-machine plumbing | Formalization | **3.0** | 3 / 2 / 3 / 4 / 5 | **Building blocks Lean-verified; assembly open** | ETH003 |
| 15 | [ETH-A08](01-algorithmic-core/ETH-A08-width-dependence-and-uw-seth.md) Dependence on the clause width and the unbounded-width frontier | Algorithmic core | **2.9** | 3 / 3 / 3 / 3 / 2 | **Partially solved conditionally** (SR-09); frontier open |  |
| 16 | [ETH-C04](03-counting/ETH-C04-graph-polynomials-and-partition-functions.md) Graph polynomials and partition functions | Counting | **2.9** | 3 / 3 / 3 / 2 / 3 | **Partly solved conditionally** (SR-07, Cor. C); Tutte at generic points and full chromatic polynomial **open** |  |
| 17 | [ETH-D07](04-fine-grained/ETH-D07-reduction-blowup-boundary.md) The reduction-blowup boundary: why NP ⊆ SUBEXP does not follow | Fine-grained complexity | **2.9** | 4 / 3 / 2 / 3 / 1 | **Open**, with one reported follow-up to inspect |  |
| 18 | [ETH-D03](04-fine-grained/ETH-D03-subexponential-fpt.md) Subexponential FPT algorithms from linear kernels | Fine-grained complexity | **2.8** | 3 / 2 / 4 / 2 / 3 | **Vertex Cover solved conditionally**; general picture open |  |
| 19 | [ETH-D02](04-fine-grained/ETH-D02-seth-nseth-gapeth-survivors.md) SETH, NSETH and Gap-ETH: what is refuted and what survives | Fine-grained complexity | **2.7** | 3 / 2 / 4 / 3 / 1 | **Conditional consequence; survivors partly mapped** |  |
| 20 | [ETH-F01](06-crypto-and-quantum/ETH-F01-inverting-local-functions.md) Inverting local functions: Goldreich's PRG and sparse LPN | Crypto and quantum | **2.7** | 3 / 2 / 4 / 2 / 2 | **Conditional consequences proved** (preprint Cor. C.2; SR-09 for sparse LPN); open beyond |  |
| 21 | [ETH-B01](02-algebraic-identities/ETH-B01-newton-parity-interpolation.md) Shifted Newton parity interpolation and its off-window defect | Algebraic identities | **2.7** | 2 / 1 / 5 / 3 / 5 | **Solved and Lean-verified**; two claims of the source corrected |  |
| 22 | [ETH-B02](02-algebraic-identities/ETH-B02-swap-algebra-support-localization.md) The commuting swap algebra and support localization | Algebraic identities | **2.7** | 2 / 1 / 5 / 3 / 5 | **Proved informally** (preprint Lemmas 4.2, 4.3); Lean open |  |
| 23 | [ETH-G02](07-formalization/ETH-G02-mathlib-serf-reduction-library.md) A Mathlib library of counting-preserving reductions | Formalization | **2.7** | 2 / 1 / 5 / 3 / 5 | **Started**: independent sets Lean-verified |  |
| 24 | [ETH-B03](02-algebraic-identities/ETH-B03-zero-pm-one-eigenbasis.md) The orthogonal $\{0,\pm1\}$ eigenbasis of the swap operators | Algebraic identities | **2.6** | 2 / 1 / 5 / 2 / 5 | **Proved informally** (preprint Section 2.7, Step 2; Lemma 4.1); statement in the source is correct |  |
| 25 | [ETH-B06](02-algebraic-identities/ETH-B06-boolean-differences.md) Boolean differences: Taylor data from fixed substitutions | Algebraic identities | **2.6** | 2 / 1 / 4 / 4 / 5 | **Solved and Lean-verified** (combinatorial core) |  |
| 26 | [ETH-B07](02-algebraic-identities/ETH-B07-measurement-separation-and-hermite-uniqueness.md) Measurement separation and Hermite uniqueness | Algebraic identities | **2.6** | 2 / 1 / 4 / 4 / 5 | **Solved and Lean-verified** (algebraic cores) |  |
| 27 | [ETH-C01](03-counting/ETH-C01-sharp-eth-collapse.md) The #ETH collapse: exact #k-SAT, sparse permanents and perfect matchings | Counting | **2.6** | 3 / 1 / 4 / 3 / 3 | **Conditional consequence** of the preprint (Thm 1.1, Cor. 1.3) |  |
| 28 | [ETH-D01](04-fine-grained/ETH-D01-ipz-constants-and-serf.md) The IPZ constants $s_k$ and the SERF class | Fine-grained complexity | **2.6** | 3 / 1 / 4 / 3 / 3 | **Conditional consequence; map done** (SR-09); refinements open |  |
| 29 | [ETH-D04](04-fine-grained/ETH-D04-treewidth-and-csps.md) Treewidth and CSPs: Marx's "Can you beat treewidth?" | Fine-grained complexity | **2.5** | 3 / 3 / 2 / 2 / 1 | **Open** (fixed domains trivial, growing domains open) |  |
| 30 | [ETH-B04](02-algebraic-identities/ETH-B04-hermite-weights-and-bit-lengths.md) Closed-form Hermite weights and bit lengths | Algebraic identities | **2.5** | 2 / 1 / 5 / 2 / 4 | **Solved** (proof below, exact check for $Q\le7$, $J\le5$); Lean open |  |
| 31 | [ETH-A05](01-algorithmic-core/ETH-A05-approximate-parity-interpolation.md) Approximate parity interpolation: Chebyshev, Krawtchouk and Padé alternatives | Algorithmic core | **2.4** | 2 / 2 / 4 / 2 / 2 | **Mostly negative** (analysis below); the 2-adic version is Appendix D |  |
| 32 | [ETH-D06](04-fine-grained/ETH-D06-gap-eth-approximation-barriers.md) Hardness of approximation built on ETH and Gap-ETH | Fine-grained complexity | **2.4** | 3 / 2 / 3 / 2 / 1 | **Open** (map needed) |  |
| 33 | [ETH-E03](05-circuits-proofs-space/ETH-E03-polynomial-space-exact-algorithms.md) Space: subexponential time with small space | Circuits, proofs, space | **2.2** | 2 / 2 / 3 / 2 / 2 | **Open** (refinement); the source's framing corrected |  |
| 34 | [ETH-F03](06-crypto-and-quantum/ETH-F03-quantum-versus-classical.md) Quantum versus classical: Grover and the new algorithm | Crypto and quantum | **2.0** | 2 / 2 / 3 / 1 / 1 | **Asymptotic statement correct; crossover computed** (SR-06); quantum speedup of the new algorithm open |  |
| 35 | [ETH-F02](06-crypto-and-quantum/ETH-F02-cryptographic-parameter-scaling.md) Cryptographic parameter scaling and concrete security | Crypto and quantum | **2.0** | 2 / 1 / 4 / 2 / 1 | **Answered for concrete sizes** (SR-06); asymptotic bookkeeping open |  |
| 36 | [ETH-A07](01-algorithmic-core/ETH-A07-lean-versus-manuscript-exponent.md) Close the gap between the Lean exponent and the manuscript's | Algorithmic core | **2.0** | 2 / 1 / 2 / 2 / 5 | **Open** | ETH003 |
| 37 | [ETH-B05](02-algebraic-identities/ETH-B05-minc-permanent-expansion.md) Minc's permanent expansion and bounded-scope Taylor extraction | Algebraic identities | **1.9** | 1 / 1 / 4 / 1 / 4 | **Classical identity; not used by the preprint**; Lean open |  |

## Subresults, ranked

Rubric: S significance, N novelty potential given the closest-work check, A assurance (5: core
Lean-verified and exact checks; 4: proved with a Lean-verified core; 3: proved informally or
conditionally; 2: empirical), V value as a base for further work. Composite
$=(3S+3N+2A+2V)/10$.

| Rank | Subresult | S / N / A / V | Composite | One line |
| --- | --- | --- | --- | --- |
| 1 | [SR-02](subresults/SR-02-cube-polynomial-designs.md) cube polynomial problem | 5 / 4 / 4 / 5 | **4.5** | Point-dependent swap designs are exactly CP(Q, R); subcube obstruction in Lean |
| 2 | [SR-04](subresults/SR-04-slab-construction.md) slab construction | 4 / 4 / 5 / 5 | **4.4** | Global formulas; $\beta\le1/R$ for every $Q$ ($2/R$ with one matrix); beats every template design by a factor of order $R$ for $Q\ge\frac98(R+2)^2$ and large $R$; the $C>3$ / $C>4$ criteria |
| 3 | [SR-10](subresults/SR-10-touched-vertices-barrier-criterion.md) touched vertices | 5 / 4 / 3 / 5 | **4.3** | An improvement forces almost every vertex to be fully good; a touched-set bound $c/R^2$ would prove the square-root barrier |
| 4 | [SR-03](subresults/SR-03-point-dependent-rank-barrier.md) point-dependent rank barrier | 4 / 4 / 5 / 4 | **4.2** | Every design needs $c_t/D\ge(h(r-h)/r^2)^R/R$; leaves room for $n\,\mathrm{polylog}/\log n$ |
| 5 | [SR-11](subresults/SR-11-subcube-identities-characterize-defects.md) subcube identities | 4 / 4 / 4 / 5 | **4.2** | CP(Q, R) is a sparse solution of one explicit identity per $R$-subcube; obstructions are combinations of subcube stresses |
| 6 | [SR-01](subresults/SR-01-isoperimetric-rank-barrier.md) isoperimetric rank barrier | 4 / 4 / 4 / 4 | **4.0** | Designs of the preprint's template pay the Gaussian price; its matrix is optimal within the template up to a constant in $R$ |
| 7 | [SR-05](subresults/SR-05-stress-duality-and-products.md) stress duality and products | 3 / 3 / 4 / 4 | **3.4** | Exact feasibility criterion; relaxations are exponentially weak; products preserve $\beta$ |
| 8 | [SR-07](subresults/SR-07-graded-counting-bounded-density.md) graded counting | 3 / 3 / 3 / 3 | **3.0** | Conditional: exact Max-$k$-SAT histograms and weight enumerators at bounded density |
| 9 | [SR-09](subresults/SR-09-coverage-map.md) coverage map | 3 / 2 / 3 / 3 | **2.7** | Which ETH-hard problems transfer, with corrected exponents and the open boundary |
| 10 | [SR-06](subresults/SR-06-galactic-thresholds.md) galactic thresholds | 3 / 2 / 3 / 2 | **2.5** | With the best parameters found the analysed bound beats $2^n$ from about $n=2^{1.6\times10^5}$ |
| 11 | [SR-08](subresults/SR-08-corrections-to-gemini-summaries.md) corrections ledger | 2 / 1 / 4 / 2 | **2.1** | Twenty corrections to the seed summaries |

SR-01 to SR-05, SR-10 and SR-11 form one story and are written up as a draft article in
[articles/](articles/README.md).

## Novelty ledger

**Novelty status of every subresult: NOT VERIFIED.** What was checked, on 2026-10-29 (sources and
inspection levels in the
[reading list](../../references/reading-list.md#exponential-time-hypothesis-consequences)):

| Subresult | Closest work found | What differs | Still to check |
| --- | --- | --- | --- |
| SR-01 | O'Donnell's exposition (R041), Lemma 4.1, a rank identity inside the swap algebra; Aspnes, Beigel, Furst, Rudich (R043) on sign errors of low-degree polynomials | Neither states a lower bound for all template designs or the optimality of $V_0f(W_0)$ | The working group's notes; the reported Anthropic paper (R058) |
| SR-02 | The preprint's Definitions 2.1 and 3.1 allow designs beyond its template (and node-dependent matrices), but its construction uses the template; no exposition discusses other designs | The reduction to CP(Q, R) and the subcube obstruction | Rigidity of direction networks with normals on the moment curve |
| SR-03 | Rank subadditivity arguments are standard | The barrier for point-dependent designs and its explicit form | Lower bounds for "measurement separation" in the polynomial-method literature |
| SR-04 | Interpolation of parity on an interval: Alman and Williams (R048); probabilistic degree of parity (R047) | Global formulas, the slab family, the comparison with all template designs, the improvement criteria | Follow-ups to the preprint after 2026-10-29 |
| SR-05 | Hypercube Turán problems: Alon, Krech, Szabó (R044); Ellis, Ivan, Leader (R045); Alon (R046); $C_4$-free subgraphs (R059) | The algebraic (stress) characterization and the weakness of the combinatorial relaxations | Whether the Turán constructions are realizable |
| SR-10 | Vertex-deletion and Turán problems in the hypercube (R044 to R046); sign-error bounds (R043) | The reduction of an exponent improvement to tiny touched sets, and the barrier criterion | Whether deletion problems for algebraic realizability have been studied |
| SR-11 | Stress duality of SR-05; rigidity-type characterizations of stresses | That subcube stresses generate all obstructions, and the local linear form | Linear-algebraic descriptions of polynomial-valued functions on the cube in the literature on cube complexes and splines |
| SR-07 | Preprint Corollaries 1.2 and 1.3 | Exact histograms and weight enumerators are not stated there | Graded counting in the tensor-network literature |

The literature check was done by web retrieval within one session; it is not a systematic
review. A claim of novelty in a publication needs the remaining checks above.

## Notes for the next iteration

What worked and what to change, kept short so the next session can act on it:

* **Exact re-verification caught overclaims.** The first draft said the slab is optimal for
  $R=2$; the exact data show this only for $Q\le4$ (a family with 7 bad edges per direction
  exists at $Q=5$). Keep "every reported family re-checked in exact arithmetic" as a rule.
* **The MILP stops at $Q=6$.** Bigger instances need structure: symmetry reduction, column
  generation over stresses, or local search with an exact incremental oracle.
* **Lean.** `import Mathlib` was unusable (full oleans not built); importing specific modules
  kept builds near 40 s. `lake --wfail build` rejects unused section variables, so use
  `omit ... in`.
* **Scores drift.** Fifteen composites were off the formula; they are now recomputed by
  script. Re-run the check after editing any score.
* **Seed summaries are maps, not sources.** Twenty corrections ([SR-08](subresults/SR-08-corrections-to-gemini-summaries.md)),
  the most important being the exponent $n/(\log n)^{1/2+o(1)}$, not $n/\log n$.
