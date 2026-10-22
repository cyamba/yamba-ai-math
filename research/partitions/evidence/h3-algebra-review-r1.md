# P007 round 1: separate finite-alternant review

Reviewed 2026-10-22 by `/root/h3_semantic_critic`; the lead `/root` authored
the proposal. This is P007's first substantive algebra challenge, separate
from P008's completed signed-array reviews. No proof source was edited.

**Verdict: incomplete for the polynomial Lean target; supported as a written
finite algebra argument and as the exact checked Boolean ingredient.** No
mathematical counterexample or actionable defect was found in the proposed
identity under its stated hypotheses. This does not complete P007 or H3.

Reviewed inputs:

- [h3-algebra-r1.md](h3-algebra-r1.md).
- `../lean/AlternantSubsets.lean`, SHA-256
  `32748cec117cbe8d97cfac47ca93079ef79271abf71ddc9a8410e3c1d0b7055b`.

The critic independently ran `lake env lean AlternantSubsets.lean` with the
existing Lean 4.34.0 toolchain. It exited zero without diagnostics, printing
the three requested exact declaration types and seven dependency reports.
Dependencies were only `propext`, `Quot.sound`, and, for
`adjacent_exponent_collision`, `Classical.choice`. The source hash was
unchanged afterward. This was a direct check, not a second fresh-copy build.
No dependency was provisioned and no numerical check was used as proof.

## Exact target

In `Z[q][x_0,...,x_(m-1)]`, for natural `a,b,m` satisfying `b <= a` and
`a+b <= m`, with

```text
A(gamma) = sum_(sigma in S_m) sign(sigma) product_(i<m) x_(sigma(i))^(gamma_i),
delta_i = m-1-i,
lambda(j) = (2^j,1^(a+b-2j),0^(m-a-b+j)),
```

prove the actual polynomial identity

```text
A(delta) * e_a * e_b = sum_(j=0..b) A(delta + lambda(j)).
```

Here `j=0..b` includes both endpoints; each exponent vector has length `m`.

## Findings

1. **Supported: permutation orientation and sign pairing.** With the stated
   action on variables, `S = sigma(T)` gives the product with exponent
   `gamma_i + 1_T(i)` at `x_(sigma(i))`. For repeated exponents at distinct
   `p,q`, the correct partner is `sigma` composed on the right with `(p q)`.
   That partner has the same monomial and opposite sign, and interchanges
   `sigma(p)<sigma(q)` with its complement. The written argument therefore
   cancels actual disjoint pairs without division or a torsion assumption.
   These finite-sum and permutation facts are not yet formalized here.

2. **Supported: exact surviving-index classification and boundaries.** An
   adjacent false/true rise creates an exponent collision except at the cut
   `a`, where the exponent difference is at least one. No-rise bits form
   prefixes in each block. Their counts are uniquely `j` and `b-j`.
   `0<=j<=b<=a` and `b-j<=b<=m-a` make every stated candidate feasible.
   Adding the first-block indicator gives exactly the displayed `lambda(j)`,
   including its `m-a-b+j` zeros. For `m=0`, the hypotheses force `a=b=j=0`
   and both polynomial sides are one. No missing endpoint or extra
   multiplicity was found.

3. **Blocking for formal integration: the checked objects are Boolean
   lists and integer expressions.** `noRise_iff_prefix` classifies any
   finite Boolean list by its actual `ones` count;
   `two_block_classification` gives the stated unique `j` under the exact
   length/cardinality bounds. `candidate_length`, `candidate_ones` and
   `candidate_injective` have the needed feasibility and uniqueness scope.
   Integration still needs the bijection to actual subsets of `Fin m`,
   correspondence with subset cardinality, and the bounded-index conversion
   from integer `exponent` to the natural monomial exponent. The source
   deliberately allows integer indices outside the polynomial range; its
   collision theorem alone does not establish that conversion.

4. **Blocking for the requested polynomial certificate: no polynomial
   theorem is present.** The source does not define `A`, `Delta`, `e_a`,
   coefficient extraction, or polynomial finite sums. Thus the checked bit
   classification cannot be reported as a kernel-checked alternant identity.
   The missing work is to instantiate the actual reindexing and sign pairing
   in item 1, transfer item 2 through item 3, and distribute the finite
   polynomial sums. The proposal accurately records this boundary.

5. **Supported in writing, unformalized: nonzero Delta and cancellation.**
   In the coefficient of `x^delta`, distinct entries of `delta` force the
   contributing permutation to be the identity, with coefficient one;
   this also applies to the empty vector. Hence `Delta` is nonzero.
   Multiplication by it cancels over the stated integral-domain polynomial
   ring. Neither the coefficient computation nor the ring cancellation has
   a certificate in this source, so neither may yet be used as a checked H3
   bridge dependency.

The narrow supported result is the checked two-block Boolean classification
plus the separately reviewed written finite-alternant proof. The decisive
next algebra check is an actual polynomial declaration implementing the
generic identity `A(gamma)*e_b = sum_(|T|=b) A(gamma+1_T)` and the explicit
repeated-exponent pairing. Coloring symmetry, the coloring coefficient
bridge, and the final survivor formula remain outside this review.

## Manual accounting

The reported P007 account before this challenge was 6 of 16 declared proxy
units, including the failed specialist attempt. This challenge adds 2, for
8 of 16. These units are not tokens or money. This is manual collaboration,
not a harness provider execution. No second P007 review round is claimed by
this record.
