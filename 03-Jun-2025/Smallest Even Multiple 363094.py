# Problem: Smallest Even Multiple - https://leetcode.com/problems/smallest-even-multiple/

class Solution(object):
    def smallestEvenMultiple(self, n):
        originalNum = n
        while (True):
            if (n%2 == 0 and n%originalNum == 0):
                return n
            n+=1
        
        """
        :type n: int
        :rtype: int
        """
        