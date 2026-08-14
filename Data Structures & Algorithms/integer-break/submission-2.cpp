class Solution {
public:
    int integerBreak(int n) {
                unordered_map<int, int> init = {
            {2, 1},
            {3, 2},
            {4, 4},
            {5, 6}};
        if (init.count(n))
        {
            return init[n];
        }
        vector<long long > dp(n + 1, 0);
        for (auto [key, val] : init)
        {
            dp[key] = val;
        }
        for (int i = 6; i < n + 1; i++)
        {
            if (i % 3 == 0)
            {
                dp[i] = 3 * dp[i - 1] / 2;
            }
            else if (i % 3 == 1)
            {
                dp[i] = 4 * dp[i - 1] / 3;
            }
            else
            {
                dp[i] = 2 * dp[i - 2];
            }
        }
        return dp[n];
    }
};