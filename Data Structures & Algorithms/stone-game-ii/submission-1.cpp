
class Solution
{
private:
    vector<vector<vector<int>>> dp;

public:
    int stoneGameII(vector<int> &piles)
    {
        int n = piles.size();
        dp.resize(2, vector<vector<int>>(n, vector<int>(n + 1, -1)));
        return dfs(1, 0, 1, piles);
    }
    int dfs(int alice, int index, int m, vector<int> &piles)
    {
        if (index == piles.size())
        {
            return 0;
        }
        if (dp[alice][index][m] != -1)
        {
            return dp[alice][index][m];
        }
        int res = alice == 1 ? 0 : INT32_MAX;
        int total = 0;

        for (int x = 1; x <= 2 * m; x++)
        {
            if (index + x > piles.size()){
                break;
            }
                
            total += piles[index + x - 1];
            if (alice==1)
            {
                res = max(res, total + dfs(0, index + x, max(m, x), piles));
            }
            else
            {
                res = min(res, dfs(1, index + x, max(m, x), piles));
            }
        }
        dp[alice][index][m] = res;
        return res;
    }
};