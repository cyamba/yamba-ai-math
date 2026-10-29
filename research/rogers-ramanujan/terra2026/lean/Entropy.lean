import Std

namespace KR1Entropy
inductive State where | E | A | B | C | D | F | G
  deriving DecidableEq, Repr

def step (f : State → Nat) : State → Nat
 | .E | .A | .B | .D => f .E + f .A + f .B + f .C + f .D + f .F + f .G
 | .C | .F => f .E + f .D + f .F + f .G
 | .G => f .E + f .F + f .G

def step3 (f : State → Nat) : State → Nat := step (step (step f))
def v : State → Nat
 | .E | .A | .B | .D => 10000
 | .C | .F => 5321
 | .G => 3473

def walks : Nat → State → Nat
 | 0 => fun _ => 1
 | n+1 => step3 (walks n)

def scale (k : Nat) (f : State → Nat) : State → Nat := fun s => k * f s

theorem v_positive (s : State) : 3473 ≤ v s := by
  cases s <;> decide

theorem witness (s : State) : step3 v s ≤ 159 * v s := by
  cases s <;> decide

theorem step_mono (f g : State → Nat) (h : ∀ s, f s ≤ g s) :
    ∀ s, step f s ≤ step g s := by
  intro s
  cases s <;> simp [step] <;>
    have h0 := h .E <;> have h1 := h .A <;> have h2 := h .B <;>
    have h3 := h .C <;> have h4 := h .D <;> have h5 := h .F <;>
    have h6 := h .G <;> omega

theorem step3_mono (f g : State → Nat) (h : ∀ s, f s ≤ g s) :
    ∀ s, step3 f s ≤ step3 g s := by
  exact step_mono _ _ (step_mono _ _ (step_mono _ _ h))

theorem step_scale (k : Nat) (f : State → Nat) (s : State) :
    step (scale k f) s = scale k (step f) s := by
  cases s <;> simp [step, scale, Nat.mul_add]

theorem step3_scale (k : Nat) (f : State → Nat) (s : State) :
    step3 (scale k f) s = scale k (step3 f) s := by
  unfold step3
  have heq : step (scale k f) = scale k (step f) := by
    funext t; exact step_scale k f t
  rw [heq]
  have heq2 : step (scale k (step f)) = scale k (step (step f)) := by
    funext t; exact step_scale k (step f) t
  rw [heq2, step_scale]

theorem walks_bound (n : Nat) (s : State) : walks n s ≤ 159^n * v s := by
  induction n generalizing s with
  | zero => simp [walks]; have hv := v_positive s; omega
  | succ n ih =>
    have hm := step3_mono (walks n) (scale (159^n) v) ih s
    have he := step3_scale (159^n) v s
    have hw := Nat.mul_le_mul_left (159^n) (witness s)
    simp only [walks, he, scale] at hm
    rw [Nat.pow_succ]
    calc
      step3 (walks n) s ≤ 159^n * step3 v s := hm
      _ ≤ 159^n * (159 * v s) := hw
      _ = 159^n * 159 * v s := by rw [Nat.mul_assoc]

theorem root_bound (n : Nat) : walks n .E ≤ 10000 * 159^n := by
  have h := walks_bound n .E
  simpa [v, Nat.mul_comm] using h

#print axioms witness
#print axioms walks_bound
#print axioms root_bound
end KR1Entropy
