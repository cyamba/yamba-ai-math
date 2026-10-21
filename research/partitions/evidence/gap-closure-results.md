# Gap ledger: finite-family and survivor-count increment

Updated 2026-10-21. **H1/H2 are proved and Lean-checked. The full coloring-to-
elementary theorem H3 and the original general research objective remain
incomplete.** This is the first bounded increment of the
[gap-closure plan](../gap-closure-plan.md), not a new positivity theorem.
The construction and its height-two positivity interpretation remain attributed
to Cho–Huh.

## Exact result

For an actual finite height-at-most-two poset, let `T_k` be its tableaux of
shape `(2^k,1^(n-2k))`, or the empty family when `2*k > n`. Let `S_k` be the
complement of the entire bubble image of `T_(k+1)` inside `T_k`. For every
natural index `k` and inversion degree `d`, Lean proves

```text
count(T_k, inv = d) = count(T_(k+1), inv = d) + count(S_k, inv = d).
```

The lists are complete and duplicate-free by proof, with actual bijective
fillings and all row/column conditions. The source shape determines the split
index. The identity uses addition of natural counts and a proved injection,
not a subtraction convention or an assumed coefficient formula. Empty and
singleton vertex sets each have one tableau at degree zero; the guard handles
all invalid indices and both odd/even maximal next sources.

The main declarations are `height_two_degreewise_cancellation` and
`finite_height_two_degreewise_cancellation` in
[WeightedCancellation.lean](../lean/WeightedCancellation.lean). The latter
extends the relation by false outside the finite vertex set, so its asymmetry
and height hypotheses are required only there. The
[formalization guide](../lean/README.md) lists every family and map obligation.

## Acceptance ledger

| Gate | Current status | Evidence and remaining obligation |
| --- | --- | --- |
| M0 | **Closed for this increment** | Baseline commit `389e31456e5c6785380810f1d14736f6d59dd6c0`; its committed successful certificate record; unchanged `CornerSlide.lean` hash; pinned Lean 4.34.0; current actual declaration inventory and source/configuration hashes in [verification.json](../lean/verification.json). |
| A1 | **Inventory complete; rebuild deferred** | [Pinned source inventory and feasibility report](external-certificate-audit.md). Zero build attempts, no dependencies installed. The general certificate remains unverified. |
| A2 | **Partial inspection** | Actual graph/coloring/elementary definitions and the decisive `historyWitness` dependency identified. The Laurent/wall expansion chain and the full paper-to-Lean correspondence remain unaudited. |
| H1 | **Proved; gate closed** | `mem_family`, `family_nodup`, `pair_decomposition` and the three family-level bubble theorems in [TableauFamilies.lean](../lean/TableauFamilies.lean); clean checking plus separate semantic review. |
| H2 | **Proved; gate closed** | Generic degreewise image/complement decomposition, actual-tableau instantiation, all-index theorem, finite-vertex specialization and explicit boundary cases. |
| H3 | **Incomplete** | No checked theorem yet identifies the actual proper-coloring polynomial with the elementary expansion whose coefficients are these survivor counts. |
| R1 | **Closed for H1/H2 only** | [Two-round critic record](gap-review.md); final source semantics supported; fresh build with no prior local artifacts and all source checks successful. No external general-proof reproduction is claimed. |
| W1 | **Closed for this increment** | Existing `paper/main.tex` updated in place with the exact theorem, a fourth vector figure and the retained bridge gap. The built-in editor compiler returned success. The same editor remains open; visual layout was not independently inspected. |

The baseline record is retained by Git at the baseline revision; the original
[investigation receipt](completion.json) and original counterexamples remain
unchanged. Current `verification.json` is the new, separately scoped certificate
record. A gate closed for H1/H2 does not close H3 or certify general positivity.

## Verification actually performed

- Lean 4.34.0/Std: fresh temporary workspace, clean build, direct checking of all
  three source modules, and printed actual declaration signatures.
- All **31** printed theorem dependency lists use only `propext`, `Quot.sound`
  and `Classical.choice`. Required reports are checked explicitly. The verifier
  rejects diagnostics, forbidden proof tokens and source changes during the run.
- The sum of recorded Lean subprocess times was **10.253 seconds** for the clean
  reproduction; this excludes proof development and is not a total research cost.
- All **40** repository tests passed, including the independent coloring/tableau
  comparison through five vertices and the existing collision regressions.
- The repository checker and whitespace check passed after the ledger was added.
- The article compiled successfully with the desktop editor's built-in compiler;
  no separate PDF was compiled or exported.

The unchanged, broader 33,474-source computation remains historical baseline
evidence. It was not rerun for this Lean-only mathematical extension. Its
smaller regression tests did run as part of the 40-test suite. Finite examples
are not the proof of the universal new count identity.

## Orchestration and resource accounting

The [P006 contract](../../../programs/partition-gap-closure.json) uses the
repository's `pair` fleet. The planner validated the serial dependency groups
`r1-propose → r1-challenge → r1-revise → r2-propose → r2-challenge → r2-revise`.
Proposal/revision stages map to `mathematician`; challenge stages map to
`critic`. The constraints allow two distinct profiles, two workers and two
rounds; the declared dispatch objective is **16 proxy units** across the six
stages. This is a finite routing result, not measured cost or scientific quality.

Actual work used the root author and one separate critic, with two review
deliveries and compact file handoffs. The root handled compilation, evidence
and article updates while the critic reviewed the final proof sources. No
harness provider execution, automatic paid API calls, extra agent fleet or
third mathematical review round occurred. Actual token usage, monetary cost
and any context-saving benefit are **unknown**, rather than inferred from the
small team or the planner's proxy budget.

The external-build inventory records zero build-process seconds, zero attempts,
and zero provisioning/build downloads. The conservative disk-space decision
does not prove a larger build impossible and does not refute the mathematics.

## Next mathematical obligation

H3 must begin with a library-route decision and a concrete prototype involving
actual finite proper-coloring polynomials. The choices in the original plan
are a restricted Schur/tableau expansion, a direct coloring argument, or
correctly attributed lemmas from a rebuilt and audited external certificate.
Formal symbols that merely assume the desired expansion do not meet the gate.
Any reuse of the general certificate still needs a proof that its coefficients
agree with these particular survivor families.

PR #1 was verified merged at `454e927b8b6be4d520a1c7df5b076729d9d9d3fe` before
preparing this follow-up. Repository integration does not strengthen the proof
assurance recorded above or make the full objective complete.
