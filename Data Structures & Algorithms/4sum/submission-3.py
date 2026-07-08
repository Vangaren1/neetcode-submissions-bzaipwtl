class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = set()

        left, right = 0, len(nums) - 1
        count = 0
        for left in range(len(nums) - 1):
            for right in range(len(nums) - 1, left, -1):
                l, r = left + 1, right - 1
                curr = nums[left] + nums[right]
                while l < r:
                    tmp = curr + nums[l] + nums[r]
                    if tmp == target:
                        res.add((nums[left], nums[l], nums[r], nums[right]))
                        r -= 1
                    elif tmp < target:
                        l += 1
                    else:
                        r -= 1

        return [[a, b, c, d] for a, b, c, d in res]