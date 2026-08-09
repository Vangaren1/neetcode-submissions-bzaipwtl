class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        s = ""
        total = a + b + c
        hq = []
        if a:
            heapq.heappush(hq, (-a, "a"))
        if b:
            heapq.heappush(hq, (-b, "b"))
        if c:
            heapq.heappush(hq, (-c, "c"))

        prev = None
        while hq:
            val, key = heapq.heappop(hq)
            others = -total - val

            if val < others and val < -1:
                s += key * 2
                val += 2
                total -= 2
            else:
                s += key
                val += 1
                total -= 1

            if prev:
                heapq.heappush(hq, prev)

            if val < 0:
                prev = (val, key)
            else:
                prev = None
        return s