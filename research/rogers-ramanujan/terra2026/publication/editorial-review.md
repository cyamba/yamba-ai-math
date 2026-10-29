# Editorial and mathematical fidelity review

**Draft:** [article.md](article.md), approximately 2,159 whitespace-separated words including image text and references. The draft is a publication handoff; it has not been published.

## Claim-by-claim checks

- **Headline and scope:** States the positive auxiliary construction near the top and explicitly says the full KR1 weight-preserving bijection is not constructed. It does not claim that equality of counts itself remains conjectural. Novelty is explicitly unverified.
- **KR1 conditions:** Product residues and the distance-two and close-pair gap conditions match Xia's introduction and the research theorem. The weight-two example is valid.
- **The general theorem:** The hypotheses c,d>0, 0<r_i<c, distinct paired nodes and 0<=m<=n match the independently reviewed theorem. The statement concerns coefficientwise positivity of a formal series, not a completed partition bijection. Its m>n example asserts only the negative q coefficient and does not omit factors by writing a truncated expression.
- **Word encoding and involution:** Inclusive cut endpoints, canonical alpha-before-beta order, strict beta-to-alpha descents, staircase weights, least-active-marker toggle, inverse and survivor condition match [general theorem note](../theory/general_positive_divided_differences.md) and [independent review](../staircase-independent-review.md). The six-cut all-empty-word example has marker weight 18 and cut indices (0,0,0,0,1,1), giving index charge 18 on either side. The nearby illustration is a separate valid example with two particles.
- **Recurrence:** The four-term C row and the weight-eight particle-count obstruction agree with [final math review](../final-math-review.md) and [recurrence note](../theory/recurrence_final_pass.md). The article rules out particle-count-preserving recurrence maps, not every possible structural construction.
- **Auxiliary results:** The finite-digit largest-part obstruction has the correct direction and bound, and is stated as an injection barrier for a restricted source family. The local surgery is explicitly not the full KR1 algorithm.
- **Verification:** 124,944 is the reported finite word/marker check. The independently generated coefficient record has 18 cases: 17 through 45 and A1 through 30, totaling 813 coefficients. A0 is a separate product calculation, and all finite results are labeled transcription evidence. Lean's claims are limited to selected universal components; it does not formalize the full source lemma, word encoding, or KR1 map. See [verification scope](../formal/verification-scope.json).
- **Mizuno formalization:** Registry-reported Lean and nanoda checks are distinguished from our own work. The coordinating agent inspected the pinned statement and solution wrapper, not a complete local external build or the entire proof. Registry statement comparison is identified as AI-mediated rather than human peer review. See [source record](../theory/mizuno_formal_source.md).
- **Primary references:** Xia v1, Mizuno, Chern–Li, and Uncu–Zudilin links are included. The two `ROOT_RESEARCH_URL` placeholders must be replaced by the coordinator with the public canonical research URL before publication.

## Figures and presentation

Four illustrations use the construct worker's SVG assets and are placed beside the associated claims. Captions and alternative descriptions were checked against the asset README. The marker illustration is a two-particle example; the article's six-cut all-empty example is separately valid. Figure 3 correctly identifies the A1 particles as beta. The SVG files have matching PNG fallbacks in `assets/`.

The source has zero Unicode U+2014/U+2015 characters, zero HTML em-dash entities and zero triple-hyphen sequences. This review is a source-level review by the drafting agent, not a separate independent mathematical review; independent reviews and their limitations are linked above. Rendering and site-specific math support remain for the publishing coordinator to check.
