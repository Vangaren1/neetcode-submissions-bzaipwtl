class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.q = []
        for n in nums:
            heapq.heappush(self.q, -n)
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.q, -val)
        return -heapq.nsmallest(self.k, self.q)[-1]