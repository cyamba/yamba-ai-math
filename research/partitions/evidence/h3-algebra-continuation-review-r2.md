# P010 round 2: alternating finite-support reconstruction

Reviewed 2026-10-23 by `/root/h3_semantic_critic`, separately from author
`/root/h3_lean_algebra`. This is the second and final P010 challenge, not a
reset of any earlier contract. Distinct roles do not establish independent
errors or different models. No proof source was edited.

**Verdict: supported for the exact generic reconstruction interfaces.** No
actionable semantic defect was found. The unchanged two-elementary identity
retains its round-1 support. Their application to the actual coloring
coefficient/survivor identity remains incomplete.

## Reviewed snapshots and execution

| File | SHA-256 |
| --- | --- |
| `../mathlib/PartitionH3/Reconstruction.lean` | `7162200879dbc87ffac85c61aedcbd1a723d52a64c3810d6a22ed07b672da59f` |
| `h3-algebra-continuation-r1.md`, completed packet | `66abe78c6627d0496179901745acd078a1d4832875814f5724341dc0bdbd139a` |
| `../mathlib/PartitionH3/ElementaryProduct.lean`, unchanged | `a260029980e2c396604b73ae145ca544c930bc344f58b8ee8371f2c184ace358` |
| Pinned Mathlib `Mathlib/Data/Fin/Tuple/Sort.lean` | `9075b412b4e447c4a01590aceaf0f05d4cf58c419192eb016e9171241a753567` |

The critic inspected the actual source and the sorting/uniqueness interfaces
in the local pinned Mathlib source. An independent
`lake env lean PartitionH3/Reconstruction.lean` check exited zero without
diagnostics, printing the exact two principal types and ten dependency
reports. All ten used only `propext`, `Classical.choice`, and `Quot.sound`.
The frozen source hash was unchanged after checking. Existing Lean 4.34.1
and imported dependency products were reused; this was not a second fresh
temporary-project build.

The critic separately inspected the author's actual
`.runs/h3-p010-r1/reconstruction-receipt.json` and `reconstruction-fresh.log`.
The receipt records exit zero, a fresh output-file check, matching before/
after source hashes, and manifest hash
`519bb42602944b5e01f310ecde293c7679e00eb50ad218be6e063048656e020c`.
The actual output hash matches the recorded
`dceaf81f053a38f07907f04aa8933271cd0e0dad08c6981f5401fb1a0cd307ef`;
its ten reports and exact signatures match the independent check. The
author's combined project-build claim was not independently replayed by
this critic. Final clean source-bound verification remains the lead's
separate responsibility. No new provisioning, deletion, or numerical
experiment was used as proof evidence.

## Exact supported statements

`IsAlternating p` means that for every actual `Equiv.Perm (Fin m)`,
`rename sigma p = signCoeff sigma * p`, with the actual library sign.
The two principal types are:

```lean
alternating_eq_of_dominant_coeff {m : Nat} (p q : Poly m)
  (hp : IsAlternating p) (hq : IsAlternating q)
  (hc : ∀ gamma : Fin m → Nat, StrictAnti gamma →
    p.coeff (powerExponent gamma) = q.coeff (powerExponent gamma)) : p = q

alternating_reconstruction {m : Nat} (p : Poly m) (hp : IsAlternating p) :
  p = ∑ e ∈ dominantSupport p,
    MvPolynomial.C (p.coeff e) * alternant (fun i => e i)
```

Here `Poly m` is the actual polynomial ring over integer polynomials, and
`dominantSupport p` is exactly `p.support` filtered by strictly decreasing
natural coordinate values. No guessed support, positivity, homogeneity,
degree bound, or coloring expansion is assumed.

## Semantic findings

1. **Permutation covariance has the correct inverse and sign.**
   `rename_antisymmetrize` reindexes by left multiplication by `sigma` and
   uses the square-one property of the actual permutation sign.
   `coeff_rename_powerExponent` moves the exponent to
   `gamma (sigma.symm i)`; `alternating_coefficient_perm` consequently
   relates the two coefficients with exactly that sign. The proof does
   not substitute `sigma` for its inverse. `alternant_isAlternating` and
   `vandermonde_mul_isAlternating` concern the actual polynomials; the
   latter explicitly requires symmetry of its other factor.

2. **Repeated-coordinate coefficients vanish in the stated coefficient
   ring.** For two distinct equal-coordinate indices, swapping them leaves
   the entire exponent unchanged and negates its coefficient. The proof
   then takes every univariate coefficient in `Polynomial Int` and uses
   integer torsion-freeness. No implication from `c=-c` in an unspecified
   ring, or division by a possibly zero two, is used.

3. **Sorting and uniqueness cover every remaining coefficient.** An
   injective exponent function is sorted using `Tuple.sort` on
   `OrderDual Nat`, yielding a strictly decreasing natural vector.
   The proof transports coefficients using `sigma.symm`, as required by
   item 1. A noninjective exponent instead falls under item 2. The inspected
   `Tuple.unique_antitone` states equality of the sorted value functions,
   not automatically of their sorting permutations; the proof correctly
   adds strict-antitone injectivity to recover `sigma=1` in
   `dominant_permutation_eq_iff`. No uniqueness premise is assumed.

4. **The finite reconstruction uses all and only actual dominant support
   coefficients.** `alternant_dominant_coefficient` proves the coefficient
   is one at its own strictly decreasing exponent and zero at every other
   one. `dominantReconstruction_coefficient` handles both support membership
   and absence, using actual zero coefficients outside support.
   The resulting finite sum is alternating and has exactly the input's
   dominant coefficients; the prior extensionality theorem proves equality.
   There is no orbit-size factor, missing sign, or implicit infinite sum.

5. **Zero variables, zero polynomial and necessity of alternation are
   handled at the correct scope.** `m=0` is unrestricted: strict antitonicity
   on `Fin 0` is vacuous, its exponent function is unique, and its alternant
   is one, giving the expected reconstruction of a constant polynomial in
   zero multivariate variables. Empty support gives the zero sum. Positive
   exponent entries are never required. Alternation must be retained:
   `m=2,p=1` has no strictly decreasing supported exponent, so the proposed
   reconstruction without that hypothesis would give zero instead of one.
   This is a counterexample to a weakened theorem, not the reviewed one.

## Remaining application and accounting

The generic reconstruction gap from the earlier algebra reviews is closed
at these exact interfaces. Applying them to `vandermonde * chromatic` still
requires actual coloring symmetry and the correct dominant coefficients.
The coloring/array bijection, complete signed-sum cancellation, canonical
padding/family correspondence, restriction to the relevant two-column
exponents, and all-alphabet survivor assembly remain separate work. This
review does not establish those statements or unconditional H3 completion.

The reported P010 account before this challenge was 8 of 16 declared proxy
units. This second challenge adds 2, giving **10 of 16**. Both permitted P010
review rounds are now used; the unused numerical allowance does not create
another review round. This is manual collaboration, and units are neither
tokens nor money. No novelty claim is made.
