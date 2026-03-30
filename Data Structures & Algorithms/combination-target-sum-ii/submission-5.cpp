class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int> &candidates, int target)
    {
        sort(candidates.begin(), candidates.end());
        vector<int> curr;
        vector<vector<int>> results;
        dfs(candidates, target, curr, results, 0, 0);
        return results;
    }

    void dfs(vector<int> &nums, int target, vector<int> &curr, vector<vector<int>> &results, int index, int total)
    {
        if (total == target)
        {
            results.push_back(curr);
            return;
        }

        if (total > target || index >= nums.size())
        {
            return;
        }

        curr.push_back(nums[index]);
        dfs(nums, target, curr, results, index + 1, total + nums[index]);

        while (index < nums.size() - 1 && nums[index] == nums[index + 1])
        {
            index++;
        }

        curr.pop_back();
        dfs(nums, target, curr, results, index + 1, total);
    }
};
