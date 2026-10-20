---
id: E009
title: "Causal decomposition of hallucination mechanisms"
status: seed
category: reliability
tags: [hallucination, causal-inference, mechanistic-interpretability, interventions]
---

# Causal decomposition of hallucination mechanisms

## Question

Can incorrect factual assertions be explained by separable, experimentally testable failure channels rather than one undifferentiated hallucination score? Can repairing a measured channel predict which architecture change will help?

## Known foothold

[Causal Abstractions of Neural Networks](https://arxiv.org/abs/2106.02997) uses interchange interventions to test proposed high-level mechanisms. [Semantic uncertainty](https://arxiv.org/abs/2302.09664) measures uncertainty across meanings, but agreement or low semantic entropy is not proof of truth. [Kalai and Vempala](https://arxiv.org/abs/2311.14648) establish a particular statistical obstruction for arbitrary facts; that obstruction should not be confused with every computational failure.

## Proposed gap

**Novelty status: NOT VERIFIED.** Create an identifiable toy causal model of factual answering with controlled information availability, retrieval, composition, decoding, and abstention. Test whether channel-specific interventions predict improvements out of distribution. Existing causal tracing, activation patching, factual editing, and error taxonomy work must be compared at full-paper depth.

## Mathematical setup

A synthetic world W generates evidence E and query Q. Internal variables include retrieved support R, composed proposition C, proposed answer A, and accept decision D. Truth is an explicit relation T(W,Q,A). Randomized interventions replace R with oracle support, C with a correct derivation, or the decoding/acceptance stage with specified alternatives. Treat channel interactions as part of the model; a sum of channel scores is not automatically a probability decomposition.

## Unproved theorem targets

1. **Unproved:** Under declared exclusion, consistency, and positivity assumptions, identify causal effects of channel interventions on false assertions. Show which effects cannot be identified from passive accuracy/confidence observations alone.
2. **Unproved:** For a restricted modular architecture and bounded interaction terms, derive a bound on the change in false-assertion risk after jointly repairing two channels. State why the bound may fail in an entangled network.

## Counterexample or obstruction

Oracle evidence can alter the input distribution and induce a new failure. An intervention may change several mechanisms at once. A model can confidently repeat one coherent false answer. An apparently irrelevant module may carry information through an unexpected path, invalidating the causal abstraction.

## Minimal falsification experiment

Generate small knowledge graphs with independently controlled missing facts, misleading distractors, and composition depth. Randomize oracle substitutions and test predicted versus observed repair effects. Reject the decomposition if interaction effects overwhelm the claimed attribution or if held-out interventions contradict it.

## Success and cost metrics

False assertions per answered query, coverage, intervention effect estimates with uncertainty, cross-world prediction accuracy, explanation fidelity, repair compute, and annotation/oracle cost.

## Next artifact

A causal graph, an identifiability table, and a finite dataset where the world state makes every factual label computable.
