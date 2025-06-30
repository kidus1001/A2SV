# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution(object):
    def maxAreaOfIsland(self, grid):
        r = len(grid)
        c = len(grid[0])

        visited = [[False] * c for _ in range (r)]

        def dfs (i, j):
            if (i >= r or i < 0 or j >= c or j < 0 or grid[i][j] == 0 or visited[i][j]):
                return 0
            visited[i][j] = True

            maxArea = 1
            maxArea += dfs(i+1, j)
            maxArea += dfs(i-1, j)
            maxArea += dfs(i, j+1)
            maxArea += dfs(i, j-1)
            
            return maxArea


        maxArea = 0
        for i in range (r):
            for j in range (c):
                maxLocal = dfs(i,j)
                maxArea = max(maxArea, maxLocal)
        
        return maxArea
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        