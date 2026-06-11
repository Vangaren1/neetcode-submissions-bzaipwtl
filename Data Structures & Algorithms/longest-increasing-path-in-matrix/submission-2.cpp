
class Solution
{
public:
    int longestIncreasingPath(vector<vector<int>> &matrix)
    {
        vector<vector<int>> dp(matrix.size(), vector<int>(matrix[0].size(), -1));
        vector<int> results;
        for (int y = 0; y < matrix.size(); y++)
        {
            for (int x = 0; x < matrix[0].size(); x++)
            {
                results.push_back(dfs(y, x, 1, matrix, dp));
            }
        }
        return *max_element(results.begin(), results.end());
    }
    int dfs(int y, int x, int dis, vector<vector<int>> &matrix, vector<vector<int>> &dp)
    {
        if (dp[y][x] != -1)
        {
            return dp[y][x];
        }
        vector<pair<int, int>> diff = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        int newDistance = 1;
        for (auto di : diff)
        {
            int ny = y + di.first;
            int nx = x + di.second;
            if (0 <= ny &&
                ny < matrix.size() &&
                0 <= nx &&
                nx < matrix[0].size() &&
                matrix[ny][nx] > matrix[y][x])
            {
                newDistance = max(newDistance, 1 + dfs(ny, nx, dis + 1, matrix, dp));
            }
        }
        dp[y][x] = newDistance;
        return newDistance;
    }
};
