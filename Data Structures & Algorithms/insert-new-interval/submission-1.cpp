class Solution {
public:
vector<vector<int>> insert(vector<vector<int>> &intervals, vector<int> &newInterval)
    {
        vector<vector<int>> result;
        if (intervals.size() == 0 || newInterval[1] < intervals[0][0])
        {
            result.push_back(newInterval);
            result.insert(result.end(), intervals.begin(), intervals.end());
            return result;
        }

        if (intervals.back()[1] < newInterval[0])
        {
            intervals.push_back(newInterval);
            return intervals;
        }

        // insert the new interval and sort the list
        intervals.push_back(newInterval);
        sort(intervals.begin(), intervals.end(), [](const vector<int> &a, const vector<int> &b)
             { return a[0] < b[0]; });

        // find the overlap point
        int ptr = 0;
        while (ptr < intervals.size() - 1 && !overlap(intervals[ptr], intervals[ptr + 1]))
        {
            ptr++;
        }

        while (ptr < intervals.size() - 1 && overlap(intervals[ptr], intervals[ptr + 1]))
        {
            intervals[ptr] = merge(intervals[ptr], intervals[ptr + 1]);
            intervals.erase(intervals.begin() + ptr + 1);
        }
        return intervals;
    }
    bool overlap(vector<int> &a, vector<int> &b)
    {
        bool left = a[1] >= b[0] && a[0] <= b[0];
        bool right = a[0] <= b[1] && a[1] >= b[0];
        bool middle = a[0] <= b[0] && a[1] >= b[1];
        return left || right || middle;
    }
    bool same(vector<int> &a, vector<int> &b)
    {
        return a[0] == b[0] && a[1] == b[1];
    }
    vector<int> merge(vector<int> &a, vector<int> &b)
    {
        vector<int> result;
        result.push_back(min(a[0], b[0]));
        result.push_back(max(a[1], b[1]));
        return result;
    }
};
