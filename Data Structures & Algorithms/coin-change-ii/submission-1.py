class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        seen = {}

        def dfs(index, value):
            if value == 0:
                return 1
            if value < 0:
                return 0
            if index >= len(coins):
                return 0
            if (index, value) in seen:
                return seen[(index, value)]

            coin = coins[index]
            seen[(index, value)] = dfs(index, value - coin) + dfs(index + 1, value)
            return seen[(index, value)]

        return dfs(0, amount)