# Revised pointwise lower-bound attempt

29 October 2026. Registry role: Mathematician, `GOLDBACH-LOWER-003`. This revision uses the populated `revise` packet and the separate `lower-review.md`. The frozen `lower-proposal.md` and root-authored `local-gap.md` remain unchanged. No new source search or computation was performed in this stage.

## Accepted reduction and its scope

The critic supports the corrected decomposition, relative to the explicitly inspected unconditional coefficient estimates in Huang-Li Lemmas 1 and 3 and ordinary Bombieri-Vinogradov. For fixed 0<theta<1/2, Q=N^theta, every requested fixed logarithmic saving A is available in

\[
G(N)=\mathfrak S(N)(N-B_N)+\mathcal O_N(Q)
                   +O_{A,\theta}(N/\log^A N), \tag{1}
\]

where G(N) is the ordered prime-prime sum with weights log p log q, B_N=sum_{1<=n<N}Lambda(n)mu(N-n), and the signed operator is exactly

\[
\begin{split}
\mathcal O_N(Q)=\sum_{\substack{1\le k<(N-1)/Q\\(k,N)=1}}\mu(k)
\left\{
\sum_{\substack{1\le n\le M_k\\n\equiv N\ (k)}}
 f_N(n)\log\frac{k}{N-n}
-\frac1{\phi(k)}\sum_{1\le n\le M_k}
 f_N(n)\log\frac{k}{N-n}\right\},\\
f_N(n)=\Lambda(n)\mu(N-n),\qquad
M_k=\max\{0,\lceil N-Qk\rceil-1\}.
\end{split} \tag{2}
\]

The strict moving endpoint and plus sign of the operator are retained. The noncoprime part is explicitly bounded by O((N/Q)log^3N), rather than discarded. The short-divisor term uses only ordinary BV: all its moduli are at most Q times a fixed power of log N, below the square-root BV range for fixed theta<1/2. The reviewed lcm tail, O(B^2) modulus multiplicity, prime-power corrections and short-h interval bounds justify the stated error. The reduction does not assume a twisted-distribution conjecture.

This is an alternative route to ordinary sufficiently-large Goldbach. Even if its missing estimate were proved, it need not establish the stronger original fixed-epsilon lower margin for the rough odd-factor count F_alpha.

## Sharper local margin, including its target dependence

The unconditional bias bound is

\[
B_N\le\mathcal A(N)N+O_A(N/\log^A N),\qquad
\delta_N=1-\mathcal A(N),\quad
\mathcal A(N)=\prod_{\substack{p\nmid N\\p>2}}
       \left(1-\frac1{p(p-1)}\right).
\]

The separate critic also supports the root-authored proposition in `local-gap.md`:

\[
\boxed{\mathfrak S(N)\delta_N\gg\frac1{\log N}}
\quad\text{uniformly for sufficiently large even }N. \tag{3}
\]

The gap delta_N alone can tend to zero. The sharper bound keeps its compensation by the singular series. Its proof uses PNT to count missing prime divisors below 4log N. Either one missing prime lies below sqrt(4log N), directly giving a large enough gap, or all primes below that boundary divide N and Mertens' product estimate makes the singular series large enough. These cases give (3) without using any Goldbach representation.

The order is sharp: along primorial targets N_y=product_{p<=y}p,

\[
\mathfrak S(N_y)\delta_{N_y}\sim e^\gamma/\log N_y.
\]

Thus the product cannot be replaced by a uniform positive absolute constant. Numerical constants and an explicit threshold have not been extracted. This is a classical local-factor refinement with a complete reviewed argument, not a new distribution estimate or claimed result of novel priority.

## The remaining sufficient inputs

The one-sided signed condition remains

\[
\mathcal O_N(N^\theta)\ge
 -(1-\kappa)\mathfrak S(N)\delta_N N
\quad\text{for all sufficiently large even }N, \tag{O-open}
\]

for one fixed theta in (0,1/2) and one fixed kappa in (0,1). Combining it with (1)-(3), requesting errors o(N/log N), would imply G(N)>0. **O-open is not proved.**

Define the unweighted partial-sum discrepancy for the same reflected sequence by

\[
E_k(j)=\sum_{\substack{1\le n\le j\\n\equiv N\ (k)}}f_N(n)
 -\frac1{\phi(k)}\sum_{1\le n\le j}f_N(n).
\]

The already reviewed endpoint-transfer lemma gives

\[
|\mathcal O_N(N^\theta)|\le\log(N-1)
 \sum_{\substack{k<N^{1-\theta}\\(k,N)=1}}\max_{j<N}|E_k(j)|.
\]

Therefore the stronger sufficient input can now be weakened to

\[
\boxed{\sum_{\substack{k<N^{1-\theta}\\(k,N)=1}}
 \max_{j<N}|E_k(j)|
 =O\!\left(N/(\log N)^{2+\eta}\right)} \tag{T2-open}
\]

for some fixed eta>0. It would make the operator O(N/(log N)^(1+eta))=o(N/log N), below the uniform margin (3). Thus it would imply O-open, for example with kappa=1/2 eventually. The old exponent 3+eta in the frozen proposal was sufficient but unnecessarily strong because it bounded delta_N separately. **T2-open remains unproved.** No full endpoint may replace the maximum over j.

The direct absolute-value estimate obtained in the proposal is only O(N log^3N), which is four logarithms larger than the guaranteed N/log N margin. This is a comparison between available bounds, not evidence that the actual operator has that magnitude. Ordinary BV controls Lambda, not Lambda(n)mu(N-n); replacing its terms by this reflected Möbius twist is not allowed. The complementary moduli also extend to N^(1-theta)>N^(1/2), and exchanging theta with 1-theta merely moves an unproved distribution requirement to the other side.

## The second attempted mechanism still fails quantitatively

For the direct rough lower sieve with z=N^alpha and alpha in [0.3,1/3], ordinary BV gives D=N^(1/2)/(log N)^B. Hence the dimension-one sifting parameter is

\[
s=\log D/\log z=1/(2\alpha)-o(1)\in[3/2,5/3]-o(1)<2.
\]

The available lower sieve does not even yield a positive general coefficient for the full rough set at this cutoff. Crossing this particular threshold would require D>z^2=N^(2alpha), missing a factor between N^0.1 and nearly N^(1/6), before any logarithmic losses. The desired odd-factor lower bound requires additional parity information.

The specialized Friedlander-Iwaniec route instead requires D>N^(2/3), its explicit absolute-outer-sum Möbius bilinear bound for the reflected-prime sequence, and uniform control as N changes its local density function. None was established here. The source theorem supplies an implication under those inputs; it does not prove them for this sequence.

## Assurance and objective status

The complete derivations and supplemental local-factor argument have separate host-agent mathematical review, relative to the inspected imported analytic lemmas. This is neither a proof-assistant check nor external human peer review. The source chain behind the imported coefficient estimates was not fully re-proved. No numerical constants, explicit finite threshold or all-N connection were obtained.

No unconditional cancellation estimate for O-open, T2-open, or the specialized bilinear expression has been proved. No original rough F margin, Goldbach proof or demonstrated breakthrough has been obtained, and no novelty claim is made. The active objective remains open.

## A distinct next bounded route

A next attempt should change the available mechanism rather than restate (2). One concrete option is a weighted Buchstab switching minorant for the original F count. Begin at a lower roughness exponent beta<1/4, where ordinary BV permits a positive dimension-one lower-sieve coefficient, and use the exact identity

\[
U_\alpha(N)=U_\beta(N)
 -\sum_{N^\beta<r\le N^\alpha\atop r\text{ prime}} C_r(N),
\]

where C_r counts prime summands whose complement has least prime factor r. For alpha in the reviewed near-cubic range, F_alpha=U_alpha-E_alpha exactly, with E_alpha the semiprime-complement count. Thus a chosen collection of pointwise upper bounds for C_r and E_alpha, combined with a lower bound for U_beta, produces an actual minorant for F_alpha.

The bounded task is to write one explicit switching decomposition, track its factor-order and coefficient ranges, and optimize the resulting sieve integrals under only inspected unconditional inputs. Its output must be either a rigorously positive lower coefficient exceeding the reviewed contamination, or a checked certificate that this particular minorant remains nonpositive. Negative outcomes are informative. Unproved cancellation must not be inserted to repair a negative coefficient. This uses nonnegative combinatorial switching and explicit upper/lower bounds, rather than another notation for the same signed AP operator. It may still fail, and no success or new budget is implied by identifying it.
