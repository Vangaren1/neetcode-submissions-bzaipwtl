class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        adj = defaultdict(list)
        visited = set()

        # build edges
        for index, point in enumerate(points):
            x, y = point
            for j in range(index + 1, n):
                nx, ny = points[j]
                dist = abs(x - nx) + abs(y - ny)
                adj[index].append((dist, j))
                adj[j].append((dist, index))

        totalCost = 0
        frontier = [[0, 0]]
        while len(visited) < n:

            cost, index = heapq.heappop(frontier)
            if index in visited:
                continue
            totalCost += cost
            visited.add(index)
            for neighborCost, neighbor in adj[index]:
                if neighbor not in visited:
                    heapq.heappush(frontier, (neighborCost, neighbor))

        return totalCost

