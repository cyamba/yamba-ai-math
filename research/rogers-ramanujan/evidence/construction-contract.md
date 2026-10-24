# RR002 construction contract

Status: **stopped after two reviewed rounds**, mathematical bridge
**unresolved**. See the [construction result](construction-result.md).
Authorized by the
user's implementation request. Start 2026-10-23 21:56:48 UTC; hard deadline
23:26:48 UTC, including review and tests. Base commit
`a7834f156ea31d3e7f6f2e8893eb8d2f76029889`.

## Actual sets

All weights N are natural numbers; the empty object has weight zero.

* A: ascending positive partitions, distance-two gap at least three;
  adjacent gap at most one implies pair sum divisible by three.
* B: positive partitions with residues 1,3,6,8 modulo nine.
* W: descending positive partitions, multiplicities at most four, with
  positional weights 1,2,3,2,1 repeated starting at position one. Its
  ordinary size need not be N.
* C: (a,b,mu,nu), ascending nonnegative vectors of exact lengths a,b,
  counting zeros, with N=a*a+3*a*b+3*b*b+sum(mu)+3*sum(nu).

## Rule and resource boundary

The intended new bridge is W <-> C. Permitted candidate constructions use
finitely many uniform Ferrers column and singleton/pair cluster moves,
arithmetic shifts with all costs charged, and reconstructible auxiliary
state. Freeze a candidate before testing it. Specify rule priority, scan
order, termination measure, inverse and auxiliary units. No whole-set
enumeration, rank matching, equal-count premise or hidden lookup table may
define the final map. Enumeration may falsify proposals only.

Initial algorithm target: O((N+1)^4) elementary bit/box operations and
O((N+1)^2) auxiliary bits, including scans and arithmetic. A candidate
exceeding it is recorded separately, not quietly admitted. Empirical move
ceiling: 10,000*(N+1)^4. Timeout is inconclusive. Confluence is required
only for a claim of order independence; it does not imply invertibility.

Use Std Python, installed Lean 4.34.1, and existing compatible dependencies.
No new provider, bulk cache download, user-file deletion or publishing.
Enumeration: pilot N<=12, then N<=30, ten cumulative minutes, 2 GiB RAM.
Incremental storage <=1 GiB; provisioning floor 5 GiB free. No full Lean
proof increment or illustrated article until the new bridge passes review.

## Execution and accounting

Manual execution of the validated `pair` DAG: root as author/mathematician,
`/root/rr_plan_critic` as critic. Each round is propose (3), challenge (2),
revise (3); two rounds, 16 declared dispatch proxies. These are not tokens,
money or measured quality. Root's coordinating work, source retrieval,
tool calls, testing, builds and elapsed time are recorded separately.
There is no configured external adapter and no automated research run.

Handoffs: frozen round proposal -> critic findings -> author revision,
with exact predicates, algorithm or restricted claim, counterexamples,
proof obligations and run results. Two profiles; no nested agents. A
manual result is recorded only after the actual work returns.

Stop with a useful obstruction or explicit unresolved obligation when
the deadline or two-round cap is reached. Do not relax proof standards.
