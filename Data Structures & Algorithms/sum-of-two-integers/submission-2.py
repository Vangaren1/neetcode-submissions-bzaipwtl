class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        res = 0
        mask = 0xFFFFFFFF

        for i in range(32):
            abit = (a >> i) & 1
            bbit = (b >> i) & 1
            tmp = abit ^ bbit
            sumBit = tmp ^ carry
            carry = (abit & bbit) | (carry & tmp)
            if sumBit:
                res |= 1 << i

        if res > (1 << 32 - 1):
            res = ~(res ^ mask)

        return res