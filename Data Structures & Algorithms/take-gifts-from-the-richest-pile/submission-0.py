import math 
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        hq = []

        for gift in gifts:
            heapq.heappush(hq, (-1) * gift)

        for _ in range(k):

            curr = -heapq.heappop(hq)
            curr = math.floor(math.sqrt(curr))
            heapq.heappush(hq, (-1) * curr)

        return -sum(hq)