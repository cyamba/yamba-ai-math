# RR002 round 1 — frozen proposal

Status: **conjecture**, frozen before running the candidate tests.
Author: root, mathematician profile; 2026-10-23.

## R1. Row-weight projection and cluster straightening

For W=(p_1,...,p_l), set R(W)=sort_ascending(w_i*p_i), with periodic
w=(1,2,3,2,1). R preserves weight, but its codomain is initially all
ordinary partitions. The candidate route is a deterministic local
straightening of R(W) to an A partition, then the attributed A-to-C
cluster encoder. Each rewrite must preserve weight and fix a canonical
priority; any inverse must recover W without an extra history field.

The first acceptance gate is injectivity of R: any two W objects with the
same R refute every deterministic bridge factoring through this exact
projection, regardless of the later straightening rules. If R is not
injective, do not repair it by arbitrary rank matching. Identify the
missing positional information and retain the exact collision.

Also test direct validity R(W) in A. This is a weaker candidate and may
fail earlier than injectivity.

## R1b. Row count as gap-partition length

An attractive refinement would require a+2*b=length(W). This is proposed
as a falsifiable extra condition, not part of KR1. Compare the full
weight-and-length distributions before attempting any rules that rely
on it. A mismatch disproves this refinement, not a general W<->C map.

## Decisive next step

If the projection loses information, replace it by labelled columns or
run-length data and specify an intrinsic output-recoverable label rule.
Do not spend the construction increment merely re-proving either known
endpoint or a counting identity.

The critic is asked to inspect the exact claims and the relevant primary
sources, independently derive a falsifier or a justified repair, and
challenge whether retained labels could be recovered from C.
