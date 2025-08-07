# Problem: Pascal's Triangle - https://leetcode.com/problems/pascals-triangle/description/

class Solution(object):
    def generate(self, numRows):
        row = [1]
        count = 0
        res = [[1]]
        while count < numRows-1:
            newRow = [1]
            for i in range (len(row)-1):
                newRow.append(row[i]+row[i+1])
            newRow.append(1)
            res.append(newRow)
            row = newRow
            count+=1
        return res
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        