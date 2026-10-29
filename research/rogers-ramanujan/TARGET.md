# KR1 pinned target

This file is the canonical completion statement for KR1. Programs pin it by path and SHA-256
(`"target": {"path": "research/rogers-ramanujan/TARGET.md", "sha256": "..."}`, see
[programs/contract.md](../../programs/contract.md)); the harness refuses to plan or dispatch when
the file no longer matches. Changing the statement below is the operator's decision, recorded with
a new hash. A route, representation or decomposition may change; this target does not.

## Statement

Construct explicit weight-preserving mutually inverse algorithms between
residue partitions B with parts 1,3,6,8 modulo 9 and ascending positive gap
partitions A: distance-two gaps at least three, adjacent difference at most
one implies sum divisible by three. Include the empty weight-zero objects.
Completion requires universal validity, weight, termination and both inverse
proofs, executable full endpoint composition and separate semantic review.
Lean certification and exposition remain subsequent obligations.
**Novelty status: NOT VERIFIED.** Preserve established attribution.

## Scope deltas

A result that adds a hypothesis, restricts the domain (a bounded weight, a fixed `a`, a marker
family, one branch) or weakens a conclusion (injective but not surjective, finite agreement) is
`restricted` relative to this target and lists each difference as its scope delta. It is progress
only through a reviewed glue argument that the remaining pieces close the gap.

Source: verbatim from the "Unchanged objective and proof gate" of
[rr004/contract.md](rr004/contract.md), which agrees with the governing objective in the root
`CLAUDE.md`.
