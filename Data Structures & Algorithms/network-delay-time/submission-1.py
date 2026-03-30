class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # build the adjacency list
        adj = defaultdict(list)
        for start, end, time in times:
            adj[start].append((end, time))

        # build the distance array
        nodes = [float("inf") for i in range(n + 1)]

        queue = [(0, k)]
        visited = set()

        while queue:
            weight, curr = heapq.heappop(queue)
            if curr in visited:
                continue
            visited.add(curr)

            nodes[curr] = min(nodes[curr], weight)

            for node, w2 in adj[curr]:
                if node not in visited:
                    heapq.heappush(queue, (weight + w2, node))

        nodes.pop(k)
        nodes.pop(0)
        if float("inf") in nodes:
            return -1
        return max(nodes)