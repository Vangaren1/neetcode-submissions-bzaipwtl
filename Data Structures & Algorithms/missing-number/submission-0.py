class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        r = len(nums) + 1
        tmp = 0
        for i in range(r):
            tmp ^= i
        for num in nums:
            tmp ^= num
        return tmp