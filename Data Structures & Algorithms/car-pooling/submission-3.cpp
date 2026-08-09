class Solution
{
public:
    bool carPooling(vector<vector<int>> &trips, int capacity)
    {
        sort(trips.begin(), trips.end(),
             [](const auto &a, const auto &b)
             { return a[1] < b[1]; });
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int,int>>> hq;

        for (const auto &trip : trips)
        {
            int passenger = trip[0];
            int origin = trip[1];
            int destination = trip[2];

            while (!hq.empty() && hq.top().first <= origin)
            {
                pair<int, int> tmp = hq.top();
                hq.pop();
                capacity += tmp.second;
            }
            capacity = capacity - passenger;
            if (capacity < 0)
            {
                return false;
            }
            hq.push({destination, passenger});
        }
        return true;
    }
};