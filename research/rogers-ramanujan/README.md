# Rogers–Ramanujan bijections: research setup

**Status: unverified target; planning only.** No new bijection or theorem is
claimed. This investigation is separate from the completed formalization of
the established height-two positivity theorem.

The branch `codex/rogers-ramanujan-bijections` starts at synchronized
`origin/main`, commit `dce60269fca1774ea8d5600d30f62dbc39c927a4`.

## Inputs and next action

- [Original brief](problem_01_rogers_ramanujan_bijections.md): copied verbatim
  from the partition archive. Its rankings, proposed targets and status claims
  are historical suggestions requiring review, not verified current facts.
- [Earlier source audit](../partitions/evidence/other-targets.md): dated
  2026-10-20; re-inspect its sources and later work before selecting a target.
- [Initial Plan-mode prompt](PLANNING_PROMPT.md): paste into a new planning
  conversation opened in this checkout.
- [Harness contract](../../programs/rogers-ramanujan-bijections.json): a
  bounded author–critic planning loop, not a proof-execution contract.

The first decision is which exact constructive question remains unresolved.
Distinguish a known partition-count identity from a potentially new explicit
bijection, refinement, algorithmic property, or formalization. A claim that a
new bijection is needed must be compared with the closest existing maps.

## Prepare the harness

From the repository root:

```sh
python3 -m harness validate
python3 -m harness plan programs/rogers-ramanujan-bijections.json
python3 -m harness packet programs/rogers-ramanujan-bijections.json
```

`plan` computes an assignment; `packet` prepares ignored handoffs under
`.runs/`. Neither runs a research worker. Do not use an external command
adapter until its executable and permissions are deliberately selected.

The intended assignment is `mathematician` for `propose` and `revise`, and
`critic` for `challenge`. Each round follows
`propose → challenge → revise`; the second round depends on the first.
Two rounds cost at most **16 dispatch proxy units** (3 + 2 + 3 per round),
with two distinct profiles. The dependency chain runs sequentially even
though the concurrency ceiling is two. The conversation lead coordinates
the work outside this worker-dispatch accounting. Proxy units do not count
lead effort, source retrieval, tokens, money, or builds; record those
separately when execution actually begins. Distinct roles do not guarantee
independent errors.

## Intended evidence

The first executed investigation should produce a dated source-status table,
one exact proposed target (or a documented selection blocker), an explicit
map class, proof obligations, falsifiers, a Lean dependency plan, a separate
critic verdict, and a revised milestone plan. Generated packets stay in
`.runs/`; deliberately reviewed research evidence can subsequently be placed
in this directory. No worker outputs, proof builds or mathematical results
are implied by this setup.

Setup checks on 2026-10-23 passed: harness validation, the assignment above,
all 54 repository tests, the repository checker, and an exact comparison of
the copied brief with the archive. A separate setup critic supported the
scope and requested explicit source re-inspection and estimated-budget
labels; both clarifications were incorporated. This is a setup review,
not a literature audit or a Lean proof check.
