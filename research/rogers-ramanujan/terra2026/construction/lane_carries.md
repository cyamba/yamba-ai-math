# Residue-lane carries and lost-origin counterexamples

Status: the lane lemma is **proved**, author-written and not separately reviewed. The proposed bridge repairs below are **refuted**. Novelty NOT VERIFIED. This is work toward KR1, not an all-charge U–C bijection. The a≤1 and a=2, μ1=0 families independently rediscovered during this attempt are already exactly formulas 1–3 in RR003 `round-1-proposal.md`; they are not new.

## A reversible two-bit carry on every ±1 residue species

Let B be partitions whose parts are congruent to 1,3,6,8 mod 9. For each part value s≡±1 (mod 9), write its multiplicity m_s=4q_s+2d_s+e_s with q_s≥0 and d_s,e_s∈{0,1}. Output e_s copies of s, d_s copies of 2s and q_s copies of 4s. Leave all parts congruent to ±3 mod 9 unchanged.

This is a weight-preserving bijection from B to partitions D with the following intrinsic lane conditions:

* Parts ≡±1 mod 9 have multiplicity at most one.
* Parts ≡±2 mod 9 are even and have multiplicity at most one.
* Parts ≡±4 mod 9 are divisible by four, with unrestricted multiplicity.
* Parts ≡±3 mod 9 have unrestricted multiplicity; no multiples of nine occur.

Here ±2 denotes residues {2,7}, and ±4 denotes {4,5}; these four pairs of residue lanes partition the nonzero classes modulo 9. Inverse: for each s≡±1, read the multiplicities e_s,d_s,q_s of s,2s,4s and replace them by 4q_s+2d_s+e_s copies of s; leave the ±3 lane. Each lane value has the appropriate unique parent s by division. Termination is immediate on finite partitions. Each forward or inverse operation preserves weight term by term. A third binary carry would return to the original ±1 lane because 8≡−1 (mod 9), so it cannot be performed naively without remembering origins.

This lemma is neither a KR1 solution nor a claim of new mathematics: it provides a concrete reversible auxiliary state and identifies where a carry must interact with another input species.

## Three distinct proposed third-lane operations, with exact collisions

Suppose, after the two-bit carry, one tries to repair every pair of equal 4s outputs by replacing them uniformly, leaving the other outputs unchanged. A pair has weight 8s. All examples below are literal legal B inputs; each proposed operation is applied to the actual two-bit carry output and then sorted. In each comparison, the second input has no 4s pair and hence is unchanged by the proposed repair.

1. **Merge to one part:** (4s,4s)→(8s). Inputs 1^8 and 8 both output (8). This already demonstrates why ordinary uncolored base-8 normalization is not invertible when both source levels occur. The ±3 base-2 analog fails on inputs 3^2 and 6, both outputting (6).
2. **Split as (s,7s):** Inputs 10^8 and (10,35,35) both output (10,70). In the latter, 35^2 carries to 70; 35≡8 and 10≡1 mod 9. The missing statistic is whether the 70 came from the third-bit repair of 10 or the second lane of 35.
3. **Split as (3s,5s):** Inputs 8^8 and (10,10,10,10,24) both output (24,40). Indeed 10^4 carries to 40 and 24 is an allowed ±3 part. The missing statistic is whether 40 came from the third-bit repair of 8 or the 4-lane of 10.
4. **Split as (2s,6s):** Inputs 1^8 and (1,1,6) both output (2,6). The 2 is the second lane of 1 and the 6 is an original ±3 part.

These counterexamples rule out the specified **uncolored, otherwise-unchanged** repairs, not repairs with explicit metadata, context, or coordinated rerouting. Moreover, injectivity is not the only issue: the unrepaired carry maps 1^8 to (4,4), violating the close-pair condition; operation 3 maps 1^10 to (2,3,5), and (2,3) is an invalid close pair. A valid replacement of the pair considered in isolation therefore does not preserve global gap validity.

## A complete local obstruction for untagged proportional binary splits

There are only four unordered positive integer splits of 8s into two parts that are integral fixed multiples of s: (s,7s), (2s,6s), (3s,5s), (4s,4s). All four have a concrete problem: the first three collide as above, and the last leaves an invalid equal pair when s is coprime to 3. More generally, for every admissible s divisible by four:

* (s,7s) is also produced by inputs s and (7s/2)^2, since 7s/2≡±1 mod 9;
* (2s,6s) is also produced by inputs s^2 and 6s;
* (3s,5s) is also produced by inputs 3s and (5s/4)^4, since 5s/4≡±1 mod 9;
* (4s,4s) violates the close-pair condition because 8s is not divisible by 3.

The comparison assumes the same unchanged two-bit lane map and no other context. Thus a successful scheme must carry some origin information, use larger or non-proportional rearrangements, or coordinate the rewriting with other species. This is a falsifier for that sharply defined local architecture, not an impossibility theorem for all local or abacus bijections.

## Reversible paired carry that retains the origin

The collisions above suggest retaining the carry quotient in a neighboring source multiplicity. This can be done with an all-parameter weight-preserving involution. Let s be an allowed source part and r≥2 such that rs is also allowed. On the pair of multiplicities (m_s,m_{rs}), write m_s=rq+d, 0≤d<r, and define

    T_r(m_s,m_{rs}) = (r m_{rs}+d, q).

It preserves m_s+r m_{rs} and is an involution, since the next quotient and second coordinate are exchanged back. At the partition level, apply T_8 to disjoint pairs (8^{2j}u,8^{2j+1}u), where u ranges over allowed ±1 parts not divisible by eight, and T_2 to (2^{2j}v,2^{2j+1}v), where v ranges over odd allowed ±3 parts. Each source species appears in exactly one pair; only finitely many pairs are nonzero. This is a total weight-preserving involution of B, with no external tag or lookup, and both inverse and termination are immediate. The quotient and neighboring multiplicity exchange roles, preserving the carry origin.

However it **does not produce a normalized bounded-digit lane**: the lower multiplicity after the move is r m_{rs}+d, so it is <r exactly when the original upper multiplicity is zero. This is forced in the following precise sense: no weight-preserving injection on the pair alone can map *every* (m_s,m_{rs}) to an output with lower multiplicity <r. The two distinct inputs (r,0) and (0,1) both have weight rs, while the sole normalized output at that weight is (0,1). The argument does not prevent borrowing other part values, extra visible colors, or history-dependent routing; these are exactly the resources the global bridge would need to use.

## Reproduction

Run `python3 research/rogers-ramanujan/terra2026/construction/check_lane_carries.py`. It checks 5,461 two-bit-lane round trips through weight 40 and the four named collisions and two validity failures. These tests are bounded corroboration, not a proof of the complete bijection.
