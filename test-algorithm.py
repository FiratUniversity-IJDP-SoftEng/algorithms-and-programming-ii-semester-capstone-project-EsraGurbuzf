# test_algorithm.py

import unittest
from algorithm import kruskal # Import the kruskal function from algorithm.py

# Create our test class by inheriting from unittest.TestCase
class TestKruskalAlgorithm(unittest.TestCase):

    def test_basic_connected_graph(self):
        # Test for a simple, connected graph
        num_nodes = 4
        edges = [
            (1, 0, 1),
            (3, 0, 2),
            (2, 1, 2),
            (4, 1, 3),
            (5, 2, 3)
        ]
        # Expected MST edges (order doesn't matter, content does)
        # Edges: (0,1,1), (1,2,2), (1,3,4)
        # Total weight: 1 + 2 + 4 = 7
        # For Kruskal: It typically selects (1,0,1) -> (1,2,2) -> (1,3,4).
        
        expected_total_weight = 7

        # Run Kruskal's algorithm (we don't need the steps for this test)
        mst_edges, total_weight, _ = kruskal(num_nodes, edges) 
        
        # Assert that the total weight matches the expectation
        self.assertEqual(total_weight, expected_total_weight)
        
        # Assert that the number of edges in MST is V-1
        self.assertEqual(len(mst_edges), num_nodes - 1)
        
        # (Optional) If you want to check specific MST edges (order-independent):
        # The exact set of edges might vary if there are multiple MSTs with the same total weight.
        # This part is commented out as checking total weight and edge count is usually sufficient.
        # sort_key = lambda x: (x[2], min(x[0], x[1]), max(x[0], x[1]))
        # sorted_actual_mst = sorted(mst_edges, key=sort_key)
        # sorted_expected_mst = sorted(expected_mst_edges, key=sort_key)
        # self.assertEqual(sorted_actual_mst, sorted_expected_mst)


    def test_disconnected_graph(self):
        # Test for a disconnected graph
        num_nodes = 4
        edges = [
            (1, 0, 1),  # Component 1: 0-1
            (10, 2, 3)  # Component 2: 2-3
        ]
        
        # Since it's disconnected, it should not find an MST (less than n_nodes - 1 edges)
        mst_edges, total_weight, _ = kruskal(num_nodes, edges)
        
        self.assertLess(len(mst_edges), num_nodes - 1) # Should have less than V-1 edges
        self.assertEqual(total_weight, 11) # Only sums weights of edges that don't form cycles (1+10)

    def test_graph_with_cycle(self):
        # Test for a graph containing a cycle (to verify algorithm skips cycle-forming edges)
        num_nodes = 3
        edges = [
            (1, 0, 1),
            (2, 1, 2),
            (5, 0, 2) # This edge (0,2,5) forms a cycle and should be skipped
        ]
        
        expected_total_weight = 3 # (0,1,1) + (1,2,2)
        
        mst_edges, total_weight, _ = kruskal(num_nodes, edges)
        
        self.assertEqual(total_weight, expected_total_weight)
        self.assertEqual(len(mst_edges), num_nodes - 1) # Should have 2 edges
        
        # Additional check: The cycle-forming edge (0,2,5) should NOT be in the MST
        found_cycle_edge = False
        for u, v, w in mst_edges:
            # Check both (0,2) and (2,0) for the edge
            if (u == 0 and v == 2 and w == 5) or (u == 2 and v == 0 and w == 5):
                found_cycle_edge = True
                break
        self.assertFalse(found_cycle_edge, "Cycle edge (0,2,5) should not be in MST")


    def test_single_node_graph(self):
        # Test for a single-node graph (MST should have 0 edges and 0 weight)
        num_nodes = 1
        edges = []
        mst_edges, total_weight, _ = kruskal(num_nodes, edges)
        self.assertEqual(len(mst_edges), 0)
        self.assertEqual(total_weight, 0)

    def test_graph_with_no_edges(self):
        # Test for a graph with no edges (MST should have 0 edges and 0 weight if disconnected)
        num_nodes = 5
        edges = []
        mst_edges, total_weight, _ = kruskal(num_nodes, edges)
        self.assertEqual(len(mst_edges), 0)
        self.assertEqual(total_weight, 0)
        self.assertLess(len(mst_edges), num_nodes - 1) # Should be less than V-1 (disconnected)

    def test_duplicate_weights(self):
        # Test with edges having duplicate weights
        num_nodes = 4
        edges = [
            (10, 0, 1),
            (10, 1, 2),
            (10, 2, 3),
            (10, 0, 3) # Also weight 10
        ]
        # Total weight 30, 3 edges. Multiple MSTs are possible but total weight will be the same.
        
        mst_edges, total_weight, _ = kruskal(num_nodes, edges)
        self.assertEqual(total_weight, 30)
        self.assertEqual(len(mst_edges), num_nodes - 1)


# This block is used to run the tests directly when this file is executed.
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
