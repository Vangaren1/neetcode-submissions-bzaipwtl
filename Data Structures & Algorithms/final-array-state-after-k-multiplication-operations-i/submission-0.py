class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        hq = []
        for index, num in enumerate(nums):
            heapq.heappush(hq, (num, index))

        for _ in range(k):
            curr, idx = heapq.heappop(hq)
            heapq.heappush(hq, (curr*multiplier, idx))
        
        hq.sort(key= lambda x: x[1])

        return [ val[0] for val in hq ]



        