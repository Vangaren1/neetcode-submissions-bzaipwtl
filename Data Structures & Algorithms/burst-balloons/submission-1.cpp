class Solution
{
    struct PairHash
    {
        size_t operator()(const pair<int, int> &p) const
        {
            size_t h1 = hash<int>{}(p.first);
            size_t h2 = hash<int>{}(p.second);

            return h1 ^ (h2 << 1);
        }
    };

public:
    int maxCoins(vector<int> &nums)
    {
        unordered_map<pair<int, int>, int, PairHash> dp;
        vector<int> nnums = {1};
        nnums.insert(nnums.end(), nums.begin(), nums.end());
        nnums.push_back(1);

        return dfs(1, nums.size(), nnums, dp);
    }
    int dfs(int left, int right, vector<int> &nums, unordered_map<pair<int, int>, int, PairHash> &dp)
    {
        if (left > right)
        {
            return 0;
        }
        if (dp.count({left, right}))
        {
            return dp[{left, right}];
        }
        dp[{left, right}] = 0;
        for (int i = left; i < right + 1; i++)
        {
            int coins = nums[i] * nums[right + 1] * nums[left - 1];
            coins += dfs(left, i - 1, nums, dp) + dfs(i + 1, right, nums, dp);
            dp[{left, right}] = max(dp[{left, right}], coins);
        }
        return dp[{left, right}];
    }
};