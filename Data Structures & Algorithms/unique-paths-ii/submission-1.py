class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        height = len(obstacleGrid)
        width = len(obstacleGrid[0])
        dp = [[0 for _ in range(width + 1)] for _ in range(height + 1)]
        
        if obstacleGrid[height-1][width-1]==0:
            dp[height - 1][width - 1] = 1
        for y in range(height - 1, -1, -1):
            for x in range(width - 1, -1, -1):
                if obstacleGrid[y][x] == 1:
                    continue
                dp[y][x] += dp[y + 1][x] + dp[y][x + 1]

        return dp[0][0]