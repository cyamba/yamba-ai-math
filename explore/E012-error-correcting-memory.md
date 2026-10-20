---
id: E012
title: "Error-correcting representations for robust compact memory"
status: seed
category: high-upside-mathematics
tags: [coding-theory, frames, superposition, memory, quantization]
---

# Error-correcting representations for robust compact memory

## Question

Can structured redundancy in a compact representation outperform an unconstrained wider memory at equal total bits when queries, stored values, or arithmetic are noisy? The aim is robustness through algebraic structure, not free information storage.

## Known foothold

[Toy models of superposition](https://www.anthropic.com/research/toy-models-of-superposition) studies sparse features sharing fewer dimensions and the resulting interference. [Robust exponential memory in Hopfield networks](https://arxiv.org/abs/1411.4625) connects robust associative memory with structured constructions. These motivate a coding perspective without showing that redundancy universally reduces language-model hallucination.

## Proposed gap

**Novelty status: NOT VERIFIED.** Co-design a finite-precision memory code, retrieval operator, and lightweight decoder for sparse compositional facts. Compare learned frames with explicit error-correcting constructions under the same storage and noise budget. Coding-theoretic associative memory and sparse recovery may already establish the main capacity claims; the architecture-level learning and cost tradeoff would need its own contribution.

## Mathematical setup

Facts are sparse symbol vectors u encoded by C into m-dimensional finite-precision states. Retrieval returns Cu plus a declared corruption channel: bounded noise, erasures, or limited symbol errors. The decoder either reconstructs u or abstains. Fix a message distribution, code redundancy, precision, and training access. For compositional facts, specify whether legal operations on messages can be implemented in code space without destructive interference.

## Unproved theorem targets

1. **Unproved:** For a chosen sparse-fact family and corruption model, derive a recoverability region in sparsity, coherence or minimum distance, dimension, and quantization precision. Compare it with known coding bounds rather than restating them.
2. **Unproved:** Establish when a structured memory plus decoder uses fewer inference operations at a fixed failure probability than a named learned-memory baseline, counting encoding, decoding, and redundancy costs.

## Counterexample or obstruction

Redundancy consumes storage. Arbitrary dense messages defeat sparse-code assumptions. Structured codes can make semantic updates or relational composition expensive. A smaller representation with a huge decoder can move rather than remove complexity. Exponential pattern capacity is not exponential storage of independently chosen arbitrary facts for free.

## Minimal falsification experiment

Generate sparse symbolic associations with quantization, bit flips, and compositional queries. Compare random frames, learned encodings, an explicit code, associative memory, and an exact store at equal bits. Reject the coding advantage if it disappears after decoding latency and redundancy are counted.

## Success and cost metrics

Recovery and abstention rates versus corruption, false decoding rate, message bits per total stored bit, compositional accuracy, update cost, training cost, and measured retrieval-plus-decoding latency.

## Next artifact

A fully specified corruption model and a capacity ledger distinguishing semantic payload, redundancy, decoder parameters, and external memory.
