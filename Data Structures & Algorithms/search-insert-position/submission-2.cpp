class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        if (nums[0] > target)
        {
            return 0;
        }
        if (nums.back() < target)
        {
            return nums.size();
        }
        int left(0), mid(0);
        int right = nums.size() - 1;
        while (left <= right)
        {
            mid = (left + right) / 2;
            if (nums[mid] == target)
            {
                return mid;
            }
            if (nums[mid] < target)
            {
                left = mid + 1;
            }
            else
            {
                right = mid - 1;
            }
        }
        return left;        
    }
};