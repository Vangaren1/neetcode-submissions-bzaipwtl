class Solution {
public:
vector<string> generateParenthesis(int n)
    {
        string s = "";
        vector<string> results;
        dfs(s, 0, 0, results, n);
        return results;
    }

    void dfs(string s, int left, int right, vector<string> &results, int n)
    {
        if (s.size() == 2 * n)
        {
            results.push_back(s);
        }

        if (left < n)
        {
            dfs(s + "(", left + 1, right, results, n);
        }
        if (right < left)
        {
            dfs(s + ")", left, right + 1, results, n);
        }
    }
};
