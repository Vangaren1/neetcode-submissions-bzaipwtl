class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        num = 1
        while num * num <= n:
            squares.append(num * num)
            num += 1
        return self.coinChange(squares, n)

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf") for _ in range(amount + 1)]
        dp[0] = 0

        for amount in range(1, amount + 1):
            for c in coins:
                if amount - c >= 0:
                    dp[amount] = min(dp[amount], dp[amount - c] + 1)
        return dp[amount] if dp[amount] != float("inf") else -1