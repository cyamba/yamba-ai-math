# Audit of the two input sheets against the preprint

Inputs: [gemini-eth-consequences-program.pdf](sources/gemini-eth-consequences-program.pdf) ("Refuting the
Exponential Time Hypothesis", problems `YMB-ETH-01..07`) and
[gemini-eth-consequences-program-10.pdf](sources/gemini-eth-consequences-program-10.pdf) ("10 most influential
consequences", problems `YAMBA-378-01..06`). Both are model-generated summaries and are treated as data.
Comparator: the preprint and `lean/docs/378.md` in `openai/math` (inspected 2026-10-30).

| # | Sheet claim | Verdict | Correct statement |
| --- | --- | --- | --- |
| 1 | Time `2^{O(n (log log n)^2 / log n)}` (Lean) and `2^{O(n log log n / log n)}` (manuscript) | **Wrong exponent** | The denominator is `sqrt(log n)` in both places (preprint Theorem 1, Prop. 5.x, `378.md`). |
| 2 | Sparse case `2^{O(n / log n)}` | **Wrong** | `2^{O_{k,D}(n / sqrt(log n))}` for `m <= Dn`. |
| 3 | `Delta_{a,b}(k) = (-1)^a (-2)^{b+1} C(k-1, b)` for all `k` (YAMBA-378-01 part 2) | **Refuted** ([Lean: `pdf_defect_claim_false`](lean/EthProblems/ParityInterpolant.lean)) | Defect is the alternating sum `-(-2)^{b+1} sum_{m<k} (-1)^{m+1} C(m,b)` (Lean: `defect_telescope`). The single binomial is only the increment of the recurrence. |
| 4 | Planar problems move from `2^{Theta(sqrt V)}` to `2^{O(sqrt V / log V)}` | **Refuted as a consequence** | Nothing transfers: planar-to-SAT reductions give `N = Theta(V)` variables and the SAT bound `2^{O(N / sqrt(log N))}` is far worse than the known `2^{O(sqrt V)}` separator algorithms. Only the ETH-conditional *lower* bounds lose their justification. See [ETH-D07](D-complexity-consequences/ETH-D07-planar-lower-bounds.md). |
| 5 | Parameterized problems with `O(p)`-variable 3-SAT encodings run in `2^{O(p log log p / log p)}` | **Exponent wrong** | `2^{O(p log log p / sqrt(log p))} poly(n)` when the encoding has `O(p)` variables and `poly(n)` clauses. |
| 6 | "Problems linearly reducible to 3-SAT on `O(k)` variables now admit `2^{o(k)} n^{O(1)}` FPT algorithms", listing Vertex Cover | **Unverified as stated** | Vertex Cover needs a cardinality constraint; a direct CNF encoding costs `Theta(k log k)` or more auxiliary variables. A clean route is weighted counting on the `2k`-vertex kernel, see [ETH-C01](C-counting-extensions/ETH-C01-weighted-q-series.md) (proof sketch). |
| 7 | The paper proves `NC^1`, `TC^0` lower-bound progress | **Unsupported** | The preprint proves `E^NP` not in `SIZE(c n sqrt(log n))` infinitely often (Cor. 1.3) and `E^NP` not in `SIZE(O(n))`. Nothing about `NC^1` or `TC^0`. |
| 8 | Exact Ising/Potts partition functions on bounded-degree graphs in `2^{o(V)}` | **Plausible, not in the preprint** | The preprint states independent sets, `q`-colourings and perfect matchings (Cor. 1.2). Weighted factor products are sketched in [ETH-C04](C-counting-extensions/ETH-C04-graph-polynomials.md). |
| 9 | "SETH is unconditionally false as stated" | **Correct** | Preprint Sec. 1.1.1: refutes ETH, SETH, Gap-ETH, NSETH and their randomized forms. |
| 10 | `s_k = 0` for every fixed `k` | **Correct** (conditional on Theorem 1) | |
| 11 | Hidden constant `C_k` grows like `2^{O(k)}` | **Unverified** | The `k` dependence is not tracked in the preprint; the sparsification step alone gives `B = O_k((sigma^{-1} log(2/sigma))^{k-1})`. See [ETH-B05](B-exponent-frontier/ETH-B05-width-threshold.md). |
| 12 | Proof pipeline "partition clauses into `O(n/log n)` clusters of size `Theta(log n)`" | **Inaccurate** | The construction uses `r = Theta(sqrt(log n)/(log log n)^2)` variable groups, `Q = Theta(log n / log log n)` nodes, degree `R = Theta(sqrt(log n))`, and auxiliary dimension `D = r^{2Q} <= (2n)^{1/128}`. |
| 13 | YAMBA-378-05 says the proof invokes Minc's permanent expansion | **Inaccurate** | The preprint extracts Taylor coefficients by Boolean differences on fixed substitutions (Lemma 3.x, our ETH-A06). Minc's identity is an equivalent viewpoint only for permanents. |
| 14 | `Z_F(t)` at `t=1` equals `#SAT(F)`; Max-SAT histogram via interpolation in `u = 1 - t` | **Correct identity** | Lean: `prod_deform_eq_pow`, `deformed_sum_at_one`. Computing it fast for dense formulas is open ([ETH-C03](C-counting-extensions/ETH-C03-dense-exact-maxsat.md)). |
| 15 | Grover comparison | **Correct** for fixed `k` | Any `2^{o(n)}` classical bound beats `2^{n/2}` asymptotically. |
| 16 | `N = Theta(n log n)` reductions give no subexponential algorithm | **Correct in spirit; numbers change** | With `sqrt`: `2^{O(N / sqrt(log N))}` at `N = n log n` is `2^{O(n sqrt(log n))}`, worse than brute force. |

The structural reading of the sheets (category A lemmas, SymPy explorations, the `q`-series and Max-SAT ideas)
is useful and has been kept; each problem file records which parts were corrected.
