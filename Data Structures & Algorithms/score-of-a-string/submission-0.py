class Solution:
    def scoreOfString(self, s: str) -> int:
        total = 0
        for index in range(1,len(s)):
            total += abs(ord(s[index]) - ord(s[index-1]))
        return total