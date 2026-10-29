# Frozen B1, 2026-10-24 about21:01 UTC

Exact rules and proof: `../author.md`, theorem candidate B1. This freeze
concerns the complete U <-> F2 carrier only; it makes no C or A parser claim.
Five primary colors, their energy, secondary parity, literal grading,
terminal convention, both maps and intrinsic full images are fixed there.

Forward: append the primary terminal0g; then append one extra0g for odd
primary length, two for even length; pair from the left. Inverse: unfold,
trim all trailing0g to one, and decode the nonterminal primaries.
Termination is by finite scans. Weight is the sum of9k+alpha_r on primary
parts and9n+alpha_i+alpha_j on secondary parts; no alternate grading.

Smallest falsifiers: empty is the first terminal/parity case; one column1
tests odd/even padding; U=(1,1) tests repetition and fusion into one
secondary11. Any F2 with two or three trailing primary-ground zeros tests
the inverse's intrinsic padding recovery. Both generator domains must be
independently literal and all actual inputs and outputs must have weight
at most12. Compare literal image sets in addition to both round trips.

Implementation: `.runs/rr007/b1-degree-two-lift.py`, pilot argument12 only.
No extension above12 is authorized. The exact symbolic R2 partwise
uncoloring failures of weight4/5 will be checked as transcription checks,
not as a claim of a C map or a fourth candidate.
