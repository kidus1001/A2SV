# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution(object):
    def maxAreaOfIsland(self, grid):
        r = len(grid)
        c = len(grid[0])

        visited = [[False] * c for _ in range(r)]

        def dfs (i, j):
            if i < 0 or j < 0 or i >= r or j >= c or visited[i][j] or grid[i][j] == 0:
                return 0
            sum = grid[i][j]

            visited[i][j] = True

            sum += dfs(i+1, j)
            sum += dfs(i-1, j)
            sum += dfs(i, j+1)
            sum += dfs(i, j-1)

            return sum
        maxArea = 0
        for i in range(r):
            for j in range (c):
                if (not visited[i][j] and grid[i][j] == 1):
                   maxArea = max(maxArea, dfs(i,j)) 
            
        return maxArea
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        