class Solution:
    def canJump(self, nums: List[int]) -> bool:
        endGoal = len(nums) - 1

        for index in range(len(nums) - 2, -1, -1):
            if index + nums[index] >= endGoal:
                endGoal = index

        return endGoal == 0