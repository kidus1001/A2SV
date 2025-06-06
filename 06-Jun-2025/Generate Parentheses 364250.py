# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution(object):
    def generateParenthesis(self, n):
        temp = []
        validResults = []

        def backTrack(open, close):
            if (open == close == n):
                validResults.append ("".join(temp))
                return
            if (close < open):
                temp.append(")")
                backTrack(open, close+1)
                temp.pop()
            if (open < n):
                temp.append("(")
                backTrack(open+1, close)
                temp.pop()
        backTrack(0,0)
        return validResults


        """
        :type n: int
        :rtype: List[str]
        """
        