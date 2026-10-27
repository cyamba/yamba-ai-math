# A bidegree-preserving local surgery and a finite-alphabet obstruction

Status: **proved, author argument; separate semantic review outstanding**. This is
an explicit local bijection, not a global KR1 bijection. Novelty **not verified**.
The local `c` coordinate is the multiplicity of one specified part, not a rank
among all partitions of a given weight; there is no global enumeration or use of
the KR1 cardinality identity.

## One move, with full forward and inverse

Let x,y be formal generators of degrees 2 and 3 respectively. Consider input
triples `(a,b,c)` of nonnegative integers, representing x^a y^b (x²y)^c.
Output is either:

* type 0, a triple `(d,e,f)`, representing y^d (x²)^e (xy)^f; or
* type 1, a triple `(e,f,g)`, representing x (x²)^e (xy)^f (x²y)^g.

Define `X=a+2c`, `Y=b+c`, `r=X mod 2`, and

    p = max(0, floor((min(X,Y)-r)/2)+1).

If `c<p`, put `f=r+2c`, `e=(X-f)/2`, `d=Y-f`, and return type 0 `(d,e,f)`.
If `c>=p`, put `h=(X-1-Y) mod 2`, `g=h+2(c-p)`,
`f=Y-g`, `e=(X-1-Y-g)/2`, and return type 1 `(e,f,g)`.
All residues here are the nonnegative residues in {0,1}.

For the inverse, given type 0 `(d,e,f)`, set `X=2e+f`, `Y=d+f`,
`c=(f-(X mod 2))/2`. Given type 1 `(e,f,g)`, set `X=1+2e+f+2g`,
`Y=f+g`, recompute `p`, and set `c=p+(g-((X-1-Y) mod 2))/2`.
In either case return `a=X-2c`, `b=Y-c`, `c`.

**Proof of totality, weight, and inverse.** At fixed bidegree `(X,Y)`, source
triples are in one-to-one correspondence with the integer interval
`0 <= c <= min(floor(X/2),Y)`. The type-0 coordinates are exactly
`f = (X mod 2)+2t` with `0 <= f <= min(X,Y)`, and thus have precisely `p`
choices; the formulas send source c=0,...,p-1 to these in order.
The type-1 coordinates are exactly `g=h+2t`, `0<=g<=min(Y,X-1-Y)`,
where `h=(X-1-Y) mod 2`; if the upper bound is negative there are none.
The source interval length is the sum of these two output counts. To see it
without appeal to KR1, split into the three cases:

1. `Y>=X`: the first count is `floor(X/2)+1` and the second is 0.
2. `Y<=floor(X/2)`: the source count is `Y+1`; the admissible f and g
   progressions are both bounded by Y. If Y is even they have opposite
   parities; if Y is odd each parity occurs equally often. In either case
   their counts sum to `Y+1`.
3. `floor(X/2)<Y<X`: the first count is `floor((Y-r)/2)+1`, the second is
   `floor((X-1-Y)/2)+1`; their sum is `floor(X/2)+1`.

Thus the prescribed c ranges are valid and cover the output on each branch
exactly. The displayed inverse recovers the progression index and therefore c,
then uniquely recovers a,b. It also follows directly that both x- and
 y-exponents are unchanged. Weight is preserved after every specialization
`x=q^u`, `y=q^v` with positive u,v. The mapping consists of fixed integer
arithmetic and terminates immediately.

Equivalently this combinatorially realizes the local identity

    1/[(1-x)(1-y)(1-x²y)]
      = 1/[(1-y)(1-x²)(1-xy)]
        + x/[(1-x²)(1-xy)(1-x²y)].

Example: input `(a,b,c)=(0,0,1)` has `(X,Y)=(2,1)` and maps to type 0
`(d,e,f)=(1,1,0)`: the part 7 becomes `(3,4)` after x=q²,y=q³.
Input `(a,b,c)=(1,0,0)` maps to the type-1 marker `2`.
The associated executable [local_surgery.py](local_surgery.py) checks 27,000
source triples and bounded target boxes in both directions; the proof above,
not that finite check, supplies the universal claim.

## Exact use on KR auxiliary product classes

For any j,k>=0 specialize `x=q^(9j+2)`, `y=q^(9k+3)`. The three input
species are

    9j+2, 9k+3, 9(2j+k)+7,

and the unmarked output species are

    9k+3, 9(2j)+4, 9(j+k)+5.

The marked output has one `9j+2` and species `9(2j)+4`, `9(j+k)+5`,
`9(2j+k)+7`. Thus each move is a weight-preserving total bijection from
unrestricted multiplicities of the chosen three P2 species into a disjoint
union of the specified P3-species class and a marked class. Other multiplicities
can be carried as labeled context; to invert, the context and branch marker must
remain available. The choice j=k=0 is the first 9-block specialization.

**Remaining global obstruction.** Different pairs `(j,k)` share species,
especially the `3` parts, while outputs at residues 4,5 can be inputs or
context of other operations. A strategy choosing moves has to prove a unique
schedule, termination, and recovery of j,k and branch information after markers
are removed. The formulas above do not supply these, do not map all P2 to P3
plus the literal K family, and do not reach the KR1 gap class. Existing
[RR003 product involution](../../rr003/product-involution.md) already gives a
claimed all-weight auxiliary P2-to-P3/K split with an author argument; this
local move does not supersede it. Relation to that split and novelty remain
unverified. The same three-variable identity is classical in nature; no
literature priority is asserted.

## Source finite-alphabet entropy obstruction

Let B* be the subset of P1 partitions in which every part congruent to 1 or 8
modulo 9 has multiplicity at most 7 and every part congruent to 3 or 6 modulo 9
has multiplicity at most 1. **This is a restricted subset, not a normal form of
all P1.** A tempting attempt to create such a form by merging eight copies of
1 into 8 is noninjective: `(1,1,1,1,1,1,1,1)` and `(8)` both merge to `(8)`.
Likewise the original source contains every member of its multiplication chain.

For each of the first L blocks of nine, B* independently admits
`8*2*2*8=256` multiplicity patterns, hence has exactly `256^L` elements with
all parts <=9L. All these fibers are finite. For the target gap class, group
parts into blocks of three. Its seven patterns and transition matrix A are the
known Chern–Li linked partition ideal; rows indexed
`E,1,21,31,2,3,33` have successor sets respectively

    all, all, all, {E,2,3,33}, all, {E,2,3,33}, {E,3,33}.

For `v=(10000,10000,10000,5321,10000,5321,3473)^T`, direct integer arithmetic
shows

    A³v=(1584707,1584707,1584707,843205,1584707,843205,550363)^T <= 159v.

Because v has positive entries, the number of length 3L paths from E is at
most `(10000/3473)159^L`, including leading/trailing empty blocks. Therefore
**no injection** from B* into the KR1 gap class can satisfy

    max(output) <= α max(input) + C

for all inputs, for any constants `α < log(256)/log(159)` (approximately
1.09396) and finite C. Otherwise the 256^L inputs in the first L blocks would
inject into O(159^(αL)) gap words, impossible for large L. Empty partition
max is 0. Weight preservation is not needed for this obstruction. In
particular, synchronous bounded-lag window maps cannot work even when tested
only on B*. This strengthens the immediate fixed-lag obstruction from the
unrestricted input `(1^n)`, since B* has bounded per-part multiplicity.
The result does not rule out unbounded carry, global transformations, or the
existing RR003 involutions.

## Primary sources, checked 2026-10-27

1. Chern–Li, *Linked partition ideals and Kanade–Russell conjectures*,
   Discrete Math. 343 (2020), 111876, https://arxiv.org/abs/1809.08655.
   Their block ideal and q-difference approach precede the seven-state model;
   see also Chern's explicit state table
   https://shanechern.github.io/publications/dissertation/Shane_Chern_Dissertation.pdf.
2. Uncu–Zudilin, *Reflecting (on) the modulo 9 Kanade–Russell identities*,
   Sém. Lothar. Combin. 85 (2021), B85e,
   https://www.mat.univie.ac.at/~slc/wpapers/s85uncuzud.pdf. Finite
   q-series and pair/singleton motions; older status statements are historical.
3. Xia, *The modulo 9 Kanade–Russell identities and their Nahm-sum duals*,
   arXiv:2609.08816 **v1**, 8 September 2026,
   https://arxiv.org/html/2609.08816v1. Theorem 1.1 claims all five analytic
   sum-product identities; §§3–4 compare three-state q-recurrences with
   divided-difference product sequences. Recent preprint, no independent
   verification claimed here. Its (3.8) identifies the P2-P3 difference; it
   is not itself the local inverse/coverage algorithm above.
4. Mizuno, *The three Kanade–Russell identities modulo nine*,
   https://arxiv.org/abs/2609.09653, preprint September 2026; the indexed
   page https://www.alphaxiv.org/abs/2609.09653 says v3 as of 5 October 2026
   and claims proofs of three symmetric identities. Full v3 proof not inspected,
   so neither method nor peer-review status is asserted.
5. RR003 [product involution](../../rr003/product-involution.md) and
   [closing source comparison](../../rr003/closing-source-comparison.md):
   closest repository precedents for full auxiliary P2/P3 branch and Xia.
   That auxiliary construction is an author argument without separate semantic
   review, according to RR003's result; it is not the requested full KR1 map.

Review questions: (i) does the three-case interval proof withstand independent
checking at zero boundaries? (ii) Can deterministic j,k surgery be organized so
that its branch information equals the existing K cut and is recoverable without
external labels, while the inverse has a strictly decreasing measure?

## All-n divided differences: why the cut interaction is essential

Xia v1 Lemma 2.2 supplies a positive *colored* cut expansion for each bare
divided difference: weakly increasing k_1,...,k_n, charge 9 sum k_i,
and independent geometric multiplicities for two node species at every index
inside each layer's interval. This is already established source machinery.
The product-side sequences C_n include the extra prefactor
`E9(q³;q³)_n`, with `E9=1/((q³,q⁶;q⁹)_inf)`. For n=1,2 the finite
factors q³, q⁶ cancel literal common denominators, as used in RR003; at
n=3 a factor `(1-q⁹)` remains because E9 has no denominator `(1-q⁹)`.

At n=3, cuts `(0,0,0)` have zero charge. After the q³ and q⁶ cancellations,
all remaining unrestricted parts have size at least 12: the common tail
starts at 12 and the node species have minimum 13. Thus the cut-zero summand
with `(1-q⁹)` has coefficient -1 at q⁹. A positive set cannot be assigned
independently to every fixed cut. This is an exact obstruction to a purely
per-cut cancellation, not to the existence of a global positive construction.

The tuple `(0,0,1)` starts with the charge q⁹, compensating this coefficient.
But the naive map that simply increases the last cut and leaves multiplicities
unchanged is not a weight-preserving well-defined correspondence. For C3 the
four node pairs at index 0 are `(13,23)`, `(16,20)`, `(19,17)`, `(22,14)`.
The last pair is present at cuts `(0,0,0)` and absent at `(0,0,1)`; the latter
has a new layer-2 pair `(28,26)` at index 1. For example the negative object
consisting of the q⁹ mark and one 14 has weight 23, but there is no positive
object of weight 23 at cuts `(0,0,1)`: its base charge 9 would require a
remaining part of weight 14, which is unavailable (all other available parts
are >=12 and the possible singletons at 12,13,16,17,19,20,23,26,28,31 do
not include 14). A same-cut replacement 9+14=23 is possible, showing how a
boundary particle might absorb the mark, but it collides with unrestricted
pre-existing 23s unless an inverse-detectable rule is supplied.

The plausible next obligation is a signed-state involution for the residual
`(1-q^{9h})` markers across cuts, with colored boundary occupations retained.
Each involution must preserve weight, pair every signed object except an
explicit positive model, and terminate if used in a Garsia–Milne path. The
local bidegree surgery above is a possible primitive when a boundary exchange
matches its denominations, but no such full involution has been established.
This route does not assume the analytic identity to manufacture a global
weight-by-weight rank pairing.

### General fixed-cut obstruction, all n≥3

**Proved, author argument; separate review outstanding.** The preceding failure
of nonnegative fixed-cut fibers is not confined to n=3. In Xia v1 (3.5), C_n
uses c=9n+9 and r_i=3n+4+3i, for i=0,...,n. Lemma 2.2 assigns to
`k_1=...=k_n=0` all 2(n+1) node species at index j=0, and only the terminal
node species at j>=1. Their smallest exponent is
`min_i {r_i,c-r_i}=3n+4`. The common prefactor satisfies the exact identity

    E9 (q³;q³)_n
      = (q⁹;q⁹)_{floor(n/3)} /
        product_{j>n, 3 not dividing j} (1-q^(3j)).

For every n>=3, the numerator has exactly one term of degree 9, namely -q⁹;
all its other nonconstant terms have degree >=18. The denominator has no
nonconstant terms below degree 3(n+1)>=12, and all node geometric factors have
no nonconstant terms below degree 3n+4>=13. Therefore the zero-cut summand has
coefficient **-1 at q⁹ for every n>=3**. Its label-preserving interpretation
cannot be a positive weighted set. This algebraic coefficient proof does not
assert that the complete C_n has a negative coefficient; cancellations across
cut tuples are precisely the outstanding task. The formula and objection apply
to C_n as defined by Xia, not automatically to A_n or other sequences.

A sound local signed cancellation is already available in the n=3 zero-cut
fiber. Label the 14 species at node 3 and the 23 species at node 0. Pair a
negative object carrying the q⁹ mark and at least one 14 with the positive
object obtained by removing the mark and one 14 and inserting one 23. The
inverse removes one 23 and inserts one 14 and the mark. All other labeled
multiplicities and cuts remain fixed. This is a weight-preserving involution
between exactly the negative subset with positive 14 multiplicity and the
positive subset with positive 23 multiplicity. Remaining negative objects
have no 14; remaining positive objects have no 23. This limited operation
cannot resolve the q⁹ zero-cut negative object, which has no particle, and
therefore requires cross-cut cancellation.

### A terminating cross-cut cancellation on zero boundary occupations

**Proved, author argument; separate review outstanding.** This provides one
actual all-n sign-reversing involution step for the 9-marker of C_n, for any
n>=3. Use Xia's labeled cut model, including all other common particles and
all other signed markers as inert context. Label each geometric species by
`(layer i, index j, α/β)`, and allow independently repeated particles in
that cell. The cell of layer i is present for `k_i <= j <= k_(i+1)` with
`k_0=0`, `k_(n+1)=infinity`. Repeated cuts retain separate layer colors.

On a **negative** object whose 9-marker is present, write t=k_n. If both
multiplicities in the layer-n cells at index t are zero, remove the 9-marker,
increase k_n to t+1, retain all other particles and markers, and create the
new layer-(n−1) cells at index t+1 with zero multiplicity. This is well
formed because the only old cells removed by the cut change are precisely
the two vacant layer-n cells at t; the only new cells are the two vacant
layer-(n−1) cells at t+1.

The inverse applies to a **positive** object without the 9-marker for which
`k_n>k_(n−1)` and both multiplicities in the layer-(n−1) cells at index k_n
are zero. Decrease k_n by 1, insert the 9-marker, remove those two vacant
cells, and insert the layer-n cells at the new index with zero multiplicity.
The strict inequality is exactly what ensures the reduced cut sequence remains
weakly increasing and guarantees that these new layer-(n−1) cells were indeed
created in the forward map. Labels of all retained particles are unchanged.

The cut-charge `9 sum k_i` increases by exactly 9 in the forward direction,
matching the removed mark. Hence weight is preserved, sign is reversed, and
both inverse identities hold by direct inspection. Each invocation performs
one finite operation; interpreted as a two-sided involution it stops in a
single step. The zero-cut, empty-particle negative object is matched.

This is a **partial** cancellation: a negative object with an occupied layer-n
cell at its last cut, or a positive object failing the inverse test, remains
unmatched. In particular, this operation does not address the marked 14
counterexample in the preceding subsection. Combining it with same-cut particle
exchanges requires a single intrinsic priority rule; simply applying two
partial involutions independently can create overlap and fail to be an
involution. With several markers, choosing which one to toggle also requires
an intrinsic priority rule. No complete positive model or KR1 bijection is
claimed.

### A complete cancellation of one q⁹ marker; positive C3, C4, C5

**Proved, author argument; independent review requested.** The previous
zero-boundary rule can be restricted and combined with a second rule so that
*every* object carrying the q⁹ marker is paired. Use the colored cut model
and fixed deterministic ordering α<β to break equal-index particle ties.
Other markers, when present, are inert signed context.

Let t=k_n, and consider a negative object (q⁹ marker present).

* If the terminal layer n is nonempty, choose its greatest occupied index j;
  among α,β at j use the predetermined larger color with a particle. Remove
  the q⁹ marker and move one particle of that color from j to j+1. The cut
  does not change. The target's terminal maximum is j+1 and exactly one
  particle occupies that maximum, because j was the source maximum.
* If the terminal layer is empty, remove the marker and increase the last cut
  from t to t+1, retaining all other labeled occupations and assigning zero
  multiplicity to the two new layer-(n−1) cells at t+1. The terminal layer
  remains empty.

To invert a positive object, first inspect the terminal layer:

* If nonempty, this object lies in the first image exactly when its maximum
  occupied index is greater than t and its total particle multiplicity at
  that maximum, across both colors, is exactly one. Move that unique particle
  back one index and add the marker.
* If empty, this object lies in the second image exactly when
  `t>k_(n−1)` and both layer-(n−1) cells at index t are vacant. Decrease
  the last cut by one and add the marker, keeping the terminal layer empty.

These conditions are intrinsic and disjoint, and the outputs of the inverse
are legal. The first inverse's moved-back particle is at an index at least t;
when there are ties at that index the moved-back color need not be the largest
color, so to make the tie rule invertible refine the selection: choose the
largest occupied index, and there choose **the larger color if present**;
the inverse at the target must additionally require that, after moving back,
the moved color is the larger color present at the old maximum. Equivalently,
if the moved color is α, the β multiplicity at index j must be zero. This is
an intrinsic test. Conversely, this test is automatic on every forward image.
The branch with β has no additional restriction. With this test, the two maps
are mutually inverse on their specified domains. (This tie condition is
essential; using only a unique maximum would cause collisions.)

Every negative object belongs to exactly one branch and is paired with a
positive object; sign is reversed and weight is preserved because either a
particle index or the last cut rises by one, increasing weight by 9. The
involution makes one deterministic move, with no global enumeration. The
unmatched positive objects are specified by failure of the corresponding
inverse predicate above. They form an explicit positive class.

For n=3,4,5 the prefactor has only the single signed marker `(1-q⁹)`, so this
constructs a full positive model for C_n. For n>=6, more factors
`(1-q^(9h))` remain. Pairing the 9-marker while treating the others as inert
context gives a reduced *signed* model; subsequent cancellation is not yet
proved because an h-step operation may leave the previous inverse-survivor
conditions. There is no claim of a complete positive model for general n,
or of a KR1 bijection. The construction is downstream of Xia's positive
colored divided-difference expansion and does not need the asserted KR1
sum-product evaluation.

The q⁹ cancellation's negative direction and weight were additionally checked
for 65,610 small colored input objects by
[terminal_cancellation.py](terminal_cancellation.py); this is a transcription
check, not the universal proof.

A concrete obstruction to naive iteration at n=6: after eliminating q⁹,
consider the q¹⁸-marked object with zero cuts and one terminal particle at
index 0. It survives the q⁹ cancellation because its terminal maximum equals
the cut. Shifting that particle forward by two indices removes the q¹⁸ mark,
but produces an object with a unique terminal maximum above the cut and no
particle at the preceding index, hence an image of the already-canceled q⁹
pair. Thus the two-step particle rule does not stay within the q⁹-survivor
class. Any all-n iteration needs a revised joint normal form or a joint
sign-reversing involution, not merely the same rule applied marker by marker.

## Joint all-n cancellation via a descent staircase (root idea)

**Proved, author argument, independent semantic review requested.** The root
agent supplied the following joint idea, which resolves the marker interaction
left open above. It constructs a positive colored model of every C_n in Xia v1,
not an endpoint bijection between P1 and KR1 gap partitions.

Fix n>=0. Start from the signed colored C_n expansion in Xia (3.5) and
Lemma 2.2, including all signs from
`(q⁹;q⁹)_m`, where `m=floor(n/3)`. Leave the independent common tail
`product_{j>n,3 not dividing j} (1-q^(3j))^-1` unchanged.

Flatten a cut object into a finite word with n ordered cut symbols and an
arbitrary finite number of particles, in the order

    layer 0 particles, cut 1, layer 1 particles, ..., cut n, layer n particles.

Within each layer sort the particles first by index j and then by color α<β.
Cut i carries index k_i. At shared endpoints multiple adjacent layers may all
contain their own separately colored particles: cuts separate them in the
word, retaining their layer labels. Repeated equal cuts are allowed. The
flattened indices j_1,...,j_N are globally weakly increasing. A strict rise
is forced at each adjacent within-layer descent β,α; all other adjacencies
allow equality. Conversely any such word and index sequence uniquely decode
to the cut object by taking each cut's index and assigning each particle to
the layer determined by the preceding cut count. Monotonicity guarantees the
inclusive bounds at every cut; no further restrictions are needed.

Let ε_s=1 if positions s,s+1 form adjacent within-layer particles β,α and
0 otherwise. Define

    delta_1 = j_1,
    delta_t = j_t-j_(t-1)-ε_(t-1)  for 2<=t<=N.

All deltas are nonnegative, and inversion by cumulative sums is unique.
For fixed word, the total index charge satisfies

    9 sum_{t=1}^N j_t
      = 9 sum_{t=1}^N (N-t+1) delta_t
        + 9 sum_{s=1}^{N-1} (N-s) ε_s.

The second term and the intrinsic node-part weights depend only on the word,
not on the deltas. Each marker h in 1,...,m has weight 9h and changes sign.
Since N>=n>=m, delta_{N-h+1} always exists and also has weight 9h. Holding
the word and all other data fixed, select the smallest h with marker h
present or delta_{N-h+1}>0. If marker h is present, remove it and increase
that delta by one; otherwise insert it and decrease the delta by one. The
selected h stays the same after the move, so the operation is its own inverse;
it reverses sign and preserves weight. Both the word and the independent common
parts are untouched. It terminates in one step.

The unmatched objects are exactly those with all markers absent and
`delta_{N-m+1}=...=delta_N=0` (an empty condition when m=0). They provide
an explicit, positive colored model for every C_n, including n=0. For fixed
n, finite weight allows finitely many words because particle bases are >=3n+4,
and finitely many delta vectors because each nonzero delta has positive
weight. Thus cancellation is valid weight-by-weight as a finite involution,
not a weight-specific matching. This positive model does not establish the
recurrences as combinatorial bijections, map its survivors to the gap side,
or remove particle colors/cut data to produce the KR1 endpoint.

[staircase_toggle.py](staircase_toggle.py) checks 124,944 word/delta/marker
states for n=3 and 6, including inverses, sign and weight; these tests are
finite checks of the transcription, not a substitute for the written proof.

### Extension to the A_n and B_n product-side sequences

**Proved, author argument, independent review requested.** For n>=1, Xia v1
(3.6) uses c=9n, `r_i=3n-1+3i`, so the node species at layer i,index j
have respective weights `3n-1+3i+9j` and `6n+1-3i+9j`. All are positive.
The additional prefactor `(1-q^(3n-1))` cancels the reciprocal geometric
factor for the α particle in layer 0,index 0, because that cell exists for
every cut choice. Thus the corresponding positive cut model is the same as
above with that single cell forbidden. Other node cells remain separately
colored even when their numeric weights coincide.

With the same flattened word and α<β ordering, the forbidden cell condition
is exactly encoded by imposing `j_1>=1` when the first word symbol is α and
otherwise imposing no additional initial constraint. Indeed, any forbidden
α at index 0 would be the first particle in layer 0 and precede every β at
index 0; the layer 0 particles occur before cut 1. Define ε0 accordingly and
use `delta_1=j_1-ε0`, with the same ordinary β,α descent rule and the same
`delta_t` for t>=2. The staircase inverse is again a bijection and now adds
the fixed word-dependent baseline `9Nε0`. Apply exactly the preceding
multi-marker involution: selected h still has coefficient 9h. The positive
survivors are the no-marker objects with last m deltas zero. For n=0 Xia
defines A_0 directly as P1, a positive product class. Finally Xia's definition
`B_n=C_n + q^(3n+2) A_(n+1)` gives an explicit positive disjoint union from
these A and C models. These positive representations are not, by themselves,
the required bijections realizing Xia's three-state recurrence.
