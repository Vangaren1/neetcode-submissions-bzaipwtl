class Solution {
public:
    vector<int> productExceptSelf(vector<int> &nums)
    {
        int n = nums.size();
        int r = 1;
        vector<int> result(n, 1);

        for (int j = 1; j < n; j++)
        {
            result[j] = result[j - 1] * nums[j - 1];
        }
        for (int i = n - 1; i >= 0; i--)
        {
            result[i] = result[i] * r;
            r *= nums[i];
        }

        return result;
    }
};
