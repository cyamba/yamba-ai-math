# Frozen B3: a complete parity interface for the mixed degree-two model

Frozen 24 October 2026, after the source inspection at21:11 UTC and before
any B3 finite trial. This is an **author-defined R2star**, not a silent
correction or relabeling of the published R2. Full KR1 remains unresolved.
All proof assurance is author-only, pending the separate critic.

Put G={0,1,2,3,4}, ground0, e(i,j)=[i<j], alpha=(0,1,3,6,8).
An ordinary primary atom P(n,c) has c>0, n>=0, literal weight9n+alpha[c].
A mixed secondary atom S(n,i,j) has i,j>0, n>=e(i,j),
n=e(i,j) modulo2, and literal weight9n+alpha[i]+alpha[j].
The domain M is every finite sequence of these atoms with the following
adjacent raw-size differences. Write x-y for their raw-size difference:

* P(c),P(d): x-y > e(c,d).
* P(c),S(l,m): x-y >= e(c,l)+e(l,m).
* S(i,j),P(c): x-y > e(i,j)+e(j,c).
* S(i,j),S(l,m): x-y >= e(i,j)+2e(j,l)+e(l,m).

These are the mixed-model relations inspected in Konan
arXiv:2002.00300v2, Definition2.5, with all constituent sizes nonnegative.
No generic mixed-model bijection is implemented by this candidate.

The codomain R2star consists of secondary sequences ending in0_00,
with every nonterminal colorij different from00, raw size n>=e(i,j),
and n=e(i,j) modulo2. Set

E(ij,lm)=e(i,j)+2e(j,l)+e(l,m), E_star=E+2D_star.

D_star is zero except the following disjoint cases:

1. j=l=0 and i,m>0: D_star=e(i,m).
2. i=0, j,l,m>0 and e(j,l)=1: D_star=-1.
3. j=0, i,l,m>0 and e(i,l)=0: D_star=-1.
4. m=0, **i,j,l>0**, and e(j,l)=0: D_star=1.
5. l=0, i,j,m>0, and e(j,m)=1: D_star=1.

Adjacent raw differences must be at least E_star. The literal weight of
any secondary is9n+alpha[i]+alpha[j], including terminal weight zero.
The bold restriction is the only difference from the predicate printed
in Definition2.11 of the inspected source, whose case(2.19) omits i>0.
No claim of a verified source erratum is made before separate review.

## Forward, inverse and intrinsic image

Keep each mixed S(n,i,j). Replace P(n,c) by n_(c0) when n is even and
by n_(0c) when n is odd. Append0_00. Conversely remove terminal0_00;
turn every colorc0 or0c into P(n,c), and every nonground colorij into
S(n,i,j). The parity of a codomain part forces precisely the named
even/odd case. Thus color recovery uses only the current atom, and the
two atom maps are inverse with no free word, trace or choice.

## Proof of every comparison

Let e=e(c,d), a=e(i,j), b=e(l,m). All raw differences have a parity
forced by their colors. For two primaries the four cases (even/even,
even/odd, odd/even, odd/odd) give E_star thresholds respectively
2, 1+2e, 1+2e, 2. These are exactly the smallest raw differences of
the required parity strictly greater than e.

For P(n,c) before S(y,l,m), put f=e(c,l). The two primary parities give
thresholds b+2f (even) and b+1 (odd). These are exactly the least
differences, of parity b or1-b respectively, at least f+b.

For S(x,i,j) before P(n,c), put f=e(j,c). The primary even/odd cases
give thresholds a+2 and a+1+2f. These are exactly the least differences
of parity a or1-a strictly greater than a+f.

For two secondary atoms there are no ground letters and D_star=0,
so the difference relation agrees literally. These nine cases exhaust
all possible adjacent types and primary parities. The terminal relation
is E_star(ij,00)=e(i,j); it agrees with the displayed lower size bounds.
Thus validity holds in both directions and the image is exactly R2star.

Both identities now follow atom by atom and from terminal deletion and
insertion. Raw sizes and the nonground primary word agree exactly,
so total literal weight agrees. Finite passes terminate. This proves a
universal M <-> R2star bijection, not merely a finite coefficient check.
It does **not** prove R2star <-> F2 or C; source theorem import across the
printed-predicate discrepancy remains unaudited.

## First falsifier and verification boundary

Paper witness of the printed interface problem: U=(9,1,1), decoded
heights(5,1,1), maps under frozen B1 to F2=(1_01,0_10,0_00).
It has raw total1 and nonground word11. A single R2 atom in color11
has even raw size; two one-letter atoms with that raw total must be
1_01 and0_10. In the printed predicate their Ereg thresholds in the
two orders are3 and1, respectively, whereas their differences are1
and-1. Hence neither order works. In R2star the first threshold is1,
and the object is exactly the image of the valid M sequence P(1,1),P(0,1).
All theorem hypotheses used here are explicit: e is a binary minimal
energy, e(0,0)=0, e(0,c)=1, e(c,0)=0, delta_g=1, and all sizes are
nonnegative. The word is all one color, so commutative vs ordered color
preservation cannot resolve this witness.

The frozen pilot `.runs/rr007/b3-parity-pullback.py 12` independently
enumerates M and literal R2star through12 and checks exact image, both
identities, weight, distinct and repeated atoms, and the printed witness.
Every actual finite input and output has literal weight<=12. No larger
trial is requested or authorized.
