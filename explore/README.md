# Research seeds

Sixteen starting points for mathematical research on efficient models, reliable generation, predictive world models, and agent systems. Every item is a **seed**. Its conjectures are unproved and its novelty is **NOT VERIFIED**. Source inspection was performed on **2026-10-20**; this is a starting bibliography, not a claim to cover all work available on that date.

The organizing question is: **which task structure can a smaller model exploit, with what learning guarantee, and at what total system cost?** A larger unrestricted hypothesis class may contain the smaller architecture. The meaningful opportunity is usually a gain in learning, robustness, memory, inference, or the allocation of computation under specified constraints.

| ID | Research seed | Category | First mathematical object |
| --- | --- | --- | --- |
| E001 | [Certified attention compression](E001-certified-attention-compression.md) | Attention and geometry | Retrieval margin and perturbation bounds |
| E002 | [Rare facts and memory bits](E002-rare-facts-and-memory-bits.md) | Attention and geometry | Conditional entropy and rate-distortion |
| E003 | [Approximate symmetry](E003-approximate-symmetry.md) | Attention and geometry | Group averaging and bias-variance tradeoffs |
| E004 | [Multiscale evidence graphs](E004-multiscale-evidence-graphs.md) | Attention and geometry | Laplacians, elimination, and query-sensitive sparsification |
| E005 | [Action-identifiable JEPA](E005-action-identifiable-jepa.md) | World models | Intervention-indexed latent dynamics |
| E006 | [Decision-sufficient world models](E006-decision-sufficient-world-models.md) | World models | Bisimulation and task-conditioned state quotients |
| E007 | [Multimodal predictive world models](E007-multimodal-predictive-world-models.md) | World models | Conditional distributions and branching latent futures |
| E008 | [Multiscale temporal operators](E008-multiscale-temporal-operators.md) | World models | Koopman operators and approximate semigroups |
| E009 | [Causal hallucination channels](E009-causal-hallucination-channels.md) | Reliability | Structural causal models and interventions |
| E010 | [Proof-carrying generation](E010-proof-carrying-generation.md) | Reliability | Sound proof systems and selective prediction |
| E011 | [Sequential risk control](E011-sequential-risk-control.md) | Reliability | Filtrations, stopping times, and conditional error budgets |
| E012 | [Error-correcting memory](E012-error-correcting-memory.md) | High-upside mathematics | Frames, sparse codes, and decoding margins |
| E013 | [Agent topology and correlation](E013-agent-topology-and-correlation.md) | Agent systems | Covariance propagation over communication graphs |
| E014 | [Value of computation](E014-value-of-computation.md) | Agent systems | Optimal stopping and information acquisition |
| E015 | [Proof-guided architecture search](E015-proof-guided-architecture-search.md) | Mathematical methodology | Compositional contracts and resource-aware search |
| E016 | [Interventional modular experts](E016-interventional-modular-experts.md) | High-upside mathematics | Causal factorization and sparse routing |

## Suggested entry paths

- **Attention first:** E001 → E002 → E012. Try to preserve answer-relevant distinctions, then discover which memory savings are impossible.
- **Geometry first:** E003 → E004. Establish a genuine task symmetry or operator structure before engineering a geometric architecture.
- **World models first:** E005 → E006 → E007 → E008. Separate identifiable state, sufficient state, uncertain futures, and long-horizon prediction.
- **Reliability first:** E009 → E010 → E011. Explain failure channels, certify a restricted domain, then control adaptive composition.
- **Systems first:** E013 → E014 → E015. Compare teams and computation policies under the same total budget, then make the reasoning auditable.
- **Cross-cutting bet:** combine E005, E009, and E016 to ask whether interventions can produce both interpretable failure explanations and smaller, repairable modules.

## From seed to a defensible contribution

1. Read the closest full papers and record a novelty matrix. Name which part is reproduced, extended, or contradicted.
2. Define one finite task family, an explicit baseline algorithm, and a computable metric. Construct the strongest simple counterexample first.
3. Prove or disprove a narrow lemma. Keep its assumptions and quantifiers visible. A failed conjecture can yield a better impossibility theorem.
4. Run the smallest experiment that could invalidate the proposed mechanism. Include a matched-budget baseline and uncertainty across seeds or task draws.
5. Write an article around what was established. Promote to a reusable framework and an executable architecture only when its interfaces and empirical scope are clear.

The source ledger is [the reading list](../references/reading-list.md). New seeds can use [the brief template](templates/brief.md). These pages contain no reported experiments, benchmark wins, or completed proofs.
