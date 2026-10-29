# RR006 focused investigation plan — 24 October 2026

**PREPARED ONLY. Research remains stopped; renewed execution instruction is
required.** This plan responds to Christopher's family/OEIS/Ferrers suggestions.
The quoted earlier invitation to run agents does not override the current stop.
No research agent, search, enumeration or new rule trial has been launched.
See the proposed [resource contract](contract.md) and [reflection](pre-run.md).

## Question and retained evidence

We need rules for **every partition object at every weight**, including empty,
not just one construction for each integer. The leading missing lemma is a
uniform explicit weight-preserving bijection `psi:F_U <-> F_C` between the
residual roots of the reviewed RR005 1/3/6 normal forms. Those forms reconstruct
in order R6, R3, R1; they do not supply psi. A different coherent representation
can be proposed, but changing representation does not discharge coverage.

The unchanged ultimate target is explicit mutually inverse algorithms between
gap partitions A and residue partitions B, with universal validity, weight,
termination, both inverse proofs, executable endpoint composition and separate
semantic review. Lean certification and exposition remain subsequent obligations.
**Full KR1 is unresolved; novelty is NOT VERIFIED.**

The [handoff](SESSION_HANDOFF.md) preserves RR005's finite figures: the empty-root
map covers 411 of 1,393 objects per U/C side at weights 0..30 (29.50%), leaving
982 (70.50%); at weight 30 it covers 36 of 195 (18.46%). These are saved-data
figures, not new measurements or percentages of the infinite problem solved.
Equal counts do not construct a map. Do not add RR003 and RR005 partial images.

| Prior record | Assurance and boundary carried into RR006 |
| --- | --- |
| [RR005 result](../rr005/result.md), [final review](../rr005/round-2-review.md) | **Proved**, written arguments with separate informal reviews: universal literal U/C normal forms and exactly the empty-root restricted map, with U supported on {1,3,6}. No formal certificate or nonempty-root map. |
| [RR003 result](../rr003/result.md) | Reviewed restricted results stay distinct from later author-only extensions, endpoints, K/L constructions and compositions. New A/B conclusions relying on those endpoints remain conditional on their separate audit. |
| [RR004 result](../rr004/result.md) | Reviewed obstruction excludes fixed signed adjacent-height transition recovery of b, including boundary potentials; richer recoverable context remains open. |
| [RR005 P/Q failure](../rr005/eight-strip-obstruction.md) | The specified cost-eight union is **refuted** by the reviewed weight-30 inputs with common weight-38 image and its symbolic infinite family. Source priority cannot repair it. No corrected eight-strip is accepted. |
| [RR002 construction result](../evidence/construction-result.md), RR003 failure table | Preserve all sixteen failed normalizations, incompatible overlays, lost phase, seed-capacity and conditional repair obstructions, with their original quantifiers and assurance. No new rule silently reinstates them. |

## Three research branches, then a separate critic

The root coordinates and preserves evidence. Three distinct research agents
receive the same pinned inputs and initially work without peer conclusions.
The fourth research profile is a distinct critic, dispatched after the research
branches finish. No nested agents. The [fleet input](fleet-plan-input.json)
specifies an attempt-local DAG using existing role cards; no global registry
or harness change is proposed. Stage costs and dependencies are in the contract.

### 1. Census and family grammar — mathematician

Start with saved RR005 data; identify whether it contains individual objects or
only aggregates before promising refinements. Any missing row-level data needs
a newly authorized, bounded enumeration, not invented reconstruction of a receipt.
Use the literal U/C definitions and reviewed normal forms as the baseline map.

Produce per-weight and cumulative tables through the permitted bound, with
separate tables for full U objects, full C objects, distinct F_U roots and
distinct F_C roots. Count each residual root once in a root table; count its
different strip-count descendants separately in a full-object table. Record
map/version, side, exact weight range, family predicate, numerator, denominator,
covered/missing counts and rounding. Use exact integer fractions before rounding;
report an empty denominator as N/A. Give the smallest witnesses and parameter
ranges. Separate disjoint family bins from overlapping cross-tabulations.

Candidate refinements: a,b and boundary equalities/gaps on C; decoded-height
runs, multiplicities and terminal gaps on U; increment congruences, width/height
and strip-count/root-weight data. Call a predicate intrinsic only on the domain
from which it can actually be recovered. Do not identify C parameters with
unproved U statistics or turn a finite pattern into a family theorem.

Make distinctness explicit. A distinct, A repeated, B distinct and B repeated
are four side-specific cohorts, not assumed bijection partners. Distinct columns
in U and repeated increments in C are different predicates. Any new A/B census
using RR003 endpoint code must disclose its author-only dependency; prefer
literal side predicates and label transported classifications conditional.
Show whether the chosen map crosses these cohorts; do not impose preservation.

Compare at most two nearby successful/missing family pairs. For each, state an
exact parameterized form, the known rule, one proposed extension, the needed
inverse statistic, the smallest falsifier and the remaining complement. Finite
family coverage is **empirical** unless a universal argument is supplied.

Planned outputs: `family-census.md` and versioned CSV/JSON data in fresh `.runs/rr006/`.

### 2. OEIS and primary-source cross-search — scout

Begin with exact sequences already extractable from the saved baseline, then
use one bounded follow-up after census and geometry handoff. Select queries
from total counts, covered counts, missing counts, F_U/F_C root counts and
distinct/repeated refinements. Keep side and definition even if terms coincide.
This is a targeted cross-search, not an exhaustive OEIS survey.

For every query record the exact term list, n=0 convention, offset, term count,
bound, provenance and any transformation. Preserve no-hit and ambiguous results.
Preselect sequences before searching; label later refinements exploratory.
Do not keep transforming terms until a familiar answer appears. For each hit
inspect the entry's definition, offsets, formulas and references, then the
relevant primary construction where feasible. Log inspection depth, date,
authors/version, exact correspondence and mismatch. A candidate ID or search
snippet alone establishes nothing. Agreement of finite terms is a clue, not
an identification proof, root algorithm or novelty verification.

Return at most six source records and at most three useful clues, each linked
to an exact family or proposed rule and a next falsifier. If search is unavailable,
save unverified query leads and continue other branches. No OEIS submission,
external message, dependency or provider installation.

Planned outputs: `oeis-search-log.md` and `clues-and-rules.md`.

### 3. Ferrers, layers and inverse recovery — geometer

Start from the existing twenty illustrated instances as exposed examples.
Compare the ordinary 2D Ferrers/boundary encoding with **one** explicitly
defined lossless layered/3D encoding. A 3D proposal must define each block,
coordinate, orientation, admissible shape, projection and reconstruction.
State whether volume equals weight or requires specified block weights.
U's decoded height is not automatically its column weight F(h).

An arbitrary plane partition is a different domain. Extra layer labels,
marks, cuts, colors and carries must be determined by the original input and
recoverable from the output, or explicitly included in both domains with their
cost. A drawing or saved forward trace is not an intrinsic inverse. Exhibit
the smallest ambiguity if projection loses data. Impose no geometric symmetry
without proving it respects the literal partition conditions.

Analyze distinct and repeated parts separately, including boundary cases and
how transitions cross the proposed family split. Explore at most three frozen
rule variants across the whole investigation, shared with the census branch;
one failed variant consumes a slot. For each, require exact domains, forward
operation, intrinsic inverse/image predicate, weight invariant, decreasing
measure if recursive, and a coverage obligation before implementation.
The initial pilot checks only the claimed family; it must not silently discard
unassigned objects while claiming full coverage. A complete-root candidate
needs an exhaustive branch argument before a broad trial.

Relate the construction to the P/Q collision and RR003 lost-phase examples.
Larger old witnesses may be inspected symbolically; no above-bound execution.
Changing a strip grammar is a documented alternative, not permission to overlay
incompatible maps or start an unbudgeted recursive-route investigation.

Planned output: `ferrers-layers.md`, with formulas and optional local diagrams;
no new media dependency is needed.

### 4. Freeze, challenge, narrow and close — distinct critic

Freeze the exact rules, proofs, source claims, code dependencies and hashes
before pilot checks; freeze the retained claim packet before criticism.
Previously inspected weights through 30 are discovery exposure, not held-out
evidence. Every executed mathematical input **and output endpoint** must obey
the current pilot/extension ceiling. Bound an edge before executing it; if it
would exceed the ceiling, record it as skipped and use symbolic reasoning.

The critic checks literal domains, denominators, empty/zero/repeated cases,
terminal drops, both inverse identities, branch disjointness/coverage, source
interpretation, hidden 3D information and reliance on author-only components.
Use an independently written bounded check when useful, with its cost charged.
Inspect old above-bound failures symbolically. Return supported, conditional,
incomplete or refuted verdicts with exact scope; separate identity does not
guarantee independent errors. A substantive correction receives the reserved
second review or remains explicitly author-only/unresolved. No new discovery
round follows a final review.

The root synthesizes at most three directions. Each needs an exact next lemma,
closest inspected work (or explicitly unverified lead), smallest falsifier,
resource estimate, drop condition and remaining global obligation. A useful
outcome may be a new obstruction or evidence that these representations add
no recoverable information. No breakthrough is promised.

Planned outputs: `claim-freeze.json`, `review-1.md`, optional `review-2.md`,
`result.md`, `NEXT_SESSION.md` and a fresh resource/completion record.

## Shared clue and tried-rule table

Create and populate this only during authorized research. An inspected clue,
unexecuted proposal, failed pilot, written proof and separately reviewed claim
must have different status/assurance values. Preserve abandoned rules and
counterexamples; do not overwrite a failed version with a repaired rule.

| ID/version | Source and earlier connection | Exact family/side | Forward rule or clue | Intrinsic inverse/context | Weight/measure | Coverage/complement | Freeze and executed bounds | Result/counterexample | Status and assurance | Next falsifier |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| No new clues or trials yet | | | | | | | | | | |

For each useful idea also record assumptions, mathematical objects and total
resource boundary. Claim labels remain **established**, **proved**,
**conjecture**, **empirical**, **unverified** or **refuted**; unresolved obligations
are not theorems. Established claims require inspected primary support, and
proved claims need an actual argument with assurance recorded.

## First action after renewed instruction

Recheck the isolated worktree and accepted contract, pin inputs, initialize a
fresh ledger and allocate the three branch packets. First establish what saved
data can support the census. Stop a branch at its deadline or first unrepaired
inverse ambiguity; preserve its output for criticism. Until renewed instruction,
leave all research stages unstarted and do not create execution receipts.
