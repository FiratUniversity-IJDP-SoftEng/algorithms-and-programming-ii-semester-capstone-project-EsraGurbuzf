# algorithm.py (Updated for step-by-step logging)

class DSU:
    
    def __init__(self, n_nodes):
        self.parent = list(range(n_nodes))
        self.rank = [0] * n_nodes

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_j] < self.rank[root_i]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            return True 
        return False 

def kruskal(n_nodes, edges):
    sorted_edges = sorted(edges)

    dsu = DSU(n_nodes)

    mst_edges = []
    total_weight = 0
    
    # NEW: List to store visualization steps
    # Each step will contain: (processed_edge, current_mst_edges, dsu_parent_state_copy)
    # We need a copy of parent state to show forest merging
    steps = []

    # Initial state (before processing any edge)
    steps.append({
        "step_type": "initial",
        "description": "Initial state: Each node is its own component.",
        "processed_edge": None,
        "current_mst_edges": [],
        "dsu_state": list(dsu.parent) # Copy the initial DSU state
    })

    # Keep track of which edge is currently being processed for visualization
    edge_index = 0

    for weight, u, v in sorted_edges:
        edge_index += 1
        processed_edge = (u, v, weight) # The edge currently being considered

        # Before union, get current DSU state to show potential change
        dsu_parent_before_union = list(dsu.parent) 

        # Check if adding this edge forms a cycle
        if dsu.find(u) != dsu.find(v):
            # No cycle: Add edge to MST and perform union
            dsu.union(u, v)
            mst_edges.append((u, v, weight))
            total_weight += weight
            
            # Log this step
            steps.append({
                "step_type": "edge_added",
                "description": f"Step {edge_index}: Considering edge ({u},{v}) with weight {weight}. No cycle. Edge ADDED. Components {u} and {v} merged.",
                "processed_edge": processed_edge,
                "current_mst_edges": list(mst_edges), # Copy the list
                "dsu_state": list(dsu.parent) # Copy the DSU state AFTER union
            })
            
            if len(mst_edges) == n_nodes - 1:
                # Log final step if MST is complete
                steps.append({
                    "step_type": "finished",
                    "description": f"Step {edge_index}: MST complete (found {n_nodes-1} edges).",
                    "processed_edge": processed_edge,
                    "current_mst_edges": list(mst_edges),
                    "dsu_state": list(dsu.parent)
                })
                break
        else:
            # Cycle: Skip edge
            steps.append({
                "step_type": "edge_skipped",
                "description": f"Step {edge_index}: Considering edge ({u},{v}) with weight {weight}. Forms a cycle. Edge SKIPPED. Components remain separate.",
                "processed_edge": processed_edge,
                "current_mst_edges": list(mst_edges), # Copy the list (no change)
                "dsu_state": list(dsu.parent) # Copy the DSU state (no change)
            })

    return mst_edges, total_weight, steps # Return steps as well
