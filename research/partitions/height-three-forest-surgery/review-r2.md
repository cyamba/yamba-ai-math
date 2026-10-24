# P013 final review: the repaired grammar is obstructed

Date: 2026-10-24. Reviewer: separate `frontier_critic` role. This is the
second and final P013 proposal/review round. The reviewer inspected the
executed source, saved receipts, protocol, selection lock and snapshots,
checked their hashes and accounting arithmetic, and independently checked
the obstruction below by hand. No reviewer enumeration, search, test
execution, coloring-oracle calculation or Lean build is asserted.

**Verdict: supported complete-grammar refutation on a development case;
held-out evaluation partly incomplete; universal target incomplete.**
The repaired relation has an isolated negative state at seven vertices.
No selector, pivot or matching using only its three frozen primitives can
cancel all negative states there. This refutes the proposed grammar as a
universal explanation, not the coefficient-unimodality conjecture. The
conditional inverse lemma remains valid. The candidate budget was reached
and respected; capped and unstarted cases remain incomplete. P013 ends
without a third repair or a theorem claim.

## Evidence and source binding

The execution records base revision
`a0c897fb7bcb0d01a9ccff5593c0471424255b96` and branch
`codex/height-three-coefficient-unimodality`. It reports round two,
`repair=true`, `source_stable=true` and `research_validated=false`.
All named source hashes matched both the files at inspection and the
retained `r2-source/` snapshot. These hashes identify the executed versions;
subsequent synthesis edits would not retroactively change that binding.

| Item | SHA-256 |
| --- | --- |
| Ignored `.runs/h3-forest-surgery/r2.json` | `4b44a5c8e863a1e22dc2fbe9590b28353d8f27b791dde6a46442239b0d0ca206` |
| Executed `forest_surgery.py` | `7920ad3a5725bdf01250eedf1c5d7f3606431a69fde4e6c669ed7af9af7987d3` |
| Frozen `round-two-protocol.json` | `b97fcd264c9100279e0a2d765526103d2d8d421c7e23095d00bd3f89317a3447` |
| Input round-one report | `d2d032da37f170a95d52ec21b59906d473beca45fd0e7e91837c52c34eb3b112` |
| Written `repair.md` | `16ed915f8ea139a17f3f3e3de58c8d1b26626ca97b0e96bba238cd97c39739cb` |

The embedded round-two specification equals the frozen specification;
its input hash matches the actual round-one report. The separate selection
lock equals the embedded lock, and its development hash matches the first
four saved case records. Source inspection places lock writing before
held-out execution. These checks support provenance and ordering in the
implementation; they are not independent attestations of wall-clock
history or mathematical proof certificates.

## Conditional lemma and engineering amendments

The sole repair is the one described in [repair.md](repair.md) and reviewed
in [round one](review-r1.md). It adds single parent-edge cuts and joins,
every compatible nonempty composition boundary in either assignment order,
and every bounded mark solution of the scalar weight equation. It retains
the two earlier primitives. Epsilon stays fixed for surgery, so changing
the number of components by one reverses total sign. Global inversion
numbers include reordered components and all cross-component edges.

Cutting the added edge, choosing the original composition boundary and
recovering the original bounded mark pair give reverse membership. The
implementation checks reverse membership in the same primitive, actual
state validity, type, sign and degree. These facts establish a symmetric
partial relation. They do not supply a uniquely recoverable selector:
several cuts, assignments or original mark pairs can reach the same state.
The exact degree equation can also have no allowed solution. The complete
raw signed space and its statistic are unchanged from the first review,
and still come from [Tom's established forest expansion](https://arxiv.org/html/2311.08020v2).

The additional source changes after the edge-repair preflight are
engineering amendments, not a second mathematical repair. Source binding
now includes the phase README, written repair and round-two protocol.
At case entry, exhausted extension or candidate counters stop the case
before enumeration; this explains the two unstarted size-ten records.
Reproduction may rebind the input receipt hash only when all other frozen
specification fields agree. An original frozen file keeps its original
hash, while the embedded specification can identify a fresh input receipt.
No previous receipt is overwritten. These changes do not alter the raw
space or any of the three move relations.

## Independently checked obstruction to all three primitives

Use the already exposed development vector and the following one-tree
state:

\[
\begin{gathered}
 h=(3,6,6,6,7,7,7),\quad M=14,\\
 p=(2,5,5,5,7,7,0),\quad
 \alpha=(3,1,3),\quad r=3,\quad\epsilon=1.
\end{gathered}
\]

Its six tree edges are
`{1,2},{2,5},{3,5},{4,5},{5,7},{6,7}`. Each is a graph edge and
the parent labels increase, so this is an actual decreasing spanning
tree. The canonical word is `1,2,5,3,4,7,6`. Its graph inversions are
exactly `{3,5},{4,5},{6,7}`, hence

\[
 D=3+(3-1)+1=6\le\lfloor14/2\rfloor=7.
\]

The bounce contacts `0,3,6,7` establish height three. There are three
composition parts, one tree and epsilon one, so the sign is
`(-1)^(3-1+1)=-1`. Its type is the required `(3,3,1)`.

Every frozen primitive fails for a structural reason:

1. A mark step from epsilon one must increase the mark to preserve degree.
   The mark is already its maximum, three.
2. Word breaking removes the last part, three. Its proposed tail is
   `4,7,6`, already minimum-starting, so normalization has rank one and
   changes nothing. Reading `7` immediately after `4` requires the absent
   edge `{4,7}`, since `h(4)=6`. The decoded tail is invalid. One component
   leaves no component pair for a word join.
3. Cutting the parent edges at `1`, `2`, `3`, `4`, `5` or `6` detaches
   respectively `1`, `2`, `1`, `1`, `5` or `1` vertices. Thus every cut
   has side sizes `1/6` or `2/5`. The two composition boundaries of
   `(3,1,3)` require sizes `3/4` or `4/3`, even when their assignment order
   is reversed. No cut reaches a compatible composition assignment,
   regardless of mark compensation. One component also leaves no
   cross-component root-edge join.

Therefore this negative state is isolated in the **complete repaired
grammar**, independently of all four selectors and the diagnostic matching
algorithm. This is a written finite obstruction with computational
confirmation, not a Lean certificate. Seven is the smallest target size;
no globally minimal-Hessenberg-vector claim is made. The coefficient on
this development example is identically zero, independently checked in
round one, so the obstruction does not contradict the target conjecture.

## Completed, capped and unstarted evidence

All four development cases completed, with the same raw coefficient and
census as round one. Their coefficient comparisons reuse the saved,
coloring-checked round-one values; they are not fresh coloring calculations.
The old example still admits a finite grammar-constrained matching covering
its 258 negatives. The empty disjoint-clique example remains vacuous.
The other two development examples have complete-grammar isolates. Empty
coverage and failed cases were retained without replacement.

The four selectors have total development unpaired-negative counts
`2582,2458,5567,4565`. Selector `1` minimizes this count, but its lock
explicitly records `eligible=false`. It was then fixed for held-out work.
Every selector fails development; no best-score claim implies a working
construction. The changed primitive priorities also prevent treating all
same-numbered round-one and round-two selectors as identical comparators.

| Held-out vector | Supported scope |
| --- | --- |
| `(4,6,6,7,7,8,8,9,9)` | Complete raw forest census and complete move analysis; coefficient agrees with a complete tableau expansion, with no new coloring check. The repaired grammar has an isolate and the locked selector leaves 9,390 negatives unpaired. |
| `(4,4,4,8,8,9,9,9,9)` | Complete raw signed census and internal coefficient/reciprocity checks, then capped during move analysis. No completed move result, selector result or independent comparison is recorded. The case remains incomplete. |
| `(4,5,6,7,7,9,10,10,10,10)` | Candidate budget already exhausted; no enumeration or move work started. |
| `(2,7,7,8,9,9,9,10,10,10)` | Candidate budget already exhausted; no enumeration or move work started. |

The first held-out coefficient has lower-half differences
`0,0,0,0,0,0,0,2,7,8`. The second has internally computed differences
`0,0,0,0,0,0,1,4,7,6`, but that does not upgrade its capped case status
or supply its missing comparison. No conclusion is supported for either
size-ten coefficient. The completed held-out case is now exposed; even
partial execution of the second also makes it unsuitable as an untouched
holdout in future work. No held-out outcome chose this repair.

## Resource boundary and final assurance

The receipt records exactly 5,000,000 candidate charges, 292,909
extensions, approximately 14.041130 wall seconds, 13.400076 process seconds
and 200,196,096 bytes peak RSS. The per-case candidate and extension deltas
sum exactly to those totals. `Budget.tick` rejects the next charge at the
limit, so the final cap is not silently treated as an extra completed
candidate. Neither the time nor memory ceiling was reached. Reported RSS
is process peak memory, including a carried peak on unstarted cases; it
is not a separate allocation attributed to each case or an OS reservation.
The inspected ignored output directory held 449,090 bytes, below 250 MiB.
Frozen-specification regeneration, engineering tests and this review are
outside these research counters, as disclosed in round one.

There was one repair and no replacement or rerun after the cap. The
partial-relation proof is still useful, and the retained isolate decisively
explains why it cannot furnish the requested universal cancellation.
Neither finite matching nor nonnegative computed differences provide that
missing argument. The exact coefficient-unimodality target remains
conjectural and its novelty unverified. No universal theorem, new proof of
general positivity or new Lean formalization was achieved. The universal
argument gate for substantial Lean work remains unmet, and this two-round
phase is closed.
