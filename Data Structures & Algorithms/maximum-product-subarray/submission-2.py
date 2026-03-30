class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        best = max(nums)
        maximum = 1
        minimum = 1
        for n in nums:
            if n == 0:
                maximum, minimum = 1, 1
                continue
            tmp = maximum * n
            maximum = max(n, maximum * n, minimum * n)
            minimum = min(n, minimum * n, tmp)
            best = max(best, maximum, minimum)
        return best