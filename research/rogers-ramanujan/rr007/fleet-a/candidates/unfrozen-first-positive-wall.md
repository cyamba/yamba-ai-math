# Unfrozen clue: a recovered first-positive mixed wall

Status: **unverified construction clue**, author-only; not a fourth frozen
variant, not part of A3, not executed at any weight. The coordinator
authorized preserving it as a next direction only. A3's frozen first
missing datum and all frozen files remain unchanged. No theorem promotion
or finite coverage addition is requested.

The intended domain is a=2, b>=1, mu=(1,1+s), s>=0, arbitrary ascending nu.
Form the positive ascending partition of length b+2

`lambda=(1,2,2+nu_1,5+nu_2,7+nu_3,...,2b+1+nu_b)`.

For b=1 this means exactly `(1,2,2+nu_1)`. Take `U=3*lambda^T` and adjoin
s ones. This would assign the first gap of A3,
`(2,1,(1,1),(0))`, to `(9,6)` at fifteen. That example is symbolic only.

The intended intrinsic image consists of U supported on ones and positive
multiples of three. After removing ones and dividing by three, V has
maximum L>=3; set b=L-2. Its ordinary conjugate, in ascending order, must
have exact length L, its first two entries must be 1,2, and its third
entry must be at least2. If L>=4, its fourth-minus-third gap must be at
least3, and every later gap must be at least2. The putative inverse is

`s=#1`, `nu_1=lambda_3-2`,
`nu_j=lambda_(j+2)-(2j+1)` for j>=2,

with mu=(1,1+s). The gap conditions imply nonnegative ascending nu.
Conjugation and subtraction would then give both inverse identities.

Here are the author checks supporting investigation; they await distinct
criticism and have no finite run behind them. The sum of the displayed
lambda is `(b+1)^2+1+sum(nu)`. Its output weight is consequently
`3(b+1)^2+3+s+3sum(nu)=Q(2,b)+2+s+3sum(nu)`.
The top two V levels L,L-1 have multiplicity one. Level L-2 has
multiplicity nu_1 and may be absent; level L-3, if present, has
multiplicity at least3, and every lower level at least2. Thus at most one
interior level is omitted. A jump by two multiple-of-three levels has
decoded height difference at most four (the successive one-level
differences are2,1,2 periodically). For b=1,nu_1=0 the minimum is6,
whose terminal height is3. Otherwise the minimum is3. Appended ones
are therefore also compatible with literal U.

The intended disjointness from the retained A3 image has simple apparent
certificates: A2 and its zero-first-mu wall require every lower level
through the maximum to have multiplicity at least2, whereas here the
second-highest level has multiplicity1. The maximum is at least9, so the
A1 and third-single 6/8/10 branches are excluded. At maximum9 this clue
always includes6, excluding the third-single9 and A1-9 branches; at
maximum12 it always includes9, excluding the third-single12 branch.
Higher maxima are outside all third-single images. A separate critic
must check these claims and all endpoint/exception conventions before
this clue can be reused as an accepted map.

The next exact lemma is a uniform recovered contour defect for arbitrary
first mu k>0, including its interaction with nu and with all existing
branches. Merely absorbing2k into an ordinary gap-two contour fails the
recorded capacity obstruction at nineteen; the new two-singleton top
pattern changes that contour class. Nothing here handles arbitrary k,
a>=4, the full F_C grammar, or the three-phase nested-hook target arms.
