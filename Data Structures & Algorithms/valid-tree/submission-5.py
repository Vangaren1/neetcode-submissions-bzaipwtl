class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != (n-1):
            return False
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = set()
        
        def dfs(v, parent):
            if(v in visited):
                return False 
            visited.add(v)
            for neighbor in adj[v]:
                if neighbor==parent:
                    continue
                if not dfs(neighbor,v):
                    return False
            return True
        return dfs(0,-1) and len(visited) == n