# Problem: Row With Maximum Ones - https://leetcode.com/problems/row-with-maximum-ones/

class Solution(object):
    def rowAndMaximumOnes(self, mat):
        rows = len(mat)
        cols = len(mat[0])
        maxOne = 0
        selectedRow = 0
        for x in range(rows):
            oneCounter = 0
            for y in range(cols):
                if (mat[x][y] == 1):
                    oneCounter += 1
            if (oneCounter > maxOne):
                maxOne = oneCounter
                selectedRow = x
        
        arrayAnswer = []
        arrayAnswer.append(selectedRow)
        arrayAnswer.append(maxOne)
        return arrayAnswer




        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        