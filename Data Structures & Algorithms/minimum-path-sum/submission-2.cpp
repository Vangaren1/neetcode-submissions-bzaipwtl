class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
                int height = grid.size();
        int width = grid[0].size();

        vector<vector<long>> dp(height + 1, vector<long>(width + 1, INT32_MAX));

        dp[height - 1][width - 1] = grid[height - 1][width - 1];
        for (int y = height - 1; y >= 0; y--)
        {
            for (int x = width - 1; x >= 0; x--)
            {
                if (y == height - 1 &&x == width - 1)
                {
                    continue;
                }
                dp[y][x] = grid[y][x] + min(dp[y + 1][x], dp[y][x + 1]);
            }
        }
        return dp[0][0];
    }
};