class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = float("inf")

        lowest = min(prices[0], lowest)
        mxP = 0
        for index in range(len(prices)):
            p = prices[index] - lowest
            if p > 0:
                mxP = max(mxP, p)
            lowest = min(prices[index], lowest)
        return mxP