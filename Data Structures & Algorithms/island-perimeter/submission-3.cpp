class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        int height = grid.size();
        int width = grid[0].size();

        int perimeter = 0;

        for (int y = 0; y < height; y++)
        {
            for (int x = 0; x < width; x++)
            {
                if (grid[y][x] == 0)
                {
                    continue;
                }
                perimeter += 4;
                if (y > 0 && grid[y - 1][x] == 1)
                {
                    perimeter = perimeter - 2;
                }
                if (x > 0 && grid[y][x - 1] == 1)
                {
                    perimeter = perimeter - 2;
                }
            }
        }
        return perimeter;
    }
};