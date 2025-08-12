# Problem: Find Center of Star Graph - https://leetcode.com/problems/find-center-of-star-graph/

class Solution(object):
    def findCenter(self, edges):
        probable = edges[0][0]
        probable1 = edges[0][1]
        probable2 = edges[1][0]
        probable3 = edges[1][1]

        if probable == probable2 or probable == probable3:
            return probable
        else:
            return probable1



        """
        :type edges: List[List[int]]
        :rtype: int
        """
        