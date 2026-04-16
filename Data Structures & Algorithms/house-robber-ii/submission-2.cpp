class Solution {
public:
    int rob(vector<int>& nums) {
        int first = nums[0] + rob1(nums, 2, nums.size()-1);
        int second = rob1(nums, 1, nums.size());
        return max(first, second);
    }


    int rob1(vector<int>& nums, int start, int end) {
        int rob1 = 0;
        int rob2 = 0;
        int tmp=0;
        for(int index = start; index < end; index++){
            int n = nums[index];
            tmp = max(n + rob1, rob2);
            rob1 = rob2;
            rob2 = tmp;
        }
        return rob2;
    }
};
