class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        height = len(matrix)
        width = len(matrix[0])

        dp = {}  # (x,y) -> lig

        def dfs(y, x, dis):
            if (y, x) in dp:
                return dp[(y, x)]

            diff = ((0, 1), (0, -1), (1, 0), (-1, 0))
            newDis = 1
            for dy, dx in diff:
                ny, nx = dy + y, dx + x
                if (
                    0 <= ny < height
                    and 0 <= nx < width
                    and matrix[ny][nx] > matrix[y][x]
                ):
                    newDis = max(newDis, 1 + dfs(ny, nx, dis + 1))
            dp[(y, x)] = newDis
            return newDis

        for y in range(height):
            for x in range(width):
                dfs(y, x, 1)

        return max(dp.values())