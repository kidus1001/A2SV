# Problem: All Nodes Distance K in Binary Tree - https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

from collections import defaultdict
from collections import deque

class Solution(object):
    def distanceK(self, root, target, k):

        graph = defaultdict(set)

        def dfs(node):

            if not node:
                return
            
            if node.left:
                graph[node.val].add(node.left.val)
                graph[node.left.val].add(node.val)

            if node.right:
                graph[node.val].add(node.right.val)
                graph[node.right.val].add(node.val)
            
            dfs(node.left)
            dfs(node.right)

        ans = []
        dfs(root)
        seen = set([target.val])
        queue = deque([(target.val,0)])

        while queue:
            node, depth = queue.popleft()

            if depth==k:
                ans.append(node)
            
            

            for n in graph[node]:
                if n not in seen:
                    seen.add(n)
                    queue.append((n, depth+1))
        
        return ans