# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution(object):
    def fib(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n-1)+self.fib(n-2)
        """
        :type n: int
        :rtype: int
        """
        