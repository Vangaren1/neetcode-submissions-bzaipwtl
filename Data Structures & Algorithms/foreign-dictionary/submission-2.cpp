class Solution
{
public:
    string foreignDictionary(vector<string> &words)
    {
        unordered_map<char, unordered_set<char>> adj;
        for (const auto &word : words)
        {
            for (char c : word)
            {
                adj[c];
            }
        }

        for (int index = 1; index < words.size(); index++)
        {
            const string &first = words[index - 1];
            const string &second = words[index];
            int minLen = min((int)first.size(), (int)second.size());

            string firstPre = first.substr(0, minLen);
            string secondPre = second.substr(0, minLen);

            if (first.size() > second.size() && firstPre == secondPre)
            {
                return "";
            }
            for (int j = 0; j < minLen; j++)
            {
                if (first[j] != second[j])
                {
                    adj[first[j]].insert(second[j]);
                    break;
                }
            }
        }

        unordered_map<char, bool> visited;
        vector<char> results;

        for (const auto &[c, neighbor] : adj)
        {
            if (dfs(c, visited, results, adj))
            {
                return "";
            }
        }
        reverse(results.begin(), results.end());
        return string(results.begin(), results.end());
    }

    bool dfs(char c, unordered_map<char, bool> &visited, vector<char> &result, unordered_map<char, unordered_set<char>> &adj)
    {
        if (visited.count(c))
        {
            return visited[c];
        }
        visited[c] = true;
        for (char neighbor : adj[c])
        {
            if (dfs(neighbor, visited, result, adj))
            {
                return true;
            }
        }
        visited[c] = false;
        result.push_back(c);
        return false;
    }
};
