# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution(object):
    def validPath(self, n, edges, source, destination):
        from collections import defaultdict

        myGraph = defaultdict(list)

        for a,b in edges:
            myGraph[a].append(b)
            myGraph[b].append(a)
        
        visited = set()
        
        def backTrack(current):
            if (current == destination):
                return True
            visited.add(current)
            for adj in myGraph[current]:
                if adj not in visited:
                    visited.add(adj)
                    if backTrack(adj):
                        return True
            return False
        return (backTrack(source))
            


        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        