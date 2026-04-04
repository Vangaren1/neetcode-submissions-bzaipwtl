class Solution
{
public:
    const vector<pair<int, int>> diff = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    bool exist(vector<vector<char>> &board, string word)
    {
        int height = board.size();
        int width = board[0].size();

        char first = word[0];

        for (int y = 0; y < height; y++)
        {
            for (int x = 0; x < width; x++)
            {
                if (board[y][x] == first and dfs(board, word, 0, y, x))
                {
                    return true;
                }
            }
        }
        return false;
    }

    bool dfs(vector<vector<char>> &board, const string &word, int pos, int y, int x)
    {
        if (pos == word.size() - 1)
        {
            return true;
        }
        char curr = board[y][x];

        int height = board.size();
        int width = board[0].size();
        board[y][x] = '#';

        for (pair<int, int> tmp : diff)
        {
            int ny = y + tmp.first;
            int nx = x + tmp.second;
            if (0 <= ny && ny < height && 0 <= nx && nx < width && board[ny][nx] == word[pos + 1])
            {
                if (dfs(board, word, pos + 1, ny, nx))
                {
                    board[y][x] = curr;
                    return true;
                }
            }
        }

        board[y][x] = curr;
        return false;
    }
};