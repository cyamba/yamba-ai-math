# RR003 result and mathematical handoff

**Complete explicit KR1 bijection: NOT ACHIEVED.** The governing objective
has not changed: actual residue parts1,3,6,8 modulo9 must correspond to
actual ascending gap partitions, with universal validity, weight, termination
and both inverse proofs. No universal U–C bridge has been accepted, no
complete residue–gap algorithm is claimed, and novelty remains unverified.
The deadline bounds this attempt rather than redefining success.

RR002 was preserved in local checkpoint `5eec6bb`. RR003 work is local to
this checkout; no pushing or publication is authorized or performed. The
[contract](contract.md), [actual execution](execution.md),
[machine-readable execution record](execution.json) and
[compact verification evidence](verification-summary.json) retain resources,
assurance and provenance. Frozen earlier files describe their historical
stage; this result is the current status.

## What is proved, with its assurance limit

| Result | Universal mathematical content | Assurance |
| --- | --- | --- |
| [Round one](round-1-proposal.md) | U–C bijection for a=0,1 and a=2,mu_1=0,1, arbitrary b/nu; intrinsic a,b, explicit Q cores and reversible operations | Written proof supported by [separate critic](round-1-review.md), ordinary manual-review assurance |
| [Round two](round-2-proposal.md) | All zero-pair a=2 and mixed a=2 except mu_1=4,5,9; recoverable carries | Written proof supported by [separate critic](round-2-review.md); full bridge explicitly incomplete |
| [Final a<=2 extension](round-2-revision.md) | All C with a<=2, arbitrary b,mu,nu, onto an intrinsically recognized U subset | Universal author argument; **no separate semantic review of this extension** |
| [Residue–U endpoint](endpoint-stockhofe.md) | Full unit-normalized Stockhofe algorithms at this interface | Established construction attributed to Andrews–Keith; new code and boundary audit author-only |
| [C–gap direct merge](endpoint-cluster-merge.md) | Full intrinsic single/pair extraction, threshold merge, weight and both inverse proofs | Attributed Kurşungöz endpoint; this direct formulation has a universal author argument, separate review outstanding |
| [Restricted residue–gap composition](partial-composition.md) | All gap partitions with at most two intrinsic singles, and a literal recognizable residue subset | Universal author composition argument; not the complete family |
| [Classical three-sector](three-divisible-foothold.md) | Conjugation on every three-divisible U; unbounded intrinsic a,b and a coupled reversible operation | Classical map; author coordinate specialization, no novelty claim |
| [Small charge](recursive-repair.md) and [separated core](charge-separated-core.md) | Zero/one/two ones plus arbitrary three-sector core; all-ones and further arbitrary-charge inputs under explicit separation hypotheses | Universal author arguments on the stated restricted domains, no separate review |
| [Auxiliary product split one](product-involution.md) | Full P2 <-> P3 disjoint-union literal cut family K | Universal author involution/path argument; no separate semantic review |
| [Auxiliary product split two](second-product-involution.md) | Weighted bit times P2 <-> original P1 disjoint-union literal cut family L | Universal author involution/path argument; no separate semantic review |
| [Intrinsic K branch](cut-branch.md) | Normalized K[-2] <-> an intrinsically specified P3 subset; cut recovered by disjoint intervals | Universal author proof; companion L branch remains missing; read [erratum](cut-branch-erratum.md) for the rejected proposal |
| [Middle source model](middle-source-model.md) | Positive two-cut interpretation of A2 and a literal B1 auxiliary family from Xia | Attributed algebraic specialization, author-only; verification enumerator supplies no branch bijection |

The elementary [auxiliary seed injection](recursive-source-seed.md) and exact
source/target grammars are also preserved. The preceding moving-pair
interpreter's finite agreement has not been promoted to a universal conformance
proof; the direct merge has its own argument. No final author result in this
table is represented as having received a third critic challenge. All
established constructions retain attribution and inspected-depth limits in
[sources](sources.md), the [closing primary-source comparison](closing-source-comparison.md)
and their later comparison records.

## Executed finite checks: implementation evidence, not proof

All actual-domain sweeps stayed at weights<=30. Each selected candidate was
frozen before its pilot; successful pilots preceded the larger runs. The
K branch uses actual K<=30 and P3<=28 because it removes a compulsory two.
Explicit structured witnesses above30 are individually identified, not
larger sweeps. Previously explored weights are exposure, not held-out data.

| Frozen implementation | Pilot | Larger check |
| --- | --- | --- |
| Reviewed first U–C map | through12 | 376 round trips each way through30 |
| Reviewed second U–C map | through12 | 606 each way through30 |
| Final a<=2 map and its residue–gap composition | through12 | 643 each way through30 for each interface; at N30 only70/195 objects |
| Full Stockhofe endpoint | through12 | 1,393 each way through30 |
| Full direct gap–C merge | through12 | 1,393 each way through30 |
| Classical three-column sector | through12 | 82 each way and82 coupled operations through30 |
| Small-charge repair | through12 | 202 each way through30 |
| Separated-core extension | through12 | 324 each way through30 |
| Auxiliary source seed | through12 | 405 each way through30 |
| Full P2 split | 34 P2 =24 P3+10 K | 780 P2=535 P3+245 K; 298,486 audited path steps including reverse checks and direct samples; max736 steps |
| Full weighted-bit/P2 split | 60 packets=59 P1+1 L | 1,449 packets=1,393 P1+56 L; max163 steps |
| Intrinsic K branch | 10 each way, actual K<=12 | 245 each way, actual K<=30/P3<=28 |
| Positive middle source model (coefficient checks only) | 7 two-cut objects<=12; 2 middle objects<=5 | 111 two-cut objects<=30; 75 middle objects<=23, with actual L<=30 |

Validity, exact weights, collisions, missing images and round trips were
checked on both actual domains, with empty objects, zero counts/increments,
repeated columns, terminal boundaries and earlier collisions. The separate
critic independently regenerated literal domains and reproduced both reviewed
maps and critical counterexamples. [Portable copies](reproduction/README.md)
of those two independently authored scripts preserve provenance; reproducing
them is not independent review of later author work.

The full repository suite passes **90 tests** after functional changes.
The final repository checker/planner and exact resource totals are recorded
in execution.json. No Lean run or complete-bijection acceptance is implied
by those engineering checks. `rr003_partial_verify.py --require-bijection`
continues to return exit2, including under optimized Python.

## Preserved failures and what each actually refutes

* Maximum-only cost-two column carries fail literal terminal/residue bounds.
  A mixed carrier overlay collides at38. Neither refutes every core mechanism.
* The weight43 single-charge insertion is valid and terminating but not
  injective: distinct cores have the same output and different move words.
* A third-one two-branch extension collides at9; an unrestricted one-new-single
  arbitrary-charge rule collides at7. Restricted repairs retain their hypotheses.
* [Naive union/fallback](partial-overlay-obstruction.md) of the two partial
  endpoint maps collides at9: residue(1,8) and residue(3,6) both give gap(3,6).
  Their values already disagree on common inputs at4. Their image counts
  cannot be added to claim coverage.
* [Fixed residue-count seed lift](recursive-seed-lift-obstruction.md) is
  impossible: five explicit weight34 sources would have only four targets.
  The later involutions change counts and avoid precisely that restriction.
* The rejected L conversion has an [explicit index-error correction](cut-branch-erratum.md).
  Its literal next-level replacement fails weight preservation; the intended
  same-level variant is still noninjective. [Two local full pairs](l-branch-boundary-obstruction.md),
  L cuts(0,(7,11)) and(0,(8,10)), both give(3,3,3,4,5,6), target24.
  This exposes discarded phase data even when the cut index is fixed.
  The same corrected rule also overlaps the intrinsic K branch at target26;
  both injectivity and disjointness need repair.
* A [local three/six phase flag](l-branch-phase-obstruction.md) still collides
  at target45. More generally eight explicit normalized L inputs at60 have
  only seven weight66 outputs if both four/five counts and these output
  levels are fixed. That class of local repairs is impossible; a later
  construction must change another statistic. This is an author-only argument.

These are exact counterexamples or conditional impossibility arguments,
not a claim that KR1 has no structural bijection. They are progress, not
completion. Frozen failed records and receipts remain available.

## Exact next unresolved lemma

**Leading core route:** find a single disjoint exhaustive U decomposition for
arbitrary a, with intrinsic a,b and recoverable zero-padded increments, or
replace the present partial assignments with a coherent better representation.
U=(6,3) and C=(3,0,(0,0,0),()) at weight9 remain omitted. The executable
partial composition still omits residue(3,6) and gap(1,3,5). A new marker
family for one small parameter is not a proof of global coverage.

**Concrete recursive alternative:** retain the proved K[-2] branch into P3.
Construct a cost6 embedding of L[-7] into its complement, recovering both
cut and the local full-pair phase, allowing output count/level carries
where the fixed-row obstruction requires them, then a literal cost3 H_(1,2) branch and
compatible inverse branches for every n. The two auxiliary product splits
now give real positive initial source models. A final [source-derived
two-cut model](middle-source-model.md) also supplies a literal middle source
family. A frozen verification-only enumerator checks its coefficients,
but no matching branch map or separate audit is supplied. These do **not** supply the
remaining positive three-state matrix decomposition, decreasing extraction
measure or gap-path correspondence. Equal analytic recurrences cannot fill
those missing maps. [Mechanism record](mechanisms.md) states the actual rules,
selection evidence and closest inspected work.

Before treating final author lemmas as accepted components, obtain a separate
semantic audit under a newly authorized review budget. Both RR003 critic
rounds are exhausted. A complete solution still requires executable full
endpoint composition, universal validity/weight/termination/inverse arguments
and separate review. Lean certification and article exposition remain explicit
subsequent obligations; novelty must be checked before any claim of a new
result or historical significance.

## Complexity and learning at handoff

Column formulas, endpoint implementations and the intrinsic K branch have
conservative polynomial bounds within preferred quartic work/quadratic
auxiliary bits. The auxiliary involution walks have only a proved
O((N+1)^3 log(N+2) 2^(3N+3)) work upper bound and quadratic auxiliary-bit
bound. This is not an exponential lower bound or a measured asymptotic
runtime. Their known work bound exceeds the preferred target. A final-map
contract would have to state that allowance explicitly unless a stronger
polynomial bound is proved. All binding investigation limits stayed in force;
no complete-map complexity has been established.

Decisive obligation at handoff: coherent universal coverage with recoverable
branches, not more finite agreement. Actually obtained: reviewed restricted
column theorems, further author proofs and executable endpoints/partial maps,
positive auxiliary decompositions, one intrinsic branch, and exact obstructions.
The next step follows because the missing source phase and global U statistic
are now explicit mathematical questions, not implementation gaps.

One transferable workflow hypothesis, **unvalidated**: combining an intrinsic
inverse statistic with a separately audited local cancellation may expose
which information a failed direct map discards. This run does not evaluate
a general harness change, establish a higher discovery success rate, or
change the original success criterion after observing results.

For reproduction, preserve all freezes and earlier failures. Use fresh ignored
output paths under a separately declared resource budget; the RR003 meter
must not be reset or used to extend its original deadline. Verifiers are
self-contained standard-library scripts in ../checks. The next session should
start with this status, the two critic reviews, the final author proofs and
the local L full-pair obstruction, rather than restarting coefficient searches.
