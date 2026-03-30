class Solution
{
public:
    bool searchMatrix(vector<vector<int>> &matrix, int target)
    {
        int height = matrix.size();
        int width = matrix[0].size();

        int left{0}, mid{0}, tmp{0};
        int right = height * width;

        while (left < right)
        {
            mid = (left + right) / 2;
            tmp = matrix[mid / width][mid % width];
            if (tmp == target)
            {
                return true;
            }
            else if (tmp > target)
            {
                right = mid;
            }
            else
            {
                left = mid + 1;
            }
        }

        return false;
    }
};