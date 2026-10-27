# Positive normalized divided differences by a joint staircase involution

**Status:** written argument, generalization proposed by the coordinating root
agent; independent semantic review requested. This is not a KR1 bijection.
**Novelty:** unverified; the descent-staircase and P-partition technique is
classical. The input positive cut expansion is Xia's Lemma 2.2, arXiv:2609.08816
v1 (https://arxiv.org/html/2609.08816v1); no claim of novelty is made for it.

## Theorem

Let c,d be positive integers, n>=0, 0<=m<=n, and integers 0<r_i<c
for 0<=i<=n. Set z_i=q^r_i+q^(c-r_i), assuming these formal Laurent series
are pairwise distinct, and

    Φ_(d,c)(z) = product_{j>=0} (1-z q^(dj)+q^(c+2dj))^(-1).

Then `(q^d;q^d)_m Φ_(d,c)[z_0,...,z_n]` has an explicit positive
weight-preserving colored-word model described below. Its coefficients are
nonnegative integers. Furthermore `(1-q^r0)(q^d;q^d)_m Φ[...]` has the
same construction with a single forbidden initial cell and is coefficientwise
nonnegative. These conclusions do not require any Kanade–Russell sum-product
identity.

The particles of layer i and index j>=0 have colors α and β, with weights
`r_i+dj` and `c-r_i+dj`. A word is a finite sequence with exactly n
indistinguishable-in-print but ordered cut symbols (their positions identify
cuts 1,...,n) and any number of particles α,β; the number of preceding cuts
determines each particle's layer. Put N=length(word)>=n and set ε_s=1 when
positions s and s+1 are consecutive particles β,α in the same layer, and
otherwise ε_s=0. Equivalently a β,α pair cannot contain a cut between them.
Choose nonnegative integers δ_1,...,δ_N with the last m entries zero, and
set j_1=δ_1 and j_t=j_(t−1)+ε_(t−1)+δ_t for t>=2. A cut at position t
has weight d j_t. An α or β at position t has its layer's base weight plus
d j_t. This word with δ vector is one positive model object. For n=m=N=0,
there is one empty word.

For the version with the extra factor `(1-q^r0)`, set ε_0=1 if the first
word symbol is an α particle, otherwise 0; take j_1=ε_0+δ_1, leaving all
other rules unchanged. If N=0, define ε_0=0 and omit the j_1 equation. The extra initial
shift is equivalent to forbidding the layer-0 α particle at index 0.

## Proof

Xia Lemma 2.2 (ζ_i=1) realizes the bare divided difference as a sum over
weakly increasing cuts `0<=k_1<=...<=k_n`, charge `d sum k_i`, and independent
unbounded particle multiplicities in every layer i at the inclusive index
range `k_i<=j<=k_(i+1)`; use k_0=0 and k_(n+1)=∞. For n=0 this is the
single evaluated product. Flatten each cut object into the word obtained by
listing layer 0 particles then cut 1, layer 1 then cut 2, and so forth. Within
a layer order particles by increasing j and, on a tie, α before β. Cut i's
index is k_i. All indices in the word are weakly increasing, and adjacent
β,α particles in one layer have strictly increasing indices. Conversely,
any word and weakly increasing indices with those strict descents yields the
unique cut object: particles between cuts i and i+1 belong to layer i and
are automatically inside the inclusive index bounds. Repeated cuts and
particles at a cut index are allowed, with separate layer/color labels.

Set ε_s as above and define δ_1=j_1 and
`δ_t=j_t-j_(t−1)-ε_(t−1)`. This bijects allowed index sequences with
nonnegative δ vectors, and

    sum_{t=1}^N j_t
      = sum_{t=1}^N (N-t+1)δ_t + sum_{s=1}^{N−1}(N-s)ε_s.

Represent the normalizing product `(q^d;q^d)_m` by independent binary signed
markers h=1,...,m of weight dh, with sign (-1)^(number of marks). For each
fixed word, N>=n>=m. Choose the least h such that marker h is present or
δ_(N−h+1)>0. If the marker is present remove it and increment that δ;
otherwise insert it and decrement that δ. Both changes preserve weight and
reverse sign. The same h is selected after the change, so the map is an
involution. Its unmatched objects are exactly those with all markers absent
and the last m δ entries zero. Those are precisely the stated positive model.

For the extra factor `(1-q^r0)`, multiply the bare cut expansion first: its
layer-0 α,index-0 geometric factor is always present, so the product removes
that cell. A forbidden α at index 0 is present exactly when the first word
symbol is α and its index is 0: any α at index 0 precedes all layer-0 β at
index 0 by tie ordering, and no cut precedes a layer-0 particle. Thus replacing
j_1=δ_1 by j_1=ε_0+δ_1 enforces the forbidden cell. The same toggle and
survivors apply. For fixed weight W, each particle has positive base and every
positive δ or mark has positive weight, while n and m are fixed; hence there
are finitely many signed objects of weight W. The involution is a finite
weight-preserving cancellation, not global rank matching.

## KR auxiliary sequences and limits

Xia (3.5) uses d=9, c=9n+9, r_i=3n+4+3i, and m=floor(n/3), together
with a positive unrestricted 3-divisible common tail; this gives C_n. Xia
(3.6) uses d=9, c=9n, r_i=3n−1+3i for n>=1, m=floor(n/3), the same
common tail and the additional factor `(1-q^(3n−1))`; this gives A_n. A0
is defined separately as P1. The disjoint union C_n and a weight-(3n+2)
shifted A_(n+1) gives B_n by Xia (3.7).

This result realizes those product-side auxiliary sequences positively for
all n. It supplies no explicit mutual inverses between these survivors and the
three gap-side states, and it does not by itself prove the recurrence
combinatorially or yield a complete KR1 bijection. Comparable staircase
cancellations may be known; no exhaustive prior-art search or novelty claim is
made. A complete computational formalization of the source expansion and
word encoding also remains outstanding.

## Why the restriction m<=n matters

It guarantees that the number N of symbols in every word is at least the
number m of markers, including cut-only words. The condition cannot simply be
dropped in the general theorem: for n=0, m=1, d=1, c=5, r_0=2, the normalized
divided difference is

    (1-q)/[(q²;q)_∞(q³;q)_∞],

whose coefficient of q is -1. Thus no universally positive model exists for
arbitrary m>n, although some special parameters may still be positive.

## Explicit positive series

Let `W_n` be all finite words with n cuts and letters α,β. For w of length
N let `B(w)` be the sum of intrinsic node bases of its particles (using the
number of cuts before a particle to choose its layer), and set

    D(w) = sum_{s=1}^{N−1} (N-s) ε_s.

Then the model yields the explicit identity

    (q^d;q^d)_m Φ_(d,c)[z_0,...,z_n]
      = sum_{w in W_n} q^(B(w)+d D(w))
          / (q^(d(m+1));q^d)_(N−m).

The denominator is an empty product when N=m. Its geometric expansion is the
sum over the unlocked nonnegative δ coordinates, whose weights are
`d(m+1),...,dN`. For the extra forbidden-initial-cell factor, the same sum
has exponent `B(w)+d D(w)+d N ε_0(w)`, where ε_0 is one precisely when
w begins with α. This formula makes positivity and the full word model
visible without an analytic recurrence.
