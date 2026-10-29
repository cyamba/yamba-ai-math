# RR005 round two: a global contextual six-strip

**Proposed proved extension; second separate review pending.** Depend on
the frozen, separately reviewed round-one chain theorem and literal U/C
definitions only. No RR003 author-only premise or counting identity.
Complete KR1 remains unresolved. Novelty status: NOT VERIFIED.

## 1. Exact E_U classification

Recall E_U consists of D_U objects with no triple predecessor. It is the
disjoint union of the following four types. Heights are decoded literally.

* A: no columns 1 or 3, including empty.
* B: one 1, with smallest other column 9.
* C0: exactly one 3, no 1 or 10, and smallest other column 9.
* C1: exactly one 3 and one 10, no 1, with the smallest height above 6
  equal to 10 (column 18); any intervening height 5 columns (9) are allowed.

For the cases with a 3, two copies permit ordinary removal, so there is
exactly one. Removal of that sole 3 fails precisely when the next height
is 5 or 6, by the valid drop bound to height two. If no 10 exists, the
next height is 5 and the special triple inverse is unavailable: C0.
If a 10 exists, replacing it by 9 and the 3 by 1 fails only when removing
the unique height 6 exposes a gap from height 10 to height 5. More than
one height 6 prevents that gap. With a unique height 6, its next higher
height is at most 10 by original validity, and replacement fails exactly
when it is 10. These are precisely C1. B is never a triple image. A has
no 3 and cannot have a triple predecessor. Thus this is exhaustive, not
an observed finite pattern.

## 2. R6_U and its intrinsic inverse

On the whole E_U define these four branch replacements, then sort:

    A:  append 6
    B:  (9,1)       -> (10,6)
    C0: (9,3)       -> (12,6)
    C1: (18,10,3)   -> (19,12,6).

Only one copy of each displayed column is replaced; all other multiplicities
are retained. Every branch adds exactly six. Outputs have no 1 or 3, so
they lie in E_U once literal validity is shown.

In A, adding height three subdivides a gap or extends an input whose bottom
height was <=4. In B, heights (5,1) become (6,3), with no gap exceeding four,
by the same insertion argument as round one. In C0, heights (5,2) become
(7,3). If the removed 5 was last at its level, its preceding height was at
most 9; inserting 7 preserves all upper gaps and the new bottom gap is
7-3=4. Additional height fives only subdivide this gap. In C1, (10,6,2)
becomes (11,7,3). There were no heights 7,8,9 between the unique 6 and
the first 10. A preceding height above the removed 10 was at most 14;
the new 11 keeps its gap <=3, or subdivides an existing gap. The gaps
11-7 and 7-3 are four, and any retained 10 or 5 subdivides them.
These arguments include repeated heights and the terminal zero.

Inverse L6_U: accept only an E_U object with no 1 or 3 and at least one 6.
Try the following fixed tests in order, accepting a reconstruction only
when it lies in the specified original E_U branch:

1. Remove a 6, accepting if literal U (type A).
2. Replace 10,6 by 9,1, accepting type B.
3. Replace 12,6 by 9,3, accepting type C0.
4. Replace 19,12,6 by 18,10,3, accepting type C1.

These are four arithmetic/membership tests, not a search or saved trace.
For B/C0/C1 images, the 6 is unique and every remaining height is >=5;
removing it fails terminal validity, separating them from A. B images
contain a 10; C0/C1 images contain none, separating B. In a C1 image,
undoing only C0 would remove its unique height 7 and put a 5 below a
remaining height at least 10, exposing a forbidden gap >=5. Thus C0 and
C1 images are disjoint. Each successful inverse test reconstructs exactly
its forward branch and multiplicities. This proves both inverse identities
on the images and total injectivity of R6_U on E_U.

## 3. R6_C on the entire E_C

The round-one inverse tests give the following E_C cases:

* empty;
* a=0,b>=2, final two nu entries equal;
* a=2,mu=(k,k),k>=1, any b, with the final nu equal to its predecessor
  when b>0 (predecessor zero when b=1);
* a>=3, final two mu entries equal, and: when b>0 the final nu equals
  its predecessor (zero if b=1); when b=0, a>=4 and mu[-3]=mu[-4].
  There are no b=0,a=3 roots.

Define R6_C: empty goes to (2,0,(1,1),()); on a=0,b>=2 raise the last
two nu entries by one; on a>=2 raise the last two mu entries by three.
These cases exhaust E_C, preserve its conditions and add six.

Their images are disjoint. Empty's image is a=2,b=0,k=1; the other
a=2 images have k>=4. On a>=3 the gap before the final equal pair of
mu entries is at least three. For a=0 the gap before the final equal
nu pair is positive, using zero before it when b=2.

L6_C reverses empty's image first. Otherwise lower the last two nu entries
by one exactly when a=0,b>=2 and their preceding gap is positive; lower
the last two mu entries by three exactly when a=2,k>=4, or a>=3 and
the preceding gap is at least three. Return no predecessor otherwise.
These conditions ensure sorted nonnegative exact-length vectors and
exactly reconstruct the input. Thus R6_C is total/injective on E_C,
with both inverse identities on its image.

## 4. Full three-stage normal forms and exact remaining task

Define F_U/F_C as E_U/E_C objects with no L6 predecessor. On either full
domain first perform the reviewed unit/triple strip, then L6 on the E
root. Strictly decreasing weight gives termination and unique

    (F root, n1, n3, n6),  |input|=|root|+n1+3*n3+6*n6.

Reconstruct in order R6, R3, R1. The partial-inverse proofs establish
both full-domain normal-form round trips and disjoint exhaustive chains,
without coefficient identities. Conservative quartic unary work and
quadratic auxiliary bits persist for these reductions. No bound is
proved for a future root map.

A uniform weight-preserving explicit bijection F_U <-> F_C, with universal
coverage and both inverses, is still missing. Such a map suffices for
full U–C by preserving the three counts. No assertion that it is easier,
unique, or necessary for all possible KR1 maps is made. No complete
endpoint composition, Lean certificate or full KR1 theorem follows.

## 5. Restricted correspondence forced by matching empty roots

Match only the two empty F roots and keep n1,n3,n6. This gives a coherent
restricted bijection on **all U with column values in {1,3,6}**, with
arbitrary multiplicities. The source characterization is exact: from
empty, R6 adds only sixes, then R3 adds threes and R1 adds ones; conversely
that reconstruction builds every such source and unique normal forms
force its F root to be empty. The C image is intrinsically exactly the
objects whose F_C root is empty. Restriction and inverse are executable;
they are not a finite table of equal-weight objects.

Writing s,t,m for counts of 1,3,6: if m>=1,t=0, the image is
(2,0,(3m-2,3m-2+s),()). If m>=1,t>=1 it is

    (3,0,(t-1,3m+t-4,3m+t+s-4),()).

For m=0 use the round-one empty-root chain formula. In particular the
weight-nine zero core (6,3) remains matched, as does its whole unit/triple
chain. This is a replacement for incompatible earlier partial assignments,
not an overlay or a claim that all C with a<=3 are covered.

The smallest unmatched F roots are proposed to remain (8) and
C=(2,0,(2,2),()), weight eight; minimality below eight follows from the
displayed chains or a literal check. Matching those alone would leave
global coverage unresolved. Test only the frozen implementation and
actual declared domains; preserve all failures and exposures.
