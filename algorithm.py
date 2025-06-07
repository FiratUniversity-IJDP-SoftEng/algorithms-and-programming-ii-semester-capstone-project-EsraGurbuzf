# DSU = Disjoint Set Union
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
            else: self.parent[root_j] = root_i
            self.rank[root_i] += 1
            return True 
        return False 
    
def kruskal(n_nodes, edges):
    sorted_edges = sorted(edges)
    dsu = DSU(n_nodes)
    mst_edges = []
    total_weight = 0

    for weight, u, v in sorted_edges:
        if dsu.union(u, v):
            mst_edges.append((u, v, weight))
            total_weight += weight
            if len(mst_edges) == n_nodes - 1:
                break
    return mst_edges, total_weight

