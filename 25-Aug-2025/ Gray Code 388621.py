# Problem:  Gray Code - https://leetcode.com/problems/gray-code/description/

class Solution(object):
    def grayCode(self, n):
        size = 1 << n 
        return [i ^ (i >> 1) for i in range(size)]

        
        """
        :type n: int
        :rtype: List[int]
        """
        