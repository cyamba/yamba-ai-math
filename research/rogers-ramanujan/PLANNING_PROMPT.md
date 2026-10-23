# Initial prompt for Plan mode

Work in `cyamba/yamba-ai-math`, branch
`codex/rogers-ramanujan-bijections`. My aim is to solve a genuinely unresolved
constructive problem among Rogers–Ramanujan-type partition identities,
produce a complete mathematical argument and Lean proof, and eventually
write a clear illustrated article. Start in **Plan mode**: deliver a
reviewable research and implementation plan before beginning proof work.
Do not promise that an open problem can be solved in one run.

Read `AGENTS.md`, `README.md`, `SKILLS.md`,
`research/rogers-ramanujan/README.md`, the copied
`research/rogers-ramanujan/problem_01_rogers_ramanujan_bijections.md`,
`research/partitions/evidence/other-targets.md`, and
`programs/rogers-ramanujan-bijections.json`. Load only relevant local skills.
Treat the original brief and its rankings as research input, not authority.
Preserve the existing height-two article and proofs.

## 1. Verify the actual gap

Re-audit current primary literature, including the sources in our dated
2026-10-20 ledger and the closest existing bijections and formalizations.
Inspect exact statements and constructions, not only abstracts. Record
source links, versions, inspection dates and depth, and separate reported
proofs from independently checked proofs. Do not repeat the brief's open
status claims without checking them; do not call involution methods
nonconstructive merely because they iterate cancellation.

Distinguish four questions: equality of partition counts; an explicit
bijection; a specified stronger property of that bijection; and Lean
formalization. Do not silently replace an unresolved constructive problem
with a known identity or a reproduction of a known construction.

Compare at most two precise candidates from the brief. For each, specify
the source and target partition sets, all parameters and boundary
conditions, weight and any refined statistics, closest known maps, the
remaining gap, and a smallest possible falsifier. Recommend one target
with the strongest evidence of both importance and a tractable foothold.
Novelty remains unverified until this comparison supports it. If no
defensible gap can be identified, report that fact and present alternatives
for my decision before expanding scope.

## 2. Specify what a solution must accomplish

State the proposed theorem for every weight `n >= 0` and every claimed
parameter value. Define the intended meanings of direct, local and
natural: permitted diagram moves or auxiliary objects, deterministic
choices, termination measure, inverse mechanism, and an explicit
complexity boundary. An arbitrary ordering/ranking match between equal
finite sets does not meet the intended constructive contribution.

List separate obligations for forward and inverse well-definedness,
restriction and weight preservation, termination, and both inverse
identities. Specify any claimed statistic correspondence and check that
its distributions could agree before imposing it. For rewrite methods,
explain when confluence is needed; termination and confluence alone do not
prove invertibility. A restricted case is a milestone, not the full result.

## 3. Plan bounded work through the existing harness

Use `programs/contract.md`, the existing `pair` fleet, and
`programs/rogers-ramanujan-bijections.json` for the first planning increment:
an author/formalizer proposes, a separate critic challenges, and the author
revises. The critic must re-inspect the primary sources supporting the
selected gap, rather than rely only on the author's source table.
Permit at most two rounds, two role profiles and 16 dispatch proxy
units. State the actual stage assignments, dependencies, handoff artifacts,
and what this accounting excludes. Do not add a nested fleet or modify the
harness merely to obtain a nicer plan.

Use the planner to validate the assignment. Preparing packets is not
executing research. Do not dispatch proof workers, run paid adapters,
install dependencies, or publish during this Plan-mode response. If a
later phase needs another specialist, propose a separate bounded contract
and explain the need instead of silently exceeding this one.

## 4. Design decisive experiments and formal acceptance gates

Plan independent enumeration of the actual partition definitions, then
tests of forward/inverse maps, collisions, missing images, weight and
statistics. Include the empty partition, minimum-part boundaries, extreme
parameters, and the smallest examples that exercise each rule. Set an
initial enumeration ceiling and time/storage budgets from existing
measurements where available; otherwise label estimates and propose a
bounded pilot for the later execution phase. Retain exact counterexamples.
Agreement through a finite
ceiling is empirical evidence, not a universal proof.

Inventory the installed Lean toolchains, available Mathlib cache and
reusable partition infrastructure before proposing downloads. Prefer
existing compatible infrastructure and explain any essential new
dependency. Do not assume a large Mathlib installation is necessary;
never delete user files. State any later provisioning limits explicitly.

The completed result must use the actual partition sets and implemented
maps, with a mathematical proof and clean Lean builds for both inverse
identities and all claimed properties. Require final declaration
signatures, axiom reports, source-bound verification records, no
`sorry`/`admit` or custom axioms, and separate semantic review. A theorem
that assumes the missing bijection or identity is not a completed proof.
Attribute imported theorems and constructions accurately.

## 5. Deliver the plan

Return: the source-status audit; one recommended exact target or an explicit
selection blocker; a dependency-ordered lemma plan; test/falsifier design;
Lean/dependency strategy; bounded agent handoffs; resource and stop limits;
and the first decisive proof obligation. Identify what could refute the
route and preserve unresolved reviewer disagreements.

Plan the eventual exposition around exact Ferrers-diagram transformations,
small worked examples and diagrams that follow the implemented map.
Publication follows proof checking and semantic review, with a clear
claim-to-declaration index. Label findings as established, proved,
conjecture, empirical, unverified or refuted. End with a concrete plan for
my review; do not claim that planning has solved the problem.
