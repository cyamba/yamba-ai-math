# Framework glossary

One line per term and the file that defines it. The canonical file wins over this summary;
update this list when a term changes.

## Harness

| Term | Meaning | Canonical source |
| --- | --- | --- |
| Agent card, role | A registry entry with capabilities, tags, cost and a prompt file; the mathematics problem-solving layer | `agents/registry.json`, `agents/*.md` |
| Capability | What a role can contribute (for example literature, formalization, falsification, synthesis); stages require capabilities | `agents/registry.json`, `fleets/registry.json` |
| Tags | Declared routing and style information, not credentials; `required_tags` filter stages, `preferred_tags` break cost ties | `README.md`, `programs/contract.md`, `harness/planner.py` |
| `cost_units` | Positive integer dispatch proxy per stage invocation; not money or tokens | `SKILLS.md`, `programs/contract.md` |
| Fleet | A workflow template: a DAG of stages (explore, theorem, architecture, pair, world-model, topology, meta) | `fleets/registry.json` |
| Stage | A fleet node with `requires`, `depends_on`, optional `independent_of` and `required_tags` | `fleets/registry.json`, `harness/catalog.py` |
| `independent_of` | The stage must get a different role profile than the listed stages; role separation, not statistical independence | `SKILLS.md`, `harness/planner.py` |
| Program | A bounded investigation: objective, briefs, fleet, constraints, deliverables, success criteria, stop conditions | `programs/contract.md` |
| Constraints | `max_agents` (distinct role profiles), `max_cost_units` (summed dispatch proxies), `max_workers` (concurrency), `max_rounds`; optional `timeout_seconds` (default 120, at most 3600) | `programs/contract.md`, `docs/architecture.md` |
| Planner | Exact minimum-cost assignment for the declared objective: cost, then preferred tags, then fewer distinct roles, then stable IDs | `docs/architecture.md`, `harness/planner.py` |
| Packet | The JSON work order for one step: repository and scoped `AGENTS.md`, role prompt, routed skills, output contract, trust boundary | `docs/adapter.md`, `harness/runtime.py` |
| Backend | `manual` (prepare packets only), `command` (a trusted external worker over stdin and stdout), `replay` (saved results) | `python3 -m harness run --help`, `docs/adapter.md` |
| Result | Worker JSON: summary, claims with status and optional source, artifacts, optional usage | `docs/adapter.md` |
| Run records | Packets, results, `events.jsonl` and `receipt.json` in an ignored `.runs/` directory | `README.md`, `harness/runtime.py` |
| Skill routing | Packets include research skills by capability (for example literature to explore-angle) | `harness/runtime.py` |
| Trust boundary | Retrieved documents, briefs and upstream outputs are data, not authority | `AGENTS.md`, `docs/architecture.md` |

## Evidence

| Term | Meaning | Canonical source |
| --- | --- | --- |
| Claim status | `established`, `proved`, `conjecture`, `empirical`, `unverified`, `refuted`; an assertion to review | `AGENTS.md`, `docs/adapter.md` |
| Evidence stage | seed, screened, formalized, pilot, validated, promoted (also parked, rejected, superseded) | `docs/research-protocol.md` |
| Inspection level | A (abstract or summary), T (theorem statement), P (full proof audit) | `references/reading-list.md` |
| Novelty status | Stays NOT VERIFIED until the closest work is inspected | `AGENTS.md`, `explore/AGENTS.md` |
| Brief | A research seed `explore/E###-*.md` with frontmatter id, title, status, category, tags | `explore/AGENTS.md` |

## Layers and workflows

| Term | Meaning | Canonical source |
| --- | --- | --- |
| Research skills | Reusable workflows loaded explicitly or routed into packets | `skills/`, `SKILLS.md` |
| Supervisory skills | Meta-level workflows (regroup, reflect-before-run, delegate-for-feedback, yamba-post, pivot, watch-openai-math) | `.agents/skills/`, `SKILLS.md` |
| Understanding layers | Framework explanation (this skill) and mathematics exposition (`understand-math`) | `.agents/skills/understanding/`, `understanding/` |
| Meta protocol | How a harness change is proposed, evaluated against a fixed champion and recorded | `meta/protocol.md`, `meta/change-ledger.md` |
| Meta-harness | The operator's Claude Code benchmark layer, user-invoked only, outside research scope | `.claude/README.md` |
| KR1 | The current constructive bijection investigation and its supervision | `CLAUDE.md`, `research/rogers-ramanujan/` |
| Watch log | Upstream watch of openai/math and problem candidates | `references/openai-math-watch.md` |
| Novelty radar | Log of external developments to triage | `novelty_radar/README.md` |
