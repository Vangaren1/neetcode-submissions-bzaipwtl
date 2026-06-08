class Solution
{
    struct PairHash
    {
        size_t operator()(const pair<int, int> &p) const
        {
            size_t h1 = hash<int>{}(p.first);
            size_t h2 = hash<int>{}(p.second);

            return h1 ^ (h2 << 1);
        }
    };

public:
    bool isInterleave(string s1, string s2, string s3)
    {
        if (s1.size() + s2.size() != s3.size())
        {
            return false;
        }

        unordered_map<pair<int, int>, bool, PairHash> cache;
        return rec(0, 0, s1, s2, s3, cache);
    }
    bool rec(int index1, int index2, string s1, string s2, string s3, unordered_map<pair<int, int>, bool, PairHash> &c)
    {
        if (c.count({index1, index2}))
        {
            return c[{index1, index2}];
        }

        int index3 = index1 + index2;

        if (index3 == s3.size())
        {
            return index1 == s1.size() && index2 == s2.size();
        }

        if (index1 < s1.size() && s1[index1] == s3[index3])
        {
            if (rec(index1 + 1, index2, s1, s2, s3, c))
            {
                c[{index1, index2}] = true;
                return true;
            }
        }
        if (index2 < s2.size() && s2[index2] == s3[index3])
        {
            if (rec(index1, index2 + 1, s1, s2, s3, c))
            {
                c[{index1, index2}] = true;
                return true;
            }
        }
        c[{index1, index2}] = false;
        return false;
    }
};
