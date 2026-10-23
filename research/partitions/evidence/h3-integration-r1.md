# P009 integration candidate, round 1

Status: direct Lean checks passed; clean combined build and separate semantic review pending.
No new mathematical novelty is claimed. The height-two theorem and survivor construction are established Cho–Huh results; finite coloring symmetry and alternant extraction follow the Shareshian–Wachs route.

The final declaration is `PartitionH3.height_two_survivor_expansion`: for arbitrary n, natural unit interval H, HeightTwo H, and every r (including zero), the actual ascent-weighted proper-coloring polynomial equals the elementary expansion with the original complete survivor coefficients. No expansion premise, custom axiom or positivity witness is supplied. Its direct axiom report is [propext, Classical.choice, Quot.sound].

The bridge constructs sorted actual color classes and the inverse coloring from unique row membership, translates the actual list permutation sign, and proves original list inversions equal descents. It sums the original involution over a complete finite array universe, identifies all fixed arrays with the complete tableau family with canonical zero padding, classifies the surviving partitions, reconstructs the alternating polynomial, lifts H2 and telescopes, cancels the nonzero Vandermonde, and specializes from max(n,r) by setting extra variables to zero.

The specialist dispatch wrote the sign/array candidate but ended with a usage-limit error. This failed dispatch remains counted. Root corrected and directly checked the retained source. P009 currently uses 6/16 proxy units, no reviews. There are no nested agents or provider harness runs.

Sources frozen for review:

```json
{
  "research/partitions/mathlib/PartitionH3/PermutationSign.lean": "ba1fa025a7aad3463491e1b4a08c69964cbfc95aff5a9d08ecf5616f4a069a7c",
  "research/partitions/mathlib/PartitionH3/ArrayColorBridge.lean": "bfebc6af39a6dbb4143f4621547262778c57f61a7af9b921e7375dbc44a39f34",
  "research/partitions/mathlib/PartitionH3/FamilyPadding.lean": "161e68118d5e3770d6b9a60e61213c796972027db749bce18e32c2100c4e60fb",
  "research/partitions/mathlib/PartitionH3/FamilyReindex.lean": "ddece994fc969905a3740d1a633186d927d7a833151b14f4d77049d6807d16d7",
  "research/partitions/mathlib/PartitionH3/SurvivorAlgebra.lean": "686ee1886a1d0432f6effd7d3103f97e4834c81407a605c723ba40592e73f27e",
  "research/partitions/mathlib/PartitionH3/DominantShape.lean": "8f81190b0937831eb47574d7d95dcc419e388804b52d7b0b81e2a02a7e9bdd62",
  "research/partitions/mathlib/PartitionH3/ChromaticArrays.lean": "b9e364b07c43c0a1d59c680e09fb442b35d52ea651b086d68395fb2d1707bf80",
  "research/partitions/mathlib/PartitionH3/FiniteH3.lean": "00a70cca54ed12927c227fedec97749ef59e06b0c3093c262ae49d4d6edfed91",
  "research/partitions/mathlib/PartitionH3/AlphabetSpecialization.lean": "d02a5715c43282624a64801bd80724c3bbabd2fc4f231c2ed58feeeb16e5cee9",
  "research/partitions/mathlib/PartitionH3/H3.lean": "c9ba9bc8ae3ce300648594278a63f56aadb6af349ea9ba659a0a8b2e11cef7c1"
}
```

Resource policy: reuse installed pinned dependencies; no new provisioning or user-file deletion. The original Lean 4.34.0 Std certificate is unchanged; the bridge uses Lean 4.34.1 and the accepted Mathlib revision. Review should check semantic definitions, complete families, orientation, labels/sign, empty/balanced/padded shapes, and the actual all-alphabet signature.
