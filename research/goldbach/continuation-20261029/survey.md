# Literature and analytic-input survey

29 October 2026. Registry role: Literature Scout. Actual mode: host-agent research with primary-source browsing. No provider billing or token measurements are available. This report establishes neither Goldbach nor the proposed pointwise signed inequality.

## Findings

**Established by inspection:** the Huang–Li hypothesis retains a maximum over the partial-sum endpoint. The published large-divisor rearrangement drops a moving endpoint. **Unverified proposed repair:** retaining that endpoint and using the original maximal hypothesis should recover the large-divisor estimate, as detailed below. The repair is explicitly anticipated by a located 2026 preprint, so it is not a novelty candidate.

**Proved elementary warning, assurance: handwritten argument awaiting the separate critic:** the sparse-deletion model does not retain the ordinary divisor identity on all integers. Its lack of Goldbach representations therefore does not, by itself, prove that it violates a naively transplanted twisted-distribution hypothesis. An explicit discrepancy calculation remains necessary.

## Inspected primary sources

1. **Jing-Jing Huang and Huixi Li, _On the connection between the Goldbach conjecture and the Elliott-Halberstam conjecture_, arXiv:2005.03811v2, revised 28 August 2022.** [Version record](https://arxiv.org/abs/2005.03811v2), [full text](https://arxiv.org/html/2005.03811), [PDF](https://arxiv.org/pdf/2005.03811). Inspection: introduction, hypotheses, Theorem 1, Corollary 1, Lemma 1, Lemma 4 and section 3.2; not a line-by-line audit of the complete proof. The repository brief's “Corollary 2” is not the numbering in this version: both inspected PDF and HTML say Corollary 1. Define

   \[
   f_N(n)=\Lambda(n)\mu(N-n),\quad F_N(y)=\sum_{n\le y}f_N(n),
   \quad E_N(q,a;y)=\sum_{\substack{n\le y\\n\equiv a\ (q)}}f_N(n)-F_N(y)/\phi(q).
   \]

   Their twisted assumption is, for every \(B>0\),

   \[
   \sum_{q\le N^{\vartheta}}\max_{y<N}\max_{(a,q)=1}|E_N(q,a;y)|
       \ll_B N/(\log N)^B.
   \]

   Ordinary EH replaces \(f_N\) by \(\Lambda\) and the centering by \(y/\phi(q)\). Theorem 1 uses ordinary level \(N^\theta(\log N)^{2A+8}\) and twisted level \(N^{1-\theta}\). Corollary 1 uses exponent \(12+\epsilon\) instead of \(2A+8\). Its conditional consequence is sufficiently-large binary Goldbach; BV would suffice on the ordinary side if the twisted exponent exceeds \(1/2\). These are source claims under explicit hypotheses, not hypotheses proved here. The fixed-residue remark does not remove the endpoint maximum. Prime-power weights, ordinary Möbius rather than Liouville, logarithmic savings and the moving \(N\) all matter.

2. **John Friedlander and Henryk Iwaniec, _Asymptotic sieve for primes_, Annals of Mathematics 148 (1998), 1041–1065, arXiv:math/9811186v1.** [Version record](https://arxiv.org/abs/math/9811186), [full PDF](https://arxiv.org/pdf/math/9811186). Inspection: section 1, Theorem 1 and section 10/Theorem 3; not all technical proofs. For nonnegative \(a_n\), \(A(x)=\sum_{n\le x}a_n\), their additional axiom is

   \[
   \sum_m\left|\sum_{\substack{M<n\le2M\\mn\le x}}
       \gamma(n,C)\mu(mn)a_{mn}\right|\le A(x)(\log x)^{-2^{22}},
   \quad \gamma(n,C)=\sum_{\substack{d\mid n\\d\le C}}\mu(d).
   \]

   Required ranges include \(\Delta^{-1}\sqrt D<M<\delta^{-1}\sqrt x\), \(1\le C\le x/D\), and \(x^{2/3}<D<x\). Their remainder axiom is uniform in \(t\le x\), with squarefree-modulus absolute errors bounded by \(A(x)(\log x)^{-2^{22}}\); Theorem 1 initially assumes squarefree support and further density conditions. Theorem 3 permits a restricted rough inner sum under a stronger error saving. Neither ordinary AP distribution nor a signed average supplies this absolute outer-sum bilinear axiom. Applying the theorem to a reflected Goldbach sequence requires verifying every condition, uniformly in the target, with target-dependent local factors controlled. No such verification is supplied here.

3. **Ramón Moya, _A Moving-Cut Correction to the Huang–Li Conditional Goldbach Argument: Consequences for Diagonal Möbius-Twisted Elliott–Halberstam Hypotheses_, 14 August 2026, Zenodo version 1.0.0.** [Primary record](https://zenodo.org/records/21939906). Inspection: repository record/description only. The linked PDF failed retrieval twice, including a decoding error. Thus the detailed proof is **unverified** here. The record explicitly describes the same missing cutoff and claims repair under the original maximal-in-endpoint assumption. This establishes direct prior-art overlap at the level of its announced result; it does not certify that proof. Do not announce the proposed repair below as new.

No other source theorem or recent manuscript was used. OpenAI divisibility-graph or prime-slot results were not inspected in this stage and supply no analytic input to its conclusions.

## Direct check of the moving cutoff

This is our algebraic inspection, independent of Moya's inaccessible proof. Let \(h=N-n\) be squarefree, \(d\mid h\), and use a real cutoff \(\eta>1\). Put \(k=h/d\). Then

\[
d>\eta\quad\Longleftrightarrow\quad k<h/\eta
\quad\Longleftrightarrow\quad n<N-\eta k.
\]

Consequently the exact large-divisor expression is

\[
\begin{split}
S_2(\eta)
&=\sum_{n<N}\Lambda(n)\mu^2(N-n)
    \sum_{\substack{d\mid N-n\\d>\eta}}\mu(d)\log(1/d)\\
&=\sum_{k<(N-1)/\eta}\mu(k)
    \sum_{\substack{n<N-\eta k\\n\equiv N\ (k)}}
       f_N(n)\log\frac{k}{N-n}.
\end{split}
\]

For nonsquarefree \(h\), both sides after the squarefree Möbius substitution vanish, so the displayed identity includes those \(n\). In the inspected Huang–Li equation (18), the last inner endpoint is instead \(n<N\). The omitted restriction is a genuine finite identity issue. It does not imply that their theorem's conclusion is false.

## A bounded endpoint-transfer lemma to prove next

**Proposed, not yet a completed proof in this survey.** For arbitrary complex \(f\) supported on integers \(1\le n<N\), define its AP discrepancy relative to its own partial sums as above and

\[
\mathcal E_f(Q)=\sum_{\substack{k\le Q\\(k,N)=1}}
     \sup_{y<N}|E_f(k,N;y)|.
\]

For \(Q=(N-1)/\eta\), retain \(n<N-\eta k\) and set \(w_k(t)=\log(k/(N-t))\). On the integration interval \(0\le t<N-\eta k\), this function is increasing and its absolute magnitude and total variation are \(O(\log N)\) when \(1<\eta<N\). Abel summation should therefore give

\[
\begin{split}
&\sum_{\substack{k<Q\\(k,N)=1}}\mu(k)
\left\{\sum_{\substack{n<N-\eta k\\n\equiv N\ (k)}}f(n)w_k(n)
 -\frac1{\phi(k)}\sum_{n<N-\eta k}f(n)w_k(n)\right\}\\
&\hspace{35mm}\ll (\log N)\mathcal E_f(Q).
\end{split}
\]

Strict real endpoints must be implemented by the largest admitted integer. This transfer uses no Goldbach conclusion. It exposes why an estimate only at \(y=N\) cannot replace the maximum over endpoints.

For \(f=f_N\), \(\eta=N^\theta\), and the full twisted hypothesis, the RHS has arbitrary logarithmic saving. Swapping the transferred main term back gives the coefficient

\[
K_N(h)=\sum_{\substack{k<h/\eta\\(k,N)=1}}
       \frac{\mu(k)}{\phi(k)}\log(k/h).
\]

For \(h/\eta\) polynomially large, a uniform form of the inspected Möbius/\(\phi\) sum estimates would make \(K_N(h)=-\mathfrak S(N)+o(1)\) with adequate logarithmic saving. Terms with \(h\le\eta N^\rho\), \(0<\rho<1-\theta\), can be bounded using the short interval's length and \(\Lambda(n)\le\log N\), provided the coefficient is explicitly bounded. Coprime and noncoprime \(k\), prime powers, moving \(N\), and exact constants still need the theorem author's treatment. This route repairs a conditional derivation; it does not establish its open distribution hypothesis.

## What the deletion model does and does not establish

The earlier report proves only a leading prime-density statement from \(D(x)=O(x/\log^2x)\). That is weaker than the arbitrary-log-saving error in ordinary EH or BV.

Define \(\Lambda_A(p^j)=\log p\) for \(p\in A\), zero otherwise. Then

\[
\psi(x)-\psi_A(x)
 =\sum_{\substack{p^j\le x\\p\notin A}}\log p\ge0.
\]

Ordinary EH contains its \(q=1\) term, \(\sup_{y\le x}|\psi_A(y)-y|\). If \(\Lambda_A\) obeyed this ordinary estimate with every logarithmic saving, the actual prime PNT error and subtraction would require the weighted deleted mass to have every logarithmic saving too. The bound \(D(x)=O(x/\log^2x)\) neither proves that stronger conclusion nor proves its failure. Inferring a power distribution level from density alone is invalid. For the self-centered twisted discrepancy, the \(q=1\) term is identically zero, so that ordinary obstruction does not transfer directly.

There is a separate structural warning. Extend \(\mu_A(n)=\mu(n)\mathbf1_{n\in M(A)}\) to all integers. Choose an allowed prime \(p\) and a deleted prime \(r\). At \(n=pr\),

\[
-\sum_{d\mid pr}\mu_A(d)\log d=\log p,
\qquad \Lambda_A(pr)=0.
\]

Thus the ordinary divisor identity used in the conditional Goldbach derivation fails for this transplant. Restoring the semigroup indicator introduces additional arithmetic information. A proof that this model fails a particular twisted hypothesis must directly lower-bound that discrepancy or account for those extra terms. It cannot be inferred solely from the absence of prime pairs in the model.

## Novelty, failure case and next questions

Novelty of the rough-pair programme and any final trilinear estimate remains **unverified**. The endpoint repair has explicit announced prior art. The strongest competing explanation for any apparent progress is that it is a standard upper-sieve or partial-summation reduction while the parity-sensitive lower bound remains untouched.

Failure case: replacing maximal partial-sum control by a single full-interval value allows cancellation between a moving initial interval and its omitted tail. Similarly, transplanting ordinary Möbius inversion into the prime-deletion semigroup gives the explicit \(pr\) failure above.

Questions for the theorem author and experimenter:

1. Can the proposed endpoint-transfer bound be proved with a concrete constant and strict endpoint convention, then independently checked on arbitrary finitely supported signed sequences?
2. For a claimed uniform three-factor upper sieve, does every accumulated remainder retain the \(\epsilon^2\) gain uniformly as \(\epsilon\downarrow0\), before any comparison with the still-open parity-sensitive lower bound?
