class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]

        for source, destination in edges:
            adj[source].append(destination)
            adj[destination].append(source)

        def dfs(node, parent):
            max_depth = 0

            for neighbor in adj[node]:
                if neighbor != parent:
                    max_depth = max(max_depth, 1 + dfs(neighbor, node))

            return max_depth

        heights = []
        for index in range(n):
            heights.append(dfs(index, None))

        minimumHeight = min(heights)
        return [index for index in range(n) if heights[index] == minimumHeight]