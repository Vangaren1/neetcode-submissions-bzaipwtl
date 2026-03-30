class Solution {
public:
    int findMin(vector<int> &nums)
    {
        int n = nums.size();
        int left{0}, mid{0}, right = n - 1;

        while (left < right)
        {
            if (nums[left] < nums[right])
            {
                return nums[left];
            }

            mid = left + (right - left) / 2;

            if (nums[mid] > nums[right])
            {
                left = mid + 1;
            }
            else
            {
                right = mid;
            }
        }
        return nums[left];
    }
};
