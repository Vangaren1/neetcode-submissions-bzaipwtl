class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []

        def dfs(index: int, curr: list, total: int):
            if total == target:
                results.append(curr.copy())
                return

            if total > target or index >= len(nums):
                return

            curr.append(nums[index])
            dfs(index, curr.copy(), total + nums[index])
            curr.pop()
            dfs(index + 1, curr, total)

        dfs(0, [], 0)
        return results