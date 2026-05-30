class Solution {
public:
bool isHappy(int n)
    {
        unordered_set<int> seen;
        while(n!=1){
            if(seen.count(n)){
                return false;
            }
            seen.insert(n);
            n = sqSum(n);
        }
        return true;
    }
    int sqSum(int n)
    {
        int total = 0;
        while (n)
        {
            total = total + (n % 10) * (n % 10);
            n = n / 10;
        }
        return total;
    }
};
