class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for index in range(len(nums) - 1, -1, -1):
            for jindex in range(index + 1, len(nums)):
                if nums[index] < nums[jindex]:
                    dp[index] = max(dp[index], 1 + dp[jindex])
        return max(dp)