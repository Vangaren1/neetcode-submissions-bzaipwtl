class Solution {
public:
    int reverse(int x)
    {
        int original = x;
        x = abs(x);
        long long result = 0;
        while(x){
            result = result * 10;
            result = result + (x % 10);
            x = x / 10;
        }
        if(result > INT32_MAX){
            return 0;
        }
        if(original < 0){
            result = result * -1;
        }
        return (int)result;
    }
};
