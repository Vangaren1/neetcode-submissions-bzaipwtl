class Solution {
public:
vector<vector<int>> merge(vector<vector<int>> &intervals)
    {
        if (intervals.size() == 1)
        {
            return intervals;
        }

        sort(intervals.begin(), intervals.end(), [](const vector<int> &a, const vector<int> &b)
             { return a[0] < b[0]; });
        
        vector<vector<int>> result;
        result.push_back(intervals[0]);

        for(int ptr = 1; ptr < intervals.size(); ptr++)
        {
            if (overlap(intervals[ptr], result.back())){
                result.back()=merge(result.back(), intervals[ptr]);
            }else{
                result.push_back(intervals[ptr]);
            }
        }

        return result;
    }
    bool overlap(vector<int> &a, vector<int> &b)
    {
        bool left = a[1] >= b[0] && a[0] <= b[0];
        bool right = a[0] <= b[1] && a[1] >= b[0];
        bool middle = a[0] <= b[0] && a[1] >= b[1];
        return left || right || middle;
    }
    vector<int> merge(vector<int> &a, vector<int> &b)
    {
        vector<int> result;
        result.push_back(min(a[0], b[0]));
        result.push_back(max(a[1], b[1]));
        return result;
    }
};
