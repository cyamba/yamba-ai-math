# P015 first formal review: valid exchange relation, missing universal pivot

Date: 2026-10-24. Reviewer: separate `critic` role, implemented by
`frontier_critic`. This is the first of exactly two planned P015 critic
calls, with no preliminary critic dispatch. The filled handoff
`.runs/h3-forest-exchange/manual-handoffs/r1--challenge.json`, program,
phase specifications, implementation, executed source snapshot and actual
round-one receipt were inspected. This reviewer ran no research enumeration,
tests or Lean, used no nested agents, and edited only this review. Hashing
and reading saved records do not constitute a research rerun.

**Verdict: incomplete universal construction; supported conditional
exchange involutions and adjacent-defect formula; refuted four fixed
selectors.** More strongly, the sole all-pairs repair cannot make any of
those selectors perfect: their retained degree-zero failures cannot gain
an exchange neighbor. Finite grammar saturation survives this objection;
no Hall obstruction to the enlarged P015 grammar has been established.

The exact unresolved target remains: for every natural unit interval
poset of height exactly three on `n>=7` vertices, with
`c_h(q)=[e_(n-4,3,1)] X_inc(P_h)(x;q)` and `M=|E|`, prove
`[q^d] (1-q)c_h(q)>=0` for `0<=d<=floor(M/2)`. The signed states are the
complete Tom forest triples with ordered compositions of that sorted
type, marks `1<=r_i<=alpha_i[0]`, and epsilon zero or one. Sign is
`(-1)^(3-m+epsilon)` and effective degree is
`D=inv_G(word)+sum_i(r_i-1)+epsilon`. This target is **conjectural** in
the bounded audited record. The expansion and tree-word definitions are
**established** mathematics from [Tom v2](https://arxiv.org/html/2311.08020v2),
Definitions 3.1/3.3, Theorem 3.4 and Lemma 3.11, inspected during this
continuous investigation. Novelty of the target and of the exchange
construction remains **unverified**.

## 1. High priority: the predeclared repair cannot fix the selector failures

**Target claim:** a universal covering pivot, or a development-perfect
member of the four frozen reciprocal selectors after the all-pairs repair.
**Status:** the universal pivot is incomplete; all four specified selectors
are refuted, and the repair cannot remove their displayed failures.

This has a short written proof, independent of any larger search. Every
term in `D=I+sum(r_i-1)+epsilon` is nonnegative. Thus degree zero forces
`I=0`, every mark one and epsilon zero. Every exchange toggles epsilon
to one while leaving marks unchanged, so any actual destination has
degree at least one. There are **no degree-zero exchange neighbors for
any pair of labels**, adjacent or arbitrary. Consequently the all-pairs
repair leaves the entire degree-zero neighbor graph and every selector
choice on it unchanged, including choices at the positive destinations.

All four saved first failures on `h=(2,4,4,6,7,7,7)` have degree zero.
The following table records their source, chosen target and chosen reverse.
Every omitted mark is one; every epsilon and inversion is zero.

| Symbol | Parent vector | Ordered compositions |
| --- | --- | --- |
| `A` | `(2,3,0,5,6,7,0)` | `((3),(3,1))` |
| `A'` | `(2,3,0,5,6,7,0)` | `((3),(1,3))` |
| `B` | `(0,3,4,5,6,7,0)` | `((1),(3,3))` |
| `C` | `(2,3,4,0,6,7,0)` | `((1,3),(3))` |
| `P` | `(2,3,0,0,6,7,0)` | `((3),(1),(3))` |
| `Q` | `(2,3,4,5,6,7,0)` | `((3,3,1))` |
| `R` | `(2,3,4,5,6,0,0)` | `((3,3),(1))` |
| `U` | `(0,3,4,0,6,7,0)` | `((1),(3),(3))` |

The recorded selector arrows are `0: A -> P -> A'`,
`1: B -> Q -> R`, `2: C -> U -> B`, and `3: B -> U -> C`.
All parent edges are allowed consecutive edges, their component words
concatenate to `1234567`, and their type is `(3,3,1)`. The sources and
reverses have two components and negative sign; the targets have one or
three components and positive sign. These are genuine nonreciprocal
choices, not isolated states or failed representation checks. The first
selector also sends the two distinct composition orders `A,A'` to `P`,
illustrating the unresolved loss of inverse choice.

**Impact:** merely adding distant transpositions cannot produce a perfect
selector or unlock held-out evaluation under this contract. This does not
refute existence of a different matching in the full grammar; the saved
graphs all saturate their negatives. A substantive universal pivot must
coordinate composition splitting/joining even where exchanges cannot act,
and make the chosen move recoverable at its destination.

**Decisive next check:** in round two, verify these same degree-zero
selector failures under the frozen all-pairs rule. A narrow verification
would already settle the selector-acceptance question; any broader
all-pairs census remains a finite grammar diagnostic. Do not add another
selector or move in this phase to bypass the obstruction. A claimed
degree-zero exchange would falsify this review only by exhibiting a
negative inversion/mark contribution or changing the stated statistic.

## 2. Conditional relation supported: payloads must move with vertex sets

**Target claim:** each fixed transposition is a type-preserving,
sign-reversing, degree-preserving partial involution. **Severity:** a
necessary proof-scope condition, not an implementation defect.
**Status:** proved by the following written argument; not Lean.

Let `tau=(a b)` with the labels in different components. The relabelled
parent function is `p'(tau(u))=tau(p(u))`, with `tau(0)=0`. Carry the
whole ordered composition and mark of each component `A` to `tau(A)`.
The component sets remain disjoint, their sizes remain fixed, and their
payloads satisfy the same composition sizes and first-part mark bounds.
Reordering the resulting components by their new minima changes only
their list positions, not those payload associations. The code implements
this through a dictionary keyed by transported vertex sets and then
`Geometry.build`, rather than attaching payloads by old component index.

Rejecting non-increasing or absent graph parents is essential: arbitrary
label exchange is not automatically a graph automorphism. Accepted
parents define the same number of decreasing trees. Toggling epsilon
therefore reverses sign while leaving the sorted composition type fixed.
The full statistic filter imposes exact degree equality. Applying the
same transposition twice restores every parent, transported component
payload and epsilon. The two labels remain in different components;
actual validity and equality of degree are symmetric conditions. Hence
the reverse is accepted and restores the source exactly. No assertion
about canonical words commuting with an arbitrary transposition is needed
for this inverse proof.

The motivating `(2 3)` calculation correctly gives parents
`(2,4,5,6,7,0,8,0)`, component words `1246`, `3578`, inversions `34,56`
and epsilon one. Each source inversion was three, so effective degree
remains three. The two distinct ordered composition tuples remain
distinct at the targets and are recovered by the same exchange.

**Impact:** fixed-pair recovery is sound, including when minima reorder.
It does not imply recovery of a state-dependent *choice* of transposition
or primitive. Several fixed involutions can still compete at a state.
**Decisive obligation:** a future pivot must prove that applying its chosen
move makes the reverse pivot select the same source; proving each
fixed-pair inverse again does not discharge this obligation.

## 3. Adjacent defect supported, with its component-order hypothesis retained

**Target claim:** for adjacent labels with stable transported component
order, `Delta I=s(e-B)`, including non-twins. **Severity:** medium if
used outside that hypothesis. **Status:** proved conditionally by pair
accounting; not a new theorem claim or Lean certificate.

Because the adjacent labels occupy different components, relabelling is
order-preserving within either component. Its canonical tree word is
therefore the relabelled old word. Stable component order then makes
the full new word exactly `tau(w)`. Pairs not incident to the two labels
are unchanged. Their mutual edge contributes `s*e`. For `k<a`, the only
distinguishing adjacency is to `a` but not `b`, exactly when `h(k)=a`.
For `k>b`, the only distinguishing adjacency is to `b` but not `a`,
exactly when `h(a)<k<=h(b)`. Each such label between the two word
positions contributes `-s`; outside those positions it contributes zero.
Common neighbors cancel in the difference. This exhausts the pairs and
proves the formula for non-twins as well.

The degree condition is `s(e-B)=2*epsilon-1`. Thus true twins with stable
component order have `B=0,e=1` and require `s=2*epsilon-1`. For non-twins,
an edge with `B=1` gives zero inversion change and cannot compensate
epsilon; larger defects can also exclude a move. The implemented exchange
uses the complete statistic rather than assuming the twin case covers all
eligible candidates. The `adjacent_defect` helper itself is a word-statistic
calculation, not an independent proof that a relabelled forest is valid.

The component-order condition cannot be dropped even for true twins.
On the retained eight-vertex graph, parents `(0,4,5,6,7,0,8,0)`,
compositions `((1),(3),(4))` and marks all one have word `1|246|3578`
and inversion two (`34,56`). Labels `2,3` are true twins. Exchanging
them gives valid parents `(0,5,4,6,7,0,8,0)`, but the last two component
minima reorder: the new word is `1|2578|346`, with inversion four
(`35,45,47,67`). The payload order becomes `((1),(4),(3))`.
The inversion change is two, not the stable-order value one, so this
graph-valid exchange is rejected by the effective-degree filter for
either epsilon. This hand example lies in the actual type `(4,3,1)`
space; it is not an extra search.

**Impact:** no false symmetry is imposed by the present implementation.
**Decisive obligation:** keep the full actual-word statistic for reordered
minima and arbitrary pairs in round two. Any proposed formula replacing
that filter must explicitly account for component permutations and
non-order-preserving tree relabellings.

## 4. Finite evidence supported; universal coverage and novelty remain unverified

**Target claim:** complete development grammar saturation and coefficient
agreement. **Severity:** high only if promoted to a universal result.
**Status:** exact finite computation, with the scope below.

The unchanged complete forest enumeration retains all forests, ordered
composition assignments, marks and epsilon states before lower-half
restriction; it checks the full raw coefficient, the first-difference
identity, palindromicity and duplicate freedom. Every generated neighbor
was checked against that complete state universe for sign and effective
degree, then for reverse membership in the same primitive group.

| Development vector | Raw triples | Doubled lower-half states | Negatives matched by grammar | Four selectors' unpaired counts |
| --- | ---: | ---: | ---: | --- |
| `(2,4,4,6,7,7,7)` | 320 | 519 | 258 | `141,178,108,109` |
| `(3,6,6,6,7,7,7)` | 2,352 | 4,182 | 2,091 | `1166,1167,916,910` |
| `(3,3,4,6,6,7,8,8)` | 480 | 726 | 358 | `224,237,151,151` |
| `(3,5,5,7,7,7,8,8)` | 5,024 | 8,976 | 4,485 | `2701,2493,1912,1900` |

All four grammar graphs saturate their negatives, and the old Hall subset
has two distinct exact exchange partners. None of these is an explanatory
covering rule. The aggregate selector scores are `4232,4075,3087,3070`;
selector three is merely the least failing candidate, with eligibility
false. No selector is locked. Both fresh held-outs remain unrun:
`(5,5,5,5,6,7,8,9,9)` and `(6,8,9,9,9,9,9,10,10,10)`.

All four P015 coefficient comparisons explicitly reuse completed
coloring-checked P014 evidence. There is no fresh coloring calculation or
fresh boundary tableau enumeration in P015. The coefficients are
`q^3(1+q)^3`, zero, `q^2(1+q)^5` and `q^5(1+q)^4`, respectively.
The n=8 exceptional 32-tableau sector is retained upstream, not silently
omitted or independently reverified by this run. These four familiar
development cases are not fresh independent evidence for the universal
target. No inspected source or computation settles exhaustive novelty
against previous exchange constructions.

**Impact and decisive obligation:** a credible universal argument still
needs existence of a recoverable pivot and positive survivors across all
states, including the degree-zero composition-choice conflict. Closest
prior label-exchange work must be inspected before claiming novelty.
The actual-coloring bridge and separate semantic acceptance remain gates
before substantial Lean; finite matching cannot replace them.

## 5. Provenance and research budgets verified within their stated accounting

**Target claim:** a source-bound, bounded first-round execution preserving
earlier work. **Severity:** informational accounting boundary.
**Status:** verified saved provenance, not proof-checker assurance.

The repository and current branch were read: origin is
`https://github.com/cyamba/yamba-ai-math.git`, branch
`codex/height-three-coefficient-unimodality`, base
`a0c897fb7bcb0d01a9ccff5593c0471424255b96`. All 174 hashes in
`upstream.json` agree with the current protected files, including P014,
publication, Lean and the failure ledger. All receipt source hashes agree
with both `r1-source/` and the current files. Relevant bindings are:

| Artifact | SHA-256 |
| --- | --- |
| Actual R1 receipt | `e2048852a9befc4f5dbac7ff34fe410ae2fe40a433ac9434995659f8bf228690` |
| Executed `forest_exchange.py` | `edccd5c0756b52c9e7987c1e00b6b4cb7bfb56dbbdcc0e8cb1b112b9edd47364` |
| Frozen protocol | `c3261f3fa3bf9c5ddc0e8d93c1341998ffae17b82df1c830d3206bfcf35f66e0` |
| Phase README | `b80b235afd410d154f0fdbf7e2c01937ead23aac93ea13d50148cf82339afdc6` |
| P015 program | `9a2a9b16e38c5dab516c3f54f872d9444cc7d9f34a5c33c4c522e18cd5417aa1` |
| Upstream preservation inventory | `e6cc738f99102489804f8e21770e737875dd4d50fb1290de1100a6d580cd91d7` |
| Inherited P014 evidence | `31d3e6f59b033b1e2cbbf1fc81d7c7601476164acd69357e3f3481b6608435e0` |

R1 completed all four cases without caps: 229,926 extension charges,
1,635,171 candidate charges, 3.1159076 wall seconds, 3.056602 process
seconds and sampled peak RSS 64,946,176 bytes. Exchange attempts are
charged before validation; inverse-membership checks and diagnostic
matching traversals are also charged. The inspected output directory,
including the source snapshot and manual handoffs, was 601,073 bytes.
The snapshot routine prospectively charges its copied bytes against the
same aggregate directory limit; report writes also check prospective total
size. The limits remain 600 computation seconds, five million extensions
and candidates per round, 120 seconds per case, one research process,
sampled 2 GiB RSS and 250 MiB output-directory bytes. RSS sampling and the
artifact guard are not OS reservations or quotas.

Input/protocol preparation, source snapshots and this semantic review are
outside the research counters; the receipt does not claim total session
cost. The program plans six formal stages at 16 dispatch proxies, with
this challenge assigned two. That plan or a filled handoff is not itself
an executed research result, token measurement or monetary total. No
pre-contract critic dispatch was used in P015. One final formal review
and at most the recorded all-pairs repair remain; there is no authority
for another feedback turn, third repair or unearned held-out evaluation.

**Decisive next check:** bind any round-two verification or census to the
preserved R1 receipt and one recorded repair, preserve all failures, and
report selector ineligibility separately from grammar saturation. The
written degree-zero obstruction already predicts that held-outs remain
unrun under the current four-selector contract. P015 has not established
a new unresolved theorem, a universal covering construction or a new Lean
certificate.
