---
id: E011
title: "Risk control for adaptive retries, retrieval, and agent stopping"
status: seed
category: reliability
tags: [sequential-statistics, calibration, martingales, agents, abstention]
---

# Risk control for adaptive retries, retrieval, and agent stopping

## Question

When an agent keeps sampling, searching, and revising until something looks convincing, which reliability guarantee still holds? Can the system spend an explicit error budget alongside its computation budget?

## Known foothold

[Time-uniform confidence sequences](https://arxiv.org/abs/1810.08240) provide tools for inference valid across stopping times under stated process assumptions. [Conformal factuality](https://proceedings.mlr.press/v235/mohri24a.html) provides a language-generation foothold. A marginal guarantee on one fixed procedure does not automatically survive selecting a result after many adaptive attempts.

## Proposed gap

**Novelty status: NOT VERIFIED.** Develop a sequential accept/continue/delegate policy with guarantees matched to what can actually be observed. The desired novelty is an efficient conditional validity construction for adaptive evidence collection, not an unexplained invocation of conformal prediction or martingales. Recent close work includes [CoFact on covariate shift](https://proceedings.iclr.cc/paper_files/paper/2026/hash/bd074b828bbd782d4bece89306caff84-Abstract-Conference.html) and [conditional factuality control](https://arxiv.org/abs/2603.27403); their full assumptions must be checked alongside sequential conformal and anytime-valid testing before a gap is claimed.

## Mathematical setup

Let Fₜ contain all actions, samples, evidence, and scores observed through step t. Acceptance occurs at a stopping time τ. A guarantee for each attempt must be conditional on the relevant history or justified by an explicit exchangeability/design assumption. A certificate may use labeled calibration data; true factual losses are generally not observed immediately after deployment. State separately whether the target is any false acceptance, average false-assertion rate, or risk conditional on answering.

## Unproved theorem targets

1. **Unproved:** Construct a valid finite-horizon procedure controlling P(any accepted false assertion) ≤ α under explicit conditional certificate assumptions, while adapting retrieval and stopping. Ordinary predictable error-budget allocation is a baseline, not a novelty claim.
2. **Unproved:** Prove a cost or coverage advantage over that baseline for a specified evidence-arrival model, and quantify sensitivity to calibration shift or verifier misspecification.

## Counterexample or obstruction

Repeatedly querying the same biased verifier can amplify false acceptance. Exchangeability may fail after adaptive retrieval. Without labels, an informative oracle, or distributional restrictions, scores alone cannot certify unknown truth. Controlling unconditional errors can conceal very poor conditional risk among answered queries.

## Minimal falsification experiment

Use a finite factual task with controllable verifier bias and correlated retries. Compare fixed sampling, naïve best-of-n, error-spending, and the proposed sequential policy. Sweep retry count, shift, and correlation. Reject the guarantee if its empirical violation probability exceeds the stated bound within justified uncertainty.

## Success and cost metrics

Any-error probability, selective risk, coverage, average and tail stopping time, total verifier/retrieval cost, and guarantee degradation under declared shifts.

## Next artifact

A guarantee taxonomy and one optional-stopping counterexample before designing the sequential architecture.
