# Phase 2: source review and a starting point for discussion

25 October 2026. Documentary review only: no mathematical scripts, census,
Lean build, research agents, publication, or external messages were run.
Closed RR006/RR007 and Codex Phase 2 records are unchanged.

## Verdict and exact objective

**Incomplete:** the inspected Argon implementation does not give a universal
KR1 bijection. It contains substantive local constructions and a finite
round-trip verification routine, but higher-sector reconstruction still
requires a finite apex table. Replacing that table alone would not establish
that the growth operators have the required universal validity, disjointness,
image characterization, and inverse properties.

The objective is explicit, terminating, weight-preserving, mutually inverse
algorithms between residue partitions B (parts 1,3,6,8 modulo 9) and the gap
partitions A specified in CLAUDE.md. The leading factorization is

    B <-> U <-> C <-> A.

U is the lossless weighted-column model; C consists of
`(a,b,mu,nu)` with ascending, nonnegative arms of lengths a and b and weight

    a^2 + 3ab + 3b^2 + sum(mu) + 3 sum(nu).

The new constructive bridge being sought is U <-> C. The counting identity
itself already has reported proofs: [Mizuno, v3, Theorem 1.1 and introduction](https://arxiv.org/html/2609.09653v3)
and [Xia, v1, Theorem 1.1](https://arxiv.org/html/2609.08816v1).
Their statements and proof outlines were inspected here, not independently
audited in full. Novelty of a proposed explicit bridge remains **unverified**.

## Evidence chronology, not a reconstructed conversation

1. Argon's Phase 1 article/constructions entered the inspected research
   branch through commit `4e2492d`. The saved program describes the a3,b0
   sector, finite KR1 coverage through 26, and tableau results at n=5.
2. The separate Codex Phase 2 checkpoint `5cbc2440aab896d3f7de9e45bba2bac027f9c5cb`
   records the reviewed H3 partial KR map (3498/5461 through 40), exact
   C-only recursion, and finite n=6 tableau cancellation. It explicitly
   leaves full KR1 unresolved; no formal checker ran in that attempt.
3. Argon's commit `e43a3d02fe3abc60364feaf4a75985b4be602247` adds the
   higher-sector octant implementation and n=6 tests. Its saved PR body
   calls Phase 2 complete and calls the finite round trip lookup-free.
4. Two review comments on that commit identify the wrong printed rotation
   branch and wrong determinant inverse below.
5. Argon's inspected local head is
   `97d6561a855ea4aac4fb89c03a6fb543c9edd56e`, a merge from main.
   Both printed errors and the 78-entry table remain in that snapshot.
6. Christopher's newly supplied later Argon audit acknowledges the missing
   general apex law and reports the weight-41 failure.

This is the order supported by the saved code, program, PR material and
supplied audit. The full Argon conversation has not been supplied or located.
The Antigravity article and scratch files are available, but they are not a
transcript. We cannot yet identify the precise conversational moment or
reason that Argon came to believe the full goal was complete.

## Claim-to-evidence map

All Argon paths below refer to the inspected checkout
`/Users/christopheryamba/YambaCode/Math/yamba-ai-math-rogers-ramanujan` at
the head above. The accompanying handoff pins the separate Codex record.

| Claim | Inspected evidence | Defensible boundary |
| --- | --- | --- |
| Universal KR1 map | `checks/rr004_multidim_cones.py`, especially `OCTANT_APEX_PAIRS` and `reconstruct_octant` | **Incomplete.** Both directions require membership in the saved apex dictionaries. |
| Complete finite round trip through 40 | `verify_roundtrip` and the article/PR report of 5461 cumulative states | **Reported finite evidence.** The routine checks B inputs, valid distinct A outputs, endpoint reversals and U reconstruction, using equal finite B/A counts. Not rerun here. The pasted 2693 count does not match the inspected 5461 cumulative claim. |
| Entire a3,b0 sector | Explicit piecewise forward/inverse routines and article table | An all-parameter candidate exists without an apex lookup for this sector. The separate reviewed Codex record also has an infinite a3,b0 result for its own pinned map. This review does not transfer that assurance automatically to every Argon branch or re-prove its full inverse language. |
| 6D cone family | Article theorem/proof and `verify_6d_cone_theorem` | An ordinary universal argument is presented, plus a bounded test. There is no corresponding partition-membership/disjointness theorem in the inspected Lean file. The statement requires a nonempty shorter tail when x=0; omitting this is false. |
| KR1 Lean certification | Eight `kr1_*` statements in `MultidimensionalFerrers.lean` | Weight arithmetic, including scale-three and routing identities. They do not formalize U/C membership, the Python operations, bijectivity or universal coverage. |
| All four printed branches of Phi221 preserve inversions | Article equation at line 155; Python `phi_221` | **Refuted as printed.** Python filters candidates by validity and exact inversion equality, so it implements a different selection rule. |
| General hook-slide theorem is fully formalized | Article theorem and Lean hook declarations | Article supplies a general ordinary argument and explicitly qualifies its Lean check to k=3, m=2,3. The formal declarations use a three-cell arm and an arbitrary leg; they do not quantify over arbitrary arm length k. |
| General-n signed cancellation | `eight_sector_e51_injection` and cascade lemma | **Incomplete.** Argon's n=6 routine uses enumerated target sets and a global used set. The universal cascade is a local invariant statement, not a total global cancellation theorem. |

The Lean receipt records a successful build. SHA-256 of the inspected
`MultidimensionalFerrers.lean` matches its recorded
`5cac97afaf92c2cbaad088764101c06a77ec1e1591aebaec76f9a71f66959e66`;
the two direct imported source hashes also match the receipt. No fresh build
was performed. A source-bound successful build supports its exact formal
statements; the prose theorem count does not extend their scope.

The older `checks/verify.py --require-bijection` is not an independent audit
of Argon's new algorithm: its report initializes the bridge and certificate
as absent and returns 2 when that flag is present. Its failure is not a
counterexample to a new map; the explicit lookup dependency is decisive here.

## The three important failures

### 1. A finite apex assignment was described as lookup-free

`reconstruct_octant` splits off d1, d3 and q2, preserving a residue r2, then
looks up the remaining C apex in `APEX_C_TO_U`. The inverse peels the moves
in reverse order and uses `APEX_U_TO_C`. There are 78 saved pairs, covering
the apexes needed by the reported finite tests through 40.

The available scratch file `inspect_apex_table.py` constructs candidate
apex correspondences by taking residual U objects, sorting them, and zipping
them with the residual C list separately at each weight through 40. This is
direct evidence of finite enumeration-based pairing in the development
artifacts, not an intrinsic all-weight apex rule. The file's presence alone
does not prove its execution history.

**Static witness of missing forward totality:** for a=4,b=0 and
`mu=(7,7,7,7)`, weight is 44. All three stripped growth coordinates are zero,
so the C apex is the input itself. It is absent from the weight-at-most-40
table, and reconstruction raises `OutsideRestrictedDomain` before taking
any growth step. This follows by reading the branch; no run was made.

**The supplied weight-41 target witness is consistent with static tracing:**
`U=(18,15,8)` decodes to heights `(10,8,4)`, with drops `(2,4,4)` including
the terminal drop. It is a valid U object. The old inverse and a3,b0 inverse
reject it; none of the one/three/six peeling branches applies. It is not a
listed U apex, so `decompose_octant` raises the reported exception. This is
a manual trace of one supplied witness, not a new numerical census.

### 2. A tested routine was substituted for a different printed formula

For `h=(2,2,4,5,5)`, the incomparability edges are `(1,2),(3,4),(4,5)`.
The source

    1 4
    2 5
    3

has one graph inversion, from edge (3,4). The printed second branch gives

    2 3 5
    1 4

with two, from (1,2) and (4,5). Thus it changes q-weight. Python rejects
that candidate and accepts the fourth candidate `((1,3,5),(2,4))`, whose
weight is one. Checking Python therefore does not validate the printed rule.
Lean's `promote32` theorem concerns the first rotation under its own
comparability hypotheses; it does not certify this failed second branch.
See the [saved original review](https://github.com/cyamba/yamba-ai-math/pull/15#discussion_r4368823775).

### 3. A set comparison did not exercise the claimed inverse

The determinant convention is `kappa[sigma(i)] = mu'_i-i`. Those right-hand
values strictly decrease with i. Therefore their sorting permutation is
sigma itself. The article instead takes its inverse.

With zero-based indices, `beta=(0,0,3)` gives keys `(0,-1,1)` and decreasing
order `(2,0,1)`. This recovers columns `(1,1,1)` and sigma `(2,0,1)`.
The printed inverse returns `(1,2,0)` and exponents `(2,2,-1)`, including
a forbidden negative exponent. Python compares beta sets; it does not call
and round-trip this inverse. See the
[saved original review](https://github.com/cyamba/yamba-ai-math/pull/15#discussion_r4368823779).

These are mathematical/expository review findings, not demonstrated Lean
compiler failures. The later user-supplied audit also describes the e51
residual sectors in the reverse sign direction: in the inspected code,
T51/T42/T3111 are negative and T21111/T321 are positive. The broad point
about residual degree-based matching remains valid.

## Intuition for the partition gap

For a3,b0, write

    mu=(d3, d3+d2, d3+d2+d1).

The common rise d3 adds three units of weight, the middle rise d2 adds two,
and the final rise d1 adds one. Splitting `d2=3q2+r2` gives

    weight = 9 + 2r2 + 6q2 + 3d3 + d1.

For example, `mu=(1,4,6)` has `(d3,d2,d1)=(1,3,2)` and weight 20.
It is a small base state plus motion along three nonnegative directions
with weight steps 6,3,1. In this special sector those directions describe
all the arm's freedom, apart from the small residue.

For a4,b0, however, every `mu=(x,x,x,x)` already has d1=d3=q2=0.
There are infinitely many such apexes. For larger a and b, the unstripped
prefix of mu and all of nu retain still more freedom. Growth rules around
an apex do not specify which apex to use or how to recover its parameters.
The 78 entries are a finite sample of this residual classification problem.

The exact C-side scale-three grammar in the reviewed Codex record suggests
a possible way to organize that remaining information recursively. A U-side
cut must reproduce the same child and retain the entire boundary data with
the correct weight. Equality of base weights alone does not supply that cut.
The earlier fixed quotient cut is specifically refuted: its child terminal
height is at most two, so it cannot produce the retained child U=(6) needed
by the recorded weight-18 C edge. The erroneous earlier bound of one was
corrected and must not be reused. See
`research/phase2-20261025/recursive-lift/revision.md` and its final review.

## Next discussion, before another run

**Proposed direction, unverified:** describe apexes recursively, with an
intrinsically recoverable boundary/carry state, then prove the U and C
boundary languages correspond. The immediate question for a geometric
picture is what the extra coordinate stores: the common offset, a remainder,
a seam, or the origin of a rerouted component. Its value must be recoverable
from the final unmarked partition, or encoded reversibly within that partition.
Attaching a free extra label would change the target problem.

The next proof obligation is an exact image/inverse rule for a genuine
infinite apex family, or a compatible shrinking U cut and glue. It must
include admissibility, weight, termination, both inverses and coherent
interaction with any partial assignments it claims to preserve. The older
H3 weight-20 gap is already assigned in Argon's finite table; it must not
be presented as a failure of this different implementation.

This note proposes no repaired theorem and starts no experimental contract.
The journal remains unpublished. We should use this review to discuss
Christopher's picture before selecting a construction or author/critic run.

## Downloaded PDFs located after Christopher's reply

Christopher does not have a conversation export and asked whether changing
Antigravity/Gemini modes would help. No mode change is required for this review,
and no claim about the application's export capabilities was established.

Two likely PDFs were found in Downloads and inspected by text extraction and
page rendering:

- `multidimensional_ferrers_article.pdf`: 10 pages; its SHA-256
  `f2d16e346999dd1cebafcdca942f41ae8fb3bb053adc2a656f8534ffe54a37e5`
  is identical to the research checkout's PDF. It contains the broad completion
  language and the finite weight-40 claims discussed above.
- `height-two-positivity_for_gemini.pdf`: 11 pages; an earlier height-two
  tableau paper whose first page explicitly limits its claims to that scope.

These are papers, not conversation exports. They help establish the written
claims but do not recover the complete dialogue. Christopher has not yet
confirmed that these are the two downloads he meant.
