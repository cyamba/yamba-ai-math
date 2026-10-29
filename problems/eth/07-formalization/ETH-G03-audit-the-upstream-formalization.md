# ETH-G03. Audit the upstream Lean formalization

| Field | Value |
| --- | --- |
| Category | Formalization / trust |
| Source items | "Bit-level formal verification of algorithmic complexity in Lean 4" |
| Status | **Open** |
| Depends on the upstream theorem | It is the check of it |
| Score (I/B/T/L/Lean) | 4 / 2 / 3 / 4 / 5, composite **3.3** |
| Subresults | none |

## Task

Independently build and check the openai/math formalization of family 378:

1. build `OAI.Algorithms.SubexponentialSAT.SqrtLogSpace.exact_count_and_sat` with the pinned
   toolchain; record `#print axioms` for the top-level theorem and its dependencies;
2. compare the comparator statement
   `lean/ComparatorChallenges/SubexponentialSAT.lean` with Theorem 1.1 of the preprint: encoding
   of inputs (`encodeCNF`), the machine model (`PrimitiveMachine`), the time and space measures
   (`visitedSpace`), and the quantifiers on $k$;
3. confirm that the formal time bound is
   $(L+1)^{O_k(1)}2^{O_k(n(\log\log n)^2/\sqrt{\log n})}$ and that no hypothesis trivializes it
   (e.g. a restricted input class);
4. report any `sorry`, `axiom`, `native_decide` or `implemented_by` in the dependency cone.

## Why

The upstream README warns that model-produced results may contain errors, and three manuscripts
were withdrawn on 2026-10-07. A formal statement that matches the paper is the strongest
available evidence; an independent check by this lab adds value regardless of the outcome.

## Resource boundary

One Lean agent with a large build budget (the upstream development is large); one reviewer for
the statement comparison. External communication about findings is the operator's decision.
