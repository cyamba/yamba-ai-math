# RR003: naive union of partial maps is refuted

**Refuted proposal; exact algebraic obstruction.** This compares the two
existing mechanisms, rather than introducing a third bridge or review round.
Both partial maps have explicit inverses on their own images. That does not
make their assignments compatible or their union a bijection.

At weight four, their values are exchanged:

| Residue input | Core/column composition A | Recursive repair B |
| --- | --- | --- |
| (1,3) | (1,3) | (4) |
| (1,1,1,1) | (4) | (1,3) |

Thus they are not restrictions of one fixed map on their common source
domain. A complete construction may replace these assignments, but cannot
claim to preserve both literally.

The seemingly practical fallback “use A when it supports the input,
otherwise B” is actually noninjective. A sends residue (1,8) to gap (3,6).
Residue (3,6) is unsupported by A, while B's classical branch sends it to
that same gap (3,6). These are distinct weight-nine sources. Direct algebra:
A's intermediate C is (2,0,(2,3),()), with U=(8,1); B's input is already
three-divisible and is unchanged by ternary Glaisher. All objects satisfy
their actual predicates. This collision alone disproves the fallback.

The metered exploratory search partial-overlay-obstruction found its first
fallback collision at weight nine; the whole <=30 region was previously
exposed, so this is discovery, not held-out evaluation. No final algorithm
uses this search or its image table. The exact witness is retained in
verification-summary.json; raw receipt remains ignored in .runs/rr003.

Decisive obligation: compatibility and disjoint target coverage when joining
partial maps. Actually refuted: unconditional union and this particular
A-first fallback. Neither full mechanism is proved impossible. The justified
next step is a coherent global decomposition that may revise old assignments,
with both inverse identities proved on its whole domain. Simply adding more
restricted image counts would not meet that obligation.

Workflow hypothesis, **unvalidated**: cross-checking exact overlaps between
partial constructions can prevent false coverage gains from being mistaken
for a complete bijection. No broader harness gain was measured.
