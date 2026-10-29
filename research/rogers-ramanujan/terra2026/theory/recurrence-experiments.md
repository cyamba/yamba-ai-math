# Experiments toward a positive recurrence bijection

Status: partial branch and refuted attempts; complete KR1 remains unresolved.

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
