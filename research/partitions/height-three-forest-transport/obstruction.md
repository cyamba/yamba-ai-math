# A complete two-to-one obstruction to the P014 grammar

**Proved by the written finite argument below, computationally confirmed;
not Lean.** This refutes cancellation pairing each source with one direct
neighbor in the frozen grammar, including its insertion-digit repair.
It does not refute coefficient unimodality. The
universal partial fork and digit inverse arguments remain valid.

Let `h=(3,5,5,7,7,7,8,8)`. Its graph edges are

```text
12 13 23 24 25 34 35 45 46 47 56 57 67 78
```

There are fourteen edges. The greedy antichain contacts `0,3,7,8` show
poset height three, as also verified by the direct height calculation.
Consider the two signed states `S_13,S_31` with common data

```text
parents       (3,5,4,6,7,0,8,0)
component A   {1,3,4,6}, word 1,3,4,6
component B   {2,5,7,8}, word 2,5,7,8
compositions  ((1,3),(4)) for S_13; ((3,1),(4)) for S_31
marks         (1,1)
epsilon       0
```

Both are actual forest triples of type `(4,3,1)`. Their concatenated word
has inversions exactly `23,24,56`. Thus each has degree three, below the
global midpoint seven, and sign `(-1)^(3-2)=-1`. They are distinct objects:
the first composition order is part of the complete signed space.

## Exhaust every frozen primitive

**Mark and insertion-digit steps.** Epsilon zero requires a one-unit
decrease of a mark or tree insertion digit. Both marks are one and both
tree words are increasing, so every digit is zero. Neither primitive has
a neighbor. This also proves that the sole round-two repair cannot help.

**Checked word surgery.** For `S_13`, removing the last composition part
three gives the word pieces `1` and `3,4,6`. After ordering the components,
the complete word is `1,2,5,7,8,3,4,6`, with four inversions. The tail has
rank one and all marks remain one, so the degree is four, not three.
For `S_31`, removing the last part one separates `6`; it gives the single
positive neighbor `U` below. The only possible word join puts the first
word before the second. Its candidate word `1,3,4,6,2,5,7,8` would require
parent `2->6` on decoding. Edge `26` is absent, so the join is invalid.
The second component's one-part composition cannot be broken.

**Single-edge surgery.** Only the first component's composition can split.
Its three edges detach subtrees of sizes one, two and three.
The size-two cut has no matching composition boundary. The size-one cut
gives the four-inversion forest just described. Its required mark sum is
`1+1+3-4=1`, smaller than the minimum two, so no bounded marks work.
The size-three cut gives `U`, with the unique marks `(1,1,1)`.
The only root-edge join is `6->7`; its canonical word is
`1,3,4,6,7,5,2,8`, with five inversions. Its forced merged mark is
`1+1-1+3-5=-1`, which is forbidden, in either composition order.

**Sibling-fork surgery.** Both components are paths, so neither has a
sibling fork to split. For a join, the only possibility has root `u=6`,
its child `v=4` and other-component vertex `p=7`. It produces the word
`1,3,4,7,5,2,6,8`, again with five inversions, and again forces merged mark
`-1`. Root eight has no larger graph neighbor. Thus there is no legal fork
neighbor for either negative state.

Consequently the complete neighbor union of the two negatives is precisely

```text
U parents       (3,5,4,0,7,0,8,0)
U compositions  ((3),(4),(1))
U marks         (1,1,1)
U epsilon       0
U word          1,3,4,2,5,7,8,6
```

Its inversions are `23,24,67`, hence degree three. Three components give
positive sign. `S_13` reaches it by one edge cut; `S_31` reaches it both by
an edge cut and word splitting. Multiple move witnesses do not create
multiple positive signed objects. Therefore

`|{S_13,S_31}|=2 > 1=|N({S_13,S_31})|`.

No injection or matching pairing states by a single accepted edge of the
complete frozen grammar can cover all negatives. This is stronger than
failure of the four selectors. A future composite-move grammar could have
a larger neighbor relation; this certificate does not rule that out.
The certificate is smallest possible in subset size after the full round-one
graph found no isolated negative. It is not claimed globally minimal over
all Hessenberg vectors or all possible grammars.

## Why this is not a coefficient counterexample

The full coloring-checked coefficient on this development graph is
`q^5(1+q)^4`, whose degree-three first difference is zero. The obstruction
concerns the allowed transformations.

For a concrete semantic check, the complete signed space contains two
different positive degree-three objects outside the displayed neighbor set:
parents `(2,4,5,6,7,0,8,0)`, the same respective two composition tuples,
marks `(1,1)`, and epsilon one. Their component words are `1,2,4,6` and
`3,5,7,8`; their only inversions are `34,56`. Their degree is `2+1=3` and
their sign is positive. This explicit comparison is not a new move, a third
repair or an unrestricted matching experiment. It illustrates the remaining
need to change component membership while retaining composition information.

The next universal argument must supply recoverable cross-block transport
for path components with minimal internal coordinates. Enlarging only the
within-block digit or mark rules cannot resolve this Hall deficit. No such
covering construction or new unresolved theorem is established here.
