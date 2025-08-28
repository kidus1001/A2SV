# Problem: Non-overlapping Intervals - https://leetcode.com/problems/non-overlapping-intervals/description/

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        res = 0

        intervals.sort(key=lambda x: x[1])
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            if prev_end > intervals[i][0]:
                res += 1
            else:
                prev_end = intervals[i][1]
        
        return res
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        