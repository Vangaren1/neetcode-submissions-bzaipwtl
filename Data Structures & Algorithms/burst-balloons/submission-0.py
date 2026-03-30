class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {}

        def dfs(left: int, right: int):
            if left > right:
                return 0
            if (left, right) in dp:
                return dp[(left, right)]
            dp[(left, right)] = 0

            for i in range(left, right + 1):
                coins = nums[i] * nums[right + 1] * nums[left - 1]
                coins += dfs(left, i - 1) + dfs(i + 1, right)
                dp[(left, right)] = max(dp[(left, right)], coins)
            return dp[(left, right)]

        return dfs(1, len(nums) - 2)