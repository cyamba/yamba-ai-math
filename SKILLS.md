# Research skills

These project skills are reusable workflows, separate from the agent roles in [the agent registry](agents/registry.json). Load the skill that matches the requested task; a role or fleet does not require loading every skill.

| Skill | Use when | Result |
| --- | --- | --- |
| [explore-angle](skills/explore-angle/SKILL.md) | Choosing a mathematical research direction | A scoped question, related-work map, and falsifiable next step |
| [audit-theorem](skills/audit-theorem/SKILL.md) | Reviewing a theorem, proof, or superiority claim | Explicit proof obligations and a supported, conditional, incomplete, or refuted verdict |
| [assemble-fleet](skills/assemble-fleet/SKILL.md) | Choosing and planning a research team | A validated capability and dependency assignment under a dispatch proxy budget |
| [design-experiment](skills/design-experiment/SKILL.md) | Testing an architecture or mechanism | A reproducible protocol with baselines, cost boundaries, and failure criteria |
| [improve-harness](skills/improve-harness/SKILL.md) | Evaluating agent roles, topology, or harness changes | A controlled comparison and a measured recommendation |

Agent cards bound each role’s contribution and require epistemic labels, evidence, failure cases, and review questions. Fleet stages in [the fleet registry](fleets/registry.json) define delivery dependencies and mandatory distinct-agent assignments. A dependency is not statistical independence; a distinct critic can still share model biases.

`cost_units` are positive integer dispatch proxies, summed per stage invocation and across rounds even when a role is reused. Optional stage `required_tags` constrain eligible assignments; program `preferred_tags` break cost ties. These are declared routing metadata, not measured competence. A minimum-cost registry assignment proves only optimality under that discrete objective and the encoded constraints. It does not establish the best research team, monetary cost, scientific truth, or independence of model errors. Actual tool use, training, inference, retrieval, verification, communication, and retries need their own measurements.

## Supervisory skills

The canonical home for these skills and future supervisory skills of this type is
`.agents/skills/`. They belong to the meta-level system/support layer; `agents/`
contains the mathematics problem-solving roles. Meta skills steer and route the
work while those roles perform mathematical discovery, proofs and semantic review.
See the [directory boundary](AGENTS.md#mathematical-agents-and-meta-level-support).
Claude Code uses links from `.claude/skills/` to the same files. The current
instructions support KR1 and preserve its objective and resource limits; authorized
framework improvements still follow the [meta protocol](meta/protocol.md).

| Skill | Use when |
| --- | --- |
| [regroup](.agents/skills/regroup/SKILL.md) | Reflecting on proved progress, failures and the next obligation |
| [reflect-before-run](.agents/skills/reflect-before-run/SKILL.md) | Selecting small evidence-based tweaks before the next run |
| [delegate-for-feedback](.agents/skills/delegate-for-feedback/SKILL.md) | Preparing a bounded question for Christopher and recording his return |
| [yamba-post](.agents/skills/yamba-post/SKILL.md) | Parking side findings locally or delivering them when requested |
| [pivot](.agents/skills/pivot/SKILL.md) | Changing the mathematical approach while preserving the objective |
| [watch-openai-math](.agents/skills/watch-openai-math/SKILL.md) | Checking openai/math and its maintainer for new results, withdrawals and problem candidates |

## Understanding skills

These skills explain rather than solve. Each layer has one entry skill that routes to its
workflows, so agents load only what a request needs. Claude Code invokes them as `/understanding`
and `/understand-math`, Codex as `$understanding` and `$understand-math`; any other agent reads
the entry `SKILL.md` directly.

| Entry skill | Explains | Workflows |
| --- | --- | --- |
| [understanding](.agents/skills/understanding/SKILL.md) | The framework itself: harness, registries, contracts, layers | framework-tutorial, framework-visualize, framework-explain-artifact, framework-qa |
| [understand-math](understanding/SKILL.md) | The mathematics: results, proofs, constructions, generated outputs | build-intuition, visualize-math, step-by-step, abstraction-levels, forge-examples, apply-theorem, answer-question, write-exposition, digest-result |

Explanations carry the status of what they explain and never upgrade it. Questions, suspected
errors and new ideas found while explaining are routed back to the research workflows above.
The harness does not yet route packets to these skills; that would be a framework change under
the [meta protocol](meta/protocol.md).
