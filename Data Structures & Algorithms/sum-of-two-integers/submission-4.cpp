class Solution {
public:
    int getSum(int a, int b) {
        int mask = 0xFFF;
        int maxp = 0x7FF;

        while(b!=0){
            int add = (a ^ b) & mask;
            int carry = ((a & b) << 1) & mask;
            a = add;
            b = carry;
        }
        if(a < maxp){
            return a;
        }
        return ~(a ^ mask);

    }
};
