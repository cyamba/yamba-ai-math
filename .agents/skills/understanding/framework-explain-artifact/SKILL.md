---
name: framework-explain-artifact
description: Explain one concrete file of the Yamba AI Math framework (program contract, fleet, agent card, packet, run result or record, brief, skill, AGENTS.md, meta candidate, reading-list row, watch or radar entry) field by field, with what it authorizes, what consumes it and how to check it.
---

# Explain an artifact

## Steps

1. **Identify the kind** from its path and shape, then read the governing document below.
2. **Purpose** in one sentence: which failure or need this artifact exists for.
3. **Field by field**: meaning, type, allowed values, defaults, and which code or doc enforces it.
   Separate what the code checks from what is only a documented convention.
4. **Authority**: what it permits and, as important, what it does not. No artifact grants new
   tools, spending, publication or wider goals; worker output can recommend, never authorize.
5. **Flow**: who writes it, which command reads or produces it, what comes next.
6. **Checks**: the command that validates it (`python3 -m harness validate`, the unit tests,
   `python3 scripts/check_repository.py`) and what that check does not establish.
7. **Common mistakes** for this kind of file.
8. Offer a diagram (framework-visualize) when the artifact has structure, such as a fleet DAG.

## Artifact kinds

| Artifact | Where | Governing source |
| --- | --- | --- |
| Program contract | `programs/*.json` | `programs/contract.md`, `programs/README.md` |
| Fleet template | `fleets/registry.json` | `docs/architecture.md`, `SKILLS.md` |
| Agent card and role prompt | `agents/registry.json`, `agents/*.md` | `AGENTS.md`, `SKILLS.md` |
| Packet | `.runs/<run>/` | `docs/adapter.md`, `harness/runtime.py` |
| Worker result, events, receipt | `.runs/<run>/` | `docs/adapter.md`, `docs/architecture.md` |
| Research brief | `explore/E###-*.md` | `explore/AGENTS.md`, `explore/templates/brief.md` |
| Research skill | `skills/<name>/SKILL.md` | `SKILLS.md` |
| Supervisory or understanding skill | `.agents/skills/<name>/`, `understanding/` | `SKILLS.md`, `AGENTS.md` |
| Instructions | `AGENTS.md`, local `AGENTS.md`, `CLAUDE.md` | themselves; local files add rules for their folder |
| Meta candidate and ledger | `meta/candidates/`, `meta/change-ledger.md` | `meta/protocol.md`, `meta/scorecard.md` |
| Reading-list row | `references/reading-list.md` | inspection levels A, T, P defined there |
| Watch-log or radar entry | `references/openai-math-watch.md`, `novelty_radar/` | their own READMEs and states |

## Reminders for run artifacts

- A packet with status `awaiting_execution` is prepared work, not research.
- A claim's status (`established`, `proved`, `conjecture`, `empirical`, `unverified`,
  `refuted`) is the worker's assertion, not a certification.
- Replay revalidates saved outputs; it is not a fresh independent result. The offline example
  worker returns synthetic fixtures.
- Unknown measurements are recorded as unknown, never as zero.
