class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stonesum = sum(stones)
        target = (stonesum+1) // 2
        memo = {}

        def dfs(index, total):
            if index == len(stones) or total >= target:
                return abs(total - (stonesum - total))

            if (index, total) in memo:
                return memo[(index, total)]

            memo[(index, total)] = min(
                dfs(index + 1, total), dfs(index + 1, total + stones[index])
            )
            return memo[(index, total)]

        return dfs(0, 0)