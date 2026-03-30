class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""

        def find(left, right):
            nonlocal longest
            while left >= 0 and right < len(s) and s[left] == s[right]:
                curr = s[left : right + 1]
                if len(curr) > len(longest):
                    longest = curr
                left -= 1
                right += 1

        for index in range(len(s)):
            left, right = index, index
            if (index + 1) < len(s) and s[index] == s[index + 1]:
                find(left, right + 1)
            find(left, right)

        return longest