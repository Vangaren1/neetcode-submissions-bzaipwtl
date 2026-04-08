class Solution {
public:
    vector<vector<string>> partition(string s)
    {
        vector<vector<string>> results;
        vector<string> curr;
        dfs(s, 0, results, curr);
        return results;
    }


    void dfs(string &s, int index, vector<vector<string>> &results, vector<string> &curr)
    {
        if (index >= s.size())
        {
            results.push_back(curr);
            return;
        }

        for (int idx = index; idx < s.size(); idx++)
        {
            string sub = s.substr(index, idx - index + 1);
            if (isPalindrome(sub))
            {
                curr.push_back(sub);
                dfs(s, idx + 1, results, curr);
                curr.pop_back();
            }
        }
    }
    bool isPalindrome(string s)
    {

        string tmp;
        for (char ch : s)
        {
            if (isalnum(ch))
            {
                tmp += tolower(ch);
            }
        }
        int start = 0;
        int end = tmp.size() - 1;
        while (start <= end)
        {
            if (tmp[start] != tmp[end])
            {
                return false;
            }

            start++;
            end--;
        }
        return true;
    }
};
