---
id: E008
title: "Multiscale latent dynamics with approximate semigroup consistency"
status: seed
category: world-models
tags: [koopman, semigroups, multiscale, stability, world-models]
---

# Multiscale latent dynamics with approximate semigroup consistency

## Question

Can a compact world model learn stable operators at several time scales and skip unnecessary fine-grained rollout steps without losing control-relevant dynamics?

## Known foothold

[Lusch, Kutz, and Brunton](https://arxiv.org/abs/1712.09707) learn coordinates for approximately linear descriptions of nonlinear dynamics using Koopman ideas. [Structured state space duality](https://arxiv.org/abs/2405.21060) illustrates the computational value of structured temporal operators. Neither guarantees a low-dimensional exact linear closure for arbitrary nonlinear controlled dynamics.

## Proposed gap

**Novelty status: NOT VERIFIED.** Couple learned coarse-step operators with explicit cross-scale consistency and uncertainty bounds, then choose temporal resolution according to the query or planning objective. Compare with model reduction, multirate integration, temporal abstraction, options, and existing Koopman control methods before calling the construction new.

## Mathematical setup

For an autonomous process, define the Koopman action Uₜf(s) = E[f(Sₜ) | S₀=s]. In a suitable Markov setting these operators compose; finite learned matrices AΔ generally introduce a defect ‖A₂Δ−AΔ²‖. For control, index operators by action sequences or use an explicitly stated controlled model. Separate an operator's approximation error from errors in the learned observation-to-latent map.

## Unproved theorem targets

1. **Unproved:** Under bounded operator norms, controlled projection residual, and a stated semigroup defect, bound coarse-rollout error for a finite horizon. Characterize when stability gives a useful bound rather than exponential amplification.
2. **Unproved:** For systems with a specified slow-fast separation, establish when adaptive coarse stepping reaches a target planning regret with less total work than the chosen one-step model, including scale-selection overhead.

## Counterexample or obstruction

Chaotic or unstable dynamics amplify small errors. Non-normal matrices can show transient growth despite apparently safe eigenvalues. A coarse latent model can erase a short event that determines an irreversible outcome. Time-homogeneous semigroup assumptions can fail in nonstationary environments.

## Minimal falsification experiment

Start with stable linear slow-fast systems, then add a threshold-triggered failure and a mildly chaotic system. Compare one-step rollout, independently trained coarse operators, consistency-constrained operators, and a standard numerical integrator. Reject the useful-cost claim when consistency improves its own residual but fails to preserve control outcomes.

## Success and cost metrics

Operator defect, observable prediction error, event recall, horizon-dependent regret, uncertainty coverage, operator storage, training cost, and time per completed plan.

## Next artifact

A telescoping-error derivation with all stability assumptions exposed and a non-normal counterexample that challenges eigenvalue-only reasoning.
