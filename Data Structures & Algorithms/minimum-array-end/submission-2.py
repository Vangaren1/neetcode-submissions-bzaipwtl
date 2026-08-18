
class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n -= 1
        # xCount = x.bit_count()
        # nCount = n.bit_length()
        # totalBits = xCount + nCount
        xBits = bin(x)[2:]
        nBits = bin(n)[2:]
        xBits = xBits[::-1]
        nBits = nBits[::-1]
        # print(f"xBits {xBits} length {len(xBits)}, nBits {nBits} length {len(nBits)}")

        totalBits = len(xBits) + len(nBits)

        xptr, nptr = 0, 0
        result = ""
        for bit in range(totalBits):
            if xptr < len(xBits):
                if xBits[xptr] == "0":
                    if nptr >= len(nBits):
                        result += "0"
                    xptr += 1
                else:
                    result += "1"
                    xptr += 1
                    continue
            if nptr < len(nBits):
                result += nBits[nptr]
                nptr += 1

        return int(result[::-1], 2)