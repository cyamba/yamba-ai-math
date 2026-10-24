---
name: bench-snapshot
description: Arm a live yamba-ai-math run for benchmarking and take intermediate computed snapshots. Meta-harness only.
disable-model-invocation: true
argument-hint: start <problem-id> [--session client:id] [--run-dir PATH] | take [label] | stop
---

# Intermediate snapshots

- `start`: `python3 .claude/bench/bench.py start --problem <id> --session <client:id> [--run-dir PATH]
  [--client C --model M --effort E]`. Records the framework commit and arms `.runs/bench/ARMED`. Pin the
  session that will do the research so the Stop hook ignores other sessions.
- `take`: `python3 .claude/bench/bench.py snapshot --step "<label>"`. Use it at stage boundaries (after
  propose, challenge, revise). The Stop hook also snapshots automatically after a turn when the working
  tree changed; it skips telemetry and slow checks.
- `stop`: `python3 .claude/bench/bench.py stop`, then benchmark the result with `/bench-run <problem>
  --key <key> --commit <output commit>`. The final record embeds the snapshot trajectory.

Snapshots compute only computed and checklist axes; judged axes stay pending. They live in ignored
`.runs/bench/<key>/snapshots/`. A Codex session does not run Claude hooks: take its snapshots by hand.
