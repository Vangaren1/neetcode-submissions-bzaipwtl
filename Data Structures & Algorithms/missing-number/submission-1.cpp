class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int r = nums.size() + 1;
        int tmp = 0;
        for(int i=0; i < r; i++){
            tmp = tmp ^ i;
        }
        for(int num: nums){
            tmp = tmp ^ num;
        }
        return tmp;
    }
};
