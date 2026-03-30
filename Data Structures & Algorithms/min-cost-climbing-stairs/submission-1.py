class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        paid = cost.copy()
        paid.append(0)

        paid[-1] = 0
        paid[-2] = cost[-1]

        for index in range(len(paid) - 3, -1, -1):
            curr = paid[index]
            paid[index] += min(paid[index + 1], paid[index + 2])

        return min(paid[0], paid[1])