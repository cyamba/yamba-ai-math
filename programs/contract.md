# Program contract

A program is a versioned investigation specification, not a grant of unrestricted autonomy. Use the JSON examples as the machine-readable form. Keep details needed by a researcher in the linked briefs or an accompanying report.

## Required fields

| Field | Meaning |
| --- | --- |
| `id` | Stable program identifier |
| `title` | Short human-readable title |
| `objective` | One specific investigation outcome |
| `fleet` | An existing fleet ID |
| `briefs` | Repository-relative research input paths; `[]` is allowed for a new question |
| `constraints.max_agents` | Maximum distinct role profiles permitted by the plan |
| `constraints.max_cost_units` | Positive integer bound on summed dispatch costs over stages and rounds; not dollars or a token estimate |
| `constraints.max_workers` | Maximum concurrently executing workers |
| `constraints.max_rounds` | Maximum communication/refinement rounds; no unbounded feedback loop |
| `deliverables` | Concrete artifacts or reports to produce |
| `success_criteria` | Checkable conditions for a useful investigation |
| `stop_conditions` | Boundaries requiring termination or a documented unresolved outcome |

Optional `rounds` defaults to 1 and must not exceed `constraints.max_rounds`. Optional `constraints.timeout_seconds` sets the per-call timeout, defaulting to 120 seconds with a maximum of 3600. Optional `preferred_tags` lists soft preferences used after minimum dispatch cost has been established. Fleet stages may declare `required_tags` as hard eligibility filters.

Optional `target` pins the statement the program serves: `{"path": "<repository file>", "sha256": "<hex digest of its bytes>"}`, for example [the KR1 target](../research/rogers-ramanujan/TARGET.md). Loading, planning and every dispatch fail closed when the file no longer matches, and each packet carries its text. Under a pinned target every `proved` claim declares `target_relation`: `target` (exactly the pinned statement, empty `scope_delta`), `restricted` (a nonempty `scope_delta` listing each added hypothesis, restricted range or weakened conclusion) or `supporting` (a lemma that is not itself a version of the target). The harness checks the declaration's form; the reviewer checks that it is honest.

The planner solves the finite registry assignment exactly: minimum summed dispatch cost, then maximum preferred-tag matches across stage invocations, then minimum distinct role count, then stable IDs. This mathematical optimum concerns the declared proxy objective and constraints. It does not establish optimal scientific quality or actual model cost. Agents' tags can describe mathematical specialties, research styles, or review functions; they do not certify competence.

## Before dispatch

Pin the program, input and harness revisions. Define where outputs will be written and what source/tool access is available. Resolve dependencies and give independent workers their first packets before exposing peer answers. Explain how budget units map to actual assignments. Reusing a role in several stages or rounds costs another dispatch even though it does not add another distinct role profile. A configured model provider may incur real costs beyond the proxy; measure and record them separately.

Human project intent, repository instructions, and tool permissions remain binding. Worker output can recommend scope changes but cannot authorize them. External command adapters run with caller permissions and are not sandboxed by the harness; configure a trusted adapter deliberately. Stop on exhausted budgets, missing required inputs, execution errors that block the workflow, or an instruction conflict. Report the condition and completed evidence honestly.

## Completion record

Record the mode (manual, external command, or replay), pinned revisions, actual assignments, sources, elapsed time, measured resource use where available, errors, leakage, deliverable paths, claim status, reviewer verdicts, and success-criterion outcomes. Unknown measurements are `unknown`, never zero.

Replay is useful for testing plumbing and auditing saved outputs. It is not a fresh independent result. A manual packet is an unexecuted task until a researcher supplies its result. A nonempty response is not evidence that success criteria were met.
