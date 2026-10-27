# Positive staircase models for Xia’s three product sequences

Status: Written author proof, independently source-audited by the formal agent; Lean checks the generic toggle, not the source interpretation or flattening. This is an auxiliary result, not a complete KR1 bijection. The joint staircase and sign-toggle mechanism was proposed by the coordinating root agent. Closest primary source: Xia, arXiv:2609.08816v1, Lemma 2.2 and equations (3.5)–(3.7), https://arxiv.org/html/2609.08816v1. Novelty is unverified.

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

## Recurrence approach: phase and node-weight accounting

The positive models still need weight-preserving, mutually inverse
combinatorial maps realizing Xia v1 (3.2). At n=0 the C0 product is P3.
Every P3 partition with no literal part 3 has a direct embedding into A1:
set the sole cut to 0, leave layer 0 empty, and copy each part 9j+4 or 9j+5
into layer 1, swapping α and β. Common parts 6,12,15,... remain common parts.
The displayed node formulas show that weights match exactly. The inverse
recognizes cut 0 and empty layer 0 and swaps colors back. This is only a
restricted branch; it matches the j=0 subcase of RR003's existing H11/K-to-P3
branch, so no novelty is asserted. The C0 partition `(3)` does not belong to
this branch; its weight makes it a candidate for the `q³ C1` branch.

For general n, let C_n node layer i have α=3n+4+3i and β=6n+5-3i.
Prepend a cut at index 0, shifting old layer i to i+1, and swap α and β.
Comparing A_(n+1) bases with C_n bases, an old α changes weight by
`3(n-2i)` and an old β by `-3(n-2i)`, before any change to indices or common
parts. Consequently this simple insertion is weight preserving automatically
for n=0 but generally requires a context-sensitive repair by layer and color
imbalance. In addition, a C_n survivor need not remain an A_(n+1) survivor,
because the order/strict-descent pattern changes under color swap.

Let T_n be the independent common tail of the positive models. When
3∤(n+1), T_n/T_(n+1)=1/(1-q^(3n+3)): C_n has an extra freely repeatable
part 3n+3. When 3|(n+1), the two common tails coincide, while the number of
locked terminal deltas rises from floor(n/3) to floor((n+1)/3). A recurrence
map must handle both phase cases; literal deletion of an extra common part
cannot cover the second. The remaining proof obligation is an explicit branch
bijection for the three-state recurrence, including target coverage, collision
control and inverse recovery. No such global recurrence map is supplied here.

### A collision in the q³ C1 branch

At n=1, C1 has a cut k>=0, prefix node species 9j+7 and 9j+11 for
j<=k, suffix species 9j+10 and 9j+8 for j>=k, common parts 6,12,15,...,
and charge 9k. A natural weight-preserving attempt to map q³ C1 to P3 is

    9j+7  -> (9j+4)+3,
    9j+11 -> (9j+5)+6,
    9j+10 -> (9j+4)+6,
    9j+8  -> (9j+5)+3,
    cut k -> 3 copies of part 3 per unit of k,

plus one 3 for the external q³. This is **refuted as an injection**: at k=0,
the input prefix particles `(7,11)` and the input suffix particles `(10,8)`
are distinct legal C1 objects of weight 18, but both give the P3 output
`(3,3,4,5,6)` of weight 21. This output is outside the existing RR003 H11
branch: it has t=2 threes and one 4, so it is outside the k=0 interval
0<=t<=1 and below the next interval's minimum 4. Therefore merely reaching
the known branch complement does not remove the collision.

A possible repair must keep enough phase to distinguish whether the 3
accompanied the 4 or the 5 and must also absorb arbitrary common 6-parts.
Changing `10 -> 4+3+3` distinguishes the first collision, but also fails
as an injection: legal source objects `(7,8,6)` and `(11,10)` both have
weight 21 and give the identical P3 object `(3,3,3,4,5,6)` after the
external q³ shift. The arbitrary common 6-parts absorb the phase encoding.
No global or restricted injectivity is asserted for this modified rule.

There is also a universal obstruction to keeping this branch inside the first
nine-block, independent of the particular replacements. At k=0 the C1
subfamily has five independent unrestricted multiplicities for 6,7,8,10,11.
The P3 parts at most 11 are only 3,4,5,6. Suppose a weight-preserving
injection after the q³ shift always output P3 parts at most 11. Restrict each
source multiplicity to 0,...,t. The `(t+1)^5` inputs have source weight at
most 42t, while the possible outputs have weight at most 42t+3, and each of
four multiplicities is at most 14t+1; hence there are at most `(14t+2)^4`
outputs. This fails for large t. Therefore any such injection must produce
an output part >=12 on some inputs. This statement uses no global KR1
identity and no fixed bound on runtime; it is a simple growth obstruction.
