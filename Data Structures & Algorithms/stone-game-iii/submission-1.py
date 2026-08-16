class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [None for _ in range(n)]
        dp[-1] = stoneValue[-1]

        def dfs(index):
            if index >= n:
                return 0

            if dp[index] is not None:
                return dp[index]

            options = []
            if index <= n - 1:
                options.append(stoneValue[index] - dfs(index + 1))
            if index <= n - 2:
                options.append(
                    stoneValue[index] + stoneValue[index + 1] - dfs(index + 2)
                )
            if index <= n - 3:
                options.append(
                    stoneValue[index]
                    + stoneValue[index + 1]
                    + stoneValue[index + 2]
                    - dfs(index + 3)
                )
            dp[index] = max(options)
            return dp[index]

        score = dfs(0)
        if score == 0:
            return "Tie"
        if score > 0:
            return "Alice"
        if score < 0:
            return "Bob"