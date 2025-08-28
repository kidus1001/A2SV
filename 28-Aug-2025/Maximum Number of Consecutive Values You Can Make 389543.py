# Problem: Maximum Number of Consecutive Values You Can Make - https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/description/

class Solution(object):
    def getMaximumConsecutive(self, coins):
        res = 1
        for a in sorted(coins):
            if a > res:
                break
            res += a
        return res