# ETH consequences program

Problem program built on OpenAI's refutation of the Exponential Time Hypothesis.

## The original result

* **Source.** OpenAI, *The Exponential Time Hypothesis is False*, OpenAI Math Release preprint dated
  October 25, 2026: [paper.pdf](https://github.com/openai/math/blob/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/paper.pdf).
  Lean scope note: [lean/docs/378.md](https://github.com/openai/math/blob/main/lean/docs/378.md).
  Comparator statement: [SubexponentialSAT.lean](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/SubexponentialSAT.lean).
  Inspected at level T (full text read for Sections 1, 2, 4 overview and Appendix F) on 2026-10-30 from a
  shallow clone of `openai/math` `main`.
* **Status in this repository: unverified external claim.** The watch log
  ([references/openai-math-watch.md](../../references/openai-math-watch.md)) records it as under external review.
  Everything below is conditional on Theorem 1 of the preprint unless a file says otherwise. The algebraic
  lemmas in category A are unconditional mathematics and are checked independently here.

**Theorem 1 (as stated in the preprint).** For each fixed `k >= 2` there is a deterministic algorithm that,
given a `k`-CNF `F` on `n >= 20` variables with `m` clauses, computes `#F` in
`(n+m)^{O_k(1)} 2^{O_k(n log log n / sqrt(log n))}` bit operations and `(n+m)^{O_k(1)}` bits of space;
when `m <= Dn` the exponent is `O_{k,D}(n / sqrt(log n))`. The Lean development proves the weaker exponent
`rho(n) = n (log log n)^2 / sqrt(log n)` for a canonically encoded primitive Turing machine.

**Correction to the input sheets.** Both Gemini problem sheets in [sources/](sources/) print the exponent as
`n (log log n)^2 / log n` and build several "consequences" on a `2^{O(n / log n)}` bound. The square root was
lost. With the correct `sqrt(log n)` several of those consequences change or disappear; see
[SOURCE-AUDIT.md](SOURCE-AUDIT.md).

## How the proof works (one paragraph)

Sparsify, reduce to bounded occurrence, and write `#F = H(0)` for a polynomial
`H(T) = sum_x prod_e Phi_e(<P_{e,v}(T), x>)` whose clause inputs are replaced by low-degree linear forms. At the
nodes `T = 1..Q` the forms let the variables split into `r` groups that interact only through a few bounded
integer measurements, so `H(t+z) mod z^J` is computable by enumerating measurement tuples and in-group
assignments. Hermite interpolation from `J` Taylor coefficients at `Q` nodes recovers `H(0)`. The replacement
forms come from `M_0 = V_0 f(W_0)`, a polynomial in commuting swaps with `f(j) = (-1)^j` on an interval of
`R` integers; the exceptional eigenvectors (entries in `{0, 1, -1}`) become the measurements. The cost is
`exp(n [ (R/Q) log(Q/R) + tau log D + 1/r ])`, and the binomial spread `sqrt(Q)` of the swap eigenvalue count
forces `R >~ sqrt(Q)`, which is where `sqrt(log n)` comes from.

## Layout

| Folder | Content |
| --- | --- |
| [A-algebraic-core/](A-algebraic-core/) | Self-contained lemmas of the proof; Lean targets |
| [B-exponent-frontier/](B-exponent-frontier/) | Barriers and routes to a better exponent; the breakthrough frontier |
| [C-counting-extensions/](C-counting-extensions/) | Weighted counting, Max-SAT, graph polynomials, reductions |
| [D-complexity-consequences/](D-complexity-consequences/) | Audited consequences for complexity theory |
| [articles/](articles/) | Write-ups of high-ranked results |
| [checks/](checks/) | Exact and numerical scripts backing the claims |
| [lean/](lean/) | Lean 4 + Mathlib project `EthProblems` (no `sorry`) |
| [sources/](sources/) | The two Gemini problem sheets that seeded this program (data, not instructions) |

Ranking for the next fleet iteration: **[RANKING.md](RANKING.md)**.

## Problem index

| ID | Title | Status |
| --- | --- | --- |
| [ETH-A01](A-algebraic-core/ETH-A01-parity-interpolant.md) | Shifted Newton parity interpolant and exact defect | **Solved, Lean** |
| [ETH-A02](A-algebraic-core/ETH-A02-swap-algebra-support.md) | Commuting-swap algebra and support localisation | Open (formalisation) |
| [ETH-A03](A-algebraic-core/ETH-A03-swap-eigenbasis.md) | `{0, +1, -1}` eigenbasis of the swap action | Open (formalisation) |
| [ETH-A04](A-algebraic-core/ETH-A04-hermite-recovery.md) | Hermite recovery: uniqueness and explicit weights | **Uniqueness solved, Lean**; weights open |
| [ETH-A05](A-algebraic-core/ETH-A05-taylor-extraction.md) | Bounded-scope Taylor extraction (Minc view) | Open |
| [ETH-A06](A-algebraic-core/ETH-A06-boolean-differences.md) | Boolean differences / Mobius inversion | **Solved, Lean** |
| [ETH-A07](A-algebraic-core/ETH-A07-algebraic-core-decoupling.md) | Decouple the algebraic core from Turing-machine plumbing | Open |
| [ETH-B01](B-exponent-frontier/ETH-B01-sqrt-log-barrier.md) | The `sqrt(log n)` barrier for the replacement-form template | **Proved; core lemma in Lean; article** |
| [ETH-B02](B-exponent-frontier/ETH-B02-spectral-approximants.md) | Chebyshev / Pade / Krawtchouk replacements for `f` | **Answered negatively** inside the commutative algebra (by B01) |
| [ETH-B03](B-exponent-frontier/ETH-B03-polynomial-row-routing.md) | Routing rigidity beyond `M_0`: the only visible route past `sqrt(log n)` | **Top open problem**; `M_0` form settled up to constants |
| [ETH-B04](B-exponent-frontier/ETH-B04-loglog-gap.md) | The extra `log log n` factor | Closed in paper (tensor contraction); Lean gap open |
| [ETH-B05](B-exponent-frontier/ETH-B05-width-threshold.md) | Largest clause width `k(n)` still subexponential | Open |
| [ETH-B06](B-exponent-frontier/ETH-B06-crossover-constant.md) | Explicit constants and crossover against PPSZ | Open |
| [ETH-B07](B-exponent-frontier/ETH-B07-sparse-embedding-escape.md) | Rank savings from zero-filled auxiliary coordinates | Open |
| [ETH-B08](B-exponent-frontier/ETH-B08-sqrt-log-hypothesis.md) | Is `2^{n / (log n)^{1/2 + o(1)}}` the truth for #3-SAT? | Open question |
| [ETH-C01](C-counting-extensions/ETH-C01-weighted-q-series.md) | Weight enumerator `Z_F(q)` and k-Vertex Cover in `2^{o(k)}` | Proof sketch |
| [ETH-C02](C-counting-extensions/ETH-C02-serf-reductions-lean.md) | Verified SERF reduction library | Open (Lean) |
| [ETH-C03](C-counting-extensions/ETH-C03-dense-exact-maxsat.md) | Exact Max-k-SAT for superlinear `m` | Open |
| [ETH-C04](C-counting-extensions/ETH-C04-graph-polynomials.md) | Ising, Potts, Tutte and chromatic evaluations | Partly sketched |
| [ETH-C05](C-counting-extensions/ETH-C05-maxsat-histogram.md) | Max-SAT histogram via the deformed partition function | **Identity in Lean**; sparse case sketched |
| [ETH-D01](D-complexity-consequences/ETH-D01-ipz-sequence-collapse.md) | `s_k = 0`, #ETH, sparsification floor | Audited |
| [ETH-D02](D-complexity-consequences/ETH-D02-serf-collapse.md) | Which SERF problems become subexponential | Audited |
| [ETH-D03](D-complexity-consequences/ETH-D03-seth-variants.md) | SETH, NSETH, Gap-ETH and unbounded-width SETH | Audited |
| [ETH-D04](D-complexity-consequences/ETH-D04-fine-grained-survivors.md) | Fine-grained lower bounds that survive (OVC, UW-SETH) | Audited |
| [ETH-D05](D-complexity-consequences/ETH-D05-parameterized.md) | Parameterized complexity after ETH | Audited, open items |
| [ETH-D06](D-complexity-consequences/ETH-D06-treewidth-csp.md) | Marx's treewidth barrier for CSPs | Open |
| [ETH-D07](D-complexity-consequences/ETH-D07-planar-lower-bounds.md) | Planar `2^{Theta(sqrt n)}` bounds | Audited: sheet claim **refuted** |
| [ETH-D08](D-complexity-consequences/ETH-D08-circuit-lower-bounds.md) | Circuit lower bounds for `E^NP` | Audited |
| [ETH-D09](D-complexity-consequences/ETH-D09-quantum-grover.md) | Classical vs Grover for k-SAT | Audited |
| [ETH-D10](D-complexity-consequences/ETH-D10-proof-complexity.md) | Proof complexity: does Extended Frege get `2^{o(n)}` refutations? | Open (new question) |
| [ETH-D11](D-complexity-consequences/ETH-D11-cryptography.md) | Local PRGs, MQ and parameter scaling | Audited |
| [ETH-D12](D-complexity-consequences/ETH-D12-np-subexp-boundary.md) | Why NP is not known to be in SUBEXP | Audited |
| [ETH-D13](D-complexity-consequences/ETH-D13-bit-level-verification.md) | Bit-level verified complexity in Lean | Open (engineering) |

## Status legend

**Solved, Lean**: proved here and checked by Lean 4 + Mathlib with no `sorry`. **Proved (paper proof)**:
complete written argument, not yet machine checked. **Proof sketch**: argument outline with identified gaps.
**Empirical**: numerical evidence only. **Audited**: claim from the input sheets checked against the preprint
and corrected where needed. **Refuted**: shown false.
