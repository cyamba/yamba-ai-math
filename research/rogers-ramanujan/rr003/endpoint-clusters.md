# RR003 candidate implementation of the attributed gap–cluster endpoint

**Unverified universal conformance; author-only code.** The endpoint theorem
and cluster idea are due to [Kurşungöz, arXiv:1808.01432v1, Theorem 7,
section 3](https://arxiv.org/html/1808.01432). The code below is a uniform
obstacle interpreter proposed to implement those moves. The two scheduled
critic challenges preceded it. Neither finite tests nor attribution alone
certify that this interpreter correctly covers every case of that theorem.
No new mechanism, review round or novelty claim is introduced.

Every actual gap partition splits intrinsically into close adjacent pairs
and singles: a close pair has equal multiples of three or consecutive parts
3r+1,3r+2; two such pairs cannot overlap by the distance-two constraint.
Index possible pairs by level l: even l=2r gives (3r+1,3r+2), odd l=2r+1
gives (3r+3,3r+3). Incrementing l adds three to the pair weight. Base pair
j (numbered from zero) has l=2j. Base single i has value 3b+2i+1.

Forward C-to-A: form b base pairs, then the a base singles with mu added
coordinatewise. Move pair j, starting at j=b-1 and descending, nu_j times.
A move increments its level once. If the resulting flattened partition
violates the gap predicate, require the immediate next atom to be a single,
subtract three from that single, increment the pair level once again and
swap the two atoms. Repeat until the gap predicate holds. Failure to find
such a single is an explicit obstruction, not an implicit fallback map.

Proposed inverse: split an actual gap partition into its intrinsic atoms.
Process pairs j=0,1,...,b-1, moving each backward until its level is 2j.
A backward move decrements the level; on a gap violation require the
immediate previous atom to be a single, add three to that single, decrement
the pair again and swap. Record the number of completed moves as nu_j.
Finally require all base pairs to be first and in order; recover mu from
the remaining singles by subtracting 3b+2i+1. Require ascending nonnegative
vectors of exact lengths. Every failure remains visible.

Immediate invariant: a completed move changes total weight by exactly
three times its direction. Every extra pair step is canceled by the
single's opposite change of three; each crossed single moves behind the
pair, so at most a crossings occur in one move. Base weight is
Q=a^2+3ab+3b^2, directly summing the base atoms. Pair counts and single
counts are preserved by the formal atom operations. Starting valid and
stopping valid is checked by the literal predicate. These facts do not
yet prove termination on every inverse input or universal injectivity.

**Decisive unproved conformance lemma:** at every required move an invalid
configuration has exactly the advertised neighboring single obstruction;
repeated crossings preserve valid already-processed boundaries and are
reversed in exactly the opposite order. In the backward process every
pair reaches its designated base without overshoot, the recorded nu is
ascending, and the residual singles recover ascending nonnegative mu.
This is stronger than a small-case pass and must be reconciled with every
source case before accepting the implementation. Its smallest useful
falsifier is a literal valid input causing a missing obstacle, overshoot,
invalid vector, weight failure, collision or either round-trip failure.

The candidate is frozen before its pilot; all weights through 30 were
already exposed by discovery. A pilot pass may advance to 30, never to a
universal proof claim. The existing universal source theorem is established;
this proposed interpreter's conformance remains separately unverified.
The U–C coverage lemma, end-to-end bijection, separate semantic review,
Lean certification and novelty verification remain obligations.
