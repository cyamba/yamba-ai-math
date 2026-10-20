---
id: E006
title: "Decision-sufficient world models and task-conditioned state quotients"
status: seed
category: world-models
tags: [bisimulation, control, sufficiency, world-models, compression]
---

# Decision-sufficient world models and task-conditioned state quotients

## Question

What information may a world model safely discard for a declared family of decisions? Can a compact predictive representation be sufficient for many tasks without reconstructing every observation or claiming to encode the entire world?

## Known foothold

[Bisimulation-based representation learning](https://arxiv.org/abs/2006.10742) studies behavioral state similarity without pixel reconstruction. [DINO-WM](https://arxiv.org/abs/2411.04983) plans in pretrained visual-feature space. [TD-MPC2](https://arxiv.org/abs/2310.16828) uses a decoder-free implicit world model for control. These provide distinct baselines; an embedding useful for one task can omit information needed for another.

## Proposed gap

**Novelty status: NOT VERIFIED.** Derive a task-family-conditioned sufficiency criterion and a minimal representation budget, then adapt the representation when a new reward or constraint invalidates an old quotient. [IFactor](https://arxiv.org/abs/2306.06561), reward-free state abstraction, successor features, predictive-state representations, and approximate bisimulation may already contain much of the required theory.

## Mathematical setup

Begin with a finite discounted MDP, bounded rewards in a declared family R, discount γ < 1, and a state map φ. States may be merged only if reward differences and abstract transition discrepancies are bounded for every r in R and every permitted action. Separate fully observed state compression from partial-observation belief-state compression. The latter can require an unbounded or continuous sufficient state.

## Unproved theorem targets

1. **Unproved:** Relate an explicitly defined task-family abstraction error to worst-case policy regret, with dependence on γ and transition discrepancy. Compare against existing abstraction bounds before claiming novelty.
2. **Unproved:** For a controlled family of reward additions, prove a lower bound on representation refinement and construct an incremental refinement scheme meeting it within stated storage overhead.

## Counterexample or obstruction

Two states identical under the training rewards can differ on an unseen safety constraint. A constant representation can achieve a degenerate predictive objective. Frozen visual features may permanently discard the object property a new task requires; no dynamics head can restore it.

## Minimal falsification experiment

Use a gridworld with irrelevant visual textures, hidden switches, and a sequence of reward families. Compare reconstruction-based models, fixed feature predictors, task-conditioned quotients, and exact tabular control. Reject universal transfer if a deliberately withheld switch distinction breaks the model; measure whether targeted refinement repairs it.

## Success and cost metrics

Worst-task regret, reward-family coverage, abstraction size, number of refinements, required environment interactions, inherited encoder cost, and end-to-end planning time.

## Next artifact

A small MDP counterexample and a side-by-side comparison of proposed versus existing bisimulation assumptions and bounds.
