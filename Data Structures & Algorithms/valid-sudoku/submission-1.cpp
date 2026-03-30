class Solution {
public:
        bool isValidSudoku(vector<vector<char>> &board)
    {
        int height = board.size();
        int width = board[0].size();

        unordered_set<char> checkRow, checkCol;
        vector<vector<unordered_set<char>>> boxSets(3, vector<unordered_set<char>>(3));
        char tmpX, tmpY, tmpB;
        int bX, bY;
        // check rows and columns;
        for (int y = 0; y < height; y++)
        {
            checkRow.clear();
            checkCol.clear();
            for (int x = 0; x < width; x++)
            {
                tmpX = board[y][x];
                tmpY = board[x][y];
                bX = x / 3;
                bY = y / 3;
                if (tmpX != '.' && (checkRow.count(tmpX) > 0 || boxSets[bY][bX].count(tmpX) > 0))
                {
                    return false;
                }
                if (tmpY != '.' && checkCol.count(tmpY) > 0)
                {
                    return false;
                }

                checkRow.insert(tmpX);
                checkCol.insert(tmpY);
                boxSets[bY][bX].insert(tmpX);
            }
        }

        return true;
    }
};
