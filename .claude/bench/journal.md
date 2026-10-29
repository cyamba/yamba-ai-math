# Benchmark journal

Operator-only, one line per decision about the instrument itself: spec changes, relevance reviews,
defects. Newest last; keep it under 30 lines and move older lines into the spec's `relevance_review`
reasons or git history. Never copy lines, scores or rubric text into research files.

- 2026-10-29 | spec 2026.10.29-1 | Retired B04, B10; added B13 novel contribution, B14 idea generation; B03 strawman cap; B05 statement fidelity; B01 n/a formal rungs | why: process axes saturated while discovery stayed low; no axis measured new mathematics
- 2026-10-29 | engine | Fixed CRLF snapshots, unknown counted as failure (B04 cap, B07 reproduction), hard-coded review glob, collect abort without recorder, Windows path scrub | why: verified by re-collecting h3 on Windows
- 2026-10-29 | relevance | Added `bench.py relevance` and the spec's scheduled review (3 records or 2027-01-31) | why: the instrument never questioned its own axes
