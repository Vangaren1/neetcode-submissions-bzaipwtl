class Solution
{
public:
    int findCheapestPrice(int n, vector<vector<int>> &flights, int src, int dst, int k)
    {
        unordered_map<int, vector<pair<int, int>>> edges;

        priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> frontier;

        for (vector<int> flight : flights)
        {
            edges[flight[0]].push_back({flight[2], flight[1]});
        }

        frontier.push({0, src, 0});

        while (!frontier.empty())
        {
            int currCost = frontier.top()[0];
            int curr = frontier.top()[1];
            int stops = frontier.top()[2];
            frontier.pop();

            if (curr == dst)
            {
                return currCost;
            }

            if (stops > k)
            {
                continue;
            }

            for (auto&edge : edges[curr])
            {

                int cost = edge.first;
                int dest = edge.second;
                frontier.push({cost + currCost, dest, stops + 1});
            }
        }
        return -1;
    }
};
