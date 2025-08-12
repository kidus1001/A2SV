# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution(object):
    def hasValidPath(self, grid):
        def dfs(grid, dire, visited, r, c, i, j):
            if i == r-1 and j == c-1: 
                return True
            visited[i][j] = 1
            for di, dj in dire[grid[i][j]-1]:
                x, y = i+di, j+dj
                if 0<=x<r and 0<=y<c and not visited[x][y] and (-di, -dj) in dire[grid[x][y]-1]:
                    if dfs(grid, dire, visited, r, c, x, y): return True
            return False
            
        r, c = len(grid), len(grid[0])
        visited = [[0]*c for _ in range(r)]
        direction = [[(0, -1),(0, 1)], [(-1, 0),(1, 0)], [(0, -1),(1, 0)], [(0, 1),(1, 0)], [(0, -1),(-1, 0)], [(0,1),(-1,0)]]

        return dfs(grid, direction, visited, r, c, 0, 0)





        # r, c = len(grid), len(grid[0])
        # visited = [[0]*c for _ in range(r)]
        # dire = [[(0,-1),(0,1)], [(-1,0),(1,0)], [(0,-1),(1,0)], [(0,1),(1,0)], [(0,-1),(-1,0)], [(0,1),(-1,0)]]
        # return dfs(grid, dire, visited, r, c, 0, 0)

        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        