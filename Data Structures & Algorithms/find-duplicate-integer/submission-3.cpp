class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        for (int index = 0; index < nums.size(); index++)
        {
            int curr = nums[index];
            if(nums[abs(curr)-1] < 0){
                return abs(curr);
            }
            nums[abs(curr)-1] = nums[abs(curr)-1] * -1;
        }

        return 0;
    }
};
