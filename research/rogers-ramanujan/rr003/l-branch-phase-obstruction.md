# RR003 local L phase repairs: exact obstructions

**Refuted restricted repairs; author-only mathematical assurance.** This
continues the existing recursive mechanism B. It neither refutes every L
embedding nor supplies one. No additional critic stage, global mechanism,
weight sweep or change of success criterion is introduced.

## A three/six phase flag still collides

Start with the corrected same-level L conversion in
[l-branch-boundary-obstruction.md](l-branch-boundary-obstruction.md). At each
suffix level i>=j, pair as many 9i+8 and 9i+10 parts as possible. For each
such pair replace one of the output sixes by two threes. This attempts to
retain the local full-pair phase that the earlier conversion discarded.
The operation preserves weight and has no negative six count: each paired
10-part supplied a six. It is an exploratory repair, not an accepted map.

Already at cut j=0 the distinct valid L data

    D1=(8,10,10,11),
    D2=(6,7,7,8,11)

both have |D|=39, actual L weight46 and normalized weight39. The proposed
cost6 repair sends both to

    (3,3,3,3,3,4,4,5,5,6,6), weight45.

For D1 the original conversion supplies three threes and three sixes; one
paired suffix (8,10) changes those to five threes and two sixes. D2 has no
suffix10, and already supplies five threes and two sixes including its
common six. Both have two fours and two fives. These multiplicities prove
the collision exactly. Appending any number of common sixes to both inputs
preserves it, so this rule fails on an infinite family. No assertion that
these are the globally smallest witnesses is made.

## A conditional impossibility for fixed output levels

The problem exceeds choosing a different phase flag in the same small rows.
Consider the eight pairs

    (A,B)=(0,1),(0,3),(1,0),(1,2),(2,1),(2,3),(3,0),(3,2).

Define an actual L cut of index zero with

    D=7^A 8^B 10^(3-A) 11^(3-B) 6^((A+B-1)/2).

All multiplicities are nonnegative integers. These cuts are distinct,
contain only permitted common/prefix/suffix parts, and have

    |D|=7A+8B+10(3-A)+11(3-B)+3(A+B-1)=60.

Their actual L weight is67; normalized weight is60. Every cost6 image must
have weight66. Suppose a proposed repair keeps the number of output fours
at count7+count10=3, keeps the number of output fives at count8+count11=3,
and uses only output parts3,4,5,6 on this fiber. The threes and sixes must
then satisfy

    3*count3+6*count6=66-3*4-3*5=39,
    count3+2*count6=13.

There are exactly seven nonnegative solutions, count6=0,...,6. Eight
sources have at most seven targets. Therefore **no injective cost6 repair
with these fixed output counts and levels exists** on this fiber. This
pigeonhole argument is independent of any particular phase-flag formula.
It does not exclude repairs that change four/five counts, move quotient
levels, or retain data in other allowed parts.

## Evidence, next lemma and learning

The direct receipt l-phase-local-repair-obstruction checks the two literal
cuts and their common output, the eight distinct cuts, their exact weights,
and the seven possible targets. These individually specified finite objects
are not an enumeration sweep above30. The argument above supplies the
conditional impossibility proof; no universal complete map follows from it.
Both scheduled critic rounds preceded this final author audit.

The next L lemma must permit a different target statistic or a reversible
carry between levels, while also avoiding the already assigned K image.
It is no longer enough to retain the single (7,11)/(8,10) full-pair bit in
three/six multiplicities while preserving both other counts at these levels.
The global all-n branch obligations and U-C route remain unchanged.

Workflow hypothesis, **unvalidated**: counting one explicitly constrained
inverse fiber can rule out a whole class of local repairs before substantial
implementation. No general harness change or improved discovery-rate claim
has been evaluated.
