---
id: E015
title: "Architecture search with compositional mathematical contracts"
status: seed
category: mathematical-methodology
tags: [formal-methods, architecture-search, contracts, theorem-discovery, reproducibility]
---

# Architecture search with compositional mathematical contracts

## Question

Can architectural ideas be searched as compositions of modules with explicit mathematical contracts, so that useful guarantees and known failure cases travel with each candidate rather than being reconstructed after benchmark selection?

## Known foothold

[Structured state space duality](https://arxiv.org/abs/2405.21060) exemplifies an algebraic framework connecting model families and algorithms. [AlphaProof](https://www.nature.com/articles/s41586-025-09833-y) exemplifies formal proof search with machine feedback. Their combination does not already establish automated discovery of better neural architectures.

## Proposed gap

**Novelty status: NOT VERIFIED.** Build a small language of attention, memory, projection, verification, and routing modules. Each module carries a resource function, an approximation contract, and proof obligations for its assumptions. Search for candidates that retain a task-specific guarantee while improving measured cost. Existing proof-carrying code, verified neural networks, program synthesis, and theorem-guided design are mandatory comparators.

## Mathematical setup

A module contract specifies input domain, output relation, perturbation bound, required margins, and symbolic memory/FLOP cost. Composition propagates approximation and failure bounds using explicit rules; dependent failure events require valid conditional reasoning or conservative bounds. A concrete implementation is linked to the abstract operator through a separate refinement obligation. Hardware latency remains an empirical quantity even if operation counts are proved.

## Unproved theorem targets

1. **Unproved:** For a restricted acyclic module language, prove soundness of contract composition relative to stated primitive contracts and implementation assumptions. This is an assurance result, not proof that search discovers an optimal architecture.
2. **Unproved:** On a finite candidate grammar and an explicit task family, characterize search completeness or an approximation guarantee for the cost-quality frontier. Avoid a vacuous theorem requiring exhaustive evaluation of an astronomical space.

## Counterexample or obstruction

Loose Lipschitz bounds can make every composite contract useless. A primitive's input assumptions may fail after a preceding learned module. Formalized floating-point behavior may differ from an ideal real-valued operator. A grammar can exclude the best construction, and proof-search compute can overwhelm any inference savings.

## Minimal falsification experiment

Use a grammar of a few exact and approximate retrieval modules for finite lookup. Compare exhaustive enumeration, unconstrained search, and contract-pruned search with equal search budgets. Reject practical value if contract checking never prunes useful work or rules out the best measured candidates because of conservative bounds.

## Success and cost metrics

Verified versus observed violations, useful-candidate yield, search/proof cost, tightness of propagated bounds, final Pareto frontier, implementation audit burden, and inference amortization threshold.

## Next artifact

A one-page module grammar and three hand-checked compositional contracts, including one deliberately failing composition.
