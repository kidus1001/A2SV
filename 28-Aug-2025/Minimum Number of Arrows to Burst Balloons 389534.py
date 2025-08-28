# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution(object):
    def findMinArrowShots(self, points):
        points.sort(key=lambda x:x[1])
        end = float("-inf")
        count = 0
        for i in points:
            if i[0] > end:
                count += 1
                end = i[1]
        return count