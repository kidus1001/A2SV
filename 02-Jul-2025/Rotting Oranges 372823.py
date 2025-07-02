# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution(object):
    def orangesRotting(self, grid):
        sources = []
        m, n = len(grid), len(grid[0])
        # visited = [[False]*n for _ in range(m)]
        fresh = 0 
        # collect the initiall cells with rotten oranges
        for i in range(m):
            for j in range(n): 
                if grid[i][j] == 2: 
                    # visited[i][j] = True 
                    sources.append((i,j))

                if grid[i][j] == 1: 
                    fresh += 1

        if fresh == 0: 
            return 0 

        def inbound(x, y): 
            return (0 <= x < m) and (0 <= y < n)
        
        queue = deque(sources)
        total_days = 0 
        result = -1 
        while queue: 
            print(queue)
        
            for _ in range(len(queue)): 
                x, y = queue.popleft()

                for dx, dy in [(0,-1), (-1, 0), (0,1), (1,0)]: 
                    nx, ny = x+dx, y + dy
                    print(nx, ny)
                    if inbound(nx, ny) and grid[nx][ny] == 1: 
                        queue.append((nx, ny))
                        grid[nx][ny] = 2
                        result = total_days + 1


            total_days += 1
        # print(grid)
        for i in range(m):
            for j in range(n): 
                if grid[i][j] == 1: 
                    return -1
        
        return  result



        

        