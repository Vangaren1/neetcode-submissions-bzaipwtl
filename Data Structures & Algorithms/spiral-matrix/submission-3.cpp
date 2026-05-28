class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> results;
        int height = matrix.size();
        int width = matrix[0].size();
        int remaining = height * width;
        vector<pair<int,int>> directions = {{0,1},{1,0},{0,-1},{-1,0}};
        int dirPos = 0;
        unordered_set<int> seen;
        pair<int,int> pos = {0,0};

        while(remaining > 0){
            seen.insert( pos.first * width + pos.second);
            results.push_back(matrix[pos.first][pos.second]);
            remaining--;
            
            pair<int, int> nextDir = directions[dirPos];

            int y = pos.first + nextDir.first;
            int x = pos.second + nextDir.second;
            pos = {y, x};
            int c = y * width + x;
            

            if( seen.count(c)>0 || y == height || y < 0 || x < 0 || x == width){
                y = y - nextDir.first;
                x = x - nextDir.second;
                dirPos = (dirPos + 1) % 4;
                nextDir = directions[dirPos];

                pos = {y+nextDir.first, x+nextDir.second};
                
            }

        }
        return results;
    }
};
