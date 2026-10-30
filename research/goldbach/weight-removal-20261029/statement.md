# Prime-relative weight removal and reflected Mobius cancellation

29 October 2026. Registry role: Mathematician, `GOLDBACH-WEIGHTS-014`, author stage. There are two candidates below. **Proved, pending distinct review:** the prime-relative moment and successive-limit argument, and its actual reflected-prime consequence relative to the explicit accepted dependency ledger. For general even H the second conclusion retains a family of selected zero-free inputs. On each fixed small-radical class those inputs follow from the named inspected classical statements and their accepted deductions. Assurance is a complete written argument using previously reviewed local results, not formal verification, external peer review or audit of every imported classical proof. Usage is unknown. No novelty, full source validation, Goldbach proof or demonstrated breakthrough is claimed.

## Definitions and fixed parameters

Let H be even and tend to infinity, L=log H. Fix rho in (0,1) and a positive integer K. For each fixed positive integer b, choose bK distinct fixed exponents a_(j,i) in (1/10,1/5), with j=1,...,b and i=1,...,K. Increasing H eventually makes all the following bands disjoint:

\[
 \Pi_{j,i}=\{r\text{ prime}:e^{L^{a_{j,i}}}<r\le e^{2L^{a_{j,i}}},\ r\nmid H\},
 \qquad V_{j,i}=\sum_{r\in\Pi_{j,i}}\frac1r.
 \tag{1}
\]

All exponents and b are fixed before H grows. The bands may depend on H through the displayed endpoints and exclusion. Write u_(j,i)(w) for their distinct-prime divisor counts. Define

\[
 w_i(u)=\begin{cases}u\rho^{u-1}/V_{j,i},&u\ge1,\\0,&u=0,\end{cases}
 \qquad W_j(w)=\prod_{i=1}^K w_i(u_{j,i}(w)). \tag{2}
\]

These weights are nonnegative; they are defined for every positive integer w, without a squarefree assumption on w. Powers of a divisor prime contribute once. We use the positive prime measure

\[
 \Theta_H(I)=\sum_{p\in I,\ p<H}(\log p),
 \qquad I=(s,t],\quad 0\le s\le t\le H.
\]

Endpoint conventions remain the same throughout. All errors for arbitrary I are absolute errors measured at H, not errors relative to the mass of a very thin I.

## Candidate 1: positive actual-prime moments and removal

**Claim, proved pending review.** Put pi_r=1/(r-1) for band primes and define the exact finite quantity

\[
 m_j=\prod_{i=1}^K\left\{
 \frac1{V_{j,i}}\sum_{r\in\Pi_{j,i}}\pi_r
       \prod_{q\in\Pi_{j,i},\ q\ne r}(1-(1-\rho)\pi_q)
 \right\},\quad X_j=W_j/m_j,\quad
 \overline W_b=\frac1b\sum_{j=1}^bX_j. \tag{3}
\]

For each fixed array, m_j=2^(K(rho-1))+o(1), simultaneously in its finitely many j. There is a constant C_X depending only on K,rho, independent of b and of the fixed array, such that eventually 0<=X_j<=C_X. For every fixed A and each j!=k,

\[
 \begin{split}
 \sum_{p\in I,p<H}\log p\,W_j(H-p)
       &=m_j\Theta_H(I)+O_{A,b,\boldsymbol a}(HL^{-A}),\\
 \sum_{p\in I,p<H}\log p\,W_j(H-p)W_k(H-p)
       &=m_jm_k\Theta_H(I)+O_{A,b,\boldsymbol a}(HL^{-A}).
 \end{split}\tag{4}
\]

The leading constants in the following consequence are independent of b:

\[
 \sum_{p\in I,p<H}\log p\,|\overline W_b(H-p)-1|^2
 \le\frac{C_X-1}{b}\Theta_H(I)
       +O_{A,b,\boldsymbol a}(HL^{-A}). \tag{5}
\]

The harmless replacement of C_X-1 by a larger positive constant is permitted. In particular, for any target f_H(p) with |f_H(p)|<=C_f, including targets that vary with H,

\[
 \left|\sum_{p\in I,p<H}\log p\,f_H(p)(1-\overline W_b(H-p))\right|
 \le C_f C_{K,\rho}\frac H{\sqrt b}+o_{b,\boldsymbol a}(H). \tag{6}
\]

No cancellation assumption on f_H is used in (4)-(6).

### Exact local model, normalizers and uniform bounds

For any squarefree d formed from eligible band primes, the condition d|(H-p) is the single reduced class p=H modulo d, since (d,H)=1. Among the phi(d) reduced classes it has proportion 1/phi(d). CRT identifies the local model with independent Bernoulli variables B_r having probabilities pi_r. This is a model used for the main term, not an assumption of exact finite-prime independence.

For u=sum_r B_r,

\[
 \mathbb E z^u=\prod_r(1-\pi_r+\pi_r z),\qquad
 \mathbb E[u\rho^{u-1}]
   =\sum_r\pi_r\prod_{q\ne r}(1-(1-\rho)\pi_q). \tag{7}
\]

This proves (3). Disjoint copies have exact model mixed expectation m_jm_k. The main-term probability is 1/(r-1), whereas 1/r is the integer-divisor model and 1/(r+1) is the projective root-line model. They describe different populations. For example, at r=3,H=2 the relevant reduced-residue probability is 1/2; with V=1/3, the single-prime weight has means 3/2, 1 and 3/4 in these three models, respectively. This refutes replacing the prime-relative mean by either alternative.

The inspected prime harmonic estimate, also used in MOMENTS-010, gives full-band V^0=log 2+o(1). Excluding primes dividing H removes at most

\[
 \frac{L}{e^{L^a}L^a}, \tag{8}
\]

because their number is at most L/L^a and each reciprocal is at most e^(-L^a). Thus each V=log 2+o(1), uniformly over the H-dependent exclusions for a fixed exponent. Further,

\[
 \sum_r\pi_r=V+O\left(\sum_r r^{-2}\right)=V+o(1),\qquad
 \sum_r\pi_r^2=o(1).
\]

Writing the single-band expression in (7) as
`prod_r(1-(1-rho)pi_r) * sum_r pi_r/(1-(1-rho)pi_r)`
shows it is `exp(-(1-rho)V+o(1))*(V+o(1))`. Dividing by V proves each factor tends to 2^(rho-1). Let m_0=2^(K(rho-1))>0. After a threshold depending on the finite array, all V>=v_*=log(2)/2 and m_j>=m_0/2. The function u*rho^(u-1) is bounded by (1-rho)^(-2), so

\[
 0\le W_j\le C_W=\{v_*^{-1}(1-\rho)^{-2}\}^K,
 \qquad 0\le X_j\le C_X=\max(1,2C_W/m_0). \tag{9}
\]

These constants do not depend on b. The thresholds may. In particular X_j^2<=C_X X_j pointwise. This avoids a same-copy second-moment expansion with repeated divisor primes.

### Finite expansion with a positive arithmetic error

For one band, set R=ceil(C_A log L), beta=1-rho. Taylor's theorem for u(1-beta)^(u-1), or its exact finite polynomial when u<=R, gives

\[
 \frac{u\rho^{u-1}}V
  =\frac1V\sum_{h=0}^{R-1}(h+1)(-\beta)^h
        \sum_{\substack{d\mid w,\ d\text{ squarefree in }\Pi\\\omega(d)=h+1}}1
       +E_\Pi(w),
\]
\[
 |E_\Pi(w)|\le B_\Pi(w):=
   \frac{(R+1)\beta^R}V
       \sum_{\substack{d\mid w,\ d\text{ squarefree in }\Pi\\\omega(d)=R+1}}1. \tag{10}
\]

The inequality includes u=0. Let A_Pi be the absolute retained divisor polynomial. For either local weight gamma(d)=1/d or 1/phi(d), its multiplicativity on these squarefree divisors and the elementary-symmetric bound imply

\[
 \sum_d |c_{\Pi,d}|\gamma(d)\le
   V^{-1}\sum_{h<R}(h+1)\beta^h\frac{M^{h+1}}{(h+1)!}
       \ll_{\rho}1,
\]
\[
 \sum_d b_{\Pi,d}\gamma(d)\le
       \frac{(R+1)\beta^R}{V}\frac{M^{R+1}}{(R+1)!}
       \ll_{\rho}\frac1{R!}, \tag{11}
\]

where M=sum_(r inPi) gamma(r)<=1 eventually. The bound uses V>=v_*. For F=W_j or F=W_jW_k, j!=k, at most s=2K disjoint bands occur. Telescope their product: in a term with the first error use B_Pi, absolute retained factors for preceding bands and the bounded true factors from (9) for following bands. This produces

\[
 F(w)=P_F(w)+\mathcal E_F(w),\quad
 P_F(w)=\sum_{d\mid w}c_d,\quad
 |\mathcal E_F(w)|\le E_F(w)=\sum_{d\mid w}e_d,\quad e_d\ge0,
\]
\[
 \sum_d|c_d|\gamma(d)\ll_{K,\rho}1,\qquad
 \sum_de_d\gamma(d)\ll_{K,\rho}1/R!. \tag{12}
\]

Constants bounding the true following factors need not be divisor expansions. Every resulting error term remains a finite positive divisor polynomial. No estimate bounds an alternating truncated polynomial by the true positive weight.

The d in (12) are squarefree, avoid H, and have at most 2K(R+1) prime factors, all at most exp(2L^(.2)). Consequently

\[
 \log d=O_K(RL^{1/5})=o(L),\quad d\le D_H=H^{o(1)}.
 \tag{13}
\]

Band factorization uniquely recovers each term's chosen primes; with at most 2K telescoping terms this gives `max(|c_d|,e_d)<=C_(K,rho)(R+1)^(2K)`. Also `sum_d|c_d|+sum_de_d<=H^o(1)`, either by (12) and d<=D_H or by the same finite enumeration bound. These statements do not use the product of a whole band, nor the product of all b copies.

For the actual positive error, simple integer counting is sufficient and retains the endpoint term:

\[
 \begin{split}
 \sum_{p\in I,p<H}(\log p)E_F(H-p)
 &\le L\sum_de_d\{H/d+1\}\\
 &\ll_{K,\rho} HL/R!+H^{o(1)}L
   =O_A(HL^{-A}).
 \end{split}\tag{14}
\]

The model error uses the 1/phi(d) version of (12). Since R! exceeds every fixed power of L eventually, both errors have any requested fixed logarithmic accuracy. The explicitly retained +1 accounts for arbitrarily short intervals and rare divisors; model smallness alone was not used as an arithmetic remainder bound.

### Passage to actual primes from the primary BV input

The imported statement is [Koukoulopoulos, *The Distribution of Prime Numbers*, Chapter 26, equation (26.1)](https://www.dms.umontreal.ca/~koukoulo/documents/publications/primes.pdf), inspected on printed page 277. For fixed B>=0 it states

\[
 \sum_{d\le Q}\max_{z\le H}\max_{(a,d)=1}
 \left|\pi(z;d,a)-\frac{\operatorname{li}(z)}{\varphi(d)}\right|
  \ll_B HL^{-B-1},\qquad Q\le H^{1/2}L^{-B-3}. \tag{15}
\]

The author-provided PDF and render hashes, and distinct visual inspection, are recorded in primary-inputs.md, pre-mortem.md and source-provenance.json. This is primary theorem-statement assurance, not audit of the entire published proof. We import precisely (15), not a full Guo or LWW theorem.

For fixed d, real partial summation of its counting-prime error multiplies the endpoint maximum by at most 2L+O(1); subtracting two endpoints only changes a constant. Thus (15) gives the sum of endpoint-uniform log-prime AP errors with one fixed logarithmic loss. Its main term on I is |I|/phi(d), up to a bounded endpoint convention error O(1/phi(d)). The d=1 case also gives `Theta_H(I)=|I|+O_B(HL^(-B))`, with the same harmless bounded endpoint error. These formulas include intervals meeting 0 or 2 after absorbing O(1).

Choose B larger than A and the fixed coefficient log loss in (13). Eventually D_H is below (15)'s level. Since (d,H)=1, each retained class H modulo d is reduced. It follows that

\[
 \sum_{p\in I,p<H}\log p\,P_F(H-p)
  =|I|\sum_d\frac{c_d}{\varphi(d)}+O_A(HL^{-A})
  =\Theta_H(I)\sum_d\frac{c_d}{\varphi(d)}+O_A(HL^{-A}). \tag{16}
\]

Indeed the error sum is at most `max|c_d|` times the BV error sum, while replacement of |I| uses the bounded absolute reciprocal coefficient mass in (12). The finite local model satisfies `E 1_(d|w)=1/phi(d)` exactly. Equations (12),(14),(16) therefore give

\[
 \sum_{p\in I,p<H}\log p\,F(H-p)
      =(\mathbb EF)\Theta_H(I)+O_A(HL^{-A}), \tag{17}
\]

because the additional model error is O(Theta_H(I)/R!) and Theta_H(I)<=O(H). The model means are m_j and m_jm_k, proving (4). There is no von-Mangoldt-to-prime conversion in (15)-(17), hence no omitted higher-prime-power correction in this step. If an application discards the primes p dividing H, their total log mass is at most log H; bounded true F and X_j restore them at O_(K,rho)(L). This is distinct from the two genuine prime-power corrections in TYPEI-013's decomposition.

### Variance and the exact order of limits

Divide (4) by the positive means in (3). With dmu(p)=log p on the actual primes, the first moments of X_j and the mixed moments X_jX_k are Theta_H(I)+O_(A,b,a)(HL^(-A)). The diagonal inequality in (9) gives

\[
 \begin{split}
 \int\left(\frac1b\sum_jX_j-1\right)^2d\mu
 &\le\left\{\frac{C_X}{b}+\frac{b-1}{b}-2+1\right\}\Theta_H(I)
      +O_{A,b,\boldsymbol a}(HL^{-A})\\
 &=\frac{C_X-1}{b}\Theta_H(I)+O_{A,b,\boldsymbol a}(HL^{-A}).
 \end{split}\tag{18}
\]

All quantities in the square are real. Cauchy on this same positive measure bounds the left side of (6) by C_f times the square root of Theta_H(I) times (18); Theta_H(I)<=O(H) proves (6). It would be invalid to substitute a variance on integers or root points.

Suppose that, for every fixed b and its chosen array,
`sum_(p<H) log p f_H(p) X_j(H-p)=o_(b,a)(H)` for each of its finitely many j. The same holds for their average. Equation (6) implies

\[
 \limsup_{H\to\infty}\frac1H
       \left|\sum_{p<H}\log p\,f_H(p)\right|
   \le C_f C_{K,\rho}/\sqrt b. \tag{19}
\]

This is true for every fixed b with the same leading constant, so sending b to infinity gives o(H). For an epsilon proof, choose b to make the right side small, then choose H above that fixed array's thresholds. No b growing with H is asserted. The array `e_b(H)=1_(H<=exp(exp(b)))` tends to zero for each fixed b but equals one for b=ceil(log log H); it refutes an automatic growing-family substitution.

## Candidate 2: the actual reflected-prime consequence

**Claim, proved pending review, with the stated dependency scope.** For every fixed C, along even H with rad(H)<=log^C H,

\[
 \sum_{p<H}\mu(H-p)\log p=o(H),\qquad
 \sum_{p<H}\mu(H-p)=o(\pi(H)). \tag{20}
\]

The same conclusions hold on any general even-H sequence satisfying the explicit fixed-b family of selected-strip hypotheses defined below. On the small-radical class no extra selected-strip hypothesis is needed after the inspected classical inputs and reviewed deductions. Here and below pi(H) denotes the ordinary prime-counting function, distinct from pi_r in the local model.

### Actual accepted dependencies and their limits

These are written mathematical dependencies, not inferences from packet completion, replay or finite agreement. Each listed revision has a positive distinct mathematical review. The current Candidate 2 still awaits its own separate review.

| Dependency | Accepted contribution used here | Retained restriction |
| --- | --- | --- |
| ROOTS-008, revision SHA256 `cff39441bcff8923153f18da3ea6ee1bcdba37439e4a8d70351ac00554ce1b7e` | Unit determinant-H joint root replacement with all S and tau(H) costs and its actual aspect range | Used through the reviewed moment proof, not outside its aspect range |
| TRACE-009, revision `07a29496d5f256bb5c5c883242515cff07029e59e72e2c52bedf86f83ddbe97e` | Ambient restricted Gram and actual endpoint list-fiber inequalities | No pointwise deletion of signed paths and no required full enlarged trace |
| MOMENTS-010, revision `947cc0c9b1fbcb79b9f221246bbc2ecf056dcdd9decf0543b508a3b7ee2931ba` | Eligible independent-line edge/memory/distinctness bound and arithmetic path replacement | Same eligible state spaces and kernels; controlled original-box/good boundaries; physical paths and finite damping before memory expansion |
| PAIRING-011, revision `21a75c833070b1436e69d6951dec67aad602f47d061b4e307c3f069aaf7a4f51` | Signed-cofactor nonnegative square, positive bad-root removal, and `Q_all-Q_maj=O(HY L^(-P))` | Original positive shifted endpoint only before Cauchy; no nonfactorable product mask in the operator; real eta and plateau psi; actual ordered harmonic normalization |
| ENERGY-012, revision `89a8963af5d1bdb724d57e8a0be12cea6a7779f5fc21ff20ed6043b53fc2e9e1` | Actual Mobius/long-prime-factor major comparison `Q_maj=O(HY L^(-P))` at sufficient precision | Fixed twist in each Gram family, classwise Cauchy before Parseval, two Mellin variables, 1/Y arc factor and YX^2 prefactor; selected strip for general H |
| TYPEI-013, revision `8e1c40489618673257f07dbdafc84cac7be910f486cb0dbf49787462592b75a2` | Exact sifted Vaughan identity, both prime-power corrections, reflected Type I, comparable inherited V0 extension, common global bands/parameters and marked-prime assembly | Correct arithmetic roles, endpoint/phase ceiling and unit costs; W still present |

The initial surveys' statements that 012 or 013 were pending are historical preparation. Their actual reviewed revisions now supply the dependencies above. None is replaced by accepting the full Guo/LWW theorem. The classical inputs remain exactly those named there: the inspected prime and Mobius BV statements, published MSTT subinterval-supremum and Burgess r=2 statements, the original Iwaniec statement, and the declared completed-L continuation/functional equation, order/growth and Hadamard background. Statement-level inspection is not full proof audit of those classical sources.

### Marked assembly, precision order and general-H quantifiers

Fix rho first and request marked accuracy A_m=2. Choose a low-prime cutoff exponent B_low=5 and dyad lower-range exponent B_d=6. Choose smoothing precision B_s>A_m+10, for example 14, and then cofactor-square precision

\[
 P>2(A_m+B_d+2B_s+5). \tag{21}
\]

These choices precede later moment and energy parameters. In TYPEI-013 the product-strip errors are `O(L^3(L^(-B_s)y+sqrt(y)))`; there are O(L^2) rectangles, O_K(L) selected-product blocks and a smooth Mellin L1 loss O(L^(2B_s)). The phase ceiling is L^(2B_s) and is fixed before the energy height. The moment accuracy/operator parameters and K are then fixed as in the accepted 010/011 proofs. K remains the same for every copy and every b. The required energy accuracy, its heights and selected-strip constants are fixed afterwards, at the required phase ceiling. Band exponents are selected only after these finite-precision choices. Fixed positive gaps between them affect thresholds, not the leading bound (9).

On a rectangle the accepted difference and energy bounds combine to `Q_all=O(HY L^(-P))`. The actual cofactor Cauchy is

\[
 |T_Y|^2\ll (H/Y)Q_{\rm all}\ll H^2L^{-P}. \tag{22}
\]

Thus the square-root accuracy is P/2, before restoring H/y<=L^(B_d), rectangles, product blocks and the Mellin L1 cost. Inequality (21) leaves a fixed reserve for those losses. The accepted Type-I proof handles the remaining convolution terms at the higher precision it needs. The exact decomposition also restores small prime bases at cost `O(Z)` and removes higher powers at `O(sqrt(y)log^2(2y))`, with `Z=exp(L^(3/4))`; both are negligible because y>=H/L^(B_d). Unit losses are exponentially small on these scales, or O(L) when restoring the prime divisors of H.

The exact common `V0=y^(1/5)` is inherited on every rectangle; ENERGY-012 initially stated V0=X^(1/5) with X=MN. TYPEI-013's accepted comparable-threshold extension, rather than a renaming of X, checks beta<=log n, V0 comparable to X^(1/5), V0>=H^(1/6), 2N<=H and the negligible inner restriction cost `(Z+L)/V0`. The global L, eligible bands, W, J,R, good tests and full-pullback arcs stay the same across rectangles. Only the bounds are expressed using the comparable rectangle logarithm. With these checks, for each j,

\[
 \sum_{y<p\le t}(\log p)\mu(H-p)W_j(H-p)
     \ll_{j,b,\boldsymbol a} yL^{-2},
 \quad H/L^6\le y\le H/2,\quad y<t\le2y. \tag{23}
\]

To state the general-H scope without hidden uniformity, choose for each fixed b its finite array and any valid accepted parameter selection above. Let `Sigma_b(H)` be precisely the finite selected-strip requirements of that choice: for its fixed constants C_(1,b),C_(2,b),A_(0,b),A_(1,b), every primitive inducing conductor

\[
 q^*\mid kH,\quad k\le L^{A_{0,b}},\quad q^*>L^{A_{1,b}}
\]

has no zero in the rectangle

\[
 \Re s\ge1-C_{1,b}\log L/L,\qquad |\Im s|\le L^{C_{2,b}}. \tag{24}
\]

If a choice uses several such rectangles, Sigma_b is their finite conjunction. The conditional general-H conclusion (20) is along a sequence for which, **for every fixed b, Sigma_b(H) holds eventually on that sequence**. The thresholds and even the chosen constants in (24) may depend on b. A single rectangle at one precision has not been asserted to imply all these requirements. Nor has one chosen width been asserted to give every logarithmic saving. This family formulation is sufficient for (19). It avoids needing an unproved uniform zero-free assertion in b.

For rad(H)<=L^C with fixed C, the accepted ENERGY-012 deduction supplies every fixed rectangle required here: `rad(q*)<=L^(A_(0,b)+C)`, `q*<=H L^(A_(0,b))`, and the inspected Iwaniec width is at least a constant times `L^(-3/4)(log L)^(-3/4)`. This exceeds every fixed `C_(1,b)log L/L` eventually. A real primitive conductor is at most eight times its radical, so choosing `A_(1,b)>A_(0,b)+C` excludes any possible real exceptional conductor above the cutoff. Conductors below the cutoff stay in the accepted MSTT/Burgess branch. This covers all q* dividing kH, not merely those dividing H. The eventual thresholds may depend on b,C and the selected constants, exactly as the successive limits allow.

### Terminal marked sums and removal

Partition the primes below H into dyads `(H/2^(n+1),H/2^n]` down to a lower endpoint between `H/(2L^5)` and `H/L^5`. Every dyad meets (23)'s lower bound for large H. Their y lengths have sum at most H. Uniformity in the upper endpoint covers a final partial interval if used. Their marked sum is therefore `O_(j,b,a)(HL^(-2))`. The remaining low primes contribute at most

\[
 C_W\sum_{p\le H/L^5}\log p\ll_{K,\rho}H/L^5,
\]

by the ordinary Chebyshev/PNT bound. Hence for each fixed j,b,

\[
 S_j(H):=\sum_{p<H}\log p\,\mu(H-p)W_j(H-p)=o_{b,\boldsymbol a}(H). \tag{25}
\]

Division by m_j>=m_0/2 preserves this. Since the average has finitely many j, its normalized marked sum is o_(b,a)(H). Apply (19) with the actual target f_H(p)=mu(H-p), whose absolute value is at most one. On either stated H-scope, for every fixed b its required estimate eventually holds, so the limsup is at most C_(K,rho)/sqrt(b). Letting b grow only after this limsup proves the first part of (20).

For completeness, logarithmic unweighting uses no claim about prefix cancellation for a changing f_H. For any |f_H(p)|<=1, choose fixed D>2 and split at T=H/L^D. On p>T,

\[
 |1-\log p/L|\le D\log L/L,
\]

and pi(H)<=O(H/L). On p<=T the difference is at most one and there are at most T primes. Thus

\[
 \sum_{p<H}f_H(p)=\frac1L\sum_{p<H}f_H(p)\log p
      +O_D\left(\frac{H\log L}{L^2}+\frac H{L^D}\right). \tag{26}
\]

Using the first part of (20) and pi(H)~H/L proves its second part. No differentiation of the reflected target and no unsupported full-dyad-prefix theorem occurs in (26).

## Closest work, falsifiers and the remaining task

The pinned [Guo source](https://github.com/aster2024/openai-math-followups/blob/a605351dce1a55fb46a494d9cca9b0baa8f2734b/mobius-goldbach-shift/source/main.tex), byte hash `e70d777424852aed92e94b2baf00384c84b4c7fc346bd7dab1085d5652ced95d`, already has these prime-relative means, positive fixed-number variance, successive-limit removal and closely related reflected-prime conclusions. Its Theorem G retains H2' plus a selected strip; its Theorem S retains H2' plus the small-radical classical deduction. The local source lines 3109-3250 and 3436-3512 were inspected as data. Their conditional conclusions are not used as the proof of an input here. The present contribution is the explicit reconstruction and dependency audit, including the actual separately reviewed 008-013 arguments, rather than validation of every Guo/LWW statement or a claim that the framework is new. The source's later growing-family packing and explicit-rate argument is outside this stage.

The smallest population falsifier is r=3,H=2 above. Empty bands would make V or m undefined, so eventual positivity from (8) is essential. Disjointness is what gives the off-diagonal mean one; identical copies in an abstract nonconstant Bernoulli model keep their variance independent of b and refute dropping it. The fixed-b counterarray following (19) refutes an unproved growing-b rate. These true counterexamples concern the omitted-hypothesis assertions, not the retained claims.

Even (20) does not isolate prime complements. At H=206 and prime p=101, `mu(H-p)=mu(105)=-1`, although 105=3*5*7 is composite. Zero values from repeated factors are also retained in the target, and sign cancellation does not give a count of all rough odd-factor complements. In the original task, for alpha=1/3-epsilon one still needs a positive pointwise lower margin for the polynomial-rough odd-factor count F_alpha strong enough to exceed the accepted three-factor upper bound of order `epsilon^2*S(H)H/log^2 H`. Neither (20), whose error is only little-o of H/log H, nor the subpolynomial band weights supply that margin. In fact every W_j vanishes on complements with no divisor below H^alpha once H is large, so applying its marked cancellation directly on that rough set would provide no information. Polynomial roughness, the nonzero parity center and the h=1 prime boundary remain separate arithmetic obligations.

The next tractable proof obligation is an actual one-sided estimate for that correctly centered polynomial-rough target at its H/log^2 H scale, with the prime boundary retained. It cannot be supplied by another substitution of local probabilities or by growing b in (19). A decisive review check for the present statement is instead the finite-to-prime error (14)-(17) and the exact dependency/zero-free quantifiers in (21)-(25). No finite experiment or harness protocol execution establishes their analytic validity. The user's Goldbach objective remains active and unsolved.
