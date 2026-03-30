class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        height = len(grid)
        width = len(grid[0])

        def bfs(node):
            nonlocal maxArea
            queue = [node]
            count = 0
            while queue:
                y, x = queue.pop(0)

                grid[y][x] = "#"
                count += 1
                maxArea = max(maxArea, count)

                diff = ((0, 1), (0, -1), (1, 0), (-1, 0))

                for dy, dx in diff:
                    ny = dy + y
                    nx = dx + x
                    if (
                        0 <= ny < height
                        and 0 <= nx < width
                        and grid[ny][nx] == 1
                        and (ny, nx) not in queue
                    ):
                        queue.append((ny, nx))

        for y in range(height):
            for x in range(width):
                if grid[y][x] == 1:
                    bfs((y, x))

        return maxArea