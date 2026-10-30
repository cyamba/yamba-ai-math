"""Exact checks for the shifted Newton-basis parity interpolant (problem ETH-A01).

f_{a,b}(z) = (-1)^a * sum_{j=0}^{b} (-2)^j * C(z-a, j)
Claims checked (exact integer arithmetic):
  (1) f(a+k) = (-1)^(a+k) for 0 <= k <= b                    [interval identity]
  (2) Gemini PDF claim: f(a+k) - (-1)^(a+k) = (-1)^a (-2)^(b+1) C(k-1,b) for all k  [expected FALSE]
  (3) Corrected: (-1)^k S(k,b) - 1 = -(-2)^(b+1) * sum_{m=b+1}^{k} (-1)^m C(m-1,b)   for k >= 0
      where S(k,b) = sum_{j<=b} (-2)^j C(k,j).  Equivalently the one-step recurrence
      S(k,b) = -S(k-1,b) - (-2)^(b+1) C(k-1,b).
  (4) Closed form of the defect via a single hypergeometric-free expression:
      (-1)^k S(k,b) - 1 = (-1)^(b+1) 2^(b+1) * sum_{m=b+1}^{k} (-1)^(m) C(m-1,b) ... (same as 3)
"""
from math import comb

def C(n, j):
    # generalized binomial for integer n (possibly negative), j >= 0
    if j < 0:
        return 0
    num = 1
    for i in range(j):
        num *= (n - i)
    den = 1
    for i in range(1, j + 1):
        den *= i
    assert num % den == 0
    return num // den

def S(k, b):
    return sum((-2) ** j * C(k, j) for j in range(b + 1))

fails_pdf = []
for b in range(0, 9):
    for k in range(-6, 25):
        # (1)
        if 0 <= k <= b:
            assert (-1) ** k * S(k, b) == 1, (k, b)
        # (2) PDF claim, with a = 0
        lhs = S(k, b) - (-1) ** k
        rhs = (-2) ** (b + 1) * C(k - 1, b)
        if lhs != rhs:
            fails_pdf.append((b, k, lhs, rhs))
        # recurrence (valid for all integers k, Pascal holds for generalized binomials)
        assert S(k, b) == -S(k - 1, b) - (-2) ** (b + 1) * C(k - 1, b), (k, b)
        # (3) telescoped form for k >= 0
        if k >= 0:
            tel = -(-2) ** (b + 1) * sum((-1) ** m * C(m - 1, b) for m in range(1, k + 1))
            assert (-1) ** k * S(k, b) - 1 == tel, (k, b)

print("(1) interval identity: OK")
print("(3) recurrence and telescoping identity: OK for b<=8, -6<=k<=24")
print(f"(2) PDF single-binomial defect claim fails in {len(fails_pdf)} cases; first few:")
for row in fails_pdf[:6]:
    print("   b=%d k=%d  true defect=%d  PDF formula=%d" % row)
# sign pattern & growth of the defect just outside the interval
print("defect at k=b+1:", [(b, (-1) ** (b + 1) * S(b + 1, b) - 1) for b in range(6)])
print("closed check: defect(b+1) = -(-1)^(b+1)... =", [(b, -(-2) ** (b + 1) * (-1) ** (b + 1)) for b in range(6)])
