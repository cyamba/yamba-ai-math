---
name: framework-qa
description: Answer questions about how the Yamba AI Math framework works or why it is designed as it is, grounded in repository files with path citations, separating documented policy from code-enforced behavior and flagging drift between them.
---

# Answer framework questions

1. **Restate** the question in one line and decide its kind: where (location), what (meaning),
   how (mechanism), why (design reason), can I (permission or capability).
2. **Find the canonical source.** Check the [glossary](../references/glossary.md) first, then
   search the docs (`AGENTS.md`, `README.md`, `docs/`, local `AGENTS.md` files), then the code
   (`harness/`, `scripts/`, `tests/`). For behavior, the code and tests decide; for intent and
   rules, the docs decide.
3. **Answer first**, in one to three sentences, with the paths that support it. Then add detail
   only as needed.
4. **Separate** "the repository says" from "my inference". Mark policy that no code enforces
   (for example, that tags are routing hints, not credentials) and behavior that code enforces
   (for example, `required_tags` filtering in the planner).
5. **Flag drift** when docs and code disagree: quote both locations and say which one currently
   determines behavior. Do not fix it silently; a fix is a separate, requested change.
6. **Permissions**: when the question is whether something is allowed, answer from the
   authorization rules in `AGENTS.md`, `CLAUDE.md` and `programs/contract.md`. Skills and
   directories grant no extra budget, execution or publication rights.
7. **Not in the repository**: say so plainly and suggest where it would belong.
8. **Next step**: offer a diagram (framework-visualize), a tutorial stop (framework-tutorial) or
   a field-by-field walkthrough (framework-explain-artifact) when it would help.

Keep answers short. Link, do not paste, long passages from the repository.
