# Distinct final review: reserved n=6 tableau refinement

Date: 25 October 2026, Europe/Stockholm. This is the reserved second critic
stage, reviewing a completed author revision. It does not revise the initial
review or the earlier proof/ledger records. The reviewed author freeze has
SHA-256 `4916798c10b6d26d5fad6abe3691f5aa6a97156a986f7db6e055ce6482b392d4`.
Its 80 pinned files and the original accepted 17-file packet matched before
and after verification. No author artifact was edited.

**Final verdict: supported within the declared finite n=6 scope.** The
revision closes the former 3,829-source gap for `[e_(5,1)]` on all 132 natural
unit interval orders of size six. Its local partial-injection construction
has an ordinary inductive proof, inspected below. Coverage of every source
in that finite class is established exhaustively. Neither symbolic totality
for a larger class nor formal certification nor verified novelty follows.
Separate reviewer identity does not guarantee independent model errors.

## 1. The finite cancellation milestone is now complete

**Severity:** informational, supported milestone. **Target:** all negative
literal e51 determinant objects at n=6. **Verdict:** supported by independent
finite exact reconstruction.

The critic independently generated all source and positive tableaux using
separate row/column backtracking and a separate graph-inversion function.
Every one of the 3,980 negative objects has a valid, degree-preserving image;
these images are distinct within each h-fiber. The inverse recognizes exactly
those 3,980 images among all 6,800 tagged positives. Both literal inverse
identities pass. All 151 original assignments are unchanged. The per-h
results are retained in `tableau-final-result.json`.

| Source / positive occurrence | Independent count |
|---|---:|
| T51 / T42 / T3111 / T2211 | 19 / 96 / 1,273 / 2,592 |
| Positive row0 / row1 / T411 / T321 / T21111 | 1 / 1 / 187 / 782 / 5,829 |
| Mapped / negative | 3,980 / 3,980 |
| Recognized / positive | 3,980 / 6,800 |
| Unmatched positives | 2,820 |
| Original assignments preserved | 151 / 151 |
| Images moving 1 / 2 / 3 labels | 3,242 / 712 / 26 |

The movement metric was reconstructed independently: delete the same chosen
labels from source and target and compare the multisets of retained ordered
row blocks, permitting whole-row reordering. The minimum deletion sizes give
the printed counts. No image requires more than three moved labels.

Every intermediate layer, not just the final output, passed injection,
validity, degree, both identities, and exact image recognition on all sources
and positives. Domain sizes at levels 0,...,22 were

`3214,3221,3250,3273,3340,3385,3866,3866,3868,3903,3938,3954,3959,3962,3964,3964,3968,3971,3975,3977,3978,3979,3980`.

The two layers admitting no new sources remain visible. Erasing every memoized
answer, testing all positive inverses first in reverse order, and then testing
the sources produced identical outputs. This addresses call-order ownership
as an implementation concern; purity also follows from the inspected code.

The critic's recursive determinant reconstruction confirms all 85 raw n=6
occurrences and all nine e51 occurrences. In particular, the two T6 tags and
their distinct permutations survive. No determinant multiplicity is silently
removed. The earlier independent coloring agreement on all 197 vectors
through six remains separate evidence for the coefficient interpretation.

## 2. The local partial-injection proof is sound

**Severity:** informational, supported ordinary proof. **Target:** validity,
weight, injectivity, intrinsic inverse, and termination on the algorithm's
defined domain. **Verdict:** supported; **status:** proved with distinct
ordinary semantic review, without a proof assistant.

I read `revision.md`, the refinement notebook, the full final map and inverse
in `revision_local.py` and `revision_layers.py`, and their verification
dependencies. The map imports no discovery matcher or saved results. Its
calls use only the input h, six entries, P-comparisons, tableau validity,
inversion tests, fixed slot cuts, and lower levels. It does not enumerate a
tableau family or a weight fiber. Sorting four labels into a checked P-chain
is an entry operation, not ranking tableaux. The lru_cache tables memoize pure
return values; they are not owner or used-target tables.

### Base cases

The original 151 pairs and their inverse languages retain first priority.
For the new inverse-bubble hook merge, any admitted target demotes to its
source. Thus two different sources cannot merge into that same target. The
inverse demotes the target and requires the deterministic forward merge to
reproduce it; earlier images are excluded before choosing a merge endpoint.

For common demotion, the removed endpoint crosses only the initial leg
entries P-less than it. These are comparable crossings. Its original
same-row neighbor is also comparable. All other incomparable-edge row
orders remain unchanged. Validity follows at the two insertion boundaries:
the last passed entry is below the endpoint, and the next unpassed entry
is not below it. The retained first singleton in the pair source remains
first. The hook and pair antecedent lists therefore contain at most four
and three target-entry cuts, respectively. Filtering for source validity,
exact demotion reproduction, absence from the original domain, and absence
from the earlier merge domain gives an exact intrinsic inverse by taking
the first eligible cut. Old target images are excluded explicitly.

### Inductive admission rule

Assume F_(l-1) is a partial injection with exact inverse I_(l-1). The code
keeps every old assignment. At a new target T it first requires
I_(l-1)(T) to be undefined. Its list E_l(T) then contains only valid sources
S outside the old domain with the fixed prescribed output p_l(S)=T. The
list order is determined by target slots. At most its first member is
admitted. Consequently new targets avoid all old targets, new sources
avoid the old domain, and two admitted sources cannot share a new target.

Conversely, if the inverse returns the first member S, then the same
prescribed output and the same first-member test make the forward map
return T. If the forward map admits S at T, the inverse returns that S.
This proves both identities and exact image recognition by induction.
The validity and explicit inversion-equality guard supply validity and
weight on every prescribed extension, including shortcuts whose guard
alone has not been classified symbolically on all posets.

I checked the target cuts for all branch families:

- Layer 1 extracts the inserted singleton into the middle arm slot.
- Layers 2 and 3 delete the promoted arm entry into its original leg slot.
- Layer 4 chooses the two original top-arm slots among the four chain entries.
- Layer 5 chooses two leg entries as chain middles, then the original two
  arm slots. Its middle entries appear in increasing P-chain order in the
  final leg: inserting the larger one first and the smaller one second
  forces the smaller one before it. Thus the slot order does not lose the
  actual source. The maximum is 6 times 6, or 36 cuts.
- Layers 6 and 10 delete v from the leg; layers 7, 8, and 12 delete the
  ordered slots for v and b, retaining the other two leg entries in order.
- Layers 11, 13, and 14 delete the uniquely inserted chain entry, trying
  all four arm slots. Layers 9 and 15–22 undo a fixed entry permutation.

Every reconstructed candidate is checked for exact prescribed reproduction.
These cuts are complete for an actual prescribed antecedent; independently,
the finite check verified this completeness for every eligible source at
every level. All extracted lists have at most 36 entries. The base has at
most seven. No global ordering of all sources enters the selection.

Every recursive consultation at level l uses level l-1. Fixed level number,
not a history or a used-target set, is the strictly decreasing rank. There
are 22 extensions above a terminating finite base. The printed loose
recurrence `B_l <= 76 B_(l-1) + C` is sufficient for termination at six
entries; this review makes no efficiency claim for the uncached tree.

I also checked the listed reversed-pair sets in layers 17–22 against the
actual row permutations. They are the complete strict row-order reversals,
after pairs comparable in a source or target row are discarded. For an
incomparable earlier-source x and later-source y, reversing their rows changes
the degree by `sgn(y-x)`. The layer-10 special crossing similarly removes
one inversion at its smaller incomparable leg entry and adds one at v,b.
The exact final inversion guard remains the load-bearing safeguard.

## 3. Totality assurance has a precise finite boundary

**Severity:** important scope boundary. **Target:** interpreting this result
as symbolic totality or general e-positivity. **Verdict:** incomplete for
those wider claims; the author does not assert them.

The partial-map induction proves an injection on the intrinsically defined
admitted domain. Its complete coverage of all natural unit interval orders
on six elements was established by exhaustive computation of that finite
class. There is no inspected symbolic case partition showing that one of
the 22 prescribed layers must accept every potential remaining source in
a larger class. The rule uses six-entry slot patterns; it is not an n>6
algorithm. The coefficient handled is e51, not every coefficient or the
full Stanley–Stembridge conjecture. Discovery used these same finite inputs;
the check is exhaustive verification, not held-out discovery validation.

The three-label routing mechanism is concrete progress. A theorem about
higher-dimensional Ferrers boards or a general volume cut/glue has not been
proved. The old one-label Hall failure and isolated-sector obstruction remain
valid and are not erased by the present multi-sector construction.

**Decisive next proof obligation:** replace exhaustive totality by a symbolic
partition of the remaining cases for the fixed layers, or derive a smaller
crossing rule with a proved exact image language and its own totality theorem.
Any extension beyond six requires a fresh authorized numerical boundary.

## 4. Historical freeze mismatch is explained, not overwritten

**Severity:** provenance qualification. **Verdict:** final accepted snapshots
supported; the comprehensive historical latest-file sweep remains a recorded
failure.

The early `structural-freeze.json` pins the 115-source Theorem-A-only code.
Its two filenames refer to versions preceding the 36 conditional triangle
sources. Comparing those old pins against the final filenames produces the
two mismatches retained in `integrity-progress.json`. I verified that the
manifest is unchanged and that this failed receipt remains a failure.

The retained `structural-initial.py` exactly matches the preliminary source
pin. The newly reconstructed `revision-recovered-initial-verifier.py` exactly
matches the preliminary verifier pin. This recovers the original bytes;
it does not retroactively make the reconstructed file an archived pre-run
copy. The recovery timing is disclosed in `historical-pin-recovery.json`.
The accepted original 17-file final handoff, initial critic pins, and all
80 revision pins pass unchanged. These are distinct statements.

The earlier v1 matching source was reconstructed after its pilot, as the
original notebook already disclosed. This review grants no retrospective
pre-run freeze or held-out status to that source.

## Reproduction and resources

The independent final checker and full results are
`tableau-final-check.py` and `tableau-final-result.json`.
Its metered call is labeled `tableau-final-critic-independent`, charged
2.5770 wall seconds, and observed peak RSS of 26,017,792 bytes. It stayed
within n=6, with no failures, external calls, dependencies, or providers.
Closure integrity and final hashes are recorded separately. Initial review
artifacts and all closed prior ledgers remain unchanged.

No further author correction is required for the stated finite result.
