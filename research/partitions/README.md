# Partition positivity: a proof attempt with checked boundaries

**Status: the full problem is unresolved in this project.** We selected Problem
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

- [Illustrated article](paper/main.tex): definitions, explicit counterexamples,
  the all-size obstruction, complete height-two argument, three vector figures,
  verification counts, and remaining general proof obligations. It compiles in
  the Codex LaTeX editor and remains open there with its PDF preview. No separate
  PDF was exported, following the user's editor instruction. Visual layout was
  not independently inspected because the available computer tool cannot access
  Codex; compiler success alone is the recorded check.
- [Lean source](lean/CornerSlide.lean) and [formalization guide](lean/README.md):
  actual bijective fillings, all row and column conditions, the exact local
  boundary criterion, general bubble validity, height-two injectivity, the
  row/word inversion equivalence, actual weight preservation, and explicit
  failures without the hypotheses. Lean 4.34.0, `Std` only.
- The Schur expansion and determinant-to-elementary coefficient bridge remain
  outside the Lean development. The general positivity theorem is not proved
  here, and the all-size cardinality obstruction has a written proof rather
  than a Lean proof.

## Reproduce the evidence

From the repository root:

```sh
python3 -m unittest discover -s tests -v
python3 scripts/check_repository.py
python3 research/partitions/checks/tableaux.py --max-n 6
python3 research/partitions/checks/verify.py --max-n 5 --bubble-max-n 7
```

In `research/partitions/lean`, with the pinned Lean toolchain available:

```sh
lake build
lake env lean CornerSlide.lean
```

The independent coloring/subset-expansion oracle agrees with the tableau/DJT
calculation on all **65** Hessenberg vectors through five vertices. All
**33,474** height-two bubble sources through seven vertices have valid,
distinct images, unchanged inversion degree, and exact inverse recovery.
These finite exact computations test code and expose counterexamples;
they do not prove a universal theorem. The universal combinatorial statements
have separate Lean proofs and explicit mathematical assumptions.

## Evidence and remaining objective

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
