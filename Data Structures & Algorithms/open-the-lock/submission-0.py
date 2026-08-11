class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def getDigit(num, pos):
            tmp = num // 10**pos
            return tmp % 10

        # store the end points using an adjacency map
        adj = defaultdict(list)

        for i in range(10000):
            # get each digit
            digits = [getDigit(i, d) for d in range(4)]
            for pos in range(4):
                # store original
                original = digits[pos]
                digits[pos] = (original + 1) % 10
                up = digits[3] * 1000 + digits[2] * 100 + digits[1] * 10 + digits[0]
                digits[pos] = (original + 9) % 10
                down = digits[3] * 1000 + digits[2] * 100 + digits[1] * 10 + digits[0]
                # store edge in adj
                adj[i].append(up)
                adj[i].append(down)
                # restore original
                digits[pos] = original

        # remove the deadends edges
        for dead in deadends:
            adj[int(dead)] = []

        # use shortest path/ djsktra's algorithm

        dist = [float("inf") for _ in range(10000)]
        pq = []

        dist[0] = 0
        heapq.heappush(pq, (0, 0))

        while pq:
            distance, node = heapq.heappop(pq)

            if distance > dist[node]:
                continue

            for neighbor in adj[node]:
                if dist[node] + 1 < dist[neighbor]:
                    dist[neighbor] = dist[node] + 1
                    heapq.heappush(pq, (dist[neighbor], neighbor))

        return dist[int(target)] if dist[int(target)] != float('inf') else -1