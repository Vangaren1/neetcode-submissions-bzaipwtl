class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervalMap = defaultdict(int)

        for start, end in intervals:
            currLen = end - start + 1
            for i in range(start, end + 1):
                if i in intervalMap:
                    intervalMap[i] = min(currLen, intervalMap[i])
                else:
                    intervalMap[i] = currLen

        res = []
        for q in queries:
            if q in intervalMap:
                res.append(intervalMap[q])
            else:
                res.append(-1)
        return res