# Problem: Last Stone Weight II - https://leetcode.com/problems/last-stone-weight-ii/description/

class Solution(object):
    def lastStoneWeightII(self, stones):
        dp = {0}
        sumA = sum(stones)
        for a in stones:
            dp |= {a + i for i in dp}
        return min(abs(sumA - i - i) for i in dp)
        """
        :type stones: List[int]
        :rtype: int
        """
        