class Solution {
public:
    vector<int> productExceptSelf(vector<int> &nums)
    {
        vector<int> left(nums.size(), 1);
        vector<int> right(nums.size(), 1);
        vector<int> result(nums.size(), 1);
        for (int j = nums.size() - 2; j > -1; j--)
        {
            right[j] = right[j + 1] * nums[j + 1];
        }

        for (int i = 1; i < nums.size(); i++)
        {
            left[i] = left[i - 1] * nums[i - 1];
        }
        for (int k = 0; k < nums.size(); k++)
        {
            result[k] = left[k] * right[k];
        }
        return result;
    }
};
