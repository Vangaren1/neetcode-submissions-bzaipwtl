class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
                if (intervals.size() == 0)
        {
            return 0;
        }
        sort(intervals.begin(), intervals.end(), [](const vector<int> &a, const vector<int> &b)
             { return a[0] < b[0]; });
        int prevEnd = intervals[0][1];
        int result = 0;

        for (int index = 1; index < intervals.size(); index++)
        {
            const auto inter = intervals[index];
            if (inter[0] >= prevEnd)
            {
                prevEnd = inter[1];
            }
            else
            {
                result++;
                prevEnd = min(inter[1], prevEnd);
            }
        }
        return result;
    }
};
