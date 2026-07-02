class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        for index in range(1, len(prices)):
            price = prices[index]
            if price > prices[index - 1]:
                total += price - prices[index - 1]
        return total