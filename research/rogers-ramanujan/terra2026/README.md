# Positive cut-word models for KR1

**Research status: partial progress. The full structural KR1 bijection has not been obtained.**

The main result is a general positive normal form for paired-node divided differences. It supplies explicit positive objects for every auxiliary index in Xia's A, B, C sequences. It does not yet give the invertible recurrence branch maps needed to turn those objects into all KR1 gap partitions. Novelty relative to the literature is unverified.

## Read first

- `kr1-positive-models.pdf`: illustrated twelve-page article.
- `kr1-positive-models.tex`: complete LaTeX source; all figures are native TikZ/PGFPlots.
- `theory/general_positive_divided_differences.md`: general theorem and proof.
- `theory/all_n_positive_staircase.md`: KR1 application.
- `failure-ledger.md`: exact failed schemes, working constructions, and live variations.
- `final-math-review.md`: independent manuscript review with source hashes.
- `formal/verification-scope.json`: precise scope of each Lean module.
- `verification/verification.json`: fresh execution receipt, source hashes, and log references.
- `contract.md`: objective, baseline, fleet execution, and assurance limits.

Christopher Yamba supplied research direction, mathematical ideas, and intuition. GPT-6.1 Terra mathematical agents developed constructions and performed reviews using the yamba-ai-math research harness and its role guidance. The coordinating session used GPT-6 Astra Pro and coordinated the work; it is not represented as Terra. The collaboration used manual agent dispatch, not a command-adapter inference run. These credits do not attribute every proof to Christopher. Token and monetary usage were not measured.

## Main theorem

For positive d,c, distinct paired nodes z_i=q^r_i+q^(c-r_i), 0<r_i<c, and 0 <= m <= n, let

    Phi(z) = product_{j>=0} (1-z q^(dj)+q^(c+2dj))^(-1).

Then (q^d;q^d)_m Phi[z_0,...,z_n] is the generating series of explicitly described colored words with n cut separators, with the last m staircase coordinates zero. Flattening and decoding are inverse operations. The sign cancellation selects the least eligible marker/coordinate pair. It works for every n, not just the finite indices used in computations.

The written proof covers the divided-difference interpretation, canonical sorting, staircase coordinates, local finiteness, and specialization. Lean checks the generic arbitrary-list involution and selected related lemmas. The entire formal power-series theorem is not formalized in this supplement.

## Reproduce the certificates and exact checks

Requirements: Python 3.11+ and the official Lean 4.34.0 binary distribution. The Lean modules use `import Std`; they do not need a separate mathlib checkout. The runner does not download dependencies.

From this directory:

```sh
python3 verify.py --lean /absolute/path/to/lean
```

This runs all four Lean modules, then the retained local surgery, staircase, lane, height-block, cyclic-recurrence and coefficient regressions. It writes a new `verification-local/` directory and leaves the original `verification/` receipt untouched.

Options:

```sh
python3 verify.py --only python
python3 verify.py --only lean --lean /absolute/path/to/lean
python3 verify.py --full --lean /absolute/path/to/lean
```

`--full` additionally repeats the independent 3,178,008-state cut-word check. That check was run earlier in the research session; it was not needlessly repeated during packaging. Its earlier result and separate implementation remain in `construction/alln_word_review.md` and `construction/check_alln_word.py`. All computations use exact integer arithmetic.

The default coefficient audit compares A_n and C_n for n=0,...,8 through weight 45, except A_1 through weight 30: 18 comparisons and 813 coefficients. A_0 is implemented as its separately defined product. These are finite transcription checks, not a construction of the missing bijection.

## Build the article

The source requires a standard TeX Live installation with amsmath, mathrsfs, microtype, TikZ, PGFPlots, fancyhdr, and hyperref:

```sh
pdflatex -interaction=nonstopmode -halt-on-error kr1-positive-models.tex
pdflatex -interaction=nonstopmode -halt-on-error kr1-positive-models.tex
```

No external image downloads are needed.

## Formal boundaries

The four modules contain 36 theorem declarations and 26 explicit axiom reports. Fresh Lean execution succeeded. There are no `sorry` or `admit` tokens or added axiom declarations in these modules, and no reported result depends on `sorryAx`. Standard Lean foundational axioms are reported in the logs. Unused-variable and unused-simp linter warnings remain visible.

- `Cancellation.lean`: least-eligible involution, weight, sign parity, fixed points.
- `Blocks.lean`: seven-state multiplicities and compatible-sequence facts.
- `Entropy.lean`: integer witness and path bound for every power.
- `MergeBounds.lean`: cluster-boundary identities and selection inequalities.

The cut-word flattening, formal-series interpretation, logarithmic counting argument, and complete cluster merge are written arguments with separate reviews. They are not silently attributed to Lean. No module asserts a full KR1 bijection.

## Supplement layout and historical context

In the downloadable archive, this directory is `kr1-research/research/rogers-ramanujan/terra2026/`. The adjacent `../checks/kr1.py` is an unchanged baseline dependency used by the lane and height-block tests. `../checks/rr003_cluster_merge.py` and `../rr003/endpoint-cluster-merge.md` preserve the older endpoint. The endpoint's original comments predate the new review in this directory. The archive also includes the frozen endpoint verifier, the new program specification, selected historical obstruction proofs, and the exact repository baseline inventory. Its directory structure preserves the original verifier's relative paths.

Repository baseline: `4ccc4fe60008e52c9846e9a63d4bf98d23108702` on `research/argon-tableau-continuation`. The earlier weight-41 collision and fixed-alphabet obstruction are not overwritten or treated as repaired.

## Next mathematical obligation

Construct a total, weight-preserving, invertible object map realizing

    C_n <-> A_(n+1)
            + q^(3n+3) C_(n+1)
            + q^(6n+6) C_(n+1)
            + q^(6n+8) A_(n+2).

Then realize the remaining state relations, prove inverse branch recognition, and prove termination. Even this first row sometimes has to change particle count: the n=0, weight-8 example in the article rules out every construction that only transports a fixed particle inventory. The weight-37 cyclic failure has a branch-dependent repair for that one input, not a general algorithm.
