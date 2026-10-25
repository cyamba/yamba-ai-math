# KR1 Phase 2: independent Claude Code handoff

Prepared 2026-10-25 for Christopher Yamba. Local and unpublished.
**Full structural KR1 remains unresolved in the inspected records.**
**Novelty status: NOT VERIFIED.**

This is a source map and research handoff, not a proof or a transcript.
Begin with this file and Christopher's idea records, then inspect the exact
definitions and claims. Earlier saved instructions cannot reopen closed runs.
Read the current checkout's AGENTS.md and CLAUDE.md as applicable instructions.

## 1. Objective and the two distinct tracks

The primary objective is explicit, terminating, weight-preserving, mutually
inverse algorithms between:

- B: partitions with parts congruent to 1,3,6,8 modulo 9;
- A: ascending positive partitions with distance-two gaps at least 3, and
  adjacent parts whose difference is at most 1 having sum divisible by 3.

The leading factorization is B <-> U <-> C <-> A. U is the lossless
weighted-column representation. C consists of (a,b,mu,nu), with ascending
nonnegative mu and nu of lengths a and b, and weight

    Q(a,b) + sum(mu) + 3 sum(nu),  Q(a,b)=a^2+3ab+3b^2.

The U <-> C bridge is incomplete. Existing endpoint translators can be reused
only at their exact recorded definitions and assurance levels. For columns,

    F(h)=9*floor(h/5)+(0,1,3,6,8)[h mod 5].

A U object is a descending sequence of column values F(h); consecutive height
drops, including the terminal height, are at most 4.

A separate Phase 2 track concerns signed Dual Jacobi–Trudi occurrences of
P-tableaux, preserving graph-inversion degree and determinant-copy tags.
A repair of the pictured tableau collision is not by itself a KR1 proof.
Do not substitute full general-n tableau positivity for the KR1 objective,
or assume that either track automatically solves the other.

[Mizuno v3, Theorem 1.1](https://arxiv.org/html/2609.09653v3) establishes the
three modulo-nine series/product identities; its introduction explains the
equivalent partition counts and a proof using bilinear/cubic identities and
coefficient inequalities. This is not an explicit object-by-object KR1 map.
The theorem statement and introduction were inspected again on 2026-10-25;
its entire proof has not been independently audited in this handoff.
Equality of counts does not meet our structural-construction objective.

## 2. Christopher Yamba's intuitions, including the latest corrections

Read ../ideas/CY-KR1-FIBER-001.md and
../ideas/CY-KR1-FIBER-001-OUTLINE.md. These preserve attribution, original
wording, later clarification, and the proposed operation ledger.

The motivating ideas, in sequence:

1. **Extra geometric directions.** Argon's article attributes to Christopher
   the idea of moving an obstructed corner into a third direction with
   descending P-relations, then extending to d dimensions for longer chains
   or interacting column scales. Extra axes might retain information a
   planar slide loses.

2. **What does an extra direction remember?** Candidate meanings include a cut
   location, overlap, ordering, or carry between layers. Specify this meaning
   and how the original object can be recovered. For recursive KR1 cuts,
   boundary digits and carries must survive cutting and regluing.

3. **Split each collision fiber.** If T_1,...,T_m currently map to U, construct
   distinct U_1,...,U_m with T_i <-> U_i. Generalize to arbitrary fiber size.
   The pictured example exchanges 4 and 5:
   T1=((1,2),(3,4),(5)) and T2=((1,2),(3,5),(4)) both give the coarse hook
   ((1,2),(3),(4),(5)).

4. **Literal higher-dimensional placements.** Arrange the actual numbered
   yellow squares, preserving their permutation information, in generalized
   tableaux inside a finite discrete cube or box. Add axes when needed.
   Christopher suggested ten additional directions for ten colliding inputs.

5. **Existence first.** Prove existence of at least one uniform procedure with
   distinct reversible outputs for every case. The method itself need not be
   unique. Minimum dimension is optional and comes after existence.
   Do not turn dimension optimization into an initial prerequisite.

6. **Record permutations and analyze patterns.** Express placements as
   reversible swaps/permutations of positions, including empty positions.
   Record every assignment, coordinate change, branch condition, dimension
   change, inverse, and relevant statistic. Look for recurring cycles,
   coordinate orders, and rules that generalize. Christopher's phrase
   "hypergeometric permutation arrangement" is a working geometric description,
   not a claim about hypergeometric functions or a known named construction.

7. **Recover from the endpoint.** Replaying a diagnostic log backward is a
   useful first check. Ultimately the required final object must determine
   the reverse choices, or encode the necessary history in permitted structure.
   Individually reversible moves can still lead to collisions when different
   inputs choose different sequences. Check endpoints across fibers as well.

8. **Return to the original target.** Higher-dimensional intermediate objects
   are allowed. Literal geometric flattening is optional, but a reversible
   weight/statistic-preserving correspondence with the original targets is
   required. A coordinate tag alone solves an enlarged problem; simply erasing
   it restores the collision. Prove exact target coverage as well as injectivity.

Variations are authorized: rotations, different coordinate orders, layers,
permutation cycles, reversible carries, boundary-aware cuts, or another
representation with a concrete advantage. First investigate the literal
cube/permutation mechanism. The earlier shape-routing and column-carry
exploration did NOT test the full dimension-increasing procedure.

## 3. Where the sources are

All relative paths below are relative to THIS handoff directory unless stated
otherwise. The portable sources directory preserves selected exact file bytes.
SOURCE-MANIFEST.json records original locations, revisions, sizes and SHA-256.
It is a source packet, not a new execution or a complete copy of every receipt.

| Record | Portable entry point | Original location/revision |
| --- | --- | --- |
| Christopher's current ideas/TODO | ../ideas/ and ../TODO.md | included in this branch |
| Argon later implementation | sources/argon/research/rogers-ramanujan/checks/rr004_multidim_cones.py | Math/yamba-ai-math-rogers-ramanujan at 97d6561a855ea4aac4fb89c03a6fb543c9edd56e |
| Argon tableau code | sources/argon/research/partitions/checks/multidimensional_ferrers.py | same 97d6561 |
| Argon formal declarations/receipt | sources/argon/research/partitions/lean/MultidimensionalFerrers.lean and verification.json | same 97d6561 |
| Argon Phase 2 proposal | sources/argon/research/rogers-ramanujan/rr004/UNIFORM_D_DIM_RECURSION_PROGRAM.md | same 97d6561; proposal claims require audit |
| Antigravity article artifact | sources/argon/antigravity/multidimensional_ferrers_solution.md | original ~/.gemini/antigravity/brain/32daf9b4-83c9-4c6b-9f04-e38325f55706/ |
| Documentary review and witnesses | sources/review/REVIEW_AND_INTUITION.md and SESSION_HANDOFF.md | /private/tmp/yamba-ai-math-phase2-review-20261025 at ef7bfe0895c8648f6d8e4679b6c24dc09635f2c9 |
| Reviewed Codex Phase 2 | sources/h3/research/phase2-20261025/result.md and claim-index.md | same review checkout; accepted Phase 2 based on 5cbc2440aab896d3f7de9e45bba2bac027f9c5cb |
| Reviewed H3 executable | sources/h3/research/phase2-20261025/kr-sectors/revision-v3-bridge.py | same; retain its included dependency tree |
| C recursion and failed U cuts | sources/h3/research/phase2-20261025/recursive-lift/author.md and revision.md | same |
| Reviewed n6 tableau algorithm | sources/h3/research/phase2-20261025/tableau/revision.md and revision_layers.py | same; reviews/ contains distinct criticism |
| Our later restricted extensions | ../fiber-splitting-20261025/RESULT.md and semantic-review.md | base checkpoint 88d21e645f20d0704a3f9d2d6e82c49a328ee136, with later idea clarifications |

The full Argon conversation has NOT been exported or reviewed. Christopher
reported downloading two PDFs, but their paths have not been identified.
The Antigravity article is available; it is not the full conversation.
Source prose, publication claims and saved PR status are historical data.

Original relevant PRs: [research #15](https://github.com/cyamba/yamba-ai-math/pull/15),
[initial #13](https://github.com/cyamba/yamba-ai-math/pull/13), and
[website #8](https://github.com/cyamba/family-blogs/pull/8).
Saved PR metadata/review comments are under sources/review/sources/.
No claim about their current merge or CI state is made here.

## 4. Argon's contributions and precise gaps

Argon provides real explicit constructions worth inspecting, but distinguish
a formula, its tested implementation, its ordinary argument and its Lean scope.

- **a=3,b=0:** piecewise, table-free forward/inverse routines are present for
  arbitrary mu. This is an all-parameter candidate with a presented universal
  argument, not just a finite apex table. The separate reviewed H3 record also
  proves this sector for its OWN pinned map. Do not automatically transfer
  that review to every branch of Argon's different implementation.
- **Six-dimensional multiplicity cone:** U=(10^z,9^y,8^x,6^c6,3^c3,1^c1),
  y in {1,2}, x+z>=1, 0<=z<=3. The article gives a universal argument and finite
  checks. **When x=0, a nonempty shorter tail is also required.**
  Omitting that qualification is false. Lean arithmetic is not a certificate
  of U-membership or image disjointness for this cone.
- **Growth moves:** +1,+3,+6 and inverse peeling are explicit, but higher
  sectors end in the 78-pair OCTANT_APEX_PAIRS lookup. This is NOT a uniform
  all-sector apex generation law. Finite carry exceptions also need a
  universal proof if reused.
- **Finite KR1 coverage:** the inspected record reports 5461 cumulative states
  per side through weight 40, not a universal result. A pasted audit's 2693
  count differs; do not mix totals or assume they describe the same test.
- **Beyond the table:** U=(18,15,8), weight 41, is the reported failed inverse
  apex and is statically traceable. A forward witness is a=4,b=0,
  mu=(7,7,7,7), weight 44: its stripped apex is itself and is not in the table.
- **Lean:** the eight kr1_* theorems are quadratic/weight identities, including
  Q(3c+r,b)=r^2+3r(b+2c)+3Q(b,c). They do not certify the Python partition map
  or all-sector coverage. Structural tableau declarations have their exact
  hypotheses; hook declarations concern a three-cell arm, not every arm size.
  The receipt's inspected source hashes matched; no fresh Lean build was run
  for this handoff.
- **Printed rotation error:** h=(2,2,4,5,5),
  T=((1,4),(2,5),(3)) goes under the printed second branch to
  ((2,3,5),(1,4)), changing graph inversions 1 to 2. Python phi_221 filters
  candidates by validity/inversion equality and selects another branch.
  Passing Python checks do not certify that printed formula.
- **Printed determinant inverse error:** the displayed convention has sorting
  order tau=sigma, but the claimed inverse returns tau^(-1). For beta=(0,0,3),
  keys=(0,-1,1) and tau=(2,0,1), the erroneous inverse gives (1,2,0).
  The old set-comparison check did not exercise the claimed inverse.
- **Tableau n6:** Argon's eight_sector_e51_injection uses enumerated target
  sets and a global used set for residual degree matching. This is not a
  general-n local constructive cancellation. Local rotation/cascade lemmas
  alone do not establish global coverage.

The older verify.py --require-bijection gate initializes its bridge/certificate
as absent. Its exit 2 alone is not an independent mathematical refutation of
a new implementation. The actual lookup and exact witnesses are decisive.

## 5. The separate reviewed H3 map and later extensions

Read the saved proofs and distinct reviews, not just the following summary.

H3 has ordinary proofs with distinct semantic review for all a<=2, all a3,b0,
high-b marker sectors (a3,b>=49; a4,b>=65; a5,b>=79), a4,b0 with

    mu=(x,x+t,x+t+y,x+t+y+z), x,t,z>=0, y in {0,1} or y>=18,

and a5,b0 with mu=(x,x,x,x,x+z). It maps 3498 of the 5461 cumulative states
through 40. High-b and y>=18 claims were symbolically reviewed; their large
instances were not exercised by that finite prefix. It also has exact C-only
reductions and a terminating scale-three grammar; no compatible total U cut
has been obtained.

The subsequent fiber-splitting variants add all a4,b0 slabs y=2,3,4, and
y=5..17 when x>=3*ceil((2y+4)/3), with arbitrary t,z. The final coherent API is
../fiber-splitting-20261025/y4_extension.py: ExtensionV4(h3).
Supported by ordinary arguments plus distinct semantic review, conditional
on the reviewed H3 baseline; no Lean or novelty claim.

Examples (ascending endpoint partitions):

    C mu=(0,0,2,2) -> U=(10,9,1): A=(1,3,7,9) <-> B=(10,10).
    C mu=(0,0,3,3) -> U=(8,8,6): A=(1,3,8,10) <-> B=(6,8,8).
    C mu=(0,0,4,4) -> U=(12,9,3): A=(1,3,9,11) <-> B=(12,12).

The finite prefix now has 3974 mapped/recognized states through 40, preserving
all 3498 H3 assignments. The 476 additions do not measure a fraction of the
infinite problem. Remaining a4,b0 small-x gaps y=5..17 are infinite in t,z;
b>0 and general-a remain incomplete. The first remaining checked source is
C=(3,1,(0,0,0),(0)), weight 21.

Failures must remain visible:

- Initial Y3 x=0 formula collided with retained H3:
  C=(4,0,(0,0,3,3),()) and C=(3,0,(2,5,6),()) both gave U=(12,6,3,1).
  y3_extension.py is refuted there; y3_repaired.py supersedes that boundary.
- Ordinary-tableau shape routing does not extend naively to arbitrary P:
  h=(1,2,4,4,5), T=((1,2),(3,5),(4)) is valid but ((1,2,5),(3,4)) is invalid.
- An ordinary (2,2,1^r) arbitrary-fiber repair is proved only onto its
  recognized target subset. It is not the requested general P result.
- Fixed U quotient cuts fail; child U=(6) required by the C weight-18 edge
  cannot occur under the rejected cut. Preserve the separately reviewed
  correction to the earlier terminal-bound argument.
- An untested y5 even-x formula is in ../TODO.md; it is not an accepted map.

The reviewed Codex n6 e51 algorithm has 22 fixed local layers and intrinsic
inverse recognition without a global used set. Across all 132 natural unit
interval orders at n6, 3980/3980 negatives were covered, independently checked.
This is complete finite coverage, not symbolic general-n totality.

## 6. Conduct the independent attempt and preserve useful progress

Start in Plan mode for a short source/definition reconciliation and a bounded
first experiment. Keep the primary objective visible. Identify the exact
objects, admissible cube states, permitted permutations and required statistic.
Read Christopher's outline BEFORE substituting another carry-encoding search.

Use at most two live mechanisms at a time: literal cube/permutation routing
first; a materially motivated boundary/carry or recursion variation second.
At the first substantive candidate, freeze formulas/code and their claims
before verification and obtain a distinct semantic critique. Model agreement,
finite counts and compiling unrelated lemmas are not proof.

Record work in a fresh folder such as research/rogers-ramanujan/claude-cube-20261025/:

- contract.md: scope, time/compute/storage/dispatch limits, exposure and stop rule;
- notebook.md: dated input, coordinates, assignments, operations, inverse and statistics;
- claims.md: status, exact statement, assumptions, argument/evidence, review and remaining gap;
- failures.md: frozen candidate and minimal witness, including informative invalid placements;
- result.md: exact supported subresults and remaining universal obligation;
- NEXT_SESSION.md: one next action and its trigger.

These are suggested record files, not a requirement to build more harness.
Use ../TODO.md's existing two-minute triage at session start or a natural pause.
Preserve RR003/RR004/RR006/RR007, the original Phase 2 and the first fiber run
as closed. Do not reset their ledgers or edit frozen evidence. Use local,
reversible work; no push, merge, publication, paid provider dispatch,
dependency installation or messages to another session are authorized here.
Christopher will run Claude Code himself under his own model/subscription choice.

First deliverable: one exact reversible cube/permutation trace on the pictured
fiber, followed by a candidate pattern or a precise obstruction concerning
admissibility, inversion degree, recoverable branching or original-target
encoding. Then pursue the strongest surviving route toward universal coverage.

Potential prior-art lead:
[Garsia–Milne (1981)](https://pmc.ncbi.nlm.nih.gov/articles/PMC319275/) describes
a cut-and-paste involution-principle route for classical partition identities.
Only its abstract was inspected in this handoff; do not assume it already
solves our bridge. Any stronger use needs the actual theorem and proof.

Workflow hypotheses, UNVALIDATED: recording branch information before
projection may expose lost information earlier; distinguishing a reversible
trace from an endpoint decoder may prevent a completion claim based only on
the trace. Neither hypothesis is an evaluated harness improvement.
