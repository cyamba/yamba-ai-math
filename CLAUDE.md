# CLAUDE.md

@AGENTS.md

## Claude Code in this repository

Two domains share this checkout:

- **Research**: everything AGENTS.md routes. Research sessions work there.
- **Meta-harness**: `.claude/`, operator tooling that measures and improves the framework itself. It runs
  only when the user invokes `/bench-run`, `/bench-snapshot`, `/bench-dashboard`, `/bench-compare` or
  `/harness-retro`. See [.claude/README.md](.claude/README.md).

Rules:

- During research work, do not open `.claude/bench/` or the bench agents, and do not optimize for any
  measurement. Research quality is defined by AGENTS.md and `docs/research-protocol.md`.
- During meta work, never copy rubric text, canary strings, metric definitions or scores into research
  files, briefs, programs, worker packets or AGENTS.md.
- Framework changes still follow `meta/protocol.md`. A benchmark result never authorizes promotion.

## Commands

```sh
python3 -m unittest discover -s tests -v
python3 scripts/check_repository.py
python3 -m unittest discover -s .claude/bench/tests -v   # meta-harness
python3 .claude/bench/bench.py validate                  # meta-harness
```

## Parallel sessions

Claude Code and Codex sessions share this repository. Start new work on a branch in its own worktree
(`git worktree add ../yamba-ai-math-<topic> -b <branch> main`) instead of switching the main checkout.
