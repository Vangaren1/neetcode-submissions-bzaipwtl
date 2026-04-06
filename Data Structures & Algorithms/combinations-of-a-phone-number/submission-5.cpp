
class Solution
{
private:
    unordered_map<char, string> lettermap = {
        {'2', "abc"},
        {'3', "def"},
        {'4', "ghi"},
        {'5', "jkl"},
        {'6', "mno"},
        {'7', "pqrs"},
        {'8', "tuv"},
        {'9', "wxyz"}};

public:
    vector<string> letterCombinations(string digits)
    {
        vector<string> results;
        string curr = "";
        if(digits.size() == 0){
            return results;
        }
        dfs(0, curr, results, digits);

        return results;
    }
    void dfs(int index, string &cur, vector<string> &results, string &digits)
    {
        if (index == digits.size())
        {
            results.push_back(cur);
            return;
        }

        for (char ch : lettermap[digits[index]])
        {
            cur.push_back(ch);
            dfs(index + 1, cur, results, digits);
            cur.pop_back();
        }
    }
};
