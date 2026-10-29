# Reserved sector refinement: H3

Status at freeze: **proved, author-only mathematical assurance**, with the
literal executable checks described below. A distinct final critic must review
this refinement. The previously reviewed H1/H2 claims and all initial frozen
files are preserved. Novelty is unverified. This is not a full KR1 solution.

## Scope and theorem

Write a literal cluster datum as `C=(a,b,mu,nu)`, with ascending, zero-padded
nonnegative riggings of lengths `a,b`. Its weight is
`Q(a,b)+sum(mu)+3sum(nu)`, where `Q=a²+3ab+3b²`.
For `a=4,b=0`, write uniquely

`mu=(x,x+t,x+t+y,x+t+y+z)`, `x,t,y,z>=0`.

Thus its weight is `16+4x+3t+2y+z`; in gap-digit notation
`(delta4,delta3,delta2,delta1)=(x,t,y,z)`.

Let D2 be the exact domain of the initial H2 in `author.md`: all `a<=2`,
all `a=3,b=0`, the two common-rigging planes at `(a,b)=(4,0),(5,0)`,
and every rigging at `a=3,b>=49`, `a=4,b>=65`, `a=5,b>=79`.
The new theorem defines a coherent weight-preserving bijection H3 from

`D3 = D2 union {a=4,b=0, y in {0,1} or y>=18}`

to an intrinsic explicitly recognized subset of literal U. It agrees exactly
with H2 on D2. The new domain leaves `2<=y<=17` open at `a=4,b=0`, with
`x,t,z` still unbounded. The requested all-b domains for `a=3,4,5` remain
open. No general recursive U lift is supplied by this theorem.

Literal U uses descending column weights `F(h)=9floor(h/5)+(0,1,3,6,8)[h mod5]`.
Every decoded height drop, including the last drop to zero, must be at most4.
The weights used here have heights
`1:1, 3:2, 6:3, 8:4, 9:5, 10:6, 12:7`.
Write `p^k` for k copies of p; an exponent zero omits that column. Every
displayed union is sorted in descending order. These formulas are direct
arithmetic maps, not matching or ranking of finite object lists.

## Two low-gap slabs and their carry

Put `x=2q+r`, `r in {0,1}`. For `y=0`, define S0 by:

| Condition | U |
| --- | --- |
| r=1 | `12,8^(q+1),3^t,1^z` |
| r=0,t<=2 | `8^(q+2),3^t,1^z` |
| r=0,t>=3 | `12,10,8^q,3^(t-2),1^z` |

At `t=0` these are exactly the old a4 common-rigging plane. The third row
is necessary: appending arbitrary threes to the second row collides with
the auxiliary injection g at weight25. The preserved first falsifier is
`C=(4,0,(0,3,3,3),())`, naive `U=(8,8,3,3,3)`; its other g-source is
`(2,1,(6,6),(0,))`. The carry replaces it with `(12,10,3)`.
This refutes the naive append-threes rule, not the retained carried rule.

For `y=1`, define S1 by:

| Condition | U |
| --- | --- |
| r=1 | `12,9,8^q,3^t,1^(z+1)` |
| r=0,t<=2 | `10,8^(q+1),3^t,1^z` |
| r=0,t>=3 | `12,9,8^q,6,3^(t-3),1^z` |

The initial coordinator suggestion was the `t=0` part of S1, initially
unverified. In particular `(10,8,1^z)` is an auxiliary g3 image, so
disjointness from g cannot prove disjointness from H1. The target-component
argument below resolves this for every z, including mandatory-one contexts.

All six rows are literal U. Repeated columns give zero drops. In S0, the
largest possible nontrivial jumps are `12->8` (7 to4), `10->3` (6 to2),
and the terminal `8->0` (4 to0); adding optional intermediate columns
subdivides these jumps. For odd S1, `12->9` is 7 to5, and without any
8 or3 the mandatory one makes `9->1` a drop4. For even small S1,
`10->8` drops2 and the 8 terminal drop is4. For even large S1,
`12->9->6` has drops2,2, and terminal6 has height3. The optional 8,
3 and1 again subdivide valid drops. These checks include all empty-tail
and zero-parameter cases.

The S0 weights are respectively
`20+8q+3t+z`, `16+8q+3t+z`, and
`22+8q+3(t-2)+z=16+8q+3t+z`.
They equal `16+4x+3t+z` in their indicated parity.
The S1 weights are `22+8q+3t+z`, `18+8q+3t+z`, and
`27+8q+3(t-3)+z=18+8q+3t+z`.
They equal `18+4x+3t+z` in their indicated parity.

Here are exact intrinsic image languages, with `n[p]` the multiplicity of p
and S the support. Every unlisted column is forbidden. Inverse parameters
`(x,t,z)` determine `mu=(x,x+t,x+t+y,x+t+y+z)`.

| Language | Conditions | Inverse `(x,t,z)` |
| --- | --- | --- |
| S0 odd | `S<={12,8,3,1}; n12=1,n8>=1` | `(2(n8-1)+1,n3,n1)` |
| S0 even small | `S<={8,3,1}; n8>=2,n3<=2` | `(2(n8-2),n3,n1)` |
| S0 even carry | `S<={12,10,8,3,1}; n12=n10=1,n3>=1` | `(2n8,n3+2,n1)` |
| S1 odd | `S<={12,9,8,3,1}; n12=n9=1,n1>=1` | `(2n8+1,n3,n1-1)` |
| S1 even small | `S<={10,8,3,1}; n10=1,n8>=1,n3<=2` | `(2(n8-1),n3,n1)` |
| S1 even carry | `S<={12,9,8,6,3,1}; n12=n9=n6=1` | `(2n8,n3+3,n1)` |

The required support and the occurrences of 12,10,9,6 distinguish these
six languages. The table proves both inverses by substitution, including
all row boundaries `t=2/3`. Inverses terminate after finitely many counts
and integer arithmetic operations, with no parameter-dependent search.

## Disjointness from the retained H1

This paragraph records the support consequences of the pinned old formulas
actually used in `bridge.py`; these are inspected algebraic facts about the
maps, not evidence from a finite census. Write f1 for the retained partial
injection and `g=g2 union g3` for the separate auxiliary injections.
An H1 output is always a final f1 or g value along its reversible splice.
However, the converse is false: some auxiliary g values lie in target-only
components rejected by the H1 inverse.

The old f1 formulas in `critic-a-literal.py` and the corrected a2,b1
formulas in `bridge.py` have these consequences:

* An 8 or10 in an isolated-marker f1 language occurs exactly once and
  cannot coexist with the other marker or12. A retained third-12 image
  has exactly one12, at least one6, and no8,9,10.
* The marker-free full-contour languages contain each lower multiple of3
  below the top at least twice. The wall variant also has this complete
  lower contour. Hence a top12 in these languages requires 3,6,9.
* Every corrected a2,b1 image with positive common parameter has9 and
  no12; the zero-common branch has6, at least two3s and mandatory ones.

The inspected `rr003_columns.py`, `rr003_revision.py`, `rr003_a2.py`
formulas give all possibilities for g2:

* A marker-free full contour has all lower multiples of3 at least twice.
  Its only missing-penultimate variant has a singleton top and all lower
  levels before the hole at least twice.
* The b=0 carrier languages have either one8 with6s/ones; or one9 with
  6s and mandatory ones; or one9, exactly one3, and6s/ones. They have no12.
* Mixed 8/10 languages have all multiples `3,...,3b`, at least two at
  each lower level and at least three at the top. The multiplicity of10
  is bounded by3. With top3 they require at least three3s.
* The marker-free hole at b1 has one9, one6, at least two3s and no12.
  The small10-hole templates have at least two6s, at most one3 and
  mandatory ones; they have no8 or12. The other hole templates carry
  17,19 or26. In particular none of these can silently add12 or8 as a
  free residual column.

The repaired g3 formulas have support contained in `{10,9,8,6,3,1}`,
so they never contain12. An image containing both10 and8 has exactly
one of each; if it has no6, it has at most one3. These facts exhaust
the recognition branches in the pinned implementations.

Now check the six new languages against these consequences. S0 odd has
12 and8 but lacks6 and9. S0 even carry has12 and10, also lacks6 and9;
the small10-hole templates are excluded by the absence of two6s and
by the extra12. Neither can be any f1 or g value. S0 even small has at
least two8s and at most two3s. Isolated-marker old branches permit
only one8, and the only mixed top3 contour would require three3s;
any larger top is absent. It too is outside both old images.

S1 odd has12 and9 and lacks6: full contours fail, the missing-penultimate
top12 pattern would have to omit9, and isolated12 forbids9. S1 even carry
has12,9,6 each once, so neither full lower multiplicities nor a singleton
top with the penultimate level missing can hold; if8 is present, the
mixed contour also fails its top and lower multiplicities. The old
marker-free b1 hole cannot accept the extra12. Other hole markers are
absent. These two languages are outside both f1 and g.

For S1 even small, f1 is excluded by the simultaneous10 and8. The g2
mixed language needs at least three3s, whereas this language has at most
two; carriers and hole templates also fail. Repaired g3 can meet this
language only when `q=0` and `t in {0,1}`. For `t=2` it is outside g3;
for `q>=1` its multiplicity of8 is too high. Thus these cases are also
outside both f1 and g.

It remains to prove rejection by H1 for the infinite exceptional language

`u=(10,8,3^t,1^z)`, `t in {0,1}`, `z>=0`.

The exact reverse path is

`g^-1(u)=(3,0,(t+1,t+4,t+4+z),())`,
`f1(g^-1(u))=v=(12,6,3^t,1^z)`.

The first source belongs to the retained f1 domain. The value v is
outside g3 because it contains12. It is outside every g2 language:
the full contour is missing9, the missing-penultimate top12 contour
would require at least two6s and two3s, and the observed counts are
one6 and at most one3. The marker-free b1 hole requires9; the b0
carriers and small10 holes cannot contain12; the other templates need
absent markers17,19,26. This reasoning does not depend on z. Therefore
the H1 reverse splice rejects u after this one retained source. This
proves universal rejection of the target-only language, rather than
mistaking its g3 membership for an H1 collision. Adding any number of
ones never repairs the missing contour or multiplicity conditions.

We have proved all new low-slab images are disjoint from H1. The overlap
at `y=0,t=0` is precisely the already retained H2 common plane and has
the identical map. For `y=0,t>=1`, the positive3 or carried12+10
distinguishes the old a4 plane; every y1 head is also distinct from
that plane. The old a5 common plane always has15 or17, absent here.
The H2 large-b coding images always have guard28, absent here. Thus
all genuinely new low-slab images are disjoint from the rest of H2.

## Uniform arithmetic head code for y>=18

This is a symbolic extension: its smallest source weight is52, and no
instance was numerically evaluated under the mandated bound40.

Put `y=6v+s`, `v>=3`, `0<=s<6`; retain `x=2q+r` and set `K=6r+s`.
Encode the twelve possible K values by a literal count pair `(A,B)`:

| K | A | B |
| --- | --- | --- |
| 0..5 | K | 0 |
| 6..9 | K-6 | 1 |
| 10..11 | K-10 | 2 |

Set `h=20+4r+2s-6A-10B` and define

`U=12^(v-1),10^B,8^(q+1),6^A,3^t,1^(z+h)`.

The mandatory-one amount is nonnegative for every bounded phase: it is
`20-4K` on K0..5, `38-4K` on K6..9, and `52-4K` on K10..11.
These formulas give minimum0,2,8 respectively. This finite phase code
stores bounded residues only; it is not a list of matched partitions.

There are at least two12s and at least one8. In decoded heights the
mandatory8 bridges top12 height7 to height4 with drop3; optional10
height6 subdivides that bridge. Optional6,3,1 have heights3,2,1;
without them the terminal8 drop is4. Hence every U condition holds,
including the terminal condition. The total weight is

`12(v-1)+10B+8(q+1)+6A+3t+z+h`
`=16+8q+4r+12v+2s+3t+z=16+4x+2y+3t+z`.

The exact intrinsic inverse language has support contained in
`{12,10,8,6,3,1}`, `n12>=2`, `n8>=1`, and admissible pair

`(B=0,0<=A<=5)` or `(B=1,0<=A<=3)` or `(B=2,0<=A<=1)`,

where `A=n6,B=n10`. Recover `K=A`, `A+6`, or `A+10` respectively;
then `r=K//6,s=K mod6`, `q=n8-1,v=n12+1,t=n3`.
Compute h by the same formula and require `n1>=h`. Put `z=n1-h`,
`x=2q+r,y=6v+s`, and recover the original mu. The three count-pair
intervals are disjoint, and substitution gives both inverses. The
algorithm is terminating finite arithmetic.

These high-gap targets have no9. Full old contours through12 therefore
fail. The old top12 missing-penultimate language has exactly one12,
whereas here there are at least two; all mixed old contours also
require the missing9. Other isolated-marker and small-hole templates
cannot contain this combination of multiple12s and8; the templates
with17,19,26 have absent compulsory markers. Repaired g3 never has12.
Consequently the new language is outside f1 and g, hence outside H1.
It has none of the15/17 or28 distinguishing the other H2 planes/tails.
It is disjoint from every new low slab because those have at most
one12. This proves the exact image, coherence, and both inverses for
the complete H3 domain, including this unexecuted high-gap portion.

## Versions, gates, resources and endpoint cohorts

This is the single reserved refinement within the existing head/marker
family, not a new general-candidate cycle. Version1 solved y0 and the
`t=0` slice of y1; version2 supplied the y1 carry for every t; version3
added the high-gap arithmetic code. All scripts, pretest definitions,
results and earlier failures are preserved. Each unchanged version ran
the sequential gates12,30,40 via the shared serialized meter. Definition
and script hashes in the outputs match each pretest pin. No KR input
or output above40 was executed, and no high-gap source was constructed.

The final retained implementation is `revision-v3-bridge.py`, importing
the unchanged v2 and v1 modules and then the unchanged H2/H1 dependencies.
Its checker enumerates all literal C and all independently generated
literal U at weights through the bound; it verifies validity, weight,
injectivity, source inverse, exhaustive target acceptance/rejection,
agreement with every H2 assignment, and the actual A and B endpoint
compositions. The special target-only components and the naive failure
are included explicitly. The high-gap theorem is checked by the
symbolic proof above, not by a hidden above-bound sample.

| Final gate | all C / all U | H3 mapped | rejected | H2 preserved |
| --- | ---: | ---: | ---: | ---: |
| 12 | 59 | 59 | 0 | 59 |
| 30 | 1393 | 1203 | 190 | 1092 |
| 40 | 5461 | 3498 | 1963 | 3014 |

At40, exactly484 assignments were added to H2:228 with `y=0,t>=1` and
256 with y1. The a4,b0 sector contributes575 accepted sources among
1292 literal sources in that sector through40. Version1 had3320 total
accepted through40; versions2 and3 both have3498, as the high-gap
extension starts at52. The first missing C is
`(4,0,(0,0,2,2),())`, weight20. The first rejected U is `(10,9,1)`,
also weight20. These are retained gaps, not covered by an implicit
completion of the map.

The distinct/repeated cohorts are literal endpoint partitions, not
rigging cohorts. Among all5461 sources through40, endpoint A has4684
distinct and777 repeated; endpoint B has325 distinct and5136 repeated.
On the H3-mapped denominator3498, A has2935 distinct and563 repeated;
B has92 distinct and3406 repeated. The endpoint maps are the pinned
cluster/gap and U/residue maps, and both inverse compositions and
weights were checked. These finite checks do not prove the requested
global sector result, novelty, or formal proof assurance.

The nine revision subprocesses all exited0; exact totals and peak memory
are in `revision-resource-use.json`. Initial phase-sector subprocess
costs remain in the separate immutable `resource-use.json`. No new
dependencies, external queries, messages, publication or push occurred.

## Remaining clues and smallest obligations

1. **Unimplemented finite-band funding design.** For `2<=y<=17`, one
   possible phase code is `K=16r+(y-2)`, `A=K mod6`, `B=3+K//6`.
   A tentative head `12^2,10^B,8^(q+1),6^A,3^t,1^(z+h)` would use
   `h=-16+4r+2y-6A-10B`, so a sufficiently large z could fund a
   negative h. Distinguishing it from the retained high-gap language
   would use B>=3, but its exact image and compatibility with all old
   languages have not been proved or executed. Further modes using
   count12=3 and consuming some threes, then count12=4 and consuming
   some eights, might bound t and q as well. This is a design only:
   it needs explicit priority, nonnegative counts, intrinsic inverses
   recovering the mode, pairwise image disjointness, and a demonstrated
   finite residual box. The smallest current uncovered source remains
   the weight20 datum above. One image collision or ambiguous mode
   decode refutes a proposed funding rule; finite absence of such a
   collision would not supply the missing universal argument.
2. **All-b lift obstruction.** The exact C reductions from the initial
   packet retain an extra pair-fusion weight `a-1` in
   `Q(a,b)-Q(a-2,b+1)`; this is2,3,4 for a3,a4,a5. A C-only
   reduction and a bounded phase do not yield a U insertion rule.
   The present thresholded marker tail uses that base energy only
   when b is large; it leaves all remaining low-b riggings unresolved.
   A useful next rule must preserve the complete lower contour and
   store its phase with an intrinsic inverse while respecting H1/H2.
3. **Carry mechanism.** Both low slabs change head when a free three
   count reaches3, and the failure is an exact overlap with the old
   mixed-marker contour. This suggests deriving carries from the old
   recognition languages before choosing a geometric interpretation.
   It is a clue toward a systematic Ferrers seam operation, not a
   proved multidimensional or all-sector construction.
