class Solution {
public:
    int jump(vector<int>& nums) {
        int n = nums.size() - 1;

        vector<int> dp(n + 1, INT_MAX);
        dp[n] = 0; // destination takes 0 jumps from itself

        for (int index = n - 1; index >= 0; index--) {
            for (int j = 1; j <= nums[index]; j++) {
                if (index + j <= n && dp[index + j] != INT_MAX) {
                    dp[index] = min(dp[index], 1 + dp[index + j]);
                }
            }
        }

        return dp[0];
    }
};