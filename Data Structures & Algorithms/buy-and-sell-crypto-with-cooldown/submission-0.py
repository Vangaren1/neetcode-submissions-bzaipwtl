class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}

        def rec(index, canBuy):
            if index >= len(prices):
                return 0

            if (index, canBuy) in cache:
                return cache[(index, canBuy)]

            curr = prices[index]
            cool = rec(index + 1, canBuy)
            if canBuy:
                buy = rec(index + 1, not canBuy) - curr
                cache[(index, canBuy)] = max(cool, buy)
            else:
                sell = rec(index + 2, not canBuy) + curr
                cache[((index, canBuy))] = max(sell, cool)
            return cache[((index, canBuy))]

        return rec(0, True)