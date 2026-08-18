class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n -= 1
        xmask = 1
        nmask = 1
        nbits = n.bit_length()
        xbits = x.bit_length()
        totalBits = nbits + xbits
        result = 0

        for _ in range(totalBits):
            currX = x & xmask
            currN = n & nmask

            if currX == 0:
                result |= currN

            else:
                result |= currX
                n <<= 1
            nmask <<= 1
            xmask <<= 1
        return result