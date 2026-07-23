class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int size = INT32_MAX;
        int curr(0), left(0), val(0);

        for (int index = 0; index < nums.size(); index++)
        {
            val = nums[index];
            curr += nums[index];
            while (curr >= target)
            {
                size = min(size, index - left + 1);
                curr = curr - nums[left];
                left++;
            }
        }
        if( size < INT32_MAX){
            return size;
        }
        return 0;
    }
};