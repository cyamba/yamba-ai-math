---
id: E014
title: "Value of computation for stopping, delegation, and verification"
status: seed
category: agent-systems
tags: [optimal-stopping, routing, decision-theory, economics, agents]
---

# Value of computation for stopping, delegation, and verification

## Question

Can a small controller decide when another model call, retrieval, proof attempt, or specialist is worth its cost? The target is improved utility per total system cost, including a principled decision to stop.

## Known foothold

[RouteLLM](https://arxiv.org/abs/2406.18665) learns routing between model choices using preference data. This is a useful baseline but does not solve every sequential computation-allocation problem or guarantee factual correctness. [Time-uniform inference](https://arxiv.org/abs/1810.08240) offers tools relevant to stopping under explicit statistical assumptions.

## Proposed gap

**Novelty status: NOT VERIFIED.** Couple conditional value-of-information estimates with a risk-constrained stopping policy that can choose heterogeneous actions. The research target is a regret or budget-efficiency result under a declared stochastic environment. Rational metareasoning, contextual bandits, cascades, selective prediction, and cost-sensitive routing require a full prior-art map.

## Mathematical setup

The controller observes history h and chooses stop, retrieve, sample, verify, or delegate. Each action has cost c(a,h), possible observations, and a distribution over final task utility. Define V(a,h) as expected utility improvement relative to stopping, minus cost. Unknown quality is not replaced by self-reported confidence without calibration. Declare whether costs are monetary, latency, energy, or a constrained vector; do not silently add incomparable units.

## Unproved theorem targets

1. **Unproved:** For a finite-horizon, finite-action model with observable delayed correctness and bounded utility, derive a regret bound against an explicitly defined oracle allocation policy when action values are learned from logged interactions with adequate exploration.
2. **Unproved:** Under a specified diminishing-information condition, establish an approximation guarantee for a cheap stopping rule and quantify how correlated evidence or verifier bias breaks that guarantee.

## Counterexample or obstruction

Some tasks require several individually unhelpful calls before a breakthrough, defeating a myopic rule. Historical logs can omit actions needed for counterfactual evaluation. Repeated evidence may look valuable while adding no information. The controller can be larger or more costly than the savings it creates.

## Minimal falsification experiment

Create exact-answer tasks with controllable cheap/expert error correlation and a multi-step information trap. Compare fixed budgets, random routing, RouteLLM-style one-shot routing, myopic value-of-information, and a finite-state optimal policy. Reject the proposed approximation assumptions when the trap induces systematic premature stopping.

## Success and cost metrics

Utility and selective risk at each budget, regret, expert-call rate, controller overhead, total tokens, monetary cost under declared prices, and median/p95 completion latency.

## Next artifact

A small computation-allocation MDP with an exactly computed oracle policy and an explicit definition of the cost objective.
