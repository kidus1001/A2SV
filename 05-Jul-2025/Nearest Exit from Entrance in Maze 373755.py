# Problem: Nearest Exit from Entrance in Maze - https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

class Solution(object):
    def nearestExit(self, maze, entrance):
        row, col = len(maze), len(maze[0])
        queue = collections.deque()
        visited = [[False] * col for _ in range(row)]
        
        queue.append((entrance[0], entrance[1], 0))
        visited[entrance[0]][entrance[1]] = True

        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        while queue:
            x, y, steps = queue.popleft()
            for dx, dy in directions:
                newX, newY = x + dx, y + dy
                if 0 <= newX < row and 0 <= newY < col:
                    if not visited[newX][newY] and maze[newX][newY] == '.':
                        if newX == 0 or newX == row-1 or newY == 0 or newY == col-1:
                            return steps + 1
                        queue.append((newX, newY, steps + 1))
                        visited[newX][newY] = True

        return -1
