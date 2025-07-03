# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution(object):
    def updateMatrix(self, mat):
        row = len(mat)
        col = len(mat[0])
        result = [[-1 for x in range (col)] for _ in range (row)]
        queue = collections.deque()

        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        def checkBound (x,y):
            if x>=0 and y >= 0 and x < row and y < col:
                if result[x][y] == -1:
                    return True
            return False

        for i in range (row):
            for j in range (col):
                if mat[i][j] == 0:
                    queue.append((i,j))
                    result[i][j] = 0

        
        while queue:
            x,y = queue.popleft()
            for a, b in directions:
                newX = a+x
                newY = b+y

                if (checkBound(newX, newY)):
                    result[newX][newY] = result[x][y]+1
                    queue.append((newX, newY))
            
        return result
                


        
        




        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        