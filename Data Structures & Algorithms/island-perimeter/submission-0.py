class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        diff = ((0, 1), (0, -1), (1, 0), (-1, 0))
        height = len(grid)
        width = len(grid[0])
        inUse = set()

        def dfs(y, x):
            if y < 0 or y == height or x < 0 or x == width or (y, x) in inUse:
                return 0

            total = 4
            inUse.add((y, x))
            for dy, dx in diff:

                ny, nx = dy + y, dx + x
                if 0 <= ny < height and 0 <= nx < width and grid[ny][nx] == 1:
                    total -= 1
                    total += dfs(ny, nx)

            return total

        for y in range(height):
            for x in range(width):
                if grid[y][x] == 1:
                    return dfs(y, x)
        return 0