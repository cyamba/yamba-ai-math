# RR006 sequence and primary-source survey

Initial survey stage, 24 October 2026 (UTC retrieval timestamps are in the
fresh `.runs/rr006/ledger.json`). This is a targeted discovery search, not an
exhaustive OEIS or novelty audit. **No OEIS sequence identification was
established.** All sequences below come from the saved, exposed RR005 record;
no new enumeration or above-12 mathematical input was executed by this branch.

**Follow-up status:** the authorized cross-search below subsequently inspected
A272397 and identified its definition with the **full literal B count only**.
The initial failures remain historical results; residual-root and distinct-B
identifications are still unestablished. This branch executed no mathematics.

## Frozen sequence provenance

Source: `illustrations/rr005-six-through30-result.json`, RR005 round 2,
ceiling 30. `T(n)` is its per-weight U count (identical saved C count),
`P(n)` its empty-F-root restricted count, `M(n)=T(n)-P(n)`, and `R_U(n)`,
`R_C(n)` count the corresponding saved F-root arrays. These are separate
definitions even where their saved terms agree. Each has integer-weight
indexing beginning at zero; the empty full object/root is counted once.
`M(0)=0`. Reading saved terms through 30 is discovery exposure, not a new
through-30 pilot, identification proof, or held-out evidence.

Preselected initial query families were total, covered, missing and residual
root counts, followed by a closest-construction topic query. A direct OEIS
retry of the total sequence consumed one additional string. No adaptive
sequence transformation was used to manufacture a familiar answer. The
fixed omitted zero prefixes and offsets below are explicit.

| Query | Exact string sent | Terms, offset and bound | Result / inspection |
| --- | --- | --- | --- |
| S-Q1 | `site:oeis.org "1,1,1,2,2,2,4,4,5,7,8,9,13"` | T, 13 terms n=0..12; T(0)=1 | Tool response: “Empty search results”; no hit. |
| S-Q2 | `site:oeis.org "1, 1, 1, 2, 2, 2, 4, 4, 4, 6, 6, 6, 9"` | P, 13 terms n=0..12; P(0)=1 | Search returned unrelated candidates below. No matching contiguous sequence accepted; no OEIS entry opened. |
| S-Q3 | `https://oeis.org/search?q=1%2C1%2C1%2C2%2C2%2C2%2C4%2C4%2C5%2C7%2C8%2C9%2C13&fmt=json` | Same T terms/offset; direct retry of S-Q1, not new data | Open failed: “URL ... is not accessible via this tool.” This consumed both a query string and a source open. |
| S-Q4 | `site:oeis.org "1,1,2,3,4,5,7,9,12,15,19,23,29"` | M, 13 terms n=8..20; omitted M(0)..M(7)=0 | “Empty search results”; no hit. Arithmetic subtraction of saved counts only. |
| S-Q5 | `site:oeis.org "1,0,1,0,1,0,0,1,1,1,1,1,2,1,1,1,3,2,2,3,3,3,4"` | R_U and R_C, 23 saved terms n=8..30; R(0)=1, R(1)..R(7)=0 omitted | “Empty search results”; no hit. Terms count saved root arrays, not descendants. |
| S-Q6 | `Kanade Russell first conjecture Andrews Keith Kursungoz bijection Ferrers partitions modulo 9` | Topic query, no sequence/offset | Located primary-source leads and a secondary apparent-status lead; only the inspected primary sources below support substantive statements. |

S-Q2 returned A355270, A347050, A372673, A097291, A243866,
A371929, A228584, A111798 (normal and internal-format results), and
A397576. These are **ambiguous/irrelevant search returns, not hits**.
For example, [A355270](https://oeis.org/A355270) has offset `1,5` and a
square-spiral adjacency definition; its displayed prefix begins with four
ones, while P begins with three. [A347050](https://oeis.org/A347050) has
offset `1,4`, a factorization definition, and its fifth displayed term is 1,
where P's fifth is 2. Other returned titles describe an Euler-phi array,
pair enumeration, tile positions, constants, a digit sieve or a table, rather
than this family. Definitions and offsets above were visible in search
responses; formulas/references were not independently inspected for a
candidate match because none was accepted. These returns cannot identify P.

The web search tool evidently did not enforce the quoted sequence as an
exact contiguous match in S-Q2. The no-hit results and inaccessible direct
endpoint therefore establish an **access/search limitation**, not absence
from OEIS. No OEIS ID, novelty conclusion or root algorithm follows.

## Source opens and depth

All opens were reserved before retrieval in the fresh ledger. Reinspection
using `find` is conservatively counted as an open. Initial usage: **6 query
strings, 7 source retrievals, 3 detailed records** (two substantive full-text
inspection records and one abstract-only lead). The follow-up allowance is
not spent by this initial stage.

| Open | Exact target / operation | Depth and result |
| --- | --- | --- |
| S-O1 | Direct OEIS JSON URL S-Q3 | Inaccessible error; no entry obtained. |
| S-O2 | <https://arxiv.org/html/1808.01432> | v1, 4 August 2018; definitions, marking and Theorem 7 proof setup inspected. |
| S-O3 | <https://arxiv.org/html/2203.05202v2> | v2; definitions, Stockhofe procedure, conjugate weighted geometry and references inspected. |
| S-O4 | <https://www.combinatorics.org/ojs/index.php/eljc/article/view/v26i1p6> | Metadata/abstract only, publication 11 January 2019; PDF link located. |
| S-O5 | Kurşungöz same URL, `open` at line 322 | Theorem 7 and forward/backward cluster discussion, including pair-phase changes and adjustments inspected; complete paper not audited. |
| S-O6 | Andrews–Keith same URL, `find` for `Theorem 6` | Exact weighted modulus-five theorem, adjacent further-work remarks and references inspected. Historical open-status wording is not current-status evidence. |
| S-O7 | Click PDF link 14 from S-O4 | PDF wrapper <https://www.combinatorics.org/ojs/index.php/eljc/article/view/v26i1p6/pdf>; response only links “Download PDF”/iframe. Full paper not obtained or inspected. |

The final <=6-open steering arrived after already-reserved S-O5/S-O6/S-O7
had completed; no eighth initial retrieval was made. S-O7 is preserved as
a depth/access failure, not reported as a full-paper inspection.

## Supported source facts and narrow clues

**S1, established source content, inspected construction scope.** Kurşungöz,
*Andrews-Gordon Type Series for Kanade-Russell Conjectures*, arXiv v1
(2018), §2 and §3 Theorem 7, gives the A-side cluster construction with
`a=n1`, `b=n2`, exact-length zero-padded mu and eta, eta divisible by 3,
and base weight `a^2+3ab+3b^2`. RR006's nu corresponds to eta/3. The
paper constructs the difference-side generating series, not the missing
B-to-C or F_U-to-F_C bijection. This inspection supports attribution and
the stated correspondence; it is not an independent full proof audit.
[Primary text](https://arxiv.org/html/1808.01432).

One useful clue is that **distinctness is not preserved by the established
cluster move itself**: its isolated adjacent pair `(3k+1,3k+2)` becomes
the repeated pair `(3k+3,3k+3)` in a weight-three forward move when the
listed context allows it. The smallest isolated case `(1,2)->(3,3)`
already crosses A-distinct/A-repeated. This is a source specialization,
not a newly implemented RR006 rule or a claimed weight-preserving A/B map.
Next falsifier for any proposed split is this smallest pair transition;
a split that treats all two-clusters as repeated parts fails immediately.
The unresolved task is to recover the phase/context intrinsically from
the opposite root representation. No claim about an equivalent U
statistic is established. This clue consumes no new rule-variant slot.

**S2, established source content, inspected endpoint scope.** Andrews–Keith,
*Schmidt-type theorems for partitions with uncounted parts*, arXiv
2203.05202v2 (2022), §§2–3 and §5 Theorem 6, uses conjugation and
Stockhofe's map. Its theorem equates residue parts 1,3,6,8 modulo nine
with partitions of multiplicity below five under periodic row weights
`(1,2,3,2,1)`. It does not provide the missing map to KR1 gap partitions.
The inspection includes the terminal drop in m-flatness and the claimed
inverse reconstruction mechanism; the full imported endpoint algorithm
has not been independently audited in this stage. The source's example
arithmetic already noted as inconsistent in the local source audit is
not adopted as evidence. [Primary text](https://arxiv.org/html/2203.05202v2).

The corresponding geometric clue is an exact **weight obligation**, not a
new map: decoded column height h has weight F(h), the partial sums of
that periodic pattern, so ordinary unweighted area need not be KR1
weight. Height two already has F(2)=3. A proposed lift whose only weight
is one unit per decoded cell fails there unless it explicitly changes
the cells/weights. Recoverable layers may re-express this known weighted
encoding; additional dimensions alone do not construct psi. The smallest
falsifier is the single height-two column. Remaining obligation: a
weight-preserving intrinsic root correspondence, including the old P/Q
collision and lost-phase contexts. This clue consumes no rule slot.

**S3, unverified applicability, abstract-only.** Kanade–Russell,
*Staircases to Analytic Sum-Sides for Many New Integer Partition Identities
of Rogers-Ramanujan Type* (2019), DOI 10.37236/7847, advertises staircase
and jagged-partition techniques for analytic sum sides. Only metadata and
abstract were inspected; the PDF wrapper did not expose the paper.
No formula, inverse, geometric rule or connection to the RR005 residual
grammar is imported from it. It remains a next-reading lead rather than
a third retained construction direction.
[Primary landing page](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v26i1p6).

Novelty remains **NOT VERIFIED**. Strongest competing explanation for any
apparent geometric advance is repackaging the existing periodic weighted
conjugate/cluster encodings while leaving their cross-domain root map
unresolved. The initial survey supplies two narrow constraints/clues,
zero identified OEIS sequences, zero new candidate algorithms and zero
finite mathematical executions. It neither changes closed RR003–RR005
ledgers nor claims full KR1 success.

Questions for the construction branches: can a proposed phase statistic
be computed from the actual U root without a saved trace, and can an
admissible weighted layer description distinguish every currently
unmatched root rather than merely preserve its weight?

## Operational record

Read-only file utilities before the handoff took approximately 13 seconds
of reported command wall time, plus administrative ledger writes. Two
failed reads are preserved: an `rg` with two nonexistent named source
paths (partial output still returned), and a zsh no-match on
`research/rogers-ramanujan/rr004/source*`. Neither executed mathematics.
No analysis subprocess, dependency, provider, external message, OEIS
submission or repository functional change was used. Model/runtime/token
measurements unavailable to this branch are unknown. This branch awaits
the authorized cross-search stage and does not self-start it.

## Authorized cross-search follow-up

Dependencies inspected before retrieval: [family census](family-census.md)
and [geometric study](ferrers-layers.md). The census's finite rows through30
followed its passing frozen pilot through12 and root-authorized unchanged
extension. Their use here reads already produced discovery data; this scout
did not regenerate them. New family proofs and G1–G5 retain author-only
assurance until the RR006 critic. The literal weight-two distinctness
obstruction does not depend on the author-only endpoint implementation.

The follow-up was preselected as: (i) one exact residual-root spacing retry,
(ii) one definition search for the census's literal B-distinct refinement,
and (iii) a closest-method search for flat/regular weighted words with
recoverable phase. No numerical transformation or new term generation.

| Query | Exact string sent | Terms, indexing and purpose | Result |
| --- | --- | --- | --- |
| X-Q1 | `site:oeis.org "1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 2, 1, 1, 1, 3, 2, 2, 3, 3, 3, 4"` | Same23 R_U/R_C terms n=8..30 as S-Q5, spacing-only retry; R(0)=1 and R(1)..R(7)=0 explicitly omitted. Census confirms saved terms. | Returned unrelated OEIS/wiki material; no contiguous/definitional root match accepted. A023416 is binary-zero counting, for example, and differs at the fifth listed term. No entry opened for these returns. |
| X-Q2 | `site:oeis.org partitions distinct parts 1 3 6 8 modulo 9` | Literal B-distinct totals n=0..30 were fixed before search: `1,1,0,1,1,0,1,1,1,2,2,2,2,2,2,3,3,3,5,5,4,6,6,5,7,8,8,10,11,11,13`; empty contributes1, no transform. Search uses the definition rather than the term list. | Returned A272397, whose full-B definition is relevant to the total sequence T, **not** the queried distinct refinement. Also A114098, whose distinct-modulo-nine definition is different. No distinct-B ID accepted. |
| X-Q3 | `"Kanade Russell" "weighted words" "flat partitions"` | Topic query from S2 reference9, periodic lift and F_C contextual terminal grammar; no sequence/offset. | Mixed, mostly irrelevant responses; no new KR1 root method established by search. The directly cited primary Konan reference was inspected below instead of importing search summaries. |

The unrelated X-Q1 returns included A099245, A368948, A141803, A023416,
A242235, A363622, A000931's Padovan note and OEIS wiki pages on fractions,
ternary notation and a constant. They are preserved in the raw tool response.
The exact terms were not treated as an enforced search constraint. This is
another search failure, not evidence that a root sequence has no OEIS entry.

| Open | Target and inspection | Result / boundary |
| --- | --- | --- |
| X-O1 | <https://oeis.org/A272397> | Entire entry inspected: definition, offset `0,4`, listed terms, comment, examples, Mathematica enumeration, author and reference. No separate FORMULA section is present. |
| X-O2 | <https://arxiv.org/html/2002.00300v2> | Konan v2,20May2021: grounded/colored partition definitions and introduction inspected. |
| X-O3 | Same Konan URL, `find Theorem 2.8` | Exact theorem, ground-energy equations, color-sequence preservation and nearby degree-two statement inspected. |
| X-O4 | Same URL, `open` at line250 | Definition2.1 verified minimal energy has values in `{0,1}`; theorem's applicable scope narrowed accordingly. Full bijective proof not audited. |

**S4, established identification by definition, finite diagnostic agreement.**
[A272397](https://oeis.org/A272397), Matthew C. Russell,28April2016,
defines exactly the literal full B count; offset `0,4` means n starts at0
and the second offset field is OEIS metadata, not a weight shift. Its listed
terms agree with saved T through30, including the empty term1. This is an
identification of B by the entry's definition, with finite agreement as a
diagnostic; it is not a proof that U/C or A are equinumerous, a construction,
or a root/refinement identification. Published entry terms above30 were
incidentally visible but not newly generated or checked here. The sole
paper reference is Kanade–Russell's *IdentityFinder and some new identities
of Rogers-Ramanujan type* (2015); that reference was located but not opened.
The relevant Kurşungöz and Andrews–Keith constructions were inspected as
S1/S2. The entry's historical conjecture comment is not used to assess
current theorem status. Its enumeration program was read, never run.

**S5, established inspected theorem statement; KR1 application unverified.**
Konan, *Weighted words at degree two, II: flat partitions, regular
partitions, and application to level one perfect crystals*,
[arXiv2002.00300v2](https://arxiv.org/html/2002.00300v2),20May2021,
defines grounded colored partitions with a terminal zero ground and
minimal energy `epsilon:C^2->{0,1}`. In Theorem2.8, subject to its ground
conditions `epsilon(g,g)=0` and
`epsilon(g,c)=delta=1-epsilon(c,g)` with fixed `delta in{0,1}`, its map
preserves total energy and the non-ground color sequence between the
specified flat/regular domains. The inspected HTML prints the condition's
quantifier as `c != 0`; a specialization must reconcile the ground
notation with the paper, rather than silently broaden it. The theorem
statement and definitions were inspected; its full proof and a KR1
specialization were **not** audited. The degree-two theorem likewise
cannot be treated as a free parser for arbitrary cluster data.

The exact missing specialization lemma is: specify a **finite** color set,
ground, allowed minimal-energy matrix and a common size specialization;
give canonical reversible encodings of all F_U and all F_C roots into
the theorem's two domains; prove their images are carried onto one another
by its map, their colors are recoverable from undecorated roots, the empty
ground and all terminal restrictions are correct, and the common
specialization equals each literal root's KR1 weight. None of those
encoding/image equalities is presently constructed. F_C's repeated terminal
coordinates and preceding mu-gap bound0..2 do not themselves establish
an allowed energy matrix or color-word correspondence. RR004's obstruction
to fixed adjacent-height charges for b remains in force, so identifying b
with an unproved color count is not permitted. The smallest exposed seed
checks would involve roots at8,10,12, but even success there leaves universal
coverage and both inverse obligations. This is a bounded next-reading/
specialization lead, not psi or a new rule variant.

The literal weight-two obstruction A=(2), B=(1,1) from G4, the source's
cluster-phase crossing, and the census's successful/missing families show
why a context-sensitive invariant is needed. The periodic-weight lift is
lossless but adds no recoverable branch data. None of S4/S5 resolves that
gap. The three consolidated clues and old failures are retained in
[clues-and-rules.md](clues-and-rules.md), with their separate assurance.

**Final scout accounting:** initial6queries/7retrievals plus follow-up
3queries/4retrievals = **9query strings,11source retrievals,5detailed source
records**. Three query strings and seven source retrievals remain globally
before any further root/critic retrieval, subject to their own reservations;
unused resources do not reopen discovery. Follow-up read-only file utility
wall time was1.2seconds; cumulative read utilities approximately14.2seconds,
plus separately recorded administrative ledger writes. No new analysis
subprocess, enumeration, code, map variant or external message. Raw outputs
are in `.runs/rr006/cross-search-raw-retrieval.json`; all queries/opens were
reserved in the fresh ledger. This closes the scout's discovery work.
