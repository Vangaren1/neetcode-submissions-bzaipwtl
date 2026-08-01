class Solution
{
private:
    struct TrieNode
    {
        bool terminal = false;
        unordered_map<char, TrieNode *> children;
    };

    TrieNode *root = new TrieNode();

    void insert(const string &s)
    {
        TrieNode *ptr = root;
        for (char ch : s)
        {
            if (ptr->children.count(ch) == 0)
            {
                ptr->children[ch] = new TrieNode();
            }
            ptr = ptr->children[ch];
        }
        ptr->terminal = true;
    }

public:
    int minExtraChar(string s, vector<string> &dictionary)
    {
        for (auto &word : dictionary)
        {
            insert(word);
        }

        int n = s.size();
        vector<int> dp(n + 1, 0);
        for (int index = n - 1; index >= 0; index--)
        {
            dp[index] = 1 + dp[index + 1];
            TrieNode *ptr = root;
            for (int j = index; j < n; j++)
            {
                if (ptr->children.count(s[j]) == 0)
                {
                    break;
                }
                ptr = ptr->children[s[j]];
                if (ptr->terminal)
                {
                    dp[index] = min(dp[index], dp[j + 1]);
                }
            }
        }
        return dp[0];
    }
};