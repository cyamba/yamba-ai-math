# P007: finite alternant identity, first proposal

2026-10-22. **Written proof, separate review pending.** The polynomial identity
below has no Lean certificate yet. Its subset-classification ingredient is
kernel-checked with the installed Lean 4.34.0 and Std, without new dependencies.
This is algebra for the known height-two argument, not a novelty claim.

## Exact objects and statement

Work in `Z[q][x_0,...,x_(m-1)]`. For `gamma` in `N^m`, define the actual
signed monomial alternant

```text
A(gamma) = sum_(sigma in S_m) sign(sigma) product_(i<m) x_(sigma(i))^(gamma_i).
e_b = sum_(S subset {0,...,m-1}, |S|=b) product_(i in S) x_i.
delta_i = m-1-i;  Delta = A(delta).
lambda(j) = (2^j,1^(a+b-2j),0^(m-a-b+j)).
```

All exponent vectors in this statement are natural valued. Assume `b <= a`
and `a+b <= m`. The target is

```text
Delta * e_a * e_b = sum_(j=0..b) A(delta + lambda(j)).
```

For `m=0`, the hypotheses force `a=b=0`. The empty permutation, empty
product, and empty subset give both sides equal to one.

## Complete finite written argument

1. For any natural exponent vector `gamma`, distribute the finite sums in
   `A(gamma)*e_b`. For each permutation `sigma`, reindex the size-b subsets
   by `S = sigma(T)`. This is a bijection. The resulting product is precisely
   `product_i x_(sigma(i))^(gamma_i + 1_T(i))`. Thus
   `A(gamma)*e_b = sum_(|T|=b) A(gamma+1_T)`.
2. If `gamma_p=gamma_q` for distinct indices, pair every permutation `sigma`
   with `sigma` composed on the right with the transposition `(p q)`.
   The monomials agree and signs are opposite. The pairs are disjoint:
   partition permutations by `sigma(p)<sigma(q)` and its complementary
   inequality. This proves `A(gamma)=0` without division or an inference
   from `A=-A` in an arbitrary coefficient ring.
3. In `delta+1_T`, an adjacent 0-to-1 rise of the membership bits creates
   equal neighboring exponents. Every bit string without such a rise is
   a string of true bits followed by false bits. Its cardinality forces
   `T={0,...,a-1}` when multiplying by `e_a`. All other terms vanish by
   step 2. Hence `Delta*e_a=A(delta+1_[0,a))`.
4. Multiply the last equality by `e_b` and use step 1. In
   `delta+1_[0,a)+1_T`, the neighboring exponents collide exactly at a
   0-to-1 rise away from the cut `a`. At the cut their difference is at
   least one. Consequently every surviving subset is a prefix separately
   in `[0,a)` and `[a,m)`. Write their sizes as `j` and `b-j`.
5. Every `j=0,...,b` occurs exactly once: `j<=b<=a`, and
   `b-j<=b<=m-a`. The bit string is exactly
   `true^j false^(a-j) true^(b-j) false^(m-a-(b-j))`.
   Adding its indicators to `1_[0,a)` gives `lambda(j)`. This proves the
   displayed identity. Noncanonical subsets have already vanished by an
   actual sign cancellation, not by discarding terms of unknown sign.

Also, the coefficient of `x^delta` in `Delta` is one. The entries of `delta`
are distinct, so only the identity permutation contributes to that monomial.
For `m=0` the same statement concerns the constant monomial. Therefore
`Delta` is nonzero. Cancellation by `Delta` is valid in the polynomial ring
over the integral domain `Z[q]`. These facts still require a polynomial Lean
certificate; the combinatorial module does not provide it.

## Checked ingredient and boundary

`../lean/AlternantSubsets.lean`, SHA-256
`32748cec117cbe8d97cfac47ca93079ef79271abf71ddc9a8410e3c1d0b7055b`.

- `noRise_iff_prefix`: exact prefix classification for arbitrary finite
  Boolean lists, with the prefix length equal to their actual number of ones.
- `adjacent_exponent_collision`: for integer exponents
  `m-1-i + 1_(i<a) + 1_bit`, equality of adjacent exponents occurs exactly
  at a false/true rise away from the cut. This identity holds even outside
  the finite range; polynomial use is restricted to `i<m`, where the
  exponents in this argument are nonnegative.
- `two_block_classification`: for every length-m list with exactly b ones,
  under `b<=a` and `a+b<=m`, the two no-rise conditions are equivalent to
  the existence of a **unique** `j<=b` with the explicit bit string above.
- `candidate_length`, `candidate_ones`, `candidate_injective`: every index
  in the stated range is feasible and gives a different actual subset.

Fresh author check: copied the source and pinned toolchain file into an empty
temporary directory and ran `lean -o AlternantSubsets.olean
AlternantSubsets.lean`. Exit zero; no diagnostics or `sorryAx`; all seven
printed reports use standard `propext`, `Quot.sound` and, for one statement,
`Classical.choice`. The source hash was unchanged. Elapsed process time
6.267 seconds; temporary files 585,033 bytes; no dependency installation.
The ignored receipt is `.runs/h3-alternant-subsets-r1/receipt.json`.

The module does **not** prove a finite subset/Finset equivalence, the
permutation reindexing, polynomial multiplication or sign cancellation,
the coefficient of the Vandermonde, or polynomial cancellation. It also
does not prove any coloring expansion. P007 and H3 remain incomplete.

## Manual dispatch accounting

This is a manual collaboration under the existing P007 contract, not an
executed harness provider run. The initial specialist proposal attempt
failed at the account usage limit (3 declared proxy units, counted as a
failure). The lead then supplied this author proposal (3 units). A critic
dispatch is separate and has not yet succeeded. The two-round, 16-unit
ceiling is unchanged; dispatch units measure neither tokens nor money.
