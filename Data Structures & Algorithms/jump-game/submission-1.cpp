class Solution {
public:
    bool canJump(vector<int>& nums) {
        int endgoal = nums.size() - 1;
        for(int index = endgoal - 1; index > -1; index--){
            if(index + nums[index] >= endgoal){
                endgoal = index;
            }
        }
        return endgoal==0;
    }
};
