---
name: understanding
description: Explain the Yamba AI Math framework itself to people or agents. Guided tutorials, diagrams of the harness and repository layers, walkthroughs of specific files (programs, fleets, agent cards, packets, results, skills), and answers grounded in the repository. For explaining mathematics, use understand-math instead.
---

# Understand the framework

These skills explain how this repository works: the research harness, its registries and
contracts, the evidence protocol, the supervisory and meta layers, and how they fit together.
They are meta-level support (see "Mathematical agents and meta-level support" in `AGENTS.md`).
They explain; they do not change the framework, start research or spend budget.

## Ground rules

1. **Read before explaining.** Start from `AGENTS.md` and `README.md`, then the canonical file for
   the topic. Cite repository paths for specific claims so the reader can check them.
2. **Never invent** commands, flags, fields or behaviors. Check the code, or run
   `python3 -m harness --help` and the subcommand help, when unsure.
3. **State the limits** as clearly as the features. Examples: a minimum-cost plan is optimal only
   for the declared proxy objective; a packet is prepared work, not research; a claim status is
   an assertion to review, not a certificate; replay is not a fresh result.
4. **Keep the layers apart.** Research and its harness (`explore/`, `research/`, `agents/`,
   `fleets/`, `skills/`, `programs/`, `harness/`, `meta/`), meta-level support (`.agents/`), the
   operator's Claude Code meta-harness (`.claude/`), and the understanding layers. Describe the
   meta-harness only from `.claude/README.md`; never copy rubric text, canary strings, metric
   definitions or scores into any output.
5. **Operator-neutral wording.** These files ship with every clone; keep names and private
   locations out of them.
6. **Read-only by default.** Running offline commands that write to the ignored `.runs/` is fine.
   Writing a durable guide (for example under `docs/`) needs a request; changing the framework
   follows `meta/protocol.md`.

## Choose the sub-skill

| Request | Load |
| --- | --- |
| A tour, onboarding, "how do I start", a tutorial for a role | [framework-tutorial](framework-tutorial/SKILL.md) |
| A diagram of the layers, the run pipeline, a fleet or the evidence stages | [framework-visualize](framework-visualize/SKILL.md) |
| "What is this file", "explain this program, packet or result" | [framework-explain-artifact](framework-explain-artifact/SKILL.md) |
| How or why something works, where something lives | [framework-qa](framework-qa/SKILL.md) |

Terms and their canonical files: [glossary](references/glossary.md).

Combine freely: a good onboarding is a tutorial with one diagram and a short Q&A at the end.

## Output

- One-off explanations go in the conversation, with paths cited.
- Diagrams: Mermaid in Markdown by default, generated from the registries where possible.
- Apply the no-em-dash rule to all authored prose.

For mathematics (results, proofs, examples, intuition, teaching), load the understand-math skill
at `understanding/SKILL.md` (repository root).
