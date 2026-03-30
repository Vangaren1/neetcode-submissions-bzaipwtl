class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        star = []

        for index, ch in enumerate(s):
            if ch == "(":
                left.append(index)
            elif ch == "*":
                star.append(index)
            else:
                if len(left) > 0:
                    left.pop()
                elif len(star) > 0:
                    star.pop()
                else:
                    return False

        if len(star) < len(left):
            return False

        while left:
            curr = left.pop()
            if star[-1] < curr:
                return False
            star.pop()

        return True