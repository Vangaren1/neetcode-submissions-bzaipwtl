class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        curr = 0
        dp = [0] * len(nums)
        for index in range(len(nums) - 1, -1, -1):

            curr += nums[index]
            dp[index] = curr

        curr = 0
        for index in range(len(nums)):
            curr += nums[index]
            if curr == dp[index]:
                return index
        return -1
