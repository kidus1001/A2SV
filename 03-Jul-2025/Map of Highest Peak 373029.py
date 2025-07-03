# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

class Solution(object):
    def highestPeak(self, isWater):
        row = len(isWater)
        col = len(isWater[0])

        queue = collections.deque()
        for i in range(row):
            for j in range (col):
                if (isWater[i][j] == 0):
                    isWater[i][j] = -1
                else:
                    isWater[i][j] = 0
                    queue.append((i,j))
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                newX = dx+x
                newY = dy+y
                if 0<=newX<row and 0<=newY<col:
                    if isWater [newX][newY] == -1:
                        isWater [newX][newY] = isWater[x][y] + 1
                        queue.append((newX, newY))
        
        return isWater
        """
        :type isWater: List[List[int]]
        :rtype: List[List[int]]
        """
        