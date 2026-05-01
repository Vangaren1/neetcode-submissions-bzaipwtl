class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        uf = self.UnionFind(n)

        for a, b in edges:
            if not uf.union(a, b):
                return False

        return True

    class UnionFind:
        def __init__(self, n):
            self.parent = [i for i in range(n)]
            self.rank = [1] * n

        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])  # path compression
            return self.parent[x]

        def union(self, a, b):
            rootA = self.find(a)
            rootB = self.find(b)

            if rootA == rootB:
                return False

            if self.rank[rootA] > self.rank[rootB]:
                self.parent[rootB] = rootA
            elif self.rank[rootA] < self.rank[rootB]:
                self.parent[rootA] = rootB
            else:
                self.parent[rootB] = rootA
                self.rank[rootA] += 1

            return True