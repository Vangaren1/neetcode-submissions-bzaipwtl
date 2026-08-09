class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda t: t[1])

        hq = []

        for passenger, origin, destination in trips:
            while hq and hq[0][0] <= origin:
                _, p = heapq.heappop(hq)
                capacity += p
            capacity -= passenger
            if capacity < 0:
                return False
            heapq.heappush(hq, (destination, passenger))
        return True