# RR004 execution contract — 2026-10-24

User authorized implementation of the next-attempt plan. Execution begins
2026-10-24 15:26:58 UTC (17:26:58 Stockholm); deadline 17:06:58 UTC
(19:06:58 Stockholm). The preceding preparation is conservatively charged
20 minutes. Total ceiling 120 minutes; new execution at most 100 minutes.
Discovery ends no later than 16:06:58 UTC (18:06:58 Stockholm).

## Unchanged objective and proof gate

Construct explicit weight-preserving mutually inverse algorithms between
residue partitions B with parts 1,3,6,8 modulo 9 and ascending positive gap
partitions A: distance-two gaps at least three, adjacent difference at most
one implies sum divisible by three. Include the empty weight-zero objects.
Completion requires universal validity, weight, termination and both inverse
proofs, executable full endpoint composition and separate semantic review.
Lean certification and exposition remain subsequent obligations.
**Novelty status: NOT VERIFIED.** Preserve established attribution.

Seek one disjoint exhaustive U–C decomposition for arbitrary a. U is the
literal descending weighted-column domain: decode values by
F(5q+r)=9q+(0,1,3,6,8)[r]; consecutive decoded heights, including the last
to zero, differ by less than five. C=(a,b,mu,nu) has ascending nonnegative
vectors of exact lengths a,b and weight
Q(a,b)+|mu|+3|nu|, Q=a^2+3ab+3b^2.
First trace U=(6,3) and C=(3,0,(0,0,0),()). Require intrinsic recovery,
zero-padding, disjoint branches and a universal coverage argument before
broad implementation. Reviewed RR003 restrictions are examples; their
assignments may be replaced coherently. Any reused author-only premise
must receive separate semantic audit within the new review budget.
No recursive-route pivot is included.

## Workflow and resources

Allocate 20 minutes to prior preparation, 40 to discovery, 15 to computation,
30 to reviews/revision and 15 to closing. All lead/critic reasoning,
coordination, file work and computations count against elapsed time.
Stop construction at the discovery deadline if reconstruction/coverage is
absent; preserve the precise obstruction for criticism. Stop earlier when
a decisive failure leaves no justified continuation. Allocations are caps,
not artificial waits, and review rounds are ceilings, not quotas.

At most author/mathematician and one distinct critic profile, one active
mathematical worker at a time, two sequential propose(3)/challenge(2)/
revise(3) rounds, at most 16 dispatch proxies. No nested agents. The
coordinator is the author; its effort is inside elapsed time. Distinct
profiles do not establish independent errors. Freeze each reviewed claim,
argument, executable dependency and exposed cases before verification.

Cumulative computational/enumeration time <=600 seconds, including critic
computations and engineering checks; measured local child peak RSS <=2GiB;
incremental attempt artifacts <=1GiB; >=5GiB free space before provisioning.
The fresh .runs/rr004/enumeration-ledger.json is binding; do not reset or
extend RR003. Bootstrap allowance 15 computational seconds is conservative,
not a measured runtime. All later research computations use rr004_meter.py.
The meter checks child RSS after exit, not a hard OS memory reservation;
model memory/runtime is not observable there. Record this limitation.
Preferred final-map complexity is quartic work/quadratic auxiliary bits;
retain actual bounds and any needed contract revision rather than claiming
that a correct map is invalid solely for exceeding that preference.

## Verification and stopping

Pilot actual domains through weight 12; at most 30 after success. Check
validity, exact weight, collisions, missing images, both round trips,
empty/zero coordinates, repeated columns and terminal drops. These weights
are discovery exposure, not held-out data. Finite agreement, enumeration,
rank matching, hidden lookup and model agreement cannot define or certify
the final bijection. Do not promote restricted results to complete KR1.
Record written proof and its assurance level; preserve disagreements.
Run repository unittest discovery and scripts/check_repository.py after
functional changes. Stop on any cap, exhausted reviews or decisive failure;
record exact proved/refuted/unverified claims and next lemma.

Local only, no push/publication/messages, no dependencies/paid providers,
no deletion of user files. Preserve all existing uncommitted preparation.
Durable mathematics stays in this research folder; raw output in .runs/rr004.
No general harness redesign. Workflow benefits remain unvalidated.
