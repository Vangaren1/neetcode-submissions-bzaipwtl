class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left == right:
            return left
        msbIndexLeft = left.bit_length() - 1
        msbIndexRight = right.bit_length() - 1

        total = 0
        while msbIndexLeft > 0:
            mask = 1 << msbIndexRight
            msbIndexRight -= 1
            msbIndexLeft -= 1
            lmask = left & mask
            rmask = right & mask
            if lmask != rmask:
                break
            total |= lmask
        return total