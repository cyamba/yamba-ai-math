---
id: E002
title: "Rare facts, conditional entropy, and the true memory budget"
status: seed
category: attention-geometry
tags: [factual-recall, information-theory, memory, long-tail]
---

# Rare facts, conditional entropy, and the true memory budget

## Question

Which factual knowledge can be compressed into reusable rules, and which knowledge requires storing unpredictable bits somewhere? Can a small rule learner plus explicit exceptions outperform a larger parametric memorizer under a transparent total-memory budget?

## Known foothold

[Understanding Factual Recall in Transformers via Associative Memories](https://arxiv.org/abs/2412.06538) studies near-linear parameter capacity for a controlled factual-recall task. [Calibrated Language Models Must Hallucinate](https://arxiv.org/abs/2311.14648) gives lower bounds for certain arbitrary facts under calibration assumptions. These do not imply that all rare facts are unpredictable, or that architecture never matters.

## Proposed gap

**Novelty status: NOT VERIFIED.** Build a task decomposition into shared algebraic rules and irreducible exceptions. Seek a rate-distortion frontier for jointly choosing neural parameters, external memory, and abstention. Existing retrieval-augmented models and information-theoretic memorization bounds may already cover major parts of this proposal.

## Mathematical setup

Entities e have attributes y = fθ(e) except on an exception set. The learning encoder observes training data D and public structure S, then produces a representation of at most B finite-precision bits, counting learned parameters and all external stores. At inference, the decoder receives only that representation, the query, and declared public side information S; it cannot revisit D unless D's storage and access are charged. Condition the storage lower bound on the decoder's free side information, not on encoder-only D, which might already contain every exception. Specify whether unseen entity identifiers are informative. Use a query distribution with a tunable long tail, and score erroneous assertions separately from abstentions. External retrieval may access only the budgeted store, not an uncharged oracle.

## Unproved theorem targets

1. **Unproved:** For an explicit rule-plus-independent-exceptions family, establish a lower bound on B for error at most ε and coverage at least c, in terms of conditional exception entropy. Prove it under a fully specified coding model before considering neural implementations.
2. **Unproved:** Construct a hybrid learner matching that rate up to stated overheads while learning the rule class from a specified sample size. Compare with a fixed parametric baseline algorithm, not every larger network.

## Counterexample or obstruction

Independent random attributes cannot generally be reconstructed from a low-dimensional semantic representation. Unlimited-precision weights invalidate ordinary bit-counting arguments. Moving knowledge into an index does not erase its storage cost; a heavily skewed query distribution can also hide catastrophic tail errors.

## Minimal falsification experiment

Generate modular-arithmetic rules with random exceptions. Sweep rule complexity, exception entropy, tail skew, and memory budget. Compare a small rule learner plus exact exception store, a lookup table, and larger transformers at equal total bits. Reject claimed structural gains if they vanish against the lookup baseline or depend on uncharged identifier features.

## Success and cost metrics

Conditional accuracy and coverage by frequency, total bits including indices, update cost per changed fact, training examples, lookup latency, and error per asserted claim.

## Next artifact

A finite coding-model definition and lower-bound proof attempt, plus a synthetic dataset specification with explicit information access.
