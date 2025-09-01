# Problem: Count Servers that Communicate - https://leetcode.com/problems/count-servers-that-communicate/description/

class Solution:
    def countServers(self, grid):
        row = len(grid)
        col = len(grid[0])
        serverInEachRow = [0]*row
        serverInEachCol = [0]*col

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    serverInEachRow[i] += 1
                    serverInEachCol[j] += 1
        answer = 0
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and (serverInEachRow[i] > 1 or serverInEachCol[j] > 1):
                    answer+=1
        return answer