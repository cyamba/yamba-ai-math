---
id: E007
title: "Branching latent futures instead of misleading predictive averages"
status: seed
category: world-models
tags: [jepa, uncertainty, stochastic-processes, latent-dynamics, world-models]
---

# Branching latent futures instead of misleading predictive averages

## Question

When a future is genuinely multimodal, can a small predictor preserve the decision-relevant branches rather than average them into a latent state that corresponds to no possible future?

## Known foothold

[I-JEPA](https://arxiv.org/abs/2301.08243) establishes a representation-prediction approach. [DreamerV3](https://arxiv.org/abs/2301.04104) supplies an alternative world-model-and-imagination baseline, while [MuDreamer](https://arxiv.org/abs/2405.15083) explores reconstruction-free predictive learning. These papers do not establish that a particular predictive objective resolves uncertainty in every environment. As an elementary starting fact, squared-error regression predicts a conditional mean when its target representation is fixed.

## Proposed gap

**Novelty status: NOT VERIFIED.** Study a compact mixture or set-valued latent predictor with an explicitly decision-aware branch budget. Seek a mathematical criterion for when one latent prediction is sufficient and when branching is unavoidable. Distributional world models, latent-variable prediction, energy-based models, and risk-sensitive planning are close prior art.

## Mathematical setup

Let Z' conditioned on history h and action a have K separated modes. The representation is fixed initially so that collapse of the encoder cannot trivialize prediction. A planner chooses actions using expected utility or a specified tail-risk criterion. A b-branch predictor approximates the conditional distribution, with costs for branch storage and evaluation. Include an observation model defining which branches are distinguishable from available history.

## Unproved theorem targets

1. **Unproved:** Construct a finite family in which any single-point predictor followed by a specified plug-in planner has positive regret, while a K-branch predictor attains a quantified improvement at bounded extra cost. Restrict the planner explicitly; a point representation could otherwise encode the full distribution.
2. **Unproved:** Bound decision regret using a distributional approximation metric and the utility's regularity, then characterize branch allocation minimizing regret under a fixed budget.

## Counterexample or obstruction

An apparently multimodal latent distribution may be unimodal for the task's value function. Branch count can grow exponentially with horizon. A learned representation can hide a distribution in a point, invalidating a naïve dimensional separation. Unobserved randomness cannot be predicted deterministically.

## Minimal falsification experiment

Use a small partially observed fork environment with rare catastrophic outcomes. Compare conditional-mean, mixture, distributional, and exact-belief planners at equal total computation. Reject the proposed branching advantage if a compact sufficient-statistic baseline achieves the same risk and cost.

## Success and cost metrics

Decision regret, rare-event miss rate, distribution calibration, effective branch count, sample complexity, memory, and planner latency across horizons.

## Next artifact

A finite counterexample to mean-based planning and an explicit sufficient-statistic baseline strong enough to challenge it.
