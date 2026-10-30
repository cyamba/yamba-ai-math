# Ranking for the next iteration

Iteration 1 (2026-10-30). Scores are judgements, not measurements. Each problem is scored 1 to 10 on

* **B**: breakthrough potential (size of the result if it succeeds),
* **N**: novelty (distance from what the preprint already contains),
* **T**: tractability for an agent fleet within one iteration,
* **L**: leverage (formalisability in Lean, reuse by other problems),

and ranked by `score = 0.40 B + 0.25 N + 0.20 T + 0.15 L`.

## A. Problems for the next fleets

| Rank | ID | Problem | B | N | T | L | Score |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | [ETH-B03](B-exponent-frontier/ETH-B03-polynomial-row-routing.md) | General polynomial rows: is `eps* = 2^{-Theta(R)}` possible? | 10 | 9 | 5 | 5 | **8.00** |
| 2 | [ETH-B04](B-exponent-frontier/ETH-B04-loglog-gap.md) item 2 | Which template assumption does the tensor route escape, and can that mechanism go below `sqrt(log n)`? | 8 | 8 | 6 | 5 | **7.15** |
| 3 | [ETH-B07](B-exponent-frontier/ETH-B07-sparse-embedding-escape.md) | Used-label measurement: type-balanced labelings avoid every product block | 8 | 8 | 6 | 4 | **7.00** |
| 4 | [ETH-C01](C-counting-extensions/ETH-C01-weighted-q-series.md) | Weight enumerator; k-Vertex Cover in `2^{o(k)}` | 6 | 6 | 8 | 7 | **6.55** |
| 5 | [ETH-C03](C-counting-extensions/ETH-C03-dense-exact-maxsat.md) | Exact Max-k-SAT for dense formulas (mod `2^l` binomial moments) | 7 | 7 | 6 | 5 | **6.50** |
| 6 | [ETH-D10](D-complexity-consequences/ETH-D10-proof-complexity.md) | `2^{o(n)}` Extended Frege / IPS refutations of 3-CNFs | 7 | 9 | 4 | 4 | **6.45** |
| 7 | [ETH-B05](B-exponent-frontier/ETH-B05-width-threshold.md) | Largest width `k(n)` with `2^{o(n)}` | 6 | 6 | 7 | 5 | **6.05** |
| 8 | [ETH-B08](B-exponent-frontier/ETH-B08-sqrt-log-hypothesis.md) | Restricted-model lower bound `2^{n/(log n)^{1/2+o(1)}}` | 7 | 8 | 3 | 3 | **5.85** |
| 9 | [ETH-D05](D-complexity-consequences/ETH-D05-parameterized.md) | Clique in `n^{o(k)}`? (hinges on B05) | 6 | 6 | 5 | 4 | **5.50** |
| 10 | [ETH-C04](C-counting-extensions/ETH-C04-graph-polynomials.md) | Spin systems; full chromatic polynomial | 5 | 5 | 7 | 5 | **5.40** |
| 11 | [ETH-A07](A-algebraic-core/ETH-A07-algebraic-core-decoupling.md) | Sorry-free algebraic core in Mathlib | 4 | 5 | 5 | 10 | **5.35** |
| 12 | [ETH-D06](D-complexity-consequences/ETH-D06-treewidth-csp.md) | Bounded-domain CSP by treewidth | 5 | 6 | 6 | 4 | **5.30** |
| 13 | [ETH-D08](D-complexity-consequences/ETH-D08-circuit-lower-bounds.md) | Beyond `n sqrt(log n)` circuit bounds | 6 | 6 | 3 | 3 | **4.95** |
| 14 | [ETH-C02](C-counting-extensions/ETH-C02-serf-reductions-lean.md) | Verified reduction library | 3 | 3 | 7 | 9 | **4.70** |
| 15 | [ETH-A02](A-algebraic-core/ETH-A02-swap-algebra-support.md) / [A03](A-algebraic-core/ETH-A03-swap-eigenbasis.md) | Swap algebra in Lean | 2 | 3 | 8 | 9 | **4.50** |
| 16 | [ETH-B06](B-exponent-frontier/ETH-B06-crossover-constant.md) | Explicit constants, crossover with PPSZ | 3 | 4 | 8 | 4 | **4.40** |
| 17 | [ETH-A04](A-algebraic-core/ETH-A04-hermite-recovery.md) | Explicit Hermite weights and bit lengths | 2 | 3 | 8 | 7 | **4.15** |
| 18 | [ETH-B04](B-exponent-frontier/ETH-B04-loglog-gap.md) items 1, 3 | Lean for the tensor route; `n/sqrt(log n)` for all `m` | 3 | 3 | 4 | 9 | **4.10** |
| 19 | [ETH-A05](A-algebraic-core/ETH-A05-taylor-extraction.md) | Taylor truncation and Minc expansion in Lean | 2 | 3 | 7 | 7 | **3.90** |
| 20 | [ETH-B02](B-exponent-frontier/ETH-B02-spectral-approximants.md) | Quantitative "no rounding gain" | 2 | 4 | 7 | 3 | **3.65** |
| 21 | ETH-D01 to D04, D07, D09, D11 to D13 | Audits; open sub-questions listed in each file | 2 to 5 | | | | < 3.5 |

## B. Subresults obtained in iteration 1

| Rank | Subresult | Status | Why it ranks here | Where |
| --- | --- | --- | --- | --- |
| 1 | **Routing rigidity (Theorem A)**: every routing-supported `M` has `rank(I-M) >= D e^{-O(1+R^2/Q)}` (`R <= Q/6`) | **proved, Lean** | Settles the full-measurement `M_0` template up to constants; basis of the article | [RoutingRigidity.lean](lean/EthProblems/RoutingRigidity.lean), [article](articles/sqrt-log-barrier.md) |
| 2 | **Template optimality (Theorem B)**: exponent `>= c n (log log n)^2 / sqrt(log n)` for every full-measurement `M_0`-form instantiation | **proved** (paper proof, refereed internally) | Shows the preprint's interpolation route is optimal for its template; the tensor route must escape it | [ETH-B01](B-exponent-frontier/ETH-B01-sqrt-log-barrier.md) |
| 3 | **General rows: `eps* >= 4^{-R}`** and the computation that `2^{-Theta(R)}` would give `n (log log n)^3 / log n` | **proved** | Pinpoints the one escape and its payoff; drives rank-1 problem | [ETH-B03](B-exponent-frontier/ETH-B03-polynomial-row-routing.md) |
| 4 | Non-commutative beats commutative at `(3,2,2)`: 10 to 9 | **empirical** (LB 8 proved) | First evidence that the swap algebra is not optimal; constant-factor only by Theorem A | [checks/](checks/) |
| 5 | Biased Smolensky lemma (Lemma B) | **proof sketch**, exact check `Q <= 4` | Spectral view of the commutative case | [ETH-B01](B-exponent-frontier/ETH-B01-sqrt-log-barrier.md) |
| 6 | Interval optimality: degree `< R` cannot match parity on `R+1` consecutive points | **proved, Lean** | One-dimensional shadow of the barrier | [ParityInterpolant.lean](lean/EthProblems/ParityInterpolant.lean) |
| 7 | Exact off-interval defect; sheet formula refuted | **proved, Lean** | Corrects the input sheet; entry-size bounds | ETH-A01 |
| 8 | Source audit: exponent is `n/sqrt(log n)`, not `n/log n`; planar claim refuted | **established** against the preprint | Prevents fleets from building on a wrong exponent | [SOURCE-AUDIT.md](SOURCE-AUDIT.md) |
| 9 | Hermite uniqueness, Mobius inversion, deformed partition identity | **proved, Lean** | Reusable algebraic layer for ETH-A07 | [lean/](lean/) |
| 10 | k-Vertex Cover in `poly(n) + 2^{o(k)}` via weight enumerator | **proof sketch** | Concrete new FPT consequence, conditional on Theorem 1 | ETH-C01 |
| 11 | Exact Max-k-SAT histogram for `m <= Dn` | **proof sketch** | Strengthens Cor. 1.1 in the linear regime | ETH-C05 |

Article written for subresults 1 to 3 (highest novelty and score); revision 2 incorporates an internal
referee pass that removed a false claim and strengthened Theorem B:
[articles/sqrt-log-barrier.md](articles/sqrt-log-barrier.md).

## C. Fleet briefs for the top four

Roles refer to [agents/registry.json](../../agents/registry.json); topologies to
[fleets/registry.json](../../fleets/registry.json). Every substantive claim needs a separate `critic` pass.

### Fleet 1: ETH-B03, general polynomial rows (topology `discover`)

* **Goal.** Decide whether node-dependent row-space components beat the `e^{-R^2/Q}` routing rigidity.
* **Roles.** `experimenter` (exact small cases), `conjecturer` (constructions), `mathematician`
  (lower-bound arguments beyond a single node set), `critic`.
* **Deliverables.** (a) exact `eps*` for general rows at `(3,2,2)` and `(4,2,2)` by Groebner bases or
  `{0,+-1}`-restricted search; (b) either a construction with `log(1/eps) >> R^2/Q` or a proof that general rows
  obey Theorem A up to constants.
* **Smallest falsifier.** If exact general-row `eps*` equals the `M_0`-form optimum at `(3,2,2)` and
  `(4,2,2)`, lower the priority of constructions and raise the lower-bound branch.
* **Budget.** CPU-only; tiny instances run in minutes on 2 cores.

### Fleet 2: what the tensor route escapes (topology `theorem`)

* **Goal.** The tensor-contraction route beats the interpolation template's optimum `rho(n)`. Find which
  template assumption it violates (Cauchy deformation on packets, recursion, structured recovery points),
  state a common "routing design" abstraction, and test whether that mechanism can go below `sqrt(log n)`.
* **Roles.** `decomposer`, `mathematician`, `critic`. Output: a lemma note plus a Lean statement.

### Fleet 3: ETH-B07, used-label measurement (topology `explore`)

* **Goal.** Type-balanced labelings already avoid every product block of Theorem A. Either prove a used-label
  rigidity bound (blocks over type classes and position subsets) or construct `M_0` with small
  `rank((I - M_0)[U,U])` for type-balanced `U`, and evaluate the resulting exponent.
* **Roles.** `scout` (coding-theory constructions), `experimenter`, `critic`.

### Fleet 4: ETH-C01 and ETH-C05 to full proofs (topology `pair`)

* **Goal.** Turn the two proof sketches into complete arguments with bit-length bounds; add the Lean identity
  layer. Produces citable corollaries (k-Vertex Cover in `2^{o(k)}`, exact linear-density Max-SAT).
* **Roles.** `mathematician`, `critic`.

## D. Process notes for the harness (meta, not research claims)

* Model-generated problem sheets lost a square root in the headline exponent. Read the primary source
  before decomposing. Cost here: about one hour of reading; saved: several mis-specified problems.
* Lean + Mathlib: the network policy in this environment blocks the Mathlib cache and the Lean release host.
  The toolchain installs from GitHub releases; the needed Mathlib closure builds from source on 2 cores in
  about 1.5 hours. Keep imports narrow.
* An independent referee pass caught a false claim (tensor route versus barrier) and a slack factor that,
  once removed, upgraded Theorem B. Reserve a separate critic for every article.
* Numerical rank experiments found a counterexample to "commutative is optimal" within minutes, and a cheap
  fooling-set argument then bounded what it could buy. Running cheap experiments before long proofs paid off.
