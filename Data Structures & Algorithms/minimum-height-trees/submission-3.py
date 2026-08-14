class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adj = [[] for _ in range(n)]
        for source, destination in edges:
            adj[source].append(destination)
            adj[destination].append(source)

        degree = [(len(adj[i])) for i in range(n)]
        leaves = [index for index in range(n) if degree[index] == 1]
        remaining = n
        while remaining > 2:
            remaining -= len(leaves)
            newLeaves = []

            for leaf in leaves:
                for neighbor in adj[leaf]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        newLeaves.append(neighbor)
            leaves = newLeaves

        return leaves