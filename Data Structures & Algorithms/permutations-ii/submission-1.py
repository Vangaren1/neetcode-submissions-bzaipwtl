class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        used = [False] * len(nums)

        def dfs(curr: List[int]) -> None:
            if len(curr) == len(nums):
                results.append(curr.copy())
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                # Only use the first unused copy of a duplicate value.
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                used[i] = True
                curr.append(nums[i])

                dfs(curr)

                curr.pop()
                used[i] = False

        dfs([])
        return results