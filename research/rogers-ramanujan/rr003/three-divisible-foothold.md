# RR003 mechanism A comparison: ordinary conjugation reaches arbitrary a

**Established conjugation, with a proved author specialization.** No novelty
is claimed. This is another intrinsic restricted representation inside the
existing core/column mechanism, not a third mechanism or a replacement of
the complete objective. It must not be silently combined with the a<=2
marker assignment: their images can disagree. It was derived after the two
critic challenges and has no additional separate review.

## Exact domain and explicit maps

Let U_3 be the entire actual column subfamily with every column divisible
by three. Write p_i=U_i/3 and append p_(L+1)=0. The decoded heights of 3j
are D(3j)=5q+(0,2,3)_r when j=3q+r. Thus a descending column sequence of
these values is valid exactly when every drop p_i-p_(i+1) is in {0,1,2},
including the final drop. A drop at least three changes decoded height by
at least five; a drop one or two changes height by at most four.

Ordinary conjugation sends p to a partition w with all multiplicities at
most two. Conversely every such w has a conjugate p with these drops.
Consequently

    A_3 = 3 * reverse(conjugate(U/3))
    U_3 = 3 * conjugate(reverse(A_3/3))

are explicit mutually inverse weight-preserving algorithms. Here A_3 is the
entire gap subfamily with parts divisible by three: its predicates reduce
exactly to multiplicity at most two. The maps are just classical partition
conjugation after scaling, not a claimed new KR1 solution.

## Intrinsic statistics without an endpoint black box

The drop d_i=p_i-p_(i+1) is the multiplicity of part 3i in A_3. Therefore

    a = number of drops equal to one,
    b = number of drops equal to two.

This recovers both statistics from U itself for unbounded a,b. Scan the
drops in increasing i. Maintain u earlier single drops and v earlier
double drops. At a single drop record

    mu_u = 3i-3v-2u-1.

At a double drop record

    nu_v = 2i-1-2v-u.

Then increment the corresponding counter. These are exactly the intrinsic
gap–C coordinates proved in endpoint-cluster-merge.md. They are nonnegative
ascending vectors of exact lengths a,b and have weight
Q(a,b)+|mu|+3|nu|. The inverse merges this C to A, requires every part
divisible by three, and conjugates back. Unsupported C are explicitly outside
this restricted image; no enumeration or matching is used by either map.

All a,b occur. For any a,b choose the valid A_3 containing pairs (3j,3j),
1<=j<=b, followed by singles 3(b+i),1<=i<=a. Its C has
mu=(2,3,...,a+1), nu=(1,...,1), with empty vectors allowed. Its U is the
sequence of 3(a+2b),3(a+2b-2),...,3(a+2), followed by 3a,3(a-1),...,3,
omitting an empty range. Its weight is
3b(b+1)+3ab+3a(a+1)/2. This family does **not** claim zero-increment
Q-cores: its increments are explicitly as displayed. The earlier reviewed
a=0 arbitrary-b core theorem remains the Q-core foothold.

## A reversible operation that changes the cluster counts

Append a column 3, i.e. a final level one. This always keeps U_3 valid and
adds exactly three to weight. On A_3 it increases the largest part by three,
as follows directly from conjugation. If the original final level was one,
a,b are unchanged. If it was two, its final drop two is replaced by two
single drops, so (a,b) becomes (a+2,b-1). Empty input becomes (a,b)=(1,0).
The inverse removes one final 3 exactly when the remaining literal U_3 is
valid; this membership test is intrinsic, including the terminal height.
No saved operation history is needed. In particular U=(6) maps to the
pair (3,3); appending 3 gives U=(6,3), mapping to (3,6), and changes
C=(0,1,(),(1,)) to C=(2,0,(2,3),()).

This supplies a coupled singleton/pair operation on an infinite family,
not only fixed-a increment carries. It has a concrete structural advantage
over isolated marker reservations: it covers a whole intrinsic U sector and
permits arbitrarily large a. The map still does not handle columns of
residue one or eight modulo nine.

## Exact extension lemma and relation to the other results

The next lemma would extend this conjugation to non-three columns while
retaining their residue and multiplicity information in recoverable single
and pair branches. Appending one or two unit columns is reminiscent of the
repaired small-charge insertion, but no compatible arbitrary-multiplicity
extension is proved. In particular, the literal U_3 assignment differs from
the marker map: U=(6,3) has C=(2,0,(2,3),()) here, whereas the marker map
assigns that C to U=(8,1). They cannot both define one global function.
Neither is protected from replacement when a better global invariant appears.

Smallest useful falsifier for a colored extension: two different remainders
or cores giving the same intrinsic drop data, or a decoded terminal height
at least five. The previous maximum-only failure and recursive weight-43
collision remain relevant information-loss controls. The classical restricted
conjugation itself has a weight-universal proof above, independently of tests.

Workflow hypothesis, **unvalidated**: choose a partial representation that
exposes operations changing the desired statistics, rather than extending
only a fixed low-a sector. This is a mathematical selection hypothesis,
not evidence of a better general research harness or a changed success criterion.
