class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {
        vector<int> trusts(n,0);

        for (auto tmp : trust)
        {
            trusts[tmp[0] - 1]--;
            trusts[tmp[1] - 1]++;
        }
        for (int index = 0; index < n; index++)
        {
            if (trusts[index] == n - 1)
            {
                return index + 1;
            }
        }
        return -1;
    }
};