# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution(object):
    def climbStairs(self, n):
        memo = {}
        return self.helper(n,memo)
    def helper (self, n, memo):
        if n == 0 or n ==1:
            return 1
        if n not in memo:
            memo[n] = self.helper(n-1, memo)+ self.helper(n-2, memo)
        return memo[n]
        """
        :type n: int
        :rtype: int
        """
        