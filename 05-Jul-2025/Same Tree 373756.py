# Problem: Same Tree - https://leetcode.com/problems/same-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        def traverse (p, q):
            if p == None and q == None:
                return True
            if p == None or q == None:
                return False
            return p.val == q.val and traverse (p.right, q.right) and traverse (p.left, q.left)
        return traverse (p, q)

            
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        