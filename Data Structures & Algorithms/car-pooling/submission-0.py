class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        hq = []

        for passenger, origin, destination in trips:
            if passenger > capacity:
                return False
            heapq.heappush(hq, (origin, passenger))
            heapq.heappush(hq, (destination, -passenger))

        curr = 0

        while hq:
            _, passenger = heapq.heappop(hq)
            curr += passenger
            if curr > capacity:
                return False

        return True