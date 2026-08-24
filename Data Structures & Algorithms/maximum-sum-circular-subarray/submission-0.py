class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currMax = nums[0]
        currMin = nums[0]
        bestMax = nums[0]
        bestMin = nums[0]
        total = nums[0]

        for num in nums[1:]:
            total += num
            currMax = max(num, currMax + num)
            bestMax = max(bestMax, currMax)
            currMin = min(num, currMin + num)
            bestMin = min(bestMin, currMin)

        if bestMax < 0:
            return bestMax

        return max(bestMax, total - bestMin)