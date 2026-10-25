"""RR003 executable restricted residue<->gap composition.

Domain on the gap side: at most two intrinsic single clusters. Author-only
universal arguments compose the attributed endpoints and restricted U<->C
map; no accepted global bridge, novelty claim or Lean certificate exists.
"""
import kr1
import rr003_a2 as bridge
import rr003_cluster_merge as clusters
import rr003_stockhofe as endpoint

OutsideRestrictedDomain=bridge.OutsideRestrictedDomain


def residue_to_gap(parts):
    columns=endpoint.residue_to_columns(parts)
    c=bridge.decompose_columns(columns)
    return clusters.cluster_to_gap(c)


def gap_to_residue(parts):
    c=clusters.gap_to_cluster(parts)
    columns=bridge.reconstruct_columns(c)
    return endpoint.columns_to_residue(columns)
