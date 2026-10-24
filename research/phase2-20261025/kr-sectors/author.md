# Phase 2 KR sector author handoff

**Status: proved with author-only ordinary proof assurance, pending the distinct
Phase 2 critic.** H2 is a strict, executable, weight-preserving extension of
the previously reviewed restricted H1. It does not solve full KR1. No formal
checker or source/novelty certification is claimed. Closed RR006/RR007 records
are immutable inputs, not reopened attempts.

## 1. Exact theorem and inherited dependency

Use literal C=(a,b,mu,nu) with ascending nonnegative zero-padded riggings and
weight Q(a,b)+sum(mu)+3sum(nu), Q=a²+3ab+3b². Literal U consists of descending
F(h) columns, F(5q+r)=9q+(0,1,3,6,8)[r], whose consecutive decoded drops,
including the last height to zero, are at most4.

The inherited H1 is the reviewed RR007 R7 construction. Its domain D1 is all
a<=2 together with all a3,b0. It preserves the accepted A3 map and the corrected
all-k a2,b1 cycle. Its proof assurance is the distinct ordinary semantic review
in `rr007/fleet-a/review-2.md`; this phase supplies its first executable
transcription and tests through40. The complete A3 source/image formulas are
imported from the canonical guarded `rr007/fleet-a/checks/critic-a-literal.py`,
not an ignored raw run. The inherited g2 formulas are the unchanged
`checks/rr003_a2.py` and transitive `rr003_revision.py`, `rr003_columns.py`.
`bridge.py` transcribes the repaired g3 and R3 b1 cycle, and implements the
exact H1 forward/reverse alternating paths. It does not replace exact image
tests by enumerating source objects.

**New theorem candidate T1.** Define D2 as the disjoint union of D1 and:

* C=(4,0,(x,x,x,x+z),()), x,z>=0;
* C=(5,0,(x,x,x,x,x+z),()), x,z>=0;
* every C with a=3,b>=49, arbitrary mu,nu;
* every C with a=4,b>=65, arbitrary mu,nu;
* every C with a=5,b>=79, arbitrary mu,nu.

There is an explicit intrinsic weight-preserving bijection H2 from D2 onto its
stated U image that agrees literally with H1 on D1. Its new source/image tests
and inverse are in `extension.py`. The full large-b domain is part of this
universal theorem, although none of those sources occur in numerical weights
through40. This is an injection into U, not an assertion that its image is all U.

### 1.1 Two common-mu planes

Write x=2q+r, r=0 or1. Append the displayed number of literal ones:

| source | r=0 output | r=1 output |
| --- | --- | --- |
| a4 plane | 8^(q+2),1^z | 12,8^(q+1),1^z |
| a5 plane | 15,10^q,9,1^(z+1) | 17,10^q,9,3,1^(z+1) |

These four entire support languages are the exact image. For the first recover
q=#8-2; for the second q=#8-1; their distinct12 marker recovers r. For the a5
rows recover q=#10, identify parity by15 versus17, and z=#1-1. No unlisted
part is allowed; required multiplicities are exact. Hence these are complete
intrinsic image predicates and both inverse identities follow by counts.

The a4 weights are16+8q+z and20+8q+z, equal16+4x+z. The a5 weights are25+10q+z
and30+10q+z, equal25+5x+z. Decoded heights are8→4,12→7,15→8,10→6,9→5,17→9,
3→2,1→1. The a4 rows end in height4, or optional1s;12→8 drops3. The a5 even
row has15→9 drop3 when no10 intervenes, and9→1 drop4; with10, drops are2,1.
The a5 odd row has17→9 drop4 when no10 intervenes,9→3 drop3,3→1 drop1;
with10, the first drops are3,1. Mandatory positive ones in both a5 rows give
terminal drop1. Repetitions give zero drops. This proves literal U validity
including both empty-tail cases and all x,z.

These languages are pairwise disjoint. They also avoid the entire auxiliary
g2/g3 image and retained f1 image, using the classifications in RR007 R7:

* 8^p,p>=2, has no three-multiple baseline; g2's b0 carrier has exactlyone8,
  and its mixed8/10 carrier requires positive full multiple-of-three support.
  g3 and f1's marker8 branches also have exactlyone8; all other f1 branches
  either have another compulsory marker, a six, or full three-level support.
* 12,8^p,p>=1, again has no3/6 baseline. g2's mixed carrier needs full support;
  its b0 carrier has no12. No other g2 hole has this marker set. g3 has no12.
  f1's only isolated12 family requires a six and has no8; its full-support
  families cannot contain8, and the b1 cycle has no12.
* 15,10^q,9,positive1s has missing12,6,3 in its multiple-of-three support,
  excluding every full or one-missing-penultimate contour. It has no6 for
  the small10 holes, and no17/19/26 for other g2 holes. Neither g3 nor the
  isolated f1 branches have15; the full f1 contours require the absent levels.
* 17,10^q,9,3,positive1s has17 exactlyonce and no6. For q>0 its marker set
  is absent from g2; for q=0 its17 hole requires the absent6. The doubled17
  hole also fails. Neither g3 nor f1 has any17 marker.

### 1.2 Complete arbitrary-rigging large-b tail

Let delta_j=mu_(a-j+1)-mu_(a-j), with mu_0=0; thus
sum(mu)=sum(j*delta_j). Let Delta_j similarly encode nu. Let D_b have two
copies of each3j, 1<=j<=b. Its literal weight is3b²+3b, so the base excess
available from C is E=a²+3(a-1)b.

Use quotient coins w_2=8,w_3=10,w_4=17,w_5=19 (only j<=a). Put
g_j=gcd(j,w_j), d_j=w_j/g_j and t_j=j/g_j. Divide
delta_j=d_j*q_j+r_j,0<=r_j<d_j for each j>=2. Place t_j*q_j copies of w_j
in the U output. Their total weight is exactly sum(j*d_j*q_j). The radices
are (4,10), (4,10,17), (4,10,17,19), with products40,680,12920.

Encode the bounded residue word by the explicit mixed-radix integer
R=r_2+d_2*r_3+d_2*d_3*r_4+..., 0<=R<P. Encode its ordinary binary digits by
the first m=ceil(log2 P) members of this fixed list of literal column values:

`35,37,44,46,53,55,62,64,71,73,80,82,89,91`.

Include each such column zero or one times according to its bit. Add exactly
a-2 copies of the guard28. This is a finite digit algorithm, not a table
matching C objects or U objects. All bit coins, guard and quotient coins are
distinct and not divisible by3. Let H be their *bounded guard/bit weight*,
excluding the variable quotient coins. Let L=sum(j*r_j). Finally include

`delta_1 + h` ones, where `h = E + L - H`,

and include `2+Delta_j` copies of every3j,1<=j<=b. This completes the output.

The guard/bit weight has the following safe upper bounds; no large KR object
was instantiated to compute them:

| a | bit width | maximum guard/bit weight | safe b threshold |
| --- | ---: | ---: | ---: |
|3|6|28+270=298|49, since9+6*49=303>=298|
|4|10|56+540=596|65, since16+9*65=601>=596|
|5|14|84+882=966|79, since25+12*79=973>=966|

Thus h>=0 for every residue word and every permitted b. The complete output
has weight

`3b²+3b+3sum(nu) + sum(j*d_j*q_j) + H + delta_1 + E+L-H`,

which is exactly Q(a,b)+sum(mu)+3sum(nu).

**All internal and terminal decoded gaps.** Full support on3,6,...,3b is
5-flat: inverse_prefix(3j) increases by at most2 between consecutive j,
as direct residues j modulo3 show (increments1,2,2 cyclically). Its smallest
decoded height is2. At b>=31 the top3b is at least93, whose decoded height
is52. Every other output value is at most91, of decoded height51, or is a
quotient coin among8,10,17,19; hence all are inside that dense height range
apart from optionalones of height1 below it. Inserting a new height into an
interval with endpoint drop<=2 only subdivides that interval. The upper gap
cannot increase because no added height is above the old top. Repetitions
give zero drops; the terminal is height2 or1. Therefore every output is
literal U, independent of every quotient, residue, repeated rigging and zero.
All stated b thresholds exceed31.

**Complete intrinsic inverse.** Validate literal U. Read a=#28+2 and require
a in{3,4,5}. Read b as the largest multiple-of-three value divided by3, and
require its stated threshold. Require full support on3j,1<=j<=b, with every
count at least2, and no other part except1,28, the j<=a quotient coins and
the first m bit coins. Require all bit counts in{0,1}; decode R and require
R<P. Successive mixed-radix division uniquely recovers all r_j. Require each
quotient-coin count divisible by t_j and recover q_j by that division. Rebuild
delta_j=d_j*q_j+r_j for j>=2. Compute E,L,H,h from the recovered data; require
#1>=h and set delta_1=#1-h. Set Delta_j=#(3j)-2. Reversed cumulative sums of
the two gap lists recover exact ascending mu and nu. These are precisely the
predicates implemented in `tail_inverse`.

Every forward output passes these tests by construction. Every accepted target
reconstructs its exact marker/bit/quotient/one/multiple counts under the forward
rule. Uniqueness of integer division and binary expansion proves both inverse
identities, including R=0, repeated mu/nu, zero quotients and h=0 if it occurs.
All operations terminate after finite scans and divisions, without histories,
coefficient equality or enumeration of a weight fiber.

**Disjointness from inherited languages.** No g2 output contains28: its only
nonmultiple-of-three non-one markers are8,10,17,19,26. No g3 or f1 output
contains28 either. Every new tail output contains28 positively. The common-mu
planes contain no28. Finally #28 recovers a, and the full contour recovers b,
so distinct tail sectors cannot collide. The new tail is consequently disjoint
from g2, g3, f1 and both planes at every weight.

### 1.3 Coherent H2, exact image and termination

Every H1 output is an f1 value or a g2/g3 value: this follows directly from
the last step of its alternating algorithm. The two preceding disjointness
proofs therefore show that all new plane/tail images avoid **all** H1 images,
not only its retained wall or a finite census.

Consequently H2 is simply H1 on D1 and the displayed direct formulas on new
sources. Its image is the disjoint union of the exact H1 image, the four plane
languages, and the tail language. Test these exact predicates and use their
respective inverse. This proves universal validity, weight, injectivity, exact
image and both inverse identities on D2. Termination is inherited H1 termination
plus finite digit algorithms on the new sectors. `extension.py` implements the
general inherited-splice wrapper, but the disjointness proof shows that every
new source takes exactly one auxiliary edge; the direct union is its mathematical
simplification. Thus the implementation preserves H1 literally.

This coding theorem is useful as a quantified partial result, but it is not a
geometric U-side realization of the scale-three recursive boundary. No optimality
or novelty is claimed. Its large thresholds are deliberate conservative bounds.

## 2. Exact all-b pair-fusion reductions

**New elementary theorem candidate T2, author-only.** For a in{3,4,5}, every b,
the following are explicit bijections onto their exact child/boundary languages.
They are C-side carriers, not U/C bijections. Use the same mu gap digits, put
B=b+1, delta_3=Bq+k,0<=k<B and nu'=(q,q+nu_1,...,q+nu_b).

The uniform base identity is
`Q(a,b)-Q(a-2,b+1)=a-1`, proved by expanding both quadratic polynomials.

* a3: child C'=(1,B,(delta_1),nu'), boundary(delta_2,k), and weight excess
  `2+2delta_2+3k`.
* a4: child C'=(2,B,(delta_2,delta_2+delta_1),nu'), boundary(delta_4,k),
  and weight excess `3+4delta_4+3k`.
* a5: write delta_4=3t+r,0<=r<3. Child is
  C'=(3,B,(4t,4t+delta_2,4t+delta_2+delta_1),nu'), boundary(delta_5,r,k),
  and weight excess `4+5delta_5+4r+3k`. The exact child restriction is that
  its first mu entry is divisible by4.

For a3/a4 the child is otherwise arbitrary literal C with the stated a and
B>=1; boundaries are nonnegative with0<=k<B. For a5 impose the displayed
divisibility and0<=r<3 as well. In the inverse read q=nu'_1 and recover
nu_j=nu'_(j+1)-q. Recover delta_3=Bq+k. Child gaps supply delta_1/delta_2;
a3's boundary supplies delta_2, a4's supplies delta_4, and a5's child first
entry4t together with r recovers delta_4=3t+r; its boundary supplies delta_5.
Reverse cumulative gap sums recover mu. This proves both identities and exact
image including all zeros and repeats. Weights follow from
sum(nu')=Bq+sum(nu) and the base identity; in a5 the carried term is
4delta_4=12t+4r=3(4t)+4r. Termination is finite arithmetic.

This identifies the exact extra phase in the a5 reduction, rather than claiming
that the a3/a4 operation automatically generalizes. The inherited all-b weight2
operation W acts on a2 images only. It does not insert the3k/4r boundary into
U or make these reductions commute with H1/H2. That remains the missing lemma.

## 3. Executed finite findings and failures

Definitions were frozen before the12 pilot. The same scripts then ran unchanged
through30 and40. All six calls completed successfully; external-table failures
were expected falsifier records rather than accepted theorem checks.

| ceiling | full C/A/U/B count | H1 image | H2 image | H2 rejected U |
| --- | ---: | ---: | ---: | ---: |
|12|59|59|59|0|
|30|1393|1049|1092|301|
|40|5461|2889|3014|2447|

At40 H2 adds91 a4-plane and34 a5-plane sources; no tail source can occur.
All accepted C/U values passed literal weight, both inverse identities and exact
enumerated image/rejection tests. Compositions used the actual guarded gap/C
merge and U/B Stockhofe endpoints, not a relabeling of increment distinctness.
The inherited endpoint paper assurances remain those in RR007; this execution
does not re-establish their equivalence to every cited source construction.

| cumulative through40 | distinct literal parts | repeated literal parts |
| --- | ---: | ---: |
| full A denominator5461 |4684|777|
| full B denominator5461 |325|5136|
| H1 accepted A2889 |2326|563|
| H1 accepted B2889 |64|2825|
| H2 accepted A3014 |2451|563|
| H2 accepted B3014 |70|2944|

Maximum H1 forward/reverse alternating length was7 through40. H2's new edges
all had length1. The C-side pair-fusion reductions were exercised on1891 a3,
1398 a4 and408 a5 inputs through40, including a3,b2 (two inputs at39,40) and
a4,b1 (106 inputs); a5,b1 has minimum43 and was not executed.

The supplied Phase 2 table is **refuted as written**. Exact smallest recorded
witnesses, retaining the global scan's weight/lexicographic order:

* a3,b1: at27, C=(3,1,(0,0,0),(2)) gives(9,9,6,3), also repaired g3's image
  of(3,0,(0,9,9),()). At30, (3,1,(0,3,3),(1)) of weight30 maps to weight33
  output(10,9,8,6). Also at30, mu=(1,1,1),nu=(2) and mu=(0,0,0),nu=(3)
  collide at(10,9,8,3).
* a4,b0: at27, mu=(2,3,3,3) and(0,1,5,5) collide at(12,9,3,3). At29,
  mu=(2,3,4,4) maps to(15,9,3) of weight27. At30, mu=(0,4,5,5) collides with
  g2's (2,2,(1,1),(0,0)) at(12,6,6,3,3). At32, mu=(0,0,8,8) gives
  (12,10,10), whose terminal decoded height6 is invalid.
* a5,b0: at30, mu=(0,0,1,2,2) maps to(17,10,3,3) of weight33. The two
  distinct sources mu=(0,0,0,3,3) of weight31 and mu=(1,1,1,1,1) of weight30
  collide at(17,10,3); this is a cross-weight collision and one source already
  violates weight preservation.
* The prior raw a3,b0 failure at36 is reproduced: mu=(1,13,13) maps to
  (9,9,6,6,3,3), also g2's (0,3,(),(1,1,1)). The repaired g3/H1 passed it.

No failed external table is patched into H2. Its test functions were extracted
as named AST definitions only; unguarded module execution and absolute imports
were not run. Prior failures and unverified universal slogans remain preserved.

## 4. Remaining exact gap and next obligation

H2's first unassigned source is (4,0,(0,0,1,1),()) at18; its first rejected
target is(10,8), also at18. Thus full KR1 is still open. Entire missing infinite
families include a3 with1<=b<=48, a4 with1<=b<=64, a5 with1<=b<=78, their
non-plane b0 riggings, and all a>=6. The scale-three C grammar does not supply
the absent U cut/gluing. New finite coverage is not proof of those sectors.

The next tractable obligation is an intrinsic U boundary normalization realizing
the pair-fusion child plus its bounded k (and a5 r) while avoiding the complete
H1/H2 image. A secondary paper clue is that a sufficiently large final mu gap
can fund a fixed dense contour and finite marker overhead even at small b;
this is not yet a retained construction or a claim to cover a finite residual
box. Do not substitute a finite matching table for that missing map.
