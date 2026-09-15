class Solution:
    def maxDifference(self, s: str) -> int:
        c = Counter(s)
        even, odd = [],[]

        for _, val in c.items():
            if val % 2 == 0:
                even.append(val)
            else:
                odd.append(val)
        minEven = min(even)
        maxOdd = max(odd)
        return  maxOdd-minEven