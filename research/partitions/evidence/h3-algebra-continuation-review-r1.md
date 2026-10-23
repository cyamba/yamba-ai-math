# P010 round 1: two-elementary identity

Reviewed 2026-10-23 by `/root/h3_semantic_critic`, separately from author
`/root/h3_lean_algebra`. This is the first P010 challenge; historical
P007/P008 reviews and the completed P011 round-1 review remain unchanged.
Distinct roles do not imply independent errors or different models.

**Verdict: supported for the exact actual polynomial theorem below.** No
actionable semantic defect was found. Reconstruction and H3 completion are
outside this candidate and remain incomplete.

## Reviewed snapshots and execution

| File | SHA-256 |
| --- | --- |
| `../mathlib/PartitionH3/ElementaryProduct.lean` | `a260029980e2c396604b73ae145ca544c930bc344f58b8ee8371f2c184ace358` |
| `h3-algebra-continuation-r1.md` | `b602eb2269cd7268dd63982f42f843d4327f2d242b7e4c4f15f58b6b387c8412` |
| `../mathlib/PartitionH3/SubsetBridge.lean` | `6acac3a84779ea950c566406b0f71be9a908fb31a9f3256fe50cecbbb5b27deb` |
| `../mathlib/PartitionH3/Vandermonde.lean` | `450de9316322b90674611407fc4cd8d8654ec79e5b74b7df702d56e6f87f30f8` |
| `../mathlib/PartitionH3/Alternant.lean` | `f903afbdd32b36e2c83dcfdc3bc86654305431da74569de1e8895ca65a6a4caf` |

The imported algebra sources retain their previously reviewed hashes. The
critic independently ran `lake env lean PartitionH3/ElementaryProduct.lean`
using existing Lean 4.34.1/Mathlib dependencies. It exited zero without
diagnostics and printed the exact main type plus eight axiom reports, each
containing only `propext`, `Classical.choice`, and `Quot.sound`. The candidate
source hash was unchanged after checking. This was a direct source check,
not a second fresh-project build.

The critic also inspected `.runs/h3-p010-r1/elementary-receipt.json` and
`elementary-fresh.log`. The receipt reports a successful fresh output-file
check; both recorded source hashes match the candidate, and the actual log
SHA-256 matches
`86cca51d8efa2e0ba44778d7098ce4dbd35a70c1afd5a3b08046b9f3ee5b6193`.
The current manifest hash matches the receipt:
`519bb42602944b5e01f310ecde293c7679e00eb50ad218be6e063048656e020c`.
The critic did not independently measure the author's elapsed time or free
storage, provision dependencies, edit proof source, or use numerical checks
as universal evidence.

## Exact supported statement

```lean
vandermonde_mul_two_elementary (m a b : Nat) (hba : b ≤ a)
  (hab : a + b ≤ m) :
  vandermonde m * elementary m a * elementary m b =
    ∑ j ∈ Finset.range (b + 1),
      alternant (fun i => delta m i + twoColumnShape m (a + b) j i)
```

This is equality in the actual `MvPolynomial (Fin m) (Polynomial Int)`
ring. `elementary` and `alternant` retain their actual subset and signed
permutation definitions. On every summed index, the shape has exactly
`j` twos, `a+b-2*j` ones and `m-a-b+j` zeros. No coloring-expansion premise,
positive witness, positive alphabet assumption, or natural subtraction
outside justified bounds appears in the theorem.

## Semantic findings

1. **Collision and vanishing are justified on actual natural exponents.**
   `bump_prefix_cast` uses a `Fin m` index, so `delta_cast` applies without
   truncation. An adjacent-rise witness has `k+1<m`; the two-block search
   also proves `k+1≠a`. `bump_prefix_adjacent_collision` converts the integer
   calculation back to equality of the actual natural entries at two
   distinct indices. `alternant_bump_prefix_eq_zero` uses the previously
   checked repeated-exponent vanishing theorem; it does not discard a term
   merely because its intended sign or coefficient is unknown.

2. **The one-block and two-block finite sums are complete.** The first
   elementary multiplication retains exactly `prefixSubset m a`, whose
   actual cardinality is proved. For the second multiplication, the filter
   removes only terms proved zero. `Finset.sum_bij` maps every `j` in the
   inclusive range `0..b` to the actual `twoBlockSubset`. Membership uses
   its cardinality and no-rise proofs; injectivity uses actual bit-list
   injectivity; surjectivity uses the complete subset classification.
   Thus no canonical term is duplicated or omitted. This closes the
   two-elementary specialization gap retained in the previous P007 review.

3. **Exponent identification and boundary cases match the target.**
   `bump_prefix_twoBlockSubset` is equality of the entire natural exponent
   functions, not only of shapes or total degree. The hypotheses imply
   `j≤b≤a` and `2*j≤a+b≤m` on the summation range. For `m=0`, they force
   `a=b=0`; the empty alternant and both sides are one. For `b=0`, the sum
   has its single `j=0` term, and the checked boundary corollary permits
   every `a≤m`. Neither zero case has been excluded by an auxiliary
   nonemptiness premise.

4. **The declared bounds must be retained.** Dropping `b≤a` fails already
   at `m=1,a=0,b=1`: the right side becomes `x_0+x_0^2`, while the left
   side is `x_0`. Dropping `a+b≤m` fails at `m=0,a=1,b=0`: the left side
   is zero and the right side is the empty alternant one. These are
   counterexamples to weakened statements, not to the checked theorem.

## Remaining work and accounting

The optional reconstruction source was not inspected or approved in this
challenge. The module does not establish actual coloring symmetry, the
coloring/array coefficient bijection, signed finite-sum cancellation,
canonical padding removal, or the all-alphabet survivor equality. The lead
must include the new module in the final source-bound verifier and project
integration; this local proof check alone is not the final H3 receipt.

P010 accounting for this proposal/challenge is **5 of 16** declared proxy
units: 3 author units and 2 review units. This is manual collaboration, not
an executed harness provider run; units are neither tokens nor money. No
third historical review, H3 completion, or novelty claim is made.
