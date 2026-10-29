# Separate RR007 review of the RR003 U/B endpoint

Reviewer: distinct Fleet B critic, 24 October 2026. **Verdict: supported.**
The statement below is **proved with separately reviewed ordinary written
argument**, together with the bounded implementation check specified below.
There is no formal certificate. This review does not independently recheck
the Andrews–Keith/Stockhofe attribution against its primary source: the
RR007 source-open allowance was exhausted by the required Konan inspection.
It does check the explicit algorithms, rather than import a source theorem.

## Exact statement

Let H be a finite descending sequence of positive integer heights with every
successive drop, including its drop to zero, in 0..4. Put
F(5q+r)=9q+(0,1,3,6,8)[r]. Literal U is the descending sequence F(H_i),
of weight sum F(H_i). Literal B is an ascending partition with parts in
residues 1,3,6,8 modulo nine. The functions `columns_to_residue` and
`residue_to_columns` in `../../checks/rr003_stockhofe.py` are mutually inverse
on precisely these full domains, preserve literal weight, and terminate.
The helper map on heights has five-regular descending output R. Its
residues, in order, are the nonzero residues of H in their original order.

The following argument also addresses the phase-order issue that an
implementation check alone cannot settle.

## Forward validity and recorded units

Call a multiple 5k directly removable when deleting it leaves a five-flat
sequence. For a noninitial part this is precisely the implementation's
test that its upper neighbor minus its lower neighbor is less than five;
an initial part is directly removable. The first phase scans from bottom
to top and deletes exactly such parts, recording k. Each deletion preserves
flatness and the nonground residue word. A multiple rejected during this
scan cannot become directly removable after deletions above it: its lower
neighbor is fixed and its upper neighbor can only increase. Consequently
all remaining multiples are essential after the scan. They are internal
and isolated. In particular, in a run of equal adjacent multiples the
bottom one is directly removable, so no such run can remain.

In phase two, let the topmost remaining multiple be 5k, with i parts above
it (the code's zero-based index). Those i parts are nonground. Its
nonground upper and lower neighbors lie respectively in
[5k+1,5k+4] and [5k-4,5k-1]. Their gap is at least five because the multiple
is essential, and at most eight by flatness. Deleting 5k and lowering the
prefix by five therefore creates a gap in 0..3 and keeps every part
positive. Other gaps remain unchanged. Every other essential multiple
keeps its own neighboring gap: even when there is only one nonground part
between consecutive multiples, that intervening part is below the deleted
one and is not lowered. Thus phase two preserves flatness and essentiality
until all multiples have been removed.

The remaining regular flat sequence L is uniquely determined by its
nonground residue word: starting at zero, each required residue has a
unique minimal nonnegative increment in 0..4. This is exactly
`_minimal_regular`. Every forward step decreases the number of parts.

For completeness, every recorded unit is at most the number l of retained
nonground parts. Below a height 5k a five-flat sequence must meet each
interval [5t-4,5t-1], t=1,...,k; otherwise it would cross a drop of at least
five. These disjoint intervals contain only nonground heights. A direct
unit k is therefore at most l. At an essential removal all i parts above
are nonground and at least k nonground parts are below, so its unit k+i is
also at most l. Conjugating the partition E of units consequently gives a
partition D with at most l parts.

## Phase order and the inverse boundary

For a five-flat sequence define f_j=j+ceil(H_j/5), with one-based j.
Consecutive f-values increase by zero or one. The last is length(H)+1.
Immediately after any multiple 5k, its lower nonground neighbor has the
same ceiling k, so f increases by one there.

The direct units are recorded in nondecreasing order because the scan is
from bottom to top. Their maximum is at most ceil(T/5), where T is the
top of the sequence remaining after phase one. Indeed, if the highest
deleted multiple 5k has no retained height above it, the first retained
nonground height below its initial equal-multiple block is at least
5k-4. Otherwise a retained larger height already supplies the bound.
Nonempty H always retains a nonground part because its positive final
height is less than five.

For an essential removal at position i+1, its unit e=k+i equals
f_(i+1)-1. Monotonicity gives e>=ceil(H_1/5), and the lowered top afterward
has ceiling ceil(H_1/5)-1. Hence reversing this removal uses the inverse's
essential branch. After removal all remaining f-values decrease by one.
Since the lower nonground neighbor had f at least one larger, the unit of
the next essential removal is no smaller. Essential units are therefore
recorded in nondecreasing order and are at least every direct unit.
Sorting E loses no needed phase information; equal units are
indistinguishable and the boundary test determines which phase applies.

Now start the inverse from any regular R. Its unique minimal sequence L
has the same ordered residues. The vector D=(R-L)/5 is nonnegative and
descending: every adjacent gap of R is at least the unique gap in 0..4
having that residue difference, namely the gap of L. Its terminal value
is also nonnegative. Thus E=D' is a partition of positive units, each at
most l, processed in descending order.

Initially L is flat and has no multiples. Before each essential insertion
maintain that every existing multiple has f_j>e, for the current unit e.
If e>ceil(H_1/5), monotonicity and the bounds e<=l<=length(H) imply that
there is a largest i with f_i<=e, and that i is not the last position.
Since the f-values have increments zero or one, f_i=e and f_(i+1)=e+1.
The invariant makes H_i nonground. Put k=e-i. Then H_i has ceiling k and
lies in [5k-4,5k-1]. The next height has the same ceiling, is no larger
than H_i, and lies in that same interval. In particular k>=1 and that
next height is also nonground.

Raising the first i heights by five and inserting 5k between them gives
two gaps in 1..4. Removing the new multiple without lowering the prefix
would leave a gap at least five, so it is essential. Its new f-value is
e+1. Every old multiple's f-value increases by one, either through its
height or through its position. This preserves the invariant for the
next unit, which is at most e. It also preserves all older essential
neighboring gaps because insertion is between two nonground heights.

When e<=ceil(H_1/5), sorted insertion of 5e preserves flatness: if it is
above the old top its new gap is at most four, otherwise it splits a
previous gap; and 5e is above the final height, which is below five.
All later units are no larger, so all subsequent insertions are direct.
These direct insertions reverse the first removal phase in reverse order.
They can become adjacent to an existing essential multiple only at its
same height, because the two nonground neighbors of that essential
multiple lie strictly between the neighboring multiples of five. The
bottom-up scan deletes the extra equal copies and leaves one essential
copy. Before the direct insertions, all inserted multiples are essential.
Phase two then deletes
essential multiples from top to bottom, in the reverse order of their
insertions, with exactly the prefix lowering just described. Conversely,
the boundary f_i=e, f_(i+1)=e+1 computed after a forward essential deletion
recovers its original position. These observations prove both identities
for every input, including the empty input (which takes no insertion
step and never accesses a nonexistent top).

## Literal weight, code scope and finite evidence

Deleting 5k directly removes weight 9k. Deleting it with i prefix shifts
removes weight 9(k+i), since F(h+5)=F(h)+9. The nonground residue word and
its alpha offsets remain fixed. Conjugation preserves sum E, and output
R=L+5E' therefore restores exactly the removed weight. The inverse
reverses this accounting. Removal reduces list length; insertion consumes
one member of a finite E; conjugation and boundary scans are finite.
All intermediate weighted sums are at most the endpoint weight.

I inspected the actual endpoint module, its `kr1` object/weight/conjugation
definitions, and its import safety. No legacy test module was imported.
The separate script `.runs/rr007/critic-b-stockhofe12.py` independently
generates all literal U and B objects of weight at most 12 and invokes the
actual endpoint functions. Receipt
`.runs/rr007/critic-b-stockhofe-pilot12.receipt.json` passed: 59 objects on
each side, exact image, both identities and weight. U has 14 distinct/45
repeated objects and B has 15 distinct/44 repeated objects in that pilot;
literal distinctness is not asserted to be preserved. The largest actual
input or output weight was 12. These finite facts supplement the proof;
they do not prove its universal quantifiers or a U/C bridge.
