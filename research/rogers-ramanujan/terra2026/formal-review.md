# Formal supplement and scope audit — 2026-10-27

**Verdict: supported for the stated multiplicity-block equivalence; incomplete for the sorted-partition and KR1 bijection claims.** The supplementary proof is not independent of the formalizer's own definitions and requires semantic review. It does not use the product identity or assert the desired bijection.

## Encoding and semantic boundary

For multiplicities c(k) of a sorted positive partition, the natural candidate equivalence is the following conjunction, for every k ≥ 1:

* c(k)+c(k+1)+c(k+2) ≤ 2;
* c(k) ≥ 2 implies k ≡ 0 (mod 3);
* c(k)>0 and c(k+1)>0 imply k ≡ 1 (mod 3).

Reason: a violation of a three-value window is precisely three parts spanning at most two units; adjacent equal parts require 2k ≡ 0, and the consecutive distinct pair k,k+1 requires 2k+1 ≡ 0. Conversely, any two consecutive parts with difference 0 or 1 are handled by these latter implications, and any distance-two pair with difference ≤2 yields three parts in a length-three window. This is a mathematical argument, not a Lean-checked equivalence to lists: the code does not define sorted lists, count occurrences, finite support, or prove these translations.

The provided seven-letter draft has no counterexample in its local transition table. The Lean file proves an exact equivalence between its table and the blockwise multiplicity restrictions for arbitrary natural-indexed sequences, and proves uniqueness of a realizing letter at each position. It uses counts at indices 3j+1, 3j+2, 3j+3 and never constrains c(0); c(0) is irrelevant to positive partitions. Infinite non-finitely-supported sequences are included, so finiteness and weight have not been verified. The sequence encoder uses classical choice and is an existence theorem, not an executable endpoint. A direct finite decoder/encoder and their weight equations remain to be checked. Local classification and transition proof are case analysis on the seven possible letters, universally quantified over every block and every multiplicity sequence, not a numerical test bounded by weight.

## Reproduction

Official release: `https://github.com/leanprover/lean4/releases/download/v4.34.0/lean-4.34.0-linux.tar.zst`, downloaded to `/tmp`; archive SHA-256 `caaa98356098c85dc0fcbbd28e1ec66f39eb6551829972b752ff20e1286b646b`. This is a recorded digest, not a separately verified upstream signature. Compiler reports `Lean (version 4.34.0, x86_64-unknown-linux-gnu, commit 293d5d0c0c3f3dded4688b3ccd6a33939ac5102b, Release)`.

Extraction first failed with ownership warnings; `tar --no-same-owner --zstd -xf /tmp/lean-4.34.0-linux.tar.zst -C /tmp` succeeded. Running in the ordinary sandbox returned `error: failed to locate application`; running outside it succeeded. From the worktree root, the successful command was:

```
/tmp/lean-4.34.0-linux/bin/lean research/rogers-ramanujan/terra2026/lean/Blocks.lean
```

Exit 0; three linter warnings about unused bindings/simp argument. An earlier draft returned exit 1 (unfinished case proof and decidability), and an intermediate draft returned exit 1 (unsupported `convert` tactic); both were repaired before the successful check. Source SHA-256 `230ad08890236797de73c7e1634aebc55e7e7c1a8a7491f4c9db8d109cb01cdc`.

## Theorems and axioms

* `block_classification`: for arbitrary natural a, b, c, `BlockValid a b c ↔ ∃ p, counts p = (a,b,c)`.
* `transition_table` and `adjacent_blocks`: all 49 pairs are handled in a kernel-checked proof of equivalence with the exact boundary constraints / four local windows.
* `counts_injective`: `Function.Injective counts`.
* `sequence_encode`: `SequenceValid c → ∃ w, Realizes c w ∧ ∀ j, Compatible (w j) (w (j+1))`.
* `sequence_decode`: converse given `Realizes c w` and compatibility for all j.
* `realization_unique`: two realizations of the same sequence are equal.

Lean's `#print axioms` reports: `block_classification`, `sequence_encode`, and `sequence_decode`: `[propext, Classical.choice, Quot.sound]`; `transition_table`, `adjacent_blocks`, and `realization_unique`: `[propext, Quot.sound]`; `counts_injective`: `[propext]`. No `sorryAx` appeared in the successful run. These are Lean standard axioms, not a claim of constructive extraction.
