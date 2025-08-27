# Problem: Step-By-Step Directions From a Binary Tree Node to Another - https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getDirections(self, root, startValue, destValue):
        p_ancestors, q_ancestors = self.getAncestors(root, startValue, destValue)
        common_ancestor_index = -1
        for i in range(min(len(p_ancestors), len(q_ancestors)) - 1, -1, -1):
            if p_ancestors[i] is q_ancestors[i]:
                common_ancestor_index = i
                break
        res = "U" * (len(p_ancestors) - common_ancestor_index - 1)
        if len(q_ancestors) - common_ancestor_index > 1:
            for i in range(common_ancestor_index, len(q_ancestors) - 1):
                res += ("L" if q_ancestors[i].left is q_ancestors[i+1] else "R")
        return res
    
    def getAncestors(self, root, target1, target2):
        stk = []
        t1_ancestors = None
        t2_ancestors = None
        lastVisitedNode = None
        node = root
        while node or stk:
            if not t1_ancestors and node.val ==  target1:
                t1_ancestors = stk[:] if stk else []
                t1_ancestors.append(node)

            if not t2_ancestors and node.val == target2:
                t2_ancestors = stk[:] if stk else []
                t2_ancestors.append(node)
            
            if t1_ancestors and t2_ancestors:
                break

            if node.left and (not lastVisitedNode or (lastVisitedNode is not node.left and lastVisitedNode is not node.right)):
                stk.append(node)
                node = node.left
            elif node.right and (not lastVisitedNode or lastVisitedNode is not node.right):
                stk.append(node)
                node = node.right
            else:
                lastVisitedNode = node
                node = stk.pop() if stk else None
        return t1_ancestors, t2_ancestors
        """
        :type root: Optional[TreeNode]
        :type startValue: int
        :type destValue: int
        :rtype: str
        """
        