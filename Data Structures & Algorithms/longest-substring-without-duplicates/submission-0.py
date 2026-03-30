class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        total = 0

        left = 0
        charSet = set()

        for index in range(len(s)):
            curr = s[index]
            if curr not in charSet:
                charSet.add(curr)
                total = max(total, index - left + 1)
            else:
                while curr in charSet:
                    charSet.remove(s[left])
                    left += 1
                charSet.add(curr)

        return total