# Height-three coefficient unimodality

P012 begins a new, user-authorized research phase from clean `main` at
`dce60269fca1774ea8d5600d30f62dbc39c927a4`, on branch
`codex/height-three-coefficient-unimodality`. Existing publications, failed
slides, the written two-sector cardinality obstruction, and Lean certificates
are preserved. The established Cho–Huh height-two theorem is not new mathematics.

Read the [frontier and written algebra](frontier.md), [results](results.md),
and separate [first](review-r1.md) and [second](review-r2.md) reviews.
The compact [finite evidence](evidence.json) and [execution record](execution.json)
bind the outcomes to saved sources, receipts and the actual manual stages.

## Exact target and assurance

**Conjecture; novelty unverified.** For every weakly increasing Hessenberg
vector `h`, `i <= h_i <= n`, whose poset `i <_P j iff h_i < j` has height exactly
three, and every `n >= 7`, put

`c(q) = [e_(n-4,3,1)] X_inc(P)(x;q)`, `M = |E(inc(P))|`.

Prove `c_d - c_(d-1) >= 0` for `0 <= d <= floor(M/2)`, with `c_(-1)=0`.
Established palindromicity then gives nonnegativity and unimodality. No proof
of this exact universal statement was found in the primary sources inspected
through 2026-10-23; this bounded search does not certify absence of prior work.
Only a theorem resolving an unresolved case satisfies the user's novelty gate.

The September 2026 general positivity result is reported with partial local
audit, not independently rebuilt here. It explicitly excludes elementary
unimodality. General positivity and Schur unimodality do not prove this target.
The [previous certificate audit](../evidence/external-certificate-audit.md)
remains unchanged.

## Preregistered experiment

The [program contract](../../../programs/partition-h3-unimodality.json) uses
the existing harness `pair` fleet. The lead develops the construction and a
separate critic reviews it; no nested agents. The harness planner checks role
separation and the 16 dispatch-unit ceiling (propose 3, challenge 2, revise 3
per round). Actual execution is manual, not an automated model backend.
Offline harness replay accepted six saved stage summaries; it validates their
response format and dependency flow, not the research claims or dispatch history.

Before construction searches, `protocol.json` freezes the eight SHA-256-ranked
development vectors at sizes 7 and 8, four prescribed held-out vectors at sizes
9 and 10, the three primitives and twelve selectors. All raw determinant tags
are retained. A first-difference state has sign `sgn(sigma)*(-1)^epsilon` and
effective degree `inv_G(T)+epsilon`, for `epsilon in {0,1}`. Only the lower
half is paired.

Primitives: same-word reblocking into a contributing shape; comparable-prefix
insertion and **all** valid candidate extractions that reinsert exactly; one
adjacent incomparable swap followed by reblocking. Every target must be a valid
tableau, have opposite sign and equal effective degree. Inversion-preserving
moves retain epsilon and reverse determinant sign. Swaps toggle epsilon and
retain determinant sign. Deterministic selectors use all six primitive priority
orders and first/last target in `(shape,sigma,rows,epsilon)` lexicographic order.
Only reciprocal choices pair. Isolated negative states obstruct the complete
grammar; failures of the twelve selectors alone do not.

Development chooses the selector with the smallest total number of unpaired
negative states, ties by selector ID. That selection is locked before held-out
evaluation. A capped development case makes selection ineligible for a success
claim. Held-out results are never used to tune that selector. Any later use is
disclosed as development exposure.

Two proposal/review rounds maximum. Each round has 600 computation seconds,
five million enumeration extensions and five million move candidates. Each
case has 120 seconds; one enumeration process, 2 GiB memory and 250 MiB artifacts.
Caps stop work and are recorded as incomplete. No replacement cases, new
dependencies, paid compute or external Lean rebuilds. Round two compares Tom's
complete forest-triple space if an isolated tableau state or certified Hall
deficiency is found; it does not silently enlarge the tableau grammar.

## Reproduction and acceptance

From the repository root, with Python 3.11+:

```sh
python3 -m harness validate
python3 -m harness plan programs/partition-h3-unimodality.json
python3 -m research.partitions.checks.height_three freeze
python3 -m research.partitions.checks.height_three run --round 1 --output .runs/h3-unimodality/r1.json
python3 -m research.partitions.checks.height_three forest --input .runs/h3-unimodality/r1.json --output .runs/h3-unimodality/r2.json
python3 -m unittest discover -s tests -v
python3 scripts/check_repository.py
```

`freeze` refuses to overwrite a different existing protocol. Execution checks
the protocol against the implemented grammar. Raw runs stay ignored; reviewed
small evidence belongs here. Resource counters include failed candidates and
coloring-oracle recursion. Peak RSS, elapsed/process time, source hashes and
cap reasons are recorded. These are exact finite checks, not universal proofs.

A credible universal argument must establish complete sector extraction,
validity, sign, statistic, inverse recovery and a survivor interpretation before
substantial Lean work. Final theorem acceptance additionally requires a bridge
to actual colorings, Lean checking without placeholders/custom axioms, and
separate semantic review. No such proof or new Lean certificate is claimed by
this experiment.
