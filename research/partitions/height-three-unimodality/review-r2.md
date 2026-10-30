# P012 construction review, round 2

Date: 2026-10-23. Reviewer: separate `frontier_critic` role. This is the
second and final construction proposal/review round of the bounded initial
phase. The reviewer inspected source, tests and saved receipts, checked their
hashes and arithmetic, and independently checked the isolated witness below
by hand. No additional forest or tableau enumeration, coloring-oracle run,
test execution or Lean build by this reviewer is asserted.

**Verdict: supported complete finite comparison; universal theorem
incomplete.** The complete forest-triple space agrees with the independently
oracle-checked tableau coefficient on the selected development example.
Changing only marks cannot cancel every negative first-difference state.
This is a refutation of that diagnostic move alone, not a refutation of a
general forest construction, nor of the coefficient-unimodality conjecture.
No collision-free forest matching or new universal result has been obtained.

## Material reviewed and evidence binding

The reviewed implementation is `research/partitions/checks/forest_triples.py`,
the prospective aggregate artifact guard in `height_three.py`, added cases
in `tests/test_height_three.py`, and frozen `forest-protocol.json`. The
accepted round-two contract compares the complete forest space after a
tableau obstruction; it does not require a new split/merge search. The
frozen protocol explicitly says no join/split search and no use of held-out
cases for repair. The earlier review's optional search recommendation has
been clarified accordingly.

At the initial review, all named source hashes in the round-two report
matched the current files. The embedded protocol equals the separate frozen
protocol, and its input hash equals the accounted round-one report. Source
stability is also recorded by the execution. The following source hashes
bind the **executed versions**, including the forest source preserved in
ignored `r2-source/`; a later reproduction amendment is disclosed below.
Relevant SHA-256 values are:

| Item | SHA-256 |
| --- | --- |
| Ignored `.runs/h3-unimodality/r2.json` | `b90a0ff29a9f46329557b9651beb7ef33b8a689668ff5bb4507e86ac377682c2` |
| Frozen `forest-protocol.json` | `c171e78b7d28e592b48fd35eddf726f6e5e607b619d9299b0beb4e67980abdbe` |
| Accounted round-one input | `3a49b79d32f6f08aba69893c7dd53fa426b87dc61c9eae593dcb7407809be54a` |
| `forest_triples.py` | `98e674f05453f9b7990df5122ee77f73e028175b1c0b8b76dfd8d96d04f40daf` |
| `height_three.py`, including prospective guard | `45ae739ed8c3ea25ee95198107d5c99ff6ed3c09d168b23bf3a45a134571dd67` |

The recorded base revision is
`dce60269fca1774ea8d5600d30f62dbc39c927a4`, on branch
`codex/height-three-coefficient-unimodality`. Hash agreement binds these
observations to saved inputs and source; it is not a proof certificate or
an attestation of the time at which the protocol was frozen.

**Reproduction amendment after execution:** the current `forest_triples.py`
has SHA-256
`da0a87a2a79c0ae84f40c46d73b80b051c43d22414effb3cc01abb3ef73a1287`.
Comparison with the preserved executed source shows only the addition of
`same_protocol_spec(recorded, proposed)` and its use at the frozen-protocol
check. It excludes `input_sha256` from equality while requiring equality of
every remaining field. Thus a fresh round-one execution receipt may be bound
without changing the selected `h`, target, selection rule, enumeration,
diagnostic, limits, round or holdout rule. A focused test checks acceptance
of a changed input hash and rejection of a changed `h`; it was read, not
executed by this reviewer. The original frozen protocol file retains its
original hash, while a replay's embedded protocol records its new input
hash. Those two protocol objects need not be byte-identical on a fresh
replay. No enumeration, statistic, diagnostic or saved research output
changed, and no research rerun is asserted for this amendment. All other
named source hashes still matched at closure. This is reproduction
engineering within round two, not a third construction proposal.

## Completeness and mathematical conventions

The inspected source agrees with [Tom, Definitions 3.1/3.3 and Theorem
3.4](https://arxiv.org/html/2311.08020v2), as recorded in the
[frontier audit](frontier.md):

- Each vertex chooses either no parent or one larger adjacent parent. The
  smallest vertex of an undirected cycle would have two larger neighbors
  on that cycle, which is impossible in this encoding. Thus these choices
  give precisely decreasing forests, with a unique parent vector for each
  forest. Keeping at most three components loses no type-`(3,3,1)` term:
  each component must receive a nonempty composition and there are only
  three parts in total. Distinct forests remain distinct even if their
  canonical words coincide.
- Components are ordered by their minima. Each tree word starts with its
  minimum and then repeatedly takes the smallest unread vertex adjacent
  to a read vertex. This is Tom's canonical listing, rather than an
  arbitrary traversal or a sorted vertex list.
- For each ordered component list, the code takes every distinct ordering
  of the multiset of target parts and every cut into nonempty composition
  blocks with the required component sizes. This exhausts all assigned
  compositions. The equal parts `3,3` are not separately labelled, so
  removing identical part permutations removes duplicates rather than
  mathematical multiplicities. Every allowed mark
  `1 <= r_i <= alpha^(i)_1` is then retained.
- With three total composition parts and `m` trees, the sign is
  `(-1)^(3-m)`. The weight is the graph inversion number of the
  concatenated canonical words plus `sum_i(r_i-1)`. The implementation
  includes inversions between trees as well as within tree words. It
  preserves parent and composition identities, not merely aggregate
  coefficients.

For a fixed forest and assigned compositions the mark sum is

\[
 (-1)^{3-m}q^{\operatorname{inv}_G(w)}
 \prod_i[\alpha^{(i)}_1]_q.
\]

Doubling each marked triple with `epsilon in {0,1}`, sign multiplied by
`(-1)^epsilon` and degree increased by `epsilon`, therefore enumerates
`(1-q)c_(3,3,1)(q)`. The retained degrees are exactly
`0,...,floor(M/2)`. The implementation checks this first-difference
identity against its full forest coefficient.

The added tests cover small complete coefficients against the independent
coloring oracle, forest distinctness, canonical frontier traversal,
repeated parts, caps and development-only witness selection. These are
meaningful checks of different failure modes; this review reports source
inspection of them, not their execution.

## Complete comparison and scoped obstruction

The selection rule uses only complete development cases with a saved
tableau isolate. Its lexicographically first choice is

\[
 h=(2,4,4,6,7,7,7),\qquad \lambda=(3,3,1),\qquad M=9.
\]

The receipt records 110 scanned forests with at most three components,
72 contributing forest/composition blocks and 320 marked triples. The
first count includes forests that receive no compatible composition; it
is not a count of contributing blocks. The marked census is 56 positive
one-tree, 156 negative two-tree, and 108 positive three-tree triples. The
result is

\[
 c(q)=q^3(1+q)^3,\qquad
 (c_d-c_{d-1})_{d=0}^4=(0,0,0,1,2).
\]

It agrees exactly with the accounted round-one tableau value. That input
case has an independently computed coloring-oracle agreement. Round two's
`coloring_agrees=true` is this **transitive comparison with the saved
oracle result**, not a newly executed coloring calculation.

The doubled lower-half space has 258 negative states and 261 positive
states. Its positive-minus-negative counts agree degree by degree with
the displayed differences. The diagnostic permits retaining the forest
and compositions, changing one mark by one, and toggling `epsilon`. Of
the 258 negative states, 206 have at least one legal diagnostic neighbor
and 52 have none. Having a neighbor does not establish injectivity or
reciprocal recovery, and no selector or matching was tested for this
diagnostic.

The first saved isolate has parent vector
`(0,3,4,5,6,7,0)`: a singleton `1` and the tree path
`2--3--4--5--6--7`. All its edges belong to this graph. Its canonical
words concatenate to `1,2,3,4,5,6,7`, so its graph inversion number is
zero. Assign compositions `(1)` and `(3,3)`, marks `(1,1)` and
`epsilon=0`. There are three parts and two trees, giving total sign
`-1`, weight zero and effective degree zero. A mark step preserving
effective degree while changing `epsilon` from zero to one must decrease
a mark by one. Both marks already equal one. Hence this state has no
diagnostic neighbor, independently of the enumeration.

This is a small explicit obstruction to mark steps alone. A split or merge
could change the forest or its composition data, so the witness gives no
obstruction to an untested larger forest grammar. It also gives no
counterexample to unimodality: the entire degree-zero signed count is zero.

## Resource amendment and next decisive work

The recorded round-two computation used 1,290 charged extensions, 539
candidate checks, approximately 0.002492 wall seconds and 23,363,584 bytes
peak RSS. These are execution measurements, not mathematical complexity
bounds. No additional construction round or reviewer enumeration was run.

The prospective report writer now refuses replacement and sums existing
file sizes recursively under the output directory before admitting a new
report. This corrects the former per-file guard for this single-directory,
single-process workflow. It is an aggregate **output-directory** guard,
not a global accounting mechanism for outputs scattered across unrelated
directories or a hard memory limit. At inspection the ignored output
directory contained 543,079 bytes, including retained earlier reports and
source snapshots, well below the 250 MiB cap. The new guard has a focused
test that a second report can exceed the shared directory allowance even
when each file fits individually.

The next mathematical requirement is a lemma that changes tree or
composition structure while accounting for both word inversions and mark
weight, with explicit inverse recovery. One possible route is a reversible
cancellation of forest/composition blocks whose positive survivors have
palindromic unimodal generating functions with common center `M/2`.
Individual signed blocks have varying centers in this example, so their
`q`-integer products alone do not supply such a lemma. An injection only
within each unrestricted degree would restate the desired inequalities.

A future experiment would first freeze a small split/merge grammar and
its weight-compensation rule, test the displayed degree-zero isolate, and
then test validity, sign, degree, inverse recovery and collisions on newly
reserved structural cases. Such an experiment requires a new explicitly
bounded phase; it was not performed here. The present two rounds end with
two retained move obstructions and a complete model comparison, not a new
construction or theorem. Substantial Lean work remains gated on a credible
universal mathematical argument.
