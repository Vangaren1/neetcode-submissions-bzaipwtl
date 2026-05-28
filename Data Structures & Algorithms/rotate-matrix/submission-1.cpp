class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();

        for(int index = 0; index < n / 2; index ++){
            vector<int> tmp = matrix[index];
            matrix[index] = matrix[n-index-1];
            matrix[n-index-1]=tmp;
        }

        for(int i = 0; i < n; i++){
            for(int j = i+1; j < n; j++){
                int k = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = k;
            }
        }
    }
};
