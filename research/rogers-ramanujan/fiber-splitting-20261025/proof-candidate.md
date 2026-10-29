# Frozen proof candidates: fiber refinement and the first KR1 middle slab

Status before checking: **author ordinary arguments; independent review pending**.
Attribution: Christopher Yamba supplied the fiber-splitting/dimension intuition.
The formulas and proofs below were developed in this attempt. Novelty is
unverified; no full KR1 or general tableau cancellation theorem is claimed.

## Fiber refinement: precise obligation

For each weight, let f:X->Z be a coarse map. Replacing u by tagged copies
(u,i) resolves a fiber in an enlarged set. To solve the original problem one
needs actual weight-preserving encodings E_u:f^-1(u)->Y, each injective,
with pairwise disjoint images and intrinsic inverses. Their union is then
a bijection onto its image; it is onto Y exactly if those images exhaust Y.
Proof: equality of outputs first determines the same u, then the same input;
the piecewise inverse is unique. Surjectivity is precisely exhaustion.

Equal global counts do not suffice for a restricted move family: two sources
can both have only one permitted neighbor even when another target exists.
Reordering labels/dimensions that disappear on flattening leaves the original
collision unchanged. The missing mathematical object is the encoding E_u,
not a name for the fiber index. This is an elementary framework, not claimed new.

## Ordinary tableaux: arbitrary fiber size handled explicitly

For every r>=1, there is an explicit bijection from standard tableaux of
shape (2,2,1^r) onto the following recognized subset of the disjoint union
of shapes (2,1^(r+2)) and (3,2,1^(r-1)). This concerns a total order;
its incomparability graph is empty. It does not prove the weighted P case.

Write T=((u,v),(a,b),(c1),...,(cr)), with c1<...<cr. Standardness gives
u<v, a<b, u<a<c1, and v<b. Put L={c_i:v<c_i<b}.
If L is empty, sort b into the singleton tail and keep the row (u,v).
Otherwise c=max L; output ((u,v,b),(a,c)) followed by the old tail minus c.

The hook image is exactly the valid standard tableaux ((u,v),(a),D)
whose tail D contains an entry greater than v. Its inverse chooses the
least such entry b and returns ((u,v),(a,b),D minus b). The lack of an
entry in (v,b) is exactly the hook branch condition.

The rotated image is exactly the valid tableaux ((u,v,b),(a,c),D)
with v<c<b and no entry of D in (c,b). Its inverse restores c to the
ordered singleton tail and returns ((u,v),(a,b),sort(D union {c})).
The inequalities ensure all source column/row conditions. Conversely the
chosen predecessor c is uniquely recovered. Top chains and the column v<c
make the rotated output valid; every remaining singleton exceeds a. Thus
both inverses and image disjointness hold for every r, without enumeration.

For any fixed coarse hook, let its eligible tail entries above v be
b1<...<bm. The original bubble fiber has m inputs. The first goes to the
hook; input j>1 goes to the rotation with (b,c)=(bj,b_(j-1)). Thus this
really resolves arbitrary fiber cardinality, not just the pictured pair.
For T1=((1,2),(3,4),(5)), T2=((1,2),(3,5),(4)), the outputs are respectively
((1,2),(3),(4),(5)) and ((1,2,5),(3,4)). This small repair was present in
the prior construction; it is not a new discovery of this attempt.

## KR1: whole y=2 slab, not just a large-parameter tail

Let D consist of C=(4,0,(x,x+t,x+t+2,x+t+2+z),()) for all x,t,z>=0.
Its weight is 20+4x+3t+z. Use p^j for j copies, omit zero powers.
Every displayed union is sorted. Put x=2q+r, 0<=r<2. Define F:

| Branch | U |
| --- | --- |
| r=1 | 8^(q+2),6,3^t,1^(z+2) |
| r=0,q>=1 | 8^(q+1),6^2,3^t,1^z |
| x=0,t=0 | 10,9,1^(z+1) |
| x=0,t=1 | 10^2,3,1^z |
| x=0,t in {2,3},z>=5 | 10,9^2,3^(t-2),1^(z-2) |
| x=0,t>=2, otherwise | 10^2,6,3^(t-2),1^z |

**Validity.** Heights of 1,3,6,8,9,10 are 1,2,3,4,5,6. Repeated
columns have zero drop. Branches one/two have an 8 and a 6, and terminal
6 has height3 even with no smaller tail. Branch three has a mandatory one
bridging 9 to height1 (drop4). Branch four has a mandatory3 bridging 10
to height2 (drop4). Branch five has at least three ones, bridging its9s
to height1; an optional3 subdivides that drop. Branch six has mandatory6
bridging height6 to3. All terminal drops are <=4; all values are allowed U.

**Weight.** First two totals are 8q+16+6+3t+z+2 and
8q+8+12+3t+z; these equal 20+4x+3t+z in the respective parity.
The next four totals are 20+z,23+z,28+3(t-2)+z-2,
and26+3(t-2)+z. Each equals 20+3t+z when x=0.

**Exact inverse.** Let n_p be literal multiplicities. For valid U, admit
exactly the following languages, forbidding any unlisted part:

| Support/conditions | (x,t,z) |
| --- | --- |
| {8,6,3,1}, n8>=2,n6=1,n1>=2 | (2(n8-2)+1,n3,n1-2) |
| {8,6,3,1}, n8>=2,n6=2 | (2(n8-1),n3,n1) |
| {10,9,1}, n10=n9=1,n1>=1 | (0,0,n1-1) |
| {10,3,1}, n10=2,n3=1 | (0,1,n1) |
| {10,9,3,1}, n10=1,n9=2,n3<=1,n1>=3 | (0,n3+2,n1+2) |
| {10,6,3,1}, n10=2,n6=1; n3>=2 or n1<=4 | (0,n3+2,n1) |

Support/mandatory markers and counts distinguish all six languages. Each
inverse satisfies its branch, and substitution recovers literal U. Both
maps terminate by finite counting/arithmetic.

**Disjointness from reviewed H3.** This is essential to the proposed coherent
extension; compare the exact prior maps, not Argon's different implementation.
The retained f1 has at most one8 or one10; its corrected b1 language with
both10 and9 has exactly one9 and a nonempty 6/3 tail. This excludes every
new output (the new 10+9 language has no 6/3 tail).

For auxiliary g2, any mixed-marker image with an8 and/or10 and maximum
multiple6 needs at least three6s; the new 8-languages have only one/two6s.
The new 10^2+6 language has only one6. The only applicable g2 hole template
10^2,6 has at most one3 and needs at least five ones; the new rule redirects
exactly those cases. The 10^2+3 language has too few3s for a mixed contour
and no6 for the hole. The new 10+9 languages have too few lower multiples
for a contour, and no mandatory 17,19,26 hole marker. Other g2 carriers
have a single8/9 and cannot match. The g3 formulas have at most one8/10;
their only 10+9 head has exactly one9 and a nonempty6/3 tail. Thus no new
output lies in f1 or g2 or g3. H1 outputs lie in their union.

H2's additional a5 plane has15 or17, its high-b images have28, and its
a4 plane has only8s or12+8s, with no6/10/9 combination above. H3's low
slabs either have12 or are pure8/3/1 or contain both10 and8. Its high slab
has at least two12s. None can equal a new output. Hence D's image is
disjoint from the whole H3 image. The union preserves every H3 assignment.

This proves an explicit candidate extension to the entire first missing
middle-gap slab. It does not cover y=3..17, missing b>0 sectors, or general a.
The fiber-inspired information is encoded in actual shape/multiplicity
choices, including a carry at z=5; no free labels survive in the codomain.

## Larger band: alternate funded encoding, not yet composed

For 2<=y<=17 put k=ceil((2y+4)/3), x=3q+r, q>=k, r=0,1,2,
h=12k-8y-12-2r. The alternative target is
12^(q-k),10^(y+2),8,6^r,3^t,1^(z+h).
It is literal U, has weight16+4x+2y+3t+z and h>=0. The counts recover
y=n10-2,r=n6,q=n12+k,t=n3,z=n1-h. Its >=4 tens distinguish it
from retained H3 mixed-marker languages and the new y=2 map's <=2 tens.
For coherence with the y=2 theorem, use this alternative only for y=3..17.
It leaves a bounded common-width strip x<3k(y) with t,z still arbitrary.
No assertion that dimension growth alone resolves that strip is made.
