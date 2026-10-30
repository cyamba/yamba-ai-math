# Primary arithmetic input to inspect

29 October 2026. Root acting as Literature Scout. The [Lue-Wang-Wu appendix](https://arxiv.org/html/2610.20242v1) displays an elementary complete Kloosterman estimate (A.2), derived from additive orthogonality, a fourth-moment collision count and the unit-scaling orbit. Its proof can be independently reconstructed for this limited purpose. The paper's full theorem remains unverified here.

Write K_m(h,k)=sum over units x modulo m of e((h*x+k*x^(-1))/m). Fourth-moment orthogonality reduces to simultaneous sums of two units and their inverses. Eliminating one variable gives m dividing (x1+x2)*(x3-x1)*(x3-x2). A linear map has kernel of size at most2, giving collision count at most2*m^2*tau3(m). Unit scaling leaves K unchanged and has orbit size phi(m/gcd(h,k,m)). Attempt to rederive all these statements, then use the resulting m^(3/4+epsilon)*gcd(h,k,m)^(1/4) bound for interval completion. The task requires no claim about the full prime-list method.

The nearby sector calculation in ../moving-sectors-20261029/statement.md is currently under separate review. It motivates the multiplier H in the complement ratio, but is not needed as a black-box analytic input. The present Fourier sum and coprime supports must be defined independently.
