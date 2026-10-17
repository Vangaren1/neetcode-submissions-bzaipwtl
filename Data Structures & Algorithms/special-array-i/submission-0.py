class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        n = len(nums)
        for index in range(1, n):
            if nums[index] % 2 == nums[index-1] % 2:
                return False
        return True 
