# Final focused recurrence attempt: cyclic reverse-complement routing

Status: **refuted candidate and explicit branch-specific repair for its smallest found obstruction**; author argument, separate review outstanding. Novelty NOT VERIFIED. No total object-level recurrence or KR1 bridge is supplied.

Assume the C and A node weights and four-branch recurrence stated in `recurrence_obstruction.md`. For each source word w, the candidate for the unshifted A_{n+1} branch forms the word |reverse(swap(w)) and allows any cyclic rotation; keep the globally swapped α/β inventory. Allow arbitrary nonnegative target gap coordinates. For the two shifted C_{n+1} branches, also keep that swapped inventory, with arbitrary legal target words and indices. For the shifted A_{n+2} branch allow arbitrary legal words and indices but again retain the globally swapped inventory. Common-tail context starts empty and is kept empty. Branch choice can be arbitrary.

This is a liberal version of a cyclic-word routing attempt: all rotations are available, target gap coordinates need not follow any proposed inverse, and target-side survivor/exclusion conditions are ignored. Failure here rules out the specified inventory and word architecture, not a different branch-dependent convention or word-changing map.

## Concrete C1 survivor, exact weight 37

Take n=1 and source word |αβα, with cut index 0 and particle indices 0,0,1. Its source intrinsic particle weights are 10,8,10, so total weight is 10+8+(10+9)=37. There is no marker because floor(1/3)=0, so the state survives.

For unshifted A2 the swapped reverse-complement word is |βαβ|. Below, minima allow all nonnegative indices, respect the necessary strict β→α rule, and ignore further A restrictions:

| Rotation | A2 minimum weight |
| --- | ---: |
| `|βαβ|` | 55 |
| `βαβ||` | 67 |
| `αβ||β` | 25 |
| `β||βα` | 40 |
| `||βαβ` | 43 |

Each gap increases weight by a multiple of 9. The only minimum at most 37 is 25, whose residue mod 9 differs from 37. Thus none of these five words realizes weight 37, even before target restrictions.

The swapped inventory is one α and two β. A C_{n+1} α is 1 mod 3 and a β is 2 mod 3, so either C2 target weighs 1+2+2=2 mod 3; both branch shifts 6 and 12 are 0 mod 3. The source weight 37 is 1 mod 3. Thus neither shifted C2 branch can accept it with globally swapped colors, whatever its cut word or indices.

For the q^14 A3 branch, an α weighs at least 8 and a β at least 10, so with swapped inventory its weight is at least 14+8+10+10=42. Thus no branch of the scoped candidate can accept the source.

## A branch-specific repair of this one object

Keeping colors instead of globally swapping them in the q^6 C2 branch does represent weight 37: place two α at index 0 in layer 0 and one β at index 0 in terminal layer 2, with both cuts zero. Their respective weights are 10,10,11, and 10+10+11+6=37. This target has no signed markers, since floor(2/3)=0. It is only a weight match for one state: no total branch-selection rule, inverse image characterization, or compatibility with other source objects has been shown.

Consequently, a successful full recurrence may need a branch-dependent inventory convention, rather than global color swapping, and a way to recover which branch was used. Rotations are not excluded in such a construction. The broader unresolved requirements are totality, source and target survivor validity, preservation of all weights, termination, disjoint images, and mutually inverse recovery without an enumeration-based matching.
