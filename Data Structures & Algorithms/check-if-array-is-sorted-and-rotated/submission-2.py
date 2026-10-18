class Solution:
    def check(self, nums: List[int]) -> bool:
        downcount = 0 
        n = len(nums)
        for i in range(1, n):
            if nums[i-1] > nums[i]:
                downcount += 1
        if downcount == 0:
            return True
        if downcount == 1:
            return nums[0] >= nums[-1]
        return False 