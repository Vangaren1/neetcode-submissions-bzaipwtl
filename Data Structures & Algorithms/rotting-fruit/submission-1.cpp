class Solution {
public:
    int orangesRotting(vector<vector<int>> &grid)
    {
        vector<pair<int, int>> diff = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        int height = grid.size();
        int width = grid[0].size();
        int oranges = 0;
        int time = 0;

        deque<vector<int>> q;

        for (int y = 0; y < height; y++)
        {
            for (int x = 0; x < width; x++)
            {
                if (grid[y][x] == 1)
                {
                    oranges++;
                }
                if (grid[y][x] == 2)
                {
                    q.push_back({y, x, 0});
                }
            }
        }

        while (!q.empty())
        {
            int currY = q.front()[0];
            int currX = q.front()[1];
            int currT = q.front()[2];
            q.pop_front();
            time = max(time, currT);

            for (pair<int, int> dyx : diff)
            {
                int ny = currY + dyx.first;
                int nx = currX + dyx.second;
                if (0 <= ny && ny < height && 0 <= nx && nx < width && grid[ny][nx] == 1)
                {
                    oranges--;
                    grid[ny][nx] = 2;
                    q.push_back({ny, nx, currT + 1});
                }
            }
        }

        if (oranges != 0)
        {
            return -1;
        }
        return time;
    }
};
