# RR005 result — 2026-10-24

**KR1 remains unresolved.** RR005 completed two review rounds and closed
without a full U–C root map or complete residue–gap endpoint composition.
It supplies universal intrinsic normal forms on both intermediate domains,
an infinite restricted bijection, and an exact failed continuation. Novelty
is **NOT VERIFIED**. No Lean certification has been performed.

## Retained mathematical claims

| Claim | Status and assurance |
| --- | --- |
| Unit/triple normal forms on all literal U and C | **Proved**, written elementary argument supported by [round-one separate informal review](round-1-review.md) |
| Contextual six-strip and unique `(F root,n1,n3,n6)` normal forms on all U and C | **Proved**, written elementary argument supported by [round-two separate informal review](round-2-review.md) |
| Restricted U–C bijection for exactly all U supported on column values `{1,3,6}`, including empty and arbitrary multiplicities | **Proved**, same second-review assurance; C image is exactly the intrinsic empty-F-root class |
| Injectivity of the union of the specified tentative cost-eight rules P and Q | **Refuted**, exact collision and symbolic infinite family separately reviewed |
| Uniform weight-preserving F_U/F_C root correspondence, full U–C and full KR1 | **Unresolved**, no claimed proof or executable full endpoint map |
| Preferred bounds for supplied strips/normal forms/restricted map | **Proved at conservative elementary-analysis level**, quartic unary work and quadratic auxiliary bits; no bound for the missing root map |
| Novelty or workflow improvement | **Unverified**; no comparative workflow evaluation or novelty audit |

The frozen [first proposal](round-1-proposal.md) gives the unit/triple
operators and inverse proofs. The frozen [second proposal](round-2-proposal.md)
classifies the entire triple-root domains E_U/E_C and gives total injections
R6 on them with intrinsic partial inverses L6. The four U branches include
the exceptional decoded-height replacement `(10,6,2) -> (11,7,3)`; its
universal validity and image separation have a written argument and separate
symbolic review, even though its smallest input has weight 31.

On either full literal domain, strip L1, then L3, then L6, obtaining

    (F root,n1,n3,n6),  |input|=|root|+n1+3*n3+6*n6.

All counts are nonnegative integers. Weight descent proves termination;
the intrinsic predecessor tests prove uniqueness and both normal-form
round trips. Reconstruct in order R6, R3, R1. These are two full-domain
normal-form algorithms, **not a map between their residual root sets**.
They do not yet recover arbitrary C parameters a,b,mu,nu from arbitrary U.

Matching only the empty F roots and preserving the three counts yields the
restricted theorem. It includes the formerly omitted U=(6,3), mapped to
C=(3,0,(0,0,0),()). It coherently replaces incompatible earlier partial
assignments, rather than combining overlapping maps. It does not cover all
C with a<=3. The implementation is [rr005_six.py](../checks/rr005_six.py);
it explicitly rejects unmatched roots.

## Exact obstruction and remaining lemma

The [cost-eight failure](eight-strip-obstruction.md) has two distinct
weight-30 F_C inputs

    X=(2,2,(1,1),(0,0)),  Y=(3,1,(3,3,3),(0,)),

whose proposed P/Q images coincide at

    Z=(4,1,(1,2,2,2),(0,)),  weight 38.

Their source domains are already disjoint, so priority between source
branches cannot fix the collision. The written infinite family is also
separately reviewed. This refutes only that specified union, not all
cost-eight strips, general contextual recovery, or KR1. No cost-eight
operator was implemented or accepted.

The next lemma is an **explicit weight-preserving bijection F_U <-> F_C**
with intrinsic extraction/reconstruction, disjoint exhaustive branches,
termination and both inverse identities. It suffices to extend these chosen
normal forms; no claim is made that every possible KR1 bijection must use
them. The smallest unmatched roots remain U=(8) and C=(2,0,(2,2),()),
of weight eight. Adding that isolated match or another free strip count
would leave the universal lemma unproved. The [continuation plan](NEXT_SESSION.md)
sets the next inverse-first target without starting another run.

## Verification and limits

The frozen author pilots passed through 12 before extension through 30.
The final author and independent critic checks each cover 1,393 U objects,
1,393 C objects, 411 restricted objects on each side, and 31 six raising
edges on each side. They check literal domains, terminal drops, zero padding,
empty input, weights, classifications, collisions, missing restricted images
and both round trips. Equal counts are diagnostics, not a bijection or proof.

First-round sweep inputs stopped at 30, but raising-edge endpoints reached
33. Isolated controls also exceeded 30: the author's frozen weight-31
bridge and critic constant vectors up to input weight 9,081/output 9,084
(its U control reached output 34). The engineering suite replayed the
frozen first-verifier control. These exceeded a strict all-input-and-endpoint
reading of the requested ceiling and are preserved as scope deviations.
Exhaustive input enumeration stayed at 30. The second-round six verifier
and independent critic kept their inputs/endpoints at most 30; C1 and the
weight-38/infinite collision were reviewed symbolically. These exposed
implementation checks are not held-out evidence or universal certification.

The repository suite passed **98 tests** after the final functional changes.
It includes optimized-Python completion failure and refusal to overwrite
evidence. Repository integrity, completion-gate outcome, hashes, commands,
receipt digests and final resource use are recorded in
[verification-summary.json](verification-summary.json) and
[execution.json](execution.json). Raw receipts stay in ignored `.runs/rr005/`;
portable critic scripts are retained in [reproduction/](reproduction/).
The first critic's failed launch and successful rerun are both charged.

Two distinct profiles, sequential mathematical stages, two review rounds
and 16 dispatch proxy units were used. No mathematical disagreement remains
on the scoped retained claims; incompleteness is agreed. Limits, accounting
and measurement limitations are in the [contract](contract.md). The
[reflection](pre-run.md) selected two workflow tweaks; their use here does
not demonstrate an improvement over a comparator.

## Provenance and closure

Fresh branch `codex/kr1-rr005` starts at fetched origin/main `98de713` in
`/private/tmp/yamba-ai-math-rr005`. RR003/RR004 evidence and ledgers, the old
checkout and the unrelated active checkout were preserved. The shared
handoff receives an explicitly dated prefix; its old content is retained
verbatim. Local feedback CY-KR1-001/002 remains PENDING; Drive was not checked.

The U representation and C quadratic weight retain the RR002 attribution
to Andrews–Keith and Kurşungöz. The source statement reinspection and its
limits are disclosed in the first proposal; no imported endpoint theorem
is a premise of these elementary strips. This is a local checkpoint only:
no push, publication, external message, new dependency or paid provider.
The authorized bounded attempt is closed; the full mathematical objective
is not achieved.
