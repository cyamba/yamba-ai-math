# A3 frozen partial bijection: third single and a mixed boundary wall

Fleet A's third and final variant. This is an exact alternative partial
bijection extending A1 and A2, with author-only assurance pending the
reserved distinct critic. It is not a full KR1 parser. The construction
was derived with the independent context investigator; its full source
hook grammar remains a separate, one-sided representation.

## Exact C domain and forward map

Retain the frozen A1 map on all a=2,b=0, and A2 on all a in{0,1}. Add
exactly these two disjoint sectors:

* all a=3,b=0, writing `mu=(x,x+y,x+y+z)` with x,y,z>=0;
* all a=2,b>=1 with `mu=(0,s)`, every ascending nu and s>=0.

On the third-single sector use this disjoint table:

| C condition | U output |
| --- | --- |
| y=3m+1, m>=0 | `(8,6^m,3^(x+1),1^z)` |
| y=3m+2, m>=0 | `(10,6^m,3^(x+1),1^z)` |
| y=3m, x=0, m>=0 | `(6^(m+1),3,1^z)` |
| y=0, x>=1 | `(9,3^x,1^z)` |
| y=3m, m>=1, x>=1 | `(12,6^m,3^(x-1),1^z)` |

On the mixed wall form the positive ascending gap-two partition

`lambda=(1,3+nu_1,5+nu_2,...,2b+1+nu_b)`.

Output `3*lambda^T` together with exactly s+1 ones. Sorting is already
implicit in descending conjugation and the final one-string. This is a
formula on the input, not matching of seed lists.

## Intrinsic U image and inverse

The exact U image is the disjoint union of the frozen A1 image, frozen A2
image, the five displayed third-single U families with exactly their
displayed exponents/ranges, and this mixed-wall image:

U has at least one one, all other entries are multiples of three. Divide
those other entries by three to obtain V. Its maximum B is at least two;
every level 1,...,B occurs, its top multiplicity is exactly one, and each
lower multiplicity is at least two.

All predicates refer only to the actual U. For the wall inverse set
`b=B-1`, `s=(number of ones)-1`, conjugate V to ascending lambda, and put
`nu_j=lambda_(j+1)-(2j+1)`. Recover `a=2,mu=(0,s)`.

For the five third-single families the numerical marker identifies the
branch. Write t=#3, m=#6 and z=#1. With marker8 recover x=t-1,y=3m+1;
with marker10 recover x=t-1,y=3m+2; with marker12 recover x=t+1,y=3m;
with marker9 recover x=t,y=0. With only sixes, exactly one three and
optional ones recover x=0,y=3(m-1). Then recover the three mu entries.
There is exactly one marker in each marker branch. Existing A1/A2 use
their unchanged inverses. No external flag, free color or saved trace is
part of the output.

## Universal validity, weight, image and inverse arguments

**Proved, author-only.** The five third-single branches have distinct
intrinsic markers or six/three multiplicity patterns. Their decoded
heights are subsets respectively of `(4,3,2,1)`, `(6,3,2,1)`, `(3,2,1)`,
`(5,2,1)`, `(7,3,2,1)`. Required positive exponents supply every necessary
bridge, so every drop including the terminal lies in0..4. Their weights
are respectively

`8+6m+3(x+1)+z`, `10+6m+3(x+1)+z`,
`6(m+1)+3+z`, `9+3x+z`, `12+6m+3(x-1)+z`.

Substituting the branch condition makes each equal `9+3x+2y+z`, exactly
the C weight. Counting the indicated multiplicities recovers x,y,z and
the branch, proving both inverse identities and exact image coverage.

For the wall, lambda_1=1 and every subsequent difference is at least two.
Conjugation therefore yields top multiplicity one and every lower level
multiplicity at least two. Conversely those multiplicities give precisely
lambda_1=1 and the required differences, so recovered nu is nonnegative
ascending of exact length B-1. Conjugation twice restores lambda and V;
the one-count restores s, proving both inverse identities and exact image.
All consecutive multiples of three occur, so their decoded drops are at
most two, and the final ones give a valid terminal. The weight is

`3(b+1)^2+3sum(nu)+s+1 = Q(2,b)+s+3sum(nu)`.

Every algorithm scans finite vectors or performs finite conjugation;
termination is immediate. Literal validity includes zero increments and
all repeated cases. No statement identifies U distinctness with
within-vector increment distinctness.

The five third-single images are disjoint from A1: A1 has a three only
in its one-three/ones family without sixes or another marker. They are
disjoint from A2: markers8/10 are nonmultiples of three; the six-only
branch has exactly one three; the9 branch lacks6; the12 branch lacks9.
A2 requires all multiple-of-three levels through its maximum and at
least two threes whenever that maximum is at least6. The wall has at
least two threes and is therefore disjoint from A1; its positive ones
and top multiplicity one exclude A2, whose corresponding top
multiplicity must be at least two. It is disjoint from all five new
families by the same nonmultiple marker, missing-level or one-three
conditions. A1 and A2 were already disjoint. These are exhaustive
intrinsic disjointness arguments, not a finite no-collision observation.

## Complete one-hook coverage and the precise remaining gap

For numerical U define the three-modular support row length ceil(u/3),
and explicitly define its Durfee rank by

`D(U)=max({j>=1:u_j>3(j-1)} union {0})`.

This equals the number of successive remove-top-row/subtract-three hook
deletions. In particular all-one strings have rank one. Rank one means
at most one part exceeds three. Literal U then has top6,8,9 or10, with
all remaining parts3/1, or consists entirely of3/1. Top9 needs a lower
row; top10 needs at least one3. These constraints follow directly from
the terminal height and the gap at most four to a row of height at most
two. Thus the A1/A2 formulas plus the m=0 or y=0 third-single branches
and b=1 mixed wall cover every rank-one U, including empty at rank zero.
The exact table and its algebraic inverse appear in context.md. The full
A3 U image is larger than rank at most one, by its stated higher-rank
A1/A2, third-single and wall sectors. No equality of D with a particle
count is assumed; that proposed invariant was refuted symbolically.

The domain remains proper. A smallest missing C datum is
`(2,1,(1,1),(0))`, weight fifteen: it has positive first mu and is
neither A1, A2, a third-single object nor the zero-first-mu wall. Its
absence is a boundary of this map, not evidence of nonexistence of the
desired full bijection. The full nested-hook interacting separator,
including positive first mu with b>0 and a>=4, is not constructed.

A1/A2/A3 use an alternative partial assignment; the old full empty-F-root
normal-form map and Fleet B's different cone map cannot be overlaid.
The previously recorded weight13 independent-union collision remains
refuted; the wall avoids it by changing the contour. Novelty is unverified.

## Frozen test boundary

Named script `.runs/rr007/a3-hook-and-wall.py`. First pilot has every
actual input/output through12. It screens literal U/C, both inverse
identities, weight, exact domain/image, pairwise branch disjointness,
complete rank-at-most-one U coverage and separate distinct/repeated
cohorts. At12 the mixed wall (minimum13), the y=2 branch (minimum13)
and positive-m marker12 branch (minimum18) are unexercised. Even if all
59 objects through12 are covered, this cannot establish global coverage.
Only root can authorize an unchanged named-script extension through30
after that pilot passes. No new above30 trial is permitted.
