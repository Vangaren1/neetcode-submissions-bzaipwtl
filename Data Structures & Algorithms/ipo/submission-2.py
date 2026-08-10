class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        currCapital = w
        n = len(profits)
        # do this k times
        capProf = [(capital[i], profits[i]) for i in range(n)]
        capProf.sort(reverse=True)

        available = []
        for _ in range(k):
            # go over and add all indexes that can be used with the starting capital to "available"

            while capProf and capProf[-1][0] <= currCapital:
                _, prof = capProf.pop()
                heapq.heappush(available, (-prof))
            # then add the top item into
            if available:
                currCapital += -available[0]
                heapq.heappop(available)

        return currCapital