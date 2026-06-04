
class Solution
{
private:
    struct PairHash
    {
        size_t operator()(const pair<string, string> &p) const
        {
            size_t h1 = hash<string>{}(p.first);
            size_t h2 = hash<string>{}(p.second);
            return h1 ^ (h2 << 1);
        }
    };
    unordered_map<pair<string, string>, int, PairHash> seen;

public:
    int longestCommonSubsequence(string text1, string text2)
    {
        seen[{"", ""}] = 0;

        return rec(text1, text2);
    }
    int rec(string a, string b)
    {
        if (seen.count({a, b}))
        {
            return seen[{a, b}];
        }
        int ptr1(0), ptr2(0);
        if (a.size() == 0 || b.size() == 0)
        {
            return 0;
        }
        string anext = a.substr(ptr1 + 1);
        string bnext = b.substr(ptr2 + 1);

        if (a[ptr1] == b[ptr2])
        {
            seen[{a, b}] = 1 + rec(anext, bnext);
            return seen[{a, b}];
        }
        int first = rec(anext, b);
        int second = rec(a, bnext);
        int tmp = max(first, second);
        seen[{a, b}] = tmp;
        return tmp;
    }
};
