# Problem: Power of Two - https://leetcode.com/problems/power-of-two/

class Solution(object):
    def isPowerOfTwo(self, n):
        if (n < 1):
            return False
        if (n == 1):
            return True
        return self.isPowerOfTwo (n/2.0)
        """
        :type n: int
        :rtype: bool
        """
        