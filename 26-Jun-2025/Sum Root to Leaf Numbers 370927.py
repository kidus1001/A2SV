# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        def dfs (root, cur):
            if not root:
                return 0
            cur = cur * 10 + root.val
            if (not root.left and not root.right):
                return cur
            return dfs(root.left, cur) + dfs(root.right, cur)
        return dfs(root, 0)
        

        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        