# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0

        n = len(prices)
        min_price = prices[0]
        max_profit = 0

        for i in range(1, n):
            profit_today = prices[i] - min_price
            max_profit = max(max_profit, profit_today)
            min_price = min(min_price, prices[i])

        return max_profit
        """
        :type prices: List[int]
        :rtype: int
        """
        