# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution(object):
    def combine(self, n, k):
        def backTrack (i, path):
            if len(path) == k:
                result.append(path[:])
                return
            for j in range(i, n+1):
                path.append(j)
                backTrack (j+1, path)
                path.pop()

        result = []
        backTrack (1, [])
        return result


        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        