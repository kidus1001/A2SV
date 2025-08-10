# Problem: Is Subsequence - https://leetcode.com/problems/is-subsequence/

class Solution(object):
    def isSubsequence(self, s, t):
        j = 0
        theChar = ""
        for i in range (len(t)):
            if j < len(s):
                if t[i] == s[j]:
                    theChar += s[j]
                    j+=1
        if s == theChar:
            return True
        else:
            return False
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        