# Argon continuation: stronger restricted results and a compiler obstruction

Date: 26 October 2026. Research base: `2ccf9c5`.

**Global KR1 bijection remains unresolved.** The previous weight-41
counterexample is preserved. Novelty is **not verified**. These are written
mathematical proofs with separate semantic review, not new Lean certificates.
The new computations are explicitly bounded corroboration.

## Retained results

1. **A proved and stronger cone theorem.** For
   `U=(10^z,9^y,8^x,6^c6,3^c3,1^c1)` with `y>=1`, literal U-validity is
   equivalent to `x+c6+c3+c1>0`. Under `x+z>=1`, membership in the current
   `a<=2` image is equivalent to
   `z<=3 and y>=3 and c6>=2 and c3>=2`. Thus the earlier cone conjecture
   holds for `y=1,2` with **no upper bound on z**. The exact first overlap
   in the larger family occurs at weight 53. See [complete proof](cone_proof.md).
2. **The entire existing a=3,b=0 sector has an all-parameter proof.** For
   every nonnegative `s,t,d`, the current map on
   `(3,0,(s,s+t,s+t+d),())` is valid, weight preserving, disjoint from the
   specified lower image, and has an explicit inverse onto its stated image.
   It is no longer only a claim checked through weight 60. This says nothing
   about coverage of all higher sectors or compatibility with other higher
   maps. See [complete sector proof](restricted_sector_proof.md).
3. **A universal obstruction to Argon's fixed-alphabet compiler.** No
   weight-preserving injection can encode all cluster apexes using any fixed
   finite column alphabet. A binary-increment apex family grows exponentially
   while cumulative fixed-alphabet capacity is polynomial. For the proposed
   six weights, `2^128` apexes have weight at most 75,081, exceeding even the
   generous upper target bound `75082^6`. See [proof](capacity_proof.md).
4. **A small, concrete compiler obstruction.** Under Argon's bounded-z
   unique-head rule there are already 30 source apexes but only 29 available
   head labels by weight 55. Tail offsets do not repair full-octant reuse:
   two translates of N^3 with the same head always intersect.
   See [repair audit](repair_audit.md).

These statements have different roles: (1) and (2) provide safe restricted
constructions; (3) and (4) rule out the proposed global architecture. Neither
kind of statement constitutes a complete proof of KR1.

## What Argon's note contributed and what failed

The 15-page PDF supplied the cone-validity argument, a lower-image exclusion
template and a distinct-head coordinate idea. We completed the forward-branch
classification and the restricted-sector proof instead of assuming that
finite checks established them. Attribution to Argon is preserved; a prior-work
novelty audit has not been conducted.

Its proposed surgical remappings collide with existing higher-sector targets.
For example, proposed `(9,8,8)` at weight 25 is already the current image of
`(4,0,(0,3,3,3),())`; proposed `(10,9,9,3)` at weight 31 already belongs to
`(4,0,(0,0,5,10),())`. Five exact collisions are in
[the audit and report](repair_audit.md). They refute those repairs **if other
assignments are retained**, rather than every possible coordinated rerouting.

The note also misidentifies a literal apex image as `(19,12)` instead of
`(18,10,3)`, weakens the terminal-height predicate incorrectly, and calls
six tuple scans constant time. The repaired proofs use the actual code
conditions and ordinary linear-time tuple decoding.

## New executable model and finite evidence

[`six_weight_cones.py`](../../rogers-ramanujan/checks/six_weight_cones.py)
implements literal multiplicity coordinates, the exact lower preimage,
coordinate recovery and same-head octant intersection. It does not modify or
repair the existing full KR1 map. A safe lower-sector-free cone target may
still be occupied by another higher-sector state.

- [Cone corroboration](cone_evidence.json): 8,375 tuples, including 828 exact
  predicted lower intersections and their reconstructed preimages.
- [Sector corroboration](sector_evidence.json): 4,329 coordinate-box cases,
  reaching weight 125, comparing the independent closed formula and inverse
  against the existing code.
- [Repair evidence](repair_probe.json): five occupied targets and the exact
  finite head/source counts.
- Seven new regression tests exercise the real decoder, terminal boundary,
  first lower intersection, unbounded-z examples, unsafe future increments,
  inverse recovery and same-head overlap.

Finite corroboration supports transcription. The all-parameter conclusions
come from the written arguments and their semantic review. No new Lean run
or theorem is claimed for these results.

**Verification:** all 107 repository tests pass, the repository integrity check
passes, and the separate mathematical critic supports all retained written
statements, including a soundness lemma needed by the code-inverse argument.
No Lean certification is claimed for these new results.

## Next precise obligation

A complete construction must leave a fixed six-weight alphabet eventually.
It must recover unbounded apex information and prove disjointness among
**all** higher families, not just from the lower image. The new restricted
bijection and exact cone signature are possible components. A global source
partition, target coverage theorem and mutually inverse algorithms remain open.

## Reproduction

From the repository root:

```sh
python3 research/partitions/argon-2026-10-26/cone_author.py
python3 research/partitions/argon-2026-10-26/sector_checks.py
python3 research/partitions/argon-2026-10-26/probe_repair.py
python3 -m unittest discover -s tests -v
python3 scripts/check_repository.py
```

Run without `-O`; exact checks use assertions. The separate review is recorded
in [review-round1.md](review-round1.md). Input hash and extraction caveats are
recorded in [input_provenance.json](input_provenance.json). No original private
chat transcript or PDF was committed. No new website publication is made by
this continuation.
