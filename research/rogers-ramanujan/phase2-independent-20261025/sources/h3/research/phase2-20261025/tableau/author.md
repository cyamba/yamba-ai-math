# Phase 2 tableau author packet

Status: **proved, author-only ordinary combinatorial arguments** for the two
partial injections below; **empirical finite exact evidence** for exhaustive
n=6 agreement and complete bounded matching. Neither a full structural n=6
cancellation nor a general e-positivity proof is claimed. Novelty is unverified.
The packet is for a distinct semantic critic; no formal checker was run.

## Objects, determinant copies and exact scope

Let P be a strict finite poset on distinctly numbered labels. A P-tableau has
partition row lengths, each row is a strict P-chain, and a lower entry is never
strictly below its upper neighbor in P. Let G be the incomparability graph.
The degree inv_G counts edges i<j with j in an earlier row than i. Write T_P(mu)
for these tableaux with weight q^inv_G. The structural arguments below use
only these definitions, transitivity, and, in Theorem B, the stated numerical
label inequalities. They do not assert a chromatic Schur expansion for arbitrary
posets. Numeric checks use the natural unit interval P(h), u<_P v iff h[u-1]<v.

For six vertices, the literal determinant-occurrence inventory gives

    [e_(5,1)] (sum_mu T_P(mu) s_mu)
      = 2 T_P(6) - T_P(5,1) - T_P(4,2) + T_P(4,1,1)
        + T_P(3,2,1) - T_P(3,1,1,1) - T_P(2,2,1,1)
        + T_P(2,1,1,1,1).

Here T_P(mu) denotes its weight polynomial in this displayed identity. The two
T_P(6) copies are distinct determinant sectors, with zero-based permutations
sigma=(0,5,1,2,3,4) and (4,0,1,2,3,5). They are NOT one coalesced positive
object. The implementation calls them row0 and row1, respectively. The other
seven literal sectors, and all sectors for every elementary coefficient
through six, are saved in inventory-through6.json. The identity concerns the
formal tableau sum by definition; its finite agreement with the actual proper
coloring oracle is independently checked, rather than assumed from this identity.

All raw determinant occurrences are retained by (shape,sigma,indices,sign).
For any shape/target with opposite-sign copies, one can pair such copies by
identity on tableaux. This pairing has an immediate inverse, unchanged degree,
and termination in one step. The numeric candidate script uses it before
cross-shape matching, retaining the paired sector records. For e_(5,1), all
nine raw sectors above already have their displayed signs without such pairing.

## Theorem A: two negative sectors cancel structurally

For every strict finite poset P on n>=6 numbered labels there is an explicit
inv_G-preserving injection

    T_P(n-1,1) disjoint-union T_P(n-2,2)
       -> T_P(n-2,1,1) disjoint-union T_P(n-3,2,1)
          disjoint-union (two distinguished copies of T_P(n)).

This is a weighted-set statement, independent of which signs those shapes
have in other determinant coefficients. Its application to the displayed
signed coefficient is specifically n=6. The executable code is tested only
at n=6. The proof below supplies the n>=6 argument; this is not a test-based
extension beyond six.

### Forward rule on the hook

Write the source as (A,y);(z), with A a chain of length n-2 ending at x. If
x<_P z and y,z are comparable, all n labels form one chain. Send the source
to the one-row chain with copy row0 when z<_P y, and copy row1 when y<_P z.
Otherwise keep A and insert y into the two-entry singleton leg:

    (A;(z);(y)) if z<_P y,
    (A;(y);(z)) otherwise.

The retained arm is a P-chain. The first leg cell has no P-descent against
the corner: z already satisfied the source condition and y lies above the
corner in P. The second leg cell cannot be below the first, by the insertion
test and asymmetry. Moving y changes row order only with entries in A, all
comparable to y, and possibly with z when z<_P y, also comparable. Thus no
G-edge contribution changes. A full-chain image has degree zero.

Given a valid target K=(A;(s);(t)), the exact hook image language is the
disjoint union of

    H1: s<_P t, x<_P t, and not x<_P s;
    H2: x<_P s, and s,t incomparable.

In H1 recover (A,t);(s); in H2 recover (A,s);(t). To see completeness, there
are only two possible extracted entries. Both could be eligible only when
x<_P s<_P t, precisely the full-chain ambiguity redirected to row0/row1.
The two full-chain copy inverses are respectively

    row0: (chain[:-2],chain[-1]);(chain[-2]),
    row1: (chain[:-1]);(chain[-1]).

Both sources are valid, including their first-column condition, and reproduce
their tags. These are entry formulas, with no search over tableau families.

### Forward rule on the two-row shape

Write the source as (A);(a,b), where A has length n-2, ends in x, and its
penultimate entry is w. Ordinarily split the bottom row:

    (A);(a);(b).

Splitting a comparable pair preserves degree and tableau validity. This image
could collide with the hook rule exactly when

    x<_P b and not x<_P a.                         (C)

Indeed a<_P b already holds. The H2 hook image requires incomparability of a,b,
so is impossible here; H1 is exactly (C). When (C) holds, redirect instead:

    R1: (A[:-1]);(a,x);(b)                  if a<_P x;
    R2: (A[:-2],b);(w,x);(a)                otherwise.

In R2 the entries a,x are incomparable because (C) also excludes x<_P a.
For n>=6 the retained prefix A[:-2] has length at least two, which is essential
for the second-column condition in R2. The rule need not work at n=5.

R1 is valid: its new second row is a<_P x, and x was above the retained arm;
b cannot be below a because a<_P b. All new row-order changes cross comparable
pairs: x versus the retained arm and a, and a versus b. In R2 the top row is
a chain because prefix<_P w<_P x<_P b. The second row w<_P x is a chain.
The first two column checks follow from the old arm chain. The bottom a cannot
be below w, for that would imply a<_P x, contradicting this branch.

For R2, compare every changed pair. Prefix entries cross only w,x,b, to which
they are comparable. The entry b crosses w,x and a, all comparable to b.
The potentially incomparable pairs (a,w) and (a,x) remain in the same strict
row order (w,x above a) as in the source. Hence degree is unchanged; numerical
label order makes no extra assumption in Theorem A.

### Intrinsic inverse and disjointness

For a valid K=(A;(s);(t)), recover the hook using H1/H2 above. Otherwise K
is the unredirected two-row image exactly when

    s<_P t, not t<_P A[1],
    and NOT (x<_P t and not x<_P s).

The second-column condition not t<_P A[1] is essential. Recover (A);(s,t).
These hook and split image languages are disjoint by the collision test.

For a valid J=(R;(s,t);(z)) of shape (n-3,2,1), R1 is recognized by

    R[-1]<_P t<_P z.

Its inverse is (R,t);(s,z). R2 is recognized by

    R[-2]<_P s, t<_P R[-1], z<_P R[-1],
    and z,t incomparable.

Its inverse is (R[:-1],s,t);(z,R[-1]). The R1 and R2 image languages are
disjoint because one requires t<_P z and the other incomparability. The
displayed conditions plus target validity give exactly the needed source
chain and column conditions and the original branch test. Thus every
recognized target recovers one valid source and reproduces the target.
All rules and inverses use bounded entry operations and terminate immediately.

## Theorem B: a three-label rotation resolving a smallest collision component

On six distinct numbered labels u,v,a,b,c,d assume

    c < v < b numerically;
    u<_P v, u<_P c, a<_P c<_P b, a<_P v;
    c and v incomparable; b and v incomparable;
    not a<_P u, not d<_P b, not d<_P c.

Consider the two negative tableaux

    S0 = ((u,v),(a,c),(b),(d)),
    S1 = ((u,v),(a,b),(c),(d)).

The assumptions imply both are valid. Send

    S0 -> K = ((u,v),(a),(c),(b),(d)) in T_P(2,1,1,1,1),
    S1 -> J = ((u,c,b),(a,v),(d))     in T_P(3,2,1).

The source subdomains S0/S1 are intrinsically disjoint: the second-row corner
is respectively below/above the third-row entry in P. Entries of either target
recover u,v,a,b,c,d directly, so these formulas are injective with a direct
inverse on the exact displayed inequalities. This is a union over all tuples
satisfying the inequalities, not a lookup for one fixed tuple.

K is valid by the displayed chain a<_P c<_P b and the remaining column
assumptions. J has chain rows u<_P c<_P b and a<_P v. Its second column is
valid because v and c are incomparable. If d<_P a then d<_P c by transitivity,
contradicting the assumptions; hence J's bottom column is also valid.

For S0->K, only comparable entries cross. For S1->J, the only changed
incomparability-edge orders are {c,v} and {v,b}. Originally v is above c,
and b is below v; afterward c is above v and b is above v. Because c<v<b,
the first change removes exactly one inversion and the second adds exactly
one. All other changed pairs are comparable: u,c,b form a chain and a lies
below c,v,b. The entry d remains below every other entry in both tableaux.
Thus inv_G is preserved. The numerical label inequalities are indispensable
to this two-edge balance; this proof does not silently discard them.

These images are disjoint from Theorem A. The K shape is new. For J, the
R1 recognizer would require b<_P v, excluded by incomparability. The R2
recognizer would require c<_P a, excluded by a<_P c. Theorems A and B
therefore combine into one structural partial injection, implemented in
structural.py, with the image tests in inverse().

The exact one-cell Hall witness at h=(1,2,4,5,6,6) is

    S0=((1,4),(2,3),(5),(6)),
    S1=((1,4),(2,5),(3),(6)).

Both have degree one. In the frozen one-label relocation family, including
all whole-row permutations, their combined positive neighbor set is just

    K=((1,4),(2),(3),(5),(6)).

Thus no injection using only that family can match both sources, regardless
of greedy order or augmenting paths. Theorem B gives the extra image

    J=((1,3,5),(2,4),(6)),

also of degree one. It changes the row blocks of three labels and lies
outside that one-label neighborhood. This is the concrete meaning of the
three-dimensional/triangular clue here: a three-label routing cycle balances
two inversion-edge crossings. It is not an assertion that embedding volumes
in a Ferrers solid proves a global cancellation.

## Exhaustive numerical results and remaining gap

- Hessenberg counts are 1,1,2,5,14,42,132 at sizes 0,...,6. There are **42 at
  n=5**, **65 through n=5**, and **197 through n=6**. The external script runs
  only 42 size-five vectors, despite printing “65”. Its assertions pass as
  finite statements; it uses a global used_pos set and has no intrinsic inverse.
- The coloring/subset oracle agrees exactly with tableau/DJT expansions on
  all 197 vectors through six. All coefficient polynomials are nonnegative
  in this finite range. This does not settle a universal conjecture.
- At n=6 the full signed e_(5,1) objects total 3,980 negative and 6,800 positive
  across all 132 posets. Family1 matches 3,955, missing 25 sources across 12
  posets; greedy family1 reaches only 3,496. The exact failed neighborhoods
  remain in candidates-through6.json. Unchanged-word recuts (family2 v1) had
  already failed at n=5, including the smaller sibling of the Hall witness.
- Frozen family2 v2 permits relocating at most three labels while preserving
  every retained row block. Both deterministic greedy and augmenting-path
  searches match all 3,980 negative objects. Family3 unrestricted degree-fiber
  matching also matches all 3,980 and serves only as a diagnostic. These are
  finite enumerative matchings; their reverse dictionaries are not structural
  inverses. They do not define or certify the full mathematical solution.
- The explicit structural union above handles **151** negative objects:
  all **19** T(5,1), all **96** T(4,2), and **36** conditional T(2,2,1,1).
  It has 151 distinct valid images, unchanged degree, recovered literal
  sources and exact image recognition checked against EVERY positive target
  on all 132 posets. It uses the two literal T6 copies once each, T411 99
  times, T321 32 times, and T21111 18 times. Zero failures are recorded.

The remaining **3,829** negative sources consist of T(3,1,1,1) and the
unhandled part of T(2,2,1,1). A structural injection into the complement of
the 151 recognized images is not constructed. Do not compose the full finite
matching with this partial rule unless the remaining positive complement is
checked: changing a prescribed partial matching can destroy extension in a
restricted graph. No such extension is asserted here.

## Reproduction, resources and review questions

Every numeric subprocess used ../checks/meter.py. Labels tableau-inventory5,
tableau-candidates5, tableau-candidates5-v2, tableau-inventory6,
tableau-candidates6, tableau-structural6, tableau-coloring6,
tableau-external5 and tableau-structural-triangle6 identify the raw logs.
The scalar summaries and per-poset failures are durable JSON in this folder.
candidate-freeze-before6.json pins rule source after the size-five pilot and
before the first size-six run. structural-freeze.json pins the first partial
rule before its first test. The triangular refinement uses exposed discovery
data and is not held out; freeze.json pins the final author packet before
distinct review. The historical v1 source was reconstructed by exact reverse
edit after its run; no pre-run v1 source pin is claimed.

The critic should challenge the exact inverse languages, the R2 n>=6 column
boundary, the two incomparable edge changes in Theorem B, and the disjointness
of its images from Theorem A. A minimal falsifier is one valid source whose
image is invalid/changes degree, two distinct sources with the same tagged
image, or one positive target falsely recognized by inverse().

Two precise next mathematical obligations: partition the remaining negative
sources into intrinsic collision components; and give a three-label routing
rule whose images avoid the recognized 151-image language without global
used sets. Neither obligation is completed in this packet.
