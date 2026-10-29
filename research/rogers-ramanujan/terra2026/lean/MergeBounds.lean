import Std
namespace KR1Merge

def L (l : Int) : Int := 3 * ((l / 2)) - 1 + (l % 2)
def R (l : Int) : Int := 3 * ((l / 2)) + 4 + 2 * (l % 2)

theorem key_identity (l : Int) : R l - 3 = L (l+1) + 1 := by
  unfold R L
  omega

theorem pair_step (l : Int) : R (l+2) = R l + 3 := by
  unfold R
  omega

theorem left_step (l : Int) : L (l+2) = L l + 3 := by
  unfold L
  omega

theorem left_step_upper (l : Int) : L (l+1) ≤ L l + 2 := by
  unfold L
  omega

theorem right_left_gap (l : Int) : R l ≥ L l + 5 := by
  unfold R L
  omega

theorem left_lipschitz (l : Int) (n : Nat) :
    L (l + n) ≤ L l + 2 * n := by
  induction n with
  | zero => simp
  | succ n ih =>
    have hs := left_step_upper (l + n)
    push_cast at *
    have eq : l + (↑n + 1) = (l + ↑n) + 1 := by omega
    rw [eq]
    omega

theorem right_repeated (l : Int) (n : Nat) :
    R (l + 2 * n) = R l + 3 * n := by
  induction n with
  | zero => simp
  | succ n ih =>
    have hs := pair_step (l + 2 * n)
    push_cast at *
    have eq : l + 2 * (↑n + 1) = (l + 2 * ↑n) + 2 := by omega
    rw [eq, hs, ih]
    omega

/-- Nonadjacent single branch: the last of h singles is above S+2(h-1). -/
theorem choose_single (l S last : Int) (h : Nat) (hh : 1 ≤ h)
    (lo : S + 2 * (↑h - 1) ≤ last) (hi : last ≤ L (l + h)) :
    S ≤ L (l+1) := by
  have hs := left_lipschitz (l+1) (h-1)
  have hn : ((h-1 : Nat) : Int) = (h : Int)-1 := by omega
  rw [hn] at hs
  have heq : l + 1 + ((h : Int) - 1) = l + h := by omega
  rw [heq] at hs
  omega

/-- Nonadjacent pair branch, under the right-bound estimate for the last pair. -/
theorem choose_pair (l S actual : Int) (h : Nat) (hh : 1 ≤ h)
    (value : actual = S + 3 * h)
    (boundary : actual ≥ R l + 3 * ((h : Int)-1)) :
    S > L (l+1) := by
  have ident := key_identity l
  omega

#print axioms key_identity
#print axioms pair_step
#print axioms left_step
#print axioms left_step_upper
#print axioms right_left_gap
#print axioms left_lipschitz
#print axioms right_repeated
#print axioms choose_single
#print axioms choose_pair
end KR1Merge
