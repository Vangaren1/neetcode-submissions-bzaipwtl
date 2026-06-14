/**
 * Definition of Interval:
 * class Interval {
 * public:
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

class Solution {
public:
    bool canAttendMeetings(vector<Interval>& intervals) {
        if(intervals.size()==0){
            return true;
        }
        sort(intervals.begin(), intervals.end(),
             [](const Interval &a, const Interval &b)
             {
                 return a.start < b.start;
             });
        for (int index = 0; index < intervals.size() - 1; index++)
        {
            if(intervals[index].end > intervals[index+1].start){
                return false;
            }
        }
        return true;
    }
};
