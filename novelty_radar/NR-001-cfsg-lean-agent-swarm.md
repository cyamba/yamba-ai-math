# NR-001: The Classification of Finite Simple Groups, formalized in Lean by an AI agent swarm

| Field | Value |
| --- | --- |
| ID | NR-001 |
| Found | 2026-10-28, via the video [Classification of Finite Simple Groups Formalized In Lean by an AI Swarm](https://www.youtube.com/watch?v=NZklSBoLC30) (Samuel Allen Alexander, uploaded 2026-10-28, about 41 minutes) |
| Kind | Formalization milestone; agentic research method; new result in group theory; new publication venue |
| State | `EXPLORE FURTHER`, with `TRACKING` items below |
| Evidence here | **Unverified.** The release reports a complete machine-checked proof. Nothing was rebuilt here, and no independent rerun or statement review had been reported publicly when this entry was written. Sources were read at announcement, README and abstract level (inspection level A). |
| Receiving project | Unassigned. Candidate hooks: the research harness (`agents/`, `fleets/`, `programs/`, `meta/`), the Lean work in `research/`, and the [understanding layer](../understanding/README.md). |
| Next action | The bounded steps under [Explore further](#explore-further) |

## The source

The video is a read-through with commentary of Axiom's announcement, its proof map and the
accompanying paper on the Unbalanced Group Theorem. It is enthusiastic and does not check
anything independently, so it is a pointer rather than evidence. Around minute 8 the presenter
calls Hexagon a competitor that is taking over arXiv's role; that is an opinion, assessed
[below](#hexagon-the-next-arxiv).

## What is new, as the primary sources state it

1. **A complete formal proof of CFSG.** Axiom announced on 2026-10-27 (blog post dated
   2026-10-26) the first complete computer-checked proof of the Classification of Finite Simple
   Groups. The [repository README](https://github.com/AxiomMath/CFSG) describes a sorry-free
   Lean 4 (v4.35.0-rc3) development built on Mathlib and TauCeti, using only the standard axioms
   `Classical.choice`, `propext` and `Quot.sound`, with no `native_decide`, and primarily
   following the first-generation proof.
2. **The target statement comes from another project.** The proved statement is TauCeti's
   `ClassificationStatement`: every finite simple group is isomorphic to one of the explicitly
   constructed groups on the classification list, indexed by `CFSGIndex`.
3. **Scale and method.** According to the [blog post](https://axiommath.ai/research/the-enormous-theorem-formalized/),
   over 24 days engineers and mathematicians directed swarms of dozens of AI agents
   (AxiomProver) that produced about 43.1 million lines of Lean. The work was organized from a
   proof map into 108 milestones and about 380 smaller tasks. Agents claimed milestones through
   GitHub issues and reported in a chat channel; lead agents decomposed arguments and reviewed
   statements; integration agents traced the final theorem back through its prerequisites.
   About 1.2 million lines came from the Qiuzhen-CFSG project. Engineers built distributed build
   caching and moved expensive finite computations into separately checked certificates; the
   README reports a full build under 24 hours with Lake changes and optimizations not yet
   upstreamed.
4. **Problems found in the literature.** Most were minor (typographical errors, wrong table
   entries, dropped hypotheses), but the post counts 34 noteworthy deviations from the published
   record and publishes an errata list. Two examples it describes: a lemma in the
   Aschbacher and Smith quasithin volumes asserting an equality that fails for a configuration
   involving SL₂(5), and counterexamples to a closure assertion in Walter's 1986 route to the
   Unbalanced Group Theorem (UGT), starting from PSL₂(49) and its field involution.
5. **A new theorem.** To repair the UGT step, AxiomProver produced and formalized an alternative
   argument built on Solomon's 1976 theory of maximal 2-components, including a preservation
   result for simple tops (Theorem 2.3). Colin Defant and Ken Ono wrote it up as
   [hexagon:2610.00575v1](https://hexagonmath.org/2610.00575?version=1) (2026-10-27, math.GR),
   which also records a shorter route found afterwards (Remark 9.5). Group theorists who worked
   on the original classification, including Richard Lyons and Ronald Solomon, were consulted.
6. **Open invitation to check.** Axiom asks group theorists and the Lean community to rerun the
   proof check and to confirm that the Lean statement says what CFSG says.

Other reports, including posts by team members, quote different figures (for example 50
million lines, 100 substantive fixes, hundreds or over 2,000 errors). Use the numbers in the
blog post and README until they are checked.

## Hexagon: the next arXiv?

**Facts.** Hexagon (hexagonmath.org) is a repository for
mathematics and theoretical computer science run by the Hexagon Mathematics Foundation, a
Delaware nonprofit seeking 501(c)(3) status. It was announced on 2026-10-06 in a
guest post by its executive director Ben Antieau on
[Terence Tao's blog](https://terrytao.wordpress.com/2026/10/06/hexagon/) and is in beta. The
board is Mohammed Abouzaid, François Charles, Bryna Kra, David Savitt and Lauren Williams; the
advisory board includes Kevin Buzzard, Akhil Mathew, Johannes Schmitt, Steinn Sigurðsson, Nikhil
Srivastava, Ravi Vakil and Rachel Ward. It accepts LLM-assisted and even entirely
LLM-generated work, including work whose submitters claim no human understanding, as well as
small results; submitters are ORCID-validated humans, while contributors can be AI labs. Records
carry a text-origin label and a human-understanding label, get arXiv-style identifiers such as
`hexagon:2610.00575`, and are readable through an API. Submission rate limits start at one per
day.

**Context.** [Tech Times reports](https://www.techtimes.com/articles/328761/20261007/mathematicians-create-nonprofit-archive-ai-generated-proofs-arxiv-declined-host.htm)
that arXiv bans entirely LLM-generated submissions and, from 2026-10-01, limits authors to two
submissions per calendar month and three active submissions, after an overload of submissions.
The founders say they consulted arXiv, which would not provide this kind of home.

**Assessment.** Not a replacement, by its founders' own framing: a first home for AI-era results
on their way toward community acceptance, arXiv and journals. It already has credible backing
and real use (the UGT paper above;
[a First Proof batch](https://hexagonmath.org/2610.00244v1) by Abouzaid, Srivastava, Ward and
Williams). Open risks: beta software, funding not yet sustainable, moderation standards not
described in the announcement, and verification questions around work with no claimed human
understanding. Treat it as a new feed to watch and as a possible venue, not as a quality signal
on its own.

## Why it may matter here

1. **Harness evidence.** The swarm's practices map onto open questions for our fleets:
   decomposing a milestone into precisely stated smaller theorems whose combination is a short
   formal proof; reviewers comparing what was proved with what was intended; a dedicated
   integration role; shared build caches and certificates. Their main failure mode, a proof
   under an added, unproved assumption that looks like progress while changing the theorem, is
   exactly what our [research protocol](../docs/research-protocol.md) guards against. These are
   workflow observations, unvalidated for this repository.
2. **Lean work.** Proof maps, certificates for finite computations and a statement review kept
   separate from proof checking are patterns the Lean obligations in `research/` could reuse.
3. **Trust.** A formal proof certifies the formal statement relative to its definitions and
   trusted base. Axiom's own request to check that the Lean statement matches CFSG is the same
   check our standards require before anything depends on a result.
4. **Venue.** Hexagon could suit LLM-assisted manuscripts that arXiv will not host. Any
   submission is the operator's decision and needs a check of licenses and labels first.
5. **Understanding.** The proof map and the UGT paper are good first material for the
   understanding layer's `digest-result` and `visualize-math` skills.

## Explore further

Bounded, read-only steps:

1. **Statement review.** Read TauCeti's `ClassificationStatement` and the `CFSGIndex` definitions:
   are the parameter restrictions and exceptional isomorphisms handled as the classification
   requires? Record the result and add a reading-list entry (level T) if a research file will
   cite it.
2. **Track validation (`TRACKING`).** Watch for independent reruns, comments from group theorists
   and the Lean community, errata updates and reactions to the UGT paper. Update this entry with
   dates.
3. **Method extraction.** Write a one-page comparison of the swarm's workflow with our fleets. Any
   proposed harness change becomes a `meta/` candidate under the meta protocol, not an edit.
4. **Digest the UGT paper** with `digest-result`: statement card, key idea, the PSL₂(49)
   counterexample worked out step by step, and what is new.
5. **Venue check.** Read Hexagon's about and submission pages and decide whether any manuscript in
   this repository fits.

Stop condition: after steps 1 to 3, return this entry to `TRACKING` unless a concrete hook into
a current project has appeared.

## Sources (checked 2026-10-28)

- Video: [Classification of Finite Simple Groups Formalized In Lean by an AI Swarm](https://www.youtube.com/watch?v=NZklSBoLC30)
- Axiom blog: [Formalizing the Enormous Theorem](https://axiommath.ai/research/the-enormous-theorem-formalized/)
- Code: [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG); proof site, proof map and errata at [cfsg.axiommath.ai](https://cfsg.axiommath.ai/) (linked from the post, not inspected here)
- Paper: [Defant and Ono, The Unbalanced Group Theorem, hexagon:2610.00575v1](https://hexagonmath.org/2610.00575?version=1)
- Announcement: [Axiom on X](https://x.com/axiommathai/status/2115089794867040584)
- Hexagon: [guest post by Ben Antieau on Terence Tao's blog](https://terrytao.wordpress.com/2026/10/06/hexagon/); [Tech Times coverage](https://www.techtimes.com/articles/328761/20261007/mathematicians-create-nonprofit-archive-ai-generated-proofs-arxiv-declined-host.htm)
- Related efforts located but not inspected: [FormaTheoria, arXiv:2608.10894](https://arxiv.org/abs/2608.10894) and [A constructive ATLAS of finite simple groups in Lean, arXiv:2609.35847](https://arxiv.org/abs/2609.35847)
