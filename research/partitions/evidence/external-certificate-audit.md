# External general certificate: pinned inventory, unverified build

Inspected 2026-10-21. **Status: partial source inspection; no external build
attempted.** This is A1's feasibility and statement inventory. A1's full rebuild
and A2's decisive proof audit remain incomplete. Nothing here is a refutation.

## Provenance and reproduction

The [official source at the inspected commit](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Combinatorics/Chromatic/Main.lean)
was retrieved through the GitHub connector. Its Git blob
`12abe371e589d0b2ca4548b3c90631afb030aa7f` agrees with the clean local checkout
at `adc7f1241b42e322a6451854ab7e4b4c146bf78a`. The official LICENSE header
identifies Apache 2.0. No external proof source was copied into this project.

[The inventory](external-certificate-inventory.json) pins Lean 4.34.1, mathlib
`d13f23b723b8a846827a245b89c10fc7d3f11612`, eight inspected file hashes and a
deterministic aggregate hash of the lexical import inventory. It traverses 549
local files / 74,575 lines, with `Mathlib` as the external import. This is a
line-based source inventory, not a compiler or semantic dependency audit.

For a clean checkout at that pin, from this repository's root:

```sh
python3 research/partitions/checks/inventory_external_certificate.py \
  --source-root /path/to/pinned/openai-math \
  --output /tmp/external-certificate-inventory.json
```

The script only reads sources and Git metadata and writes the requested report.
It does not invoke Lake, fetch dependencies or install a toolchain. The upstream
monorepo build configuration declares numerous unrelated packages. Any future
reduced build must preserve the selected theorem's actual dependencies and
record its configuration rather than claim equivalence without checking it.

## Actual statement and mathematical objects

In `lean/OAI/Combinatorics/Chromatic/Model.lean`, `NaturalUnitIntervalGraph n`
contains an extensive monotone function `h : Fin n → Fin n`. `Edge` is the
usual symmetric adjacency relation. `Proper` means adjacent vertices get
different colors. `chromatic r` sums actual maps `Fin n → Fin r`, weighted by
`coloringAscents`, in `MvPolynomial (Fin r) (Polynomial Nat)`.

`PermutationWitness` assigns a partition of `n` to each permutation satisfying
the specified nondescent condition. Its `expansion` field states, **for every
color-alphabet size `r`**, equality of that proper-coloring polynomial with a
sum of inversion-weighted actual elementary products `MvPolynomial.esymmPart`.
These are relevant mathematical objects, rather than symbols defined to be
positive by construction. This observation does not check the expansion proof.

`Main.lean` declares `OAI.elementaryPositivityWitness (n) (G) :
G.PermutationWitness`. The exact source is pinned above; no declaration type
or axiom list from a successful local build is available.

## Decisive dependency and next audit

The final `selectedTable` is chosen from a finite test, but the existence of a
passing table uses `G.historyWitness`. Moreover,
`Witness/ElementaryAlphabetRigidity.lean:121` takes an existing witness `W`
and uses `W.expansion` to prove `uniform_expansion_of_test`. Thus auditing only
the finite table would miss the proof of positivity.

The next trace is:

```text
Main.elementaryPositivityWitness
  → NaturalUnitIntervalGraph.historyWitness
  → ofAdmissibleWitness
  → TriangularDynamics.admissible_polynomial_expansion
  → decorated_polynomial_expansion / decorated_coefficient
  → Laurent and wall machinery
```

`Witness/HistoryMainWitness.lean:9` constructs the history witness from the
admissible expansion. `Witness/ElementaryProductDegree.lean:104` proves that
expansion using decorated histories. Its `ofAdmissibleWitness` transfers an
inversion-weighted expansion to the ascent convention through reversal and
reflection. The energy bounds used with natural subtraction and the wall
identities are substantive remaining semantic obligations. No circularity has
been established; this trace identifies where an audit must continue.

## Feasibility decision and limits

The inventory measured 9,625,600,000 bytes free on the temporary filesystem
(about 9 GiB); an earlier check showed about 11 GiB. Only Lean 4.34.0 is installed
locally, and the upstream checkout has no local mathlib dependency. We made a
conservative decision to defer provisioning the larger environment during this
increment. The plan's 15 GiB storage limit is a ceiling, not a demonstrated
minimum requirement; these observations do not prove that a build cannot fit.

External build attempts, build-process time and provisioning/build downloads
are all zero. No new dependency or toolchain was installed. Source retrieval
through the connector is not included in that zero-download provisioning
measurement. Full-build storage and time requirements remain unknown.

A future attempt must pin the reduced configuration, build the actual theorem,
print its type and axioms, and separately review the mathematical meaning of
the decisive expansion chain. The current result remains **unverified here**.
