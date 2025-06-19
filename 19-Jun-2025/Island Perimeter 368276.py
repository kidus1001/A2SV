# Problem: Island Perimeter - https://leetcode.com/problems/island-perimeter/description/

class Solution(object):
    def islandPerimeter(self, grid):
        visited = set()

        def dfs(i,j):
            if (i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] == 0):
                return 1
            if ((i,j) in visited):
                return 0
            visited.add((i,j))
            res = dfs (i, j+1)
            res+= dfs(i, j-1)
            res+= dfs(i+1, j)
            res+= dfs(i-1, j)

            return res

        for i in range (len (grid)):
            for j in range (len (grid[0])):
                if grid[i][j] == 1 :
                    return dfs(i,j)

        """
        :type grid: List[List[int]]
        :rtype: int
        """
        