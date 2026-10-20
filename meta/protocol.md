# Bounded harness improvement protocol

## 1. Register one candidate

Record a stable ID, motivating failure, exact proposed change, hypothesized mechanism, affected files, parent champion revision, allowed tools, budget, expected benefit, likely downside, and rollback method. Prefer a single interpretable change. Declare development tasks before using them and identify which feedback the candidate author has already seen.

Do not change the objective and the method in the same trial. A proposed change to project goals, permissions, spending authority, evidence standards, or this governance boundary needs an explicit project decision outside the candidate's own execution. The meta agent cannot approve its own expanded authority.

## 2. Freeze an evaluation

Create an evaluation manifest before held-out execution. Include:

- Task IDs, versions, content hashes, provenance, and difficulty strata.
- Separate development and held-out IDs, with duplicate and near-duplicate checks.
- Champion and challenger revisions, provider/model versions when applicable, tool access, seeds, and configuration.
- A fixed rubric, scorer/checker versions, hard gates, minimum useful improvement, uncertainty method, and total trial budget.
- How paired outcomes, execution errors, missing artifacts, ties, abstentions, and censored costs will be scored.
- Who can inspect held-out content, score outputs, and decide promotion.

Keep held-out content out of candidate-generation context. This public repository can store manifests, hashes, rubrics, and retired examples; it cannot provide secrecy for published test answers. For a credible held-out study, an independent evaluator must keep active content outside candidate access until scoring is complete. Once exposed, retire or relabel that set and record the leak.

## 3. Run a fair paired trial

Run champion and challenger on the same task distribution with comparable evidence, tools, and measured resource budgets. Pin execution order or randomize it before the trial. Preserve raw outputs, work packets, dependency logs, versions, and scorer decisions.

Use tasks with independently checkable outcomes when possible: theorem error detection, source-grounded claim auditing, known counterexamples, bounded synthesis, or reproducible experimental design. Include open-ended research assessments only with a documented rubric and independent adjudication. This trial estimates performance on its evaluated distribution; it does not certify future scientific discovery.

Fix the sample size or a valid sequential stopping rule before execution. Do not repeatedly inspect a small sample and stop at a favorable result. Count all attempted tasks and resource use, including orchestration and failed calls. Missing data is a limitation, not an efficiency gain.

## 4. Apply gates before tradeoffs

Use the `scorecard.md` hard gates first. A lower cost does not compensate for unsupported factual or mathematical claims. Compare quality and cost jointly; report the tradeoff rather than inventing a universal scalar score after seeing results.

Use paired uncertainty estimates suitable for the outcome type and sample size. Report task-level wins, losses, ties, stratum effects, errors, and disagreement. If many candidates were tried, disclose the search and use a fresh confirmation set for the selected candidate.

## 5. Review and decide

An evaluator who did not author the candidate reviews the preserved evidence and checks for leakage, rubric gaming, regressions, and uncounted resources. A different role prompt alone does not ensure independence if the evaluator sees the author's argument or shares the same failure modes; disclose that limitation.

Possible decisions are `accept`, `reject`, or `inconclusive`. Acceptance requires the preregistered gates and improvement criterion, a usable rollback, and a project-maintainer decision recorded in the ledger. An agent may recommend acceptance; it may not label an unreviewed proposal accepted. Rejection records why; inconclusive trials identify the missing evidence.

## 6. Promote reversibly and monitor

Keep the champion pinned until promotion. Store the prior revision and configuration. After promotion, run the preregistered regression checks and observe a bounded confirmation period. Revert to the previous champion if hard gates fail, hidden costs exceed the declared limit, or a leakage or scoring flaw invalidates the conclusion. Record the rollback and preserve the trial.

Do not modify held-out tests to rescue a failing candidate. A necessary evaluator correction gets a new version, a reason, and reruns of both systems. Do not rewrite earlier results.

## Anti-Goodhart checks

- Reward correct, supported, complete work; track verbosity separately.
- Score substantive answer coverage alongside abstention and uncertainty.
- Check the reasoning or artifact, not merely the agent's claimed status.
- Evaluate rare cases and adversarial tasks as well as average performance.
- Include equal-budget single-worker and independent-retry baselines when adding a team.
- Audit whether the candidate learned benchmark answers, grader preferences, or task identifiers.
- Preserve regressions and failed proposals so the search history is visible.

The protocol itself can be challenged as a research proposal. Its replacement must still be assessed under the currently accepted boundary, with an explicit maintainer decision.
