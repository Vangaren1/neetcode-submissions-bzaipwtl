class Solution {
public:
int subsetXORSum(vector<int> &nums)
    {
        vector<int> curr;
        vector<vector<int>> results;
        int total(0), tmp(0);
        dfs(nums, curr, results, 0);

        for (auto &subset : results)
        {
            tmp = 0;
            for (auto &val : subset)
            {
                tmp = tmp ^ val;
            }
            total += tmp;
        }
        return total;
    }
    void dfs(vector<int> &nums, vector<int> &curr, vector<vector<int>> &results, int index)
    {
        if (index == nums.size())
        {
            results.push_back(curr);
            return;
        }

        curr.push_back(nums[index]);
        dfs(nums, curr, results, index + 1);

        curr.pop_back();
        dfs(nums, curr, results, index + 1);
    }
};