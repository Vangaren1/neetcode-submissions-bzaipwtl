class Solution {
public:
    int hammingWeight(uint32_t n) {
        int total(0);

        while(n){
            total = total + (n % 2);
            n = n >> 1;
        }
        return total;
    }
};
