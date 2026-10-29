# Session decision log

One line per workflow decision, newest last: how the work was organized, not what was proved.
Before deciding, read only the last ten lines; after deciding, append one. Details stay in the linked
research or meta file. Never record benchmark scores, rubric text or mathematical claims here.

Format: `- YYYY-MM-DD | who | math or framework | decision | why: <path or event> | check: <observable signal>`.
When the check can be judged, append ` -> kept (YYYY-MM-DD)` or ` -> reverted (YYYY-MM-DD): <reason>`.
Keep at most 40 entries and 300 characters per entry; move closed entries out to
`meta/session-log-archive.md`. A decision reverted twice, or a difficulty seen in several sessions,
is input for the improve-harness skill.

## Entries

- 2026-10-29 | claude | framework | Pin the KR1 target (TARGET.md, program target hash); proved claims declare target_relation and scope_delta | why: novelty_radar/NR-001 added-assumption failures | check: restricted claims are labeled at freeze, not found later in review
- 2026-10-29 | claude | framework | Stalled obligation: smallest-case falsifier first, then decomposer with a reviewed glue argument before sub-lemmas | why: NR-001 replanning; KR1 lead obligation open since RR003 | check: the next stall yields a reviewed glue argument
- 2026-10-29 | claude | framework | Add conjecturer role and discover fleet | why: no registered role generates conjectures | check: a discover run returns two or more mechanism families, killed ones with witnesses
- 2026-10-29 | claude | framework | Start this one-line log; reflect-before-run, regroup and pivot read ten lines and append one | why: only meta/change-ledger.md recorded decisions | check: after three sessions entries are closed and the log stays under 40 lines
