# Launch the independent Claude Code session

Recommended checkout:
`/Users/christopheryamba/YambaCode/Math/yamba-ai-math-claude-phase2-cube`

Use its own Git worktree and branch `codex/kr1-claude-phase2-cube`.
It starts from the handoff checkpoint, not from main or Argon's different
checkout. Both research sessions can then edit independently.

Start in Plan mode for a concise source/definition audit and first bounded
attempt; approve the concrete plan in Claude Code, then keep working in the
same session and model. Do not spend the session producing more plans.

For this difficult proof search, Codex suggests **Claude Fable 5.1, max effort**
if available under Christopher's chosen access/budget. Otherwise use
**Claude Opus 5.5, max effort**. This is a task-based recommendation, not a
measured comparison on KR1. Availability varies by account; Fable can require
usage credits. The installed CLI was inspected as version 2.1.308.

From the recommended checkout:

```sh
claude --model claude-fable-5-1 --effort max --permission-mode plan
```

Or select Opus:

```sh
claude --model opus --effort max --permission-mode plan
```

Paste CLAUDE_START.txt from this directory. HANDOFF.md is the detailed source
map, and SOURCE-MANIFEST.json pins the portable selected source snapshots.
Record the actual selected model, effort and scope in the new run contract.

Official guidance inspected 2026-10-25:
[model and effort](https://code.claude.com/docs/en/model-config),
[Fable 5.1](https://platform.claude.com/docs/en/models/fable-5-1/overview),
[worktrees and Plan mode](https://code.claude.com/docs/en/common-workflows).
No Claude model request was launched by preparing this handoff.
