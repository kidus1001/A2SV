# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

import math
class Solution(object):
    def uniquePaths(self, m, n):
        aboveRow = [1]*n
        for _ in range (m-1):
            current = [1]*n
            for i in range (1,n):
                current[i] = current[i-1]+aboveRow[i]
            aboveRow = current
        return aboveRow[-1]

        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        # nCr = n! / (r! * (n-r)!). 

        # numer = m+n
        # denom = m

        # result = math.factorial(numer) / (math.factorial(numer-denom) * math.factorial(denom))

        
        # return result