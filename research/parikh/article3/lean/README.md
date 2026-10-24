# Lean: completeness of Parikh matrices for doubled and tripled letters

Copyright (c) 2026 Christopher Yamba. All rights reserved.

Lean 4.34.0, core library only, no external dependencies. This folder is separate from `lean/`
(no shared file is touched). Build with `lake build` from this directory.

`ParikhCompleteness.lean` works at the level of words. A word is a `List Nat`, `occ w p` is the
number of embeddings of `p` as a scattered subword of `w`, and `E w j m` is the Parikh-matrix
entry `|w|_{j(j+1)⋯(j+m-1)}`. Nothing is proved about an abstract model: every statement is
about actual words.

Main theorems (notation of `notes/explore-completeness.md`):

- `rectangle`: the **rectangle rule**, for any multiplicities. If `w` has no subword
  `e (e+1) e (e+1)`, then `|w|_{j⋯l} · |w|_{e(e+1)} = |w|_{j⋯(e+1)} · |w|_{e⋯l}` for every
  window `j ≤ e < e+1 ≤ l`. This is the thesis's product rule (Prop 3.4) with "the letter occurs
  once" replaced by "the edge is a rectangle".
- `crossing_formula`: **case (c)**. If every inner edge of a window of at least four letters is
  the crossing `abab`, the window entry is `a₁(d₁ + (t+1)d₂ + d₂) + b·d₂`, where `a₁, b, d₁, d₂`
  are fixed by four short entries.
- `avoid_of_not_crossing`: with at most two copies of `k` and `k+1`, an edge that is not a
  crossing avoids `k (k+1) k (k+1)`.
- `complete_two`: **Theorem 3**. In a window of at least four letters whose inner letters occur
  at most twice, the window entry is determined by the shorter entries of the window.
- `determined_by_short`: **Corollary 4**. If the inner letters occur at most twice, the entries
  of length at most 3 (diagonals 1–4) determine every entry. For permutations this contains the
  thesis's Parikh Matrix Completeness Theorem (Thm 3.5).
- `sharp_fourth_diagonal`, `sharp_three_copies`: the two sharpness certificates (`21332` /
  `32123`; `2343212443` / `3221443234`), checked by `decide`.
- `family_three`, `family_four`: the sharpness family of Proposition 7 at n = 3 and 4
  (content (1, n, …, n); the Parikh matrices differ only in the corner), checked by `decide`.
  The family for every n is proved on paper (Lemma 8 by the reflection principle), and is
  verified for n ≤ 30 by `notes/completeness-scripts/family.py`.

Supporting lemmas: the cons recursion `E_cons` (the Parikh-matrix morphism read one letter at a
time), the splits at the first copy of a letter (`occ_first`, `occ_second`, `occ_mid`), and the
chain lemma `chain` (the transfer vector is multiplied by `[[1,1],[0,1]]` at each crossing).

Axioms (`#print axioms`, 23 October 2026): `rectangle` uses `propext` and `Quot.sound`;
`crossing_formula`, `complete_two` and `determined_by_short` use `propext`, `Classical.choice`
and `Quot.sound`; the two sharpness certificates use none. There is no `sorry` and no
`native_decide`.

## `ParikhCompletenessThree.lean`: three copies (24 October 2026)

Conjecture C of Article 3 at n = 3, by the pivot-letter method of `notes/proof-c3.md`. It uses the
same conventions and imports `ParikhCompleteness`. Main theorems:

- `pivot_theorem`: **Theorem 4.1** of the note.
  - Setting: the window `j, …, j+s+u+4` (at least five letters) with pivot `m = j+s+2`, so every
    pivot at distance at least 2 from both ends is covered.
  - Hypothesis: `m` occurs at most twice (any other multiplicities), or `m-1`, `m` and `m+1` occur
    at most three times each.
  - Conclusion: the window entry is determined by the shorter entries of the window.
- `complete_three`: **Corollary 4.2**, Conjecture C for n = 3. In a window of at least five
  letters whose inner letters occur at most three times, the window entry is determined by the
  shorter entries.
- `determined_by_short_three`: **Corollary 4.3**. If the inner letters occur at most three times,
  the entries of length at most 4 (diagonals 1–5) determine every entry.
- `determined_by_short_doubled`: **Corollary 4.4**. If every letter `k` with `lo+2 ≤ k ≤ hi-2`
  occurs at most twice, the entries of length at most 4 determine every entry. The letters
  `lo`, `lo+1`, `hi-1` and `hi` are unrestricted.

The steps of the proof, as formalised:
- **The pivot decomposition.**
  - `occ_insert`: inserting a copy of `m` adds exactly the occurrences through it.
  - `pivot_one`, `pivot_two`, `pivot_three` and `decomp_one`, `decomp_two`, `decomp_three` split a
    word at the copies of the pivot.
- **The copy data.** `Copies3` and `Copies2`, built by `copies3` and `copies2`, hold the moment
  identities, the monotonicity, the transfer of equal values and the boundary values
  (Lemmas 2.1, 2.2).
- **Rules 1 and 2 over `Int`.** `rule1_two`, `rule1_three`, `minor_two` and `minor_three`. The
  polynomial identities are closed by core `grind`.
- **The chain lemma (Lemma 3.3), by kernel evaluation.**
  - `chainCheck_eq` checks the 16 rigid chains against all 4⁶ chains with values in `[0, 3]`, and
    `rigidCheck_eq` checks that every rigid chain is one of the 16.
  - From these: `chain_lemma` and `rigid_mem`.
- **The rigid case (Lemma 3.4).** `rigid_arith` and `rigid_three` (16 cases, `omega`).

The sharpness statements of the note (Proposition 4.5(a), (b)) are the certificates
`family_three` and `family_four` of `ParikhCompleteness.lean`.

Axioms (`#print axioms`, 24 October 2026):
- `pivot_theorem`, `complete_three`, `determined_by_short_three` and `determined_by_short_doubled`
  use `propext`, `Classical.choice` and `Quot.sound`;
- `chain_lemma` and `occ_insert` use `propext` and `Quot.sound` only.

There is no `sorry` and no `native_decide`. The module builds in about 16 s.

Not formalised: Conjecture C for multiplicity `n ≥ 4`, which is open.
