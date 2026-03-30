class Solution:
    def isHappy(self, n: int) -> bool:
        def calc(i):
            s = str(i)
            sum = 0
            for ch in s:
                sum += int(ch) ** 2
            return sum

        seen = set()

        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = calc(n)
        return True