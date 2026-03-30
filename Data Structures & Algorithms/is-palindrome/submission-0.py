class Solution:
    def isPalindrome(self, s: str) -> bool:
        ar = "".join(re.split(r"[^A-Za-z0-9]+", s))
        ar = ar.lower()
        left, right = 0, len(ar) - 1

        while left < right:
            if ar[left] != ar[right]:
                return False
            left += 1
            right -= 1

        return True