# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution(object):
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        red_adj = defaultdict(list)
        blue_adj = defaultdict(list)

        for u, v in redEdges:
            red_adj[u].append(v)
        for u, v in blueEdges:
            blue_adj[u].append(v)

        result = [-1] * n
        visited = set()

        queue = deque()
        queue.append((0, 0, None))

        while queue:
            node, steps, color = queue.popleft()

            if (node, color) in visited:
                continue
            visited.add((node, color))

            if result[node] == -1:
                result[node] = steps

            if color != 'r':
                for nei in red_adj[node]:
                    queue.append((nei, steps + 1, 'r'))

            if color != 'b':
                for nei in blue_adj[node]:
                    queue.append((nei, steps + 1, 'b'))

        return result


        """
        :type n: int
        :type redEdges: List[List[int]]
        :type blueEdges: List[List[int]]
        :rtype: List[int]
        """
        