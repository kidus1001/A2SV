# Problem: Univalued Binary Tree - https://leetcode.com/problems/univalued-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        from collections import deque
        q = deque()
        q.append(root)
        value = root.val
        while q:
            node = q.popleft()
            if node.val != value:
                return False
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return True

        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        