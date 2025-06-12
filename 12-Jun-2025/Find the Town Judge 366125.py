# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution(object):
    def findJudge(self, n, trust):
        trustedBy = [0]*n
        trustCount = [0]*n

        for a,b in trust:
            trustCount[a-1] += 1
            trustedBy[b-1] +=1
        for x in range(n):
            if (trustedBy[x] == n-1 and trustCount[x] == 0):
                return x+1
        return -1

        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        