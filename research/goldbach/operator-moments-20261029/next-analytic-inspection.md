# Preview of the small-radical analytic route

29 October 2026. Independent Critic, separate bounded two-unit source inspection while the MOMENTS-010 author stage is pending. This file is a preview and dependency map, not the main critic verdict, a proof of Guo's analytic chain, or acceptance of H1, H2', a reflected parity theorem or Goldbach. Ownership is this file only. No usage measurements are available.

## Inspected sources and assurance

The pinned Guo input is `.runs/goldbach-source-inputs-20261029/guo-mobius-main.tex`, SHA256 `e70d777424852aed92e94b2baf00384c84b4c7fc346bd7dab1085d5652ced95d`, Git blob `a114f906cf205f4e50053c7a657f7de55048213c`. I inspected selected input, reflected major-arc, contour, sparse-frequency/Gram, energy, small-radical and assembly sections. This is proof-text inspection of those passages, not validation of the whole paper. The relevant pinned [source link](https://github.com/aster2024/openai-math-followups/blob/a605351dce1a55fb46a494d9cca9b0baa8f2734b/mobius-goldbach-shift/source/main.tex) fixes the provenance.

I read the PDF skill before attempting PDF inspection. Inspection levels below distinguish reading an exact theorem statement from checking its proof.

| Source | Inspection level | What is actually supported |
| --- | --- | --- |
| D. R. Heath-Brown, *Burgess's Bounds for Character Sums*, arXiv:1203.5219v2, introduction (1) and following theorem | Exact primary PDF statement inspected, proof not audited | The r=2 Burgess input permits arbitrary moduli; the separate mean-value theorem has additional hypotheses |
| H. Iwaniec, *On zeros of Dirichlet's L series*, Invent. Math. 23 (1974), 97-104, Theorem 2 on page 97 | Primary-page indexed OCR excerpt only; exact displayed width not visually inspected | The exceptional character/zero assertion is visible; the exact normalization remains an access-limited dependency |
| Guo's transcription of Iwaniec and subsequent reduction | Exact local proof text inspected | The conditional algebra of its small-radical implication can be checked, independently of accepting the imported theorem |

The [Springer article](https://link.springer.com/article/10.1007/BF01405163) provides metadata and an access restriction; its PDF endpoint redirects there. A [Goettingen original-volume scan](https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0023/PPN356556735_0023.pdf) exposes page 97 in indexed primary OCR, but exceeds the web reader's 10 MiB limit. Direct local read-only retrieval failed because network name resolution is restricted. Its OCR garbles the width definition. I did not purchase access, infer the formula from metadata or claim a complete original-page inspection. A later primary-page reading must confirm the exact exponent, constant, t dependence, scope of characters and exceptional case. Guo's transcription and later authors' citations are not substitutes for that check.

## The Burgess input is available at the needed modulus type

The [primary Heath-Brown PDF](https://arxiv.org/pdf/1203.5219v2), introduction (1), gives the familiar interval bound uniformly in the starting point, with either cube-free modulus or r<=3. For a primitive nonprincipal character of conductor q*>1, its r=2 specialization is

    |sum_{H0<n<=H0+H} chi*(n)|
       <= C_epsilon * H^(1/2) * (q*)^(3/16+epsilon).

Thus a large power of two is allowed. The separate displayed mean-value theorem assumes a primitive character, H<=q, separated starting points in [0,q), and a lower length condition in its r=2 case. Those hypotheses must not be omitted if that stronger theorem is used; Guo cites the ordinary introductory interval estimate instead. This is theorem-statement inspection, not a fresh proof of Burgess.

Guo applies the bound to primitive inducing characters. For an imprimitive product character, it expands missing-prime unit factors over squarefree divisors and retains a divisor-count cost. Its selected Gram use has conductor q*<=kN, k<=L^A0, length M>=N^(3/8+eta0), eta0=1/40, and epsilon=eta0/8. The exponent margin is coherent:

    M^(-1/2) * N^(3/16+epsilon)
       <= N^(-eta0/2+epsilon).

Subpower sparse-family and imprimitive costs can fit within that fixed negative power. This checks the proposed parameter margin; it does not establish the preceding Gram matrix estimate or its complete frequency and coefficient hypotheses. Principal inducing characters require their separate same-character/low-conductor treatment and cannot receive this Burgess cancellation bound.

## Why the small-radical condition could supply the selected strip

Use N for the reflected even shift and L=log N. The source's universal H1 is the asserted zero-free half-plane Re(s)>7/8 for all Dirichlet characters, with the principal pole excepted. It is an unverified input here. The reflected energy argument asks only for one selected H1*: for all primitive conductors q* dividing kN, k<=L^A0 and q*>L^A1, a zero-free closed strip of width C1*log L/L up to height L^C2. The fixed C1,C2 depend on the desired energy precision. H1 would imply that selected strip eventually, but must not be called classical.

The Iwaniec formula transcribed in Guo is

    theta^(-1) = 4*10^4 *
       (log rad(q*) + (ell*log(2ell))^(3/4)),
    ell = log(q*(|t|+3)),

with at most one nonprincipal exceptional character and zero in the corresponding region; if present they are real, and the zero is real and simple. The exact formula remains incompletely inspected at the original page for the reasons above. The following deduction is conditional on that exact primary theorem being confirmed.

If rad(N)<=L^C and q* divides kN with k<=L^A0, then rad(q*)<=L^(A0+C), and at the required fixed polylogarithmic height ell<=2L eventually. The stated width is consequently at least a constant times L^(-3/4)(log L)^(-3/4). Its ratio to C1*log L/L tends to infinity. A real primitive character has fundamental-discriminant conductor at most 8*rad(kN), so it lies below L^A1 when A1=A0+C+1 and L>=8. The possible real exception is therefore outside the large-conductor range demanded by H1*. Strict domination of the widths handles its closed boundary.

For N=2^m, rad(N)=2, so this small-radical argument would apply. Nevertheless k can have odd prime factors. The required conductors divide k*2^m, not necessarily a power of two. A theorem restricted solely to prime-power conductors would leave a real gap. The elementary bound on real primitive conductors and the radical dependence are exactly what the proposed reduction uses. This does not establish a universal zero-free half-plane, generalized RH, or exceptional-zero exclusion for unrelated conductors.

## A verified operator chain would still leave a major-energy theorem

The analytic obligation is an independently proved uniform estimate of the form

    (1/phi(N)) * sum_{chi mod N} integral_{|t|<=T0}
       |B_{xi_b}(t) M_xi(t) N_xi(t)|^2 dt
        <= C_A * L^(-A)/N,

for the actual reflected character fibers, polynomial coefficients, phase twists, dyadic lengths and unit/sifting support. Here the last N_xi is the source's polynomial, not the shift N. This estimate is the source's alpha* interface. The source's reflected energy theorem at lines 2297-2404 is a proposed proof of this interface from the selected strip and additional inputs. Neither an operator moment bound nor Burgess alone proves it.

An actionable next analytic audit should freeze the complete definitions and reconstruct that theorem in this order:

1. Prove the character-fiber expansion and its fixed powers of k when k and N share primes; check the Mellin transform and all prefactors for the full denominator-N pullback comparison.
2. Prove the long-prime-factor polynomial bound from the selected strip by Perron, including imprimitive corrections, contour-height margins, short endpoint intervals and prime-power/sifting losses.
3. Prove the sparse large-value family count and its Gram bounds at the actual support lengths. Retain principal/same-character terms, imprimitive divisor costs and frequency separation; only then insert the checked Burgess and Polya-Vinogradov inputs.
4. Audit the small-conductor twisted sifted Mobius estimate from its own primary source, including conductor/frequency ranges, interval extensions and the smooth-divisor tail. Its citation has not been validated by this preview.
5. Sum the bulk and exceptional energies with the selected fixed C1,C2,A1 and verify that the major comparison form has the needed saving after all arc, character and Mellin costs.

Even after that analytic theorem and the operator chain are verified, the actual-prime conclusion still requires the decomposition, endpoint pairing and good-state removal, auxiliary-weight removal, logarithmic unweighting and support/boundary corrections. Those are separate proof obligations. A cancellation bound for sum_{p<N} mu(N-p), or a split between its two nonzero signs, is not itself a Goldbach lower bound: a Mobius sign does not identify a prime complementary summand. The original polynomial-roughness and h=1/nonzero-center bridge must remain explicit.

The useful preview conclusion is therefore narrow. Burgess r=2 has the correct arbitrary-modulus statement. The small-radical zero-free reduction is algebraically coherent conditional on confirming the exact Iwaniec primary statement. Powers of two are a natural test class for a later complete parity proof, but neither that parity result nor the major-energy theorem has been accepted here. The frozen MOMENTS-010 author statement and its actual critic packet take priority over further preview work.
