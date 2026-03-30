class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pile = []
        for stone in stones:
            heapq.heappush(pile, -stone)
            
        while len(pile) > 1:
            first = -heapq.heappop(pile)
            second = -heapq.heappop(pile)
            
            if first == second:
                continue
            heapq.heappush(pile, -abs(first - second))
            
        if len(pile) == 0:
            return 0
        return abs(pile[0])