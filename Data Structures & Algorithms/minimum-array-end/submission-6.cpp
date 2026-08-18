class Solution {
public:
    long long minEnd(int n, int x) {
        long long k = static_cast<long long>(n) - 1;
        long long xmask(1), kmask(1), result(0), currX(0), currK(0);
        int xBits(0), tmpX(x), kBits(0), tmpK(k);
        while (tmpX)
        {
            xBits++;
            tmpX = tmpX >> 1;
        }
        while (tmpK)
        {
            kBits++;
            tmpK = tmpK >> 1;
        }
        int totalbits = xBits + kBits;
        for (int bit = 0; bit < totalbits; bit++)
        {
            currX = x & xmask;
            currK = k & kmask;

            if (currX == 0)
            {
                result = result | currK;
            }
            else
            {
                result = result | currX;
                k = k << 1;
            }
            kmask = kmask << 1;
            xmask = xmask << 1;
        }
        return result;
    }
};