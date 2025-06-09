# Problem: Transpose Matrix - https://leetcode.com/problems/transpose-matrix/

class Solution(object):
    def transpose(self, matrix):
        row = len (matrix)
        col = len(matrix[0])

        matrixNew = []
        for i in range(col):
            newRow = []
            for j in range(row):
                newRow.append(matrix[j][i])
            matrixNew.append(newRow)
        return matrixNew

        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        