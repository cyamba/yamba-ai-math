# An exact cone-validity and lower-image classification

Date: 26 October 2026. Status: complete written argument, supported by [separate semantic review](review-round1.md). The bounded checker corroborates the transcription; it does
not prove the all-parameter statement. No Lean certification or novelty claim
is made here.

## Objects and scope

For nonnegative integers `z,y,x,c6,c3,c1`, let

\[
 U(z,y,x;c_6,c_3,c_1)
 =(10^z,9^y,8^x,6^{c_6},3^{c_3},1^{c_1}),
\]

where superscripts denote multiplicities, in descending order. The encoded
column values `10,9,8,6,3,1` have decoded heights `6,5,4,3,2,1`, respectively.
The literal class \(\mathcal U\) is that in
[`kr1.decode_columns`](../../rogers-ramanujan/checks/kr1.py): consecutive decoded
height differences, including the final difference to zero, must be strictly
less than five. The encoding then conjugates to a partition with multiplicities
at most four.

Define \(\mathcal L\) to be the image of the *current literal forward map*
[`rr003_a2.reconstruct_columns`](../../rogers-ramanujan/checks/rr003_a2.py) on
valid `ClusterData` with \(a\le2\). This names one specific family of formulas.
It is not a claim about every possible lower-sector construction or a full
KR1 bijection. In particular, the classification below does not assume that
those formulas have independently established every other desired property.

Argon's supplied PDF suggests the validity argument on page 7 and a
lower-image exclusion template on pages 13 and 14. Inspecting all actual
forward branches yields a stronger exact theorem, and identifies precisely
why the restriction on the multiplicity of 9 is useful.

## Theorem 1: exact validity, with no bound on z

Assume \(y\ge1\). Then

\[
 U(z,y,x;c_6,c_3,c_1)\in\mathcal U
 \quad\Longleftrightarrow\quad x+c_6+c_3+c_1>0.
\]

**Proof.** All column values are valid encoded values and are already in
descending order. Their heights are a repetition of a subsequence of
\((6,5,4,3,2,1)\). Height 5 occurs because \(y\ge1\).

Any heights preceding the height-5 block are 6, so the transition into that
block is 1, with repeated-height transitions equal to zero. All heights at
and after that block are in \(\{1,2,3,4,5\}\), so differences between any
successive positive heights are at most four. If
\(x+c_6+c_3+c_1>0\), some height below 5 occurs after the height-5 block.
The terminal height is then in \(\{1,2,3,4\}\), and its difference to zero
is also less than five. These are exactly the literal flatness predicates.

Conversely, if \(x+c_6+c_3+c_1=0\), the last height is 5. Its difference
to zero equals five, so `decode_columns` rejects the object. This proves both
directions. Notice that merely saying that a terminal height is not divisible
by five would not characterize the general class; the actual boundary is
terminal height less than five. The family here satisfies that stronger
condition. There is no upper bound on \(z\) or \(y\). \(\square\)

## Theorem 2: exact intersection with the current lower image

Assume

\[
 y\ge1,\qquad x+z\ge1,\qquad x+c_6+c_3+c_1>0.
\]

Then

\[
 U(z,y,x;c_6,c_3,c_1)\in\mathcal L
 \quad\Longleftrightarrow\quad
 z\le3,\quad y\ge3,\quad c_6\ge2,\quad c_3\ge2.
\tag{1}
\]

In the intersecting case, the corresponding lower-sector input is explicitly

\[
 \begin{aligned}
 k&=4x+5z-2,\\
 C_{\rm low}
 &=\bigl(2,3,(k,k+c_1),
 (y-3,\ y+c_6-5,\ y+c_6+c_3-7)\bigr).
 \end{aligned}
\tag{2}
\]

Here \(k\ge2\). The three entries of \(\nu\) in (2) are nonnegative and
weakly increasing because their successive differences are
\(c_6-2\) and \(c_3-2\).

**Proof of necessity by exhaustive symbolic branch classification.** The
forward map calls `rr003_revision.reconstruct_columns`, which may first call
`rr003_columns.reconstruct_columns`. The final `rr003_a2` layer handles only
three missing common increments \(k\in\{4,5,9\}\), with \(b>0\). Thus
the following list covers all its lower-sector source branches. For completeness,
for \(k\ge2\), `_marker_digits(k)` fails exactly at \(k=4,5,9\): if
\(k\equiv0,1,2,3\pmod4\), its value of \(z\) is respectively
\(2,3,0,1\), and nonnegativity of \(x=(k+2-5z)/4\) gives exactly those
three exceptions. Thus the final hole layer covers the full complement of the
reviewed branches.

| Forward branch | Consequence for a possible cone intersection |
| --- | --- |
| `rr003_columns`: all \(a\le1\), and \(a=2,k\le1\) | Outputs only 1 and multiples of 3. They contain neither 8 nor 10, contrary to \(x+z\ge1\). |
| `rr003_revision`: \(a=2,b=0,k\ge2\) | Carrier is `(8)`, `(9)` or `(9,3)`, plus 6s and 1s. A carrier with 8 has no 9; carriers with 9 have neither 8 nor 10. All are excluded. |
| `rr003_revision`: mixed-marker \(a=2,b>0\) | This is the only possible intersection; analyze it below. |
| `rr003_a2`: hole \(k=4,b=1\) | Contains only 9, 6, 3 and 1, so neither 8 nor 10. |
| Hole \(k=4,b\ge2\) | Contains marker 17, outside the cone support. |
| Holes \(k=5,b=1\) and \(k=9,b=1\) | Contain 10 and only 6, 3, 1 thereafter; no 9. |
| Hole \(k=5,b\ge2\) | Contains marker 19, outside the cone support. |
| Hole \(k=9,b=2\) | Contains marker 17, outside the cone support. |
| Hole \(k=9,3\le b\le5\) or \(b\ge6\) | Contains marker 26, outside the cone support. |

In the one remaining mixed-marker branch, the literal marker equation is

\[
 k+2=4x+5z,\qquad x\ge0,\quad0\le z\le3,\quad x+z\ge1.
\]

For \(1\le j\le b\), the multiplicity of column \(3j\) is

\[
 2+\delta_j+\mathbf1_{j=b},\qquad
 \delta_j=\nu_{b-j}-\nu_{b-j-1}\ge0,
\]

where the missing entry \(\nu_{-1}\) is zero. If \(b\le2\), no 9 is
present. If \(b\ge4\), a 12 is present with multiplicity at least two,
outside the cone support. Therefore an intersection forces \(b=3\).
At that value the three relevant multiplicities are

\[
 y=3+\nu_0,\qquad
 c_6=2+\nu_1-\nu_0,\qquad
 c_3=2+\nu_2-\nu_1.
\]

Hence all four conditions on the right side of (1) are necessary, and solving
these equations yields (2). The output ones count is \(\mu_1-\mu_0=c_1\).

**Proof of sufficiency.** Suppose the right side of (1) holds. Set \(k\) and
\(C_{\rm low}\) by (2). Since \(x+z\ge1\), \(k\ge2\). Moreover
\((k+2)\bmod4=z\) because \(0\le z\le3\), and
\((k+2-5z)/4=x\). Thus `_marker_digits(k)` returns exactly `(x,z)`, so this
input is supported by the mixed-marker branch. Substituting its nonnegative
increments gives exactly \(y\) nines, \(c_6\) sixes, \(c_3\) threes,
\(x\) eights, \(z\) tens and \(c_1\) ones. Therefore its forward image
is the prescribed \(U\). This proves (1). \(\square\)

The symbolic branch proof concerns the literal forward image. It does not
infer membership solely from the behavior of the recognizer. The bounded
checker independently verifies that the implemented recognizer agrees with
this classification in the stated finite box, and reconstructs every accepted
case back to its input tuple.

## Corollaries and sharpness

1. **The original 6D cone conjecture is proved, and strengthened:** if
   \(y\in\{1,2\}\), \(x+z\ge1\), and
   \(x+c_6+c_3+c_1>0\), every such cone object lies in
   \(\mathcal U\setminus\mathcal L\), for every \(z\ge0\).
   The previously imposed bound \(z\le3\) is unnecessary.
2. **Additional safe families:** the same conclusion holds for any \(y\ge1\)
   if at least one of \(z\ge4\), \(c_6\le1\), \(c_3\le1\) holds.
3. **The multiplicity restriction cannot simply be deleted:**
   \(U=(9,9,9,8,6,6,3,3)\) has weight 53 and is the image of
   \((a,b,\mu,\nu)=(2,3,(2,2),(0,0,0))\).
   This is the smallest-weight intersection under the displayed hypotheses,
   because any intersection has at least three 9s, two 6s, two 3s, and at
   least one marker of minimum weight 8, totaling at least 53.
4. The classification supplies **safe target space**, not a complete KR1
   bijection. Distinct proposed higher-sector families may still occupy the
   same safe cone. In particular, proving exclusion from \(\mathcal L\)
   does not prove exclusion from the existing \(a\ge3\) images.

## Generating function for the y=1,2 safe cone

The all-parameter safe subfamily in Corollary 1 has exact weight generating
function

\[
 (q^9+q^{18})\left[
 \frac{q^8}{(1-q^8)(1-q^{10})}
 \frac1{(1-q^6)(1-q^3)(1-q)}
 +\frac{q^{10}}{1-q^{10}}
 \left(\frac1{(1-q^6)(1-q^3)(1-q)}-1\right)
 \right].
\]

Indeed, the first term enumerates \(x\ge1,z\ge0\) with arbitrary tails.
The second enumerates \(x=0,z\ge1\) with nonempty tail. These cases are
disjoint. The six distinct part values make their multiplicity encoding
injective, so there is no overcount. This is a generating function for this
safe target subfamily only, not the KR1 generating function.

## Bounded corroboration and provenance

`python3 research/partitions/argon-2026-10-26/cone_author.py` checks 8,375 valid
parameter tuples with \(0\le x,z\le5\), \(1\le y\le5\),
\(0\le c_6,c_3\le3\), \(0\le c_1\le2\). It finds exactly 828 lower-image
objects, all with the input (2), and confirms literal decoding and round trips.
The proof above is an all-parameter branch argument; these finite counts are
corroboration only. The input PDF's SHA-256 is
`5c86926416fce825c8ff8e68471a1918493ddf0f248dc57f15a12ebe8afbd9a9`.
