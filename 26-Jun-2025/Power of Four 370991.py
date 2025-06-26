# Problem: Power of Four - https://leetcode.com/problems/power-of-four/

class Solution(object):
    def isPowerOfFour(self, n):
        if n < 1:
            return False
        while n > 1:
            if n%4 != 0:
                return False     
            n/=4.0
        return True


        """
        :type n: int
        :rtype: bool
        """
        