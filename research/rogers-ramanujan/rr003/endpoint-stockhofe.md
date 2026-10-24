# Attributed residue–column endpoint, RR003 final author work

**Established construction, newly implemented here; author-only implementation
and proof audit.** This is Stockhofe's map as presented in [Andrews–Keith,
section 2 and Theorem 6](https://arxiv.org/html/2203.05202v2). No novelty is
claimed. The two scheduled critic challenges preceded this implementation;
there is no separate review of this code. This endpoint does not solve U–C.

## Units and explicit endpoint rules

Let H be the descending decoded heights of a literal U. H is five-flat:
all drops, including the last to zero, are less than five. Its weighted
column sum is sum F(H_i), with F(5q+r)=9q+(0,1,3,6,8)_r.
A five-regular height R_i=5q+r, r!=0, corresponds to residue part F(R_i).

The forward implementation follows the attributed two removal phases,
records each removed amount in **units of five**, and conjugates the
partition of units. This corrects the units in the inconsistent displayed
example already identified in RR002; it does not change the theorem.
The retained nonzero residue word v has a unique minimal five-flat regular
partition L: build upward from the last residue, taking at each step the
smallest integer at least the next part with the required residue. If E
is the descending partition of recorded units, return R=L+5 E' (zero pad).
Its F-values, reversed into ascending order, are the residue partition.

For the inverse start with the residue partition, decode its F-values to
five-regular R and form L from its ordered residue word. Then
D=(R-L)/5 is a nonnegative descending partition. Put E=D'. Starting at L,
process each unit e of E in descending order. If e<=ceil(H_1/5), insert 5e
in sorted order. Otherwise set

    i = max { j : j+ceil(H_j/5) <= e }, with j numbered from one,
    k = e-i.

Add five to the first i parts and insert 5k immediately after them. The
final H gives U by applying F to every height. The algorithm never lists
other partitions or ranks objects. Its only boundary search scans positions
of the current partition, not a weight-indexed lookup or inverse history.
Empty inputs return empty outputs in both directions.

## Boundary lemma for the explicit inverse

Here is the additional argument making the insertion position executable.
Before the first direct insertion the current partition is five-flat, and
every existing multiple of five has j+ceil(H_j/5)>e. Initially there are no
multiples. Write f_j=j+ceil(H_j/5). Flatness implies consecutive f-values
differ by zero or one, and the final value is length(H)+1. Every e is at
most the original number l of nonzero residues, while length(H)>=l.
In the essential branch e>ceil(H_1/5)=f_1-1; hence the displayed set has
a largest element i, with f_i=e and f_(i+1)=e+1. Its H_i is not a multiple
by the invariant. Therefore, for k=e-i, both H_i and H_(i+1) lie in
[5k-4,5k-1]. After lifting the prefix, the new adjacent gaps around 5k
are each in {1,2,3,4}; other gaps are unchanged. Removing this new multiple
without lowering the prefix leaves a gap at least five, so it is essential.
Its new f-value is e+1. All older multiples' f-values increase by one;
thus the invariant persists for the next, no larger unit.

In the direct branch sorted insertion preserves flatness because 5e is
no more than four above the current top and lies above the bottom height,
which is less than five. All later units are no larger, so they also admit
direct insertion. The essential phase is therefore followed by a direct
phase. The last case is exactly the inverse order of the two removal
phases: direct insertions are removed from small to large; essential ones
are removed from top to bottom, each lowering its prefix and recovering
e=k+i. They restore the previous partition and exact unit. This gives both
inverse identities of the attributed map with the implemented units.
All endpoints keep the original nonzero residue word. This is an ordinary
written argument, not a Lean certificate or a new separate semantic review.

## Weight, validity, termination and bounds

Removing 5k directly lowers sum F by 9k. An essential removal of 5k with
i larger parts lowers it by 9(k+i), since F(h+5)=F(h)+9. The recorded unit
is exactly k or k+i. Conjugation preserves sum E, so the final displacement
restores exactly that weight. Insertion reverses the same accounting.
Five-flat validity was proved above; output five-regular heights have
nonzero residues and so yield precisely parts 1,3,6,8 modulo nine.
The residue word determines the minimal regular flat L uniquely, and
R-L is a five-divisible descending nonnegative displacement by its adjacent
residue gaps. Thus the algorithms apply to every actual endpoint input.
Each removal decreases the number of parts and each inverse iteration
consumes one unit of the finite E. All intermediate weighted sums are at
most N and F(h)>=h. Straight scans, counting and conjugation consequently
fit conservative O((N+1)^2 log(N+2)) bit work and O((N+1)^2) auxiliary bits.
These bounds and claims concern this attributed endpoint, not a missing
complete residue-to-gap algorithm. The A–C endpoint is still an obligation.

## Learning and next mathematical step

Decisive obligation: a correct unit-normalized inverse with a terminal
boundary, rather than treating a source theorem as executable code.
Actually supplied: explicit rules and the insertion boundary argument.
Frozen implementation checks will test both full endpoint domains through
12 and then 30; source attribution is established, code assurance is author-only.
Next step: retain this endpoint and return to the unresolved U–C coverage
lemma. Workflow hypothesis, **unvalidated**: implementing an imported
endpoint can expose unit and boundary errors that citation alone would miss.
No workflow success-rate claim or general harness change follows.
