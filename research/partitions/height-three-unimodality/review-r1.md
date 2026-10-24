# P012 construction review, round 1

Date: 2026-10-23. Reviewer: separate `frontier_critic` role. This is the first
of at most two construction proposal/review rounds. The reviewer inspected
source and saved records and independently derived the witness obstruction
below by hand. The reviewer did not launch another tableau enumeration,
rerun the coloring oracle, or build Lean.

**Verdict: supported finite grammar refutation; universal theorem incomplete.**
The complete frozen tableau grammar has an isolated negative first-difference
state already at `n=7`. This is stronger than failure of its twelve selectors.
It refutes the proposed grammar as a universal cancellation mechanism; it
does not refute the selected coefficient-unimodality conjecture. The source
and receipts support the reported finite results, subject to the explicit
resource-accounting amendment below. Round two should compare the complete
forest-triple signed space on this same development witness.

## Material reviewed and source binding

- `research/partitions/checks/height_three.py`, the existing tableau and
  coloring oracles, `tests/test_height_three.py`, `protocol.json`, and program
  `P012`. The tests were read; no reviewer test execution is asserted.
- Ignored `.runs/h3-unimodality/r1.json` and its selection lock, followed by
  `.runs/h3-unimodality/r1-accounted.json` and its separate selection lock.
- Base revision `dce60269fca1774ea8d5600d30f62dbc39c927a4`, branch
  `codex/height-three-coefficient-unimodality`.
- Original `height_three.py` SHA-256:
  `f08290484f921cea6aa3ddb3b5248bb405e8d46229eb445706cdc3ceeaba2032`.
  Accounted replay SHA-256:
  `5774a14ab4848ac23c572b46e971854006d0ab796ed77b9a9b1ca3cf43c2c4d6`.
  The original source snapshot was retained in ignored `r1-source/`.
- Frozen protocol SHA-256:
  `25f438466e506afc5c5e61ae9abe5b7bb5a8b503660c261ec8a924a82470016c`.
- Original report SHA-256:
  `abd6c750e89e5cab78e6c158bff8cc71a89edc09468a345bb9071053f48004fa`.
  Accounted replay SHA-256:
  `3a49b79d32f6f08aba69893c7dd53fa426b87dc61c9eae593dcb7407809be54a`.

The original report's named source hashes matched current files when checked
before amendment. Both reports record source stability. The reviewer compared
all saved case statuses, complete signed-space fields, move results and
oracle results between the two reports: they are identical. Resource fields
and the development hash containing those fields necessarily differ.

## Completeness, statistic and evaluation checks

**Supported by inspected implementation and written algebra:**

- The dual Jacobi--Trudi loop visits every partition shape of width at most
  three and every determinant permutation. The contributing-index filter
  treats negative indices as zero terms and zero indices as `e_0=1`; it
  keeps determinant tags separate. Its zero-based index formula agrees with
  the one-based mathematical formula. The exceptional `n=8` sector is present.
- Prefix enumeration fills row-major order with every unused label. Its row
  test uses the immediate left entry and its column test the already filled
  upper entry; both are exactly the actual tableau conditions. Each valid
  tableau has exactly one retained branch. No shape sector is replaced by a
  convenient subfamily.
- The row-major graph inversion agrees with the tableau row statistic because
  rows contain chains and therefore no graph edges. The independent coloring
  oracle counts ascents; established symmetry/reciprocity supplies the known
  tableau convention bridge, while exact development comparisons test it.
- Each raw determinant/tableau object is doubled with sign
  `sgn(sigma)*(-1)^epsilon` and degree `inv+epsilon`. The code checks equality
  with the lower-half coefficients of `(1-q)c(q)`, and restricts the universe
  to degree at most `floor(M/2)`. It also checks full coefficient reciprocity.
- Legal targets retain actual filling validity, contributing raw tags,
  opposite total sign and equal effective degree. All exact candidate
  extractions are considered; the height-two first-eligible inverse is not
  silently assumed. The reciprocal-choice requirement prevents a directed
  selector from being misreported as an involution.
- The protocol fixes eight development vectors, four held-out vectors,
  primitive orderings and first/last target ordering. Source inspection shows
  selection-lock writing occurs after development and before held-out work.
  The separate lock file equals the embedded original lock, and its
  development SHA-256 matches the saved development cases. This is a
  source/receipt check, not a cryptographic attestation of wall-clock order.

All twelve original cases completed. All eight development coefficients agree
with the independent coloring/subset-expansion oracle. The four held-out
cases do not have coloring-oracle comparisons scheduled; their evidence is
the complete signed enumeration and its internal checks. Every saved
lower-half difference is nonnegative, including zero coefficients. This is
finite empirical evidence, not a proof of the universal inequalities.

Every selector has total development score `25` unpaired negative states.
Tie-breaking chooses selector `0`; its lock explicitly records
`eligible=false`. Held-out evaluation retains that selector without tuning.
Some held-out directed choices collide or fail reciprocal recovery, and the
records preserve those failures separately from isolation. Those cases are
now exposed and cannot serve as untouched holdouts for a revised grammar.

## Independently checked isolated state

Use

\[
 h=(2,4,4,6,7,7,7),\quad
 T=(1,3,5)/(2,6)/(4,7),\quad
 \mu=(3,2,2),\quad\sigma=123,\quad\epsilon=1.
\]

The rows are chains and the column conditions hold. The bounce contacts
`0,2,4,7` give height three by the written height--bounce argument in the
frontier audit. There are nine graph edges. Exactly the edges `(2,3)`,
`(4,5)` and `(4,6)` are inversions, so this is a negative state of effective
degree `3+1=4`, inside the permitted lower half.

At seven vertices the complete contributing sectors are `+(3,2,2)` with
identity determinant tag and `-(3,3,1)` with tag `132`.

1. Same-word reblocking into the opposite determinant sector gives
   `(1,3,5)/(2,6,4)/(7)`. It is invalid because `6` is not below `4` in `P`.
2. The only eligible final two-cell row for comparable-prefix insertion is
   `(4,7)`. Splitting it gives shape `(3,2,1,1)`, outside the contributing
   sectors. The source has no singleton suffix admitting an extraction.
3. Its row-major word is `1,3,5,2,6,4,7`. The only adjacent incomparable
   pair is `6,4`. Swapping it, toggling `epsilon` and retaining the determinant
   sign can only reblock into `(1,3,5)/(2,4)/(6,7)`. This is invalid:
   `h(2)=4` and `h(6)=7` rule out both required row comparisons.

Thus **none of the three primitives has a legal neighbor**, independently
of selector order or tie-breaking. Seven is the smallest allowed target
size; no lexicographically minimal-vector claim is made. The saved isolated
state agrees with this written obstruction.

The oracle-checked coefficient here is `q^3(1+q)^3`; its lower-half
differences are `0,0,0,1,2`. Therefore the obstruction concerns the move
grammar and is compatible with the target conjecture. It is not a new
counterexample to positivity or unimodality.

## Resource-accounting amendment and next step

The first implementation charged the final raw target checks but omitted
forward bubble generation and attempted inverse-generation checks performed
inside `bubble_neighbors`. The first report's `77,468` candidate charges are
therefore not a count of every raw grammar attempt. The lead preserved that
report and its source, added these charges without changing the grammar or
selection rule, and replayed the identical protocol within the same round.
The reviewer inspected the amendment; no new construction was proposed.

| Execution | Extensions | Recorded candidate charges | Wall seconds | Peak RSS bytes |
| --- | ---: | ---: | ---: | ---: |
| Original | 1,023,403 | 77,468, incomplete scope | 9.077615 | 32,260,096 |
| Accounted replay | 1,023,403 | 116,439 | 8.947456 | 32,243,712 |

Combined measured extensions are `2,046,806` and wall time about `18.0251`
seconds, within the round ceilings. Recorded candidate charges sum to
`193,907`; this sum retains the original omitted scope. Identical deterministic
work with only added accounting supports an **inferred**, rather than
originally measured, complete two-execution count of `232,878`, also below
five million. Both executions finish below every case-time ceiling. The
recorded memory peaks are comfortably below two GiB. The artifact guard was
per output rather than aggregate directory size; this was disclosed, and
the observed reports were far below 250 MiB. Aggregate guarding should be
corrected prospectively. No claim of perfect hard memory-limit enforcement
is inferred from sampled RSS.

**Round-two recommendation:** first compare all forest triples of type
`(3,3,1)` on this same development witness, including every composition order
and every `r` choice. Apply the doubled first-difference identity and compare
the exact coefficient with the saved tableau and coloring values. This is
the accepted round-two comparison scope. Freezing and searching a small
forest split/merge and adjacent-edge-swap grammar was an optional proposal
for further construction work, not a mandatory accepted round-two task.
Such work would need complete weight, sign, type and inverse checks; a
finite obstruction would concern the specified grammar. Do not tune a new
tableau grammar on exposed held-out cases. A universal proof remains
necessary before substantial Lean work or a theorem claim.
