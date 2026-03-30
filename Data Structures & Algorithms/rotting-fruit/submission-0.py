class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        diff = ((0, 1), (0, -1), (1, 0), (-1, 0))
        time = 0
        oranges = 0
        queue = deque()

        for y in range(height):
            for x in range(width):
                if grid[y][x] == 1:
                    oranges += 1
                elif grid[y][x] == 2:
                    queue.append((y, x, 0))

        while queue:
            y, x, t = queue.popleft()
            time = max(t, time)
            for dy, dx in diff:
                ny, nx = dy + y, dx + x
                if 0 <= ny < height and 0 <= nx < width and grid[ny][nx] == 1:
                    grid[ny][nx] = 2
                    oranges -= 1
                    queue.append((ny, nx, t + 1))

        return time if oranges == 0 else -1