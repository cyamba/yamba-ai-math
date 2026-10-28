# Novelty radar

The novelty radar records external developments that could change what this lab studies,
builds or trusts: new results, new methods, new verification milestones and new venues where
AI and mathematics meet. It complements the narrower
[openai/math watch](../references/openai-math-watch.md), which follows one upstream collection.

**Standing instruction: look for novelty.** When a session, paper, video, post, repository or
conversation reports something genuinely new in AI-assisted mathematics, formal verification,
agentic research workflows or the infrastructure around them, log it here as a short entry,
even when it looks far from current work. Capturing a lead is not investigating it.

## Why it matters

The frontier is moving in weeks, not years. October 2026 alone brought a release of more than
700 model-generated manuscripts (see the [watch log](../references/openai-math-watch.md)), a new
arXiv-style repository for LLM-assisted mathematics (Hexagon), and a reported complete Lean
formalization of the Classification of Finite Simple Groups produced by an agent swarm
([NR-001](NR-001-cfsg-lean-agent-swarm.md)). For this lab that matters in four ways:

1. **Prior work moves.** Every idea here carries **Novelty status: NOT VERIFIED** until the
   closest work is checked. A radar shortens the distance to the closest work and lowers the
   risk of rediscovering, or claiming, something already done.
2. **Methods transfer.** How other teams decompose, check and integrate large proofs is direct
   evidence for the research harness (`agents/`, `fleets/`, `programs/`, `meta/`) and for the
   Lean obligations in `research/`. Such lessons stay unvalidated workflow hypotheses until a
   controlled comparison under [meta/protocol.md](../meta/protocol.md).
3. **Trust changes.** What counts as verified, which published arguments turned out to have
   gaps, and which results are safe to depend on all shift with new formalizations, errata and
   withdrawals.
4. **Venues and norms change.** Where AI-assisted results can be posted, how provenance is
   labeled and what journals accept affects how the lab publishes its own work.

## What counts as a signal

- A new theorem, disproof or construction, especially one generated or formalized by AI.
- A formalization milestone: size, method, trusted base, what was found along the way.
- A new agentic research method: orchestration, decomposition, review, integration, tooling.
- Errata, withdrawals and repairs, above all those touching sources in the
  [reading list](../references/reading-list.md).
- New venues, policies and norms: preprint servers, provenance labels, journal rules.
- Tools and datasets: Lean libraries, proof maps, benchmark sets, verification services.

## How to record an entry

1. Create `NR-###-short-slug.md` with the next free number and add a row to the index below.
2. Start with a field table: ID, found (date and link), kind, status, evidence here, receiving
   project (or "unassigned"; do not invent one) and next action. The fields follow the capture
   format of the [yamba-post skill](../.agents/skills/yamba-post/SKILL.md).
3. Then: what the source is, what is new as the sources claim it, why it may matter here,
   bounded next actions with a stop condition, and dated source links.
4. Use one of these states:

| State | Meaning |
| --- | --- |
| `PENDING triage` | Captured, not yet read beyond the headline |
| `EXPLORE FURTHER` | Read enough to know it deserves bounded follow-up |
| `TRACKING` | Waiting for an external event (independent check, revision, reaction) |
| `PROMOTED` | Became an `explore/` brief, a program contract or a task in a research folder |
| `DROPPED` | Not relevant or superseded; keep the reason |

## Evidence rules

- External claims are **unverified** here. Citing one in a research file needs a
  [reading-list](../references/reading-list.md) entry with an inspection level; depending on
  one needs the `audit-theorem` workflow.
- Record numbers as the primary source states them. When secondary reports disagree, say so.
- Promotion needs the operator's authorization: an `explore/` brief written with
  `explore-angle`, or a program contract. Following, posting, submitting or contacting anyone
  is the operator's action.
- To make sense of a lead before acting on it, use the understanding layer's `digest-result`
  skill ([understanding/](../understanding/README.md)).

## Index

| ID | Found | Lead | Kind | State |
| --- | --- | --- | --- | --- |
| [NR-001](NR-001-cfsg-lean-agent-swarm.md) | 2026-10-28 | The Classification of Finite Simple Groups formalized in Lean by an AI agent swarm (Axiom), with a repaired route to the Unbalanced Group Theorem posted on Hexagon | Formalization milestone, method, new result, venue | `EXPLORE FURTHER` |
