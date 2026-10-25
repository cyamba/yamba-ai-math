# KR1 working TODO

Created 2026-10-25 at Christopher's request. These are queued choices, not
new results, dispatched work, or extensions of closed research budgets.
Full structural KR1 bijection and novelty remain unresolved.

## Lightweight review rule

At the start of a KR1 session, when new intuition/evidence arrives, or at a
natural pause, spend at most two minutes checking this list. Do not interrupt
the current task for repeated checks. Choose at most one relevant item whose
next step fits the current authorization and remaining budget. A small paper
trace can be a ten-minute step; a new fleet, enumeration, or proof run needs
its own applicable resource contract. This list itself authorizes none.

Use `QUEUED`, `READY`, `ACTIVE`, `WAITING`, `DONE`, or `PARKED`. On a meaningful
change, record the date, next action, and evidence link or specific blocker.
Only mark DONE when the stated deliverable exists. At handoff, name one next
item and its revisit trigger; keep deferred items visible rather than copying
the whole queue. This is a user-requested documentation workflow, not an
evaluated harness improvement or a background scheduler.

Last triage: **2026-10-25**, after Christopher clarified the construction.
Next: **KR1-08**, existence of the literal extra-dimension procedure; minimum
dimension is optional. Earlier variants
produced reviewed extensions to the entire y=2/3/4 slabs, but did not test
that procedure. KR1-03 remains available after this clarification is addressed.
The first isolated attempt is checkpointed, and earlier runs remain closed.

## Choices

- [x] **KR1-01 — DONE 2026-10-25: record Christopher's geometric intuition.**
  Preserve his wording, then describe the objects, extra coordinate, and
  proposed reversible move without upgrading intuition to proof.

  > The intuition I need from you is quite concrete: **what would the extra direction remember?** A cut location, an overlap, an ordering, or a carry between layers? A sketch showing how that information survives—and how you would undo the move—is enough to give us a productive starting point.

  Returned: [Christopher Yamba's fiber-splitting intuition](ideas/CY-KR1-FIBER-001.md),
  preserved with original wording and attribution.

- [x] **KR1-02 — DONE 2026-10-25: trace the idea on one small example.**
  After KR1-01, draw before/after Ferrers diagrams; name what each coordinate
  stores and recover the input literally. First checks: weight, boundary
  validity, lost information, and collision with an already assigned image.
  Deliverable: one worked reversible trace or a precise counterexample.

  Completed: ordinary-tableau shape routing, exact KR1 examples at weights20
  and22, and the refuted third-12 collision, all in the
  [new result](/Users/christopheryamba/.codex/worktrees/kr1-fiber-splitting/autodidactic-traveler/research/rogers-ramanujan/fiber-splitting-20261025/RESULT.md).

- [ ] **KR1-03 — READY 2026-10-25, partially advanced: finish the a=4, b=0 middle-gap band.**
  Write μ=(x,x+t,x+t+y,x+t+y+z). The reviewed H3 map leaves y=2..17.
  Start with μ=(x,x,x+2,x+2), N=20+4x; the first source is (0,0,2,2).
  Progress: entire y=2, y=3 and y=4 now have explicit maps/inverses disjoint from
  the retained H3 image, supported by ordinary proofs with distinct semantic
  review. A funded encoding also covers y=5..17 when
  x>=3*ceil((2y+4)/3), arbitrary t,z. Novelty and full KR1 remain unresolved.
  [Evidence, code, failures and remaining scope](/Users/christopheryamba/.codex/worktrees/kr1-fiber-splitting/autodidactic-traveler/research/rogers-ramanujan/fiber-splitting-20261025/RESULT.md).

  Next: try y=5 with small x, using marker counts and carry states that
  survive flattening. Record exact image recognition before enumeration.
  Deliverable: the missing boundary rule and its exclusion proof. Revisit
  at the next authorized KR1 session; a fresh bounded contract is needed.
  One untested first trace: even x=2q>=2, y=5 candidate
  U=(10,9,8^q,6,3^t,1^(z+1)); start at (x,t,z)=(2,0,0), weight34.
  This is a candidate next step, not an accepted extension.

- [ ] **KR1-04 — QUEUED: translate the exact C recursion into U geometry.**
  Try a boundary-aware cut/glue that retains ordered remainders and carries.
  First falsifier: C=(0,2,(),(1,1)) at weight 18 requires retained child
  U=(6), which the rejected fixed quotient cut cannot produce. Also retain
  the weight-9/child-(3) obstruction. Deliverable: a compatible cut and its
  inverse, not just the quadratic weight identity.

- [ ] **KR1-05 — QUEUED: replace Argon's finite apex assignments.**
  Identify all residual data after the +1/+3/+6 growth is stripped, including
  unbounded prefixes and ν. Seek an intrinsic all-sector apex rule. Prove
  growth validity, termination, both inverses, image disjointness and
  exhaustion; a larger table alone does not discharge these obligations.
  First recorded out-of-range witness: U=(18,15,8), weight 41.

- [ ] **KR1-06 — QUEUED: reconcile written formulas, code and proof scope.**
  Repair/reject the displayed inversion-changing tableau branch and the
  determinant inverse using the wrong permutation. Trace each saved witness
  through the actual printed formula and implementation separately. Record
  precisely what Lean certifies before reusing any repaired claim.

- [ ] **KR1-07 — QUEUED: check novelty and significance against prior work.**
  Compare the restricted maps with the closest explicit constructions;
  distinguish Mizuno's counting proof, established endpoints, our partial
  bridge, and elementary weight algebra. Deliverable: a short source-backed
  scope/novelty assessment, with unknowns retained.

- [ ] **KR1-08 — READY 2026-10-25: investigate Christopher's literal extra-dimension construction, existence first.**
  For a fiber of m inputs, arrange the actual numbered yellow entries in
  generalized tableaux. First seek existence of a uniform procedure in some
  finite dimension; optimal dimension and uniqueness of the procedure are
  unnecessary. Start with his ten-input/ten-extra-dimensions example, then
  seek a compatible selection rule and an intrinsic inverse for all fibers.
  A coordinate tag alone separates a decorated class; connecting that class
  to the original targets is a separate obligation. First define admissibility,
  axis conventions and the statistic; then trace the pictured two-input
  fiber before a ten-input example. Prove finite-dimensional existence,
  separation between fibers, and exact target coverage. A bijection to an
  intermediate higher-dimensional class alone leaves the target translation
  open. This exact procedure has not been implemented or tested.
  [Faithful specification and scope](ideas/CY-KR1-FIBER-001.md).
  Latest outline, 2026-10-25: represent placements as explicit reversible
  permutations in a discrete cube/box; log every assignment and inverse;
  analyze arrangements for a general selection/decoding rule. First deliver
  a small coordinate trace and compare its endpoints. Distinguish a reversible
  logged history from an inverse recoverable from the final target itself.
  [Suggested outline, recorded before an attempt](ideas/CY-KR1-FIBER-001-OUTLINE.md).
  Revisit at the next authorized KR1 work window, before further carry variants;
  preserve closed contracts and set a fresh boundary for any new proof run.

- [x] **KR1-09 — DONE 2026-10-25: prepare independent Claude Code handoff.**
  Includes Christopher's full idea progression, exact Argon/H3/extension source
  map, known failures and assurance boundaries, a copyable starting prompt,
  and portable source snapshots with hashes. Independent research itself is
  not marked complete or executed by this preparation.
  [Handoff](phase2-independent-20261025/HANDOFF.md),
  [launch guidance](phase2-independent-20261025/LAUNCH.md).

- [ ] **TAB-01 — QUEUED, separate problem: explain tableau totality.**
  Seek a structural case split explaining the reviewed n=6 cancellation
  coverage, or a uniform rotation rule preserving graph inversions and an
  intrinsic inverse. Start from the two-input/one-output slide collision.
  Finite coverage does not establish general-n totality or the KR1 bridge.

## Evidence to resume from

- [Session review and intuition notes](/private/tmp/yamba-ai-math-phase2-review-20261025/research/rogers-ramanujan/phase2-review-20261025/REVIEW_AND_INTUITION.md).
- [Reviewed Phase 2 result and exact assurance boundaries](/private/tmp/yamba-ai-math-phase2-review-20261025/research/phase2-20261025/result.md),
  [three precise continuation directions](/private/tmp/yamba-ai-math-phase2-review-20261025/research/phase2-20261025/NEXT_SESSION.md).
- [Argon implementation](checks/rr004_multidim_cones.py), inspected at 97d6561;
  [Mizuno Theorem 1.1](https://arxiv.org/html/2609.09653v3).

The reviewed checkpoint is in a separate checkout; follow its source links
instead of assuming its accepted H3 map is identical to Argon's later map.
Preserve closed ledgers and frozen evidence. Keep this working queue and the
journal local and unpublished. Formal certification follows a complete
mathematical candidate; arithmetic Lean lemmas alone are not that candidate.
