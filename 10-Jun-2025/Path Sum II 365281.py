# Problem: Path Sum II - https://leetcode.com/problems/path-sum-ii/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        results = []
        potential = []

        if (root is None):
            return []
        def backTrack (root, curSum):
            if (root is None):
                return []
            potential.append(root.val)
            curSum += root.val

            if root.left is None and root.right is None and curSum == targetSum:
                results.append(potential[:])

            backTrack (root.left, curSum)
            backTrack(root.right, curSum)

            potential.pop()
        backTrack (root, 0)
        return results
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        
