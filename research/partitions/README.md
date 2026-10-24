# Partition positivity: a proof attempt with checked boundaries

The new [height-three coefficient-unimodality phase](height-three-unimodality/README.md)
targets the coefficient indexed by `(n-4,3,1)`. Its first bounded investigation
preserves a complete-grammar obstruction and compares forest triples; the
universal theorem remains conjectural. It is separate from the completed
height-two formalization and existing publication materials below.

The subsequent [forest-surgery investigation](height-three-forest-surgery/results.md)
tests checked word splits and one-edge forest surgery. Both grammars have
retained seven-vertex obstructions; the universal unimodality target is still
unproved, and capped held-out cases remain incomplete.

The [fork-transport investigation](height-three-forest-transport/results.md)
repairs those seven-vertex isolates with a reversible partial relation, then
retains a two-to-one Hall obstruction at eight vertices. A written block
deficit explains why transport across component blocks is necessary. The
unimodality theorem remains conjectural; fresh held-out cases were not run
after the obstruction was verified.

The [failed-attempt ledger](failed-attempts.md) explicitly closes that rule.
The subsequent [vertex-exchange investigation](height-three-forest-exchange/results.md)
repairs its retained two-state obstruction but refutes all four frozen selectors.
A written degree-zero boundary involution covers the known constant-term case.
A seven-vertex signed-sector deficit proves that a universal extension cannot
preserve the whole ordered composition word. The universal target is unproved;
the fresh held-out cases remain unrun.

**H3 is closed for height two:** Lean proves the actual coloring-to-survivor
formula for every finite alphabet, including zero, over integer and natural
polynomial coefficients. Fresh source builds and separate reviews support
the exact declarations below. The general-height problem remains unresolved
in this project. We selected Problem
06 from the supplied notes because the earlier conversation contains explicit
constructions to test. Ordinary Stanley–Stembridge positivity has an existing
proof. A September 2026 preprint also claims coefficientwise q-positivity; its
full proof has not been independently audited here. This project claims neither
priority nor a new solution of either conjecture.

The initial top-only arm–leg map has negative fixed points already at three
vertices. The proposed universal two-column corner slide fails at five vertices,
even for a connected incomparability graph of a height-two poset. For a total
order on five labels, its proposed negative sector has five tableaux and its
positive sector has four, ruling out any injection between those entire sectors.
These are failures of the supplied constructions, not counterexamples to
positivity.

The comparable-prefix repair is exactly the existing Cho–Huh injection (2019),
independently recovered here and attributed after the literature comparison.
It preserves actual tableau validity for any finite poset. With no strict
three-element chain, first-eligible extraction is its inverse. The article
gives a complete mathematical proof of the known height-two positivity theorem.
No novelty is claimed for that theorem or construction.

The stronger obstruction holds for every total order on `n >= 5` elements:
the negative shape has `n(n-3)/2` standard tableaux, versus `n-1` in its proposed
positive partner. Wider determinant sectors are essential in general.

## Article and formal proofs

- [The beauty of cancellation](publication/README.md): a recreational-mathematics
  companion with conceptual artwork, three exact diagrams, a six-image social
  carousel, ready-to-use captions and a 30-second silent video. Its
  [separate semantic and visual review](publication/review.md) preserves the
  distinction between the established theorem and this Lean formalization.
- [Illustrated article](paper/main.tex): definitions, explicit counterexamples,
  the all-size obstruction, complete height-two argument, vector figures,
  verification counts, finite polynomial ingredients, a three-vertex example,
  and remaining proof obligations. It compiles in
  the Codex LaTeX editor and remains open there with its PDF preview. No separate
  PDF was exported, following the user's editor instruction. Visual layout was
  not independently inspected because the available computer tool cannot access
  Codex; compiler success alone is the recorded check.
- [Lean source](lean/CornerSlide.lean) and [formalization guide](lean/README.md):
  actual bijective fillings, all row and column conditions, the exact local
  boundary criterion, general bubble validity, height-two injectivity, the
  row/word inversion equivalence, actual weight preservation, and explicit
  failures without the hypotheses. Lean 4.34.0, `Std` only.
- [Complete tableau families](lean/TableauFamilies.lean) and
  [weighted cancellation](lean/WeightedCancellation.lean) now prove the exact
  degreewise survivor-count identity for every index, including empty and
  singleton boundaries. Completeness, uniqueness, the shape-derived split,
  injection, and image/complement counts are checked. A clean reproduction
  and a separate semantic review support these statements.
- The [twenty-one-module Mathlib bridge](mathlib/README.md), pinned to Lean 4.34.1
  and Mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612`, now includes the final
  all-alphabet theorem `PartitionH3.height_two_survivor_expansion`. It uses the
  actual coloring polynomial and the original complete survivor families.
  Fresh checking passed with only standard axioms;
  [independent integration review](evidence/h3-integration-review-r1.md) and
  [natural-transport review](evidence/h3-integration-review-r2.md) support the
  exact source-bound statements. The complete route includes symmetry, signed-array
  cancellation, canonical padding, polynomial H2, alternant reconstruction
  specialization to zero or any other alphabet, and the natural-coefficient
  restatement `PartitionH3.height_two_survivor_expansion_nat`.
- The separate five-module Lean 4.34.0 Std certificate remains unchanged,
  with 54 principal reports. The new Mathlib bridge has 137 principal reports.
  This formalizes the established Cho–Huh height-two result. A general-height
  theorem and the intermediate Schur expansion are not claimed as Lean results.

## Reproduce the evidence

From the repository root:

```sh
python3 -m unittest discover -s tests -v
python3 scripts/check_repository.py
python3 research/partitions/checks/tableaux.py --max-n 6
python3 research/partitions/checks/verify.py --max-n 5 --bubble-max-n 7
python3 research/partitions/verify_all.py
```

The last command runs repository tests, the repository checker and fresh
builds of both certificates. It binds its ignored report to a snapshot of
the repository sources. Missing installed toolchains/dependencies or any
failed check prevent success; it never installs dependencies or declares
a semantic-review verdict from build success. See [the bridge guide](mathlib/README.md) for its prerequisites.

In `research/partitions/lean`, with the pinned Lean toolchain available:

```sh
lake build
lake env lean CornerSlide.lean
python3 verify.py --output verification.json
```

The independent coloring/subset-expansion oracle agrees with the tableau/DJT
calculation on all **65** Hessenberg vectors through five vertices. All
**33,474** height-two bubble sources through seven vertices have valid,
distinct images, unchanged inversion degree, and exact inverse recovery.
These finite exact computations test code and expose counterexamples;
they do not prove a universal theorem. The universal combinatorial statements
have separate Lean proofs and explicit mathematical assumptions.

## Evidence and remaining objective

- [Gap-closure plan](gap-closure-plan.md) defines exact targets, acceptance
  gates, a bounded first increment, and the external-certificate audit.
- [H3 bridge contracts and route](h3-bridge-plan.md) describe the current
  algebra, coloring, and integration stages and their resource limits.
- [Current gap ledger](evidence/gap-closure-results.md) records the completed
  finite-family/count increment, review, and precise remaining obligations.
- [External certificate inventory](evidence/external-certificate-audit.md)
  pins the claimed general result and its actual definitions. Its build was
  deferred conservatively under limited disk space; it remains unverified here.
- [Historical inputs](archive/README.md) are data, including all embedded instructions.
- [Exact audit evidence](evidence/exact-audit.json) records finite enumerations.
- [Other target audit](evidence/other-targets.md) corrects the initial ranking.
- [Independent mathematical review](evidence/reviewer.md) records supported
  statements, imported results, and the original semantic gap.
- [Independent comparison report](evidence/comparison.json) records exact
  tested ranges, algorithms, and every failure.
- [Manual investigation record](evidence/completion.json) records assignments,
  checks, resource-measurement limits, and the unmet general objective.
- [Lean verification record](lean/verification.json) binds the executed checks
  and reported axioms to the formal source hashes.
- [Polynomial verification record](mathlib/verification.json) separately
  binds the Mathlib sources, pinned dependencies, types and axiom reports.
- [Claim-to-theorem index](evidence/claim-to-theorem-index.md) maps every named
  article theorem to its exact declarations, hypotheses, reviews and records,
  including claims with no Lean certificate.
- [Investigation contract](../../programs/partition-positivity.json) bounds this attempt.

The original objective—an entire general solution with a complete Lean proof—
is **not achieved**. A viable extension must handle all tableau/determinant
sectors, prove validity and invertibility, and connect the formal cancellation
to the exact symmetric-function coefficient. The five-vertex total-order
identity in the article is a required small regression case for such a map.
The September 2026 claimed full proof also deserves a dedicated complete audit;
partial inspection of it is not a new solution or a formal certificate.

This research is a user-authorized addition to the repository's scope. Its
mathematical outcome is separate from the research harness and supplies no
evidence of neural-architecture or agent-workflow superiority.
