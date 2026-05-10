class Solution {
public:
    int minCostConnectPoints(vector<vector<int>>& points)     {
        int n = points.size();
        unordered_map<int, vector<pair<int, int>>> adj;
        unordered_set<int> visited;

        for (int index = 0; index < n; index++)
        {
            int x = points[index][0];
            int y = points[index][1];
            for (int j = index + 1; j < n; j++)
            {
                int nx = points[j][0];
                int ny = points[j][1];
                int dist = abs(x - nx) + abs(y - ny);
                adj[index].push_back({dist, j});
                adj[j].push_back({dist, index});
            }
        }

        int totalcost = 0;
        priority_queue<pair<int, int>, vector<pair<int,int>>, greater<pair<int,int>>> frontier;
        frontier.push({0, 0});
        while (visited.size() < n)
        {
            int cost = frontier.top().first;
            int idx = frontier.top().second;
            frontier.pop();
            if (visited.count(idx))
            {
                continue;
            }
            totalcost = totalcost + cost;
            visited.insert(idx);
            for (pair<int, int> curr : adj[idx])
            {
                if (!visited.count(curr.second))
                {
                    frontier.push(curr);
                }
            }
        }
        return totalcost;
    }
};
