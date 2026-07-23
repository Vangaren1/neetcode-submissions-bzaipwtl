class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        size = float("inf")
        left = 0
        curr = 0
        for index, val in enumerate(nums):
            curr += val
            while curr >= target:
                size = min(size, index - left+1)
                curr -= nums[left]
                left += 1
        return size if size < float('inf') else 0