class Solution {
public:
 vector<vector<int>> combine(int n, int k)
    {
        vector<vector<int>> results;
        vector<int> curr;
        dfs(curr, n, k, 1, results);
        return results;
    }

    void dfs(vector<int> &curr, int n, int k, int index, vector<vector<int>> &results)
    {
        if (curr.size() == k)
        {
            results.push_back(curr);
            return;
        }

        if (index > n)
        {
            return;
        }

        curr.push_back(index);
        dfs(curr, n, k, index + 1, results);
        curr.pop_back();
        dfs(curr, n, k, index + 1, results);
        return;
    }
};