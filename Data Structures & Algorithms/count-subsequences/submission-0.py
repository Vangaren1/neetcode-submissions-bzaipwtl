class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}

        def recursive(indexS, indexT):
            if (indexS, indexT) in cache:
                return cache[(indexS, indexT)]
            if indexT == len(t):
                return 1
            if indexS == len(s):
                return 0

            currS = s[indexS]
            currT = t[indexT]

            total = 0
            if currS == currT:
                total += recursive(indexS + 1, indexT + 1)
            total += recursive(indexS + 1, indexT)
            cache[(indexS, indexT)] = total
            return total

        return recursive(0, 0)