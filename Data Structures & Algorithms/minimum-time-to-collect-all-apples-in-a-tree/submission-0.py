class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        applesToFind = hasApple.count(True)
        if applesToFind == 0:
            return 0

        adj = defaultdict(list)

        for src, dest in edges:
            adj[src].append(dest)
            adj[dest].append(src)

        visited = set()

        def dfs(node):
            visited.add(node)
            total = 0
            apple = False
            if hasApple[node]:
                apple = True

            for child in adj[node]:
                if child in visited:
                    continue
                app, cost = dfs(child)
                if app:
                    apple = True
                    total += cost + 2
            return (apple, total)

        return dfs(0)[1]