# Three-dimensional Ferrers clue

This note responds to Christopher's 24 October suggestion during the active
paper revision. It separates an already reviewed representation from an
unproved proposed mechanism. It introduces no fourth frozen finite variant
and no finite execution.

For a U object, write its nonincreasing decoded heights as h_i=5q_i+r_i,
0<=r_i<5. The reviewed three sheets have row lengths

`P_t(h)=3q+clamp(r-t,0,3), t=0,1,2`.

They satisfy P_0>=P_1>=P_2 and are nonincreasing in i. Consequently the
same representation is a genuine finite Ferrers order ideal in three
coordinates:

`S={(i,j,t+1): 1<=j<=P_t(h_i), t=0,1,2}`.

Its volume is exactly the U weight, since the five residual volumes are
0,1,3,6,8. This is a reformulation of the already reviewed lossless sheet
encoding, not an additional full correspondence. Retaining every cube
retains h and all U data. Retaining just sheet areas does not: U=(8,3,1)
and U=(6,6) both have sheet areas(6,4,2). Earlier RR006 shadow and axis
transpose failures remain failures; a coordinate permutation need not
preserve this special cross-section language and the terminal gap bound.

The useful new question concerns a periodic boundary and a reversible
slice rule, rather than volume alone. The exact source grammar has three
phases, height offsets(0,2,3), and cyclic increments(2,1,2). A candidate
cylindric interpretation must realize those phases intrinsically and
explain how the two C rigging vectors appear after slicing. Merely adding
a phase label or counting diagonal cubes does not meet that obligation.
In particular the already reviewed Durfee-count obstruction still applies
to its stated small statistic; it does not rule out a full 3D boundary.

The smallest useful mathematical deliverable would be an explicit class
of such solids, a canonical cut, and a volume-preserving local move with
an intrinsic inverse. Its image must satisfy the literal U terminal bound,
and the cut must recover a,b,mu,nu without saved history. For an extension
of A3 it must also avoid A3's occupied images. The raw b=1 cycle's weight27
collision shows why internal reversibility alone is insufficient.

Two additional search strings were used (now10/12 queries,18/18 opens).
Only search-result abstracts were available within the remaining source
boundary. Corteel's [2017 paper](https://www.ams.org/journals/proc/2017-145-05/S0002-9939-2016-13373-X/)
describes a proof of the second classical Rogers--Ramanujan identity via
cylindric plane partitions and RSK. Kanade and Russell's
[Tight cylindric partitions](https://arxiv.org/abs/2508.15113) advertises
functional equations and a colored-partition connection. These are
primary-source analogy leads, not inspected constructions, an identified
KR1 equivalence, or evidence of novelty. Raw search output is retained
locally in `.runs/rr007/ferrers-search.json`. No source open was added.

The mathematical author is assessing this boundary/slicing direction in
the existing revision stage. Any new mechanism remains author-only until
the final distinct critic reports.

Correction during final criticism: this note initially wrote `r-t+1`
while using zero-based t. That expression incorrectly gives residual
volume3 at h=1. The displayed expression above is corrected to `r-t`;
equivalently the author's R5 uses `r-t+1` with one-based t=1,2,3.
This notation error was in root's explanatory note, not the pinned
author construction. The correction and critic finding are retained.
