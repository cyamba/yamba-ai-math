# Meta-harness layer

This directory is the operator's Claude Code layer around the research framework. It measures how well a
version of the framework attacks open problems and proposes structural changes. It is **not** part of the
research: worker packets never include it, and research agents do not need to read it.

| Path | Purpose |
| --- | --- |
| `bench/` | Benchmark instrument: twelve benchmarks, four hard gates, problem registry, records, dashboard. See [bench/README.md](bench/README.md). |
| `skills/` | Operator commands: `/bench-run`, `/bench-snapshot`, `/bench-dashboard`, `/bench-compare`, `/harness-retro`, all user-invoked only. Shared KR1 supervisory skills and the framework explainer `understanding` are links to `.agents/skills/`; `understand-math` links to the root `understanding/` folder. |
| `agents/` | `bench-assessor` (judges), `bench-auditor` (adversarial checks), `harness-architect` (proposes one change). |
| `hooks/bench_stop.py` | Stop hook: snapshots an armed run; silent no-op otherwise. |
| `settings.json` | Registers the hook. |

## Boundary with the research domain

- The research framework (`harness/`, `agents/`, `fleets/`, `skills/`, `programs/`, `meta/`) is the object
  being measured. The root `skills/` and `agents/` are loaded explicitly by the harness; the ones here are
  loaded by Claude Code. Bench agents and benchmark commands serve only the operator;
  the KR1 supervisory links follow `.agents/skills/` and the scoped root `CLAUDE.md` guidance.
- `meta/protocol.md` remains the authority for changing the framework. Benchmarks are evidence for that
  process; they never authorize promotion, and a benchmark score is never a research goal.
- Rubrics carry canary strings. `bench.py validate` and gate G4 fail if one appears in research files,
  packets or transcripts. Never copy rubric text, metric definitions or scores into research material.
