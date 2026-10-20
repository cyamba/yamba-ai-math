# Instructions for research exploration

This directory contains research seeds, not established contributions. Preserve that distinction in every edit.

- Keep stable IDs and simple YAML frontmatter: `id`, `title`, `status`, `category`, and `tags`. New briefs start with `status: seed`.
- State a concrete question, the closest known result, a proposed gap, mathematical assumptions, an explicitly **unproved** theorem target, an obstruction, a falsification experiment, cost metrics, and a next artifact.
- Use the exact label **Novelty status: NOT VERIFIED** until a documented search and comparison of full papers supports a narrower novelty claim. A checked URL or abstract is insufficient to establish novelty.
- Cite primary papers next to factual claims and register their inspection depth and verification date in `../references/reading-list.md`. Separate abstract inspection, theorem-statement inspection, and a full proof audit. Do not imply that the last occurred when it did not.
- Treat every proposed numerical win, architecture benefit, and mathematical extension as a hypothesis until evidence is recorded. An elegant reduction can still be computationally useless.
- Specify the task distribution, data access, optimizer, precision, training budget, comparison class, and inference budget behind a small-versus-large claim. Count memory outside the network, pretrained encoders, routers, verifier calls, and repeated samples.
- Distinguish representation, learning, optimization, generalization, and runtime results. Do not promote one into another. Compare lower bounds and upper bounds under matching assumptions.
- A low-rank logit matrix need not produce a low-rank softmax matrix. Attention concentration, confidence, semantic agreement, or a citation alone does not prove truth.
- State the actual task symmetry. Variable renaming and permutation of independent evidence may qualify; changing word order or arbitrary embedding rotations need not.
- Give abstention a cost and report answer coverage. Formal proof guarantees are relative to the formal statement, axioms, checker, and trusted premises; they do not certify the translation from ordinary language.
- Keep negative findings and counterexamples. Retire or revise a seed when its central premise fails; do not silently replace the objective to preserve a claimed success.
- Begin with local, small, reproducible falsification. Expensive training and external publishing remain separate actions requiring the authorization applicable to that action.

Use `templates/brief.md` for a new seed. The index should offer multiple research paths without claiming that one path has already won.
