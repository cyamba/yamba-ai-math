# Independent semantic review, round 1

Date: 26 October 2026. Reviewer role: independent mathematical critic.
Reviewed sources: cone_proof.md, capacity_proof.md, restricted_sector_proof.md,
repair_audit.md, six_weight_cones.py and test_argon_cones.py, against the actual
kr1.py, rr003_columns.py, rr003_revision.py, rr003_a2.py, and
rr004_multidim_cones.py definitions.

## Verdict

**Supported by complete written arguments within the stated literal model.**
No P1 mathematical error found in the retained cone, restricted-sector or
capacity statements. These are manually reviewed written proofs, not Lean
certification. Novelty remains unverified. No general KR1 bijection is obtained.

## Cone theorem

The validity equivalence is exact: with y>=1, at least one column below height 5
is necessary and sufficient. All preceding transitions are below 5 because the
height 5 block bridges height 6 to any lower support. Terminal height less than5,
not merely nonzero modulo5, is the literal condition.

The lower-image classification covers every forward layer. Original first-layer
outputs have no 8/10 markers. The b=0 extension cannot have both 9 and an 8/10.
The hole families have either an excluded 17/19/26 marker or no 9 or no 8/10.
The only surviving branch is mixed a2,b3: its mandatory baseline forces at
least three 9s, two 6s, two 3s, while marker normalization forces z<=3. The displayed
formula for k and ascending nu reconstructs every parameter choice satisfying
those conditions. This proves both directions without assuming recognizer
completeness. The smallest intersection weight 53 follows by minimizing its
mandatory columns. The generating function correctly separates x>=1 from
x=0,z>=1 with positive tail.

Scope is essential: L is the image of the current rr003_a2 forward formulas.
This is not a theorem about arbitrary alternative lower-sector maps, and safe
cone coordinates can already be occupied by other higher-sector states.

## Entire a3,b0 restricted sector

The table exhausts t=0,1,2,3 and the three residue classes above 3. Direct
inspection of step_one confirms that its only exceptional action on this
family is (9,6) to (10,6); all remaining moves append 1. The other guard
patterns require absent markers or larger 6 counts. Each core has descending
heights, avoids the possible 6-to-1 jump, and terminates below 5. Each table sum
matches9+3s+2t. The symbolic lower-family exclusions are exhaustive, including
the additional three hole-template patterns.

The listed marker signatures, with the stated 6/3-count exceptions, distinguish
all image families. The recovery formulas recover exactly the declared source
domains. The greedy code inverse removes appended 1s because every predecessor
has already been proved valid and outside L. The exceptional successor is
reversed once to(9,6). For primitive(9,9,1), stripping its last 1 would give an
invalid height 5 terminal, so it stops correctly. The code's subsequent branch
table is exactly the displayed recovery. Thus the claimed bijection is onto
the explicit image family for all nonnegative s,t,d, not onto all U outside L.

The phrase "all-parameter proof" is justified for this restricted sector.
It must not be abbreviated to an all-weight proof of KR1 or of the full map.

## Capacity obstruction

The binary-nu construction produces distinct valid a3,bk apexes, with mu0 and
recoverable binary differences. Its weight bound M(k) is exact for the all-one
vector. Counting target multiplicities by(M+1)^m gives an upper bound even
before U-validity restrictions. The binomial comparison with r=2m+1 is valid:
(k-i)/(r-i)>=k/r for k>=r; choosing k>25^m*r^r yields the required strict
inequality. The explicit six-weight arithmetic at k=128 is correct. Therefore
the fixed-alphabet injection obstruction is supported, including arbitrary tail
offsets. It does not obstruct target alphabets growing with input weight.

The smaller weight 55 unique-head obstruction and same-head translated-octant
intersection argument in repair_audit.md are also valid for their declared
full-octant architecture. The five occupied target witnesses are executable
counterexamples to keeping the other existing assignments unchanged.

## Independent finite corroboration

critic_checks.py uses a different sample scheme from the author checks:
3,500 deterministic coordinate samples including z=17, y=9 and large tail counts,
1,208 restricted-sector samples including s=80, t=120, d=40 boundaries, and all
binary apex vectors for k=1 through 10. Results are in critic-evidence.json.
All passed; 3,390 marked samples were valid, with 414 lower intersections.
These computations support transcription and implementation only. The universal
verdict above rests on the written case and counting arguments.

## Remaining obligations

No repair to the broken global octant map is supplied. The weight 41 witness
must remain recorded. No global totality, coverage or mutual-inverse theorem
follows from these restricted results. Any later publication should state the
assurance level and exact scope, retain Argon's motivating attribution, and
make no priority claim without a separate prior-work audit.

## Appendix: soundness of the literal lower inverse

The sector proof's greedy unstep argument uses the recognizer inside
`is_in_u_rem`. It therefore needs more than exclusion from the forward image.
The following direct soundness lemma supplies that dependency without assuming
an unreviewed global lower-sector bijection.

**Lemma.** If `u` is a valid literal U tuple and
`rr003_a2.decompose_columns(u)` returns `c`, then `c` is a valid cluster with
`a<=2` and `rr003_a2.reconstruct_columns(c)==u`.

**Proof.** Follow the three possible accepting inverse layers.

1. In `rr003_columns`, pure ones are reconstructed identically, including the
   empty tuple. In a full multiple-of-three baseline, every nontop count is
   at least two. The selected top regime gives nonnegative delta: top count
   minus one for a0, top count minus two for a1, or removal of the single
   extra top marker for a2 with first mu entry zero. The positive ones count
   in the latter case gives nonnegative second mu entry. In the separated-top
   regime, the inverse removes exactly the one top marker, leaves all required
   lower baseline counts at least two, and sets first mu entry one. In all
   cases `_recover` takes reversed cumulative sums of delta. Computing the
   forward successive differences recovers those deltas exactly; the marker
   and ones counts are also exact. Thus the first forward layer reconstructs
   the input tuple.
2. In `rr003_revision`, a mixed accepted tuple has only markers 8/10 with
   nonnegative counts x,z, x+z>=1, and 0<=z<=3. It has every multiple3j for
   j=1..b, count at least three at the top and at least two below. Hence the
   extracted delta counts are nonnegative. The recovered k=4x+5z-2 is at least
   two, and `_marker_digits(k)` returns exactly (x,z), since z is its residue
   modulo 4. The reconstructed nu cumulative sums invert all extracted deltas;
   ones give the difference of the two mu entries. The other accepting cases
   are exactly one carrier 8, carrier 9 with positive ones, or carrier(9,3),
   with arbitrary 6/1 counts. Substituting each returned k and tail into the
   b0 forward branches gives the same carrier, 6 count and 1 count.
3. In `rr003_a2`, each accepting hole branch identifies one of k=4/5/9 and b>=1.
   These k values are outside `_marker_digits`, so its corresponding forward
   call uses the same hole template. The inverse requires all template counts
   and minimum ones, then subtracts them. All remaining counts are nonnegative.
   In ordinary mode only multiples 3j with 1<=j<=b may remain. Reversed
   cumulative sums recover nu whose successive differences are exactly those
   residual counts. In parity mode only 6 and at most one 3 remain; the recovered
   nu entry is 2r6+r3, whose quotient and remainder modulo 2 are exactly (r6,r3).
   Finally the recovered second mu entry restores exactly the removed minimum
   ones plus the free ones. No other residual symbols are accepted. Thus this
   forward layer also reconstructs the accepted input exactly.

All returned tuples are sorted and nonnegative by these same checks and the
`ClusterData` constructor. Each inverse layer first calls a predecessor that
validates literal U, so no unsupported invalid tuple is included. Every
accepting case has now been covered. This proves the lemma.

Consequently a valid tuple outside the forward lower image cannot be accepted
by the lower inverse. For every predecessor in the restricted-sector theorem,
validity and forward exclusion therefore do establish `is_in_u_rem`, justifying
the greedy removal of appended 1s. This added lemma closes that implementation
proof dependency; it does not prove lower inverse completeness on any larger
class or a full KR1 bijection.
