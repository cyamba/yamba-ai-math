# A2 frozen partial bijection: zero or one single, every pair count

Version A2, frozen before finite trials. Author-only assurance pending the
reserved distinct critic. This is Fleet A's second of at most three variants.
It uses an alternative full-domain decomposition basis. It must not be
overlaid with the entire reviewed empty-F-root map.

## Exact maps, domain and intrinsic image

The C domain is exactly all literal C with a in{0,1}, every b>=0, and their
full ascending exact-length increment vectors. When a=1 write mu=(u).
For j=1,...,b form the ascending partition

`lambda_j=2j-1+a+nu_j`.

Conjugate it ordinarily, obtaining the descending positive partition V.
Map C to the sorted descending union of `3*V` with no ones if a=0, or
`1^(u+1)` if a=1. Empty lambda has empty conjugate. The empty C datum maps
to empty; a=1,b=0 maps to a nonempty all-one U.

The exact U image is empty or a partition supported on1 and positive
multiples of3, satisfying these intrinsic predicates. Let o be its number
of ones, let a=0 when o=0 and a=1 otherwise, and let V be the multiples-of3
subpartition divided by3. If V is empty, accept empty or all ones as above.
Otherwise put b=max(V), require every level1,...,b to occur, require its
top multiplicity c_b>=a+1, and every lower multiplicity c_k>=2. There are
no other conditions. Recover u=o-1 if a=1. Conjugate V back to an ascending
lambda and set `nu_j=lambda_j-(2j-1+a)`.

## Universal author proof

**Proved, author-only elementary argument.** Adjacent lambda entries differ
by at least2, and lambda_1>=a+1. In its conjugate, the top level has
multiplicity lambda_1>=a+1, and lower level k has multiplicity equal to an
adjacent lambda difference, hence at least2. Every level occurs. These
are precisely the displayed image conditions. Conversely those conditions
give lambda_1>=a+1 and differences at least2, so the recovered nu is
nonnegative ascending of exact length b. Ordinary conjugation is an
involution and the one-count recovers a,u; this proves both inverse
identities on the full stated domains and exact image coverage.

All multiples3,6,9,12,... are allowed U numerical values, with successive
decoded heights differing by1 or2. The image contains every consecutive
multiple-of3 level from3 to3b, so every positive decoded-height drop is at
most2. Its terminal3 has decoded height2; optional ones have height1.
Thus every output is literal U, including all zero and repeated cases.

The lambda sum is `b²+ab+sum(nu)`. The image weight is therefore
`3b²+3ab+3sum(nu)+a+sum(mu)`. Since a in{0,1} gives a²=a, this is exactly
the C weight. Conjugation preserves ordinary size. All procedures operate
on finite partitions and terminate; no enumeration, rank matching, free
colors or saved path is involved.

This construction is uniform over unbounded b. Within-vector repetitions
and U multiplicities are side-specific: for b>=2 all image U have repeated
threes, while nu may be strictly increasing. Empty remains distinct
vacuously. The pilot reports both predicates instead of identifying them.

## Coherence and the explicit limit

The A2 image is disjoint from the complete A1 two-single image. An A1 image
with8 or10 has a forbidden nonmultiple3 marker; one with9 also has ones
but lacks levels3 and6; pure sixes lack level3; the only A1 branch with3
has exactly one3 and at least one1, while A2 then requires either b=1 with
at least two3 or b>1 with at least two3. Hence A1 and A2 may form a single
precisely limited alternative partial bijection, with disjoint C domains.

The full old empty-F-root map conflicts with A2. At C a=0,b=2,nu=(0,0),
A2 gives U=(6,3,3), whereas the old map assigns this U a different C datum
through its empty F root. No old assignment is silently retained or
overlaid. A1 agrees with the old empty-root map only on its own overlap.

The naive attempt to extend A2 by independently adjoining the A1 image of
mu for a=2 is **refuted symbolically**: C=(2,1,(0,0),(0,)) gives shifted
lambda=(3), pair image(3,3,3), and A1 single image(3,1), totaling
U=(3,3,3,3,1). A2 already gives the same U from C=(1,1,(0,),(2,)). Both
have weight13. This witness is paper arithmetic, not an above12 pilot.
Priority cannot restore both preimages. The missing next lemma is a
canonical interacting separator carrying the single/pair allocation,
not an independent multiset union.

Smallest global domain gap includes C=(3,0,(0,0,0),()) at9, unless a
separate compatible map is supplied. No full U/C theorem follows from
this partial construction or its union with A1. Novelty remains unverified.

## Frozen trial boundary

Named script `.runs/rr007/a2-zero-or-one-single.py`, first pilot bound12.
It checks full literal U/C inputs through12, exact image and its complement,
validity, weights, both round trips, A1-image disjointness and separate
distinct/repeated cohorts. Every actual input and output stays at most12.
No extension is authorized here; root must record a named unchanged30
extension after a passing pilot. No new above30 execution or dependency.
