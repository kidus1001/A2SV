# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution(object):
    def orangesRotting(self, grid):

        numOfFresh = 0
        time = 0
        row, col = len(grid), len(grid[0])

        def inBound(r,c):
            return r>=0 and r <row and c >=0 and c < col

        queue = collections.deque()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    numOfFresh +=1
                if grid[i][j] == 2:
                    queue.append([i,j])
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        while queue and numOfFresh > 0:
            for _ in range(len(queue)):
                r,c = queue.popleft()
                for x,y in directions:
                    newRow = r+x
                    newCol = c+y
                    if inBound(newRow, newCol) and grid[newRow][newCol] == 1:
                        grid[newRow][newCol] = 2
                        queue.append([newRow, newCol])
                        numOfFresh -=1
            time+=1
        
        if numOfFresh == 0:
            return time
        else:
            return -1
        
        
