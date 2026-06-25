class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> dp(nums.size(), 1);
        for (int index = nums.size() - 1; index >= 0; index--)
        {
            for (int jindex = index + 1; jindex < nums.size(); jindex++)
            {
                if (nums[index] < nums[jindex])
                {
                    dp[index] = max(dp[index], 1 + dp[jindex]);
                }
            }
        }
        return *max_element(dp.begin(), dp.end());
    }
};
