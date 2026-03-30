class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for index in range(len(nums)):
            if nums[abs(nums[index]) - 1] < 0:
                return abs(nums[index])
            nums[abs(nums[index]) - 1] *= -1

        return 0