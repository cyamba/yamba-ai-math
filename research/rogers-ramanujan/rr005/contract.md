# RR005 bounded execution contract — 2026-10-24

Authorized by the user's attached RR005 prompt and explicit reply selecting
execution. Base: fetched `origin/main`, `98de713`; branch `codex/kr1-rr005`,
isolated worktree `/private/tmp/yamba-ai-math-rr005`. The old research checkout
is clean and untouched. Exact start and deadlines: [execution.json](execution.json).
Preparation is conservatively charged twenty minutes; execution has at most
100 further minutes, for a total ceiling of 120 minutes.

## Objective and obligations

Construct explicit weight-preserving mutually inverse algorithms between
partitions with residues 1,3,6,8 modulo 9 and ascending positive partitions
with distance-two gap at least three and adjacent difference at most one
implying pair sum divisible by three. Include the empty partition.
Require universal domain validity, weight, termination, both inverse
identities, executable full endpoint composition and separate semantic review.
Lean certification and exposition remain subsequent obligations.
**Complete KR1 is unresolved; novelty is NOT VERIFIED.** Preserve attribution.

Keep U–C leading. Seek a disjoint exhaustive intrinsic decomposition on the
literal U domain: descending columns F(h), F(5q+r)=9q+(0,1,3,6,8)[r],
with all decoded drops, including the terminal drop to zero, in {0,...,4}.
Return nonnegative integers a,b and ascending nonnegative exact-length
zero-padded vectors mu,nu, with weight

    |U| = a*a + 3*a*b + 3*b*b + |mu| + 3*|nu|.

Specify recoverable context, extraction, reconstruction, invariant,
decreasing measure and universal coverage. Do not assume the extra context
exists. Do not overlay old partial images. RR003 author-only components
need separate audit before reliance. RR004 excludes fixed signed adjacent
height-transition sums for b, not every contextual decomposition.

## Limits and stages

Caps: preparation 20 minutes, discovery 40, computation 15, review/revision
30, closing 15. Stop discovery by its recorded deadline; if intrinsic
recovery/coverage is absent, freeze the precise gap or obstruction for review.
These are ceilings; no artificial waiting or automatic extension.

At most two profiles: root as author/mathematician and one distinct critic.
Sequential mathematical stages; two propose(3)/challenge(2)/revise(3)
rounds at most, total 16 dispatch proxies, no nested agents. Critic is a
separate profile, not a claim of independent errors. A manual stage counts
only when actually performed. Freeze claims and dependencies before checks.

Cumulative local computation <=600 seconds including critic and engineering
checks; child peak RSS <=2 GiB, incremental storage <=1 GiB and free-space
floor 5 GiB. Fresh ledger: `.runs/rr005/enumeration-ledger.json`. Use the
attempt-only `rr005_meter.py`; never reset or extend earlier ledgers.
Sixty computational seconds conservatively cover bootstrap and routine
maintenance; measured children are charged in addition. Record extra
maintenance charges if needed. The copied meter checks child RSS and
artifact size after exit, not an OS memory reservation or a hard transient
storage bound. Model RAM/runtime and Git metadata are not metered; include
worktree allocation and bytecode in closing storage accounting.

Preferred map bounds: quartic unary work and quadratic auxiliary bits,
including context reconstruction. Do not silently relax a binding cap.
No new dependencies, providers, paid tools, push, publication, external
messages or deletion of user files. No general harness changes.

## Verification and closing

Inverse/coverage argument before broad implementation. Pilot a frozen map
through weight 12; extend at most to 30 only if it passes. Check literal
domains, weight, collisions, missing images, both round trips, empty input,
zero increments, repetitions and terminal boundaries. Exposed cases are
discovery evidence. Counting, rank matching, hidden lookup, finite agreement
and model agreement cannot define or certify the final bijection.

Separate criticism audits final reusable claims. Substantive revisions
need the second review; after it, narrow or preserve unresolved claims.
Run repository unittest discovery and `scripts/check_repository.py` after
functional changes. Close at any binding cap with exact statuses, resource
use, review scope, failures/disagreement and the next unresolved lemma.
Earlier ledgers and evidence remain unchanged. Human feedback remains
PENDING unless actually returned; do not inspect Drive automatically.
