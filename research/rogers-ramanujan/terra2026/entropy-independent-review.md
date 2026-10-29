# Independent review: bounded-digit obstruction and block reduction

## Entropy obstruction

**Verdict: supported by a universal counting argument, subject to the independently checked seven-block encoding.** Novelty is unverified; neither weight preservation nor a full KR1 bijection is assumed or established. The bounded-multiplicity product subset is a restriction, not a normalization of arbitrary product partitions.

Let B_L be the product-side partitions supported on parts `9k+1, 9k+3, 9k+6, 9k+8`, `0≤k<L`, with respective multiplicity ranges `0..7, 0..1, 0..1, 0..7`. Multiplicities are independent, and distinct multiplicity vectors are distinct partitions, so `|B_L|=256^L` and every input maximum is at most `9L` (indeed at most `9L-1`).

For every nonnegative integer M let G(M) be gap partitions with all parts at most M, including the empty partition. Put `t=ceil(M/9)`. These partitions inject into valid length-`3t` block words by recording the pattern in each interval `{3j+1,3j+2,3j+3}` and padding all unused higher blocks by E. The word uniquely recovers the partition. Writing columns of the matrix A by successor state and rows by current state, starting in E gives exactly `(A^(3t) 1)_E` walks, because E allows all seven first letters. The final state needs no restriction, and padding with E is always permitted. At M=0 the unique length-zero word is also correct.

The stated witness has positive coordinates and `A³v≤159v`. The smallest coordinate of v is 3473, so `1≤v/3473` componentwise. A has nonnegative entries; induction gives

`|G(M)| ≤ (A^(3t)1)_E ≤ (10000/3473) 159^t`.

For an injective f with `max f(λ)≤α max λ+C`, assume first α≥0. For all λ∈B_L, the output maximum is at most `9αL+C`, even if this bound is not an integer. If it is negative for some L, a nonempty source set has no possible image, already contradicting the assumption. Otherwise let `M_L=floor(9αL+C)`. The injection and bound give

`256^L ≤ |G(M_L)| ≤ (10000/3473) 159^(ceil(M_L/9)) ≤ (10000/3473) 159^(αL+C/9+1)`.

When `α<log(256)/log(159)`, the ratio `(256/159^α)^L` grows without bound, contradicting the last inequality for sufficiently large L. If α<0, use inputs containing the part `9L-1`: their maxima tend to infinity and the claimed upper bound on the nonnegative output maximum eventually becomes negative. This covers arbitrary finite real α,C, including negative C and floor endpoints. Numerically, the threshold is approximately 1.0939598033931512. A larger additive constant or finitely many exceptional inputs cannot remove the exponential contradiction; equality at the threshold is not ruled out by this argument.

`lean/Entropy.lean` checks a direct finite-state operator corresponding to the row/successor table, the componentwise witness, and `walks n s≤159^n v s` for all natural n and all seven states, by induction and monotonicity. Its root corollary uses the weaker constant 10000 because it begins with `1≤v`; this does not change the obstruction. The file does not define gap partitions or formally link them to words, encode B_L, or establish the real logarithm limit. These steps are the hand argument above. Run with:

```
/tmp/lean-4.34.0-linux/bin/lean research/rogers-ramanujan/terra2026/lean/Entropy.lean
```

Compiler Lean 4.34.0, successful exit 0, one unused simp-argument warning. A first draft's stronger root inequality failed because it did not propagate the factor 3473; the final root corollary correctly uses 10000. Axiom report: `witness` no axioms; `walks_bound` and `root_bound` each `[propext, Quot.sound]`; no `sorryAx`. Final source SHA-256 `9cc8fee5dfe19b425756d9f9dbdd006a66203e1c9cc5381963408e53973c763a`.

## Height-block reduction

**Verdict: supported with a specific correction to the exposition.** For nonempty blocks the two displayed conditions `p(M_0)≤3` and `s(M_k)+p(M_{k+1})≤3` are necessary and sufficient for the positive heights to start by 4 and have successive gaps at most 4. A missing four-run within a five-block must touch its start or end: if it is a prefix, the first-block or previous boundary condition excludes it; if it is a suffix in a non-final block, the next boundary condition excludes it. Trailing zeros in the final block lie beyond the maximum and are not constrained. Conversely, a forbidden gap between successive occupied heights cannot skip an entire nonempty block, so is caught by the initial or boundary inequalities. The multiplicity and weight formulas reconstruct uniquely, and the cluster increment coordinates and their inverse telescope correctly.

**Concrete correction:** the sentence saying the internal rule “excludes masks {1}, {5} and also mask {3}” is false as written. The immediately following parenthetical correctly says mask `{3}` has no four consecutive zeros and is allowed. For example the one-block word `(0,0,1,0,0)` represents the valid one-height object with height 3; neither the initial nor boundary rule excludes it. Remove “and also mask {3}”; retain the stated allowance for `{3}`. Furthermore `{1}` is allowed in a final block, as the subsequent refined paragraph correctly explains. This is an exposition inconsistency, not a counterexample to the displayed boundary characterization or transfer series.

Reviewed source digests at time of review: theory `75e226953470110e5c34c47e7d049ea52b16e806191fa292548166bf365245f3`; block-reduction `9acd7062f3a0d64d181054003ebaa48530491ed1ef44e6b6080cb48c2028ecf2`. Authors may subsequently edit those drafts; review applies to these exact hashes.
