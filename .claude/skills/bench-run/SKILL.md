---
name: bench-run
description: Final benchmark of one yamba-ai-math run on a registered problem (computed metrics, independent assessment and audit, tracked record, dashboard sync). Meta-harness only.
disable-model-invocation: true
argument-hint: <problem-id> [--commit SHA] [--framework-commit SHA] [--run-dir PATH] [--session codex:ID|claude-code:ID] [--key KEY] [--deep]
---

# Benchmark a run

Scores one version of the framework on one problem. It never authorizes promotion; `meta/protocol.md`
governs that. Run every command from the repository root.

1. **Pin the inputs.** Problem id from `.claude/bench/spec/problems.json`. Output commit (where the run's
   results landed), framework commit (the version under test: the commit the run started from), run
   directory, and the run's sessions. If the run was armed with `/bench-snapshot start`, pass `--key` and
   the start record supplies the framework commit, run directory and sessions. Otherwise list candidate
   Codex sessions with `python3 .claude/bench/bench.py sessions --framework-commit <sha>` and pin the lead
   thread; children and overhead threads follow automatically. Ask the user only if the lead is ambiguous.
2. **Collect.** `python3 .claude/bench/bench.py collect --problem <id> --commit <out> --framework-commit <fw>
   --run-dir <dir> --session <client:id> [--deep]`. Note the key and packet paths it prints.
3. **Assess.** Spawn a fresh `bench-assessor` agent with only: "Judge packet: <judge-packet path>". Take
   the JSON block it returns, set `assessor.session` to the agent id the Agent tool reported, and write it
   to the packet's `write_to` path. Do not edit its judgments.
4. **Audit.** Spawn a fresh `bench-auditor` agent with only: "Audit packet: <audit-packet path>". Write its
   JSON block to the audit packet's `write_to` path with `auditor.session` set to its agent id.
5. **Finalize.** `python3 .claude/bench/bench.py finalize --key <key> --judgments <judgments.json> --audit
   <audit.json>`, then `python3 .claude/bench/bench.py validate`.
6. **Sync** with `/bench-dashboard`.
7. **Report** the record id, the twelve axes with status, the gates, flags, unanswered requests and
   disputes. Say which axes are unknown and why. Do not describe any axis as an improvement unless
   `/bench-compare` against a same-problem baseline shows it, and never call a version better overall.
8. **Question the instrument.** Run `python3 .claude/bench/bench.py relevance` and report its flags in one
   or two lines. Append one line to `.claude/bench/journal.md` only for a decision (a defect found, a
   review started); a due review is proposed to the user as a new spec version, never edited silently.

Never paste rubric text, canaries or scores into research packets, briefs, programs or AGENTS.md.
