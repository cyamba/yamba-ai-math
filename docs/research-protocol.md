# Research protocol

Every research brief starts as a **seed**. The initial repository contains ideas and proposed work, not completed studies, established new theorems, or benchmark wins.

## Evidence stages

| Stage | Entry evidence | Required output before the next stage |
| --- | --- | --- |
| `seed` | A potentially valuable question | Explicit problem, motivation, closest known work, falsifier, first investigation |
| `screened` | A recorded primary-literature search and feasibility check | Novelty comparison, clarified assumptions, resource estimate, decision to proceed or park |
| `formalized` | Definitions, quantifiers, task family, baselines, and testable predictions | Complete proof attempt or explicit conjecture; counterexamples; preregistered pilot plan |
| `pilot` | Executed small experiment with preserved configuration and raw outcomes | Reproduction, uncertainty assessment, ablations, cost accounting, decision on stronger validation |
| `validated` | Independent checking appropriate to the claim | Audited proof or robust experiments; known limits; reproducible artifacts |
| `promoted` | A documented decision that the validated result merits sustained development | A scoped article, framework, model project, or software program with owners and acceptance criteria |

Stages describe evidence maturity, not the value of an idea. `parked`, `rejected`, and `superseded` may be used with an explanation and links to the evidence. A promising seed may remain a seed. Experiments do not validate a theorem, and a proof under restrictive assumptions does not validate a practical performance claim.

## Research record

Each investigation should preserve:

- The question, task distribution, information available to each participant, and intended contribution.
- A dated source log with direct links, inspection depth, and distinctions between a paper's claims and our interpretation.
- Definitions and assumptions; a claim ledger labeling established results, proposed lemmas, conjectures, observations, and unresolved objections.
- A novelty comparison against the closest methods, including ways our idea may already be covered.
- Counterexamples and negative results alongside successful derivations.
- A smallest falsifying experiment and its prediction before execution.
- A pinned configuration, data provenance, seeds, baseline tuning allowance, budget, outputs, and deviations from plan.
- Limitations, failure channels, leakage or contamination, execution errors, and the next decision.

Cite primary sources for technical claims. A paper located by title is not a paper whose proof has been checked. Claims of novelty require more than the absence of a familiar keyword.

## Claim-specific checks

**Mathematical claims:** write the complete statement before a proof; expose dimensions, domains, quantifiers, precision, computational assumptions, and dependence on constants. Check edge cases, units, vacuous assumptions, and counterexamples. Record a proof's checker and the limits of that check. Agreement between language models is not formal verification.

**Architecture claims:** distinguish expressivity, optimization, sample efficiency, generalization, robustness, and runtime. Report both model-only and whole-system resources. Compare at fixed resource budgets and at matched quality where feasible. Count memory and retrieval as part of the system.

**Reliability claims:** define truth, evidence support, coverage, and abstention separately. Report error conditional on answering as well as unconditional error. Model verifier failures and correlated errors. Zero observed failures has finite-sample uncertainty.

**World-model claims:** define which observations, actions, and interventions identify the proposed latent state. Test observationally indistinguishable worlds with different consequences. Prediction quality alone does not establish a causal or decision-sufficient representation.

**Harness claims:** use the separate protocol in `meta/`. Do not improve a harness score by weakening the research standards it is scored against.

## A useful investigation report

State the finding first. Include the strongest supported claim, assumptions, evidence, objections, and the decision it supports. Preserve minority conclusions when disagreements remain unresolved. End with one concrete next experiment, proof obligation, or reason to stop. Do not call unfinished work a discovery.
