class Solution:
    def addBinary(self, a: str, b: str) -> str:
        aptr = len(a) - 1
        bptr = len(b) - 1

        result = []
        total, carry = 0, 0

        while aptr >= 0 or bptr >= 0 or carry:
            abit = int(a[aptr]) if aptr >= 0 else 0
            bbit = int(b[bptr]) if bptr >= 0 else 0
            total = abit ^ bbit ^ carry
            carry = (abit & bbit) or carry & (abit ^ bbit)
            result.append(str(total))
            aptr -= 1
            bptr -= 1

        return "".join(result[::-1])