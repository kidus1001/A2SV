# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution(object):
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        current = [1]
        count = 0
        while (count < rowIndex):
            newCurrent = [1]
            for i in range(len(current)-1):
                newCurrent.append(current[i]+current[i+1])
            newCurrent.append(1)
            count+=1
            current = newCurrent
        return current

        """
        :type rowIndex: int
        :rtype: List[int]
        """
        