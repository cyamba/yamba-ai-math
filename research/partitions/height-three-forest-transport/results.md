# P014 results: fork inverse, necessary cross-block transport, Hall obstruction

**Target: conjectural. Novelty: unverified. Universal theorem: not achieved.**
The next bounded phase is complete with two author/critic rounds and one
predeclared digit repair. A written universal partial fork inverse repairs
the old seven-vertex isolate, and complete development tests improve its
grammar coverage. A separate eight-vertex Hall obstruction then refutes
direct cancellation in this extended grammar. No new Lean work began.

The [frozen proposal](README.md), [protocol](protocol.json),
[round-one review](review-r1.md), [recorded repair and narrowed second check](repair.md),
[written obstruction](obstruction.md), [final review](review-r2.md),
[compact evidence](evidence.json) and [execution record](execution.json)
keep conditional proofs, computations, source versions and gates separate.

## Mathematical progress

1. **Established mathematics, attributed:** Tom's tree-list bijection and
   maximum-insertion coordinates give a product-of-chains representation
   for every fixed component-set/composition block, including every tree
   and mark. Zero-neighbor blocks are empty, not zero-capacity coordinates.
   See [Tom v2, Lemmas 3.11/3.13](https://arxiv.org/html/2311.08020v2).
2. **Written and separately checked reduction, not Lean:** the rectangle
   symmetric-chain recursion pairs all interior epsilon-doubled states,
   leaving bottom/epsilon-zero and top/epsilon-one endpoints. For the P013
   witness block, the polynomial is `[2]_q^3 [3]_q^2 [4]_q`; its degree-six
   first difference is `53-60=-7`, below the global midpoint seven. Thus
   cancellation confined to that block cannot suffice, regardless of
   coordinate order. Cross-block transport is mathematically necessary.
3. **Written universal partial relation, not a covering theorem:** sibling
   subtrees `v<u` with parent `p` can be split by replacing `v--p,u--p`
   with `v--u`. The root/child inverse restores the exact parent edges.
   Every composition boundary, both assignments and all bounded mark
   solutions are retained. Full inversion differences determine the mark
   equation. Validity, type, sign, degree and reverse membership follow;
   a collision-free universal pivot and positive survivors do not.

The explicit P013 witness is paired at degree six by `v=2,u=3,p=5` with
parents `(2,3,0,5,7,7,0)`, compositions `((3),(3,1))`, marks `(3,3)` and
epsilon one. Its inversion drops from three to one and the mark sum rises
to compensate. The inverse recovers the exact source. The composition
boundary must be assigned in reverse order; retaining only one sector or
assignment would miss this pair.

None of these partial facts establishes a new unresolved unimodality
theorem. The source comparison remains bounded to the retained frontier
audit and the inspected Tom statements; novelty is not certified.

## Complete development evidence

Round one enumerated all four development signed spaces, before lower-half
restriction, and checked every accepted primitive edge for actual validity,
sign, degree and same-primitive inverse membership. Three coefficients
were compared with P013's saved independent-coloring results. The additional
size-eight case received a new independent coloring calculation and complete
tableau comparison. Saved comparisons are not fresh oracle runs.

| Development vector | Marked forest triples | Lower-half negatives | Complete-grammar diagnostic |
| --- | ---: | ---: | --- |
| `(2,4,4,6,7,7,7)` | 320 | 258 | All 258 saturated by finite diagnostic matching |
| `(3,6,6,6,7,7,7)` | 2,352 | 2,091 | All 2,091 saturated by finite diagnostic matching |
| `(3,3,4,6,6,7,8,8)` | 480 | 358 | All 358 saturated by finite diagnostic matching |
| `(3,5,5,7,7,7,8,8)` | 5,024 | 4,485 | Verified Hall subset: two negatives, one neighbor |

All four frozen selectors fail on every development case. Their unpaired
counts are respectively `150,193,98,95`; `1468,1544,767,733`;
`240,277,148,140`; and `3473,3110,1717,1630`. Collision witnesses and failed
reciprocal recovery are retained. Finite diagnostic saturation is not an
explanatory cancellation rule or a universal proof.

The new nonempty size-eight comparison explicitly includes all contributing
raw determinant sectors: shapes `(3,2,2,1)`, `(3,3,1,1)` and the exceptional
sorting-correction shape `(3,3,2)` have respectively 104, 40 and **32**
tableaux, with signs positive, negative, negative. The signed coefficient is
`q^2(1+q)^5`. This supplies additional nonempty exceptional-sector coverage;
it does not change or retrospectively upgrade the earlier empty P013 case.

## The decisive remaining obstruction

On `h=(3,5,5,7,7,7,8,8)`, both negative states have parents
`(3,5,4,6,7,0,8,0)`, marks `(1,1)` and epsilon zero. Their compositions are
`((1,3),(4))` and `((3,1),(4))`. The component words are increasing paths,
and the three inversions are forced across components. Both have degree
three, below the global midpoint seven.

Their complete accepted neighbor union contains just one positive object:
parents `(3,5,4,0,7,0,8,0)`, compositions `((3),(4),(1))`, marks `(1,1,1)`
and epsilon zero. The two composition orders collapse to this same object;
different edge/word witnesses do not provide additional positive objects.
The [written exhaustive check](obstruction.md) proves the deficiency `2>1`.

The sole digit repair cannot add a neighbor: epsilon zero requires lowering
a tree digit, and all digits are already zero. Mark steps also fail at their
minimum. Round two therefore verified this small complete-neighborhood
certificate directly instead of repeating full enumeration or exposing
held-out cases. The verification reconstructs actual states and statistics,
checks every primitive and reverse membership, and confirms the exact
neighbor union. This refutes single-edge cancellation in the frozen union,
not an as-yet-undefined composite-move grammar or unimodality itself.

The graph's full coefficient is `q^5(1+q)^4`, consistent with unimodality.
Explicit positive degree-three signed objects outside the frozen neighbor
set are recorded in the written note. They illustrate the need for further
component-membership transport; no additional rule or third repair was tested.

## Held-out status and resource boundary

Neither fresh held-out vector was run:
`(3,5,5,6,6,9,9,9,9)` and `(4,4,5,7,7,8,8,10,10,10)`.
They were frozen before development and remain untested. No round-two
selector was locked and no held-out success is claimed. No cases were
capped, replaced or rerun. The second check was explicitly narrowed in
`repair.md` before verification because the complete development Hall
certificate already refutes the sole repair.

| Research round | Mode | Extensions | Candidate charges | Wall seconds | Peak RSS bytes |
| --- | --- | ---: | ---: | ---: | ---: |
| One | Complete development census and grammar checks | 252,890 | 1,243,264 | 4.879618 | 57,098,240 |
| Two | Direct repaired-grammar Hall verification only | 2 | 228 | 0.461501 | 24,297,472 |

Per-round limits were 600 computation seconds, five million extensions,
five million candidate charges, 120 seconds per case, one enumeration process,
sampled 2 GiB RSS and aggregate output-directory artifacts 250 MiB. Neither
round approached a resource cap. Attempted/rejected primitives, inverse checks
and grammar-matching traversals are charged. The second round's two extension
charges are certificate-source visits, not two full forest enumerations.
The verifier validates only the stated subset, not the whole repaired graph.

Memory is sampled process high-water RSS, not an OS reservation; the artifact
guard covers its output directory, not a filesystem quota. Literature reading,
specification generation, focused/full engineering tests and review are
separate from research counters. Model tokens and monetary cost were not
independently metered. No installations, new dependencies or paid compute
were used. Historical round-one source and final verification source are
both retained; the latter adds certificate execution without changing the
frozen mathematical grammar.

The harness validates/plans the `pair` program and prepares six manual stage
packets, at 16 declared dispatch proxy units. Root performed lead work and
`frontier_critic` supplied the separate reviews. Manual packets remain
prepared instructions. Offline replay accepted six lead-written post-hoc
stage summaries as saved response protocol. It was not a fresh worker
dispatch, mathematical proof or test of scientific independence.

Workflow accounting includes an additional critic preflight call before the
written P014 contract and freeze, followed by the two formal review calls.
Conservatively pricing that call as another critic-stage dispatch adds two
proxy units: **18 overall versus the planned formal-stage total 16**. This
preparation/deviation must not be hidden by a six-stage replay receipt. There
were still only two formal proposal/review rounds, one repair and two research
executions; the search resource caps were not exceeded. The proxy tally is
not measured money or tokens.

All **90 repository unit tests** passed after the functional changes.
Repository checks, harness validation and the whitespace check also passed.
These engineering checks do not validate the mathematical claims or novelty.

## Gate and next obligation

The universal proof gate remains **unmet**. The next construction must
distinguish composition order when path components sit at minimal internal
weight, and supply recoverable transport to different component blocks.
More within-block digit/mark steps cannot remove the displayed Hall deficit.
No third repair, new search or substantial Lean work was performed.

Reproduction uses fresh output paths and is not asserted as an additional run:

```sh
python3 -m harness plan programs/partition-h3-forest-transport.json
python3 -m research.partitions.checks.forest_transport freeze
python3 -m research.partitions.checks.forest_transport run --round 1 --output .runs/h3-forest-transport-reproduction/r1.json
python3 -m research.partitions.checks.forest_transport certify --input .runs/h3-forest-transport-reproduction/r1.json --output .runs/h3-forest-transport-reproduction/r2.json
python3 -m unittest discover -s tests -v
python3 scripts/check_repository.py
```

The frozen original verification spec is retained. Fresh reproduction permits
only an input-receipt-hash rebind when every other specification field agrees;
the new report embeds that actual binding and existing receipts are never
overwritten. Earlier certificates, publication work and all P012/P013 files
are protected by the [opening hash inventory](upstream.json).
