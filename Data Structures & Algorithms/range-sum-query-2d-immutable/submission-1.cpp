class NumMatrix
{
private:
    vector<vector<int>> sumMatrix;
    int height;
    int width;
public:
    NumMatrix(vector<vector<int>> &matrix)
    {
        height = matrix.size();
        width = matrix[0].size();
        sumMatrix = vector<vector<int>>(height+1, vector<int>(width+1, 0));
        for(int y=0; y < height; y++){
            for(int x = 0; x < width; x++){
                sumMatrix[y+1][x+1] = matrix[y][x] + sumMatrix[y][x+1] + sumMatrix[y+1][x] - sumMatrix[y][x];
            }
        }
    }

    int sumRegion(int row1, int col1, int row2, int col2)
    {
        return sumMatrix[row2+1][col2+1] - sumMatrix[row2+1][col1] - sumMatrix[row1][col2+1] + sumMatrix[row1][col1];
    }
};
/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix* obj = new NumMatrix(matrix);
 * int param_1 = obj->sumRegion(row1,col1,row2,col2);
 */