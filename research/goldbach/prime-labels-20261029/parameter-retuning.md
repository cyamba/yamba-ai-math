# A concrete attempt to retune the displayed moment bounds

29 October 2026. Root-authored supplement to the bounded-label attempt, pending separate review. This is a feasibility calculation for the displayed source bounds, not a lower bound on an actual operator norm and not a theorem ruling out a different small-label argument.

Put L=log N. The inspected [source equations (4.48)-(4.51)](https://arxiv.org/html/2610.20242v1) use J=floor(L^(0.01)), R comparable to L^(1/2), and an error budget containing

\[
\epsilon_K=C_{K,\rho}\left(L^2(J+1)^{-K}
                         +L^{2K}e^{-cL^{0.1}}\right).
\]

The dirty-edge Schur bound has a fixed power-of-L factor times sqrt(epsilon_K). The source makes that displayed bound small by choosing a sufficiently large fixed K. For genuine polynomial labels that divide q<N, nonzero support imposes K<=3 in the present alpha range.

Try to repair that bound by increasing J while holding K<=3. Write its fixed logarithmic prefactor as L^C, C>=0. For the displayed positive first error term itself to fit an edge budget L^(-G), with fixed G>0, it would be sufficient and, for that particular positive error-budget term, necessary up to constants that

\[
L^{C+1}(J+1)^{-K/2}\ll L^{-G},
\qquad
J+1\gg L^{2(G+C+1)/K}.
\tag{1}
\]

This is not a necessary condition on the actual dirty-edge operator, whose norm may be much smaller than the available bound. It is the cost of using this displayed bound as the certificate.

Now retain the source's moment order R comparable to sqrt(L) and fixed logarithmic moment precision. For a product D_aux of K(J+1) distinct polynomial labels each greater than N^alpha,

\[
\log D_{\rm aux}\ge K(J+1)\alpha L.
\]

The product D_aux is comparable, up to the fixed dyadic factors, to the source's height parameter d0*Y. The dimension factor that remains after its moment transfer therefore obeys

\[
D_{\rm aux}^{1/(2R)}
 \ge\exp(cK\alpha(J+1)\sqrt L).
\tag{2}
\]

Already for J>=0, the right side exceeds every fixed power of L. Increasing J according to (1) worsens it. Thus this explicit attempt to improve the dirty-edge budget while keeping the published moment order cannot produce the desired logarithmic pairing bound. The additional primes in D_aux may be artificial padding; no unsupported assertion that all J+1 primes divide the original q is needed for this height calculation.

One can next try increasing R as well. To keep this same dimension loss within a fixed power of L would require

\[
R\gg\frac{K\alpha(J+1)L}{\log L}.
\tag{3}
\]

Such an enlarged moment order is not supplied by the cited theorem. There is also an earlier input-range issue: the root-averaging proof in Proposition 4.4 prescribes prime residues only for squarefree S<=exp(O_K(L^(0.98))). A polynomial label p>N^alpha is eventually outside that stated range even when S=p. No choice of J or R changes alpha L>C L^(0.98) for every fixed C. Applying that particular root-averaging statement would therefore require a new enlarged-range proof before a retuned moment calculation could be justified.

The conclusions are deliberately limited. The published parameters do not transfer directly; raising only J makes the displayed height loss worse; raising R requires a theorem in a different range; and the stated root-averaging range itself does not cover one polynomial label. A genuinely different bound, a sharper weighted Schur estimate, a different normalization, or a new root-averaging argument is not disproved. None has been established in this supplement. This attempted parameter repair supplies no actual prime-correlation estimate or Goldbach breakthrough.
