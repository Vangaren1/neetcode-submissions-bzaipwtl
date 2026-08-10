class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        currCapital = w
        n = len(profits)
        used = [False for _ in range(n)]
        # do this k times
        available = []
        for _ in range(k):
            # go over and add all indexes that can be used with the starting capital to "available"

            for i in range(n):
                if capital[i] <= currCapital and not used[i]:
                    used[i] = True
                    heapq.heappush(available, (-profits[i]))
            # then add the top item into
            if available:
                currCapital += -available[0]
                heapq.heappop(available)

        return currCapital