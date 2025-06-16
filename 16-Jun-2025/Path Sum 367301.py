# Problem: Path Sum - https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        def myFun (root, sum):
            if not root:
                return False
            sum += root.val

            if not root.left and not root.right:
                if (sum == targetSum):
                    return True
                else:
                    return False
            return myFun (root.left, sum) or myFun (root.right, sum)
        return myFun(root, 0)
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        