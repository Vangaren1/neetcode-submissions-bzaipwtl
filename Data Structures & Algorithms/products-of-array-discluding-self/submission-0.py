class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [
            1,
        ] * len(nums)
        right = left[:]
        left[0] = 1
        right[-1] = 1

        for index in range(1, len(nums)):
            left[index] = left[index - 1] * nums[index - 1]
        for index in range(len(nums) - 2, -1, -1):
            right[index] = right[index + 1] * nums[index + 1]

        return [left[index] * right[index] for index in range(len(nums))]
