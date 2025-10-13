# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution(object):
    def maxProfit(self, prices):
        from functools import reduce
        a, b, c = reduce(
            lambda x, p: (max(x[0], x[2] - p), x[0] + p, max(x[2], x[1])),
            prices,
            (float('-inf'), 0, 0)
        )
        return max(b, c)