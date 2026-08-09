class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)

        if max(count.values()) > (len(s) + 1) // 2:
            return ""

        minArray = []

        for key, val in count.items():
            heapq.heappush(minArray, [-val, key])

        result = ""
        prev = None

        while minArray:

            val, key = heapq.heappop(minArray)

            result += key
            val += 1

            if prev:
                heapq.heappush(minArray, prev)

            if val < 0:
                prev = [val, key]
            else:
                prev = None

        return result