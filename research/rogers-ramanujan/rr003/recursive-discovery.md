# RR003 mechanism B — recursive branch discovery and obstruction

**Status:** two exact attributed representations; one classical restricted
bijection; a proposed insertion **refuted**. No full recursive matching exists
here. This is mechanism B, not a third mechanism or an extra review round.

## Exact separately invertible recursions

Chern–Li v3 section 4.1, Claims 4.1–4.3 gives the seven gap tails
(), (1), (1,2), (1,3), (2), (3), (3,3), in that order. Strip parts <=3
and subtract three from every other part. Their linking sets in this order
are all seven states for 0,1,2,4; {0,4,5,6} for 3,5; and {0,5,6} for 6.
These finite states and edges are inspected prior work, not a new finding.
Reinsertion is tail union (residual+3). Weight changes by |tail|+3*length(residual).

A short direct justification checks only cross-boundary pairs and triples:
inside the residual, translation by three preserves all predicates; a part
beyond its <=3 tail reconstructs to at least seven and cannot violate a
cross-boundary distance-two or adjacency test. For tail (1,3) or (3), any
residual 1 causes an invalid 3,4 pair, and residual (1,2) or (1,3) also has
that 1; the remaining four states work. Tail (3,3) additionally excludes a
residual 2, since 3,3,5 has distance-two gap two, leaving states 0,5,6.
The other four tails permit all states, by the literal pair/triple checks.
Thus this is a disjoint exhaustive recursion, not merely a numerical equation.

Residue partitions strip parts <9, recording the four counts of 1,3,6,8,
and subtract nine from the rest. Inverse reinserts those counts and shifts
by nine. Weight change includes 9*length(residual). Empty residual is allowed.
Both recursions decrease maximum part and weight on every nonempty residual;
empty state is the base case. They are encodings of their own domains, not
a bijection between domains. Auxiliary states for a future match must be
recoverable from the target, not retained as an external transcript.

Same-cutoff empty-residual matching is impossible: at cutoff three and N=4,
B has (1,1,1,1),(1,3), while A has only (1,3). At cutoff nine the first
computed discrepancy is N=11, with 8 product objects versus 7 gap objects.
Preserving ordinary length already fails at N=2: B=(1,1) and A=(2).
These refute those particular branch constraints, not all recursive approaches.
For any fixed cutoff M, gap partitions with maximum <=M have finitely many
parts (at most two in every interval of three consecutive values), whereas B
contains arbitrarily many ones. Hence no weight-preserving bijection can
preserve every fixed maximum cutoff. A future matching must change levels
or retain more intrinsic state than the identical cutoff and ordinary length.

## A genuine, established infinite matching sector

Let B_3 contain residue partitions all of whose parts are divisible by three.
Its parts have the unique form 3s, with 3 not dividing s. Let A_3 be gap
partitions all of whose parts are divisible by three. Such an A partition
has exactly multiplicities <=2: three equal parts violate distance two,
while any unequal multiples of three are at least three apart and every
adjacent sum is divisible by three. This is an equivalence of predicates.

Apply the **classical ternary Glaisher map** after dividing by three. For each
allowed part 3s with multiplicity m, uniquely write m=sum(d_k*3^k), d_k in
{0,1,2}, and output d_k copies of 3^(k+1)*s. Every output part has a unique
3-adic factorization with s prime to three, so these digit groups never
collide. The inverse expands a part 3^(k+1)*s into 3^k copies of 3s.
Weight is preserved termwise; digit uniqueness proves both inverses for every
weight. Division/extraction terminates, and output is in A_3 by the preceding
predicate equivalence. Empty input and zero digits are included.

This is a direct executable residue-to-gap bijection on B_3<->A_3, not the
full KR1 bijection and not a novelty claim. Glaisher's theorem is restated
in Konan, *Weighted Words at Degree Two, II*, Theorem 1; its closing remarks
also explicitly discuss flat-partition interpretations of KR identities.
Inspection: theorem and closing remarks, not all crystal constructions.

## Actual proposed extension: insert one charge

For a core in A_3, write c_j for the multiplicity of 3j (0<=c_j<=2), and
start a charge x=3i+1 with i=0. These rules were invented and explored here;
we make no novelty assertion for related particle insertion methods.

* Single branch, priority first: if i>0 and c_i>0, replace one 3i by
  3(i-1), move i to i+1. A zero column would be omitted.
* Double branch: otherwise, if c_(i+1)=2, move those two copies to 3i
  and move i to i+2; omit the two zeros when i=0.
* Otherwise stop and output the remaining multiples of three and charge 3i+1.

Invariant and partial proof: after the first step, i>=2 and c_(i-1)<=1.
A single step decreases c_i to at most one and raises c_(i-1) to at most two;
a double step has c_i=0, makes it two, and makes c_(i+1)=0. Thus all counts
stay in {0,1,2} and the stated invariant holds at the new index. Each step
preserves total weight and strictly increases i. Nonnegative remaining weight
bounds i by (N-1)/3, proving termination. At stop c_i=0 and c_(i+1)<=1,
which are exactly the additional predicates needed for a single charge 3i+1
to coexist with the three-divisible core. Hence validity and weight are proved.

The proposed inverse would have to distinguish the prior single and double
branches intrinsically. That decisive lemma is **false for these rules**.
All 60 exposed A_3 cores with core weight plus one <=30 had valid, distinct
outputs in discovery. This finite observation did not prove the missing lemma.

## Exact information-loss witness, derived before verification

Two different A_3 cores of weight 42 are

    P=(3,3,6,9,9,12),      Q=(3,3,6,6,12,12).

Both insertions produce the valid gap partition (3,6,9,9,16), weight 43.
Their rule sequences are double,single,single,single and double,single,double.
The final target contains no branch information distinguishing them.

After an identical initial double move, this is the local ambiguity between
three single moves on digit pattern (1,2,1), and single then double on
(2,0,2), at levels 2,3,4. Both leave counts (1,1,2,0) at levels 1..4 and
charge index five. In residue inputs, Glaisher inversion gives

    (1,3^8,6,12)  and  (1,3^2,6^2,12^2),

both literal B objects of weight 43. This refutes even the extension with
exactly one exceptional part 1. It is a derived explicit witness, not a
verification sweep above 30. The raw discovery traces are preserved.

Next lemma for mechanism B: replace these overlapping branches by a disjoint,
exhaustive reversible insertion/deletion scheme whose branch choice is encoded
in the output. It must handle both this single-charge ambiguity and then
arbitrary multiplicities and values of the 1,8 residue classes. Keeping a
transcript or selecting an image by enumeration is not a solution.

Learning: the classical sector supplies a real inverse; the attempted mixed
extension supplies validity and termination but loses reconstruction. This
justifies preserving its failure and preferring the new proved column carry
for round two. Workflow hypothesis, **unvalidated**: comparing local branch
words symbolically may expose collisions beyond an enumerated pilot. No
workflow success-rate claim follows from this one investigation.
