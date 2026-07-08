class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums) - 1
        ptr = 0

        while ptr < n:
            if nums[ptr] == nums[ptr + 1]:
                for index in range(ptr, n):
                    nums[index] = nums[index + 1]
                n -= 1
            else:
                ptr += 1

        return n+1