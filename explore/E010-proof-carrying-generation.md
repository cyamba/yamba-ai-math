---
id: E010
title: "Proof-carrying generation with explicit coverage and trust boundaries"
status: seed
category: reliability
tags: [verification, proof-carrying, hallucination, abstention, formal-methods]
---

# Proof-carrying generation with explicit coverage and trust boundaries

## Question

Can a small generator produce useful answers with checkable derivations in a restricted factual domain, while abstaining efficiently outside its certified competence? Which part of the cost-quality frontier comes from architecture rather than the availability of a checker?

## Known foothold

[Conformal factuality](https://proceedings.mlr.press/v235/mohri24a.html) connects correctness guarantees with backing off the specificity of language outputs. [AlphaProof](https://www.nature.com/articles/s41586-025-09833-y) demonstrates a formal-system-based reasoning approach. Formal proof acceptance and statistical factuality are different guarantees with different assumptions.

## Proposed gap

**Novelty status: NOT VERIFIED.** Design a compact generator whose internal steps align with a restricted evidence calculus, then study the cost of achieving specified verified coverage. The observation that a sound checker rejects invalid proofs is established logic, not the proposed novelty. The possible contribution is a coverage/cost theorem and an architecture making proof search materially cheaper.

## Mathematical setup

Fix a finite relational language, a trusted fact base K, a sound inference calculus, and a bounded proof checker. The model emits an answer plus a proof DAG or abstention. The checker validates derivability from K. A separate relation specifies when K and the formal query faithfully represent the external world and user request. For the first experiment both are generated exactly, eliminating translation ambiguity by design.

## Unproved theorem targets

1. **Unproved:** On a restricted proof family with stated width/depth limits, compare the generator size and search work needed for verified coverage c with a specified unrestricted sequence generator. Include proof serialization, checking, retries, and caching costs.
2. **Unproved:** Bound external false-assertion risk by explicit premise, translation, checker, and pipeline failure terms under stated conditional assumptions. Do not assume those terms are independent or known without measurement.

## Counterexample or obstruction

A valid proof of the wrong formal statement does not answer the intended question. False premises support false real-world conclusions. Proof search may be much harder than checking, and abstaining on everything achieves vacuous safety. Soundness does not imply completeness within a fixed time budget.

## Minimal falsification experiment

Generate bounded-depth Datalog-style queries with machine-known answers and derivations. Compare proof-aligned and generic small models, exact symbolic search, and a larger model under equal wall-clock budgets. Reject the architecture thesis if symbolic search or ordinary verifier-guided sampling dominates its verified coverage.

## Success and cost metrics

Verified coverage, answer usefulness, completeness within budget, proof and translation errors, total generated tokens, checker calls, latency, and trusted-base size.

## Next artifact

A small evidence calculus and a threat-to-validity table separating formal soundness, external truth, coverage, and practical cost.
