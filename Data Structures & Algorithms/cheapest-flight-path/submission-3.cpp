class Solution
{
public:
    int findCheapestPrice(int n, vector<vector<int>> &flights, int src, int dst, int k)
    {
        unordered_map<int, vector<pair<int, int>>> edges;

        priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> frontier;
        vector<vector<int>> dist(n, vector<int>(k + 2, INT_MAX));

        for (auto &flight : flights)
        {
            edges[flight[0]].push_back({flight[2], flight[1]});
        }

        dist[src][0] = 0;
        frontier.push({0, src, 0});

        while (!frontier.empty())
        {
            auto currFront = frontier.top();
            frontier.pop();
            int currCost = currFront[0];
            int curr = currFront[1];
            int stops = currFront[2];

            if (curr == dst)
            {
                return currCost;
            }

            if (stops == k + 1)
            {
                continue;
            }

            for (auto &edge : edges[curr])
            {

                int cost = edge.first;
                int dest = edge.second;
                int newCost = cost + currCost;
                int stopsTaken = stops + 1;
                if (newCost < dist[dest][stopsTaken])
                {
                    dist[dest][stopsTaken] = newCost;
                    frontier.push({cost + currCost, dest, stops + 1});
                }
            }
        }
        return -1;
    }
};