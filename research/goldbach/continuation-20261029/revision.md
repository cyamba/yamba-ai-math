# Revision after the separate mathematical review

29 October 2026. Registry role: Mathematician. This revision uses the populated `revise` packet, the separate `review.md`, and the independent finite-check result. The reviewed original statements are preserved unchanged. No further source search or new computation was performed in this revision stage.

## Accepted results and assurance

The critic's verdict is **supported** for Proposition H, its fixed-epsilon consequence, the adaptive-epsilon counterexample, the moving-endpoint transfer lemma, the exact divisor-switch identity, and its sharpness witness. No repair to those mathematical statements was requested. I accept that review with its stated limits.

The strongest accepted pointwise statement is: for absolute effective but numerically unspecified C and N0, every even N>=N0 and every epsilon in [0,1/30], with alpha=1/3-epsilon, satisfy

\[
H_\alpha(N)\le\omega_{>N^\alpha}(N)+
 C\mathfrak S(N)\frac{N}{\log^2N}
       \left(\varepsilon+\frac1{\log N}\right)^2,
\qquad\omega_{>N^\alpha}(N)\le3. \tag{H}
\]

The exceptional prime summands divide N and exceed N^alpha. They are counted globally, once per summand. The proof includes repeated factors, primes equal to small sieving primes, and the distinction between actual admissible factor pairs and the enlarged harmonic sum. This is a classical upper-sieve consequence, rather than an average-to-pointwise inference.

Write A_N=mathfrak S(N)*N/log^2N. For each fixed epsilon>0 in the stated interval, (H) gives

\[
\limsup_{\substack{N\to\infty\\2\mid N}}
 H_{1/3-\varepsilon}(N)/A_N\le C\varepsilon^2. \tag{H-fixed}
\]

The lower-scale term in (H) cannot simply be deleted while allowing epsilon to depend on N. The reviewed N=r^3+3 family proves the failure of that stronger uniform assertion. When deriving (H-fixed), N tends to infinity with epsilon fixed first.

The supplemental endpoint lemma supplies a constant-one weighted-discrepancy transfer, with the exact strict endpoint M_k=max(0,ceil(N-eta*k)-1). Its prime-weighted use is conditional on the maximal-in-endpoint twisted estimate, and controls only the explicitly coprime part. It supplies neither that estimate nor the omitted noncoprime contribution or global analytic main term.

**Assurance:** complete handwritten arguments plus a separate host-agent substantive review. The finite worker separately checked the specified arithmetic identities and examples. No proof assistant or external human peer review was run. Separate agent identities do not ensure statistically independent errors. The finite run does not establish an infinite bound or a numerical value of its unspecified constant.

## Dated erratum to the imported brief

The imported `research/goldbach/orchestrated-prompt.md` says that at alpha=1/4 rough numbers may have four prime factors. Under its strict convention P^-(q)>floor(N^alpha), that statement is **refuted**.

Indeed, every admitted prime factor is an integer at least floor(N^(1/4))+1, hence is strictly greater than N^(1/4). A product of four admitted factors therefore exceeds N. For q<N, at most three factors can survive. Triple factors can survive: at N=30, the prime summand p=3 has q=27=3^3 and cutoff floor(30^(1/4))=2. Thus the P/S four-cell classification is still nonexhaustive at the quarter-root cutoff, because of triples, not four-factor survivors.

This correction changes neither Proposition H nor the endpoint lemma. The original imported file remains preserved as provenance; this dated erratum records its corrected interpretation.

## The remaining pointwise input

For the original rough-complement counts, define F_alpha(N)=(U_alpha(N)-L_alpha(N))/2. In the present range a rough complement has at most three prime factors, so exactly

\[
R_z(N)=F_\alpha(N)-H_\alpha(N).
\]

The quantity R_z counts prime summands p with a prime complement N-p>z. The prime p itself is unrestricted by z. This is the convention used throughout the reviewed result.

The sufficient missing estimate is still

\[
\liminf_{\substack{N\to\infty\\2\mid N}}
 F_{1/3-\varepsilon}(N)/A_N>C\varepsilon^2
\quad\text{for at least one fixed }\varepsilon\in(0,1/30]. \tag{P-open}
\]

Here C is the fixed constant supplied by (H). **Status: conjectural and unproved.** No signed mean, unsigned Chen count, source statement of a distribution conjecture, finite scan, or successful harness protocol response supplies (P-open). The condition gives a quantitative prime-pair-scale margin and is stronger than mere existence of a Goldbach representation.

## Conditional linear-margin corollary

The following elementary implication clarifies the margin that would suffice. It is not a new solution of the parity problem.

Suppose there exist c>0 and epsilon0>0 such that, for every sufficiently small fixed epsilon in (0,epsilon0],

\[
\liminf_{\substack{N\to\infty\\2\mid N}}
 F_{1/3-\varepsilon}(N)/A_N\ge c\varepsilon. \tag{L-open}
\]

The same c must work for those epsilon. The threshold in N may depend on each chosen epsilon. Select one fixed epsilon with

\[
0<\varepsilon<\min\{\varepsilon_0,1/30,c/C\}
\]

and small enough to lie in the assumed range of (L-open). Then

\[
\begin{split}
\liminf_{\substack{N\to\infty\\2\mid N}} R_z(N)/A_N
&\ge\liminf F_{1/3-\varepsilon}(N)/A_N
       -\limsup H_{1/3-\varepsilon}(N)/A_N\\
&\ge c\varepsilon-C\varepsilon^2>0.
\end{split}
\]

Therefore every sufficiently large even N would have a Goldbach representation. Epsilon is chosen before taking N to infinity, so no interchange of limits is used. This is a proved conditional implication from the reviewed upper bound; **(L-open) itself is unproved**, and requiring a c independent of epsilon may make it harder than proving (P-open) for one fixed epsilon. There is no evidence here that (L-open) is more accessible. A full all-N proof would additionally require an explicit threshold and verification below it, neither of which is supplied.

## Source and priority qualifications

The reviewed proof of H uses the inspected coefficient-uniform two-form upper bound in [Ford, Theorem 2.5](https://ford126.web.illinois.edu/sieve2023.pdf) and the inspected log-weighted prime harmonic estimate in [Tao, Theorem 1, equation (1)](https://terrytao.wordpress.com/2013/12/11/mertens-theorems/). Numerical effective constants have not been extracted. The result's closest-work comparison is insufficient to establish priority.

The [Huang-Li maximal hypothesis and divisor calculation](https://arxiv.org/html/2005.03811) were inspected in the preceding stage. [Moya's record](https://zenodo.org/records/21939906) explicitly announces overlap with the endpoint repair; its linked proof was inaccessible to the survey worker. The accepted finite transfer lemma does not certify that external repair or a complete conditional Goldbach proof.

The independent arithmetic run reports zero failures in 29,994 rough-complement cases, 628 exact symbolic-log divisor switches, and the stated finite numerical transfer checks. Those results verify implementation within their ranges. They are not used as a proof of H or (P-open).

The next substantive obligation is a noncircular target-uniform parity-sensitive lower estimate for F_alpha with a proved margin exceeding the contamination. The original Goldbach objective remains incomplete. The accepted upper bound closes a specific logarithmic-loss gap in this programme, but the evidence does not establish a novel Goldbach breakthrough.
