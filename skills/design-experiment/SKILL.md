---
name: design-experiment
description: Design a reproducible experiment that can distinguish a proposed learning or agent mechanism from matched-budget baselines and competing explanations.
---

# Design a discriminating experiment

State one primary hypothesis and the observation that would refute it. Define the task distribution, data version or generator, sampling unit, held-out split, success metric, uncertainty method, and stop rule before looking at final test outcomes. Use a small smoke run to validate execution, then retain a separate final evaluation.

Compare a credible baseline and an ablation that removes the claimed mechanism. Match the relevant budget and account for auxiliary retrieval, verification, memory, communication, retries, and training or tuning. Report parameter count separately from total cost and measured latency. Avoid choosing the benchmark or budget after observing which favors the proposal.

Include a failure distribution. For structural bias, break the assumed symmetry; for compression, test rare facts and role binding; for grounded answers, include missing and false evidence and report risk with coverage; for agent fleets, compare a simpler workflow with the same information and resource budget.

Deliver the protocol, at most three primary comparisons, executable entrypoint or implementation obligations, expected artifacts, seeds or repetitions, cost ledger, and explicit acceptance and rejection thresholds. Label a plan, simulation, and measured run distinctly. Preserve negative outcomes; an unrun protocol is not empirical evidence.

Stay within the authorized execution budget. When a missing dependency or resource blocks a run, return the prepared protocol and specific unmet requirement rather than inventing measurements.
