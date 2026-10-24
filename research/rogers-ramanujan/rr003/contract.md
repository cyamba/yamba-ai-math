# RR003 execution contract

User-authorized 2026-10-24. Start 10:02:35 UTC (12:02:35 Stockholm); hard
deadline 13:02:35 UTC (15:02:35 Stockholm). RR002 local checkpoint: `5eec6bb`.

## Objective and actual objects

The unchanged objective is a complete explicit weight-preserving bijection
between residue partitions B (parts 1,3,6,8 modulo 9) and ascending gap
partitions A (distance-two gap >=3; adjacent gap <=1 implies sum divisible
by 3), with universal validity, termination and both inverse proofs.

Leading intermediates: descending W with multiplicities <=4, periodic
weights (1,2,3,2,1); U obtained by conjugation and F(5q+r)=9q+(0,1,3,6,8)[r].
Decoded heights have every adjacent drop <5, including the last to zero.
C=(a,b,mu,nu) has nonnegative ascending vectors of exact lengths a,b, with
N=a^2+3ab+3b^2+sum(mu)+3sum(nu). Empty objects have weight zero.
Endpoint constructions retain their attribution. Novelty is UNVERIFIED.

## Discovery and reviews

Author instructions explicitly include [exploration rules](../../../explore/AGENTS.md)
and [explore-angle](../../../skills/explore-angle/SKILL.md). Develop at most
two mechanisms: inverse-first U core/increment decomposition; and matched
recursive decompositions with recoverable branch choices. Recurrences are
a research obligation, not assumed. Each record gives rules/conjecture,
inverse, invariant, central lemma, closest inspected construction and
smallest useful falsifier. Other representations require a concrete
mathematical advantage within one of these mechanisms.

Explore small actual objects, traces and boundaries. Mark observations
empirical. Seek a nontrivial infinite core family, intrinsic a,b and at
least one proved reversible operation before extensive implementation.
Freeze a selected candidate before verification. Enumeration may invent
or falsify, but cannot define the final map; no ranking or hidden lookup.

Two sequential pair rounds: root/mathematician propose (3), separate critic
challenge (2), root revise (3). Two profiles, 16 dispatch proxies, no nested
agents. Distinct identities do not guarantee independent errors. Author
discovery is inside proposal. Critic checks coverage, unique reconstruction,
information loss and attribution. Round two may pivot upon a structural
failure; preserve the first proposal and precise obstruction.

Allocation: checkpoint/contract/sources 15 minutes; discovery/selection 35;
first explicit candidate/pilot/review 60; revision or pivot/verification/
review 50; engineering and handoff 20. These are allocations, not artificial
wait requirements; two exhausted reviews may end the run earlier. All lead,
critic, retrieval, coordination, computation and testing time counts.

## Verification, limits and learning

Initial ceiling 12, at most 30 after passing pilot. Check both actual
domains, validity, weights, collisions, missing images and both round trips.
Include empty, zero clusters/increments, repeated columns, terminal
boundaries and RR002 collisions. Previously exposed objects are not held-out.
A bridge needs an unconditional argument and separate semantic review.
Full B<->A completion also needs executable verified endpoints. Lean and
exposition remain subsequent explicit obligations. No finite check proves
universal coverage or novelty. No third mechanism or silent weakening.

Investigation limits: 10800 elapsed seconds; cumulative enumeration <=600
seconds; computational peak RSS <=2147483648 bytes; incremental artifacts
<=1073741824 bytes; preserve >=5368709120 free bytes before provisioning.
Budget runner logs all new discovery/verification invocations; baseline
engineering tests took 2.257 seconds and are conservatively charged 3
seconds to enumeration. Critic must use the same ledger for computations.
Model runtime/RSS is not observable or controlled by Python resource caps.

O((N+1)^4) work and O((N+1)^2) auxiliary bits are preferred targets. A
correct construction exceeding them is retained with actual bounds and
a required contract revision; runtime/storage safeguards remain binding.
No new dependencies/providers, paid adapters, user-file deletion,
publication or pushing. Raw artifacts stay in `.runs/rr003/`.

At each review and final handoff record decisive proof obligation, what was
proved/refuted, why the next step is justified, and one unvalidated
transferable workflow hypothesis. Preserve disagreements. Do not evaluate
broader harness changes here or claim a measured discovery-rate gain.
At stopping report exactly what is proved and the next unresolved lemma.
