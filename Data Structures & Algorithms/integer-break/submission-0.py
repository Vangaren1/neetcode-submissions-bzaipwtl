class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        if n == 4:
            return 4
        if n == 5:
            return 6

        dp = [float("-inf") for _ in range(n + 1)]

        dp[2] = 1
        dp[3] = 2
        dp[4] = 4
        dp[5] = 6

        for i in range(6, n + 1):
            if i % 3 == 0:
                dp[i] = 3 * dp[i - 1] // 2
            elif i % 3 == 1:
                dp[i] = 4 * dp[i - 1] // 3
            else:
                dp[i] = 2 * dp[i - 2]
        return dp[n]