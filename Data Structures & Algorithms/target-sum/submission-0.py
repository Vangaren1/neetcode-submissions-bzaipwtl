class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}

        def dfs(index, total):
            if index == len(nums):
                return 1 if total == target else 0
            if (index, total) in cache:
                return cache[(index, total)]

            curr = nums[index]
            cache[(index, total)] = dfs(index + 1, total - curr) + dfs(
                index + 1, total + curr
            )
            return cache[(index, total)]

        return dfs(0, 0)