# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution(object):
    def restoreString(self, s, indices):
        newS = ['']*len(s)
        for i in range(len(indices)):
            newS[indices[i]] = s[i]
        return ("".join(newS))
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        