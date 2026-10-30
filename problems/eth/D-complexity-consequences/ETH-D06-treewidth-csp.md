---
id: ETH-D06
source: sheet "10 consequences" item 4 ("Can you beat treewidth?")
category: complexity-consequences
status: open
---

# ETH-D06: Marx's treewidth barrier for binary CSPs

Marx (2010): under ETH, binary CSP with primal graph `G` cannot be solved in `f(G) n^{o(tw(G)/log tw(G))}`.
With ETH refuted the lower bound loses its basis. **No algorithm follows automatically**: the CSP domain has
size up to `n`, so a Boolean encoding needs `|V(G)| log n` variables with unbounded-width constraints.

## Questions

1. For CSPs with **bounded domain** `|Sigma| = O(1)` and arbitrary primal graph on `v` variables, Theorem 1
   gives `2^{o(v)}` (constraints of arity 2 over a constant domain are constant-width CNF). Can one get
   `2^{o(tw) } poly` from it via tree decompositions (sum over bags with subexponential inner solver)?
2. For large domains: does a fine-grained version of the barrier survive under a `sqrt(log)` hypothesis
   ([ETH-B08](../B-exponent-frontier/ETH-B08-sqrt-log-hypothesis.md))?
