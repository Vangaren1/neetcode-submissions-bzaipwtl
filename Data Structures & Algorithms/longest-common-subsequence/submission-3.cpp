
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

        return rec(text1, text2, 0, 0);
    }
    int rec(string &a, string &b, int ptr1, int ptr2)
    {
        string acurr = a.substr(ptr1);
        string bcurr = b.substr(ptr2);
        if (seen.count({acurr, bcurr}))
        {
            return seen[{acurr, bcurr}];
        }
        if (acurr.size() == 0 || bcurr.size() == 0)
        {
            return 0;
        }
        string anext = acurr.substr(1);
        string bnext = bcurr.substr(1);

        if (a[ptr1] == b[ptr2])
        {
            seen[{acurr, bcurr}] = 1 + rec(a, b, ptr1+1, ptr2+1);
            return seen[{acurr, bcurr}];
        }
        int first = rec(a, b, ptr1 + 1, ptr2);
        int second = rec(a, b, ptr1, ptr2 + 1);
        int tmp = max(first, second);
        seen[{acurr, bcurr}] = tmp;
        return tmp;
    }
};
