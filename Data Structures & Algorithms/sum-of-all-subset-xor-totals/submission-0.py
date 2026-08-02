class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def xor(subset: List[int]):
            total = 0
            for val in subset:
                total ^= val
            return total

        curr = []
        result = 0

        def dfs(index):
            nonlocal result
            if index == len(nums):
                result += xor(curr)
                return
            curr.append(nums[index])
            dfs(index + 1)

            curr.pop()
            dfs(index + 1)

        dfs(0)

        return result