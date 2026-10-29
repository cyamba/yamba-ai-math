---
name: improve-harness
description: Evaluate and improve research-agent prompts, assignments, communication topology, and runtime behavior through controlled comparisons rather than assumed multi-agent benefits.
---

# Improve the research harness

Identify one observed failure or measurable bottleneck in the current harness. Start from [meta/session-log.md](../../meta/session-log.md): a decision reverted twice, or the same difficulty noted in several sessions, is a candidate; register it as a `meta/candidates/` proposal under [meta/protocol.md](../../meta/protocol.md). Preserve the original task and compare one proposed change against the current version plus a simpler baseline when useful. Do not equate a better-looking report, more agents, or lower dispatch proxy cost with better research.

Choose held-out tasks representing the intended use. Separate harness development cases from evaluation cases, and record the versions of prompts, registries, runtime, model, tool access, and budgets. Measure outcomes such as valid proof obligations resolved, independently confirmed defects found, source correctness, useful experiments completed, cost, and latency. Use blind review or objective checks where feasible, acknowledging any judge’s limitations.

Hold information and total resource access constant when testing topology. Vary role prompts, number of agents, communication, or selection policy one at a time unless the hypothesis concerns their interaction. Repeated agreement from the same model family does not demonstrate independent confirmation. Include failure recovery and reproducibility in the evaluation.

Return the hypothesis, controlled protocol, artifacts, observed results or explicit unrun status, uncertainty, and a keep/revise/reject decision. Distinguish a planner’s exact discrete optimum from the quality of the resulting research. Change the harness only as authorized and retain negative cases as regression material when they exercise meaningful behavior.
