# RR003 final author revision: every cluster datum with a at most two

**Proposed proved restricted theorem; author-only assurance.** The two
scheduled critic challenges are complete. This further extension has a
written universal argument and will receive finite implementation checks,
but it has **not** received separate semantic review. It is not an accepted
global bridge, a complete KR1 bijection, or a novelty claim.

The first two proposals, their freezes, receipts and separate reviews are
preserved verbatim. This is the final author revision of round two, not a
third mechanism or review round. The original mathematical objective and
success criterion are unchanged. Discovery exposed all objects through 30.

## Exact formulas filling the three mixed holes

Retain the reviewed second map on its complete stated domain. Its only
missing a<=2 inputs have a=2,b>=1 and k=mu_1 in {4,5,9}. Write
mu=(k,k+t), t>=0, and delta_j=nu_(b-j+1)-nu_(b-j), with nu_0=0.
Then delta_j>=0 and sum(j*delta_j)=|nu|. A template below consists of fixed
columns T and a minimum ones count s. Add t ones to these s ones. Except
for the two parity branches, add delta_j copies of 3j, 1<=j<=b.
Let D_b be two copies of every column 3,6,...,3b. Superscripts mean literal
multiplicity, not exponentiation of a part value.

| k | b | T | s | increment convention |
|---|---|---|---|---|
|4|1|(9,6,3,3)|0|ordinary|
|4|2|(17,9,6,3)|1|ordinary|
|4|>=3|D_b plus 3(b-2),17|1|ordinary|
|5|1|(10,6,6)|1|parity|
|5|2|(19,12,6)|1|ordinary|
|5|3|(19,12,9,6,6,3,3)|1|ordinary|
|5|>=4|D_b plus 3(b-2),19|1|ordinary|
|9|1|(10,10,6)|5|parity|
|9|2|(17,17,9,3)|0|ordinary|
|9|3,4,5|(26^(b-2),18,10,3)|10,11,18 respectively|ordinary|
|9|>=6|D_b plus 3(b-2),26|2|ordinary|

For either parity branch write nu_1=2q+r, 0<=r<=1, and add q sixes and
r threes. Its added weight is 6q+3r=3nu_1. These are finitely many uniform
parameter formulas, not a table of enumerated images or an index by weight.
They are an intentionally restricted embedding; their suitability for a
global extension is unproved and they may be replaced if necessary.

## Intrinsic recognition and proof of image separation

First validate literal U, including the terminal step to zero, and try the
reviewed second inverse. On its complement inspect the non-three columns,
ignoring ones. Recognize the following disjoint branches and then subtract
the fixed template and minimum ones. Reject a negative count, an extra
unlisted column, or an invalid residual range. In the ordinary branches,
the remaining counts of 3j are exactly delta_j, so reversed cumulative sums
recover the zero-padded vector nu. In parity branches the remaining threes
must number zero or one; twice the remaining sixes plus this number is nu_1.
The remaining ones number t. Return a=2,mu=(k,k+t).

* No non-three marker: the only new branch has one 9, one 6 and at least
  two 3s; it is k=4,b=1. Its six count prevents the reviewed full-support
  branch, and its 3 count prevents the reviewed zero-pair 9-and-3 branch.
* Only 10, and at most one 3: multiplicity one or two of 10 means respectively
  (k,b)=(5,1) or (9,1). The reviewed mixed images require at least two 3s.
* A single 17: k=4. Largest multiple 9 of count one gives b=2. Otherwise
  the largest multiple is 3b with b>=3 and top count at least two.
* Two 17s: (k,b)=(9,2).
* A single 19: k=5. Largest multiple 12 of count one gives b=2 when there
  is no 9 and b=3 when there is a 9. Otherwise the largest multiple is 3b,
  b>=4, with top count at least two.
* Both 26 and a single 10: k=9 and b is two plus the multiplicity of 26,
  required to lie in {3,4,5}.
* A single 26 without 10: k=9,b>=6, recovered from the largest multiple 3b.

These marker sets and counts distinguish the new branches. The reviewed
second images have non-three markers only 8 or 10 (or a single 9 in the
zero-pair sector). Thus 17,19,26 cannot be masked by the reviewed inverse.
The two marker-free/single-10 exceptions are excluded there by the counts
just given. Extra ordinary increments never change a fixed distinguishing
marker or top count: the exceptional templates with a top single 9 or 12
allow increments only below that top. For b=2,k=5, no increments create a
9; for b=3,k=5 its baseline contains a 9. Therefore recognition is intrinsic
and unambiguous for every input weight, rather than merely through 30.
Subtracting the uniquely recognized template and taking cumulative sums
inverts the forward rule. Conversely reconstruction restores every accepted
residual count, proving the other inverse identity on the recognized image.

## Universal validity, weight and termination arguments

The decoded heights of 1,3,6,9,10,12,17,18,19,26 are respectively
1,2,3,5,6,7,9,10,11,14. Every listed exceptional baseline has successive
height drops strictly less than five, including the final drop to zero.
For the dense branches, consecutive multiples of three have height drops
one or two. The worst marker-to-dense-top drops occur at b=3 for marker17,
b=4 for marker19, and b=6 for marker26: each equals four. Adding a column
inside the existing height interval only subdivides a valid drop. Every
ordinary free column is in that interval. In the parity branches adding
3 or 6 also has this property. Additional ones subdivide the terminal drop.
Thus every output is in the actual U domain at every weight.

The weight of T plus s ones is Q(2,b)+2k, where Q(2,b)=3b^2+6b+4.
For dense templates, |D_b|=3b^2+3b; adding 3(b-2), the marker and s gives
3b^2+6b plus respectively 12,14,22, namely Q+2k. The exceptional totals
are respectively 21,36,23,38,59,31,46,67,94,127, agreeing with Q+2k at
the indicated b. The free weight is t+3|nu| in either convention. Hence
the result has exactly the C weight Q+|mu|+3|nu|. All counting, division
and cumulative-sum loops are finite. Conservative unary-weight bit bounds
remain O((N+1)^2 log(N+2)) work and O((N+1)^2) auxiliary space.

## Reversible operations and exact remaining lemma

On this restricted image, decode C intrinsically, add one to both mu
coordinates, and reconstruct. Its inverse subtracts one from both when
mu_1>0. This conjugated explicit operation has cost two, terminates, and
has no saved history, search or lookup. The new branch transitions need
not be local column replacements. Likewise a nu suffix increase is defined
by intrinsic decoding, increasing that suffix, then reconstruction; its
inverse decreases that suffix when the resulting vector is valid.
The reviewed literal local carries and column insertions remain unchanged
on their frozen stated domains. The new parity branches do not promise
that every nu increase is a single added 3j column.

This establishes, at author-only proof assurance, mutually inverse explicit
maps from **all C with a<=2** to a specified subset of U, for arbitrary
b,mu,nu. It proves neither that every U lies there nor that any a>=3 sector
is handled. The next decisive lemma remains a canonical, disjoint and
exhaustive extension to arbitrary a, with intrinsic recovery of both a,b.
The valid uncovered object U=(6,3), of weight nine, and the omitted datum
C=(3,0,(0,0,0),()) are explicit boundary witnesses. A finite test cannot
remove this obligation. No endpoint implementation, complete bijection,
Lean certificate or novelty verification is supplied by this restricted result.

## Learning at final revision

Decisive obligation: fill all mixed a=2 holes without losing nu or confusing
inverse branches. Actually proved in the argument above: explicit disjoint
formula families for those holes, extending the restricted image to every
a<=2 datum. Separate review covers the earlier map, not this extension.
Next justified step: freeze and check implementation, then investigate a
global statistic rather than treating coverage of small a as universal.

Workflow hypothesis, **unvalidated**: completing one full parameter sector
can reveal whether an apparent local obstruction is only a poor coding
choice. This does not establish that marker embeddings aid global discovery
or that RR003 increases discovery success. The complete KR1 objective is
unchanged and the finite verification remains exposure, not held-out evidence.
