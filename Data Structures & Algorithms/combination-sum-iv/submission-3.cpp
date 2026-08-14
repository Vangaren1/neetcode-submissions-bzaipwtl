class Solution
{
private:
    unordered_map<int, int> memo;

public:
    int combinationSum4(vector<int> &nums, int target)
    {
        memo.clear();
        sort(nums.begin(), nums.end());
        return dfs(0, target, nums);
    }
    int dfs(int total, int target, vector<int> &nums)
    {
        if (memo.count(total))
        {
            return memo[total];
        }
        if (total == target)
        {
            return 1;
        }
        int count = 0;
        for (auto num : nums)
        {
            if (total + num > target)
            {
                break;
            }
            count += dfs(total + num, target, nums);
        }
        memo[total] = count;
        return count;
    }
};
