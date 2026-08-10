class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        diff = ((0, 1), (0, -1), (1, 0), (-1, 0))
        height = len(grid)
        width = len(grid[0])

        perimeter = 0

        for y in range(height):
            for x in range(width):
                if grid[y][x] == 0:
                    continue

                perimeter += 4

                if y > 0 and grid[y - 1][x] == 1:
                    perimeter -= 2

                if x > 0 and grid[y][x - 1] == 1:
                    perimeter -= 2
        return perimeter