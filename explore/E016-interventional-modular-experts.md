---
id: E016
title: "Interventional modular experts for cheap repair and transfer"
status: seed
category: high-upside-mathematics
tags: [causal-modularity, mixture-of-experts, interventions, transfer, identifiability]
---

# Interventional modular experts for cheap repair and transfer

## Question

Can interventions reveal reusable computational modules so that a small routed model adapts to a changed mechanism by updating one expert rather than relearning an entangled larger model? The proposed gain concerns update cost and distribution shift as well as inference.

## Known foothold

[Interchange intervention training](https://proceedings.mlr.press/v162/geiger22a/geiger22a.pdf) trains neural representations toward a supplied causal abstraction. [Compressed Sensing for Capability Localization, 2026](https://proceedings.mlr.press/v306/bair26a.html) provides a recent capability-localization direction. Neither establishes that arbitrary language capabilities decompose into independently repairable experts.

## Proposed gap

**Novelty status: NOT VERIFIED.** Learn a routing architecture aligned with intervention-defined mechanisms, then prove a modular adaptation advantage in a restricted causal task family. Causal representation learning, independent mechanisms, modular meta-learning, conditional computation, and sparse expert specialization are close prior art. The mathematical claim must survive a strong entangled baseline with equivalent information and regularization.

## Mathematical setup

Data arise from a finite structural causal model with k mechanisms. Training environments intervene on known subsets with enough diversity to identify the relevant structure. The learner has k candidate experts, a router, and a declared interface state. A test environment changes one mechanism. Restrict parameter precision and count all experts, including inactive ones; active parameter count is not total model size.

## Unproved theorem targets

1. **Unproved:** Under identifiable interventions, correct interfaces, and a restricted mechanism class, bound samples and parameter updates required to adapt to a single-mechanism change. Compare with a named learner and quantify any extra pretraining cost.
2. **Unproved:** Derive a sufficient routing-error condition under which sparse execution retains the modular adaptation gain and improves total inference cost. Include interface communication and load-balancing overhead.

## Counterexample or obstruction

Mechanisms can be statistically inseparable without diverse interventions. Shared representations may be necessary for efficiency, so forced modularity can increase size. A change in one mechanism may alter the router's input distribution, causing global failures. Apparent expert specialization may be an arbitrary coordinate choice rather than causal modularity.

## Minimal falsification experiment

Generate compositional arithmetic or small causal dynamical systems with one-rule interventions. Compare intervention-aligned experts, an ordinary mixture of experts, dense small/large baselines, and an oracle router. Test held-out mechanism combinations. Reject the modular thesis if gains require oracle routing or disappear against matched information and update budgets.

## Success and cost metrics

Post-shift accuracy, adaptation samples, updated parameter bits, interference with unchanged mechanisms, router error, active and total parameters, full pretraining cost, and inference latency.

## Next artifact

A two-mechanism identifiability example, a router-failure counterexample, and a comparison table separating causal modularity from ordinary expert specialization.
