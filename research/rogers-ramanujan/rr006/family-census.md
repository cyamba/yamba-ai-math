# RR006 family census — 24 October 2026

**Full KR1 remains unresolved.** The RR005 empty-F-root correspondence covers
411/1,393 full objects on each literal U/C side through weight30 (29.50%), but
only 1/34 distinct residual roots on each side (2.94%). These denominators
answer different questions. This census supplies exact exposed finite rows
and two elementary family classifications; it supplies no new root map.
Novelty is **unverified**. New arguments below initially have author-only
assurance and are submitted to the distinct RR006 critic.

## Definitions, provenance and finite scope

The baseline is exactly the separately reviewed RR005 three-stage normal
form and empty-root partial map from [second proposal](../rr005/round-2-proposal.md)
and [final review](../rr005/round-2-review.md). First strip L1, then L3, then
L6; reconstruct R6, R3, R1. A full object is covered exactly when its F root
is empty. No RR003 partial image is overlaid with this map.

U is the literal descending positive column domain, with
`F(5q+r)=9q+(0,1,3,6,8)[r]`, whose decoded-height drops, including the terminal
drop to zero, are in0..4. C is `(a,b,mu,nu)` with a,b nonnegative and ascending
nonnegative vectors of exact lengths a,b, including zeros. Its weight is
`a*a+3*a*b+3*b*b+sum(mu)+3*sum(nu)`. A/B retain the literal gap/residue
conditions in [handoff](SESSION_HANDOFF.md). Empty is distinct vacuously.

The saved [RR005 record](illustrations/rr005-six-through30-result.json) contains
per-weight U/C/partial aggregates and explicit residual-root rows through30.
It does **not** contain full-object rows for the new refinements. Newly
regenerated rows are in `.runs/rr006/census-through12.json` and
`.runs/rr006/census-through30.json`; these are discovery evidence on previously
exposed weights, not held-out evaluation. Each row retains its full object,
root, strip counts, intrinsic predicates and endpoint projection.

Four distinct table denominators follow below: full U, full C, literal F_U
objects counted once each, and literal F_C objects counted once each.
In the root tables, covered means the sole matched empty root. A root's many
strip-count descendants are counted separately only in the full-object tables.
All percentages are exact displayed numerator/denominator fractions rounded
to two decimal places; an empty denominator is N/A. Cumulative ranges are
0..N inclusive. Data tables preserve side labels even when coefficients agree.

The frozen pilot through12 passed before root approval of the unchanged
extension through30. At12 there are59 full objects per side,48 covered and11
missing, versus four roots per side, one covered and three missing. The
implementation checked literal membership, empty/zero/repeated cases, tail
drops, normal-form weights and both round trips; covered U/C partial-map
round trips; both endpoint round trips; exact root grammar; and agreement
with saved exposed aggregates/root rows. All executed input, reconstruction,
partial-map and endpoint weights were at most12 in the pilot and30 in the
extension. No raising control beyond either bound was executed.

## Distinct and repeated are side-specific predicates

U-column distinctness and within-vector increment repetition on C are separate
intrinsic predicates. The latter means a repetition within mu **or** within
nu, counting zero entries; equality across different vectors does not count.
A/B distinctness means literal part distinctness on that side. These pairs
of bins partition their respective domains, but do not identify partners.
The a,b table also consists of disjoint bins. Root-weight, width/height,
terminal-height and final-increment-gap row fields are additional cross
tabulations, not extra coverage to add.

Literal A/B denominator/distinctness counts are **empirical exact enumeration**.
Their covered/missing classification and cross-side correspondence are
**conditional** on the RR003 author-only
[direct gap/C endpoint](../rr003/endpoint-cluster-merge.md) and
[Stockhofe residue/U implementation](../rr003/endpoint-stockhofe.md).
The finite endpoint round trips do not upgrade those universal assurances.
No full A/B theorem is inferred from this census.

Conditional covered-pair cross tabulation through30:

| A literal cohort | B distinct | B repeated | Total |
| --- | ---: | ---: | ---: |
| A distinct | 8 | 353 | 361 |
| A repeated | 0 | 50 | 50 |

The smallest crossing is A=(2), B=(1,1), weight2. Distinctness is therefore
not preserved by the chosen endpoint composition. The zero in the other
direction is a bounded observation here, not a proposed domain split theorem.

Smallest missing examples, ordered by weight then lexicographic tuple:

| Side/cohort | Smallest missing object | Weight | Assurance |
| --- | --- | ---: | --- |
| U distinct columns | (8) | 8 | literal RR005 predicate |
| U repeated columns | (8,1,1) | 10 | literal RR005 predicate |
| C repeated increments | (2,0,(2,2),()) | 8 | literal RR005 predicate |
| C no repeated increments | (2,0,(2,3),()) | 9 | literal RR005 predicate |
| A distinct parts | (3,5) | 8 | transported coverage conditional |
| A repeated parts | (1,2,6,6) | 15 | transported coverage conditional |
| B distinct parts | (8) | 8 | transported coverage conditional |
| B repeated parts | (1,1,8) | 10 | transported coverage conditional |

For comparison, repeated U=(1,1) is covered at2; repeated C increments
`(2,0,(0,0),())` are covered at4 and correspond conditionally to distinct
A=(1,3). Repeated A=(3,3) is covered at6. Thus no one of the four ordinary
distinct/repeated A/B cohorts isolates success or failure. In particular all
three repeated A objects through12 happen to be covered; this fails at15.

## Elementary residual-C grammar

**Proved, author elementary argument, RR006 separate review pending.** This
is a restatement of the reviewed predecessor failures, not a new strip or
cross-domain construction. Assume literal C throughout. For b>0 put
`V: nu_b=nu_(b-1)`, using `nu_0=0` when b=1. The following disjoint branches
are exactly F_C:

1. Empty.
2. a=0,b>=2, with `nu_(b-1)=nu_b=nu_(b-2)`, interpreting the preceding
   entry as zero when b=2.
3. a=2, `mu=(k,k)`, k in{1,2,3}, V if b>0, excluding b=0,k=1.
4. a>=3, `mu_(a-1)=mu_a`, `mu_(a-1)-mu_(a-2)<=2`, and V if b>0;
   when b=0 require a>=4 and `mu_(a-3)=mu_(a-2)`.

Proof: start from RR005's exhaustive E_C cases. On the a=0,b>=2 case,
L6 exists exactly when the gap before the final equal nu pair is positive;
the failed test is the equality in branch2, including the b=2 zero boundary.
For a=2, E_C has k>=1; L6 subtracts three precisely for k>=4, and separately
removes the exceptional b=0,k=1 object. The surviving k are branch3.
For a>=3, E_C already imposes the final mu equality, the nu condition and
the stated b=0 boundary. L6 exists exactly when the preceding mu gap is at
least three; its failure is branch4. Empty has no six predecessor.
These cases exhaust E_C and the six failure tests, proving equivalence.

Corollary: **every nonempty F_C root has a within-vector repeated increment**.
Branch2 repeats nu, and branches3–4 repeat mu. This does not mean every full
missing C object has repeated increments:625 of982 missing full C rows have
no repetition. Stripping the final unit excess can change this predicate;
the smallest example `(2,0,(2,3),())` lowers to `(2,0,(2,2),())`.
The frozen census checked the grammar against the predecessor predicate on
all1,393 C objects through30; that check supports transcription, not the proof.

## Two neighboring family comparisons

### Pair1: two singles and a residue obstruction

Let `C(k,s)=(2,0,(k,k+s),())`, integers k,s>=0, of weight `4+2k+s`.
Its literal gap expression is A=(k+1,k+s+3), always distinct. Interpreting
that expression as the endpoint image retains the author-only endpoint
dependency; the following normal-form statement itself uses only reviewed C
operators.

**Proved, author argument, separate review pending:** C(k,s) is covered by
the RR005 empty-root map iff `k=0` or `k=1 mod3`.

For k>0, L1 removes exactly s, leaving equal positive increments k,k;
L3 has no predecessor. For k>=4, L6 subtracts three from both increments.
If the remaining k is1, the exceptional empty six inverse removes it; if it
is2 or3, it is a nonempty F_C root. Thus for `k=3m-2`,m>=1, the normal form
is `(empty,n1=s,n3=0,n6=m)`, with known U image `(6^m,1^s)` and conditional
B image `(1^s,6^m)`. For `k=3m+2`,m>=0, the root is `(2,0,(2,2),())` with
counts `(s,0,m)`; for `k=3m+3`,m>=0, it is `(2,0,(3,3),())` with those
counts. These last two families remain unassigned. For k=0, the special
L1 inverse removes the equal-zero datum, then L3 removes the single pair:
counts are `(s+1,1,0)`, with empty root. This proves the exact classification,
including both zero boundaries. All successful/missing cases have mu
repetition exactly when s=0; repeated increments do not explain the split.

The first missing k=2,s=0 has weight8; k=1,s=0 is its covered neighbor of
weight6. A plausible **unexecuted clue**, not an accepted rule variant, is
to match the two surviving seeds k=2,3 to U=(8),(9,1), respectively, and
transport the existing counts. An intrinsic inverse would first strip and
recognize exactly those roots. Both seed weights match, and their normal
form chains would be disjoint, but all other roots remain outside this
proposal. The smallest falsifier of an asserted complete-root extension is
the already exposed root `(0,2,(),(0,0))` at12. A global root parser, rather
than two extra seed assignments, remains the substantive obligation.

### Pair2: one pair versus two pairs

Let `D(t)=(0,1,(),(t,))`,t>=0, of weight `3+3t`. It is always covered:
L3 removes t increments and then the exceptional zero pair, giving counts
`(n1,n3,n6)=(0,t+1,0)`. Thus U is `(3^(t+1))`. Its conditional A expression
is `P_t`, where `P_(2r)=(3r+1,3r+2)` and `P_(2r+1)=(3r+3,3r+3)`.
This successful family alternates distinct and repeated A parts.

Compare `E(t,s)=(0,2,(),(t,t+s))`,t,s>=0, of weight `12+6t+3s`.
**Proved, author argument, separate review pending:** every E(t,s) is
uncovered by this baseline. L1 is unavailable. L3 removes precisely s,
giving equal nu entries t,t. L6 then removes t from both, leaving the
nonempty root `(0,2,(),(0,0))`. The counts are `(0,s,t)` and no extra
predecessor exists. Its conditional literal A expression is
`P_t` followed by `P_(t+s+2)`; these atoms satisfy all gap conditions.
It is distinct iff both t and s are even, and repeated otherwise. Indeed
an odd pair level repeats its two parts, while two different pair atoms
have separated parts. The smallest repeated missing member is t=0,s=1,
A=(1,2,6,6), weight15; t=s=0 is the distinct missing core at12.

The proposed **unexecuted clue** is to seek an intrinsic U representation
of this two-pair root, starting with exposed U=(9,3) of equal weight12;
any extension must expose a recoverable branch when it meets the first
comparison's seed chains. No such new root operation was implemented or
accepted. The smallest falsifier of claiming this alone covers the missing
objects is U=(8) or C(2,0), already at8. The complement includes mixed a,b,
higher a, all other F roots and every required global inverse/coverage case.

These are at most two family comparisons, not an overlay with old RR003
assignments. Exact seed proposals are not universal parsers and have not
consumed construction-pilot slots in this census stage.

## Failures, assurance and resource boundary

No census command failed and no case was silently discarded from a claimed
domain. Missing objects/roots stay explicitly unassigned in every table.
No new U–C construction rule was run. The universal normal-form result is
inherited only with its recorded RR005 separate informal review; the new
grammar/family arguments initially have author-only assurance; finite row
counts are empirical exact computation; A/B transported coverage is
conditional. None is a formal certificate or novelty audit.

Prior failures remain unchanged: all16 RR002 normalizations; RR003 overlap,
lost-phase and seed-capacity failures and later author-only dependencies;
RR004's fixed adjacent-height charge obstruction; and RR005's reviewed P/Q
collision at weight30 with common weight38 image. The latter was read
symbolically only, never newly executed above30. Closed ledgers/reviews were
not reset. The finite check is discovery exposure throughout.

Reproduction, only with a fresh authorized RR006 ledger:

```sh
python3 -B .runs/rr006/meter.py census-freeze census 5 0 -- python3 -B .runs/rr006/census-freeze-prep.py
python3 -B .runs/rr006/meter.py census-pilot12 census 15 12 -- python3 -B .runs/rr006/census.py 12
# Root approved unchanged extension only after the passing frozen pilot.
python3 -B .runs/rr006/meter.py census-extend30 census 30 30 -- python3 -B .runs/rr006/census.py 30
python3 -B .runs/rr006/meter.py census-format30 census 10 30 -- python3 -B .runs/rr006/census-report.py
```

Receipts, all under fresh `.runs/rr006/`: census-freeze0.039422458s;
census-pilot12 0.126038625s; census-extend30 0.829612708s;
census-format30 0.063098625s. Total metered census child time1.058172416s
of150s; maximum child RSS52,576,256bytes. Peak memory is post-exit RSS,
not a hard transient guarantee; local computation was serialized by the
fresh lock. Census stage dispatch costs3 proxy units. File-read utility
wall time was approximately8seconds, no failed utility commands; the root's
separate conservative maintenance charge covers it. Model tokens/runtime
and model memory are unavailable/unknown. No dependencies, paid providers,
web retrieval, external messages, publication, Git mutation or nested agent.

## Exact tables

The rows below were formatted from the frozen successful through30 census.
For A/B distinctness tables, entries are `total/covered` (not a fraction
claiming total is the numerator). Coverage remains conditional as above.

### U: exact-weight and cumulative denominators

| N | Total | Covered | Missing | Cumulative total | Cumulative covered | Cumulative missing | Cumulative coverage |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | 1 | 1 | 0 | 1 | 1 | 0 | 1/1 = 100.00% |
| 1 | 1 | 1 | 0 | 2 | 2 | 0 | 2/2 = 100.00% |
| 2 | 1 | 1 | 0 | 3 | 3 | 0 | 3/3 = 100.00% |
| 3 | 2 | 2 | 0 | 5 | 5 | 0 | 5/5 = 100.00% |
| 4 | 2 | 2 | 0 | 7 | 7 | 0 | 7/7 = 100.00% |
| 5 | 2 | 2 | 0 | 9 | 9 | 0 | 9/9 = 100.00% |
| 6 | 4 | 4 | 0 | 13 | 13 | 0 | 13/13 = 100.00% |
| 7 | 4 | 4 | 0 | 17 | 17 | 0 | 17/17 = 100.00% |
| 8 | 5 | 4 | 1 | 22 | 21 | 1 | 21/22 = 95.45% |
| 9 | 7 | 6 | 1 | 29 | 27 | 2 | 27/29 = 93.10% |
| 10 | 8 | 6 | 2 | 37 | 33 | 4 | 33/37 = 89.19% |
| 11 | 9 | 6 | 3 | 46 | 39 | 7 | 39/46 = 84.78% |
| 12 | 13 | 9 | 4 | 59 | 48 | 11 | 48/59 = 81.36% |
| 13 | 14 | 9 | 5 | 73 | 57 | 16 | 57/73 = 78.08% |
| 14 | 16 | 9 | 7 | 89 | 66 | 23 | 66/89 = 74.16% |
| 15 | 21 | 12 | 9 | 110 | 78 | 32 | 78/110 = 70.91% |
| 16 | 24 | 12 | 12 | 134 | 90 | 44 | 90/134 = 67.16% |
| 17 | 27 | 12 | 15 | 161 | 102 | 59 | 102/161 = 63.35% |
| 18 | 35 | 16 | 19 | 196 | 118 | 78 | 118/196 = 60.20% |
| 19 | 39 | 16 | 23 | 235 | 134 | 101 | 134/235 = 57.02% |
| 20 | 45 | 16 | 29 | 280 | 150 | 130 | 150/280 = 53.57% |
| 21 | 55 | 20 | 35 | 335 | 170 | 165 | 170/335 = 50.75% |
| 22 | 62 | 20 | 42 | 397 | 190 | 207 | 190/397 = 47.86% |
| 23 | 70 | 20 | 50 | 467 | 210 | 257 | 210/467 = 44.97% |
| 24 | 86 | 25 | 61 | 553 | 235 | 318 | 235/553 = 42.50% |
| 25 | 96 | 25 | 71 | 649 | 260 | 389 | 260/649 = 40.06% |
| 26 | 109 | 25 | 84 | 758 | 285 | 473 | 285/758 = 37.60% |
| 27 | 130 | 30 | 100 | 888 | 315 | 573 | 315/888 = 35.47% |
| 28 | 146 | 30 | 116 | 1034 | 345 | 689 | 345/1034 = 33.37% |
| 29 | 164 | 30 | 134 | 1198 | 375 | 823 | 375/1198 = 31.30% |
| 30 | 195 | 36 | 159 | 1393 | 411 | 982 | 411/1393 = 29.50% |

### C: exact-weight and cumulative denominators

| N | Total | Covered | Missing | Cumulative total | Cumulative covered | Cumulative missing | Cumulative coverage |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | 1 | 1 | 0 | 1 | 1 | 0 | 1/1 = 100.00% |
| 1 | 1 | 1 | 0 | 2 | 2 | 0 | 2/2 = 100.00% |
| 2 | 1 | 1 | 0 | 3 | 3 | 0 | 3/3 = 100.00% |
| 3 | 2 | 2 | 0 | 5 | 5 | 0 | 5/5 = 100.00% |
| 4 | 2 | 2 | 0 | 7 | 7 | 0 | 7/7 = 100.00% |
| 5 | 2 | 2 | 0 | 9 | 9 | 0 | 9/9 = 100.00% |
| 6 | 4 | 4 | 0 | 13 | 13 | 0 | 13/13 = 100.00% |
| 7 | 4 | 4 | 0 | 17 | 17 | 0 | 17/17 = 100.00% |
| 8 | 5 | 4 | 1 | 22 | 21 | 1 | 21/22 = 95.45% |
| 9 | 7 | 6 | 1 | 29 | 27 | 2 | 27/29 = 93.10% |
| 10 | 8 | 6 | 2 | 37 | 33 | 4 | 33/37 = 89.19% |
| 11 | 9 | 6 | 3 | 46 | 39 | 7 | 39/46 = 84.78% |
| 12 | 13 | 9 | 4 | 59 | 48 | 11 | 48/59 = 81.36% |
| 13 | 14 | 9 | 5 | 73 | 57 | 16 | 57/73 = 78.08% |
| 14 | 16 | 9 | 7 | 89 | 66 | 23 | 66/89 = 74.16% |
| 15 | 21 | 12 | 9 | 110 | 78 | 32 | 78/110 = 70.91% |
| 16 | 24 | 12 | 12 | 134 | 90 | 44 | 90/134 = 67.16% |
| 17 | 27 | 12 | 15 | 161 | 102 | 59 | 102/161 = 63.35% |
| 18 | 35 | 16 | 19 | 196 | 118 | 78 | 118/196 = 60.20% |
| 19 | 39 | 16 | 23 | 235 | 134 | 101 | 134/235 = 57.02% |
| 20 | 45 | 16 | 29 | 280 | 150 | 130 | 150/280 = 53.57% |
| 21 | 55 | 20 | 35 | 335 | 170 | 165 | 170/335 = 50.75% |
| 22 | 62 | 20 | 42 | 397 | 190 | 207 | 190/397 = 47.86% |
| 23 | 70 | 20 | 50 | 467 | 210 | 257 | 210/467 = 44.97% |
| 24 | 86 | 25 | 61 | 553 | 235 | 318 | 235/553 = 42.50% |
| 25 | 96 | 25 | 71 | 649 | 260 | 389 | 260/649 = 40.06% |
| 26 | 109 | 25 | 84 | 758 | 285 | 473 | 285/758 = 37.60% |
| 27 | 130 | 30 | 100 | 888 | 315 | 573 | 315/888 = 35.47% |
| 28 | 146 | 30 | 116 | 1034 | 345 | 689 | 345/1034 = 33.37% |
| 29 | 164 | 30 | 134 | 1198 | 375 | 823 | 375/1198 = 31.30% |
| 30 | 195 | 36 | 159 | 1393 | 411 | 982 | 411/1393 = 29.50% |

### F_U: exact-weight and cumulative denominators

| N | Total | Covered | Missing | Cumulative total | Cumulative covered | Cumulative missing | Cumulative coverage |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | 1 | 1 | 0 | 1 | 1 | 0 | 1/1 = 100.00% |
| 1 | 0 | 0 | 0 | 1 | 1 | 0 | 1/1 = 100.00% |
| 2 | 0 | 0 | 0 | 1 | 1 | 0 | 1/1 = 100.00% |
| 3 | 0 | 0 | 0 | 1 | 1 | 0 | 1/1 = 100.00% |
| 4 | 0 | 0 | 0 | 1 | 1 | 0 | 1/1 = 100.00% |
| 5 | 0 | 0 | 0 | 1 | 1 | 0 | 1/1 = 100.00% |
| 6 | 0 | 0 | 0 | 1 | 1 | 0 | 1/1 = 100.00% |
| 7 | 0 | 0 | 0 | 1 | 1 | 0 | 1/1 = 100.00% |
| 8 | 1 | 0 | 1 | 2 | 1 | 1 | 1/2 = 50.00% |
| 9 | 0 | 0 | 0 | 2 | 1 | 1 | 1/2 = 50.00% |
| 10 | 1 | 0 | 1 | 3 | 1 | 2 | 1/3 = 33.33% |
| 11 | 0 | 0 | 0 | 3 | 1 | 2 | 1/3 = 33.33% |
| 12 | 1 | 0 | 1 | 4 | 1 | 3 | 1/4 = 25.00% |
| 13 | 0 | 0 | 0 | 4 | 1 | 3 | 1/4 = 25.00% |
| 14 | 0 | 0 | 0 | 4 | 1 | 3 | 1/4 = 25.00% |
| 15 | 1 | 0 | 1 | 5 | 1 | 4 | 1/5 = 20.00% |
| 16 | 1 | 0 | 1 | 6 | 1 | 5 | 1/6 = 16.67% |
| 17 | 1 | 0 | 1 | 7 | 1 | 6 | 1/7 = 14.29% |
| 18 | 1 | 0 | 1 | 8 | 1 | 7 | 1/8 = 12.50% |
| 19 | 1 | 0 | 1 | 9 | 1 | 8 | 1/9 = 11.11% |
| 20 | 2 | 0 | 2 | 11 | 1 | 10 | 1/11 = 9.09% |
| 21 | 1 | 0 | 1 | 12 | 1 | 11 | 1/12 = 8.33% |
| 22 | 1 | 0 | 1 | 13 | 1 | 12 | 1/13 = 7.69% |
| 23 | 1 | 0 | 1 | 14 | 1 | 13 | 1/14 = 7.14% |
| 24 | 3 | 0 | 3 | 17 | 1 | 16 | 1/17 = 5.88% |
| 25 | 2 | 0 | 2 | 19 | 1 | 18 | 1/19 = 5.26% |
| 26 | 2 | 0 | 2 | 21 | 1 | 20 | 1/21 = 4.76% |
| 27 | 3 | 0 | 3 | 24 | 1 | 23 | 1/24 = 4.17% |
| 28 | 3 | 0 | 3 | 27 | 1 | 26 | 1/27 = 3.70% |
| 29 | 3 | 0 | 3 | 30 | 1 | 29 | 1/30 = 3.33% |
| 30 | 4 | 0 | 4 | 34 | 1 | 33 | 1/34 = 2.94% |

### F_C: exact-weight and cumulative denominators

| N | Total | Covered | Missing | Cumulative total | Cumulative covered | Cumulative missing | Cumulative coverage |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | 1 | 1 | 0 | 1 | 1 | 0 | 1/1 = 100.00% |
| 1 | 0 | 0 | 0 | 1 | 1 | 0 | 1/1 = 100.00% |
| 2 | 0 | 0 | 0 | 1 | 1 | 0 | 1/1 = 100.00% |
| 3 | 0 | 0 | 0 | 1 | 1 | 0 | 1/1 = 100.00% |
| 4 | 0 | 0 | 0 | 1 | 1 | 0 | 1/1 = 100.00% |
| 5 | 0 | 0 | 0 | 1 | 1 | 0 | 1/1 = 100.00% |
| 6 | 0 | 0 | 0 | 1 | 1 | 0 | 1/1 = 100.00% |
| 7 | 0 | 0 | 0 | 1 | 1 | 0 | 1/1 = 100.00% |
| 8 | 1 | 0 | 1 | 2 | 1 | 1 | 1/2 = 50.00% |
| 9 | 0 | 0 | 0 | 2 | 1 | 1 | 1/2 = 50.00% |
| 10 | 1 | 0 | 1 | 3 | 1 | 2 | 1/3 = 33.33% |
| 11 | 0 | 0 | 0 | 3 | 1 | 2 | 1/3 = 33.33% |
| 12 | 1 | 0 | 1 | 4 | 1 | 3 | 1/4 = 25.00% |
| 13 | 0 | 0 | 0 | 4 | 1 | 3 | 1/4 = 25.00% |
| 14 | 0 | 0 | 0 | 4 | 1 | 3 | 1/4 = 25.00% |
| 15 | 1 | 0 | 1 | 5 | 1 | 4 | 1/5 = 20.00% |
| 16 | 1 | 0 | 1 | 6 | 1 | 5 | 1/6 = 16.67% |
| 17 | 1 | 0 | 1 | 7 | 1 | 6 | 1/7 = 14.29% |
| 18 | 1 | 0 | 1 | 8 | 1 | 7 | 1/8 = 12.50% |
| 19 | 1 | 0 | 1 | 9 | 1 | 8 | 1/9 = 11.11% |
| 20 | 2 | 0 | 2 | 11 | 1 | 10 | 1/11 = 9.09% |
| 21 | 1 | 0 | 1 | 12 | 1 | 11 | 1/12 = 8.33% |
| 22 | 1 | 0 | 1 | 13 | 1 | 12 | 1/13 = 7.69% |
| 23 | 1 | 0 | 1 | 14 | 1 | 13 | 1/14 = 7.14% |
| 24 | 3 | 0 | 3 | 17 | 1 | 16 | 1/17 = 5.88% |
| 25 | 2 | 0 | 2 | 19 | 1 | 18 | 1/19 = 5.26% |
| 26 | 2 | 0 | 2 | 21 | 1 | 20 | 1/21 = 4.76% |
| 27 | 3 | 0 | 3 | 24 | 1 | 23 | 1/24 = 4.17% |
| 28 | 3 | 0 | 3 | 27 | 1 | 26 | 1/27 = 3.70% |
| 29 | 3 | 0 | 3 | 30 | 1 | 29 | 1/30 = 3.33% |
| 30 | 4 | 0 | 4 | 34 | 1 | 33 | 1/34 = 2.94% |

### Side-specific distinct/repeated refinements, weights0..30

| Side and predicate | Total | Covered | Missing | Coverage |
| --- | ---: | ---: | ---: | ---: |
| U: Repeated columns | 1297 | 403 | 894 | 403/1297 = 31.07% |
| U: Distinct columns | 96 | 8 | 88 | 8/96 = 8.33% |
| C: No within-vector increment repetition | 926 | 301 | 625 | 301/926 = 32.51% |
| C: Repeated increments within mu or nu | 467 | 110 | 357 | 110/467 = 23.55% |
| A: Repeated parts | 164 | 50 | 114 | 50/164 = 30.49% |
| A: Distinct parts | 1229 | 361 | 868 | 361/1229 = 29.37% |
| B: Repeated parts | 1266 | 403 | 863 | 403/1266 = 31.83% |
| B: Distinct parts | 127 | 8 | 119 | 8/127 = 6.30% |
| F_U: Repeated root columns | 14 | 0 | 14 | 0/14 = 0.00% |
| F_U: Distinct root columns | 20 | 1 | 19 | 1/20 = 5.00% |
| F_C: No within-vector root increment repetition | 1 | 1 | 0 | 1/1 = 100.00% |
| F_C: Repeated root increments | 33 | 0 | 33 | 0/33 = 0.00% |

### C disjoint a,b bins, weights0..30

| Bin | Total | Covered | Missing | Coverage |
| --- | ---: | ---: | ---: | ---: |
| a=0,b=0 | 1 | 1 | 0 | 1/1 = 100.00% |
| a=0,b=1 | 10 | 10 | 0 | 10/10 = 100.00% |
| a=0,b=2 | 16 | 0 | 16 | 0/16 = 0.00% |
| a=0,b=3 | 2 | 0 | 2 | 0/2 = 0.00% |
| a=1,b=0 | 30 | 30 | 0 | 30/30 = 100.00% |
| a=1,b=1 | 108 | 108 | 0 | 108/108 = 100.00% |
| a=1,b=2 | 39 | 0 | 39 | 0/39 = 0.00% |
| a=2,b=0 | 196 | 92 | 104 | 92/196 = 46.94% |
| a=2,b=1 | 237 | 0 | 237 | 0/237 = 0.00% |
| a=2,b=2 | 4 | 0 | 4 | 0/4 = 0.00% |
| a=3,b=0 | 406 | 170 | 236 | 170/406 = 41.87% |
| a=3,b=1 | 84 | 0 | 84 | 0/84 = 0.00% |
| a=4,b=0 | 241 | 0 | 241 | 0/241 = 0.00% |
| a=5,b=0 | 19 | 0 | 19 | 0/19 = 0.00% |

### A/B literal part distinctness by weight (transported coverage conditional)

| N | A distinct total/covered | A repeated total/covered | B distinct total/covered | B repeated total/covered |
| ---: | ---: | ---: | ---: | ---: |
| 0 | 1/1 | 0/0 | 1/1 | 0/0 |
| 1 | 1/1 | 0/0 | 1/1 | 0/0 |
| 2 | 1/1 | 0/0 | 0/0 | 1/1 |
| 3 | 2/2 | 0/0 | 1/1 | 1/1 |
| 4 | 2/2 | 0/0 | 1/1 | 1/1 |
| 5 | 2/2 | 0/0 | 0/0 | 2/2 |
| 6 | 3/3 | 1/1 | 1/1 | 3/3 |
| 7 | 4/4 | 0/0 | 1/1 | 3/3 |
| 8 | 5/4 | 0/0 | 1/0 | 4/4 |
| 9 | 7/6 | 0/0 | 2/1 | 5/5 |
| 10 | 8/6 | 0/0 | 2/1 | 6/5 |
| 11 | 9/6 | 0/0 | 2/0 | 7/6 |
| 12 | 11/7 | 2/2 | 2/0 | 11/9 |
| 13 | 12/7 | 2/2 | 2/0 | 12/9 |
| 14 | 14/7 | 2/2 | 2/0 | 14/9 |
| 15 | 18/10 | 3/2 | 3/0 | 18/12 |
| 16 | 22/11 | 2/1 | 3/0 | 21/12 |
| 17 | 26/11 | 1/1 | 3/0 | 24/12 |
| 18 | 32/14 | 3/2 | 5/0 | 30/16 |
| 19 | 37/14 | 2/2 | 5/0 | 34/16 |
| 20 | 42/14 | 3/2 | 4/0 | 41/16 |
| 21 | 49/17 | 6/3 | 6/0 | 49/20 |
| 22 | 55/17 | 7/3 | 6/0 | 56/20 |
| 23 | 62/17 | 8/3 | 5/0 | 65/20 |
| 24 | 72/21 | 14/4 | 7/0 | 79/25 |
| 25 | 82/22 | 14/3 | 8/0 | 88/25 |
| 26 | 94/22 | 15/3 | 8/0 | 101/25 |
| 27 | 111/27 | 19/3 | 10/0 | 120/30 |
| 28 | 128/27 | 18/3 | 11/0 | 135/30 |
| 29 | 147/27 | 17/3 | 11/0 | 153/30 |
| 30 | 170/31 | 25/5 | 13/0 | 182/36 |
