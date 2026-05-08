class Solution {
public:
    int networkDelayTime(vector<vector<int>> &times, int n, int k)
    {
        unordered_map<int, vector<pair<int, int>>> adj;
        for (vector<int> time : times)
        {
            adj[time[0]].push_back({time[1], time[2]});
        }
        vector<int> nodes(n+1, INT32_MAX);
        unordered_set<int> visited;

        priority_queue<pair<int, int>, vector<pair<int,int>>, greater<pair<int,int>>> queue;
        queue.push({0, k});

        while (!queue.empty())
        {
            pair<int, int> tmp = queue.top();
            queue.pop();
            int curr = tmp.second;
            int weight = tmp.first;
            if (visited.count(curr))
            {
                continue;
            }
            visited.insert(curr);
            nodes[curr] = min(nodes[curr], weight);

            for (pair<int, int> adjacent : adj[curr])
            {
                int adjNode = adjacent.first;
                int adjWeight = adjacent.second;
                if (!visited.count(adjNode))
                {
                    queue.push({weight + adjWeight, adjNode});
                }
            }
        }
        int found = -1;
        for (int i = 1; i <= n; i++)
        {
            found = max(found, nodes[i]);
        }
        if (found == INT32_MAX)
        {
            return -1;
        }
        return found;
    }
};
