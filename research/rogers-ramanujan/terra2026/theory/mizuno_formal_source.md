# Mizuno modulo-nine formalization source record

Checked 27 October 2026. Palomar's indexed entry
https://palomar-registry.org/entry?id=PALOMAR-2026-09-10-000002&version=1
reports Yuma Mizuno's KR-mod9-lean, with immutable source snapshot
`yuma-mizuno/KR-mod9-lean@d8b921339ecc`, Lean `leanprover/lean4:v4.31.0`,
and checked declarations `Challenge.kr₁`, `Challenge.kr₂`, `Challenge.kr₃`
plus three product initial-coefficient theorems. The registry describes the
main assertions as the three symmetric double-sum/product identities, with
coefficientwise convergence, in integer formal power series. It says the
statement file imports Mathlib alone, and lists permitted axioms `propext`,
`Quot.sound`, and `Classical.choice`.

The registry reports checking by the Lean kernel and the independent nanoda
kernel, plus an AI-mediated statement-comparison review. Its statement review
is explicitly not human peer review. The source snapshot listed is a formal
analysis result and is not claimed here to supply an explicit structural KR1
partition bijection. These are *registry-reported* mechanical details: we did not run the
external formalization. The coordinating root agent inspected the pinned
[Challenge.lean](https://github.com/yuma-mizuno/KR-mod9-lean/blob/d8b921339ecc/Challenge.lean)
and [Solution.lean](https://github.com/yuma-mizuno/KR-mod9-lean/blob/d8b921339ecc/Solution.lean)
through the GitHub connector. The challenge KRChallenge.KR1 states `HasSum`
of the (0,0) double-series summand to the product on residues 1,3,6,8 in
integer formal power series, with explicit finite denominators. The challenge
file has intentional `sorry` placeholders in theorem templates; Solution.lean
imports Comparator.Submission and forwards to Submitted.kr1 and related
declarations. That wrapper is not itself the underlying proof. We did not
locally build the external development or independently trace its full proof.
Direct web fetch returned DisabledError and sandbox curl could not connect to
the configured proxy; source inspection was instead by the root agent.

Associated preprint: Yuma Mizuno, *The three Kanade–Russell identities modulo
nine*, https://arxiv.org/abs/2609.09653; latest version and publication status
not independently checked here. Another recent preprint is Ernest Xia,
https://arxiv.org/html/2609.08816v1. This source record corrects an overly
weak previous summary that merely said the analytical claim was unverified:
the registry now reports substantial machine-checking evidence, with the
specific scope and limitations above.
