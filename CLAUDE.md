# KR1 research supervision

Read [AGENTS.md](AGENTS.md) for repository standards. For KR1, begin with the
[current result](research/rogers-ramanujan/rr003/result.md),
[regroup note](research/rogers-ramanujan/rr003/regroup.md), and
[pending feedback](research/rogers-ramanujan/feedback.md). Other projects retain
their own instructions; these KR1 details do not redefine their objectives.

Fresh-session entry: [NEXT_SESSION.md](research/rogers-ramanujan/NEXT_SESSION.md).

## Mathematical agents versus meta agents

- `agents/` is the mathematics problem-solving layer: discovery, constructions,
  proofs, mathematical criticism and research experiments.
- `.agents/` is the meta-level system and supervisory layer. Its skills live in
  `.agents/skills/`; future meta agents belong under this layer. Use it for system
  work, reflection, coordination, feedback and authorized framework improvement.
- `.claude/skills/` links to the shared meta-level skills in `.agents/skills/`.

Meta skills may use mathematical evidence to steer the work; the problem-solving
roles execute the mathematics and its semantic review. Follow the full
[directory boundary](AGENTS.md#mathematical-agents-and-meta-level-support), including
historical registry exceptions. Framework changes remain governed by the user's
scope and [meta protocol](meta/protocol.md), with unchanged proof and review standards.

## Governing objective

Construct explicit, weight-preserving, mutually inverse algorithms between
partitions with parts congruent to 1,3,6,8 modulo 9 and ascending positive gap
partitions: distance-two gaps are at least three, and adjacent parts differing
by at most one have sum divisible by three. Require universal validity, weight,
termination and both inverse proofs, executable endpoints, and separate semantic
review. Lean certification and exposition remain subsequent obligations.

U–C is the leading route. Another representation may replace it when a concrete
mathematical advantage justifies the change. Partial theorems and counterexamples
are progress. Finite agreement, enumeration, rank matching and hidden lookup
tables cannot define or certify the final bijection. Preserve attribution;
**Novelty status: NOT VERIFIED** until the closest constructions are inspected.

## Supervisory skills

| Skill | Use |
| --- | --- |
| [regroup](.agents/skills/regroup/SKILL.md) | Reflect on evidence and choose the next bounded proof obligation |
| [reflect-before-run](.agents/skills/reflect-before-run/SKILL.md) | Choose small evidence-based workflow tweaks before the next attempt |
| [delegate-for-feedback](.agents/skills/delegate-for-feedback/SKILL.md) | Prepare a checkable question for Christopher and preserve his return |
| [yamba-post](.agents/skills/yamba-post/SKILL.md) | Park useful findings locally; deliver to YambaPost when requested |
| [pivot](.agents/skills/pivot/SKILL.md) | Change the approach on evidence while preserving the mathematical goal |

These project skills follow the [Claude Code skill layout](https://code.claude.com/docs/en/skills)
and can be invoked by their slash names. Load only the relevant skill. Reuse
[existing research skills](SKILLS.md) for discovery and mathematical audits.

All supervisory skills of this type live in `.agents/skills/<name>` as the
canonical source. Keep new skills there and link them from `.claude/skills/<name>`
for Claude Code. In Codex use `$skill-name` or `/skills`; Claude Code uses
`/skill-name`. See [official Codex discovery guidance](https://learn.chatgpt.com/docs/build-skills).

RR003 is closed; its clock, computation ledger and two review rounds are spent.
A later investigation needs its own declared contract and resource ledger within
the user's authorization. Reflection does not silently start another run.
Retain local-only work, no pushing, no new dependencies or paid providers, and
binding resource safeguards. Skills do not grant permission to send messages or
publish. Broader harness changes require separate evaluation; workflow hypotheses
remain unvalidated. Keep durable mathematics and feedback in the research folder.
