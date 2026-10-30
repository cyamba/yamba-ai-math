# Goldbach elementary Lean certificates

`GoldbachElementary.lean` is a self-contained Lean 4.19.0/Std proof file. It has no Mathlib dependency. It does not prove the Goldbach conjecture or any of the asymptotic results discussed in the research program.

## Checked results

* `no_adjacent_common_summand`: for every natural k≥1, the targets 30k+8 and 30k+10 cannot share a prime summand. `PrimeLike` is the explicit standard divisor characterization: n≥2 and every divisor is 1 or n. The theorem expresses both decompositions with the same summand p and complementary pair q,q+2.
* `prime_pair_symmetry`: reflection swaps the two prime summands of a fixed target.
* `four_cell_identity` and `chen_parity_identity`: integer arithmetic identities behind the four-cell and Chen parity discussions. They do not construct or analyze the corresponding combinatorial sets.
* `trialPrime_sound` and `trialPrime_complete`: the executable finite trial-division test is equivalent to `PrimeLike`.
* `sums30_exact` and `sums30_characterization`: the 30 list is exactly [7, 11, 13, 17, 19, 23], and its entries are precisely the natural summands 0≤p≤30 for which both p and 30−p are prime by the explicit divisor definition.

## Reproduction

Install Lean via `elan` and, from this directory, run:

```sh
lake build
```

The run on 28 October 2026 used the official Lean 4.19.0 release and returned `Build completed successfully`. All named general theorems printed below depend on the standard Lean axioms `propext` and `Quot.sound`; `sums30_exact` reports no axioms. There is no `sorry`, `admit`, or `native_decide` in the source. The source includes `#print axioms` commands for inspection. This is kernel verification of the precise declarations, not human peer review of the surrounding article.

The execution environment used for this run denied access to `/proc/<own-pid>/exe`, so the run used a tiny process-path compatibility shim to redirect that lookup to `/proc/self/exe`; it did not replace Lean, its standard library, or the kernel. This workaround is specific to that container. The source and project files do not depend on it and it should not be needed on a normal installation.
