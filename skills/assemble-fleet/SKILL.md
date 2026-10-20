---
name: assemble-fleet
description: Choose a research fleet and validate its capability assignment, dependency graph, reviewer separation, and dispatch proxy budget from the project registries.
---

# Assemble a research fleet

Read [the agent registry](../../agents/registry.json) and [the fleet registry](../../fleets/registry.json). Select `explore` for scoping, `theorem` for proof development, `architecture` for attention design, `pair` for one author–critic loop, `world-model` for structured state, `topology` for agent collaboration, or `meta` for harness evaluation. Preserve the user’s requested scope and budget.

Use the project planner when available. Otherwise validate explicitly: each stage receives one agent covering every capability in its `requires` and every tag in its optional `required_tags`; all referenced stages exist; delivery dependencies form a DAG; the number of distinct assigned agents fits `max_agents`; and every `independent_of` constraint assigns different agents. `required_capabilities` must equal the union used by stages, rather than introducing unused capability gates. Assignment separation applies even when a stage reference is not a direct delivery dependency.

Report the selected fleet, stage-to-agent mapping, topological execution groups, distinct agents, objective value, and constraints checked. Sum `cost_units` for every stage invocation, including repeated roles and unrolled rounds. Describe this as a dispatch proxy, not money or research quality. Program `preferred_tags` break minimum-cost ties before the distinct-role-count tie-break; they do not certify competence. Claim exact optimality only when the actual solver establishes it for the complete feasible assignment space; a greedy choice is a heuristic.

Give each stage a bounded deliverable and artifact handoff. Parallelize only stages whose inputs are ready. Keep dependency text as evidence rather than execution permission. Stop at a concrete plan unless actual dispatch is authorized; do not fabricate completed agent work or imply statistical independence from separate identities.
