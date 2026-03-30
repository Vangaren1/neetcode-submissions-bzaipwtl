class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()
        hq = []
        for n in nums:
            if n not in numSet:
                numSet.add(n)
                heapq.heappush(hq, n)

        count = 0
        mCount = 0
        while hq:
            tmp = heapq.heappop(hq)
            numSet.remove(tmp)
            count = 1
            while (tmp + 1) in numSet:
                tmp = heapq.heappop(hq)
                numSet.remove(tmp)
                count += 1
            mCount = max(mCount, count)

        # print(hq)
        return mCount