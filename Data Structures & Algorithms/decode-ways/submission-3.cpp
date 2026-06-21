class Solution {
public:
int numDecodings(string s)
    {
        unordered_map<string, int> seen;
        seen[""] = 1;
        seen["0"] = 0;
        return dfs(s, seen);
    }
    int dfs(string sub, unordered_map<string, int> &seen)
    {
        if (seen.count(sub))
        {
            return seen[sub];
        }
        if (sub[0] == '0')
        {
            return 0;
        }
        if (sub.size() == 1)
        {
            return 1;
        }
        int second = stoi(sub.substr(0, 2));

        int total = dfs(sub.substr(1), seen);
        if (second >= 10 && second <= 26)
        {
            total += dfs(sub.substr(2), seen);
        }
        seen[sub] = total;
        return total;
    }
};
