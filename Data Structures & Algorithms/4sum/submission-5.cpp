class Solution
{
public:
    vector<vector<int>> fourSum(vector<int> &nums, int target)
    {
        vector<vector<int>> res;
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int l, r;
        for (int left = 0; left < n - 3; left++)
        {
            if (left > 0 && nums[left] == nums[left - 1])
            {
                continue;
            }
            for (int right = n - 1; right > left + 2; right--)
            {
                if (right < n - 1 && nums[right] == nums[right + 1])
                {
                    continue;
                }
                l = left + 1;
                r = right - 1;
                while (l < r)
                {
                    if (l > left + 1 && nums[l] == nums[l - 1])
                    {
                        l++;
                        continue;
                    }
                    if (r < right - 1 && nums[r] == nums[r + 1])
                    {
                        r--;
                        continue;
                    }
                    long long total =
                        (long long)nums[left] + nums[l] + nums[r] + nums[right];
                    if (total == target)
                    {
                        res.push_back({nums[left], nums[l], nums[r], nums[right]});
                        l++;
                        r--;
                    }
                    else if (total < target)
                    {
                        l++;
                    }
                    else
                    {
                        r--;
                    }
                }
            }
        }
        return res;
    }
};
