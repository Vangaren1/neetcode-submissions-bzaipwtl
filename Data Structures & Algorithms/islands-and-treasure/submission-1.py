class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        diff = ((1, 0), (-1, 0), (0, 1), (0, -1))
        height = len(grid)
        width = len(grid[0])
        inf = 2**31 - 1

        queue = deque()

        for y in range(height):
            for x in range(width):
                if grid[y][x] == 0:
                    queue.append((y, x))

        while queue:
            y, x = queue.popleft()

            for dy, dx in diff:
                ny = y + dy
                nx = x + dx
                if 0 <= ny < height and 0 <= nx < width and grid[ny][nx] == inf:
                    grid[ny][nx] = grid[y][x] + 1
                    queue.append((ny, nx))