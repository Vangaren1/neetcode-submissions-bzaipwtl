
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def palinSkip(n):
            left, right = 0, len(s)-1
            while left < right:
                if left == n:
                    left += 1
                elif right == n:
                    right -= 1
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                return palinSkip(l) or palinSkip(r)
            l += 1
            r -= 1
        return True