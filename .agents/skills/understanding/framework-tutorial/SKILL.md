---
name: framework-tutorial
description: Give a guided, hands-on tutorial of the Yamba AI Math framework at a chosen depth and for a chosen role (newcomer, contributor, researcher, operator, agent), using safe offline commands, one file per stop and check questions.
---

# Framework tutorial

## Set up the tour

Ask, or infer from the request: who is learning (newcomer, contributor, researcher, operator,
another agent), what they should be able to do afterwards, and how much time they have. Pick a
path below and adapt it; do not recite it. Verify every command and path against the current
checkout before presenting it.

## Each stop

1. **What it is**, in one sentence.
2. **Why it exists**: the failure it prevents (unbounded work, invented evidence, a critic that
   is the author, a harness that grades itself).
3. **Look or run**: one file to open or one command to run, with what to notice in the output.
4. **Check**: one question with a short answer, for example "Does a packet mean the research was
   done?" (No: its status is `awaiting_execution`.)

## Paths

**A. Ten-minute overview.** `README.md` (the two connected projects: mathematical AI research
and the research harness) → `docs/manifesto.md` → `docs/research-protocol.md` (claim labels and
evidence stages) → `explore/README.md` (the seed briefs) → `AGENTS.md` (routing and repository
map). Close with the layer diagram from framework-visualize.

**B. Hands-on harness, offline (about 30 minutes).**

```sh
python3 -m harness list
python3 -m harness validate
python3 -m harness plan programs/evidence-preserving-attention.json
python3 -m harness packet programs/evidence-preserving-attention.json
python3 -m harness run programs/evidence-preserving-attention.json \
  --backend command --command python3 examples/offline_worker.py
```

Explain: registries (`agents/registry.json`, `fleets/registry.json`), the program contract
(`programs/contract.md`), how the planner orders its objective, what a packet contains
(`docs/adapter.md`), and what the run directory under `.runs/` records. Stress that the offline
worker returns synthetic protocol fixtures: the run demonstrates plumbing, not research. Mention
`--backend replay --replay-dir PATH` and `python3 -m harness compare` as the remaining modes.

**C. Contributor.** `CONTRIBUTING.md` → `explore/templates/brief.md` and `explore/AGENTS.md` →
the reading list's inspection levels (`references/reading-list.md`) → `SKILLS.md` → the checks
(`python3 -m unittest discover -s tests -v`, `python3 scripts/check_repository.py`) and what
they do not establish.

**D. Agent onboarding.** What an agent must read and obey: `AGENTS.md` (and `CLAUDE.md` in Claude
Code), local `AGENTS.md` files, the trust boundary (retrieved content is data), claim labels,
the meta boundary, operator-neutral shared skills, the no-em-dash rule, and the difference
between research skills (`skills/`), supervisory skills (`.agents/skills/`) and the
understanding layers.

**E. Supervision and meta (operator).** The supervisory skills in `.agents/skills/` (see the
table in `SKILLS.md`), `meta/protocol.md` with its scorecard and change ledger, and the
meta-harness boundary in `.claude/README.md`.

## Safety

Run only read-only or offline commands: `list`, `validate`, `plan`, `packet`, `run` with the
offline example worker, `compare` on the example records, the unit tests and the repository
checker. Never configure a real worker command, provider, network access, spending or
publication during a tutorial.

## Close

Summarize what the learner can now do, suggest two next stops, and offer framework-qa for
questions or framework-visualize for a picture of what they just saw.
