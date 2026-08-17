class Solution {
public:
    int rangeBitwiseAnd(int left, int right) {
                int tmp1(left), tmp2(right);
        int lbits = 0;
        while (left > 0)
        {
            lbits++;
            left >>= 1;
        }
        int rbits = 0;
        while (right > 0)
        {
            rbits++;
            right >>= 1;
        }
        left = tmp1;
        right = tmp2;

        int total(0);

        while (lbits >= 0)
        {
            int mask = 1 << rbits;
            rbits--;
            lbits--;
            int lmask = left & mask;
            int rmask = right & mask;
            if (lmask != rmask)
            {
                break;
            }
            total = total | lmask;
        }
        return total;
    }
};