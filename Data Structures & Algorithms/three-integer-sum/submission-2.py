class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()

        nums.sort()

        for index, val in enumerate(nums):
            left = 0
            right = len(nums) - 1
            while left < index and right > index:
                check = nums[left] + val + nums[right]
                if check == 0:
                    res.add((nums[left], val, nums[right]))
                if check < 0:
                    left += 1
                else:
                    right -= 1

        return [list(p) for p in res]