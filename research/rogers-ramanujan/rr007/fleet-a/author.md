# RR007 Fleet A author: full context and the missing fusion

Status: initial author stage completed, 24 October 2026. Full KR1 is **unresolved** and
novelty is **unverified**. Every new lemma below has **author-only informal
assurance**, pending the reserved separate critic. None asserts a U–C map.
The U/C definitions and the 1/3/6 normal forms retain their RR005 reviewed
assurance; the exact F_C grammar retains its RR006 reviewed assurance.

## L1. A complete intrinsic descent word for U

**Definitions.** Reverse the decoded U heights and write
`0=h_0<h_1<=...<=h_L`, with the initial strict inequality only when L>0.
Literal U means `0<=h_i-h_(i-1)<=4` for every i, including i=1. Put
`r_i=h_i mod5`, `r_0=0`, `p=(0,1,3,6,8)`, and

`d_i = #{j:1<=j<=i, r_j<r_(j-1)}`.

The word domain is empty, or a word on {0,1,2,3,4} whose first letter is
nonzero. No further word predicate is imposed. Define its weight by

`wt(r)=sum_i p[r_i] + 9*sum_(j:r_j<r_(j-1)) (L-j+1)`.

**Proved, author-only elementary argument.** The encoding just defined is
a weight-preserving bijection between all literal U and that entire word
domain. Its inverse is `h_i=5*d_i+r_i`, followed by reversing and applying
F to the heights.

Indeed an increment in0..4 crosses a multiple of five exactly when its
residue strictly decreases. Equal residues force equal heights, since a
positive increment of five is forbidden. Consequently
`floor(h_i/5)-floor(h_(i-1)/5)=1_(r_i<r_(i-1))`, and the initial quotient is
zero. This proves the inverse formula for every U. Conversely that formula
gives increment `r_i-r_(i-1)` when the residues do not decrease and
`5+r_i-r_(i-1)` when they do; these lie in0..4. The nonzero first letter
gives positive heights. Every encoded height and every residue is recovered
exactly, proving both inverse identities. Finally
`F(h_i)=9*d_i+p[r_i]`; interchanging the finite sums of descent indicators
gives the displayed weight. Each algorithm scans a finite word once, so it
terminates. Integer magnitudes are at most linear in L plus the input
height. No arbitrary color, rank, search or saved history is present.

This retains all ordered context. It is compatible with the 0/1 descent
energy `epsilon(x,y)=1_(y<x)` but is not, by itself, an invocation of a
colored-bijection theorem. The exact F_U word image is intrinsic: recover U
by the stated inverse and apply the reviewed predecessor-failure tests.
No C output or image closure is supplied by that predicate.

Smallest boundary falsifier if the initial nonzero-letter condition is
dropped: word(0) reconstructs height zero, outside positive U, with weight
zero. Smallest missing next lemma: an intrinsic reversible fusion of this
full ordered word into the C data, or into the exact F_C grammar below.

## L2. A positive gap-coordinate grammar for F_C

This is a constructive restatement of the RR006 grammar, not a new
cross-domain theorem. For a nonnegative ascending mu define
`alpha_i=mu_i-mu_(i-1)`, with `mu_0=0`; define beta from nu in the same
way. The inverse is cumulative summation. Each alpha_i contributes
`(a-i+1)*alpha_i` to weight and each beta_j contributes
`3*(b-j+1)*beta_j`. Thus the following disjoint language is exactly F_C.
Every named free variable is an arbitrary nonnegative integer.

1. Empty, weight0.
2. `a=0,b>=2`: beta_(b-1)=beta_b=0, the remaining beta free. The free
   costs are9,12,...,3b; for b=2 there are no free variables. Base3b².
3. `a=2,b=0`: mu=(k,k), k=2 or3. Weights8 or10.
4. `a=2,b>=1`: mu=(k,k), k in{1,2,3}; beta_b=0 and all preceding beta
   free. Weight `Q(2,b)+2k` plus free costs6,9,...,3b.
5. `a>=3,b>=1`: alpha_a=0, alpha_(a-1)=delta in{0,1,2}; alpha_1 through
   alpha_(a-2) are free. beta_b=0 and earlier beta are free. Weight
   `Q(a,b)+2delta` plus free alpha costs3,4,...,a and free beta costs
   6,9,...,3b.
6. `a>=4,b=0`: alpha_a=alpha_(a-2)=0,
   alpha_(a-1)=delta in{0,1,2}; the earlier alpha are free. Weight
   `a²+2delta` plus free costs4,5,...,a.

**Proved, author-only elementary argument.** For a=0 the terminal triple
equality is exactly the two displayed zero gaps, including b=2 where the
preceding entry is the stipulated zero. For a=2 the two equal mu entries
give alpha_2=0 and alpha_1=k, and the separate b=0 exception removes k=1.
For a>=3 the final equality gives alpha_a=0 and the preceding gap is
alpha_(a-1) in0..2. The extra b=0 equality is precisely
alpha_(a-2)=0. The nu equality is beta_b=0, also at b=1. These are exactly
the four RR006 branches and no new condition. Nonnegative free gaps and
cumulative summation prove both encoding/reconstruction identities and
literal sorted exact-length validity. The weight formulas follow by
counting each gap in every succeeding coordinate. All algorithms terminate
after a+b coordinates.

This grammar gives the exact recursive particle target for a positive
construction: two species of free parts, with costs depending on their
shell a,b, plus one bounded delta. It does not supply a U-side shell cut.
Smallest boundary falsifier of forgetting the a=2,b=0 exclusion is
`(2,0,(1,1),())` at6, which has a six predecessor. Smallest next lemma:
construct disjoint exhaustive intrinsic U word branches with exactly these
shells, bounded delta and free gap costs, and reconstruct the whole word.

## L3. Ordinary sheet Durfee ranks cannot determine the particle counts

Use the context investigator's exact three-sheet representation, retaining
the full row order: at h=5q+r the row is

`P(h)=(3q+clamp(r,0,3),3q+clamp(r-1,0,3),3q+clamp(r-2,0,3))`.

Let lambda^(t) be sheet t and D_t its ordinary Durfee rank. Adjacent sheet
entries differ by at most one, so `D_1-D_2` and `D_2-D_3` each lie in{0,1}.
To see the upper bound, at row D_t the next sheet has length at least
`D_t-1`, hence rank at least `D_t-1`. Each sheet contains its own Durfee
square, so `|U|>=D_1²+D_2²+D_3²`.

**Proved, author-only paper pigeonhole argument.** No weight-preserving
surjection F_U -> F_C can have its two output counts (a,b) determined only
by `(D_1,D_2,D_3)`, even by an arbitrary nonlinear function. The claim does
not restrict how the remaining output coordinates depend on U.

Here is an explicit finite symbolic witness set, with no computation at
these weights. The49 F_C objects with `a=3,...,9`, `b=1,...,7` and both
increment vectors zero are valid by the exact grammar; their distinct count
pairs have weights at most `Q(9,7)=81+189+147=417`. A preimage of any of them
must have U weight at most417. Such a U has D_1<=12: if D_1>=13, then
`D_2>=12,D_3>=11`, forcing weight at least434. At D_1=0 there is one rank
triple, at D_1=1 at most three, and at each D_1=2,...,12 at most four,
because the two successive differences are0 or1. Thus there are at most
`1+3+11*4=48` triples, fewer than the49 required distinct count pairs.
Weight preservation and the proposed dependence force the contradiction.

This strengthens, and does not replace, the context investigator's narrower
failure of a=D_1-D_3. The first version sent during discovery used a looser
121-versus112 bound at961; the refined417 argument above uses the stronger
adjacent-sheet inequalities. Neither version was numerically executed.
The displayed finite set is a sufficient falsifier, not a claim of the
smallest possible weight for this entire recovery class. Multi-level,
oblique or full-boundary statistics are not excluded.

## Construction status and failure accounting

No exact full U–C candidate has been frozen or piloted. L1 and L2 are exact
one-sided encodings; L3 is a narrow obstruction. A context code requires the
whole ordered word or a proven richer cut. Matching the first roots8,10,12
does not define it, and adding seed families does not establish coverage.
The first roots correspond to words(4), (1,0), (2,0), respectively; a future
fusion must account for their different C branches intrinsically.

The RR002 normalization failures, RR003 overlap/lost phase, RR004 fixed
adjacent-charge obstruction and RR005 P/Q collision are preserved. The
context investigator's local-corner collision is recorded in context.md.
None is repaired by deterministic postprocessing of its collided output.
Full endpoint composition is still separate; the relevant old author-only
A/C proof is `rr003/endpoint-cluster-merge.md` and its literal implementation
is `checks/rr003_cluster_merge.py`.

## Positive partial constructions frozen during the active stage

Candidate [A1](candidates/a1-two-singles.md) is an exact partial bijection
for every C with a=2,b=0. Its five arithmetic U branches have literal
intrinsic predicates and both inverse proofs. The frozen pilot through12
passed on25 objects per side. Root then approved the unchanged named script
through30; that check passed on196 objects per side, screening all1,393
literal objects per side. All five branches were reached through30. U
distinct/repeated counts were10/186; C within-vector increment counts were
182/14. These are exact exposed finite checks, not universal evidence by
counting. Its proof is the written branch argument. It recognizes the
empty/8/10 F-root pairs on this family and does not supply the remaining
root parser.

Candidate [A2](candidates/a2-zero-or-one-single.md), derived by the context
investigator and written/executed by the author, is an exact alternative
partial bijection for all C with a in{0,1} and arbitrary b. It conjugates the
shifted odd staircase `2j-1+a+nu_j`, multiplies by3 and adjoins the recovered
one-string when a=1. Its exact image is disjoint from A1. Pilot12 passed
on27 objects per side, including mixed a=1,b=1 and repeated b=2, with all
actual inputs/outputs through12. Its relation to the old empty-F-root map
is explicitly different: that old map cannot be overlaid on this new basis.
The separate A2 file records the symbolic weight13 collision refuting a
naive independent union for a=2,b=1. No such collision object was newly
executed above the pilot bound.

At this point two exact Fleet A variants had been frozen. No full
parser candidate is implied by their union. The next positive construction
obligation is a global interacting single/pair separator. The first mixed
a=2 case already requires this separator to carry allocation information.

The root-approved unchanged A2 extension through30 also passed:206 objects
per side, with U distinct/repeated3/203 and C increment distinct/repeated
182/24. Its profiles included a=0,b=3 and a=1,b=2. These counts are from
the alternative A1+A2 basis and cannot be added to the old normal-form
coverage. A1 and A2 are disjoint, so their precisely stated union has402
objects per side through30; this finite total is not a fraction of the
infinite problem solved.

## L4. A proposed particle-count versus hook-rank invariant fails

This is a symbolic check of a coordinator-suggested heuristic, not a new
candidate. Replace each numerical row u by full cells of weight three and
one final cell of weight one or two when needed. Its ordinary support row
length is `ceil(u/3)`. Define its ordinary Durfee rank explicitly by
`D(U)=max({j>=1:u_j>3(j-1)} union {0})`. Equivalently D counts the
successive top-row/subtract-three hook deletions. Thus all-one strings have
D=1, and rank one is exactly `u_2<=3` for nonempty U. This statistic is not
`max{j:u_j>=3j}`. Let `d(C)=b+floor(a/2)`. The quadratic identities
`Q(2c,b)=3(b+c)²+c²` and
`Q(2c+1,b)=3(b+c)(b+c+1)+c(c+1)+1` suggest, but do not prove, a hook
interpretation. The equality D=d cannot be a complete invariant.

First all-one U strings have D=1, whereas their elementary a=1,b=0
counterparts have d=0. Even after putting that string family aside, the
rank-one U sector and the d=1 C sector have different generating functions.
This can be proved by exact rational-function arithmetic, with no trial at
weight14 or above.

Set `E=(1-q)(1-q³)`. The rank-one U objects other than all-one strings are:
at least one3 and arbitrary1; one6 with arbitrary3/1; one8 with arbitrary
3/1; one9 with a nonempty3/1 tail; and one10 with at least one3 and
arbitrary1. Thus their generating function is

`G=(q³+q⁶+q⁸+q⁹+q¹³)/E-q⁹`.

The d=1 C profiles are exactly (a,b)=(0,1),(1,1),(2,0),(3,0), giving

`H=q³/(1-q³)+q⁷/E+q⁴/((1-q)(1-q²))+q⁹/(E(1-q²))`.

Putting the two expressions over `E(1-q²)` gives numerators
`q³-q⁵+q⁶-q¹⁴` and `q³-q⁵+q⁶`, respectively. Therefore

`H-G=q¹⁴/((1-q)(1-q²)(1-q³))`.

**Proved, author-only elementary algebra.** In particular the proposed
sector identification first differs at14 after the unit strings have been
separated. No pairing of these two entire sectors can preserve weight.
The conclusion excludes that exact invariant, not nested hooks, other
particle profiles, or the full KR1 correspondence. The context parser's
mixed a=2 zero-rigging wall already sends some D=1 U to d=2 C and therefore
does not assume the refuted invariant.

## Final A3 partial map and source grammar

Candidate [A3](candidates/a3-hook-and-wall.md) is the third and final frozen
Fleet A variant. It retains A1/A2 and adds all C with a=3,b=0 and all
a=2,b>=1 with first mu zero. Five intrinsic third-single branches and a
conjugation wall have written validity, exact image, disjointness,
termination, weight and both inverse arguments. These are universal
restricted claims, with author-only assurance, not a full C map. Its
smallest omitted C datum is `(2,1,(1,1),(0))`, weight fifteen.

The complete rank-at-most-one source sector is contained in this map,
using the explicit D definition of L4. Its full image also has higher
ranks. Pilot12 admitted all59 literal objects per side, of which58 U had
rank at most one and one had rank two. That finite coincidence is not
full coverage. The wall, marker10 and marker12 branches were not reached
in that pilot. Root then approved the unchanged named script through30;
all branches were reached and all checks passed. The exposed restricted
domain/image has874 objects per side through30, screening1,393 literal
objects per side. This includes A1's196 and A2's206; it must not be added
to them again. Source rank cohorts were empty1, rank-one546, rank-two327;
all547 rank-at-most-one sources through30 were covered. U distinct versus
repeated cohorts were29/845, while within-vector C increment cohorts
were695/179. These are finite transcription checks; the universal claim
rests on the written branch/conjugation proof.

The context investigator also gave a complete source-only recursive hook
grammar in [context.md](context.md), headed “Exact three-phase recursive
hook grammar.” Its phases are intrinsic depth modulo three. With
`c=(0,2,3)`, `F_t(h)=F_0(h+c_t)-3t` and `d=(2,1,2)`, deleting the top
row and subtracting three from every surviving numerical row sends U_t
to U_(t+1). The code retains top height and small bottom multiplicities;
the inner length contributes3 per row to the hook weight. Its exact
inverse reassembles and tests literal gaps. This is full ordered source
context, not free colors and not a C parser. Its independently pinned
representation pilot through12 passed in all three phases; it did not
consume a cross-domain candidate slot or assert equality of phase counts.

The [unfrozen first-positive-wall clue](candidates/unfrozen-first-positive-wall.md)
records a possible recovered contour for a=2, first mu one and arbitrary
b. It is outside all frozen maps, unexecuted, and not a fourth frozen
variant. It cannot alter A3's stated gap or be added to its retained
results. It is a precise next direction for criticism, with candidate
image, inverse and exceptional b=1 case spelled out.

The central missing lemma is unchanged: translate the complete phased
hook/word context into every exact F_C shell and both unrestricted arm
families, with recoverable nested interactions. The full KR1 objective
has not been achieved, and no endpoint composition to a full A/B map is
presented.
