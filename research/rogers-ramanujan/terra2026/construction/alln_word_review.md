# Independent review: all-n cut-word cancellation

This reviews the root agent's cut-word proposal, not a completed KR1 bijection. **Conclusion: the sign-reversing involution and survivor description are sound conditional on Xia's labeled cut expansion and its stated prefactor.** The theory agent reports checking the specialization in Xia v1 (3.5) and Lemma 2.2; I have not independently rechecked the primary source. Written semantic review, not Lean certification. Novelty NOT VERIFIED.

## Explicit coordinates

Fix n≥1. The input has cuts 0≤k1≤⋯≤kn; independently repeated particles of colors α and β in layer i, index j, with k_i≤j≤k_(i+1), where k0=0 and k_(n+1)=∞; and, for 1≤h≤m=floor(n/3), an optional marker of weight 9h and sign −1. Particle weights in layer i are α: 3n+4+3i+9j, β: 6n+5−3i+9j; cut weight is 9Σk_i. Retain all common-tail particles as inert context.

Flatten each layer by sorting particles by increasing index and then α<β, placing cut symbol `|` between layers. This gives word w of N≥n symbols and weakly increasing integer indices j1,...,jN. The only required strict inequalities are j_t>j_(t−1) if w_(t−1)=β and w_t=α: these two consecutive symbols lie in one layer and an equal-index β must follow α. There are no constraints across a cut marker, including repeated cuts. Conversely, the word and indices uniquely reconstruct cuts and every colored multiplicity by splitting at markers. Set j0=0, ε_t=1 for β→α and 0 otherwise, and δ_t=j_t−j_(t−1)−ε_t. Then all δ_t≥0, and every nonnegative vector produces exactly one legal state. A cut marker separates layers, so β→α is automatically within a layer.

Each index increment contributes 9 to the total weight. Hence each δ_t costs 9(N−t+1). The word contributes the sum of intrinsic node weights and the strict-step shift 9Σ ε_t(N−t+1). This is nonnegative, and all operations preserve the word and its intrinsic weight.

## Involution and exact survivors

Each h≤m addresses δ_(N−h+1); this coordinate exists since N≥n≥m. Scan h increasingly for the first h such that its marker is present or the addressed δ is positive. If marked, remove the marker and increase δ by one; if unmarked and δ>0, insert the marker and decrease δ by one. This is weight preserving because both changes have size 9h; sign flips. The selected h stays active after either operation and all smaller h stay inactive, so repeating the rule chooses the same h and reverses the change. It is a deterministic one-step involution with no lookup and no need to normalize moves sequentially. It terminates on every finite state.

Fixed points are exactly the unmarked objects with δ_(N−h+1)=0 for all 1≤h≤m. Thus they are an explicit positive, weight-preserving model of the signed cut expansion, for every n, if the expansion and prefactor hypotheses hold. In original indices, these last m consecutive jumps equal their forced strictness ε; this does **not** force the last m raw jumps to zero when ε=1. For fixed w their generating factor is

    q^[intrinsic(w)+9Σ_t ε_t(N−t+1)] / ∏_{h=m+1}^N (1−q^(9h)).

Sum over all n-cut words and multiply by the common unrestricted-tail factor. Since particle intrinsic weights are positive, only finitely many words contribute at each weight, so the series is well defined. This representation relies on no enumerative rank matching. It is a new candidate positive model for the auxiliary C_n, not a map from the product to the KR1 gap class; the remaining bridge is still required.

## Model caveats

The argument assumes the two colors are separately distinguishable even if numerical particle weights coincide, the cuts' intervals are inclusive at both ends, and there are no other per-layer occupancy restrictions. Changing those hypotheses can invalidate the word bijection. The fixed-letter word itself is necessary: deleting it or forgetting particle colors would generally lose inverse data. No claim is made here about A_n or other sequences, whose restrictions must be checked separately.

## Bounded independent executable corroboration

`python3 research/rogers-ramanujan/terra2026/construction/check_alln_word.py` produced `3178008 cut-word states: coordinate round-trip, weight, sign, inverse, survivors`. It checks n=3,4,6 with bounded words, gaps and marker choices, including m=2. The source script SHA256 at this run was `bf764c18909540da801d5e3c5d882c9551d733ac6f3f4117a30002e6728f1c47`. This test does not replace the all-parameter proof or source verification.
