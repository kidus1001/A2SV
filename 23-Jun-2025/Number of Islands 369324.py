# Problem: Number of Islands - https://leetcode.com/problems/number-of-islands/

class Solution(object):
    def numIslands(self, grid):
        row = len(grid)
        col = len(grid[0])
        visited = set()

        def dfs (r, c):
            if (r < 0 or r >= row or c < 0 or c >= col or (r,c) in visited  or grid[r][c] == '0'):
                return
            visited.add((r,c))
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1' and (i,j) not in visited:
                    dfs(i,j)
                    count+=1
    
        return count
        

        """
        :type grid: List[List[str]]
        :rtype: int
        """
        