# P013: reversible forest surgery

User-authorized continuation of [P012](../height-three-unimodality/results.md),
from clean `cyamba/yamba-ai-math` revision
`a0c897fb7bcb0d01a9ccff5593c0471424255b96` on
`codex/height-three-coefficient-unimodality`. Existing evidence and publication
material are preserved. No new theorem is asserted.

## Target and primary-source comparison

**Conjecture, novelty unverified:** for every height-exactly-three natural unit
interval poset `P_h`, `n>=7`, and `lambda=(n-4,3,1)`, let
`c(q)=[e_lambda]X_inc(P_h)(x;q)` and `M=|E|`. Construct nonnegative signed
survivors for `c_d-c_(d-1)` at `0<=d<=floor(M/2)`, with `c_(-1)=0`.
The [prior frontier audit](../height-three-unimodality/frontier.md) remains
applicable. General positivity is reported established; the audited proof
does not claim elementary unimodality. Novelty of this exact target remains
unverified, and no claim of an exhaustive new literature search is made here.

[Tom v2](https://arxiv.org/html/2311.08020v2), Definitions 3.1/3.3 and
Theorem 3.4, supplies the complete signed forest model. Proposition 3.7 and
Definition 4.7 supply path and clique splitting/joining. Those mechanisms
are established mathematics. This phase tests a **conditional extension**
outside those hypotheses, rather than claiming their proof as new.

Each raw state contains a decreasing parent forest, every compatible ordered
composition tuple of sorted type `lambda`, every allowed mark, and epsilon.
Its sign is `(-1)^(3-number_of_trees+epsilon)`, and degree is the inversion
number of the concatenated canonical words plus `sum(mark-1)+epsilon`.
Full enumeration, before the lower-half restriction, must recover P012's
complete signed coefficient. Repeated equal parts are not separately labelled.

## Conditional mathematical argument before search

Let a component have canonical word `w`, composition `alpha` with at least
two parts, last part `k`, and mark `r`. Write `w=uv`, `|v|=k`. Replace it by
`(u,alpha_without_last,r)` and `(startmin(v),(k),indstart(v))`, reorder all
components by minima, and retain epsilon. Here startmin successively swaps
values of adjacent ranks until the first value is minimal; startr reverses
those swaps. Decode each proposed word to a decreasing tree and reject it
unless its actual canonical word is exactly the proposed word.

The inverse candidate joins two components in minima order, the second with
one composition part: use `u startr(v,r_v)`, concatenate their compositions,
and retain the first mark. Require actual tree validity and exact recovery
by the break operation. Other components are unchanged. On a legal pair,
the maps are inverse because word cuts and the rank swaps are inverse;
type is unchanged and tree count changes by one, so sign reverses. If
`I_old,I_new` are **global** word inversion numbers, degree preservation
is equivalent to `I_old-I_new=indstart(v)-1` for a break. This equation must
be checked; the clique identity does not justify it in general. Reordering
components can change inversions with components outside the split.

This proves only a reversible **partial relation**, not a global selector or
an injection covering all negative states. A complete proof still needs a
recoverable pivot and positive survivor interpretation. The smallest useful
falsifier is a degree-at-most-`M/2` isolated negative state at `n=7`.

## Frozen experiments and boundaries

Round one has two primitives: one mark changes by one with epsilon toggled;
the checked word split/join above, retaining epsilon. Four deterministic
selectors use both primitive priority orders, each with first/last target in
lexicographic `(parents,compositions,marks,epsilon)` order. Only reciprocal
choices pair. Record collisions, failed recovery and minimal isolates in
`(n,h,degree,state)` order. If there is no isolate, a bounded augmenting-path
test may return a Hall witness **only in this grammar**. Such matching is a
diagnostic, not an explanatory construction or a theorem.

Development includes the prior boundary witness, a critic's new saturated
seven-vertex state, a size-eight disjoint-clique boundary case, and a prior
nonzero size-eight case. The protocol records their exact vectors. Four new
held-out cases are the first two connected height-three vectors at each size
9 and 10 by SHA-256 of `h3-forest-surgery-v1:` plus the comma-separated vector,
excluding every P012 case. Their vectors are frozen before testing; they are
evaluated only after the single possible repair is fixed from development.

Round two permits **one** recorded repair, or retains the original rule.
A possible repair is a single parent-edge cut/join, composition splitting
at any boundary in either concatenation order, and exact scalar mark
compensation. It must be specified before its search. No new held-out
outcome may select the rule. No third proposal/review round.

The [program contract](../../../programs/partition-h3-forest-surgery.json)
uses the harness `pair` fleet: lead mathematician, separate critic, two
rounds, 16 declared dispatch proxy units. Actual research is manual; generated
packets are unexecuted and offline replay is response validation only.
Per round: 600 computation seconds, five million enumeration extensions and
five million candidate charges. Per case: 120 seconds. One enumeration
process; sampled RSS limit 2 GiB; aggregate output-directory cap 250 MiB.
Capped cases remain incomplete, without replacement. No installations or
paid compute. Engineering tests and inspection are reported separately.

## Acceptance and reproduction

A credible universal argument for completeness, validity, sign, degree,
inverse recovery and survivors is required before substantial Lean work.
Acceptance of the target additionally needs an exact coloring bridge,
placeholder-free Lean checking without custom axioms and separate semantic
review. Proved partial identities and finite successes do not meet that gate.

The implementation entrypoint will be
`python3 -m research.partitions.checks.forest_surgery`. Freeze the protocol
before running either round; keep bulk receipts under ignored
`.runs/h3-forest-surgery/`. Run the repository unit tests and
`python3 scripts/check_repository.py` after functional changes.
