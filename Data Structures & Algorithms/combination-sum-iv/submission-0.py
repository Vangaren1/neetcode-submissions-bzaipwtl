class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        memo = {}

        def dfs(total):
            if total in memo:
                return memo[total]
            if total == target:
                return 1
            if total > target:
                return 0
            count = 0
            for num in nums:
                if num > target:
                    break
                count += dfs(total + num)
            memo[total] = count
            return count

        return dfs(0)