# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution(object):
    def findCircleNum(self, isConnected):
        from collections import deque

        n = len(isConnected)
        
        graph = {i: [] for i in range(n)}
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1 and i != j:
                    graph[i].append(j)
        
        visited = [False] * n
        provinces = 0

        def bfs(start):
            queue = deque([start])
            visited[start] = True
            
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
        
        for city in range(n):
            if not visited[city]:
                bfs(city)
                provinces += 1
                
        return provinces

        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        