class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def overlap(interval1, interval2):
            # [0,2] and [1,3]
            onTheLeft = interval1[1] >= interval2[0] and interval1[0] <= interval2[0]
            # [1,3] and [2,4]
            onTheRight = interval1[0] <= interval2[1] and interval1[1] >= interval2[0]
            # [1,4] and [2,3]
            inTheMiddle = interval1[0] <= interval2[0] and interval1[1] >= interval2[1]
            return onTheLeft or onTheRight or inTheMiddle

        def merge(interval1, interval2):
            left = min(interval1[0], interval2[0])
            right = max(interval1[1], interval2[1])
            return [left, right]

        def same(interval1, interval2):
            return interval1[0] == interval2[0] and interval1[1] == interval2[1]

        # if empty or the new interval goes before everything else
        if len(intervals) == 0 or newInterval[1] < intervals[0][0]:
            intervals.insert(0, newInterval)
            return intervals

        # if the new interval goes after everything else
        if newInterval[0] > intervals[-1][1]:
            intervals.append(newInterval)
            return intervals

        ptr = 0

        # insert the newInt where the start is <=

        while ptr + 1 < len(intervals) and intervals[ptr + 1][0] <= newInterval[0]:
            ptr += 1

        intervals.insert(ptr, newInterval)

        while ptr + 1 < len(intervals) and overlap(intervals[ptr], intervals[ptr + 1]):
            intervals[ptr] = merge(intervals[ptr], intervals[ptr + 1])
            intervals.pop(ptr + 1)

        intervals.sort(key=lambda x: x[0])
        return intervals