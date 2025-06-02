# Problem: Smallest Even Multiple - https://leetcode.com/problems/smallest-even-multiple/

class Solution(object):
    def smallestEvenMultiple(self, n):
        ans = 0
        originalNum = n
        flag = True
        while (flag is True):
            if (n%originalNum == 0 and n%2 == 0):
                flag = False
                ans = n
            n+=1
        return ans
        """
        :type n: int
        :rtype: int
        """
        