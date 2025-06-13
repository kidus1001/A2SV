# Problem: Determine Whether Matrix Can Be Obtained By Rotation - https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

class Solution(object):
    def findRotation(self, mat, target):
        n = len(mat)
        if mat == target:
            return True
        for _ in range (3):
            for i in range(n):
                for j in range(i+1, n):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
            for a in range(n):
                mat[a] = mat[a][::-1]
            if mat == target:
                return True
        
        return False
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
        