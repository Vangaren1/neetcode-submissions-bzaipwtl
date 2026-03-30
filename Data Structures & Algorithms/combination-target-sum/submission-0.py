class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = set()

        nums.sort()

        def dfs(index, curr):
            total = sum(curr)
            if total == target:
                results.add(tuple(curr.copy()))
                return

            if total > target or index >= len(nums):
                return

            curr.append(nums[index])
            # dfs(index)
            dfs(index, curr.copy())
            dfs(index + 1, curr.copy())

            curr.pop()
            dfs(index + 1, curr.copy())

        dfs(0, [])
        return [[i for i in r] for r in results]