# Phase 2 KR final distinct review

25 October 2026, Europe/Stockholm. This is the reserved final review, by the
same distinct critic as the initial review, of the **new frozen corrections**.
The initial authors' packets, the initial review and its failed check remain
unchanged. No further author round is requested or authorized by this review.

**Final verdict: supported for the precise restricted H3 theorem, the C-only
reductions/grammar, and the corrected quotient-cut obstructions; incomplete for
the requested complete a3/a4/a5 unification and full KR1.** New accepted proofs
have distinct ordinary semantic assurance. No formal proof checker ran, novelty
is unverified, and finite implementation checks are not universal proofs.
Same-model role separation does not imply independent model errors.

The sector revision freeze is
`5ea85a8a232d72e004bcd80a80171bf4d418bfd1d29004d9f1d82e942ce82a99`
(49 dependency entries). The recursive correction freeze is
`edd18b65d4ec5c05ebe5288ac07d4616b5af1cc79989fa3e5a9f627c8677cf07`
(7 correction entries plus40 upstream entries). All96 entries matched before
review. The initial packets and initial critic freeze were checked as well;
`kr-final-dependencies.json` records final readback rather than trusting the
authors' preservation assertions.

## 1. Accepted: coherent H3 on its exact restricted domain

**Status: proved, distinct ordinary semantic review.** Write a4,b0 riggings as
`mu=(x,x+t,x+t+y,x+t+y+z)`. H3 extends the initial H2 on exactly the additional
slabs `y=0,1` and the region `y>=18`, with arbitrary x,t,z. Its domain is the
union with the inherited D2, not all a4,b0 and not all b for a3/a4/a5.
I inspected every forward/inverse branch of `revision-bridge.py`,
`revision-v2-bridge.py`, `revision-v3-bridge.py` and the full written proof.
The final implementation imports these pinned canonical files and the original
H2/H1 code; it does not read ignored run outputs to decide a map value.

For the six low-slab languages, the marker supports distinguish y and the
parity of x. Within each support, the8 count determines q, the3 count determines
t with the stated carry correction, and the1 count determines z after its
explicit mandatory offset. These inverses are exact even at t=2/3, q=0 and
z=0. Substitution recovers every literal count, proving both identities.
The listed weights reduce to `16+4x+3t+2y+z`. Every decoded jump and terminal
jump is at most four; in the odd-y1 branch the compulsory one is essential
when q=t=0. All procedures are finite scans and arithmetic.

The old-language exclusions are complete. Marker12 with8 but without6/9;
marker12 with10 but without6/9; and multiple8s with at most two3s each violate
all old f1/g2/g3 support or multiplicity requirements. The other y1 heads have
12+9 but missing6, or have exactly one12/9/6 each. They violate the full lower
contour and the alternative singleton-top missing-penultimate contour, and
cannot be an isolated12 head or any exceptional old hole template. Mixed8/10
contours require at least three3s if their top is3, and all intermediate
levels if their top is larger. The inspected implementations reject unlisted
residual columns rather than freely adding them to a recognized head.

The sole exception to exclusion from the auxiliary g image is important:
`u=(10,8,3^t,1^z)`, t=0 or1, z arbitrary. Its g inverse is exactly
`(3,0,(t+1,t+4,t+4+z),())`, a retained f1 source. Applying f1 gives
`v=(12,6,3^t,1^z)`. This v has neither a full contour nor a valid missing9
contour: the latter would require at least two6s and two3s, whereas v has
one6 and at most one3. Its12 excludes g3 and every old b0/small-hole marker
language. Other hole templates require absent17/19/26. Hence g rejects v,
so the H1 inverse rejects u. None of these tests depends on z. This proves
the required all-z target-component rejection, not merely sampled rejection.

At y0,t0 the map agrees identically with the old a4 plane. Other low-slab
outputs are distinguished from that plane by positive3s or their carried
markers. The old a5 plane requires15 or17, absent here; high-b tails require28,
also absent. Thus all genuinely new low slabs avoid the complete H2 image.

For y>=18, write y=6v+s, x=2q+r and K=6r+s. The three disjoint count-pair
intervals for `(n6,n10)` encode exactly K=0..11. The mandatory-one offset is
`20-4K`, `38-4K` or `52-4K` in those intervals, with minima0,2,8. Therefore
its nonnegativity holds for every phase, not just tested phases. Counts12 and8
uniquely recover v and q; the3 count recovers t; subtracting the known one
offset recovers z. Requiring the stated count-pair intervals and sufficient
ones is necessary and sufficient. Substitution reconstructs all part counts
and gives exactly the original C weight, so both inverse identities hold.

At least two12s and one8 ensure literal flatness even if all smaller optional
parts vanish: decoded7 falls to4 by three, then to zero by four. Optional10,
6,3,1 only subdivide these valid gaps. The missing9 excludes every old full
or mixed contour; the multiple12s exclude the old singleton missing-penultimate
head and every isolated12 head. Other old holes require markers absent here;
g3 has no12. Low slabs have at most one12; other H2 planes/tails have the
distinguishing15/17/28. These facts prove every disjointness claim universally.

Consequently the direct union with H2 is coherent, preserves H2 literally,
has the complete stated intrinsic image, and terminates with both inverses.
Its smallest high-gap source weight is52. **No high-gap source or output was
instantiated** under the numerical40 cap; acceptance of this infinite region
comes from the argument above. The inherited large-b coding likewise received
symbolic, not above-40 numerical, review in the initial verdict.

## 2. Accepted correction: exact exposed quotient boundary

**Status: proved, distinct ordinary semantic review.** The original assertion
of child terminal height at most one and global absence of child `(3)` remains
**refuted**. The correction explicitly withdraws it and preserves the erroneous
initial text and the critic's failed check. Parent `(10,3)`, decoded `(6,2)`,
is the actual counterexample, of weight13.

For a nonempty quotient child, its last positive parent height H is either
terminal at most four, or is followed by K in{1,2}. In the second case flatness
gives H<=K+4<=6. Thus the true child terminal bound is two, with equality
forcing precisely H=6,K=2. Positive adjacent quotient drops remain at most
two; deleting a suffix of zeros exposes only this bottom boundary.

An exact child `(3)` has one positive quotient row, of height two. The preceding
argument forces parent rows6 then2, costing at least F(6)+F(2)=10+3=13.
The counterexample attains13, so this is an exact universal minimum. Therefore
the C weight-nine edge `(3,0,(0,0,0),())->(0,1,(),(0))` still cannot commute
with this cut and retained child value `(3)`, now for a correct weight reason.

The terminal bound two genuinely excludes child `(6)`, decoded height three,
at every weight. Parent C=`(0,2,(),(1,1))` of weight18 has exact child
`(2,0,(1,1),())` of weight6 and zero residual. Actual g2 and H1 both send
that child to `(6)`. This universally refutes this fixed quotient cut as the
required compatible recursion. It does not refute other cuts or embeddings.
Quotient plus ordered remainders still gives its stated exact one-sided carrier;
its admission reconstructs and validates the full positive flat parent.

The initial exact C grammar, all-b pair-fusion reductions and norm/reflection
interpretation remain supported under the scopes in `kr-review.md`. None
supplies the missing U-side boundary insertion or gluing theorem.

## 3. Failure-accounting clarification: auxiliary overlap versus H1 overlap

**Status: proved distinction; empirical new witness.** The named naive
append-threes failure at25 is an overlap with auxiliary g. H1 actually rejects
its target `(8,8,3,3,3)`, so that witness alone does not show a collision with
the retained H1 map. The revision states the g overlap correctly; wording that
treats it as an H1 collision should be narrowed in synthesis.

The naive rule nevertheless does collide with H1. An independent exact scan
of all66 affected naive sources through40 finds seven H1 intersections. The
first observed one is at36:

`C=(4,0,(2,6,6,6),()) -> naive U=(8,8,8,3,3,3,3)`

`H1^-1(U)=(2,2,(1,1),(1,1))`.

Both sources and U have weight36. This supplies an actual H1 obstruction to
the naive extension; it does not affect the retained carried H3 rule. The full
records are in `kr-final-naive-audit.json`. No failed result was erased or
silently turned into a different falsifier.

## 4. Supported finite execution; exact remaining infinite domains

My unchanged final checker ran gates12,30,40. It reuses the initial critic's
independent weighted-gap C and decoded-flat-path U generators and independently
filters ordinary partitions for literal A/B. It reconstructs the six new image
languages independently of author inverse code, and compares their union with
the retained H2 inverse against exhaustive H3 acceptance/rejection. Actual
cluster/gap and U/residue endpoint implementations are used in both directions.

| Ceiling | C/U/A/B total | H3 accepted | H3 rejected | H2 preserved |
|---:|---:|---:|---:|---:|
|12|59|59|0|59|
|30|1393|1203|190|1092|
|40|5461|3498|1963|3014|

All forward pairs passed literal validity, weight, injectivity and source
inverse. Every reverse accepted target reconstructed exactly its source and
forward target; every other target rejected. Through40 the added source counts
are228 for y0,t>=1 and256 for y1; a4,b0 has575 accepted among1292 sources.
All43 available q0,t0/1 target-only contexts were traced and rejected by H1.
The corrected quotient bound, exposed pair and actual C edges were also checked.

| Through40 literal cohort | Distinct | Repeated |
|---|---:|---:|
| Full A /5461 |4684|777|
| Full B /5461 |325|5136|
| H3 A /3498 |2935|563|
| H3 B /3498 |92|3406|

These are literal endpoint-part statistics, not rigging repetition. They are
finite implementation evidence, not source theorem equivalence, novelty,
formal certification, or the full KR1 bijection.

First missing source is `(4,0,(0,0,2,2),())` and first rejected target is
`(10,9,1)`, both at20. The exact unassigned C domain is:

* a3 with1<=b<=48, all riggings;
* a4,b0 with2<=y<=17 and arbitrary x,t,z, and a4 with1<=b<=64;
* a5,b0 outside the old common-mu plane, and a5 with1<=b<=78;
* every a>=6.

An exact C-only recursive language and these enlarging partial U images do
not complete that domain. Full KR1 remains **incomplete**. Promising funding
ideas in the author's final notebook remain **unverified designs**, with no
new assurance from this review.

## Validation boundary and resource record

Source inspection found a small gate-label qualification in the author's
recursive `revision-check.py`: even its `--bound12` call constructs the fixed
C weight18 witness. Its U census is through12, but that label is not a claim
that every object constructed by that particular call had weight<=12. It stays
within the authorized overall40 cap. My final pilot constructs the weight18
edge only at gates30/40; its gate12 objects stay within12. No numerical result
or proof acceptance depends on concealing the author's fixed above-pilot edge.

Four final mathematical subprocesses used the shared meter, all exited0, with
timeout180, total wall and CPU and peak RSS in `kr-final-resource-use.json`.
No object exceeded40, no high-gap/high-b object was instantiated, and no new
dependency, provider, web lookup, external message or nested dispatch was used.
Administrative reads and hashes are elapsed work rather than subprocess math
time. All original error/failure records and closed ledgers remain preserved;
`kr-final-freeze.json` pins this final review and its evidence after the final
dependency readback. No further correction round is needed for this scoped
verdict, and none is available under the current contract.
