class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def checkDict(d: dict):
            dList = [(key, val) for key, val in d.items()]
            dList.sort(key=lambda x: x[1])
            dList.pop()
            total = 0
            for key, val in dList:
                total += val
                if total > k:
                    return True
            return False

        charDict = defaultdict(int)
        left = 0
        kCount = k
        maxFound = 0
        for index in range(len(s)):
            c = s[index]
            charDict[c] += 1
            while checkDict(charDict):
                charDict[s[left]] -= 1
                left += 1
            maxFound = max(maxFound, index - left + 1)

        return maxFound