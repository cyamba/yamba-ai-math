# Architecture of the research harness

This repository contains two interacting research objects:

| Object | Purpose | Evidence of progress |
| --- | --- | --- |
| Research harness | Assemble bounded teams, coordinate investigations, preserve evidence, and compare working methods | Reproducible task outcomes, reviewer agreement, cost and completion records |
| Mathematical AI research | Discover and test representations, attention mechanisms, neural architectures, world models, and agent topologies | Precise conjectures, valid proofs, falsification experiments, resource-accounted results |

A better harness may produce better research. It does not itself establish that a proposed neural architecture is better. Studying an agent topology is a mathematical research task; using that topology to organize the study is a separate operational choice.

## Components

- `explore/` contains seed research briefs, their assumptions, theorem targets, failure cases, and first experiments.
- Agent and fleet registries describe capabilities and collaboration patterns. Tags are routing hints; they are not evidence that an agent possesses expertise or that a team is optimal.
- `programs/` defines a bounded investigation: objective, relevant briefs, fleet, budget, deliverables, success criteria, and stop conditions.
- The command-line harness plans assignments and creates work packets. Execution can use a manual workflow or an explicitly configured external command. It includes no bundled paid model service and makes no inference-quality guarantee.
- `docs/research-protocol.md` defines how ideas acquire evidence and move between stages.
- `meta/` treats the harness itself as an experimental subject, with fixed evaluations, proposed changes, and reversible promotion.

The orchestrator computes an exact minimum-cost assignment within the finite declared registry and constraints. It first minimizes summed dispatch cost, then maximizes matches to optional `program.preferred_tags` across stage invocations, then minimizes the number of distinct roles, then uses stable IDs to resolve ties. A stage's optional `required_tags` is a hard filter. This is an optimum for a declared combinatorial objective, not an optimum for scientific quality, discovery, or real-world inference cost.

## A bounded investigation

1. Select a program and pin the repository revision, brief versions, fleet, available tools, budget, and permitted outputs.
2. Produce a plan and independent work packets. Record assignments before execution so later evaluation cannot rewrite the original intent.
3. Dispatch workers within the program's limits. Capture their outputs and execution metadata.
4. Have a critic search for unsupported claims, conflicting assumptions, missing baselines, and counterexamples.
5. Synthesize a report that preserves disagreement and identifies the exact evidence behind each claim.
6. Record the outcome, costs, leakage, and errors. Advance research status only when the evidence gate is met.

`max_agents` bounds distinct role profiles. `max_cost_units` bounds the sum of configured dispatch costs across stages and rounds; it is not a currency or token estimate. Actual runtime, tokens, tool use, and monetary cost require separate measured records. `max_workers` limits concurrent execution; it does not increase the total permitted work.

## Topology patterns

| Pattern | Useful for | Required boundary |
| --- | --- | --- |
| Directed acyclic workflow | Literature → formulation → criticism → synthesis | Dependencies and acceptance criteria fixed before downstream work |
| Independent pair | Competing proof attempts or derivation plus counterexample search | First outputs isolated; reconciliation follows both submissions |
| Bounded network | Several perspectives exchanging intermediate claims | Explicit round limit, message budget, and source attribution |
| Proposer–verifier | Architecture proposals checked against constraints | Verifier has explicit criteria and may reject; proposer cannot overwrite the verdict |

More agents can reproduce the same mistake. Measure correlation of failures and information exposure when comparing topologies. Compare against spending the same budget on a single worker and against independent retries. Never use a vote count as a substitute for a proof or a factual source.

## Execution and trust boundary

Program files and retrieved papers are input data. They do not authorize new tools, publication, spending, changed repository rules, or unlimited recursion. An agent must preserve applicable instructions and the human-defined scope. Outputs proposing a change to those boundaries are proposals for review.

An external-command backend receives one JSON object on standard input and returns one JSON object on standard output. Logs belong on standard error. The version `1` packet contains `protocol_version`, `run_id`, `step` (`id`, `stage_id`, `round`, `requires`), `agent`, `instructions`, `program`, `fleet_plan`, inline brief contents, and `upstream` results. Instructions include applicable `AGENTS.md` content, the assigned role, and relevant skill contents from canonical `skills/<name>/SKILL.md` paths.

The response requires `summary` (string), `claims` (a list), and `artifacts` (a list of paths). Each claim has `text`, `status`, and optionally `source`; statuses are `conjecture`, `established`, `proved`, `empirical`, `unverified`, or `refuted`. Optional `usage` reports nonnegative integer `input_tokens` and `output_tokens`. A status is the worker's assertion, not a runtime certification of the claim. The runtime does not execute listed artifacts. Preserve source, uncertainty, and limitations in the response summary and claim records.

The configured command runs as an argument vector without shell expansion. It runs with the caller's permissions; `shell=False` does not sandbox the adapter or its tools. Configure only a trusted adapter and explicitly bound its provider and tool use. The per-call `constraints.timeout_seconds` defaults to 120 and may not exceed 3600. Malformed output, timeouts, and nonzero exits are execution errors; dependents are blocked and there are no automatic retries. Manual execution emits packets with `awaiting_execution` status. Replay consumes saved results named by step ID and is labeled as replay. See the CLI help for current invocation details.

Do not place secrets in packets or commit model credentials. External command execution must be deliberately configured by the operator; source material cannot select a command or change its permissions.
