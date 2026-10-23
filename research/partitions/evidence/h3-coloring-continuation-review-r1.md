# P011 round 1: adjacent-color construction

Reviewed 2026-10-23 by `/root/h3_semantic_critic`, separately from author
`/root`. This is the first P011 challenge, not another P008 signed-array
review. Distinct roles do not imply independent errors or different models.
No Lean proof source was edited or new proof certificate claimed.

**Verdict: supported as a written construction; incomplete as a Lean
polynomial proof.** No counterexample was found under the exact properness,
height-two, natural-unit-interval and adjacent-color hypotheses.

Reviewed snapshots:

- `../h3-continuation-20261023.md`, SHA-256
  `de67f9f12ee1b8e7af0943666f81e98d5719425fe73ce4d5a2976c94339189cb`.
- `../mathlib/PartitionH3/Coloring.lean`, SHA-256
  `dc415218fa4d625d96a711469d11aadf016437a6dd1a79c7337e21422dc12235`.

The review inspected the written rule and existing exact coloring definitions
and preliminaries. It did not review the new `ColorSymmetry.lean`, execute a
new Lean check, or infer a universal theorem from finite experiments.

## Findings

1. **The one-/two-edge dichotomy and isolated-vertex choice are sound.**
   Properness and the existing class-size bound reduce positive unequal
   sizes to `1,2`. Write the double class as the chain `u <_P v`, and the
   singleton as `z`. The endpoints have no graph edge. If `z` had no edge
   to either endpoint, it would be comparable with both; their natural
   label order then supplies a strict three-chain, contradicting height
   two. Thus there are exactly one or two induced edges. In the one-edge
   case the isolated vertex is the other double-class endpoint, never `z`.
   Changing only that vertex exchanges multiplicities and creates no
   equal-colored internal edge.

2. **The path-case ascent argument uses monotonicity essentially.**
   With both edges present, `z<u` would imply
   `h(z)<=h(u)<v`, contradicting the `z,v` edge. Likewise `v<z` implies
   `h(u)<v<z`, contradicting the `u,z` edge. Hence `u<z<v` in labels.
   The two edges contribute exactly one ascent for either assignment of
   the two colors. A smallest regression against dropping monotonicity
   has three vertices and the extensive but nonmonotone zero-based
   `h=(2,1,2)`: the comparable pair `(1,2)` and singleton `0` give a
   two-edge path, but swapping their two colors changes ascents from zero
   to two. This refutes the weakened hypothesis, not the stated rule.

3. **Outside comparisons, properness and involutivity are sound.** Every
   outside color is below both adjacent colors or above both, so changing
   an endpoint within that pair preserves its comparison and inequality
   with an outside endpoint. Equal multiplicities remain in the identity
   branch. In every other branch the counts exchange, the same support
   `U` remains, and its induced graph is unchanged; the isolated vertex is
   consequently the same on reapplication. Both the empty-class swap and
   the path swap also repeat the same branch. Empty support is covered by
   the equal-size branch. Adjacency cannot be omitted: for a single edge
   with colors `(0,1)` in a three-color alphabet, swapping colors `0,2`
   changes its ascent count from one to zero.

4. **Monomial reindexing needs an aggregate proof.** The required equality
   is `colorMonomial (F κ) = rename (swap a b) (colorMonomial κ)`.
   It follows from exchanging the two multiplicities and preserving all
   other multiplicities. It is not a pointwise identity of colorings:
   when the two counts agree, the proposed map deliberately fixes `κ`.
   The same issue occurs in the isolated-vertex branch. Reindex the finite
   sum by an equivalence of the subtype of proper colorings, or explicitly
   account for improper summands being zero. Then use ascent preservation
   and the actual monomial equality. No coloring expansion may be assumed.

5. **The remaining Lean scope is substantive and well specified.** No
   adjacent-color symmetry theorem follows solely from the existing
   reversal and cardinality lemmas. Generation by adjacent swaps must use
   valid adjacent `Fin m` colors; `m=0,1` have no such generator and still
   require the eventual all-permutation result. The empty vertex case
   follows the identity branch. The actual coloring/list-array coefficient
   bijection and survivor equality remain separate H3 obligations.

## Narrow helper interfaces

- Use symmetric adjacency `Adj H i j := Edge H i j ∨ Edge H j i` in the
  structural dichotomy. Prove the isolated vertex belongs to the double
  class and its uniqueness inside the actual support `U`.
- Prove `PosetLt H u v → Adj H u z → Adj H z v → u<z ∧ z<v` for distinct
  vertices. Height is unnecessary for this middle-label helper;
  monotonicity and extensiveness are the relevant structural assumptions.
- For `b.val=a.val+1` and `c≠a,b`, prove comparison invariance of either
  `a` or `b` against `c`. Use this for the outside-edge contribution.
- For proper `κ`, expose preservation of support/outside colors, exchanged
  class cardinalities, properness, equal ascent degree, involutivity, and
  the actual monomial-renaming equality as separate checked statements.
  These suffice to construct the proper-coloring equivalence and then
  `rename (swap a b) (chromatic H m) = chromatic H m`.

P011 accounting for this proposal/challenge is **5 of 16** declared proxy
units: 3 author units and 2 review units. This is manual collaboration;
units are neither tokens nor money. The historical P007/P008 accounts remain
frozen. This record claims neither H3 completion nor novelty.
