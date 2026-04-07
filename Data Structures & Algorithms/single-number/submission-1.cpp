class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int total = 0;
        for(int num : nums){
            total = total ^ num;
        }
        return total;
    
    }
};
