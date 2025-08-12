# Problem: Minimum Number of Vertices to Reach All Nodes - https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        indegree = [0]*n
        for i, j in edges:
            indegree[j]+=1

        result = []
        for i in range(n):
            if indegree[i] == 0:
                result.append(i)
        return result
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        