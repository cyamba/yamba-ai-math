# Rogers–Ramanujan bijections: research setup

**Status: bounded construction attempt; KR1 bridge unresolved.** Independent
finite checks reach weight 30. Two construction proposals were challenged;
the tested 16-profile local straightening family is refuted by exact
collisions. No complete new bijection, full KR1 Lean certificate or novel
count theorem is claimed. This investigation is separate from the completed
formalization of the established height-two positivity theorem.

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

The selected candidate is a structural bijection for KR1, whose counting
identity has reported proofs. Novelty of a structural bridge is still
unverified. The current route uses the established endpoint constructions
and seeks a new weighted-partition-to-cluster decomposition.

The first planning decision was which exact constructive question remains unresolved.
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

## Executed construction increment

[RR002](../../programs/rogers-ramanujan-construction.json) is the separate
user-authorized implementation contract. The [source audit](evidence/source-audit.md)
separates the established endpoints from the missing bridge; the
[construction contract](evidence/construction-contract.md) fixes definitions,
resources, two review rounds and failure accounting. Manual reviews and
revisions live beside those records. No paid adapter was used. The
[construction result](evidence/construction-result.md) records the final
obstructions and the precise unresolved obligation; the
[second review](evidence/round-2-review.md) is the separate critic verdict.

Run the exact finite checks from the repository root:

```sh
python3 research/rogers-ramanujan/checks/verify.py --ceiling 12
python3 research/rogers-ramanujan/checks/verify.py --ceiling 30 --output .runs/rr002/verification.json
python3 -m unittest discover -s tests -v
python3 scripts/check_repository.py
```

The verifier generates the actual A, B, W and C sets by independent paths,
checks the lossless column interface, and retains exact candidate collision
traces. Its result is explicitly `finite_checks_passed_bridge_unresolved`.
Adding `--require-bijection` returns exit code **2** while the maps and Lean
certificate are absent. Missing required source inputs or failed checks
return a failure; finite equalities cannot produce a full-proof success.

The weighted column encoding and the terminating local normalizations are
useful interfaces, not the sought bijection. In particular, strict energy
growth does not establish injectivity. No full Lean or article increment
has started because the new bridge has not passed its mathematical gate.

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
