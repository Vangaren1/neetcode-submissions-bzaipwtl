class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        maxArea = 0
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def dfs(pos):
            y, x = pos

            grid[y][x] = "#"
            total = 1
            for dy, dx in directions:
                ny, nx = dy + y, dx + x
                if 0 <= ny < height and 0 <= nx < width and grid[ny][nx] == 1:
                    total += dfs((ny, nx))
            return total

        for y in range(height):
            for x in range(width):
                if grid[y][x] == 1:
                    maxArea = max(maxArea, dfs((y, x)))

        return maxArea