# Instructions for understanding work

This folder explains, illustrates and teaches mathematics that exists elsewhere in the
repository or in cited sources. It does not establish new results. Preserve that distinction in
every edit. The entry point is [SKILL.md](SKILL.md).

- **Status first.** Every explainer, answer or chapter starts with the status and source of what
  it explains, using the repository labels (`established`, `proved`, `conjecture`, `empirical`,
  `unverified`, `refuted`) and inspection levels (A, T, P) from `references/reading-list.md`.
  Generated or external results default to `unverified`.
- **Never upgrade.** A clear explanation, a convincing picture, agreement on examples or a
  finite computation does not make a claim proved. Heuristics stay labeled as heuristics.
- **Verified examples only.** Numbers, tables and figures come from code that implements the
  definitions, kept beside the output (`examples.py`, `figures/make_*.py`) with the command that
  reproduces them and the range that was checked. Prefer the Python standard library and exact
  arithmetic.
- **Faithful statements.** Quote definitions and statements exactly where precision matters, with
  every quantifier and hypothesis. Simplifications must say what they drop.
- **Route findings.** Suspected errors, gaps and new ideas go to the owning research folder, the
  `audit-theorem` workflow, an `explore/` proposal (with authorization) or the novelty radar.
  Do not fix research files from here.
- **Sources.** Cite primary sources next to claims. A source that a research file will rely on
  needs a reading-list entry. Paraphrase rather than reproduce third-party text.
- **Prose.** Follow the no-em-dash rule (`.agents/skills/no-em-dash/SKILL.md`) in all authored
  text, titles, captions and alt text. Keep skills operator-neutral: no personal names or private
  locations.
- **Outputs.** Durable explainers live in `explainers/<slug>/` (create on first use, with a
  `README.md` explainer and its scripts) unless they belong to a project's paper or publication
  folder under that project's own instructions.
- **Publishing.** Writing is not publishing. Posting, submitting or releasing material requires
  the operator's separate authorization.
