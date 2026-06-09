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
    int minDistance(string word1, string word2)
    {
        unordered_map<pair<int, int>, int, PairHash> dp;
        if (word1 == word2)
        {
            return 0;
        }
        return recursive(0, 0, word1, word2, dp);
    }
    int recursive(int index1, int index2, string &word1, string &word2, unordered_map<pair<int, int>, int, PairHash> &dp)
    {
        if (dp.count({index1, index2}))
        {
            return dp[{index1, index2}];
        }
        if (index1 == word1.size())
        {
            dp[{index1, index2}] = word2.size() - index2;
            return dp[{index1, index2}];
        }
        if (index2 == word2.size())
        {
            dp[{index1, index2}] = word1.size() - index1;
            return dp[{index1, index2}];
        }
        if (word1[index1] == word2[index2])
        {
            dp[{index1, index2}] = recursive(index1 + 1, index2 + 1, word1, word2, dp);
            return dp[{index1, index2}];
        }

        int insert1 = 1 + recursive(index1 + 1, index2, word1, word2, dp);
        int delete1 = 1 + recursive(index1, index2 + 1, word1, word2, dp);
        int swap = 1 + recursive(index1 + 1, index2 + 1, word1, word2, dp);
        dp[{index1, index2}] = min({insert1, delete1, swap});
        return dp[{index1, index2}];
    }
};
