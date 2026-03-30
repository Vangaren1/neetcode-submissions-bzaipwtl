class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def check():
            return all(k in sDict and sDict[k] >= v for k, v in tDict.items())

        if len(t) > len(s):
            return ""

        sDict = defaultdict(int)
        tDict = defaultdict(int)

        for ch in t:
            tDict[ch] += 1

        ptr2 = 0

        last = None
        for ptr1 in range(len(s)):
            while ptr2 < len(s) and not check():
                sDict[s[ptr2]] += 1
                ptr2 += 1
            if ptr2 <= len(s):
                if check() and (last == None or len(last) > (ptr2 - ptr1)):
                    last = s[ptr1:ptr2]
            sDict[s[ptr1]] -= 1

        if last == None:
            last = ""

        return last