class Solution {
public:
    vector<vector<int>> subsets(vector<int> &nums)
    {
        vector<int> curr;
        vector<vector<int>> results;

        dfs(nums, curr, results, 0);

        return results;
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
