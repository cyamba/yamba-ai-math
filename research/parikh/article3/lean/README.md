# Lean: completeness of Parikh matrices for doubled letters

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

Not formalised here: the general conjecture for multiplicity `n ≥ 3` (Conjecture 6 of the note),
which is open.
