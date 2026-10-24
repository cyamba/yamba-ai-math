# KR1 source audit

Inspection date: **2026-10-23**. Novelty of a structural W<->C bridge:
**unverified**. A bounded search finding no completing map is not a
certificate that none exists. The historical problem brief is input,
not authority. KR1 is selected over KR2; no automatic scope expansion.

| Primary source and version | Inspection depth | Supported status |
| --- | --- | --- |
| [Mizuno, v3, 5 October 2026](https://arxiv.org/html/2609.09653v3) | Theorem 1.1, definitions, proof route in sections 2–6 | **Reported proved:** the first three sum-product identities. Inspected argument is series-based; no direct residue-to-gap map supplied there. Not independently fully checked here. |
| [Xia, v1, 8 September 2026](https://arxiv.org/html/2609.08816v1) | Theorem 1.1 and proof outline | **Reported proved:** all five modulo-nine identities. No independent full proof audit performed. |
| [Kurşungöz, arXiv:1808.01432, v1](https://arxiv.org/html/1808.01432) | Section 3, Theorem 7, base partition and forward/backward cluster moves | **Established construction:** A<->C with zero-padded increments. Numbering is this preprint's. Published in Annals of Combinatorics 23 (2019), 835–888. Not a B<->C construction. |
| [Andrews–Keith, arXiv:2203.05202v2, 14 July 2022](https://arxiv.org/html/2203.05202v2) | Sections 2–3 algorithms and section 5 Theorem 6 | **Established construction:** B<->W via conjugation/Stockhofe. Preprint title is *Schmidt-type theorems for partitions with uncounted parts*; published as *A general class of Schmidt theorems*, JNT 247 (2023), 75–99. Its 2022 open-status wording is historical. |
| [Mizuno's KR-mod9-lean](https://github.com/yuma-mizuno/KR-mod9-lean) | README and theorem declarations | Public power-series formalization, **not locally rebuilt**. Not an executable partition-bijection certificate. |

## Attribution and transcription caution

Andrews–Keith's section 2 example has inconsistent auxiliary vectors and
scaling. Accumulated removed weights (30,25,5,5) normalize to (6,5,1,1),
whose conjugate is (4,2,2,2,2,1). The final displacement is five times
that vector. Any adapter must use explicit units, then check weight and
both inverse identities; it must not blindly copy a displayed formula.
This does not refute the endpoint theorem.

The new proposed contribution is solely a recoverable structural W<->C
algorithm, its proof and formal verification. Reproducing endpoint maps,
finite equalities, or a known counting identity is not that contribution.

## Selection and limitations

KR2 uses the same gap restrictions with minimum part two and product
residues {2,3,6,7} modulo nine. KR1 has the simpler minimum-part boundary
and the inspected weighted-model foothold. A current explicit primary
declaration that a structural KR1 bijection remains open was not located.
The two planning reviews therefore supported only a **conditional**
construction target, with novelty still requiring comparison of any
actual proposed map against the closest work and cited generalizations.
