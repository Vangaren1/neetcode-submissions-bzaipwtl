class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left, right = 1, x // 2

        mid = (left + right) // 2

        while left < right:
            curr = mid * mid

            if curr == x:
                return mid

            cnext = (mid + 1) * (mid + 1)
            if cnext == x:
                return mid + 1

            if curr < x:
                if cnext > x:
                    return mid
                left = mid + 1
            else:
                right = mid - 1
            mid = (left + right) // 2

        return mid
