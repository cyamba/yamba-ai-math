# Separate semantic review of finite-family cancellation

Reviewed 2026-10-21 under P006's two-round author–critic contract. The root
agent authored the proofs; `/root/positivity_audit` reviewed their meaning
without editing them. These are separate role identities, not a claim of
statistically independent errors or different model capabilities. This was a
manual collaboration, not an executed harness provider run.

## Round 1: target and obligation review

**Verdict: the target is supported; implementation was incomplete.** The critic
required complete actual-tableau families and uniqueness, a shape-derived split
index, the full image/complement degree-count partition, explicit empty and
maximal-index behavior, and a finite-vertex interpretation of `NoThreeChain`.

For the external audit, the critic identified `historyWitness` as the decisive
upstream dependency. The final finite table is downstream of an existing
positive-expansion witness. Inspecting that table alone would not audit the
general theorem.

## Round 2: final source review

**Verdict: supported for H1/H2; no actionable mathematical defect found.**

The reviewed declarations are:

- `mem_family`, `family_nodup`: exact actual-tableau/shape membership and no
  duplicates, without assuming enumeration completeness.
- `pair_decomposition`, `bubbleAt_family`, `bubbleAt_family_injective`,
  `bubbleAt_family_weight`: the source shape determines the split, and the
  actual map has the required target, injection and inversion degree.
- `degreewise_cancellation`, `height_two_degreewise_cancellation`: a natural
  addition identity for every index and degree, using the full image complement.
- `empty_vertex_degree_count`, `single_vertex_degree_count`,
  `survivorFamily_empty_source`: the empty, singleton and maximal-index cases.
- `finiteRelation_on_vertices`, `finiteRelation_height`, `finiteRelation_asym`,
  `finite_height_two_degreewise_cancellation`: hypotheses need hold only on
  the finite vertex set when the relation is extended by false elsewhere.

The critic found no hidden coefficient premise, proxy positivity definition,
circularity or missing hypothesis in this scope. The root subsequently changed
one explanatory comment; the proof declarations were unchanged. The final
hash-bound source reproduction is [verification.json](../lean/verification.json).

**Retained gap:** H3 is unproved. These finite counts have not been connected
in Lean to actual proper-coloring polynomials and their elementary expansion.
The source inspection and review do not certify the claimed external general
proof. Limited free disk motivated deferring its build; the 15 GiB ceiling is
not a demonstrated minimum requirement or proof that a build is impossible.

The critic reviewed source semantics and did not independently measure disk
space or execute the clean reproduction. Those checks have separate recorded
outputs. No third mathematical review round was used.
