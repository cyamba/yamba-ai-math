# CUBIC022 final revision after independent mathematical challenge

29 October 2026. Actual original-author revise stage, round 1. This revision preserves the frozen proposal and challenge.

**Final mathematical verdict: incomplete for the requested fixed constant gap.** The independent critic supports the two actual signed \(o(M_N)\) sectors, the separate rough squareful long error, and the exact residual partition. No assertion of the frozen proposal was refuted. The critic's critical finding F1 is accepted: the required lower bound for the three actual residuals is unproved. No Goldbach theorem, fixed positive \(\delta\), power-of-two improvement, substantive breakthrough or novelty determination is claimed.

This is a bounded revision of the same two mechanisms. No new mechanism, helper, numerical search, source search, inference supplement or extra round was used.

## 1. Frozen evidence and assurance

The populated revise packet, including its Mathematician role, brief, output contract and actual challenge result, was read. The full frozen review was read, and its SHA256 matched the assigned value. The mathematical proof remains the complete derivation in statement.md, with the critic's complete independent checks in review.md. This revision incorporates those proofs by reference to the exact frozen hashes and records the final scope and unresolved obligation below.

| Frozen input | SHA256 |
| --- | --- |
| statement.md | 9f385113df4b561399311ece472e41affd989ff187a93bdbec66a8d1cccffa5a |
| review.md | 4eaf6c19f2e36a5822915e5f1029cd4311ce09b79fe2131fdfcd49ff7bae5d1b |
| source-provenance.json | d9f5054a3f1d8048b2e47c9aa7b8ebe0fe868491b5e8bf9fb8b5df1ef2608114 |
| .runs/goldbach-cubic-022-manual-20261029/packets/revise.json | 40eeb4927e2a7d33e6e96e5659b247b6f2568045cae2ea77aa8733986ff2acfd |

The current provenance record has nine inputs: seven Arneth files and the Koukoulopoulos preliminary book PDF and page-277 render. Root reported verification of all nine. In this stage the provenance record and its hash were checked; root's wider file verification is not represented as a new source-proof audit by this author.

Assurance is human-readable derivation plus distinct-role independent mathematical review. It is not proof-assistant certification, source-wide semantic certification, or a claim of statistically independent model errors. Claim 1 expressly imports the classical maximal Bombieri–Vinogradov theorem. The inspected primary statement is Koukoulopoulos, *The Distribution of Prime Numbers*, preliminary version, printed p.277, (26.1), preserved in the nine-file provenance. The classical proof of that theorem is not reproduced here. No unproved assertion from Arneth Hypothesis 8.2 is imported.

## 2. Exact operator and unchanged target

For even \(N\), put
\[
 L=\log N,\quad I=(N/3,2N/3]\cap\mathbb N,\quad
 y=N^{1/6},\quad z=L^4,\quad D=N^{1/2}L^{-B}.
\]
The point weight \(\theta(m)\) is \(\log m\) when \(m\) is prime and zero otherwise. Retain the full radical wheel, normalization and atom:
\[
 W=\operatorname{rad}\left(N\prod_{p\le z}p\right),\quad
 \kappa={W\over\varphi(W)},\quad
 u(n)=\theta(N-n)-\kappa1_{(N-n,W)=1}
                  -\theta(N/2)1_{n=N/2}.
\]
Define
\[
 \Phi(t)=1-3t^2+2t^3,\quad
 h_{>y}=\prod_{\substack{p\mid h\\p>y}}p,\quad
 C_D(n)=\sum_{\substack{h\mid n\\h>D}}\mu(h)
                   \Phi\left({\log h_{>y}\over\log n}\right).
\]
Then
\[
\begin{split}
 H_{3,D}(N)
 &=\sum_{1\le k\le2N/(3D)}
     \sum_{\substack{h>D\\kh\in I}}
       \mu(h)\Phi\left({\log h_{>y}\over\log(kh)}\right)u(kh)\\
 &=\sum_{n\in I}u(n)C_D(n).
\end{split}                                                   \tag{V1}
\]
The variable \(k\) is an integer and includes one. Products need not be rough or squarefree. The \(I\) endpoints and the true \(h_{>y}\) are unchanged.

The normalization remains
\[
 \mathfrak S(N)=2\prod_{p>2}\left(1-{1\over(p-1)^2}\right)
       \prod_{\substack{p\mid N\\p>2}}{p-1\over p-2},
 \qquad M_N={\mathfrak S(N)N\over3L}.
\]
The target is a fixed \(\delta>0\) with
\[
 H_{3,D}(N)\ge-\left({3\over4}-\delta+o(1)\right)M_N
                                                               \tag{V2}
\]
for every sufficiently large even \(N\). The source leaves this signed assertion open. The deductions below do not prove it, even on all sufficiently large powers of two.

## 3. Retained proved deductions and their exact limitations

### 3.1 Tiny-prime product sector, relative to classical BV

Fix \(B\ge8\). Set
\[
 w=\left\lfloor{\log L\over4\log\log L}\right\rfloor,\quad
 G=\prod_{p\le w}p,\quad
 H_{\le w}=\sum_{\substack{n\in I\\(n,G)>1}}u(n)C_D(n).
\]
The retained result is
\[
 H_{\le w}
 =O\left({N\over L^{3-o(1)}}+N^{15/16+o(1)}
                         +N^{3/4+o(1)}\right)=o(M_N).           \tag{V3}
\]
Its complete proof is frozen statement (2)–(7), independently checked in the review's Supported deduction 1.

The key exact step is worth preserving. For squarefree \(g\mid G\), \(g>1\), restrict products by \(g\mid n\), and write contributing divisors uniquely as \(h=ed\), \(e\mid g\), \((d,g)=1\). The large-prime-part weight is independent of \(e\). Its summed coefficient
\(\sum_{e\mid g}\mu(e)1_{ed>D}\) vanishes outside \(D/g<d\le D\). After imposing \(g\mid n\), the actual progression modulus is \(m=gd\). Thus
\[
 H_g=\sum_{\substack{D<m\le gD\\g\mid m\\(m/g,g)=1}}
       \lambda_g(m)U_m,\quad
 |\lambda_g(m)|\le\tau(g),\quad
 U_m=\sum_{\substack{n\in I\\m\mid n}}u(n)
                   \Phi\left({\log m_{>y}\over\log n}\right).
\]
Products \(n\) may have repeated prime factors. For \(g=p\), the coefficient is exactly \(\mu(m)\) on \(D<m\le pD,\ p\mid m\).

The critic supports the complete error budget: the true model density
\[
 g_b(m)={1\over\varphi(m)}
       \prod_{\substack{p\mid m\\p\nmid W}}(1-1/p)
\]
has total mismatch \(O(L^{-3})\), rather than being silently replaced by \(1/\varphi(m)\). Adjacent small-prime Bonferroni orders near \(L/(16\log L)\) retain products at most \(N^{1/4+o(1)}\); the exact divisor expansion of \(F=\prod_{p\mid N,\ p>z}p\) costs \(2^{\omega(F)}=N^{o(1)}\). The inequalities are applied to a positive \(F\)-sieved count before its signed expansion. Weighted partial summation retains the actual endpoints and has bounded variation.

BV with \(A=4\) applies up to \(Q\le\sqrt N L^{-7}\). Here \(G\le w!\le L^{1/4}\), so \(GD\le\sqrt N L^{1/4-B}\) lies in that range. The sum of product inclusion–exclusion coefficient costs is \(3^{\omega(G)}=L^{o(1)}\). Noncoprime rows vanish using the correction atom, and the only atom on a coprime row is the \(m=1\) contribution when \(N/2\) is prime.

This does not permit \(p\) to grow up to \(y\): the exposed shell \(D<m\le pD\) then extends as far as \(N^{2/3}L^{-B}\). Classical BV in the imported range supplies no control there. This limitation is retained.

### 3.2 Odd squarefree rough central strip, elementary proof

For squarefree \(y\)-rough \(n\), let
\[
 {\cal C}(n)=\{h\mid n:D<h<n/D\},\qquad
 T(n)=\sum_{h\in{\cal C}(n)}\mu(h)\Phi(\log h/\log n).
\]
For every fixed \(B>0\), the retained result is
\[
 E_{\rm odd}:=
 \sum_{\substack{n\in I\\P^-(n)>y\\\mu(n)=-1}}u(n)T(n)
 =O_B\left({\mathfrak S(N)N(\log L)^5\over L^2}
                                   +\log L\right)=o(M_N).       \tag{V4}
\]
Its complete proof is frozen statement (8)–(17), independently checked in Supported deduction 2 of the review.

The strict central set is invariant under \(h\mapsto n/h\) once \(D^2<n\). Its exact complement among long divisors is the closed outer set \(h\ge n/D\), corresponding to \(d=n/h\le D\). With \(t_h=\log h/\log n\), squarefreeness and roughness give
\[
 T(n)={1\over2}\sum_{h\in{\cal C}(n)}\mu(h)
        [\Phi(t_h)+\mu(n)\Phi(1-t_h)].
\]
For \(\mu(n)=-1\) the bracket is \(2\Phi(t_h)-1\). The bound
\(|\Phi'|\le3/2\), \(\Phi(1/2)=1/2\), and at most 32 divisors give
\[
 |T(n)|\le48\left({1\over2}-{\log D\over\log n}\right)
                   =O_B(\log L/L).
\]
The necessary actual mass bound is
\[
 \sum_{\substack{n\in I\\P^-(n)>y}}|u(n)|
                  \ll{\mathfrak S(N)N(\log L)^4\over L}+L.
\]
It uses an even upper Bonferroni order
\(K=2\lfloor(\log L)^2/32\rfloor\), with
\(q=\exp(L/(\log L)^2)<y\). Retained products are at most \(N^{1/16+o(1)}\). Their total lattice error is bounded by the divisor sum, and the factorial tail is \(O_J(L^{-J})\) for every fixed \(J\).

For the actual term, sieve both \(n\) and \(N-n\) by primes at most \(q\), with one excluded root for \(p\mid N\) and two otherwise, retaining the full singular-series factor. For the model upper bound, sieve \(n\) by \(p\le q\) and \(N-n\) by \(p\le z\), retaining the true \(\kappa\). Its mixed density is \(P_qV_N(z)\), and direct local multiplication gives
\[
 \kappa V_N(z)=\mathfrak S(N)
 \prod_{\substack{p>z\\p\nmid N}}
             \left(1-{1\over(p-1)^2}\right)^{-1}
                    \ll\mathfrak S(N).
\]
This explicitly keeps the prime divisors of \(N\) in the model normalization. The correction atom costs at most \(L\). No actual-prime sign is inferred from a comparison mass.

The even-parity extension remains excluded. A central rough semiprime \(n=pq\) has
\(T(n)=-\Phi(\log p/\log n)-\Phi(\log q/\log n)=-1\).
As the critic records, comparable distinct primes with ambient \(N=2pq-2\) give arbitrarily large admissible coefficient examples. This refutes a pointwise suppression extension, already disclaimed in the proposal. It does not refute an eventual inequality weighted by the actual \(u\).

Nonrough products are not covered by this symmetry: complementary large-prime logarithms sum to \(\log(n_{>y})/\log n\), not one, and squareful products lack the needed Möbius complement relation.

## 4. Accepted F1 and exact unresolved arithmetic

The separate rough squareful long error remains
\[
 E_{\rm sf,long}=O(N^{5/6}L^4)=o(M_N).
\]
This follows from at most 32 contributing squarefree divisors on each rough product and at most \(O(N^{5/6})\) rough squareful products. It is a bound on the long operator itself. It neither discards nonrough squareful products nor certifies the different full-minorant squarefree-removal ledger in source (8.3).

The actual residuals retained without change are
\[
\begin{aligned}
 R_{\rm nr}&=\sum_{\substack{n\in I\\w<P^-(n)\le y}}u(n)C_D(n),\\
 R_{\rm even}&=\sum_{\substack{n\in I\\P^-(n)>y\\\mu(n)=1}}u(n)C_D(n),\\
 R_{\rm outer,odd}&=
 \sum_{\substack{n\in I\\P^-(n)>y\\\mu(n)=-1}}
 u(n)\mu(n)\sum_{\substack{d\mid n\\d\le D}}\mu(d)
             \left[1-\Phi\left({\log d\over\log n}\right)\right].
\end{aligned}                                                     \tag{R}
\]
The exact support identity, supported by the critic, is
\[
 H_{3,D}=H_{\le w}+E_{\rm sf,long}+E_{\rm odd}
                           +R_{\rm nr}+R_{\rm even}+R_{\rm outer,odd}.
                                                               \tag{V5}
\]
The remaining nonrough interval \(w<P^-(n)\le y\) includes every remaining nonrough squareful product. The closed outer boundary \(d\le D\) is present. All integer cofactors and \(k=1\) are retained: on rough products its true weight \(\Phi(1)\) is zero, whereas the generally nonzero nonrough \(k=1\) term remains in \(R_{\rm nr}\).

The only general bound obtained here is
\[
 |R_{\rm nr}|+|R_{\rm even}|+|R_{\rm outer,odd}|\ll NL^5.
\]
It follows from \(|u|\ll L^4\) and the divisor sum. It supplies no fixed margin at the \(M_N\) scale.

**Response to F1: accepted and unresolved.** No proof is obtained of
\[
 R_{\rm nr}+R_{\rm even}+R_{\rm outer,odd}
       \ge-\left({3\over4}-\delta+o(1)\right)M_N
                                                               \tag{V6}
\]
for any fixed \(\delta>0\), uniformly over all sufficiently large even \(N\). Equation (V6) is statement (21), the precise first failed load-bearing inequality. The critic identifies an evidence gap, not a counterexample to (V2), and this revision makes no repair claim. The two signed sector estimates remain valid at their stated assurance.

A bounded next proof obligation is an actual weighted estimate for the even rough semiprime central sector together with its outer terms, preserving the wheel, atom and endpoints. Success there alone would still leave the other residuals. No earlier 014, 018, 019 or 021 result has been transported to these different weights or ranges. No source comparison asymptotic or conditional Goldbach implication fills F1.

## 5. Final scope and handoff

The final retained mathematical output is (V3), (V4), the rough squareful long error, and the exact identity (V5), with full proofs and independent review frozen upstream. The full signed lower bound (V2), novelty and the original Goldbach objective remain incomplete. The all-large-even-\(N\) quantifier has not been weakened to an average or a pilot family.

The actual pair round is propose, distinct Independent Critic challenge, original-author revise: eight declared proxy units, plus two root primary-access units, ten total. Token and monetary usage remain unknown, so no numerical usage values are invented. No publication, external message, paid call, supplement or full-goal completion is authorized by this revision. Output hashes and schema validation are reported after writing rather than made self-referential.
