# Problem: Binary Tree Level Order Traversal - https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        from collections import deque
        q = deque()
        q.append(root)
        res = []

        while q:
            sub = []
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    sub.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                
            if sub:
                res.append(sub)
        return res
                



        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        