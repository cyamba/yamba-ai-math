# KR1 discussion handoff: family census, OEIS and geometry

Date: 24 October 2026, Europe/Stockholm.

**Research stopped at Christopher's request. This handoff does not resume it.**
Full explicit KR1 remains unresolved; novelty is **NOT VERIFIED**.
RR006 is preparation only: a fresh worktree was created, but no research
contract/ledger was saved, no agents were spawned, no OEIS/web search was
performed, and no new construction variation or 3D experiment was executed.
Christopher subsequently authorized this documentation handoff only.

## 1. Workspace and first reads

Repository: cyamba/yamba-ai-math.

- Completed RR005: branch `codex/kr1-rr005`, commit `692c65d`,
  worktree `/private/tmp/yamba-ai-math-rr005`.
- Prepared continuation: branch `codex/kr1-rr006-family-search`,
  worktree `/private/tmp/yamba-ai-math-rr006`, created from `692c65d`.
  The handoff itself may be committed on this branch after that base.
- Historical checkout:
  `/Users/christopheryamba/YambaCode/Math/yamba-ai-math-rogers-ramanujan`.
  Do not switch it or the unrelated active checkout
  `/Users/christopheryamba/YambaCode/yamba-ai-math`.

Inspect status and worktrees before changing anything. The prepared RR006
worktree can be used if still present and exclusively available; otherwise
create a fresh isolated worktree carrying the RR005 checkpoint and this
handoff. Temporary worktree paths and the localhost diagram server are
session conveniences; the local Git branch/commits preserve tracked work.

Read [AGENTS.md](../../../AGENTS.md), [CLAUDE.md](../../../CLAUDE.md),
[RR005 result](../rr005/result.md), [final review](../rr005/round-2-review.md),
[second proposal](../rr005/round-2-proposal.md), and
[next lemma](../rr005/NEXT_SESSION.md). Consult
[RR003 result](../rr003/result.md) and [RR004 result](../rr004/result.md)
for earlier progress and assurance distinctions.

## 2. Unchanged objective and exact current result

Construct explicit weight-preserving mutually inverse algorithms between:

- **A, gap partitions:** ascending positive parts with distance-two gap at
  least three; adjacent parts differing by at most one must sum to a
  multiple of three.
- **B, residue partitions:** parts congruent to 1,3,6,8 modulo nine.

Include empty input. The target is every object at every total size,
not one representative for each integer. Completion needs universal
validity, weight, termination, both inverse proofs, full executable
endpoint composition and separate semantic review. Lean certification
and exposition remain subsequent obligations.

The leading route uses intermediate U columns and C cluster data:

    C=(a,b,mu,nu)
    weight=a*a+3*a*b+3*b*b+sum(mu)+3*sum(nu).

Here a,b are nonnegative, and mu,nu are ascending nonnegative vectors of
exact lengths a,b, including zero entries. U consists of descending columns
F(h), F(5q+r)=9q+(0,1,3,6,8)[r], with every decoded drop, including to
zero, in 0..4.

RR005 supplied written arguments, supported by two separate informal
reviews, for universal reversible weight-1, weight-3 and weight-6 strips
on both full intermediate domains. Each object has a unique form

    (F root,n1,n3,n6),
    weight=weight(root)+n1+3*n3+6*n6.

Reconstruct in the order R6, R3, R1. These are complete normal-form
algorithms on each side. **A uniform weight-preserving correspondence
between all residual roots F_U and F_C is missing.**

Matching only empty residual roots gives a reviewed restricted U–C
bijection for exactly U supported on {1,3,6}, arbitrary multiplicities.
In the displayed endpoint examples its function is

    phi(A)=(1 repeated n1, 3 repeated n3, 6 repeated n6),

when the C root is empty; otherwise phi is undefined. The endpoint
implementations used for these pictures retain RR003 author-only
assurance. The pictures do not establish a new direct Ferrers sliding
rule or a full A–B theorem.

The smallest unmatched residual shapes are:

    A=(3,5), C=(2,0,(2,2),())
    B=(8),   U=(8).

They are unassigned, not an accepted general matching rule.

## 3. Progress and failures that must not be forgotten

| Attempt | Retained result | Limit |
| --- | --- | --- |
| RR002 | Literal definitions, column encoding, exact failures of all 16 tested normalization candidates | No U–C bijection |
| RR003 | Separately reviewed restricted maps; later extensions, endpoint implementations and recursive alternatives preserved | Later author-only results did not receive an extra review; incompatible maps cannot be overlaid |
| RR004 | Separately reviewed impossibility of recovering b by a fixed signed sum over adjacent decoded-height transitions, including terminal/initial potentials | Richer context is not excluded |
| RR005 | Reviewed universal 1/3/6 normal forms and exact empty-root restricted map | All nonempty residual roots remain outside this map |

The [RR005 cost-eight continuation](../rr005/eight-strip-obstruction.md)
has a separately reviewed collision:

    X=(2,2,(1,1),(0,0)), Y=(3,1,(3,3,3),(0,))
    both have weight30;
    proposed P(X)=Q(Y)=(4,1,(1,2,2,2),(0,)), weight38.

Its infinite collision family is in that record. This refutes the
specified P/Q union only. Source-priority changes cannot repair their
overlapping images. No corrected cost-eight operator was accepted.

RR005 finished with 98 passing tests and repository integrity checks.
Its first-round raising edges/isolated controls exceeded a strict
input-and-output ceiling of 30; the deviations are disclosed in the
result and final revision. Future finite work must obey both bounds,
using symbolic arguments for larger branches. Closed RR003/RR004/RR005
ledgers and review budgets must never be reset or extended.

## 4. Existing finite coverage: answer the percentage question carefully

These counts were read from the already saved RR005 result, without
re-enumeration. A copy is retained at
[illustrations/rr005-six-through30-result.json](illustrations/rr005-six-through30-result.json).
The percentages are arithmetic on that exposed finite record, not new
research measurements, asymptotic densities or proof of completion.

| Cohort, each side separately | Total objects | Covered | Missing | Covered % | Missing % |
| --- | ---: | ---: | ---: | ---: | ---: |
| Exactly size8 | 5 | 4 | 1 | 80.00 | 20.00 |
| Exactly size10 | 8 | 6 | 2 | 75.00 | 25.00 |
| Exactly size20 | 45 | 16 | 29 | 35.56 | 64.44 |
| Exactly size30 | 195 | 36 | 159 | 18.46 | 81.54 |
| All sizes0..30 inclusive | 1,393 | 411 | 982 | 29.50 | 70.50 |

The equal U/C totals and restricted totals are diagnostics. To discuss
A/B coverage, preserve the endpoint assurance distinction. Do not add
RR003 and RR005 image counts: their assignments may disagree or overlap.
There is no stated percentage of the infinite problem solved.
The new census should name its map, side, weight bound, denominator and
whether it counts full objects, distinct residual roots, or a refined family.

## 5. Christopher's discussion and proposed directions

Christopher asked to contribute intuition before another attempt. The
discussion isolated two problems: regrouping can discard recoverable
information, and a successful infinite family need not exhaust the roots.
Three possible levers were raised: Ferrers/boundary pictures, an intrinsic
marker or carry that survives regrouping, and changing the 1/3/6 stripping
if its residual grammar is unnecessarily difficult.

Christopher requested both:

1. One worked Ferrers example at each total size1..10.
2. The first ten A partitions ordered by total size then lexicographic
   ascending A, including empty.

These 20 displayed instances were checked individually in both directions
using existing code. Tuple labels are ascending; diagrams draw longest
row first. They do not constitute new independent review. See the
[preserved pictures and data](illustrations/README.md).

Rules explained in conversation, within the existing partial construction:

    phi((n))=(1^n)
    phi((1,m))=(1^(m-2),3), m>=3
    phi((2,m))=(1^(m-4),6), m>=4
    phi((1,3,m))=(1^(m-5),3,6), m>=5.

Superscripts mean multiplicities. For inputs without close pairs, the
single-increment coordinates subtract the odd staircase (1,3,5,...).
Thus (2,4) gives increments(1,1), which strips successfully; (3,5)
gives(2,2), a nonempty residual root. The general case also contains
close-pair coordinates and cannot be reduced to staircase subtraction alone.

Christopher then proposed the following subresult, **but stopped it before
execution**:

- Measure coverage and classify missing families, with forms and percentages.
- Compare successful and missing neighboring families; freeze and try
  plausible extensions or genuinely different rules.
- Systematically search the OEIS and primary literature for structural
  clues from the relevant sequences.
- Try Ferrers representations as 3D blocks/layers.
- Split partitions into distinct-part and repeated-part families, and
  other intrinsic classes, looking for separate construction mechanisms.
- Keep promising clues in Markdown and every tried rule in a table,
  including failure information and what it teaches.
- Use a separate set of agents, connect all earlier work, and report any
  substantial insight accurately before deciding on other approaches.

No success, search result, family extension or geometric discovery from
that proposed investigation exists yet.

## 6. Proposed next-session work, pending renewed execution authorization

First prepare a fresh contract and reflect-before-run note. Christopher's
request for several agents supersedes the old two-profile topology only
for a newly authorized attempt; declare the new topology and resource
boundary explicitly. Preserve the earlier scope and no-push/no-publication,
no external messages, no paid providers/dependencies restrictions.

A small proposed team is three parallel research branches followed by
a distinct critic, with the root coordinating. At most four active
workers including root fit the available concurrency; dispatch the critic
after a research branch finishes. No nested agents. This topology is a
proposal, not a dispatched or planner-validated run.

1. **Census/family branch:** separate full objects from residual roots.
   Classify matched/unmatched cases by intrinsic a,b, boundary gaps,
   increment congruences, multiplicities, width/height and distinctness.
   Record smallest witnesses and explicit parameter ranges. Begin with
   already saved data; distinguish a recurrence/formula conjecture from proof.
2. **OEIS/primary-source branch:** search total counts, matched-family
   counts, missing counts, residual-root counts and selected refinements.
   Record exact terms, indexing/offsets, query, inspected entry links,
   definitions and supporting papers. Sequence agreement is a clue,
   not a matching algorithm or novelty evidence. No OEIS IDs have been
   identified in this discussion.
3. **Geometric/rule branch:** test lossless Ferrers lifts, boundary words,
   layered/3D blocks, marked cuts and carries. Preserve exact input/output
   domains, weight and intrinsic inverse recovery. An arbitrary plane
   partition is a different domain: extra 3D coordinates must be determined
   by the original object or charged/recovered explicitly. Analyze
   distinct and repeated parts separately and prove how any proposed
   pieces fit together.
4. **Separate semantic challenge:** inspect the strongest frozen claims,
   exact counterexamples, coverage denominators, dependence on old
   author-only premises and any information hidden by a geometric projection.

Suggested rule/clue table fields:

| ID | Source/earlier connection | Exact family | Forward rule | Intrinsic inverse/context | Weight/measure | Coverage obligation | Freeze/check bounds | Counterexample/result | Status/assurance | Next falsifier |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| To populate during the authorized investigation | | | | | | | | | | |

Rank at most three resulting directions. Each should name a precise next
lemma, closest inspected work, smallest falsifier, expected resource cost
and what would make the team drop it. First pilot frozen candidates
through12; extend at most to30 only after passing, with every executed
input and raising endpoint inside the declared bound. Finite matching,
rank pairing, hidden tables and equality of coefficients cannot define
the final bijection. Reserve criticism for final reusable claims.

No budget was accepted for RR006 before the stop. The old 120-minute
example and resource ceilings are historical/proposed, not an active
allowance. Agree/save a new bounded contract rather than silently
launching a full construction attempt from this handoff.

## 7. Restart prompt

> Continue the KR1 discussion from
> /private/tmp/yamba-ai-math-rr006/research/rogers-ramanujan/rr006/SESSION_HANDOFF.md.
> Read the applicable repository instructions and the RR005 result/review.
> Verify the prepared branch/worktree or create an isolated replacement.
> Full KR1 remains unresolved; RR006 was stopped before agents, OEIS
> searches or rule experiments began. First prepare a concise plan and
> fresh resource contract for the requested family census, OEIS cross-search,
> Ferrers/3D and distinct/repeated-part exploration, with separate agent
> branches and a critic. Preserve the exact coverage/assurance distinctions
> and all old failures. Wait for my renewed instruction before executing
> the research. Do not push, publish, contact others or add dependencies.

CY-KR1-001/002 remains PENDING in the local feedback queue. Do not check or
post to Drive automatically. This handoff is local and makes no delivery claim.

## 8. Planning-only continuation — 24 October 2026

Christopher subsequently requested a focused plan and fresh resource contract,
explicitly retaining the research stop pending renewed instruction. Prepared
[plan](plan.md), [proposed contract](contract.md), [pre-run reflection](pre-run.md)
and [study-local fleet input](fleet-plan-input.json). These supersede the absence
of planning documents described at the historical handoff above; that historical
record and `preparation-status.json` remain unchanged.

The proposed team has three distinct research branches and a separate critic,
with at most three executing children plus root, eight invocations and twenty
dispatch proxy units. The proposed fresh envelope is 150 charged minutes:
30 conservative preparation plus at most 120 future elapsed execution minutes.
Neither the budget nor execution is accepted by saving these documents.
No research agents, searches, new enumerations, construction trials or 3D
experiments have started. Read `planning-status.json` and
`planning-validation.json` for the documentation/assignment check record;
neither is a research execution receipt or mathematical review.
