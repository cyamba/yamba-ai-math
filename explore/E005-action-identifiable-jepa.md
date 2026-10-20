---
id: E005
title: "Action-identifiable latent prediction beyond observational JEPA"
status: seed
category: world-models
tags: [jepa, identifiability, interventions, nonlinear-ica, world-models]
---

# Action-identifiable latent prediction beyond observational JEPA

## Question

Which action or intervention information makes predictive latent coordinates identifiable enough to support new policies? Can that structure reduce the size of the dynamics model rather than merely yield visually useful features?

## Known foothold

[I-JEPA](https://arxiv.org/abs/2301.08243) predicts representations of masked image regions. [V-JEPA 2](https://arxiv.org/abs/2506.09985) connects video representation learning with an action-conditioned planning model. [Khemakhem et al.](https://proceedings.mlr.press/v108/khemakhem20a.html) establish identifiability for latent-variable models under specific conditional-prior assumptions. [IFactor](https://arxiv.org/abs/2306.06561) already studies identifiable world-model factorization and is particularly close prior work. A predictive loss alone does not inherit either identifiability result.

## Proposed gap

**Novelty status: NOT VERIFIED.** Identify a minimal set of interventions that turns an observationally ambiguous latent predictor into a recoverable modular dynamics model. The proposed result should distinguish identifiability up to an arbitrary invertible map from recovery up to transformations that preserve a useful causal factorization. Identifiable world models and action-conditioned nonlinear ICA are mandatory close-reading areas.

## Mathematical setup

Latent state s follows sₜ₊₁ = F(sₜ,aₜ,ηₜ), and observations satisfy xₜ = g(sₜ) with an injective g in the first model. Assume independent innovations, known intervention targets, sufficient action diversity, and no hidden confounding between interventions and innovations. Define two models as equivalent only under an explicit coordinate-transformation class. Start with linear dynamics and observation before attempting nonlinear encoders.

## Unproved theorem targets

1. **Unproved:** Characterize the remaining equivalence class of linear latent dynamics under partial action interventions and persistent excitation. State exactly when block structure is recoverable and when only similarity equivalence is possible.
2. **Unproved:** Under additional conditional-independence and variability assumptions, derive a nonlinear identifiability result for a joint predictive/interventional objective, with a finite-sample stability statement if possible.

## Counterexample or obstruction

Two hidden mechanisms can generate identical passive videos but respond differently to action. An unexcited state direction is unidentifiable. Even perfect predictive equivalence may leave coordinate ambiguities that make a purported causal interpretation arbitrary. Real camera observations may not be injective.

## Minimal falsification experiment

Construct two visually indistinguishable systems with different intervention responses. Train observational and action-conditioned predictors across controlled action coverage. Compare recovered interventional predictions, not linear-probe labels alone. Reject the proposed identification assumptions if multiple non-equivalent models fit all available interventional distributions.

## Success and cost metrics

Interventional prediction error, recovery modulo the declared equivalence class, unseen-policy regret, action sample complexity, encoder pretraining cost, latent dimension, and planning latency.

## Next artifact

An ambiguity-pair construction and a linear-system identifiability map identifying the smallest intervention set worth collecting.
