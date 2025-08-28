# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution(object):
    def eventualSafeNodes(self, graph):
        n = len(graph)
        state = [0] * n  # 0: unvisited 1: visiting 2: safe
        safe = []

        def dfs(node):
            if state[node] != 1 and state[node] != 0:
                return state[node] == 2
            
            state[node] = 1 

            for neighbor in graph[node]:
                if state[neighbor] == 1 or not dfs(neighbor):
                    return False
            
            state[node] = 2
            return True
        
        for i in range(n):
            if dfs(i):
                safe.append(i)
        
        return safe