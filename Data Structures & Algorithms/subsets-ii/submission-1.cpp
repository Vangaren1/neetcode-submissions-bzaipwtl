class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<int> curr;
        vector<vector<int>> results;

        sort(nums.begin(), nums.end());

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

        while (index + 1 < nums.size() && nums[index] == nums[index + 1])
        {
            index++;
        }

        curr.pop_back();
        dfs(nums, curr, results, index + 1);
    }
};
