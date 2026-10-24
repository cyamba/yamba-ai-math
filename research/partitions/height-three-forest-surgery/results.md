# P013 results: reversible relations, failed universal grammars

**Conjecture: unresolved. Novelty: unverified.** This second bounded phase
is complete, with two proposal/review rounds and one grammar repair. It
does not prove the selected coefficient-unimodality theorem. No substantial
Lean work was started. Existing certificates, failed rules, P012 evidence
and publication files are preserved.

The [frozen proposal](README.md), [protocol](protocol.json), sole
[repair](repair.md), separate [round-one](review-r1.md) and
[round-two](review-r2.md) reviews, [finite evidence](evidence.json) and
[execution record](execution.json) distinguish the mathematical argument,
computations, resource limits and remaining gates.

## What is proved and what failed

**Written partial argument; not Lean:** checked canonical-word splitting and
joining form a type-preserving, sign-reversing, degree-preserving symmetric
relation on the instances where the actual trees and full weight pass the
checks. The one-edge repair also has a written symmetric-relation proof.
For a split its mark equation is

`r_A+r_B = r_old+1+I_old-I_new`.

For a join it is

`r_new = r_A+r_B-1+I_old-I_new`.

All inversion numbers concern the entire canonical forest word, including
reordering other components. Epsilon stays fixed. The equations enumerate
every bounded mark solution, but may have none. Edge and composition-boundary
witnesses prove reverse membership; they are not extra labels in the signed
space and do not prevent collisions of a chosen map.

These partial facts do not supply a universal pivot or positive survivors.
The existing path/clique construction remains attributed to
[Tom](https://arxiv.org/html/2311.08020v2). Its clique weight identity was
not assumed outside that hypothesis. This phase claims no new theorem of
constructive positivity or unimodality.

**Refuted:** both the round-one checked-word grammar and the repaired
mark/word/edge grammar fail to cover negative states. The separate critic
verified an explicit isolated state for each. These are finite written
obstructions, confirmed computationally, not Lean certificates and not
counterexamples to the unimodality conjecture.

## Decisive seven-vertex obstruction after the repair

Take

```text
h            = (3,6,6,6,7,7,7)
parents      = (2,5,5,5,7,7,0)
composition  = (3,1,3) on the single tree
mark         = 3
epsilon      = 1
canonical word = (1,2,5,3,4,7,6)
```

The graph has `M=14` edges and bounce contacts `0,3,6,7`, hence poset height
three. Its word inversions are exactly `{3,5}`, `{4,5}`, `{6,7}`. Therefore
the effective degree is `3+(3-1)+1=6<=7`, and the doubled sign is negative.

- A mark step would increase mark three to four, outside the first-part bound.
- Word splitting removes the last part three and produces tail `4,7,6`.
  It already starts with its minimum, and cannot be a tree word because
  `{4,7}` is absent. There is only one component, so neither join applies.
- A composition-boundary split of `(3,1,3)`, in either assignment order,
  needs subtree sizes three and four. Every single-edge cut of this tree
  has sizes one/six or two/five, in one order or the other. No such cut can
  realize the required sizes, regardless of mark compensation.

Thus the complete repaired grammar has no neighbor for this negative state.
The exact coefficient on this graph is zero, independently checked by the
coloring oracle in round one. The failure obstructs the move grammar while
remaining compatible with unimodality. Seven is the smallest allowed size;
no global lexicographic minimality across all Hessenberg vectors is claimed.

## Development and held-out evidence

Every development case was enumerated completely in both rounds. Round one
checked all four coefficients with the existing independent coloring/subset
oracle. Round two compared development coefficients with those saved results;
it did not rerun the coloring oracle. Full raw forests, all distinct ordered
composition assignments and marks, and both epsilon values were retained
before the lower-half restriction.

| Development vector | Marked triples | Negative lower-half states | Round one | Repaired grammar |
| --- | ---: | ---: | --- | --- |
| `(2,4,4,6,7,7,7)` | 320 | 258 | Grammar admits a diagnostic matching | Same diagnostic saturation |
| `(3,6,6,6,7,7,7)` | 2,352 | 2,091 | Isolate at degree 2 | Isolate at degree 6 |
| `(3,3,3,6,6,6,8,8)` | 0 | 0 | Empty target space | Empty target space |
| `(3,5,5,7,7,7,8,8)` | 5,024 | 4,485 | Isolate at degree 2 | Isolate at degree 6 |

The old degree-zero witness is repaired by a word split into the two paths
`2,3,4` and `5,6,7`, composition `(3)` and mark one on each. The complete
grammar admits a matching of all 258 negatives there, but **all four frozen
selectors still fail**. Matching existence is diagnostic evidence only.

The size-eight disjoint-clique case has no tree large enough for target part
four, so it has no target forest triples. Its empty success does not repair
P012's missing nonempty exceptional tableau-sector coverage. The case is
retained and was not replaced.

After development, selector `1` was locked by the prescribed score and tie
rule. The four scores were `2582,2458,5567,4565` unpaired negatives; eligibility
for a success claim was explicitly false. Held-out data did not select the
repair or selector. All primitive edges in completed cases passed actual
state validity, sign, degree and same-primitive reverse-membership checks;
selector collisions and recovery failures are retained separately.

| Fresh held-out vector | Outcome |
| --- | --- |
| `(4,6,6,7,7,8,8,9,9)` | Complete: 32,296 triples; coefficient agrees with complete tableau expansion. Repaired grammar has an isolate; selector leaves 9,390 negatives unpaired. |
| `(4,4,4,8,8,9,9,9,9)` | Capped during move analysis: full signed forest census retained, but no completed move verdict or independent comparison. |
| `(4,5,6,7,7,9,10,10,10,10)` | Not enumerated: round candidate budget already exhausted. |
| `(2,7,7,8,9,9,9,10,10,10)` | Not enumerated: round candidate budget already exhausted. |

The first held-out polynomial is
`2q^7+9q^8+17q^9+17q^10+9q^11+2q^12`; its lower-half differences are
`0,0,0,0,0,0,0,2,7,8`. Its comparison uses the complete tableau expansion,
not a new coloring computation. The second held-out forest polynomial is
saved as a partial-case artifact; it must not count as a completed held-out
test. No capped case was replaced, rerun or credited as a success. Both
size-nine vectors are now exposed; the two size-ten cases remain untested.

## Execution and resources

The harness validated the new P013 `pair` contract, generated the six-stage
plan and prepared manual packets. The lead and separate critic performed
the research manually. Offline replay accepted six post-hoc stage summaries;
it validates saved response format and dependencies,
not a new model dispatch, theorem, novelty or scientific independence.
Declared dispatch cost is 16 proxy units, not money or tokens.

| Run | Extensions | Candidate charges | Wall seconds | Peak RSS bytes |
| --- | ---: | ---: | ---: | ---: |
| Round one, development | 449,218 | 102,855 | 5.527842 | 33,128,448 |
| Round two, repaired development and held-out | 292,909 | 5,000,000 | 14.041130 | 200,196,096 |

Candidate charges include attempted primitive generation, failed candidates,
same-primitive inverse checks and diagnostic matching traversals. Extension
charges include parent/composition/mark enumeration, coloring-oracle recursion
and selector/matching iterations. Round two stopped at the candidate ceiling;
the ten-minute wall and five-million extension ceilings were not reached.
Later cases were immediately marked capped without further enumeration.
Memory is sampled high-water RSS, not an OS reservation. The artifact guard
covers the aggregate output directory, not unrelated directories.

Bulk receipts, source snapshots, prepared packets and test logs stay in
ignored `.runs/h3-forest-surgery/`. Public compact evidence keeps exact
censuses, minimal failures and source/report hashes. The executed round-one
source predates the sole repair and subsequent engineering additions:
immediate stop of later cases after a round counter is exhausted, extra
proposal/protocol source bindings, and strict reproduction with only input
receipt-hash rebinding. Those changes do not change the round-one mathematics;
no round-one rerun is asserted. Round-two sources and its frozen repair are
preserved separately. Engineering test compute is separate from research
counters; model token usage was not independently metered.

All **81 repository unit tests**, repository checks and harness validation
passed. There were no installations, new dependencies or additional compute
services. No commits, pushes or publication changes were made in this phase.

For an explicitly requested fresh reproduction, choose new output paths:

```sh
python3 -m harness plan programs/partition-h3-forest-surgery.json
python3 -m research.partitions.checks.forest_surgery freeze
python3 -m research.partitions.checks.forest_surgery run --round 1 --output .runs/h3-forest-surgery-reproduction/r1.json
python3 -m research.partitions.checks.forest_surgery run --round 2 --input .runs/h3-forest-surgery-reproduction/r1.json --repair --output .runs/h3-forest-surgery-reproduction/r2.json
python3 -m unittest discover -s tests -v
python3 scripts/check_repository.py
```

These reproduction commands are provided as instructions; no additional
research rerun is asserted. Existing receipts are never overwritten. A new
input hash is permitted only if every other frozen round-two field agrees;
the original protocol file is retained and the report embeds the new binding.

## Universal proof gate and next obligation

The universal argument gate was **not met**. We have conditional inverse
relations and written finite obstructions, not a positive-survivor construction.
No unrestricted degreewise matching is offered as an explanation of
nonnegativity. Lean formalization remains gated.

Any next proposal must account for a saturated one-tree state whose composition
boundaries do not coincide with any single-edge cut. It needs a precisely
defined richer tree transformation and recoverable weight transport, followed
by a universal pivot or survivor lemma. Extending the failed selectors or
spending more computation on this fixed grammar cannot remove the displayed
isolate. A further proposal would require a new bounded phase; no third repair
or additional search was performed here.
