class Solution {
public:
    int maxTurbulenceSize(vector<int> &arr)
    {
        int n = arr.size();
        int best = 1;
        int count = 1;

        vector<int> compare;
        for (int index = 1; index < n; index++)
        {
            if (arr[index] > arr[index - 1])
            {
                compare.push_back(1);
            }
            else if (arr[index] < arr[index - 1])
            {
                compare.push_back(-1);
            }
            else
            {
                compare.push_back(0);
            }
        }

        for (int i = 0; i < compare.size(); i++)
        {
            if (compare[i] == 0)
            {
                count = 1;
            }
            else if (i > 0 && compare[i] == -compare[i - 1])
            {
                count++;
            }
            else
            {
                count = 2;
            }
            best = max(best, count);
        }
        return best;
    }
};