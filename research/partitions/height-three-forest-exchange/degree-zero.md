# A complete degree-zero boundary involution

**Written proof of an elementary established base case; not a novel
unresolved theorem or a Lean certificate.** Prepared in P015 after the first
review, for separate review in round two. It supplies an actual covering
pivot at degree zero, but makes no claim at positive degree.

Let `h` be a natural unit interval Hessenberg vector on `[n]`, `n>=1`,
and let `lambda` be any partition of n with `ell` positive parts. Let
`C_1,...,C_t` be the graph components in increasing label order, and put
`gamma=(|C_1|,...,|C_t|)`. In the complete Tom signed forest space of
type lambda, doubled by epsilon, the degree-zero states admit the following
sign-reversing involution, with fixed points positive:

1. Flatten the ordered component compositions to a part word
   `A=(a_1,...,a_ell)`. Set `P(A)={a_1,a_1+a_2,...,a_1+...+a_(ell-1)}`.
2. Let `F={p<n:h(p)=p}` be the forced graph-component gaps.
3. If `P(A)\F` is nonempty, choose its least element p. Toggle the forest
   edge `p--(p+1)`: split the component at that part boundary, or join the
   two components in their original order. Preserve A, all marks and epsilon.
4. If no such p exists, keep the state fixed.

There is exactly one fixed point if `sort(gamma)=lambda`, and none otherwise.
Consequently

`[q^0][e_lambda] X_G(x;q) = 1 if sort(gamma)=lambda, and 0 otherwise`.

## Why every zero-degree object has this form

All contributions in `D=inv_G(w)+sum(r_i-1)+epsilon` are nonnegative.
Hence `D=0` forces inversion zero, all marks one and epsilon zero.

The graph components are consecutive intervals: if an edge spans a label,
the natural unit interval property connects that label too; unions along
a connected edge path are therefore intervals. The gaps between these
intervals are exactly F. Indeed, `h(p)=p` and monotonicity prevent any edge
from a label at most p to a larger one. Conversely, if `h(p)>p`, the edge
`p--(p+1)` crosses the cut. Each component thus contains every consecutive
edge within its interval.

A forest tree cannot span graph components. Forest components are ordered
by their minima, so the full word concatenates graph components in their
label order. Within each graph component, inversion zero on its consecutive
edges forces `1,...,n` in increasing relative order. Therefore the entire
forest word is `1,...,n`.

Each forest component is consequently a consecutive label interval. The
inverse of the canonical tree word (Tom's Lemma 3.11) makes the unique tree
with increasing word the consecutive path: each vertex except the largest
has the next vertex as parent. Thus a zero-degree object is determined by
its part word A and its cut set K, with

`F subset K subset P(A)`.

The components are the intervals cut by K, their compositions are the
corresponding consecutive blocks of A, and all marks and epsilon are forced.
Conversely every such `(A,K)` is an actual zero-degree forest triple:
K contains every missing consecutive graph edge, so each uncut path edge
is present. The part word has sorted type lambda. Repeated equal parts
create no additional identical A objects.

## Validity, inverse, sign, statistic and survivors

For a chosen `p in P(A)\F`, toggle K to `K symmetric_difference {p}`.
The result still contains F and lies inside P(A). It therefore describes
an actual state. Its ordered part word A is unchanged, even if two
component compositions merge. All marks stay one, epsilon stays zero and
the full word remains increasing, so degree stays zero. The number of
components changes by one, reversing `(-1)^(ell-number_of_components)`.

The chosen p depends only on A and the fixed graph gaps F. Both survive
the operation unchanged, so the inverse chooses the same p. This proves
involution and collision freedom on all nonfixed states, without matching
or a finite search. The edge split/join is already in the inherited edge
grammar; this paper argument is not an additional active P015 primitive
or a replacement of the four frozen experimental selectors.

A fixed state has `P(A) subset F`. Since every actual zero-degree state
also has `F subset P(A)`, equality holds, and K=F. There is one tree per
graph component and one part in each composition. Thus `t=ell`, its sign
is positive, and A must be gamma. Such a state exists precisely when
sorting gamma gives lambda. It is then unique. Every negative state is
therefore paired with a distinct positive state.

For the observed selector collision, the two negative states with parents
`(2,3,0,5,6,7,0)` and compositions `((3),(3,1))` or `((3),(1,3))`
have first part boundary p=3. This pivot joins at `3--4` and gives the
distinct one-tree compositions `((3,3,1))` and `((3,1,3))`, respectively.
The part words make the reverse choice recoverable. This is why a first
legal target that forgets their order can collide while this base-case
pivot does not.

## Independent bridge to actual colorings

In a q-zero proper coloring, every consecutive edge in a graph component
requires strictly decreasing colors along its label interval. All colors
within that component are distinct; all its other edges are then descents
as well. Each chosen color set gives exactly one such coloring. Different
graph components may reuse colors independently. Hence, directly from the
actual coloring definition,

`X_G(x;0)=product_(j=1)^t e_(|C_j|)(x)`.

This independently confirms the survivor formula; the desired expansion
or coefficient inequalities were not assumed. At height exactly three and
lambda `(n-4,3,1)`, a fixed point is possible only for three graph components
of those sizes. The poset is an ordinal sum across components, so height
three then forces each component to be a clique. This is a boundary case
of the target, not a proof of its positive-degree inequalities.

The possible extension "preserve A at every degree" is a separate hypothesis.
Before proposing it as a universal pivot, round two will test its necessary
condition: each `(A,D)` signed space must have at least as many positives
as negatives. A deficit would refute such an A-preserving extension, without
refuting the whole grammar or elementary unimodality.
