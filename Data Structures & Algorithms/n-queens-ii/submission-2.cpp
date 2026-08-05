class Solution
{
private:
    int count, rows;
    unordered_set<int> columns;
    unordered_set<int> posDiag;
    unordered_set<int> negDiag;

public:
    int totalNQueens(int n)
    {
        count = 0;
        rows = n;
        backtrack(0);
        return count;
    }
    void backtrack(int row)
    {
        if (row == rows)
        {
            count++;
            return;
        }
        for (int col = 0; col < rows; col++)
        {
            if (columns.count(col) || posDiag.count(row - col) || negDiag.count(row + col))
            {
                continue;
            }

            columns.insert(col);
            posDiag.insert(row - col);
            negDiag.insert(row + col);

            backtrack(row + 1);

            columns.erase(col);
            posDiag.erase(row - col);
            negDiag.erase(row + col);
        }
    }
};