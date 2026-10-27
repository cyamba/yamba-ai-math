import Std

/- A block records multiplicities at 3j+1, 3j+2, 3j+3. -/
namespace KR1
inductive Letter where
 | E | A | B | C | D | F | G
 deriving DecidableEq, Repr

def counts : Letter → Nat × Nat × Nat
 | .E => (0,0,0) | .A => (1,0,0) | .B => (1,1,0)
 | .C => (1,0,1) | .D => (0,1,0) | .F => (0,0,1)
 | .G => (0,0,2)

/-- Local restrictions on the multiplicities of one block. -/
def BlockValid (a b c : Nat) : Prop :=
 a+b+c ≤ 2 ∧ a ≤ 1 ∧ b ≤ 1 ∧ (b > 0 → c = 0)

theorem block_classification (a b c : Nat) :
 BlockValid a b c ↔ ∃ p, counts p = (a,b,c) := by
 constructor
 · intro h
   rcases h with ⟨h, ha, hb, hbc⟩
   have ha' : a = 0 ∨ a = 1 := by omega
   have hb' : b = 0 ∨ b = 1 := by omega
   have hc' : c = 0 ∨ c = 1 ∨ c = 2 := by omega
   rcases ha' with rfl | rfl <;> rcases hb' with rfl | rfl <;>
     rcases hc' with rfl | rfl | rfl <;>
     simp_all [counts] <;> first | omega | exact ⟨.E, rfl⟩ | exact ⟨.A, rfl⟩ | exact ⟨.B, rfl⟩ | exact ⟨.C, rfl⟩ | exact ⟨.D, rfl⟩ | exact ⟨.F, rfl⟩ | exact ⟨.G, rfl⟩
 · rintro ⟨p, hp⟩
   cases p <;> simp_all [counts, BlockValid] <;> omega

def Compatible : Letter → Letter → Prop
 | .C, .A | .C, .B | .C, .C
 | .F, .A | .F, .B | .F, .C
 | .G, .A | .G, .B | .G, .C | .G, .D => False
 | _, _ => True

/-- The two extra length-three windows and boundary adjacent restriction. -/
def BoundaryValid (p q : Letter) : Prop :=
 let (a,b,c) := counts p
 let (d,e,f) := counts q
 b+c+d ≤ 2 ∧ c+d+e ≤ 2 ∧ (c > 0 → d = 0)

theorem transition_table (p q : Letter) : Compatible p q ↔ BoundaryValid p q := by
 cases p <;> cases q <;> simp [Compatible, BoundaryValid, counts]

/-- Every compatible pair satisfies all four length-three windows, and conversely. -/
theorem adjacent_blocks (p q : Letter) : Compatible p q ↔
 let (a,b,c) := counts p
 let (d,e,f) := counts q
 a+b+c ≤ 2 ∧ b+c+d ≤ 2 ∧ c+d+e ≤ 2 ∧ d+e+f ≤ 2 ∧ (c > 0 → d = 0) := by
 cases p <;> cases q <;> simp [Compatible, BoundaryValid, counts]

/-- Reading a valid block back to a letter is unique. -/
theorem counts_injective : Function.Injective counts := by
 intro p q h
 cases p <;> cases q <;> simp_all [counts]

/-- Global multiplicity conditions, expressed blockwise over all natural j. -/
def SequenceValid (c : Nat → Nat) : Prop :=
 (∀ j, BlockValid (c (3*j+1)) (c (3*j+2)) (c (3*j+3))) ∧
 (∀ j, c (3*j+2)+c (3*j+3)+c (3*j+4) ≤ 2) ∧
 (∀ j, c (3*j+3)+c (3*j+4)+c (3*j+5) ≤ 2) ∧
 (∀ j, c (3*j+3) > 0 → c (3*j+4) = 0)

def Realizes (c : Nat → Nat) (w : Nat → Letter) : Prop :=
 ∀ j, counts (w j) = (c (3*j+1), c (3*j+2), c (3*j+3))

theorem sequence_encode (c : Nat → Nat) (h : SequenceValid c) :
 ∃ w : Nat → Letter, Realizes c w ∧ ∀ j, Compatible (w j) (w (j+1)) := by
  have hex : ∀ j, ∃ p, counts p = (c (3*j+1), c (3*j+2), c (3*j+3)) :=
    fun j => (block_classification _ _ _).mp (h.1 j)
  let w := fun j => Classical.choose (hex j)
  have hw : Realizes c w := fun j => Classical.choose_spec (hex j)
  refine ⟨w, hw, ?_⟩
  intro j
  apply (transition_table _ _).mpr
  unfold BoundaryValid
  rw [hw j, hw (j+1)]
  simp only
  have h1 := h.2.1 j
  have h2 := h.2.2.1 j
  have h3 := h.2.2.2 j
  have e1 : 3 * (j+1) + 1 = 3*j+4 := by omega
  have e2 : 3 * (j+1) + 2 = 3*j+5 := by omega
  rw [e1, e2]
  exact ⟨h1, h2, h3⟩

theorem sequence_decode (c : Nat → Nat) (w : Nat → Letter)
 (hw : Realizes c w) (ht : ∀ j, Compatible (w j) (w (j+1))) : SequenceValid c := by
  constructor
  · intro j
    exact (block_classification _ _ _).mpr ⟨w j, hw j⟩
  · have hb : ∀ j, c (3*j+2)+c (3*j+3)+c (3*j+4) ≤ 2 ∧
        c (3*j+3)+c (3*j+4)+c (3*j+5) ≤ 2 ∧
        (c (3*j+3) > 0 → c (3*j+4) = 0) := by
      intro j
      have h := (transition_table _ _).mp (ht j)
      unfold BoundaryValid at h
      rw [hw j, hw (j+1)] at h
      simp only at h
      have e1 : 3 * (j+1) + 1 = 3*j+4 := by omega
      have e2 : 3 * (j+1) + 2 = 3*j+5 := by omega
      rw [e1, e2] at h
      exact h
    exact ⟨fun j => (hb j).1, fun j => (hb j).2.1, fun j => (hb j).2.2⟩

theorem realization_unique (c : Nat → Nat) (w v : Nat → Letter)
 (hw : Realizes c w) (hv : Realizes c v) : w = v := by
  funext j
  apply counts_injective
  rw [hw j, hv j]

#print axioms block_classification
#print axioms transition_table
#print axioms adjacent_blocks
#print axioms counts_injective
#print axioms sequence_encode
#print axioms sequence_decode
#print axioms realization_unique
end KR1
