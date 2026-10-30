# P012 results: an obstruction, not a unimodality proof

**Universal target: conjectural and incomplete. Novelty: unverified.**
The first bounded investigation is complete as a two-round author–critic
study. It does not establish a new positivity or unimodality theorem. No
substantial Lean work was started because the universal-argument gate was
not met. Existing Lean certificates and publication files are unchanged.

## Round one: complete signed tableaux

All eight frozen development cases and four held-out structural cases
completed. Every computed coefficient is palindromic and all lower-half
first differences are nonnegative. Six development coefficients are nonzero;
two are zero. All eight development coefficients agree with the independent
proper-coloring/subset-expansion oracle. Held-out sizes 9 and 10 have complete
signed-tableau enumeration, without independent coloring checks.

The raw determinant space has two sectors at `n=7`, three at `n=8`, four at
`n=9`, and five at `n=10`. Every sector has a separate permutation tag,
sign and degree census. The exceptional `n=8` term is present. Its tableau
family happens to be empty in all four frozen size-eight development cases;
the determinant-level boundary regression is therefore stronger than the
actual nonempty-family coverage at that boundary. Both size-nine cases and
both size-ten cases have nonempty families in every contributing sector.

**Refuted construction:** all twelve selectors leave 25 development negative
states unpaired. Selector `0` wins only by the prespecified tie break, and
its lock is explicitly ineligible for a success claim. It was fixed before
held-out testing. Held-out failures are retained, including collisions and
nonreciprocal choices; those cases are now exposed for future research.

More decisively, the complete three-primitive grammar has an isolated
negative state at the smallest permitted size:

```text
h = (2,4,4,6,7,7,7),  M = 9
T = 1 3 5     shape = (3,2,2), sigma = identity
    2 6       inversion = 3, epsilon = 1
    4 7       effective degree = 4, sign = -1
```

The [separate review](review-r1.md) gives a complete written proof that
reblocking, comparable-prefix insertion/extraction and one adjacent
incomparable swap each fail to produce a legal opposite-sign target. This
obstructs every matching using that grammar, not merely the twelve selectors.
It is a written finite obstruction with computational confirmation, **not a
Lean certificate**, and no global minimal-Hessenberg-vector claim is made.

The coloring-checked coefficient is `q^3(1+q)^3`, with lower-half first
differences `0,0,0,1,2`. Thus the counterexample refutes the rule grammar
while supporting, rather than refuting, this instance of the conjecture.

## Round two: complete forest-triple comparison

The comparison used the lexicographically smallest complete development
grammar obstruction, the same seven-vertex `h`. The second protocol was
written before forest enumeration. No held-out result chose or repaired it.

The implementation enumerates all decreasing forests by larger-neighbor
parent choices, orders their tree words by component minima, and includes
all composition orders of type `(3,3,1)` and all marks `1<=r_i<=alpha_i[0]`.
Repeated equal parts are not artificially labeled. The weight is the full
word inversion plus `sum(r_i-1)`, as in Tom's Theorem 3.4. The representation
and completeness argument are reviewed separately in [round two](review-r2.md).

| Number of trees | Sign | Forest triples |
| --- | --- | ---: |
| 1 | positive | 56 |
| 2 | negative | 156 |
| 3 | positive | 108 |

There are 320 triples in 72 composition blocks. Their signed polynomial
again equals `q^3(1+q)^3`, agreeing with the tableau and coloring computations.
After doubling, lower-half positive counts are `6,29,64,86,76`, versus
negative counts `6,29,64,85,74`.

The preregistered diagnostic only changes one mark by one and toggles epsilon.
Of 258 negative lower-half states, 206 have such a neighbor and 52 are
isolated under **that restricted mark-step grammar**. Neighbor availability
does not imply a collision-free pairing. This does not obstruct Tom's full
forest approach, which can change trees and compositions. Individual signed
composition blocks also have different symmetry centers; termwise
unimodality of products of q-integers does not prove the desired centered
first differences after subtraction.

No forest split/join construction was searched or certified. This round
compared the complete alternative space before proposing further moves;
it did not silently introduce a third proposal round.

## Execution, resources and evidence boundary

The repository harness validated P012 and produced the `pair` plan and manual
packets. Its planned dispatch proxy is 16 units for two roles over two rounds.
Actual lead/critic work was manual; packet status alone is not execution
evidence. The [execution record](execution.json) maps the actual stages to their
artifacts. Offline harness replay accepted the six saved summaries, validating
response format and dependencies without certifying research or dispatch history.
Separate role identities do not imply independent models or errors.

| Computation | Extensions | Candidate charges | Wall seconds | Peak RSS bytes |
| --- | ---: | ---: | ---: | ---: |
| Original round one | 1,023,403 | 77,468; omitted bubble-generation scope | 9.077615 | 32,260,096 |
| Same-round accounting replay | 1,023,403 | 116,439 | 8.947456 | 32,243,712 |
| Round-two forest comparison | 1,290 | 539 | 0.002492 | 23,363,584 |

The first accounting implementation omitted attempted bubble generations.
The omission was corrected and the identical frozen experiment repeated,
retaining original sources and both receipts. No rule changed. The two runs'
mathematical outputs agree exactly. The complete two-run candidate count
`232,878` is inferred from the deterministic accounted replay, rather than
measured in the original run. Their combined 18.0251 seconds and 2,046,806
extensions remain within round-one limits. The initial per-file artifact
guard was subsequently strengthened to aggregate output-directory size.
Memory monitoring is sampled RSS, not an OS reservation; all observed peaks
are far below the limit. No case was capped. Auxiliary unit tests and source
inspection are engineering work, separately reported from research counters.

Bulk execution receipts, source snapshots and generated harness packets stay
in ignored `.runs/h3-unimodality/`. The reviewed compact `evidence.json`
retains exact case outcomes and original source/report hashes. The current
code includes the disclosed accounting and artifact-guard fixes; historical
hashes bind the actual executed versions. Fresh execution produces new time
and receipt hashes. The recorded forest protocol keeps its original input
hash; reproduction may bind a new receipt only if the experiment specification
is otherwise identical.

Engineering verification passed: all 70 repository unit tests, the repository
checker and harness contract validation. These checks validate implementation
behavior and repository consistency; they do not establish the conjecture.

## Next decisive obligation

The accepted conjecture is still the target. The fixed tableau grammar is
exhausted; extending its search cannot repair an isolated state without a
new primitive. Forest triples expose a different obstruction: mark steps
cannot cancel negative two-tree boundary states with every mark equal to one.
A subsequent, separately bounded proposal should first give an exact
type-preserving forest split/join rule that handles those boundary states,
accounts for the canonical-word inversion change, and has a recoverable
inverse. Its universal lemma and comparison with Tom's existing constructions
must precede another search or formalization. This is an unexecuted next step,
not an asserted new construction or proof.
