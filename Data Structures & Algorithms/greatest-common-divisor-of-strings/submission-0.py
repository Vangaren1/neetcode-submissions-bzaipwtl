class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if set(str1) != set(str2):
            return ""
        if len(str2) < len(str1):
            str2, str1 = str1, str2

        # now str1 is shorter or equal
        l1 = len(str1)
        l2 = len(str2)

        g = math.gcd(l1, l2)
        # g is the theoretical largest length the gcd of strings could be

        multiplier = l2 // g

        while g > 1 and multiplier * str1[: g + 1] != str2:
            g -= 1
            if l1 % g != 0 or l2 % g != 0:
                continue
            multiplier = l2 // g

        # print(f"{l1} {l2} {g}")
        return str1[: g + 1]