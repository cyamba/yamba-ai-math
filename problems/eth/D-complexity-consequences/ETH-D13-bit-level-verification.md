---
id: ETH-D13
source: sheet "Refuting ETH" consequence 10
category: complexity-consequences
status: open (engineering)
---

# ETH-D13: Bit-level verified complexity in Lean

OpenAI's comparator `SubexponentialSAT.lean` states the result for a `PrimitiveMachine` with explicit tape
accounting. Tasks for this repository:

1. Build the comparator locally against its pinned Mathlib and record the exact statement and axioms
   (`#print axioms`) in a verification note. (Network policy here blocks the Mathlib cache; a source build of
   the needed closure on 2 cores took about an hour for the polynomial modules.)
2. Map each paper lemma to its Lean counterpart (dependency table), to make agent work on
   [ETH-A07](../A-algebraic-core/ETH-A07-algebraic-core-decoupling.md) and [ETH-B04](../B-exponent-frontier/ETH-B04-loglog-gap.md)
   reuse existing definitions.
3. Lessons for agent harnesses: which parts of the formalisation are pure algebra (cheap for agents) versus
   machine plumbing (expensive). Feed into `meta/` only through the meta protocol.
