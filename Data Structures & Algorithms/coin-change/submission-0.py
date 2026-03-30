class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf") for _ in range(amount + 1)]
        dp[0] = 0

        for amount in range(1, amount + 1):
            for c in coins:
                if amount - c >= 0:
                    dp[amount] = min(dp[amount], dp[amount - c] + 1)
        return dp[amount] if dp[amount] != float("inf") else -1