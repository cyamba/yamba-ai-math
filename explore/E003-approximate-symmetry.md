---
id: E003
title: "When approximate symmetry justifies a smaller model"
status: seed
category: attention-geometry
tags: [equivariance, representation-theory, geometry, generalization]
---

# When approximate symmetry justifies a smaller model

## Question

How wrong may a symmetry prior be before its reduction in estimation error is outweighed by its bias? Can an equivariant core plus a small residual adapt to the correct amount of symmetry breaking?

## Known foothold

[Elesedy and Zaidi](https://proceedings.mlr.press/v139/elesedy21a/elesedy21a.pdf) quantify a strict equivariance benefit for minimum-norm linear regression with appropriate group, input-distribution, and target assumptions. This is a narrow learning result, not a general transformer guarantee. [On the hardness of learning under symmetries](https://proceedings.iclr.cc/paper_files/paper/2024/hash/6e5112eaa45f8c30b242c5f576213a92-Abstract-Conference.html) warns that symmetry does not generally make optimization easy.

## Proposed gap

**Novelty status: NOT VERIFIED.** Quantify a budgeted symmetry-breaking residual in relational attention, beginning with a tractable linear teacher. The interesting question is an explicit crossover law and an estimator that discovers the crossover without access to the true symmetry defect. Approximate equivariance and subgroup-selection literature require a full audit.

## Mathematical setup

A compact group G acts on inputs and outputs by specified representations. Use an invariant input measure and orthogonal output representations, or explicitly choose an invariant inner product, so the induced action is unitary in the relevant L² function space. Let Q be its orthogonal averaging projector and write f* = Qf* + r, with defect τ² = E‖r(X)‖². Begin with invariant Gaussian input, bounded noise, and a fixed ridge or minimum-norm estimator. Count the dimension of the equivariant linear subspace and a residual subspace of dimension k. For language-like tasks, use permutations of interchangeable evidence nodes, not arbitrary word permutations.

## Unproved theorem targets

1. **Unproved:** Derive an exact or matching-order excess-risk comparison among unrestricted, strictly equivariant, and residual-augmented estimators over a stated range of n, τ, and noise. Identify where constraining the model strictly improves risk.
2. **Unproved:** Establish an oracle inequality for selecting k using independent validation, including the selection penalty. Extend to attention only after the linear result is understood.

## Counterexample or obstruction

The label can depend entirely on a direction removed by averaging. The input distribution may fail to share the proposed symmetry. A nominally larger baseline with suitable regularization may recover the same inductive bias, removing any architectural separation.

## Minimal falsification experiment

Use a permutation-equivariant linear teacher plus a tunable non-equivariant perturbation. Sweep sample size and τ, comparing all three estimators and a properly tuned unrestricted baseline. Then test graph lookup where a small fraction of named nodes breaks exchangeability. Reject the crossover claim if predicted ordering is wrong beyond sampling uncertainty.

## Success and cost metrics

Risk versus τ and n, residual dimension, parameter bits, learning cost, symmetry violation under interventions, and runtime of enforcing equivariance.

## Next artifact

An assumptions-and-projection note reproducing the known linear setup, followed by an approximate-symmetry risk calculation.
