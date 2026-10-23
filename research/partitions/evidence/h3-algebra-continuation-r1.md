# P010 author proposal, round 1

Status: **proved by Lean kernel check** for both candidates below. The
two-elementary identity has passed the separate round-1 critic review in
`h3-algebra-continuation-review-r1.md`; reconstruction awaits separate review.
The previous P007/P008 sources and accounts
remain frozen. This proposal is the 3-unit P010 dispatch authorized on
2026-10-23. No nested agent, download, toolchain or dependency provisioning
was used. H3 as a whole remains incomplete.

The round-1 critic inspected the candidate-1-only handoff snapshot with hash
`b602eb2269cd7268dd63982f42f843d4327f2d242b7e4c4f15f58b6b387c8412`.
This handoff was subsequently extended to record candidate 2 and its check;
the reviewed candidate-1 source hash has never changed.

## Candidate 1: actual two-elementary identity (frozen)

Source: `research/partitions/mathlib/PartitionH3/ElementaryProduct.lean`.
SHA-256:
`a260029980e2c396604b73ae145ca544c930bc344f58b8ee8371f2c184ace358`.

The checked public type is:

```lean
theorem vandermonde_mul_two_elementary (m a b : ℕ) (hba : b ≤ a)
    (hab : a + b ≤ m) :
    vandermonde m * elementary m a * elementary m b =
      ∑ j ∈ Finset.range (b + 1),
        alternant (fun i => delta m i + twoColumnShape m (a + b) j i)
```

`twoColumnShape m n j i` is `2` for `i.val < j`, `1` for
`j ≤ i.val < n-j`, and `0` thereafter. Here `j ≤ b ≤ a`, so `2*j ≤ a+b ≤ m`;
the block lengths are exactly `j`, `a+b-2*j`, and `m-a-b+j`. The statement uses
the pre-existing actual `MvPolynomial` elementary functions and signed
permutation alternants. There is no coloring-expansion premise or positivity
witness.

The argument first applies `alternant_mul_elementary` to `delta`. Any bit
rise outside a cut produces equal adjacent natural exponents: the checked
`delta_cast` and `bump_prefix_cast` justify the integer calculation at indices
strictly below `m`. `bump_prefix_adjacent_collision` returns an equality of the
actual natural entries. `alternant_bump_prefix_eq_zero` therefore kills every
term outside the two no-rise blocks. At cut zero, `noRise_iff_prefix` leaves
one initial-segment subset, proving `vandermonde_mul_elementary` for every
`a ≤ m`. For the second elementary factor, the actual subset classification
is transferred through a `Finset.sum_bij`; injectivity uses the previously
checked candidate uniqueness, and surjectivity uses the complete no-rise
classification. `bump_prefix_twoBlockSubset` identifies each retained natural
exponent vector with `delta + twoColumnShape`.

All natural subtraction bounds are explicit. `delta` is cast only at a
`Fin m` index. A collision witness has `k+1 < m`, and never crosses the cut
(`k+1 ≠ a`). The target needs exactly `b ≤ a` and `a+b ≤ m`. No positive
alphabet or positive index assumption is used. Checked corollaries are
`vandermonde_mul_two_elementary_empty` (`m=a=b=0`) and
`vandermonde_mul_two_elementary_zero` (`b=0`, arbitrary `a ≤ m`). Removing
`b ≤ a` can already fail at `m=1,a=0,b=1`: the displayed right side would
include the extra `j=1` alternant. This is an algebraic reproduction and
formalization, not a novelty claim.

## Fresh check and resource receipt

Working directory: `research/partitions/mathlib`. Command:

```sh
~/.elan/bin/lake env lean PartitionH3/ElementaryProduct.lean \
  -o /Users/christopheryamba/YambaCode/autodidactic-traveler/.runs/h3-p010-r1/ElementaryProduct.olean
```

The real run exited 0 in 3.760 seconds, with no warnings or errors; source
hashes before and after were the frozen hash above. It emitted a fresh
712144-byte `.olean`. Lean was `leanprover/lean4:v4.34.1`; manifest SHA-256 was
`519bb42602944b5e01f310ecde293c7679e00eb50ad218be6e063048656e020c`.
All eight printed axiom reports contain only
`[propext, Classical.choice, Quot.sound]`, including the main theorem and
both boundary corollaries. Output SHA-256:
`86cca51d8efa2e0ba44778d7098ce4dbd35a70c1afd5a3b08046b9f3ee5b6193`.
The complete local output and machine receipt are in ignored
`.runs/h3-p010-r1/elementary-fresh.log` and `elementary-receipt.json`.
Free storage before/after this check was 20520960000 bytes. This is a proof
check receipt, not a benchmark of the mathematical research process.

## Candidate 2: actual finite-support reconstruction (frozen)

Source: `research/partitions/mathlib/PartitionH3/Reconstruction.lean`.
SHA-256:
`7162200879dbc87ffac85c61aedcbd1a723d52a64c3810d6a22ed07b672da59f`.

```lean
def IsAlternating {m : ℕ} (p : Poly m) : Prop :=
  ∀ sigma : Equiv.Perm (Fin m),
    MvPolynomial.rename sigma p = signCoeff sigma * p

theorem alternating_eq_of_dominant_coeff {m : ℕ} (p q : Poly m)
    (hp : IsAlternating p) (hq : IsAlternating q)
    (hc : ∀ gamma : Fin m → ℕ, StrictAnti gamma →
      p.coeff (powerExponent gamma) = q.coeff (powerExponent gamma)) : p = q

theorem alternating_reconstruction {m : ℕ} (p : Poly m)
    (hp : IsAlternating p) :
    p = ∑ e ∈ dominantSupport p,
      MvPolynomial.C (p.coeff e) * alternant (fun i => e i)
```

`dominantSupport p` filters the actual finite monomial support `p.support`
by `StrictAnti (fun i => e i)`. The input is an actual polynomial; there is
no separate finite-support premise, guessed support set or assumed desired
expansion. All exponents are natural, and no homogeneity, lower positive
degree, nonempty alphabet, degree bound or positivity premise occurs.
In particular `m=0` is included. Omitting alternation fails already for
`m=2,p=1`: its support exponent is constant, so the displayed sum is zero.

The proof first reindexes the genuine signed permutation sum to show that
each alternant is alternating. Coefficients transform by the actual
permutation sign (`alternating_coefficient_perm`). Repeated entries force
a coefficient to equal its negative by the corresponding transposition;
coefficientwise torsion-freeness over integer polynomials makes it zero.
When entries are distinct, the local pinned `Tuple.sort` on the dual natural
order gives a permutation to a strictly decreasing vector, which determines
every coefficient from a dominant one. For two strictly decreasing vectors,
the antitone uniqueness theorem shows they can be permutations of one
another only when equal. Hence an alternant has dominant coefficient one
at its own exponent and zero at every other decreasing exponent.
Multiplying by `C (p.coeff e)` and summing over `dominantSupport p` produces
an alternating polynomial with precisely the dominant coefficients of `p`;
extensionality proves reconstruction.

The public bridge `vandermonde_mul_isAlternating p hp` proves alternation of
`vandermonde m * p` from actual `MvPolynomial.IsSymmetric p`. No coloring
symmetry is assumed by an unconditional coloring theorem here.

One existing pinned Mathlib source module, `Mathlib.Data.Fin.Tuple.Sort`, was
compiled locally after confirming all five imported compiled dependencies
were already installed; no dependency was fetched. Its inspected source
SHA-256 is
`9075b412b4e447c4a01590aceaf0f05d4cf58c419192eb016e9171241a753567`.
The exact local command was:

```sh
~/.elan/bin/lake env lean .lake/packages/mathlib/Mathlib/Data/Fin/Tuple/Sort.lean \
  -o .lake/packages/mathlib/.lake/build/lib/lean/Mathlib/Data/Fin/Tuple/Sort.olean
```

It exited 0. The fresh reconstruction source check was:

```sh
~/.elan/bin/lake env lean PartitionH3/Reconstruction.lean \
  -o /Users/christopheryamba/YambaCode/autodidactic-traveler/.runs/h3-p010-r1/Reconstruction.olean
```

This real run exited 0 in 3.261 seconds, with no warnings or errors; source
hashes before and after matched the frozen hash above. It emitted a fresh
338512-byte `.olean`. All ten printed axiom reports contain only
`[propext, Classical.choice, Quot.sound]`. Output SHA-256:
`dceaf81f053a38f07907f04aa8933271cd0e0dad08c6981f5401fb1a0cd307ef`.
The complete output and machine receipt are in ignored
`.runs/h3-p010-r1/reconstruction-fresh.log` and
`reconstruction-receipt.json`. Free storage before/after this source check
was 20520960000 bytes. The Lean version and manifest hash match candidate 1.
Neither source contains a placeholder, custom axiom or unchecked evaluator.

After both direct checks, the actual project command
`lake --no-cache build PartitionH3.ElementaryProduct PartitionH3.Reconstruction`
also exited zero (`Build completed successfully (1334 jobs)`). It built the
existing local Sort module (1.8 seconds) and the two new project modules
(2.6 and 2.1 seconds), replaying existing dependency products. No shared root
import or configuration was edited. This project build emitted the same
eight plus ten standard-only axiom reports.

Integration still needs actual coloring symmetry, the coloring/array
coefficient bijection, finite signed involution cancellation, canonical
padding removal, identification of the relevant dominant exponents with the
two-column survivor shapes, and assembly with the full survivor families.
No unconditional H3 conclusion is claimed. Root owns
those sources and verification configuration. This file changes no previously
reviewed source, project configuration, article or shared root import.
