class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        maxDay = max(days)
        dp = [0] * (maxDay + 1)
        ptr = 0
        for day in range(1, maxDay + 1):
            if day != days[ptr]:
                dp[day] = dp[day - 1]
                continue
            dp[day] = min(
                costs[0] + dp[max(0, day - 1)],
                costs[1] + dp[max(0, day - 7)],
                costs[2] + dp[max(0, day - 30)],
            )
            ptr += 1
        return dp[-1]