# Frozen U-side candidate families, v1

These are proposed cuts, not asserted KR1 maps. Frozen before numerical pilots.
Each must produce a valid child, retain a literal inverse, and eventually match
the C grammar's dimensions and boundary range. Missing any of these rejects a
full bridge claim. There are exactly three discovery families in this track.

1. **Lower sheet core.** For each decoded row `h=5q+r`, remove the
   common prism of height `P2(h)=3q+clamp(r-2,0,3)` from all three slices;
   propose its ordinary row lengths as the child U numerical parts. Store the
   row notches for reconstruction. Test literal child U membership. This is
   the most direct equal-volume-three prism cut; no reinterpretation or phase
   correction is silently supplied after a failure.
2. **Triple-row compression.** Retain decoded rows in positions 3,6,9,...
   in the descending full height list, apply F, and propose this as child U.
   Store the intervening rows. Test child U flatness, including the terminal
   drop. The first and second row may remain in the boundary; no post-hoc
   rotation or tail repair is introduced.
3. **Ternary-height compression.** Replace every decoded height by floor(h/3),
   remove zeros, and apply F. Retain every row's remainder and leading-zero
   convention so this carrier has an intrinsic literal inverse. Test child U
   membership and the nonnegative residual `|U|-3|child|`; then test whether
   the possible child range can be the full recursively demanded U range.
   The quotient's upper decoded-height gap is at most two; this invariant is
   recorded before testing. There is no claim that bounded finite residual
   positivity supplies the C boundary language.

The old area-only collision `(8,3,1)` versus `(6,6)` and the weight-13
two-cube inclusion obstruction remain in force. The sheet lift is the
zero-based corrected `P_t(5q+r)=3q+clamp(r-t,0,3)`, t=0,1,2.
