
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        aptr = len(a) - 1
        bptr = len(b) - 1

        result = ""
        total, carry = 0, 0

        while aptr >= 0 and bptr >= 0:
            abit = int(a[aptr])
            bbit = int(b[bptr])
            total = abit ^ bbit ^ carry
            carry = (abit & bbit) or carry & (abit ^ bbit)
            result += str(total)
            aptr -= 1
            bptr -= 1

        while aptr >= 0:
            abit = int(a[aptr])
            bbit = 0
            total = abit ^ carry
            carry = (abit & bbit) or carry & (abit ^ bbit)
            result += str(total)
            aptr -= 1

        while bptr >= 0:
            abit = 0
            bbit = int(b[bptr])
            total = bbit ^ carry
            carry = (abit & bbit) or carry & (abit ^ bbit)
            result += str(total)
            bptr -= 1

        if carry:
            result += "1"

        return result[::-1]