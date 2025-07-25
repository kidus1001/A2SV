# Problem: Binary Tree Preorder Traversal - https://leetcode.com/problems/binary-tree-preorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        res = []
        def preorderTraversall (root):
            if root is None:
                return
            else:
                res.append(root.val)
                preorderTraversall (root.left)
                preorderTraversall (root.right)
        preorderTraversall(root)
        return res


        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        