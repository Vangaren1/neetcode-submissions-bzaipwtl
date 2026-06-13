
class Solution
{
public:
    bool isMatch(string s, string p)
    {
        // first bool is whether or not it's used, second is value
        vector<vector<pair<bool, bool>>> grid(
            s.size()+1,
            vector<pair<bool, bool>>(p.size()+1, {false, false}));
        return dfs(s, p, 0, 0, grid);
    }
    bool dfs(string &s, string &p, int i, int j, vector<vector<pair<bool, bool>>> &cache)
    {
        if (j == p.size())
        {
            return i == s.size();
        }
        if (cache[i][j].first)
        {
            return cache[i][j].second;
        }
        bool match = i < s.size() && (s[i] == p[j] || p[j] == '.');
        if (j + 1 < p.size() && p[j + 1] == '*')
        {
            cache[i][j].first = true;
            cache[i][j].second = dfs(s, p, i, j + 2, cache) || (match && dfs(s, p, i + 1, j, cache));
            return cache[i][j].second;
        }

        if (match)
        {
            cache[i][j].first = true;
            cache[i][j].second = dfs(s, p, i + 1, j + 1, cache);
            return cache[i][j].second;
        }

        cache[i][j].first = true;
        cache[i][j].second = false;
        return false;
    }
};
