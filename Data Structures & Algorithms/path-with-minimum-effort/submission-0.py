class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        height = len(heights)
        width = len(heights[0])
        diff = ((1, 0), (-1, 0), (0, 1), (0, -1))
        dist = [[float("inf") for _ in range(width)] for _ in range(height)]
        dist[0][0] = 0
        queue = [(0, 0, 0)]

        maxdiff = float("-inf")

        while queue:
            effort_so_far, y, x = heapq.heappop(queue)

            if effort_so_far > dist[y][x]:
                continue

            print(f"visiting {y},{x}, diff = {effort_so_far}")
            maxdiff = max(maxdiff, effort_so_far)
            currHeight = heights[y][x]

            for dy, dx in diff:
                ny = y + dy
                nx = x + dx
                if 0 <= ny < height and 0 <= nx < width:
                    stepDiff = abs(currHeight - heights[ny][nx])
                    newEffort = max(effort_so_far, stepDiff)
                    if newEffort < dist[ny][nx]:
                        dist[ny][nx] = newEffort
                        heapq.heappush(queue, (newEffort, ny, nx))
        return dist[height-1][width-1]