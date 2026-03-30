class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        results = []
        height = len(heights)
        width = len(heights[0])

        diff = ((0, 1), (0, -1), (1, 0), (-1, 0))
        visited = set()

        def pacific(y, x):
            if y == 0 or x == 0:
                return True
            visited.add((y, x))

            curr = heights[y][x]

            for dy, dx in diff:
                ny, nx = dy + y, dx + x
                if (
                    0 <= ny < height
                    and 0 <= nx < width
                    and (ny, nx) not in visited
                    and heights[ny][nx] <= curr
                ):
                    if pacific(ny, nx):
                        visited.remove((y, x))
                        return True
            visited.remove((y, x))
            return False

        def atlantic(y, x):
            if y == height - 1 or x == width - 1:
                return True
            visited.add((y, x))

            curr = heights[y][x]

            for dy, dx in diff:
                ny, nx = dy + y, dx + x
                if (
                    0 <= ny < height
                    and 0 <= nx < width
                    and (ny, nx) not in visited
                    and heights[ny][nx] <= curr
                ):
                    if atlantic(ny, nx):
                        visited.remove((y, x))
                        return True
            visited.remove((y, x))
            return False

        for y in range(height):
            for x in range(width):
                if pacific(y, x) and atlantic(y, x):
                    results.append((y, x))
        return results