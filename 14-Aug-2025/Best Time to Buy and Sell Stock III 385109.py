# Problem: Best Time to Buy and Sell Stock III - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution(object):
    def maxProfit(self, prices):
        transaction1 = float('inf')
        transaction2 = float('inf')
        profit1 = 0
        profit2 = 0

        for i in range (len(prices)):
            transaction1 = min(prices[i], transaction1)
            profit1 = max(profit1, prices[i] - transaction1)
            transaction2 = min(transaction2, prices[i] - profit1)
            profit2 = max(profit2, prices[i]-transaction2)
        return profit2

        """
        :type prices: List[int]
        :rtype: int
        """
        