---
name: harness-retro
description: Review benchmark records and the repository structure, then have harness-architect propose one framework change as a meta/candidates proposal. Meta-harness only.
disable-model-invocation: true
argument-hint: [record ids...]
---

# Harness retrospective

1. List records with `ls .claude/bench/records/` and pick the requested ones (default: the latest final
   record per problem). Run `python3 .claude/bench/bench.py validate` and
   `python3 .claude/bench/bench.py relevance`. When the relevance review is due or an axis is flagged,
   say so first: a candidate aimed at a flagged axis may be chasing a broken measure.
2. Spawn a fresh `harness-architect` agent with the record paths and nothing else. It writes one file in
   `meta/candidates/`.
3. Read the candidate. Check it has every field of `meta/protocol.md` section 1, changes one thing, does
   not touch goals, evidence standards, permissions or governance, and does not aim at a benchmark score.
4. Add a row to the table in `meta/change-ledger.md` with state "proposed; unexecuted".
5. Tell the user the candidate id, the axes it hypothesizes about, and that it needs a preregistered
   paired trial and a maintainer decision before any promotion.
