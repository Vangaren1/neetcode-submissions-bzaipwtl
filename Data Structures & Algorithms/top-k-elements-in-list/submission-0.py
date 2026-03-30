class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nCount = defaultdict(int)
        for n in nums:
            nCount[n] += 1
        countList = [list(t) for t in nCount.items()]
        countList.sort(key=lambda x: x[1], reverse=True)
        retVal = []
        for _ in range(k):
            tmp = countList.pop(0)
            retVal.append(tmp[0])
        return retVal
