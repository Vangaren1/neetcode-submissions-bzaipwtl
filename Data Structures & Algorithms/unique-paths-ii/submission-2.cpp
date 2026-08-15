class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
                int height = obstacleGrid.size();
        int width = obstacleGrid[0].size();
        vector<vector<int>> dp(height + 1, vector<int>(width + 1, 0));
        if(obstacleGrid[height-1][width-1]==0){
dp[height - 1][width - 1] = 1;
        }
        
        for (int y = height - 1; y >= 0; y--)
        {
            for (int x = width - 1; x >= 0; x--)
            {
                if (obstacleGrid[y][x] == 1)
                {
                    continue;
                }
                dp[y][x] += dp[y + 1][x] + dp[y][x + 1];
            }
        }
        return dp[0][0];
    }
};