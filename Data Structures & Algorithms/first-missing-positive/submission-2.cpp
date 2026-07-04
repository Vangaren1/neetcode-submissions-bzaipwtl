class Solution {
public:
    int firstMissingPositive(vector<int> &nums)
    {
        int n = nums.size();
        for (int index = 0; index < n; index++)
        {
            if (nums[index] <= 0 || nums[index] > n)
            {
                nums[index] = 0;
                continue;
            }
            hop(nums[index], nums);
        }
        for (int idx = 0; idx < n; idx++)
        {
            if (nums[idx] != idx + 1)
            {
                return idx + 1;
            }
        }
        return n + 1;
    }
    void hop(int value, vector<int> &nums)
    {
        while (nums[value - 1] != value)
        {
            int curr = nums[value - 1];
            nums[value - 1] = value;
            if (curr <= 0 || curr > nums.size())
            {
                break;
            }
            value = curr;
        }
    }
};