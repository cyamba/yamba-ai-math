# Preserving the whole ordered part word is impossible at positive degree

**Written finite proof, supported by two exact combinatorial calculations;
not Lean and not a counterexample to elementary unimodality.** This is a
post-execution hand exhaustion of the smallest deficient case among the
four disclosed P015 development vectors, ordered by `n,h,D,A`. It is not
claimed smallest among all natural unit interval graphs or all grammars.

Let `h=(2,4,4,6,7,7,7)`. Its graph edges are

```text
12 23 24 34 45 46 56 57 67
```

Thus `M=9`. The poset has height three, with successive bounce contacts
`0,2,4,7`. Fix the **flattened ordered** composition word `A=(3,3,1)`,
which still has sorted type `(3,3,1)`. Define its raw signed sector
polynomial by summing all forest triples with this A, before epsilon
doubling. This sector is not itself an elementary coefficient: the latter
sums all distinct part words with that sorted type.

The full sector polynomial is

`C_A(q) = -q [2]_q^2 [3]_q`.

It follows that the degree-one coefficient of `(1-q)C_A(q)` is `-1`.
No sign-reversing positive-survivor cancellation restricted to this A
can cover all degree-one negatives. The conclusion applies even to
unrestricted matching *within* this sector, so it is stronger than a
failure of a particular A-preserving local rule. It says nothing against
the complete P015 grammar, which can change A.

## Exhaust the possible component sets and compositions

Put `u=[2]_q=1+q`, `v=[3]_q=1+q+q^2`. For fixed component sets and
compositions, the inherited insertion-coordinate formula gives

`(-1)^(3-m) q^cross product_(B,x>min B) [b_x(B)]_q product_B [alpha_B[0]]_q`,

where `b_x(B)` counts smaller graph neighbors in B. A zero b makes the
block empty. This is Tom's existing tree-word/insertion formula applied
to the full marked block; no tree or bounded mark is discarded.

All nine nonempty component-set/composition blocks are:

| Component sets, in order of minima | Compositions | Signed block polynomial |
| --- | --- | --- |
| `1234567` | `(3,3,1)` | `+u^3 v` |
| `123 / 4567` | `(3) / (3,1)` | `-u^2 v^2` |
| `123456 / 7` | `(3,3) / (1)` | `-u^2 v` |
| `124567 / 3` | `(3,3) / (1)` | `-q u^2 v` |
| `123457 / 6` | `(3,3) / (1)` | `-q u v` |
| `123467 / 5` | `(3,3) / (1)` | `-q^2 u v` |
| `123 / 456 / 7` | `(3) / (3) / (1)` | `+u v^2` |
| `123 / 457 / 6` | `(3) / (3) / (1)` | `+q v^2` |
| `123 / 467 / 5` | `(3) / (3) / (1)` | `+q^2 v^2` |

Completeness can be checked without a search. One component gives only
the first row. For two components, the only composition boundaries of A
give sizes `(3,4)` or `(6,1)`. The first component contains vertex one.
A connected three-vertex set containing one must contain two, and is
therefore `123` or `124`; the latter leaves vertex three isolated in its
complement. This leaves only `123 | 4567` for sizes `(3,4)`.

For sizes `(6,1)`, deleting the singleton must leave a connected six-set
containing one. Deleting two or four disconnects it; deleting one violates
component order. Deleting three, five, six or seven gives exactly the four
listed rows. These exhaust the possible singletons.

For three components, sizes are `(3,3,1)`. The same first-component argument
leaves `123`, since `124` leaves vertex three isolated in the remaining
triple. The last singleton must be five, six or seven; singleton four would
precede the remaining triple by minimum and give the wrong component sizes.
These give the last three rows. Every listed induced block is connected.
Its insertion factors and forced cross inversions give the displayed
polynomial, including all marks. There are no other component counts or
composition boundaries.

Summing the table gives

`u^3 v - u^2 v^2 - (1+q)u^2 v - (q+q^2)u v + u v^2 + (q+q^2)v^2`.

Using `1+q=u` and `q+q^2=qu`, the first and third terms cancel, and the
remaining `v^2` terms cancel. What remains is `-q u^2 v`, as claimed.

## Actual positive and negative counts

Before doubling, the positive rows have coefficients `2,8` at degrees
zero and one. The absolute negative rows have coefficients `2,9`.
At effective degree one, epsilon zero retains the base sign, while
epsilon one reverses the degree-zero base sign. Thus there are

`8+2=10` positive states and `9+2=11` negative states.

The missing capacity is therefore an exact cardinality obstruction.
It occurs below `floor(M/2)=4`. The complete forest enumeration and the
independent component-set product calculation agree on all lower-half
first differences for this sector, namely `0,-1,-2,-1,1`.
The component-set calculation enumerates sets and composition boundaries,
not parent forests; the written table independently explains its nine
nonempty assignments. This is not a new independent coloring run.

The full coloring-checked elementary coefficient, retained from P014, is
`q^3(1+q)^3`. Its degree-one first difference is zero. Other ordered part
sectors cancel the displayed deficit. Consequently the promising
degree-zero invariant A **cannot** be imposed on a universal positive-degree
construction. Part order must sometimes change; a successful pivot must
make that change recoverable rather than erasing it. No such universal
pivot, unresolved theorem or new formal certificate is established here.
