class Solution {
public:
    int findMaximizedCapital(int k, int w, vector<int>& profits, vector<int>& capital) {
        int n = profits.size();
        int currCapital = w;
        vector<pair<int, int>> capProf;

        for (int index = 0; index < n; index++)
        {
            capProf.push_back({capital[index], profits[index]});
        }
        sort(capProf.begin(), capProf.end(), greater<pair<int, int>>());

        priority_queue<int> available;

        for (int i = 0; i < k; i++)
        {
            while (!capProf.empty() && capProf.back().first <= currCapital)
            {
                available.push(capProf.back().second);
                capProf.pop_back();
            }
            if (!available.empty())
            {
                currCapital += available.top();
                available.pop();
            }
        }
        return currCapital;
    }
};