class Solution
{
private:
    class UnionFind
    {
    private:
        vector<int> parent;

    public:
        UnionFind(int n)
        {
            parent.resize(n);
            iota(parent.begin(), parent.end(), 0);
        }

        int root(int x)
        {
            while (x != parent[x])
            {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            return x;
        }

        bool connected(int a, int b)
        {
            return root(a) == root(b);
        }

        void unite(int a, int b)
        {
            int rootA = root(a);
            int rootB = root(b);

            if (rootA != rootB)
            {
                parent[rootA] = rootB;
            }
        }
    };

public:
    vector<vector<string>> accountsMerge(vector<vector<string>> &accounts)
    {
        UnionFind qu = UnionFind(accounts.size());

        unordered_map<string, int> emailMap;
        vector<string> usernames;
        vector<vector<string>> results;

        for (int index = 0; index < accounts.size(); index++)
        {
            vector<string> &email = accounts[index];
            usernames.push_back(email[0]);
            for (int idx = 1; idx < email.size(); idx++)
            {
                if (emailMap.count(email[idx]))
                {
                    qu.unite(index, emailMap[email[idx]]);
                }
                else
                {
                    emailMap[email[idx]] = index;
                }
            }
        }

        unordered_map<int, vector<string>> newAcct;

        for (auto [em, i] : emailMap)
        {
            newAcct[qu.root(i)].push_back(em);
        }

        for (auto [key, arr] : newAcct)
        {
            vector<string> account = {usernames[key]};
            account.insert(account.end(), arr.begin(), arr.end());
            results.push_back(account);
        }
        return results;
    }
};