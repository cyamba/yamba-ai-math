---
id: E013
title: "Agent communication topology under correlated mistakes"
status: seed
category: agent-systems
tags: [multi-agent, topology, covariance, debate, reliability]
---

# Agent communication topology under correlated mistakes

## Question

When does communication help a team of small models, and when does it merely synchronize their mistakes? Can a sparse topology preserve independent evidence while concentrating communication where it has measurable value?

## Known foothold

[Multiagent debate](https://arxiv.org/abs/2305.14325) reports task-specific improvements from interaction. [Sparse communication topology](https://aclanthology.org/2024.findings-emnlp.427/) is already an explicit research direction. [Ha and Mitchell, 2026](https://proceedings.mlr.press/v306/ha26a.html) study answer-revision dynamics and report that interaction can also overturn correct answers. More agents and more agreement are not universal evidence of higher reliability.

## Proposed gap

**Novelty status: NOT VERIFIED.** Optimize topology against an empirically identified model of error correlation and social influence, with independent-evidence rounds before interaction. Seek guarantees for a narrow stochastic process, then test whether real agents satisfy its assumptions. Distributed detection, consensus, correlated ensembles, and existing debate topologies are close prior art.

## Mathematical setup

Each agent receives an evidence channel and emits an answer estimate. Initial estimation errors have covariance Σ. Messages update estimates through a specified graph-dependent operator, with a separate innovation term for new evidence. For m > 1 equal-variance equicorrelated initial errors, positive semidefiniteness requires −1/(m−1) ≤ ρ ≤ 1. The elementary variance calculation gives Var(mean) = σ²[ρ + (1−ρ)/m]; fixed shared positive correlation leaves a variance floor as m grows. Admissible negative correlation can instead reduce the variance, even to zero at the lower boundary. This is motivation, not a complete model of language-model debate.

## Unproved theorem targets

1. **Unproved:** For a defined linearized update process with biased agents and correlated innovations, derive final risk as a function of topology, rounds, and evidence overlap; characterize regimes where adding an edge increases risk.
2. **Unproved:** Under explicit innovation and influence assumptions, show when a budgeted sparse graph improves a specified error/cost objective over independent voting and fully connected debate. Do not assume agent errors remain independent after messages.

## Counterexample or obstruction

All agents may share one missing fact or false premise. Fast consensus can lock in a biased influential agent. Repeated model samples are not independent experts. A topology optimized on one task distribution can transmit errors under shift.

## Minimal falsification experiment

Use synthetic evidence channels with controllable overlap and bias, followed by a small exact-answer reasoning suite. Compare independent voting, a star, ring, random sparse graph, and dense debate with equal generated-token and latency budgets. Reject the process model if its predicted harmful edges or correlation trends fail on held-out interventions.

## Success and cost metrics

Correctness, correct-to-wrong revisions, covariance/effective diversity, evidence coverage, communication tokens, critical-path latency, and total model-call cost.

## Next artifact

A covariance propagation derivation and a topology benchmark specification including a shared-bias stress test.
