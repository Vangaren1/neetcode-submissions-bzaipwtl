class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float("inf")] * n
        dist[src] = 0

        edges = defaultdict(list)

        for source, destination, cost in flights:
            edges[source].append((cost, destination))

        numStops = 0
        currCost = 0
        queue = [(src, numStops, currCost)]
        visited = set()
        while queue:
            curr, stops, currCost = heapq.heappop(queue)
            if curr in visited:
                continue
            visited.add(curr)

            flightsFrom = edges.get(curr, [])
            for cost, destination in flightsFrom:
                if stops <= k:
                    dist[destination] = min(dist[destination], currCost + cost)
                    if stops + 1 <= k:
                        heapq.heappush(
                            queue, (destination, stops + 1, dist[destination])
                        )

        return dist[dst] if dist[dst] != float("inf") else -1