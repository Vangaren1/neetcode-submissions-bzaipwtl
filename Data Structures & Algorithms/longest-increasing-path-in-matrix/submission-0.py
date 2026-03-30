class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        height = len(matrix)
        width = len(matrix[0])

        seen = set()
        mDist = 0

        def dfs(y, x, dis):
            nonlocal mDist
            curr = matrix[y][x]
            diff = ((0, 1), (0, -1), (1, 0), (-1, 0))
            mDist = max(mDist, dis)
            seen.add((y, x))
            for dy, dx in diff:
                ny, nx = dy + y, dx + x
                if (
                    0 <= ny < height
                    and 0 <= nx < width
                    and (ny, nx) not in seen
                    and matrix[ny][nx] > curr
                ):
                    dfs(ny, nx, dis + 1)

            seen.remove((y, x))
            pass

        for y in range(height):
            for x in range(width):
                dfs(y, x, 1)
        return mDist