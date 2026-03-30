class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def getDict(s):
            d = defaultdict(int)
            for c in s:
                d[c] += 1
            return frozenset(d.items())

        groupDict = defaultdict(list)

        for s in strs:
            d = getDict(s)
            groupDict[d].append(s)

        return [v for v in groupDict.values()]