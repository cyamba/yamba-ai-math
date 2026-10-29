# RR007 Fleet B construction notebook and author handoff

Status: construction-stage handoff,24 October2026 at21:14:53 UTC.
**Full KR1 is unresolved.**
The primary-source handoff is frozen separately in `sources.md`; this file
adds constructions and obstructions and does not upgrade that handoff's
inspection or assurance. All new proofs below have **author-only, ordinary
written-argument assurance**, pending the distinct B critic. No novelty or
formal certification is asserted.

## Theorem candidate B1: a canonical degree-two carrier for the entire U domain

**Proved, author-only.** Let G={0,1,2,3,4}, ground 0, and
e(i,j)=1 if i<j, otherwise 0. Set alpha=(0,1,3,6,8).
Write a primary colored part as (k,i), with literal weight
`9*k+alpha[i]`. A secondary part is `(k;i,j)`, whose raw size is
`n=2*k+e(i,j)` and whose two primary halves are `(k+e(i,j),i)` and `(k,j)`.
Its literal weight is `9*n+alpha[i]+alpha[j]`.

The exact source interface is Konan, arXiv:2002.00300v2, Definitions 2.4,
2.9 and 2.11 and Theorem 2.13. The additional two opens inspected these
definitions and the theorem statement, **not its section-5 proof or executable
algorithm**. In our notation, put

`E(ij,lm)=e(i,j)+2*e(j,l)+e(l,m)`.

The degree-two flat domain F2 consists of secondary sequences ending in
`(0;0,0)`, with no preceding identical terminal secondary, and adjacent raw
size differences exactly E. Define U literally as positive descending decoded
heights, all drops including the drop to zero in 0..4, with weight sum F(h),
`F(5*k+r)=9*k+alpha[r]`.

**Forward U -> F2.** Replace each h by its unique `(floor(h/5),h mod5)`
and append terminal `(0,0)`. Let m be this primary list's length. Append
one additional `(0,0)` if m is odd and two if m is even. Pair from the
left. Each pair is a secondary part; its lower size is its k coordinate.
The last pair is exactly `(0;0,0)`.

**Inverse F2 -> U.** Expand every secondary into its two primary halves.
Remove the entire final block of `(0,0)` except one copy. Remove that
remaining terminal copy and decode every other primary as h=5*k+r.

**Intrinsic image and validity.** A U drop in 0..4 is equivalent to
`k-k_next=e(r,r_next)`. In particular its final positive height is in1..4,
so the last nonterminal primary has nonzero residue and size zero. Every
adjacent pair of primaries therefore satisfies the flat equality. For
consecutive secondaries, adding their internal and twice their boundary
primary differences gives exactly E; hence the output lies in F2.
The only added primaries are zeros of the ground color, so no preceding
secondary can be `(0;0,0)`.

Conversely, the secondary parity condition and the E equality imply that
the lower half of one secondary minus the upper half of the next is
`e(j,l)`. Thus unfolding gives a primary flat sequence. All primary sizes
are nonnegative: its final size is zero and all preceding differences are
nonnegative. A primary ground-colored zero cannot precede a nonground
primary: e(0,c)=1 would force the latter size to be negative. All such
zeros are consequently in a final block. That block has exactly two or
three copies: at least two come from the terminal secondary, and four or
more would give a forbidden preceding `(0;0,0)`. After trimming, the
nonterminal primaries decode to positive heights, with every drop in0..4.
This proves the exact full image, including the terminal and zero cases.

**Both identities.** Unfolding reverses pairing on each part. Trimming
leaves the original primary list. In the reverse direction, a trimmed list
has one terminal ground zero; parity uniquely restores a total of two or
three trailing ground zeros. The expanded original F2 list had even
length and exactly that block length, so pairing restores every original
secondary. Empty U maps to the sole terminal secondary and back.

**Weight and termination.** The sum of two primary literal weights is the
secondary literal weight by definition. Ground-colored zero padding has
weight zero. Thus the map preserves exactly the KR1 U weight. Both maps
make one pass through finite lists; no other objects, ranks, saved traces
or free colors are consulted. The source theorem's hypotheses hold:
e(0,0)=0, e(0,c)=1 and e(c,0)=0 for c!=0.

This constructs a complete intrinsic finite-color **carrier of U**, not
a C encoding. Konan's stated degree-two correspondence carries F2 to R2
with the same raw total and nonground primary word, so the specialization
above would preserve the literal weight. That import alone supplies no
R2 -> C/A parser, and we have not claimed an implementation or a separate
audit of the generic degree-two algorithm.

**Subsequent source-interface hold,21:11 UTC:** the stated import above
must not be treated as a verified usable bijection. The displayed R2
correction conflicts atweight11 with its section5 parity embedding under
these hypotheses. See `source-interface-addendum.md` and frozen B3 for
the exact witness and the separately named author domain R2star. B1's
U/F2 construction and proof do not use the disputed correction.

## The exact R2 predicate and first parser obstruction

For reproducibility, write the source's correction D(ij,lm) as zero except
the following mutually applicable cases (the displayed conditions are
disjoint for this ground):

* if j=0, l=0, i,m!=0, set D=e(i,m);
* if i=0 and j,l,m!=0 and e(j,l)=1, set D=-1;
* if j=0 and i,l,m!=0 and e(i,l)=0, set D=-1;
* if m=0 and j,l!=0 and e(j,l)=0, set D=1;
* if l=0 and i,j,m!=0 and e(j,m)=1, set D=1.

Set `Ereg=E+2*D`. R2 consists of secondary parts ending in `(0;0,0)`,
with all nonterminal colors different from00, and adjacent raw-size
differences at least Ereg. The parity of each raw size must be e(i,j).
For the terminal comparison Ereg(ij,00)=e(i,j); thus all lower sizes k
are nonnegative, and all nonterminal literal weights are positive.

**Refuted: literal partwise uncoloring.** The natural proposed forward
operation “replace each secondary by its literal weight and sort” does
not map all R2 to A. The valid R2 object consisting of two raw-size-zero
parts in color11 has Ereg(11,11)=0 and Ereg(11,00)=0. Its two literal
weights are2,2. The A adjacent-pair rule fails, since4 is not divisible
by3. This is a symbolic weight4 counterexample, not a finite match.

Nor can the inverse repair this only by choosing another color for each
unchanged A part: the valid A=(1,3) has only possible individual R2 parts
`0_10` and `0_20`. In either order their Ereg is2, while the raw-size
difference is zero. The only individual encodings of positive weights1
and3 are those colors, as follows directly from the parity and the
nonnegative k bound. A=(5) has no single R2 part at all: colors34 have
alpha sum14 but odd raw size and minimum literal weight23; the complete
secondary residue list gives no other weight5 representative.

Thus the missing interface must split, fuse or redistribute literal
parts. Different colors at repeated literal weights (for example weight6
has colors30 and22) are only part of the issue; an unchanged-part color
selection cannot suffice. This obstruction does **not** refute a nonlocal
R2/A bijection, the degree-two theorem, or KR1.

## Ongoing candidate questions and preserved subfamily clue

The exact task still missing is an intrinsic R2 parser producing the C
coordinates with weight a^2+3ab+3b^2+sum(mu)+3sum(nu), and a complete inverse
whose image is all R2. We are testing interpretations against its literal
secondary parity, terminal convention and the obstruction above.

An elementary closed-family clue, **unexecuted and not a full parser**:
F_U contains every root `(8^m)`. The literal F_C grammar contains
R_0=empty, R_1=(2,0,(2,2),()), and for m>=2
R_m=(4,0,((2*m-4)^4),()). Their weights are8m. The grammar proves these
are roots, and the formulas recover m uniquely. Matching them and
transporting the reviewed1/3/6 strip counts would cover every U supported
on{1,3,6,8}. This is an artificial family assignment, not a canonical
solution of the full colored parser; no computation or extension of it
has run. It is retained as a precise symbolic partial clue, with no
claim that it solves the full C bridge or agrees with every older partial
assignment.

## Construction-stage handoff

The stronger precise restricted result replacing the preceding unexecuted
family clue is frozen B2: all B supported on1,3,6,8 correspond to its
explicit intrinsic C cone, including an unbounded a4 cone. See
`candidates/b2-low-four-parts.md` for every branch and both inverses. Its
pilot12 and root-approved unchanged extension30 passed. Through30 the
image contains680 of1393 C objects; this is a bounded coverage fact,
not a full bridge. The independent zero-energy secondary grammar in
`b2-zero-energy-corollary.md` composes with B2 to encode exactly that C
cone in R20. Its separate pilot12 passed. The disputed printed correction
never occurs in raw zero, so this corollary's predicate is unchanged.

B3 defines R2star and proves a complete intrinsic mixed-model M/R2star
interface, with exact parity recovery, image, weight and both inverses.
Its pilot12 has59 objects on each side, while the printed R2 has58.
This supports the recorded source-interface concern and does not replace
its distinct primary review. It also does not identify M/R2star with C.

The complete B mathematical handoff consists of:

1. Frozen B1: full U/F2 carrier, universal proof and pilot12.
2. Frozen B2: full low-four-part B/C-cone map, universal proof and
   authorized pilots12/30; its derived exact R20 word parser.
3. Frozen B3: full M/R2star parity interface, universal proof and pilot12;
   the source's printed R2 remains separately named and unaudited.
4. `failedideas.md`: physical mixed-slope obstruction, common-slope lemma,
   contextual splitting/fusion requirement and cross-fleet incompatibility.
5. `source-interface-addendum.md`: all extra source opens, exact printed
   formula, complete weight11 witness, and remaining critic retrieval.
6. `journal.md`: frozen trials, failed command and resource accounting.

The additional paper-only `positive-energy-obstruction.md` proves that
any injective extension of B2 must change the C particle count on every
positive-energy one-letter word; absorbing its energy into a single mu
entry necessarily collides with B2's raw-zero image. Its exact raw-total1
grammar is preserved without freezing an additional seed assignment.

The decisive unfilled requirement is a finite algorithm that recovers C
from **every positive-energy** F2 or R2star object and whose inverse has
that exact full image and Q weight. A composition cannot be asserted from
the separately complete carrier and parity interfaces. Generic source
existence statements,59-object pilot agreement, low-four-part parsing,
and a0/1 cross-fleet success do not supply that algorithm. In particular,
do not overlay B2 and Fleet A's a0/1 map: their B images collide at12.

For the distinct critic, first independently inspect Definition2.11
case(2.19), Theorem2.13 and the ground hypotheses using the one remaining
primary open; then audit the B3 comparison table, B1 terminal padding,
B2 inverse congruences and zero-energy uniqueness. Any upgrades should
be scoped to those precise subresults. Full KR1 remains unresolved.
