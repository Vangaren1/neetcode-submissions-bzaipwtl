class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def overlap(interval1, interval2):
            # [0,2] and [1,3]
            onTheLeft = interval1[1] >= interval2[0] and interval1[0] <= interval2[0]
            # [1,3] and [2,4]
            onTheRight = interval1[0] <= interval2[1] and interval1[1] >= interval2[0]
            # [1,4] and [2,3]
            inTheMiddle = interval1[0] <= interval2[0] and interval1[1] >= interval2[1]
            return onTheLeft or onTheRight or inTheMiddle

        def combine(interval1, interval2):
            left = min(interval1[0], interval2[0])
            right = max(interval1[1], interval2[1])
            return [left, right]

        intervals.sort(key=lambda x: x[0])

        ptr = 0
        while ptr < len(intervals) - 1:
            if overlap(intervals[ptr], intervals[ptr + 1]):
                intervals[ptr] = combine(intervals[ptr], intervals[ptr + 1])
                intervals.pop(ptr + 1)
            else:
                ptr += 1

        return intervals