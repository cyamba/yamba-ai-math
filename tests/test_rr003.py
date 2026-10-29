"""RR003 boundary, resource-protocol and honest-completion regressions."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
CHECKS=ROOT/'research/rogers-ramanujan/checks'
sys.path.insert(0,str(CHECKS))
import kr1
import rr003_columns as first
import rr003_revision as maps
import rr003_recursive as recursive
import rr003_a2 as all_a2
import rr003_stockhofe as stockhofe
import rr003_cluster_merge as merge
import rr003_clusters as obstacle
import rr003_small_charge as charge
import rr003_partial as partial
import rr003_charge_extension as extended_charge
import rr003_recursive_seed as recursive_seed
import rr003_product_involution as product_walk
import rr003_second_product as second_walk
import rr003_cut_branch as cut_branch


class RR003Tests(unittest.TestCase):
    def test_empty_and_missing_global_sector_are_distinguished(self):
        self.assertEqual(maps.decompose_columns(()),kr1.ClusterData(0,0,(),()))
        c=kr1.ClusterData(3,0,(0,0,0),())
        self.assertFalse(maps.supported(c))
        with self.assertRaises(maps.OutsideRestrictedDomain):
            maps.reconstruct_columns(c)
        self.assertTrue(kr1.is_weighted(kr1.decode_columns((6,3))))
        with self.assertRaises(maps.OutsideRestrictedDomain):
            maps.decompose_columns((6,3))

    def test_literal_terminal_boundary_is_checked_before_recognition(self):
        for u in ((10,), (10,1), (11,), (9,)):
            with self.subTest(u=u):
                try:
                    maps.decompose_columns(u)
                except ValueError as error:
                    self.assertNotIsInstance(error,maps.OutsideRestrictedDomain)
                else:
                    self.fail('malformed U accepted')
        c=kr1.ClusterData(2,1,(3,3),(0,))
        self.assertEqual(maps.reconstruct_columns(c),(10,3,3,3))
        self.assertEqual(maps.decompose_columns((10,3,3,3)),c)

    def test_zero_pair_carry_crosses_original_invalid_ten_boundary(self):
        c=kr1.ClusterData(2,0,(2,2),())
        u=maps.reconstruct_columns(c)
        self.assertEqual(u,(8,))
        raised=maps.raise_common_columns(u)
        self.assertEqual(raised,(9,1))
        self.assertEqual(maps.lower_common_columns(raised),u)
        self.assertEqual(maps.raise_common_columns(maps.raise_common_columns(raised)),(8,6))

    def test_large_common_carries_preserve_nu_and_have_intrinsic_inverse(self):
        # Direct structured samples above the enumeration ceiling; no sweep.
        cases=((1,(7,),13,13),(4,(0,2,2,7),25,31),(0,(),101,104))
        for b,nu,k,v in cases:
            with self.subTest(b=b,k=k):
                c=kr1.ClusterData(2,b,(k,v),nu)
                u=maps.reconstruct_columns(c)
                self.assertEqual(maps.decompose_columns(u),c)
                operation=maps.raise_common_mixed_columns if b else maps.raise_common_columns
                reverse=maps.lower_common_mixed_columns if b else maps.lower_common_columns
                raised=operation(u)
                expected=kr1.ClusterData(2,b,(k+1,v+1),nu)
                self.assertEqual(maps.decompose_columns(raised),expected)
                self.assertEqual(reverse(raised),u)
                self.assertEqual(sum(raised),c.weight+2)

    def test_mixed_initial_split_and_finite_marker_holes(self):
        c=kr1.ClusterData(2,1,(1,1),(0,))
        u=maps.reconstruct_columns(c)
        raised=maps.raise_common_mixed_columns(u)
        self.assertEqual(raised,(8,3,3,3))
        self.assertEqual(maps.lower_common_mixed_columns(raised),u)
        for k in (4,5,9):
            c=kr1.ClusterData(2,1,(k,k),(0,))
            self.assertFalse(maps.supported(c))
            with self.assertRaises(maps.OutsideRestrictedDomain):
                maps.reconstruct_columns(c)
        for u in ((8,3,3),(10,10,10,10,3,3,3)):
            with self.assertRaises(maps.OutsideRestrictedDomain):
                maps.decompose_columns(u)

    def test_zero_padded_nu_is_preserved_in_new_mixed_sector(self):
        c=kr1.ClusterData(2,3,(2,5),(0,0,0))
        self.assertEqual(maps.decompose_columns(maps.reconstruct_columns(c)),c)
        d=kr1.ClusterData(2,3,c.mu,(0,1,1))
        image=maps.reconstruct_columns(c)
        self.assertEqual(maps.reconstruct_columns(d),tuple(sorted(image+(6,),reverse=True)))

    def test_classical_glaisher_uses_3_adic_groups_not_gap_normalization(self):
        p=(3,)*8+(6,)*2+(12,)
        image=recursive.glaisher_three(p)
        self.assertEqual(image,(3,3,6,6,9,9,12))
        self.assertEqual(recursive.unglaisher_three(image),p)
        self.assertEqual(recursive.glaisher_three(()),())
        for p in ((1,), (3,3,3)):
            with self.assertRaises(ValueError):
                (recursive.glaisher_three if p==(1,) else recursive.unglaisher_three)(p)

    def test_refuted_insertions_retain_information_loss_witness(self):
        cores=((3,3,6,9,9,12),(3,3,6,6,12,12))
        outcomes=[recursive.refuted_insert_one(p,capture_trace=True) for p in cores]
        self.assertEqual(outcomes[0][0],outcomes[1][0])
        self.assertEqual(outcomes[0][0],(3,6,9,9,16))
        self.assertNotEqual(outcomes[0][1],outcomes[1][1])
        self.assertTrue(kr1.is_gap(outcomes[0][0]))
        self.assertEqual(sum(outcomes[0][0]),43)

    def test_forbidden_link_is_rejected_and_shift_weight_includes_length(self):
        with self.assertRaises(ValueError):
            recursive.gap_unstrip(6,(2,))
        p=(1,3,6,6,10)
        self.assertTrue(kr1.is_gap(p))
        state,rest=recursive.gap_strip(p)
        self.assertEqual(recursive.gap_unstrip(state,rest),p)
        self.assertEqual(sum(p),sum(recursive.TAILS[state])+sum(rest)+3*len(rest))
        counts,rest=recursive.residue_strip((1,1,3,10,17))
        self.assertEqual(recursive.residue_unstrip(counts,rest),(1,1,3,10,17))

    def test_optimized_python_keeps_completion_gate_and_receipt_no_overwrite(self):
        with tempfile.TemporaryDirectory() as folder:
            output=Path(folder)/'receipt.json'
            command=[sys.executable,'-O',str(CHECKS/'rr003_round2_verify.py'),
                     '--ceiling','0','--require-bijection','--output',str(output)]
            result=subprocess.run(command,cwd=ROOT,capture_output=True,text=True)
            self.assertEqual(result.returncode,2,result.stdout+result.stderr)
            saved=output.read_bytes()
            report=json.loads(saved)
            self.assertEqual(report['full_bijection'],'unresolved')
            self.assertIn('No universal bridge',report['required_completion_failure'])
            result=subprocess.run(command,cwd=ROOT,capture_output=True,text=True)
            self.assertEqual(result.returncode,2)
            self.assertIn('refusing to overwrite',result.stderr)
            self.assertEqual(output.read_bytes(),saved)

    def test_frozen_source_change_fails_closed_under_optimized_python(self):
        freeze=json.loads((ROOT/'research/rogers-ramanujan/rr003/round-2-freeze.json').read_text())
        with tempfile.TemporaryDirectory() as folder:
            destination=Path(folder)
            for name in list(freeze['frozen_sha256'])+[
                    'research/rogers-ramanujan/rr003/round-2-freeze.json',
                    'research/rogers-ramanujan/checks/rr003_round2_verify.py']:
                target=destination/name
                target.parent.mkdir(parents=True,exist_ok=True)
                shutil.copyfile(ROOT/name,target)
            altered=destination/'research/rogers-ramanujan/rr003/round-2-proposal.md'
            altered.write_text(altered.read_text()+'\nUNREVIEWED CHANGE\n')
            output=destination/'receipt.json'
            result=subprocess.run([sys.executable,'-O',str(destination/'research/rogers-ramanujan/checks/rr003_round2_verify.py'),
                                   '--ceiling','0','--output',str(output)],cwd=destination,capture_output=True,text=True)
            self.assertEqual(result.returncode,1,result.stdout+result.stderr)
            self.assertIn('frozen source changed',json.loads(output.read_text())['error'])


    def test_final_a2_parity_branch_keeps_nu_distinct_from_mu(self):
        c=kr1.ClusterData(2,1,(5,8),(1,))
        u=all_a2.reconstruct_columns(c)
        raised=all_a2.raise_nu_columns(u,1)
        self.assertEqual(all_a2.decompose_columns(u),c)
        self.assertEqual(all_a2.decompose_columns(raised),kr1.ClusterData(2,1,(5,8),(2,)))
        self.assertEqual(sum(raised)-sum(u),3)
        self.assertNotEqual(raised,tuple(sorted(u+(3,),reverse=True)))
        self.assertEqual(all_a2.lower_common_columns(all_a2.raise_common_columns(u)),u)

    def test_final_a2_dense_marker_boundary_has_terminal_validity(self):
        c=kr1.ClusterData(2,6,(9,10),(0,0,0,0,0,0))
        u=all_a2.reconstruct_columns(c)
        self.assertEqual(sum(u),c.weight)
        self.assertTrue(kr1.is_weighted(kr1.decode_columns(u)))
        self.assertEqual(all_a2.decompose_columns(u),c)
        self.assertFalse(all_a2.supported(kr1.ClusterData(3,0,(0,0,0),())))

    def test_stockhofe_published_example_uses_normalized_removal_units(self):
        heights=(26,25,22,19,15,13,11,7,5,5,3)
        regular=(41,27,24,23,21,12,3)
        self.assertEqual(stockhofe.flat_to_regular(heights),regular)
        self.assertEqual(stockhofe.regular_to_flat(regular),heights)
        u=tuple(kr1.prefix_weight(x) for x in heights)
        b=stockhofe.columns_to_residue(u)
        self.assertEqual(sum(b),sum(u))
        self.assertTrue(kr1.is_residue(b))
        self.assertEqual(stockhofe.residue_to_columns(b),u)

    def test_direct_merge_and_adjustment_interpreter_agree_on_long_obstacles(self):
        # Structured instances above 30, not a larger enumeration sweep.
        cases=(kr1.ClusterData(5,4,(0,2,3,5,8),(0,0,4,9)),
               kr1.ClusterData(4,1,(0,0,0,0),(15,)),
               kr1.ClusterData(0,3,(),(1,1,3)))
        for c in cases:
            with self.subTest(c=c):
                p=merge.cluster_to_gap(c)
                self.assertTrue(kr1.is_gap(p))
                self.assertEqual(sum(p),c.weight)
                self.assertEqual(merge.gap_to_cluster(p),c)
                self.assertEqual(obstacle.cluster_to_gap(c),p)
                self.assertEqual(obstacle.gap_to_cluster(p),c)

    def test_repaired_charge_separates_the_old_collision_and_rejects_extension(self):
        cores=((3,3,6,9,9,12),(3,3,6,6,12,12))
        sources=[(1,)+recursive.unglaisher_three(c) for c in cores]
        outputs=[charge.residue_to_gap(p) for p in sources]
        self.assertNotEqual(outputs[0],outputs[1])
        for p,a in zip(sources,outputs):
            self.assertEqual(charge.gap_to_residue(a),p)
            self.assertEqual(sum(a),43)
        for p in ((1,1,1),(8,),(10,)):
            with self.assertRaises(charge.OutsideSmallCharge):
                charge.residue_to_gap(p)
        for t in (0,1,2):
            p=(1,)*t+(3,3,6)
            self.assertEqual(charge.gap_to_residue(charge.residue_to_gap(p)),p)

    def test_restricted_composition_preserves_actual_endpoint_boundaries(self):
        a=merge.cluster_to_gap(kr1.ClusterData(2,2,(4,7),(0,3)))
        b=partial.gap_to_residue(a)
        self.assertTrue(kr1.is_residue(b))
        self.assertEqual(sum(a),sum(b))
        self.assertEqual(partial.residue_to_gap(b),a)
        with self.assertRaises(partial.OutsideRestrictedDomain):
            partial.residue_to_gap((3,6))
        with self.assertRaises(partial.OutsideRestrictedDomain):
            partial.gap_to_residue((1,3,5))
        with tempfile.TemporaryDirectory() as folder:
            output=Path(folder)/'receipt.json'
            result=subprocess.run([sys.executable,'-O',str(CHECKS/'rr003_partial_verify.py'),
                                   '--ceiling','0','--require-bijection','--output',str(output)],
                                  cwd=ROOT,capture_output=True,text=True)
            self.assertEqual(result.returncode,2,result.stdout+result.stderr)
            self.assertEqual(json.loads(output.read_text())['full_bijection'],'unresolved')


    def test_separated_charge_recovers_count_and_preserves_boundary_rejection(self):
        for t in (0,1,2,3,4,9,37):
            p=(1,)*t
            a=extended_charge.residue_to_gap(p)
            self.assertEqual(extended_charge.gap_to_residue(a),p)
            self.assertEqual(sum(a),t)
        p=(1,)*4+(6,6)
        a=extended_charge.residue_to_gap(p)
        self.assertEqual(a,(1,3,6,6))
        self.assertEqual(extended_charge.gap_to_residue(a),p)
        for p in ((1,1,1,3),(1,1,1,1,3),(8,),(10,)):
            self.assertFalse(extended_charge.source_supported(p))
            with self.assertRaises(extended_charge.OutsideRestrictedDomain):
                extended_charge.residue_to_gap(p)
        # Unbounded-parameter sample, constructed directly above sweep ceiling.
        core=(24,24,27,27,30,33,36)
        p=(1,)*13+recursive.unglaisher_three(core)
        a=extended_charge.residue_to_gap(p)
        self.assertEqual(extended_charge.gap_to_residue(a),p)
        self.assertTrue(kr1.is_gap(a))
        self.assertEqual(sum(a),sum(p))

    def test_auxiliary_seed_preserves_branch_information_lost_by_naive_rewrite(self):
        self.assertEqual(recursive_seed.inject((3,3,4)),(2,2,3,3))
        self.assertEqual(recursive_seed.inject((5,5)),(3,7))
        for p in ((3,3,4),(5,5),(3,4,5,12,15,15)):
            target=recursive_seed.inject(p)
            self.assertEqual(recursive_seed.recover(target),p)
            self.assertEqual(sum(p),sum(target))
        # A quotient-decorated source is explicitly outside the proved lift.
        with self.assertRaises(recursive_seed.OutsideSeedDomain):
            recursive_seed.inject((13,))
        with self.assertRaises(recursive_seed.OutsideSeedDomain):
            recursive_seed.recover((2,))

    def test_involution_walk_changes_counts_to_avoid_fixed_fiber_obstruction(self):
        p=(3,3,14,14)
        image=product_walk.join_p3(p,audit=True)
        self.assertEqual(image,(3,3,3,3,11,11))
        self.assertEqual(product_walk.split_p2(image,audit=True),('P3',p))
        cut=product_walk.Cut(0,())
        p=product_walk.join_cut(cut,audit=True)
        self.assertEqual(p,(2,))
        self.assertEqual(product_walk.split_p2(p,audit=True),('K',cut))
        with self.assertRaises(ValueError):
            product_walk.join_cut(product_walk.Cut(0,(3,)))

    def test_second_walk_recovers_parity_and_distinguishes_complement(self):
        for p in ((),(1,1,1),(1,3,6,8,10)):
            packet=second_walk.join_p1(p,audit=True)
            self.assertEqual(packet.weight,sum(p))
            self.assertEqual(second_walk.split_packet(packet,audit=True),('P1',p))
        cut=second_walk.Cut(0,())
        packet=second_walk.join_cut(cut,audit=True)
        self.assertEqual(packet,second_walk.Packet(0,(7,)))
        self.assertEqual(second_walk.split_packet(packet,audit=True),('L',cut))
        with self.assertRaises(ValueError):
            second_walk.split_packet(second_walk.Packet(True,()))

    def test_intrinsic_cut_branch_rejects_interval_gap_and_six_deficit(self):
        cut=product_walk.Cut(3,(6,7,11,12,16,29,31,32,34))
        p=cut_branch.cut_to_p3(cut)
        self.assertEqual(cut_branch.p3_to_cut(p),cut)
        self.assertEqual(sum(p),cut.weight-2)
        for p in ((3,),(3,3),(3,3,3,5)):
            with self.assertRaises(cut_branch.OutsideBranch):
                cut_branch.p3_to_cut(p)

if __name__ == '__main__':
    unittest.main()
