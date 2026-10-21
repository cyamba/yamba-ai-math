# Closing the partition-proof gaps

Created 2026-10-21. **Status: planned; no new mathematical gap is closed by this
document.** Baseline research revision:
`389e31456e5c6785380810f1d14736f6d59dd6c0`.

This is the original planning snapshot. Execution status, checked declarations,
and the still-open gates are recorded in the
[current gap ledger](evidence/gap-closure-results.md).

The objective is a complete, reproducible argument from the actual coloring
definition to nonnegative elementary coefficients, with a precise explanation
of which parts Lean checks. Completing or reproducing an existing theorem is
a useful result; a new solution or priority requires a separate literature
comparison. The [previous investigation record](evidence/completion.json)
remains the historical record and will not be rewritten as a success.

## Starting evidence

| Claim | Current assurance | Remaining obligation |
| --- | --- | --- |
| Simple corner slide works without a suffix condition | **Refuted** | Preserve the counterexamples as regression cases |
| Comparable-prefix bubbling gives valid tableaux, and preserves graph inversions | **Proved**, checked Lean statements | Lift to finite, complete, duplicate-free tableau families |
| Bubbling is injective in height at most two | **Proved**, checked Lean statement at a fixed split index | Relate the shape parameter to that index and construct the family map |
| Height-two elementary positivity and survivor interpretation | **Established** prior work; complete written argument here | Formal weighted counts, basis identities, and the coloring bridge |
| All-size cardinality obstruction to the original unrestricted injection | **Proved** by written argument | Optional separate Lean proof; does not replace the positivity bridge |
| General coefficientwise positivity in the September 2026 preprint | **Unverified here**, partially inspected claimed proof | Pinned rebuild, assumption audit, semantic audit, and comparison with its paper |

See [the independent review](evidence/reviewer.md),
[Lean assurance map](lean/README.md), and
[source-bound build record](lean/verification.json). Finite experiments are
regressions, not universal proof certificates.

## Exact targets

Let `h` be a weakly increasing Hessenberg vector on `1,...,n`, with
`i <= h(i) <= n`. Define `i <_P j` by `h(i) < j`. Its incomparability graph has
edges `i < j <= h(i)`. Height at most two means no strict three-element chain.
Use the article's English tableaux and its row-based graph inversion statistic.

For `0 <= k <= floor(n/2)`, let `T_k` be the actual P-tableaux of shape
`(2^k,1^(n-2k))`. Outside that range the family is empty. Let `B_k` map
`T_(k+1)` into `T_k` by the already-proved bubble operation, and let `S_k`
be the complement of its image in `T_k`.

The first target is the finite identity, for every natural inversion degree `d`:

```text
count(T_k, inv = d) = count(T_(k+1), inv = d) + count(S_k, inv = d).
```

This must use complete families of actual tableaux. No input list may merely
be assumed to enumerate all tableaux. Prove finiteness/completeness and
uniqueness, either with finite types or with a verified enumerator. Express
the primary identity using addition of natural counts. If a difference is
used, cast to integers or integer polynomials; truncated natural subtraction
must not conceal a negative coefficient.

The full height-two target is the following identity for **every** finite
color alphabet size `r`, using actual proper colorings:

```text
X_(h,r)(x;q) = sum_(k=0..floor(n/2)) W_(S_k)(q) * e_(n-k)(x) * e_k(x),
W_(S_k)(q) = sum_(U in S_k) q^(inv(U)).
```

Here `e_0 = 1`, and the empty graph has `X = 1`. When `n = 0`, its empty
tableau contributes one. Small alphabets may kill elementary factors, so
uniqueness of coefficients must not be inferred from one alphabet of size
`r < n`. Prove compatibility as alphabets grow, or use a faithful alphabet
with `r >= n` and a justified stable interpretation. This establishes the
intended symmetric-function statement rather than a chosen finite evaluation.

The general audit target is the corresponding positive elementary expansion
for all natural unit interval graphs, without the height restriction. An
external certificate, if verified, is attributed to its authors. It does not
make our height-two map new or make its missing semantic connections disappear.

## Milestones and acceptance gates

| ID | Work and dependency | Required evidence before closing |
| --- | --- | --- |
| M0 | Freeze statements, source versions, toolchains, and baseline | Source hashes, actual declaration signatures, documented conventions, and successful baseline checks |
| A1 | Inventory and attempt a pinned rebuild of the external general certificate; depends on M0 | Reproducible commands and logs, actual final declaration, complete reported axiom dependencies, and explicit build result or exact blocker |
| A2 | Audit the certificate's mathematical meaning and its decisive dependency chain; depends on A1's source inventory | Proper-coloring definition, arbitrary `n,h,r` quantifiers, correct q-statistic, actual elementary products, hypotheses and paper-to-Lean correspondence; all findings retain exact file/declaration references |
| H1 | Define complete finite tableau families and degree counts; depends on M0 | Finiteness or enumerator soundness/completeness, no duplicates, shape/filling equivalence, and the family-level bubble map |
| H2 | Prove degreewise survivor cancellation; depends on H1 | Checked family injection, weight restriction, image/complement partition, and the displayed natural-count equality for every degree |
| H3 | Prove the coloring-to-elementary identity; depends on H2 and a documented library-route decision | An unconditional checked theorem about actual coloring polynomials; all Schur or determinant dependencies are either proved or imported from an inspected, rebuilt certificate |
| R1 | Separate adversarial review and a clean reproduction; follows any proposed closed milestone | Independent role reviews exact theorem statements and assumptions; the intended final declaration rebuilds in an environment without stale local artifacts |
| W1 | Update article and repository evidence; depends on the relevant R1 verdict | Article matches checked scope; original counterexamples remain; existing LaTeX source compiles in its current editor; precise proof and novelty labels |

M0 leads to two workstreams: A1/A2 investigate the general certificate, while
H1/H2 extend our small combinatorial certificate. They can be scheduled
independently once their inputs are frozen. Their outputs meet at H3's
library-route decision. The first bounded increment covers M0, A1's build
feasibility and statement inventory, and H1/H2. It does **not** promise a full
audit of the general certificate or completion of H3.

## Audit of the claimed general proof

The inspected local upstream checkout was clean at revision
`adc7f1241b42e322a6451854ab7e4b4c146bf78a`. Its entry point is
`lean/OAI/Combinatorics/Chromatic/Main.lean`, declaring
`OAI.elementaryPositivityWitness`. Its model is in
`lean/OAI/Combinatorics/Chromatic/Model.lean`.
The model's `PermutationWitness.expansion` states an identity of actual
finite-color multivariate polynomials with coefficients in `Polynomial Nat`.
**This is a source inspection, not a verified certificate.**

An initial lexical inventory traversed 549 local files and 74,575 lines from
that entry point, with `Mathlib` as an external import. This is not a semantic
dependency count, an assurance level, or an estimate of how many lines require
independent review. Freeze and reproduce the inventory before relying on it.
The upstream toolchain is Lean 4.34.1; our certificate uses Lean 4.34.0. Keep
the projects separate until compatibility is demonstrated.

The audit sequence is:

1. Pin the upstream commit, mathlib revision, and relevant source hashes.
   Check the official upstream source and license before copying any material.
   The [primary preprint and source repository](https://github.com/openai/math/tree/main/preprints/Elementary-Positivity-of-Chromatic-Quasisymmetric-Functions-September-24-2026)
   supplies provenance, not automatic mathematical assurance.
2. Build only the relevant dependency closure in a disposable workspace.
   Inspect build configuration before execution. Avoid fetching unrelated
   theorem packages merely because the upstream monorepo lists them.
   Record any reduced build configuration and justify its equivalence for
   the selected theorem. Do not modify upstream proofs to force a success.
3. Print the final theorem type and its axiom dependencies. Inspect its actual
   graph, coloring, inversion, and elementary-polynomial definitions. Check
   for circular assumptions, hidden positivity hypotheses, proxy objects,
   proof placeholders, and unrecorded computational trust.
4. Trace the decisive expansion proof, particularly positive reordering,
   wall constructions, and the extraction of a global witness. Map paper
   claims to actual declarations. A clean build and a semantic audit answer
   different questions; retain both results.
5. Classify the outcome: **reproduced certificate with audited meaning**,
   **conditional/incomplete**, **build blocked**, or **refuted with a precise
   defect**. Failure to rebuild is not by itself a mathematical refutation.
   No source scan or model agreement can substitute for these checks.

An accepted general certificate could provide reusable coloring and basis
machinery, or establish the general theorem by attributed import. We must
still prove any claimed identification of its coefficients with our specific
survivor sets.

## Building the small certificate

Proposed module boundaries below are design targets, not existing checked
declarations. Prefer a small dependency surface over adopting the full
upstream development without need.

- `TableauFamilies`: finite actual tableaux, fixed shape, family-level map,
  soundness/completeness, and empty/balanced boundary cases.
- `WeightedCancellation`: a finite weight-preserving injection partitions
  the target into image and complement, degreewise. Instantiate it with
  `CornerSlide.bubble_tableau_injective` and
  `CornerSlide.bubble_tableau_graph_inversions`.
- `HeightTwoExpansion`: prove that no row has length three; establish the
  needed two-column identity
  `s_(2^j,1^(n-2j)) = e_(n-j)e_j - e_(n-j+1)e_(j-1)`, handle `j = 0`
  separately, and collect coefficients with the empty next-source convention.
- `ChromaticBridge`: prove or correctly reuse the exact coloring-to-tableau
  expansion. If the Shareshian–Wachs expansion is a hypothesis, label the
  resulting theorem **conditional**. It does not close H3.
- `HeightTwoMain`: combine these ingredients into the actual coloring
  identity above, without assuming the desired positivity, basis-change
  equation, or an unproved equivalence of proxy objects.

At H3 compare a restricted Schur-expansion route with a direct finite-coloring
route and with inspected reusable upstream lemmas. Record the dependency
burden and a working prototype before committing to a large new library.
Definitions of a formal Schur symbol or a polynomial named `chromatic` are
not sufficient; their equivalence to the intended mathematical objects is
part of the obligation.

## Tests that challenge the proof

Retain all existing exact tests and add only tests for new meaningful
behavior. Required adversarial cases include:

- `n = 0,1,2`, an empty source, and even balanced shapes;
- no edges, all edges, disconnected graphs, and small color alphabets;
- the connected slide failure `h = (3,4,4,5,5)`;
- the two distinct height-three sources with the same bubble image;
- all six sectors in the five-vertex total-order identity
  `4 - 5 - 6 + 5 + 4 - 2 = 0`, not only its first two terms;
- comparison with the independent proper-coloring oracle on every vector
  through five vertices, preserving q orientation and partition conventions.

The existing 33,474-source check is a baseline. Repeat or enlarge it when
changed code or a new concern warrants the cost. Enumeration never replaces
the universal theorem. Incorrect hypothesis weakening should be rejected by
the counterexamples, not hidden by a restricted test set.

## Review, resources, and stopping rules

Use one author and one separate critic for each bounded proof increment,
following the repository's `pair` fleet. The critic audits the conclusion
and its hypotheses, not just whether the file compiles. Distinct identities
may share model biases and are not statistically independent. A successful
dispatch does not establish a theorem. No worker has been dispatched by this
plan.

The [first-increment contract](../../programs/partition-gap-closure.json)
allows two proposal/review rounds, two role profiles, at most two workers,
and 16 declared dispatch cost units. Its planner schedule is author, critic,
author, repeated for round two. These are protocol bounds, not money or a
model-quality measurement. No automatic paid provider calls are part of the
plan. The user can retain GPT-6.1 Sol with Max effort; no comparative
performance or optimality claim is made for that choice.

For the initial external build audit, cap cumulative build-process wall time
at 60 minutes and downloaded dependency/build storage at 15 GiB. Check disk
space first. Permit one clean attempt and at most one diagnosed retry within
those limits; report a blocker or revise the next increment if the limit is
reached. Sample progress frequently enough to keep the chat responsive.
Record actual elapsed time, dependencies, retries, disk use, and available
usage measurements. Unknown token or monetary costs remain `unknown`.
These are ceilings, not forecasts or instructions to run background jobs.

After two unsuccessful mathematical revisions, preserve the exact failed
obligation and propose a narrower next increment. Never weaken the final
theorem silently or replace the coloring identity with a tautological
definition. The full project is complete only when all required proof gates
and their semantic review pass; a bounded increment may end unresolved.

Baseline and final verification use the repository tests and checker, pinned
Lean builds, direct checking of each final theorem and its axiom list, and
hash-bound reports. The allowed foundational dependencies must be explicit;
our current certificate uses only `propext`, `Quot.sound`, and
`Classical.choice`. Any additional trusted mechanism requires explanation,
not an undisclosed relaxation. Keep large logs and build products in ignored
`.runs/` or `.lake/`; intentionally publish compact evidence with hashes.

## Publication gate and next action

Maintain a gap ledger recording statement, assumptions, source/declaration,
status, reviewer verdict, and evidence path. Close a row only after its
acceptance gate passes. Update the existing `paper/main.tex` in place when
proof content changes and use the built-in compiler; preserve the user's
current editor and PDF preview. A planning document is not a reason to
rewrite the article's mathematical claims.

Before integrating execution results, check the remote state of PR #1 and
base any follow-up contribution on the actual main revision. Do not assume
that a proposed merge has occurred. Review staged files and keep historical
input evidence intact.

**Immediate execution target:** M0 plus a family-level, degreewise survivor
cancellation theorem (H1/H2), accompanied by an A1 feasibility report. This
delivers a precisely bounded improvement even if the general proof audit
turns out to require a longer investigation.
