class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 2: 
            return True 
        
        ptr = 0 
        while ptr < n-1 and nums[ptr] == nums[ptr+1]:
            ptr += 1

        if ptr == n-1:
            return True 
        increasing = nums[ptr] < nums[ptr+1]

        for i in range(ptr, n-1):
            if increasing:
                if nums[i] > nums[i+1]:
                    return False 
            else:
                if nums[i] < nums[i+1]:
                    return False 
        return True 