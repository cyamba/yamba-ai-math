# RR002 round 2 — final independent challenge

Reviewer: `/root/rr_plan_critic`, the separate critic profile. This is the
second and final authorized construction review, not a third repair round.
Only this review file was written by the critic in this round. No new
candidate, proof worker, installation, Lean increment or exposition increment
was started.

## Verdict

**Supported, with an elementary unformalized proof:** every frozen profile
defines a total, weight-preserving normalization from actual W to actual A.

**Refuted, with exact finite certificates:** none of the sixteen frozen
profiles is injective. Four disjoint witness groups below cover all sixteen.
Consequently none supplies W <-> A, and composing any of them with the known
A <-> C correspondence cannot supply W <-> C. The missing bridge remains
**incomplete**. This review neither certifies novelty nor rules out another
structural construction.

The partial normalization result and the finite-family obstruction are useful
outcomes of the bounded attempt. A successful finite check, a termination
argument, and a bijection are distinct claims here.

## 1. Exact semantics and universal partial proof

The implementation matches the proposal's four switches in the declared
order `(plateau_first, residue_guard, plateau_spread, merge_upper)`. In
particular, `plateau_first` selects the first *equal-top defective triple*
before pairs, not the first arbitrary defective triple. The fallback triple
scan occurs only after the pair scan fails. Zero removal occurs only in a
triple spread. These distinctions matter to the certificates.

The initial U encoding is lossless: if h is a conjugate column height, its
value is F(5q+r)=9q+s_r, s=(0,1,3,6,8). F is strictly increasing; its residue
determines r, so it has the stated inverse on its image. Summing weighted
column heights counts every box with its row weight, hence gives N. Sorting
these values ascending is reversible by reversing their order. Subsequent
R2 rewrites need not remain in the U domain; losslessness of the *initial*
encoding does not establish losslessness of normalization.

At every later step the state is an ascending positive list of sum N. The
only potentially nonpositive pair-spread entry is x-1 when x=1. Its possible
nearby pairs are (1,1) and (1,2); the first fails the residue guard, while the
second is not defective. Thus pair spreading has x>=2. Triple spreading has
nonnegative entries, and explicitly deletes its zero entries. All merging
rules produce positive entries. All five replacement forms preserve the sum.

For E(p)=sum p_i^2, the exact changes are:

| Replacement | Increase in E |
| --- | --- |
| (x,y) -> (x+y) | 2xy |
| (x,y) -> (x-1,y+1) | 2(y-x)+2 |
| (x,y,z) -> (x,y+z) | 2yz |
| (x,y,z) -> (x+y,z) | 2xy |
| (x,y,y) -> (x-1,y-1,y+2), zeros deleted | 2(y-x)+6 |

Every increase is at least two. Sorting and deleting zeros do not change E.
For positive parts of total N, E<=N^2. Hence the number of updates is at most
floor((N^2-E(initial))/2), in particular at most N^2/2. Empty input returns
empty. At termination there is no adjacent defect and no triple with z-x<=2;
because the entries are integers, these are exactly the literal A conditions.
This argument applies to every switch setting and does not use equal counts,
enumeration, or a purported inverse. Assurance: hand-checked algebra and
implementation inspection, not a proof-assistant certificate.

The claimed asymptotic resource class is compatible with the default
history-free program. There are at most N parts, each at most N. Charging
scans, sorting, comparisons, modulo-small-constant arithmetic, and the energy
checks gives O(N log^2(N+1)) bit work per update using elementary arithmetic,
and O(N^3 log^2(N+1)) overall; this is within O((N+1)^4). The initial direct
conjugation is also within that bound. Current states and temporary copies
use O(N log(N+1)) bits, within O((N+1)^2). This is an asymptotic argument,
not a measured worst-case constant or a formal analysis of Python's runtime.
The diagnostic full trace has a different, potentially cubic-size history;
the proposal correctly excludes it from the map's quadratic-space claim.
The exhaustive test enumerators are also not part of this map complexity.

## 2. Four exact collision certificates cover all sixteen profiles

Here `?` denotes either Boolean. These groups are disjoint and contain
8+4+2+2=16 profiles. Every displayed W is descending, has multiplicity <=4,
and has the indicated positional weight. Every common image is an actual A
partition of that weight.

| Profiles | Number | N | Distinct W inputs | Common image |
| --- | ---: | ---: | --- | --- |
| `??0?` | 8 | 7 | (2,1,1), (3,2) | (1,6) |
| `1?1?` | 4 | 3 | (1,1), (3) | (3) |
| `001?` | 2 | 8 | (1,1,1,1), (8) | (8) |
| `011?` | 2 | 8 | (4,2), (8) | (3,5) |

For `??0?`, U(2,1,1)=(1,6) is already normal. U(3,2)=(1,3,3) has no bad
pair, and its equal-top triple is merged to (1,6). Whether the triple is
examined before or after pairs has no effect. The residue guard and the
unequal-top merge choice are never used. Thus all eight profiles fail.

For `1?1?`, U(1,1)=(3) is already normal, while U(3)=(1,1,1). Plateau-first
spreading sends (1,1,1) to (0,0,3), hence (3). The other two switches are
unused. Thus all four profiles fail.

For the remaining four profiles, plateau processing follows bad pairs and
plateau spreading is enabled. For W=(8), the complete common prefix is

```text
(1,1,1,1,1,1,1,1)
 -> (1,1,1,1,1,1,2)
 -> (1,1,1,1,2,2)
 -> (1,1,2,2,2)
 -> (2,2,2,2)
 -> (2,2,4)
 -> (4,4).
```

Every step in this prefix is a bad-pair merge, for either residue setting.
For `001?`, the final pair is merged to (8), which is already U(1,1,1,1).
For `011?`, it is spread to (3,5). But U(4,2) follows
(1,1,3,3) -> (2,3,3) -> (3,5): the bad pair (2,3) takes priority over the
equal-top triple, and its sum five fails the spreading guard. The choice of
unequal-top triple merge is unused in both groups. This covers the last four
profiles, including the default `0111`.

These exact traces alone prove noninjectivity; they do not rely on the count
identity or on a claim that the witnesses are smallest. The independent
bounded enumeration below also found them at the first collision weights
3, 7 or 8 respectively. Minimality here has finite computational assurance,
not a separately formalized proof.

For any fixed profile P, write its map as T_P. A displayed pair u!=v has
T_P(u)=T_P(v). Therefore for every deterministic function H defined on that
output, H(T_P(u))=H(T_P(v)). No postprocessing of the output alone, including
the known A -> C map, can recover injectivity. This is the exact obstruction
scope: all sixteen listed algorithms and all deterministic compositions
through their unlabelled terminal outputs. It says nothing about unlisted
rules, priorities, intermediate labelled states, or all structural bridges.

## 3. Independently executed finite confirmation

The critic executed an ephemeral standard-library reference calculation,
without importing the author's generators, predicates, weights, or rewrite
function to define the reference side. It recursively generated ordinary
ascending partitions by choosing the first part and a nondecreasing tail;
filtered A using literal distance-two and adjacent-sum tests; filtered B by
the literal four residues; and formed W by reversing ordinary partitions of
every ordinary size <=30, imposing multiplicity <=4, and calculating the
positional weighted size independently. This search is complete through
weighted N=30 because every row weight is at least one.

It independently formed U by counting boxes in each column and applying the
five prefix values. A separately written rewrite routine formed each ordered
list of eligible moves and took its first member according to the frozen
priority. Only after constructing these reference results did it compare
them with `kr1.py`.

Results through all N=0..30:

* Actual A, B, and W sets agreed with their corresponding author generators.
  Their counts agreed at each N; the cumulative W count was 1,393.
* All 22,288 profile/input outputs and rewrite counts agreed exactly with the
  independent rewrite routine. Every output belonged to independently
  enumerated A of the right weight. Every update in the reference routine
  preserved weight and increased energy by at least two.
* The largest observed rewrite count was 33. This is empirical, not the
  universal bound.
* The first collision groups were exactly those above. The empty case and
  lower weights were included.
* The author's `kr1.py` SHA256 was
  `6a961d737f0bf5907a60c5ecc0922816323c2e01edac8b4a7561c74c321418a8`
  both before and after this comparison. The script's measured calculation
  time was about 1.32 seconds; that is not the parent's elapsed time or total
  project resource use. The critic did not measure a separate peak RSS.

The independent script was not saved as another project executable; this
review records its procedure and outputs. It did not independently enumerate
C or execute the full repository test suite. Those are not implied by the
figures above. Agreement through thirty establishes no all-N bijection.

## 4. Implementation and assurance review

No blocking semantic mistake was found in the frozen `kr1.py` rewrites,
termination invariant, column encoding boundary, or the inspected verifier
and tests. The tests retain empty objects, literal small boundaries, the
zero-padded C data model, the final column-height boundary, default failure,
all sixteen actual collisions, and every normalization's observed energy
bound. The verifier uses a failure-producing `--require-bijection` gate;
ordinary success explicitly reports that the bridge is unresolved.

The author's coefficient DPs and brute-force checks use different search
structures, but share definitions or constants with the generators. They
are algorithmic cross-checks, not independent source verification or proof
certificates. In particular, both C enumeration and its DP use the same
quadratic base formula, and both U processing and its DP use the same F.
The critic's separate A/B/W definitions reduce this particular shared-code
risk; they do not independently certify C's source interpretation. No
universal endpoint algorithm or Lean proof was executed in this round.

The verifier's 600-second alarm bounds a single process. The contract's ten
*cumulative* enumeration minutes, total storage, free-space floor, and parent
plus critic resources require the separate run ledger; they are not all
enforced by that alarm. RSS is observed after each weight, not preemptively
limited by an OS memory cap. Small successful runs do not demonstrate a
general hard memory limit. Final measurements must bind the final source
hashes: the earlier receipt before all-profile checks were added cannot stand
in for the updated verifier. Full repository tests and the repository checker
remain the author's completion responsibility.

The proposal's initial conjecture status is a historical pretest statement.
The final revision and summary must label all sixteen candidates **refuted**,
and the total-normalization claim separately **proved, elementary/unformalized**.
The family extension was informed by the default's collision; it is correctly
exploratory, not held-out validation. No further repair round is authorized.

## 5. Remaining mathematical obligation and source limits

The remaining new obligation is an explicit, uniform, invertible passage
between the lossless U domain and actual C, or between U and actual A followed
by the attributed A <-> C endpoint. It must assign a,b and zero-padded
increments by structural rules, without imposing the already-refuted
length(W)=a+2b refinement. For each state transformation, its admissible
domain, output state, and deterministic inverse must recover the branch,
position, and any arithmetic shift from the state itself. At termination,
all information retained during the construction must be represented in
actual C or actual A; an unbounded discarded history is not an inverse.
Both inverse laws, totality on both actual endpoint sets, and preservation
of N remain necessary. A forward energy measure supplies only one of those
obligations. This states the missing proof requirement; it does not propose
or test a third candidate.

Previously inspected sources remain attributed endpoints:
[Andrews–Keith, §§2–3 and §5 Theorem 6, preprint v2](https://arxiv.org/html/2203.05202v2)
for the weighted/regular-partition side, and
[Kurşungöz, §3 Theorem 7](https://arxiv.org/html/1808.01432)
for the gap/cluster side. The Stockhofe quotient-unit scaling issue recorded
in the source audit still requires care if that endpoint is implemented;
this round did not implement it. The inspected
[Mizuno v3](https://arxiv.org/html/2609.09653v3) and
[Xia v1](https://arxiv.org/html/2609.08816v1) counting results cannot be
relabeled as a new counting theorem. No new literature search was executed
in this final construction review. The absence of a checked prior direct
map remains an **unverified novelty question**, not an openness certificate.

Stop RR002 after recording this obstruction, the final source-bound receipt,
and the required engineering checks. Preserve the unresolved bridge instead
of promoting finite counts or normalization to a bijection.
