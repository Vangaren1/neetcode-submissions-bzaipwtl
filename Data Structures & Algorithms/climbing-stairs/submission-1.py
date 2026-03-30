class Solution:
    def climbStairs(self, n: int) -> int:
        stairs = [0 for _ in range(n)]

        stairs[0] = 1
        if n == 1:
            return 1
        stairs[1] = 2
        if n == 2:
            return 2

        for index in range(3, n + 1):
            stairs[index - 1] = stairs[index - 2] + stairs[index - 3]

        return stairs[n - 1]