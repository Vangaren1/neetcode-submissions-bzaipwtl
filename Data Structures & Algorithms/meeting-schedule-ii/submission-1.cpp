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
    int minMeetingRooms(vector<Interval> &intervals)
    {
        if(intervals.size() == 0){
            return 0;
        }
        vector<Interval> startTimes(intervals);
        vector<Interval> endTimes(intervals);
        sort(startTimes.begin(), startTimes.end(), [](const Interval &a, const Interval &b){
            return a.start < b.start;
        });
        sort(endTimes.begin(), endTimes.end(), [](const Interval &a, const Interval &b){
            return a.end < b.end;
        });

        int sPtr(0), ePtr(0), count(0), maxCount(0);

        while( sPtr < intervals.size() && ePtr < intervals.size()){
            if(startTimes[sPtr].start < endTimes[ePtr].end){
                sPtr++;
                count++;
            }else{
                ePtr++;
                count--;
            }
            maxCount = max(maxCount, count);
        }
        return maxCount;
    }
};
