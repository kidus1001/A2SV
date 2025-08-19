# Problem: Counting Bits - https://leetcode.com/problems/counting-bits/

class Solution(object):
    def countBits(self, n):
        result = []
        for i in range(n+1):
            bin = []
            x = i
            while x>0:
                rem = x%2
                bin.append(rem)
                x = x//2
            oneCount = 0
            for i in bin:
                if i == 1:
                    oneCount+=1
            result.append(oneCount)
        return result
        """
        :type n: int
        :rtype: List[int]
        """
        