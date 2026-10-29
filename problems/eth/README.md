# Problem set `eth`: consequences of "The Exponential Time Hypothesis is False"

Source: openai/math family 378, "The Exponential Time Hypothesis is False" (manuscript revised
2026-10-25, released 2026-10-26), which claims a deterministic algorithm counting the
satisfying assignments of a $k$-CNF in $2^{O_k(n\log\log n/\sqrt{\log n})}$ time and polynomial
space. **The theorem is an unverified upstream claim** under review by a working group led by
Impagliazzo, Paturi and Williams. What we read, and how carefully, is in [SOURCE.md](SOURCE.md);
the external development is logged as [NR-002](../../novelty_radar/NR-002-eth-refutations.md).

The set was seeded from two AI-generated summaries of consequences supplied with the request;
their errors are corrected in [SR-08](subresults/SR-08-corrections-to-gemini-summaries.md).

## What is here

| Path | Holds |
| --- | --- |
| [SOURCE.md](SOURCE.md) | The theorem, its mechanism in one page, inspection levels |
| [RANKING.md](RANKING.md) | Rubric, the ranked problem and subresult lists, program contracts for the next iteration, novelty ledger |
| `01-` to `07-` | One file per problem: statement, status label, closest work, obstruction, smallest falsifier, resource boundary, score |
| [subresults/](subresults/README.md) | Nine subresults proved or computed in iteration 1 |
| [lean/](lean/) | Lake project `EthConsequences` (Lean 4.34.1, pinned Mathlib): 45 checked declarations, certificate [`verification.json`](lean/verification.json) |
| [experiments/](experiments/README.md) | Exact computations (cube polynomial optima, swap-matrix ranks, Hermite weights, galactic thresholds) |
| [articles/](articles/README.md) | Draft article on point-dependent designs and the square-root barrier |

## Headline results of iteration 1

All results below concern the **method** of the preprint unless marked conditional; none
depends on the theorem being true unless it says so. Novelty is **not verified**
([novelty ledger](RANKING.md#novelty-ledger)).

1. **Where the square root comes from** ([SR-01](subresults/SR-01-isoperimetric-rank-barrier.md),
   proved, Lean core). Every design that uses one measurement matrix at all nodes pays a Gaussian
   price $c/D\gtrsim e^{-\Theta(R^2/Q)}$; the preprint's matrix is optimal up to a constant in $R$.
2. **Point-dependent designs are a clean cube problem** ([SR-02](subresults/SR-02-cube-polynomial-designs.md),
   proved and checked on actual matrices). The measurement count at node $t$ equals the weight of
   the bad edges in direction $t$ of a family of polynomials on the cube.
3. **Point dependence provably helps, but not yet enough** ([SR-04](subresults/SR-04-slab-construction.md),
   Lean). The slab family has bad fraction $\le1/R$ for every $Q$, beating every single-matrix
   design once $Q\ge\frac98(R+2)^2$. A family with $\beta\le R^{-C}$, $C>4$, at $Q\approx R^{(C+2)/3}$
   would improve the exponent to $n(\log n)^{-(C-1)/(C+2)+o(1)}$.
4. **The general barrier is far away** ([SR-03](subresults/SR-03-point-dependent-rank-barrier.md),
   Lean): any design needs only $c_t/D\ge4^{-R}/R$, which would still allow $n(\log\log n)^{O(1)}/\log n$.
5. **Exact feasibility and products** ([SR-05](subresults/SR-05-stress-duality-and-products.md),
   Lean for one direction): a set of edges can be made good iff every stress has zero total;
   combinatorial relaxations are exponentially weak, so a polynomial lower bound must use algebra.
6. **The analysed bound is galactic** ([SR-06](subresults/SR-06-galactic-thresholds.md), exact
   evaluation): it beats $2^n$ only for $n\gtrsim2^{160000}$ and PPSZ only for $n\gtrsim2^{4\times10^6}$.
7. **Conditional counting consequences** ([SR-07](subresults/SR-07-graded-counting-bounded-density.md),
   [SR-09](subresults/SR-09-coverage-map.md)): exact Max-$k$-SAT histograms and weight enumerators at
   bounded density, and a coverage map of which ETH-hard problems transfer.

## Problems by category

Composite scores follow the rubric in [RANKING.md](RANKING.md#rubric).

### [01-algorithmic-core](01-algorithmic-core/): Algorithmic core: the method itself, its exponent and its barriers

| Problem | Status | Composite |
| --- | --- | --- |
| [ETH-A01](01-algorithmic-core/ETH-A01-break-the-sqrt-log-barrier.md) Break the $\sqrt{\log n}$ barrier, or prove it intrinsic | **Open.** Method-level barriers and reformulations proved (SR-01 to SR-05) | 4.2 |
| [ETH-A02](01-algorithmic-core/ETH-A02-optimality-of-the-spectral-construction.md) Optimality of the single-matrix spectral construction | **Largely solved** by SR-01; constant factor and hypotheses open | 3.0 |
| [ETH-A03](01-algorithmic-core/ETH-A03-point-dependent-designs.md) Point-dependent designs: the cube polynomial problem CP(Q, R) | **Open.** Reformulation, bounds, constructions and small exact optima proved | 4.5 |
| [ETH-A04](01-algorithmic-core/ETH-A04-tensor-mode-counting-barrier.md) The tensor-contraction route: mode counting and its square root | **Open** | 3.0 |
| [ETH-A05](01-algorithmic-core/ETH-A05-approximate-parity-interpolation.md) Approximate parity interpolation: Chebyshev, Krawtchouk and Padé alternatives | **Mostly negative** (analysis below); the 2-adic version is Appendix C | 2.4 |
| [ETH-A06](01-algorithmic-core/ETH-A06-explicit-constants-and-crossover.md) Explicit constants and the crossover with exhaustive search and PPSZ | **Partially solved** (SR-06); improvements open | 3.0 |
| [ETH-A07](01-algorithmic-core/ETH-A07-lean-versus-manuscript-exponent.md) Close the gap between the Lean exponent and the manuscript's | **Open** | 2.0 |
| [ETH-A08](01-algorithmic-core/ETH-A08-width-dependence-and-uw-seth.md) Dependence on the clause width and the unbounded-width frontier | **Partially solved conditionally** (SR-09); frontier open | 2.9 |

### [02-algebraic-identities](02-algebraic-identities/): Algebraic identities behind the method

| Problem | Status | Composite |
| --- | --- | --- |
| [ETH-B01](02-algebraic-identities/ETH-B01-newton-parity-interpolation.md) Shifted Newton parity interpolation and its off-window defect | **Solved and Lean-verified**; two claims of the source corrected | 2.7 |
| [ETH-B02](02-algebraic-identities/ETH-B02-swap-algebra-support-localization.md) The commuting swap algebra and support localization | **Proved informally** (preprint Lemmas 4.2, 4.3); Lean open | 2.7 |
| [ETH-B03](02-algebraic-identities/ETH-B03-zero-pm-one-eigenbasis.md) The orthogonal $\{0,\pm1\}$ eigenbasis of the swap operators | **Proved informally** (preprint Section 2.7, Step 2; Lemma 4.2); statement in the source is correct | 2.6 |
| [ETH-B04](02-algebraic-identities/ETH-B04-hermite-weights-and-bit-lengths.md) Closed-form Hermite weights and bit lengths | **Solved** (proof below, exact check for $Q\le7$, $J\le5$); Lean open | 2.5 |
| [ETH-B05](02-algebraic-identities/ETH-B05-minc-permanent-expansion.md) Minc's permanent expansion and bounded-scope Taylor extraction | **Classical identity; not used by the preprint**; Lean open | 1.9 |
| [ETH-B06](02-algebraic-identities/ETH-B06-boolean-differences.md) Boolean differences: Taylor data from fixed substitutions | **Solved and Lean-verified** (combinatorial core) | 2.6 |
| [ETH-B07](02-algebraic-identities/ETH-B07-measurement-separation-and-hermite-uniqueness.md) Measurement separation and Hermite uniqueness | **Solved and Lean-verified** (algebraic cores) | 2.6 |

### [03-counting](03-counting/): Counting consequences

| Problem | Status | Composite |
| --- | --- | --- |
| [ETH-C01](03-counting/ETH-C01-sharp-eth-collapse.md) The #ETH collapse: exact #k-SAT, sparse permanents and perfect matchings | **Conditional consequence** of the preprint (Thm 1.1, Cor. 1.3) | 2.6 |
| [ETH-C02](03-counting/ETH-C02-weighted-counting-q-series.md) Weighted counting: the weight enumerator $Z_F(q)$, Max-Ones and exact-weight #SAT | **Solved conditionally at bounded density** (SR-07, Cor. B); **open at arbitrary density** | 3.0 |
| [ETH-C03](03-counting/ETH-C03-max-sat-histogram.md) The exact Max-k-SAT clause histogram, and dense Max-2-SAT | **Solved conditionally at bounded density** (SR-07, Cor. A); **dense case open and important** | 3.4 |
| [ETH-C04](03-counting/ETH-C04-graph-polynomials-and-partition-functions.md) Graph polynomials and partition functions | **Partly solved conditionally** (SR-07, Cor. C); Tutte at generic points and full chromatic polynomial **open** | 2.9 |
| [ETH-C05](03-counting/ETH-C05-counting-beyond-linear-encodings.md) Beyond linear encodings: chromatic number, Hamiltonicity, dense permanents | **Open** | 3.4 |

### [04-fine-grained](04-fine-grained/): Fine-grained complexity

| Problem | Status | Composite |
| --- | --- | --- |
| [ETH-D01](04-fine-grained/ETH-D01-ipz-constants-and-serf.md) The IPZ constants $s_k$ and the SERF class | **Conditional consequence; map done** (SR-09); refinements open | 2.6 |
| [ETH-D02](04-fine-grained/ETH-D02-seth-nseth-gapeth-survivors.md) SETH, NSETH and Gap-ETH: what is refuted and what survives | **Conditional consequence; survivors partly mapped** | 2.7 |
| [ETH-D03](04-fine-grained/ETH-D03-subexponential-fpt.md) Subexponential FPT algorithms from linear kernels | **Vertex Cover solved conditionally**; general picture open | 2.8 |
| [ETH-D04](04-fine-grained/ETH-D04-treewidth-and-csps.md) Treewidth and CSPs: Marx's "Can you beat treewidth?" | **Open** (fixed domains trivial, growing domains open) | 2.5 |
| [ETH-D05](04-fine-grained/ETH-D05-planar-and-geometric-problems.md) Planar and geometric problems: can the algebra beat $2^{O(\sqrt n)}$? | **Open**; the source's claimed consequence is wrong | 3.2 |
| [ETH-D06](04-fine-grained/ETH-D06-gap-eth-approximation-barriers.md) Hardness of approximation built on ETH and Gap-ETH | **Open** (map needed) | 2.4 |
| [ETH-D07](04-fine-grained/ETH-D07-reduction-blowup-boundary.md) The reduction-blowup boundary: why NP ⊆ SUBEXP does not follow | **Open**, with one reported follow-up to inspect | 2.9 |
| [ETH-D08](04-fine-grained/ETH-D08-polylog-eth-and-surviving-lower-bounds.md) Replacement hypotheses: polylog-ETH and the lower bounds that survive | **Open** (definitional and survey work) | 3.2 |

### [05-circuits-proofs-space](05-circuits-proofs-space/): Circuits, proof complexity and space

| Problem | Status | Composite |
| --- | --- | --- |
| [ETH-E01](05-circuits-proofs-space/ETH-E01-circuit-lower-bounds-williams-program.md) Circuit lower bounds through Williams's program | **Conditional result in the preprint; improvement open** | 3.1 |
| [ETH-E02](05-circuits-proofs-space/ETH-E02-proof-complexity-of-the-algorithm.md) Proof complexity: which proof systems capture the algorithm? | **Open** | 3.3 |
| [ETH-E03](05-circuits-proofs-space/ETH-E03-polynomial-space-exact-algorithms.md) Space: subexponential time with small space | **Open** (refinement); the source's framing corrected | 2.2 |

### [06-crypto-and-quantum](06-crypto-and-quantum/): Cryptography and quantum computing

| Problem | Status | Composite |
| --- | --- | --- |
| [ETH-F01](06-crypto-and-quantum/ETH-F01-inverting-local-functions.md) Inverting local functions: Goldreich's PRG and sparse LPN | **Conditional consequences proved** (preprint Cor. D.2; SR-09 for sparse LPN); open beyond | 2.7 |
| [ETH-F02](06-crypto-and-quantum/ETH-F02-cryptographic-parameter-scaling.md) Cryptographic parameter scaling and concrete security | **Answered for concrete sizes** (SR-06); asymptotic bookkeeping open | 2.0 |
| [ETH-F03](06-crypto-and-quantum/ETH-F03-quantum-versus-classical.md) Quantum versus classical: Grover and the new algorithm | **Asymptotic statement correct; crossover computed** (SR-06); quantum speedup of the new algorithm open | 2.0 |

### [07-formalization](07-formalization/): Formalization

| Problem | Status | Composite |
| --- | --- | --- |
| [ETH-G01](07-formalization/ETH-G01-decouple-algebraic-core.md) Decouple the algebraic counting core from the Turing-machine plumbing | **Building blocks Lean-verified; assembly open** | 3.0 |
| [ETH-G02](07-formalization/ETH-G02-mathlib-serf-reduction-library.md) A Mathlib library of counting-preserving reductions | **Started**: independent sets Lean-verified | 2.7 |
| [ETH-G03](07-formalization/ETH-G03-audit-the-upstream-formalization.md) Audit the upstream Lean formalization | **Open** | 3.3 |

## Verifying the Lean certificate

```sh
cd problems/eth/lean
python3 verify.py          # builds with lake --wfail, inventories statements and axioms
```

The script needs the Lean toolchain named in `lean-toolchain` on `PATH` and rewrites
`verification.json` with file hashes, the theorem list and the axioms used (currently only
`Classical.choice`, `Quot.sound` and `propext`).
