class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        dp = [[0 for _ in range(width + 1)] for _ in range(height + 1)]
        dp[height - 1][width - 1] = grid[height - 1][width - 1]
        for y in range(height - 2, -1, -1):
            dp[y][width - 1] = grid[y][width - 1] + dp[y + 1][width - 1]
        for x in range(width - 2, -1, -1):
            dp[height - 1][x] = grid[height - 1][x] + dp[height - 1][x + 1]

        for y in range(height - 2, -1, -1):
            for x in range(width - 2, -1, -1):
                dp[y][x] = grid[y][x] + min(dp[y + 1][x], dp[y][x + 1])

        return dp[0][0]