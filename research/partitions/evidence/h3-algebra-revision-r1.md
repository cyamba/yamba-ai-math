# P007 author revision: actual polynomial bridge ingredients

2026-10-22. Author profile: `/root/h3_lean_algebra`, continued by lead `/root`
after the worker reached an account usage limit. This is the same bounded
round-1 revision, not a successful autonomous worker run or a new dispatch.
Its 3 units bring the P007 manual account from 8 to **11 of 16** proxy units.
The failed initial specialist attempt remains charged. These units are not
tokens or money.

## Checked sources and actual execution

The separate `../mathlib/` project is pinned to Lean 4.34.1 and Mathlib
`d13f23b723b8a846827a245b89c10fc7d3f11612`. The original Std project remains
pinned to 4.34.0; its new verification record passes 54 dependency reports.

`../mathlib/verify.py --output ../mathlib/verification.json` completed a
fresh temporary project build, five direct source checks and an exact
statement inventory, with **28 principal dependency reports**. Only pinned
dependency products were reused. No project proof products were reused.
All dependency reports contain only `propext`, `Quot.sound` and
`Classical.choice`; there were no diagnostics, proof placeholders or custom
axioms. Exact source/configuration hashes and Git dependency revisions are
in [the source-bound record](../mathlib/verification.json).

The recorded fresh build took 19.862 seconds; each direct bridge source
check took 2.660–3.330 seconds. These are observed execution times, not
estimates of future proof work.

## Exact completed interfaces

All polynomials below live in `Poly m = MvPolynomial (Fin m) (Polynomial Int)`.
Definitions use actual functions and finite sums, rather than a desired
positive witness.

- `chromatic H m`: sum over all actual proper `Fin n -> Fin m` colorings,
  with `q^ascents` and their actual color monomials.
- `elementary m b`: Mathlib's subset-defined `esymm`.
- `tableauCoefficient` and `survivorCoefficient`: actual weighted sums of
  the original complete `CornerSlide.columnFamily` and full-image complement
  `CornerSlide.survivorFamily`, using `List.range n` and extension of the
  finite poset relation by false outside these vertices. No equality with
  `chromatic` is assumed or asserted.
- `alternant gamma`: the signed sum over actual `Equiv.Perm (Fin m)` of
  `product_i X_(sigma i)^(gamma i)`. `alternant_eq_sum` prints this equality.
- `alternant_mul_elementary`: for every `m,gamma,b`, with no bound on `b`,

  ```text
  A(gamma) * e_b = sum_(T subset Fin m, card T=b) A(gamma + 1_T).
  ```

  It proves symmetry of the actual elementary polynomial, distributes its
  actual subset sum and the actual permutation sum. Thus inverse-variable
  reindexing is encapsulated by the checked `rename` action and symmetry.
- `alternant_eq_zero_of_eq`: distinct positions with equal exponents give
  zero. Right composition by the actual transposition changes the sign.
  The final step uses that `2` is nonzero in the stated polynomial domain;
  this is proved by taking the constant coefficient twice. No claim for
  arbitrary rings with 2-torsion is made.
- `vandermonde_delta_coefficient`: the coefficient at the actual finitely
  supported vector `delta_i=m-1-i` is exactly one. The proof proves
  injectivity of `delta` on `Fin m` and that only the identity permutation
  contributes. `vandermonde_ne_zero`, `vandermonde_cancel` and
  `vandermonde_empty` give valid polynomial cancellation and the `m=0` case.
- `twoBlockSubset_classification`: the previous Std bit classification now
  transfers bijectively to **actual subsets of `Fin m`**, with actual
  cardinality and unique `0<=j<=b`, under `b<=a` and `a+b<=m`.
- Actual coloring preliminaries prove that every color class is a chain
  and has at most two vertices under height two; reversing all colors is
  involutive, preserves properness, and interchanges ascents and descents.
  `descents_eq_colorRowInversions` counts actual incomparable vertex pairs
  in increasing color rows, corresponding to descending colors on ordered
  vertex pairs. It does not identify this finite-pair statistic
  with the original list-array statistic.

## Remaining obligations and verdict requested

**H3 is incomplete. P007 is incomplete as a whole.** Request separate review
of the precise completed interfaces above. The generic alternant-product
acceptance gate now has a source-checked declaration. The reviewed written
two-elementary-product identity still lacks a complete Lean derivation:
the bit/subset bijection is supplied, but its no-rise condition must still
be connected to the actual bumped natural exponents and the polynomial sum
reduced to the surviving `j` indices.

Polynomial reconstruction from dominant alternating coefficients is also
absent. For P008, adjacent-color symmetry, actual coloring/list-array
bijections, complete signed-sector finite-sum cancellation, permutation-sign
translation and the full padding/family bijection remain absent. P009 has
not begun: its checked compatible P007/P008 prerequisites are incomplete.
No new signed-array review round is requested; its two rounds remain frozen.

The mathematical source route remains Shareshian–Wachs, Sections 4 and 6,
and the attributed Cho–Huh injection. The formal ingredients are not a new
solution of the general positivity conjecture and do not establish novelty.

## Local provisioning record

Lean itself and the original Std proof needed no new library. Optional
Mathlib provisioning began only after more than 20 GiB was free. The first
cache call rejected filesystem paths relative to the bridge directory; the
single diagnosed network retry used module names and downloaded only the
three selected imports and their 1308 transitive files. A disk monitor
measurement raced with temporary cache files; it lost that cache process's
exit receipt. Its log records full extraction, and the subsequent actual
project build and fresh certificate checks passed. The failure is retained
in `.runs/h3-mathlib/provision.json`, with recovery in `recovery.json`.

The conservative elapsed upper bound for the initial setup/build was
281.076 seconds, below the 3600-second limit. Added allocated storage at
that observation was 5,110,640,640 bytes, below 15 GiB, with
18,841,600,000 bytes free, above the 5 GiB stop. No third network attempt,
full-Mathlib cache, user-file deletion or TeX installation was used.
