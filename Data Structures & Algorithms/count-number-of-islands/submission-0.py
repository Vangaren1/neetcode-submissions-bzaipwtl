class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        height = len(grid)
        width = len(grid[0])

        def bfs(node):
            nonlocal count
            queue = [node]

            while queue:
                y, x = queue.pop(0)
                
                grid[y][x] = "#"
                diff = ((0, 1), (0, -1), (1, 0), (-1, 0))

                for dy, dx in diff:
                    ny = dy + y
                    nx = dx + x
                    if 0 <= ny < height and 0 <= nx < width and grid[ny][nx] == "1":
                        queue.append((ny, nx))

        for y in range(height):
            for x in range(width):
                if grid[y][x] == "1":
                    count += 1
                    bfs((y, x))

        return count