# RR003: the fixed-count quotient lift is impossible

**Refuted structural proposal; universal finite-fiber obstruction.** The
restricted injection in recursive-source-seed.md is valid on its literal
domain. It cannot be lifted to every quotient-decorated source while
retaining exactly the same residue-count rule. This is a counterexample
to that specified lift, not to every product-side recursion or KR1 map.
No third mechanism, extra review or changed objective is introduced.

## Precise proposal and direct counterexample

The proposed lift retains the counts 4^x 5^(2q+r) ->
2^(2x+r) 3^(q+r) 7^q, leaves the original counts of residues 3 and 6,
and redistributes only the nine-block quotients. It may redistribute those
quotients by any algorithm, not merely the naive sorted attachment.
Set x=0,q=1,r=0 and take two original residue-three parts, no residue-six
parts. The base source is (3,3,5,5), weight16. Its quotient weight two
adds eighteen, giving these five distinct actual P3 sources of weight34:

    (3,5,5,21), (5,5,12,12), (3,3,5,23),
    (3,3,14,14), (3,5,12,14).

The fixed count rule requires every image to have exactly three residue-three
parts and one residue-seven part, with no other residues. Its base is
(3,3,3,7), also weight16. The complete list of weight34 possibilities is

    (3,3,3,25), (3,3,12,16), (3,3,7,21), (3,7,12,12).

Exhaustion proof: the quotient sum is two. Assigning two to the seven-row
leaves all three-rows zero; assigning one leaves one quotient in the
three-rows; assigning zero leaves the three-row partitions (2,0,0) or
(1,1,0). These are exactly four targets. There are five displayed distinct
sources, so the pigeonhole principle rules out every injective lift that
retains these counts. The lists are mathematical boundary witnesses;
none is a lookup table defining a candidate map.

The metered recursive-seed-lift-obstruction34 invocation checks only these
nine explicitly constructed objects for sorting, sum and residue counts.
There is no sweep above thirty and no claim that weight34 is the smallest
obstruction to every possible lift. The target exhaustion is the argument
above, not an assumption from a finite generating-function comparison.

Equivalently, writing t for a nine-block, this fiber compares
1/(t;t)_2^2 with 1/((t;t)_1(t;t)_3). Their degree-two coefficients are five
and four. These finite coefficients expose a universal obstruction to the
specified invariant; equality of total KR series cannot repair it.

## Revised extension obligation and learning

A successful product-side adapter must permit the small residue counts
themselves to depend on quotient data, or use other intrinsic states whose
information is recovered by the inverse. Keeping the seed counts fixed
has insufficient capacity. No such replacement is supplied in RR003.
The seed remains a restricted theorem with author-only assurance; its
arbitrary quotient lift and the complete H_(n,r) branch system remain open.

Decisive obligation refuted: preservation of the seed's residue-count
invariant while retaining all quotient information. The justified next
step is to design a genuine quotient-dependent branch and its inverse,
starting with the displayed 5-to-4 obstruction, before extensive code.
Workflow hypothesis, **unvalidated**: comparing the capacity of one exact
invariant fiber can rule out a proposed lift earlier than testing individual
rewrite choices. No broader discovery-rate claim is made.
