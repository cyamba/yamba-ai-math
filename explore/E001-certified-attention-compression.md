---
id: E001
title: "Certified attention compression through retrieval margins"
status: seed
category: attention-geometry
tags: [attention, linear-algebra, compression, margins, retrieval]
---

# Certified attention compression through retrieval margins

## Question

Can attention allocate rank and precision according to the distinctions a query actually needs, while certifying preservation of a discrete answer? The target is a smaller retrieval module on structured factual tasks, compared with a specified dense attention implementation at equal training data and inference quality.

## Known foothold

Attention has an associative-memory interpretation with separation-dependent retrieval guarantees in [Hopfield Networks is All You Need](https://arxiv.org/abs/2008.02217). Head dimension can restrict representable attention patterns in [Low-Rank Bottleneck in Multi-head Attention Models](https://proceedings.mlr.press/v119/bhojanapalli20a/bhojanapalli20a.pdf). These are different observations; neither establishes that a low-rank approximation preserves factual answers.

## Proposed gap

**Novelty status: NOT VERIFIED.** Study query-dependent compression with a cheap certificate and an exact fallback. The proposed contribution is a bound relating representation dimension, score perturbation, decoder margin, and actual fallback cost. Random projections, adaptive attention, and approximate nearest-neighbor retrieval must be audited as close prior art.

## Mathematical setup

Let normalized keys be rows of K, values rows of V, and a query q produce logits s = Kq/T. A projection P gives approximate logits and attention output. Assume bounded value norms and a decoder with a certified local Lipschitz bound. Define the correct-answer logit margin separately from the correct-key retrieval margin. The world supplies a unique verifiable answer; the certificate need only preserve the dense module's answer, whose correctness must be assessed independently.

## Unproved theorem targets

1. **Unproved:** For a finite query family with a specified lower retrieval margin, derive a sufficient projection dimension and quantization precision that preserve every answer with probability at least 1−δ. Include all constants needed to compare projection storage with dense storage.
2. **Unproved:** Under a distribution of query margins and a fallback policy, establish an expected-cost improvement at a fixed answer-preservation probability, counting the cost of obtaining the certificate itself.

## Counterexample or obstruction

Almost-tied keys can encode opposite facts. Compression can destroy the decisive direction even when average attention error is small. A low-rank QKᵀ can have a full-rank row-wise softmax. An accurate approximation to a wrong dense model remains wrong.

## Minimal falsification experiment

Generate key-value lookup with controllable intrinsic dimension, near-collision rate, and distractor count. Sweep projection rank and precision; compare fixed compression, certified fallback, dense attention, and exact lookup over held-out keys. Reject the practical premise if certificate plus fallback costs exceed dense inference throughout the intended margin regime.

## Success and cost metrics

Exact answer accuracy, disagreement with dense output, certificate violations, fallback frequency, tail-query accuracy, total stored bits, training FLOPs, and measured latency/peak memory. Report the cost of the dense fallback cache.

## Next artifact

A two-page perturbation lemma and a table comparing it with projection/retrieval guarantees, followed by a collision-controlled lookup harness.
