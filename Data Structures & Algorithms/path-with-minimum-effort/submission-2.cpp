class Solution
{
public:
    int minimumEffortPath(vector<vector<int>> &heights)
    {
        int height(heights.size()), width(heights[0].size());
        vector<pair<int, int>> diff = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        vector<vector<int>> dist(height, vector<int>(width, INT32_MAX));
        dist[0][0] = 0;
        priority_queue<
            pair<int, pair<int, int>>,
            vector<pair<int, pair<int, int>>>,
            greater<pair<int, pair<int, int>>>>
            pq;
        pq.push({0, {0, 0}});
        while (!pq.empty())
        {
            auto [effort, pos] = pq.top();
            pq.pop();
            auto [y, x] = pos;
            if (effort > dist[y][x])
            {
                continue;
            }
            int curr = heights[y][x];
            for (auto [dy, dx] : diff)
            {
                int ny = y + dy;
                int nx = x + dx;

                if (0 <= ny && 0 <= nx && ny < height && nx < width)
                {
                    int newHeight = heights[ny][nx];
                    int stepDiff = abs(curr - newHeight);
                    int newEffort = max(effort, stepDiff);
                    if (newEffort < dist[ny][nx])
                    {
                        dist[ny][nx] = newEffort;
                        pq.push({newEffort, {ny, nx}});
                    }
                }
            }
        }
        return dist[height - 1][width - 1];
    }
};
