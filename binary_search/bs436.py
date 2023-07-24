"""
436. Find Right Interval

You are given an array of intervals,
where intervals[i] = [starti, endi] and each starti is unique.
The right interval for an interval i is an interval j such that startj >= endi
and start j is minimized. Note that i may equal j.
Return an array of right interval indices for each interval i.
If no right interval exists for interval i, then put -1 at index i.
"""

from typing import List
from bisect import bisect_left


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = [interval[0] for interval in intervals]
        starts_sorted = sorted(starts)
        result = []

        for interval in intervals:
            end = interval[1]
            index = bisect_left(starts_sorted, end)

            if index == len(starts_sorted):
                result.append(-1)
            else:
                right_interval_start = starts_sorted[index]
                right_interval_index = starts.index(right_interval_start)
                result.append(right_interval_index)

        return result


intervals = [[3,4],[2,3],[1,2]]
s = Solution()
s.findRightInterval(intervals)