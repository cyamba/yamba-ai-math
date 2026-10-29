# ETH-G02. A Mathlib library of counting-preserving reductions

| Field | Value |
| --- | --- |
| Category | Formalization |
| Source items | "YMB-ETH-05: formal SERF reductions in Lean (#IndependentSet and chromatic polynomial)" |
| Status | **Started**: independent sets Lean-verified |
| Depends on the upstream theorem | No |
| Score (I/B/T/L/Lean) | 2 / 1 / 5 / 3 / 5, composite **2.7** |
| Subresults | Lean [`IndependentSets.lean`](../lean/EthConsequences/IndependentSets.lean): `card_indepSets_eq_card_satAssignments`, `card_indepSets_size_eq` |

## Task

On Mathlib's `SimpleGraph`, prove count-preserving encodings into CNF on $O(|V|)$ (or
$O(|V|+|E|)$) variables:

1. independent sets and independent sets of each size (done);
2. proper $q$-colourings, $q$ fixed: one-hot variables, $\#\mathrm{Col}_q(G)=\#\mathrm{SAT}(F_{G,q})$;
   connect to `SimpleGraph.Coloring` and its `Fintype.card`;
3. vertex covers (complements of independent sets) and the Vertex Cover kernel statement in a
   form usable by [ETH-D03](../04-fine-grained/ETH-D03-subexponential-fpt.md);
4. perfect matchings via Tseitin encodings of "exactly one edge at each vertex" with unique gate
   values (parsimony);
5. a generic Tseitin lemma: circuits with fan-in 2 encode parsimoniously with one variable per
   gate.

## Correction

The chromatic **polynomial** needs colourings with up to $|V|$ colours, which is not an
$O(|V|)$-variable encoding; only fixed $q$ is in scope.

## Resource boundary

One Lean agent per item; items 1 to 3 in one iteration.
