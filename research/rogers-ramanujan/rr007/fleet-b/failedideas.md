# Fleet B exact failed interfaces and constructive clues

Author-only ordinary written arguments; no independent semantic review yet.
These failures concern specified interfaces, not KR1 or all colored maps.

## Physical single/pair quotient: exact finite colors, wrong Konan interface

Take the intrinsic A atomization from RR003's direct endpoint. Use five
colors S1,S2,S3,E,O. For a nonnegative quotient k their literal meanings are

* S_r(k) is one part3k+r, r=1,2,3;
* E(k) is the pair(3k+1,3k+2);
* O(k) is the pair(3k+3,3k+3).

In increasing physical order the exact required quotient gap from one atom
to the next is the following matrix (row=current, column=next):

| | S1 | S2 | S3 | E | O |
|---|---:|---:|---:|---:|---:|
| S1 |1|1|0|1|1|
| S2 |1|1|1|1|1|
| S3 |2|1|1|2|1|
| E |1|1|1|1|1|
| O |2|2|1|2|1|

This matrix is derived, not fitted: two singles require physical gap>=2;
a single before E(k) is at most3k-1, before O(k) at most3k; a single after
E(k) is at least3k+4, after O(k) at least3k+6; successive pair levels
2k/2k+1 must differ by at least2. Division by3 gives each displayed entry.
Those atom boundary conditions are sufficient for all A conditions, since
every triple meeting a pair is covered by its two boundary inequalities,
and a triple of singles spans at least4. They are necessary by the same
local checks. Close pairs cannot overlap, since three overlapping close
parts span at most2, violating distance-two separation.

Consequently the model has an exact intrinsic inverse: expand its atoms;
the close pairs in the expansion are exactly E/O, and all other parts are
the singles. Its weight is

`sum_S(3k+r) + sum_E(6k+3) + sum_O(6k+6)`.

With the written RR003 A/C extraction/merge proof, this gives a complete
finite-color encoding of C in a generalized regular model. That endpoint
has author-only assurance in this session until the distinct critic
reviews it. This is **not** an encoding into Konan's flat/regular domains:
the energies take2, and the literal raw-size slopes depend on the species.

Two precise simple repairs fail:

1. A color-dependent quotient shift k->k+v_color changes a directed energy
   by a potential difference. The E->O and O->E entries sum to3, and that
   sum is invariant under these shifts. Two binary energies sum to at
   most2. Hence no such shift turns this exact five-color model into a
   degree-one minimal-energy model.
2. Keeping physical-position quotients gives literal slope3 for a single
   and6 for a pair. Degree-one size/word preservation alone does not
   preserve this grading. The universal rigidity argument below proves
   that a common affine specialization is necessary for the full theorem
   map, rather than only observing that it was not stated.

The source's degree-two domains allow larger derived energies, but each
part has size2k+e(i,j) and a common q specialization. Treating an E/O atom
as one such secondary while treating S as a different slope does not meet
that definition. A nonlocal split/fuse/reordering remains possible; the
argument does not exclude it.

## Affine specialization rigidity for the full degree-one map

Let a nonempty finite nonground color set satisfy Konan's ground hypotheses,
and suppose its stated degree-one map preserves
`w(k,c)=d_c*k+z_c` for **every** flat input. All terminal weights cancel
between source and target. Then z_ground=0 and all d_c equal d_ground.
Here preservation means literal additive weight, not just total raw size.

Fix one nonground color c and set t=1-delta. The singleton retained word
has baseline c_t. One leading ground part has size1. The explicit source
formulas send `(g_1,c_t)` to `c_(t+1)`, omitting the common terminal.
Thus `d_c=d_g+z_g`.

If e(c,c)=1, the retained word cc has baseline sizes t+1,t. A leading
ground of size2 is exchanged for an increase of1 in both c sizes.
Weight conservation gives `2*d_g+z_g=2*d_c`; together with the preceding
equation this forces z_g=0 and d_c=d_g.

If e(c,c)=0, take the flat chain with nonground sizes t+2,t+1,t and ground
parts of sizes2,1 in the two internal slots. The explicit slot formula has
conjugate-displacement partition(2,2,2), so all three output c sizes are
t+2. Equality gives `3*d_g+2*z_g=3*d_c`. Combining with the singleton
again forces z_g=0 and d_c=d_g. Both chains satisfy the flat relations for
either delta, so the two cases exhaust the binary diagonal possibilities.
Applying this to every c proves the assertion.

Conversely, a common slope and zero ground offset suffice: total raw size
and the ordered nonground color word are preserved by the stated theorem.
This is an elementary author argument using its explicit formulas, not a
fresh independent proof of the entire source bijection. It rules out a
mixed slope specialization of the **full** degree-one domain; a proper
subfamily with separately proved closure is not excluded.

## Natural degree-two literal forgetting

The fully specified natural five-color R2 predicate is in `author.md`.
It is not enough to choose colors for unchanged A parts. R2 color11 twice
is valid atweight4 but forgets to invalid A=(2,2); A=(1,3) has no
unchanged-part R2 encoding; A=(5) cannot be a single R2 part. The pilot
checks these exact transcription claims at weights4/5. It neither solves
nor refutes the nonlocal fusion interface.

## Two partial maps cannot simply be united

B2's low-four-part cone and A2's a0/1 wall map agree where both C source
domains meet. Nevertheless A2 sends C=(0,2,(),(0,0)) to B=(3,3,6), while
B2 assigns that same B to C=(3,0,(1,1,1),()). The union is noninjective at
weight12. Agreement on an intersection is weaker than disjointness of
the extra images. The exact frozen B2 pilot checks this collision and
does not overlay the maps.
