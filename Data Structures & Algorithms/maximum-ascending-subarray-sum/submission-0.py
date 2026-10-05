class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        curr = nums[0]
        best = curr
        for index in range(1, len(nums)):
            if nums[index] > nums[index-1]:
                curr += nums[index]
                best = max(best, curr)
            else:
                curr = nums[index]
        return best 

