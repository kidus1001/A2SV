# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution(object):
    def isBipartite(self, graph):
        n = len(graph)
        color = [None] * n

        def dfs(node, mau):
            color[node] = mau 
            for nei in graph[node]:
                if color[nei] is None:
                    if not dfs(nei, 1- mau):
                        return False

                if color[nei] == color[node]:
                    return False

            return True

        for i in range(n):
            if color[i] is None:
                if not dfs(i, 0):
                    return False

        return True
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        